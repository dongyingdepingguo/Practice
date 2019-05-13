# !/usr/bin/env python

# _*_ coding: utf-8 _*_

def get_C1(Data):
    '''
    生成候选1项集
    :param Data:
    :return: 获取候选频繁1项集
    '''

    C1 = []
    for items in Data:
        for item in items:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
    return [frozenset(c1) for c1 in C1]

def Scan_Data(Dataset, Ck, minSupport):
    '''
    扫描整个数据集，生成候选频繁k项集每一项的支持度计数，并对候选项集剪枝，
    生成频繁k项集，最终返回频繁k项集及频繁k项集的支持度
    :param Data:
    :param Ck: 候选频繁k项集
    :param minSupport: 最小支持度
    :return: 返回频繁项集及频繁项集的支持度
    '''
    num_items = {}
    for items in Dataset:
        for item in Ck:
            if item.issubset(items):
                if item not in num_items:
                    num_items[item] = 1
                else:
                    num_items[item] += 1

    all_items = len(Dataset)
    fre_items = []
    support_items = {}
    for item in num_items:
        support = num_items[item] / all_items
        if support >= minSupport:
            fre_items.insert(0, item)
            support_items[item] = support
    return fre_items, support_items

def get_Ck(Lk_1, k):
    '''
    由频繁(k-1)项集生成候选频繁k项集
    :param Lk_1: 频繁k-1项集
    :param k:
    :return: 返回候选频繁k项集
    '''
    Ck = []
    Len_Lk_1 = len(Lk_1)
    for i in range(Len_Lk_1):
        for j in range(i+1, Len_Lk_1):
            L1 = list(Lk_1[i])[:k-2]
            L2 = list(Lk_1[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                Ck.append(Lk_1[i] | Lk_1[j])
    return Ck

def apriori(Data, minSupport):
    '''
    得到所有的频繁项集，及其支持度
    :param Data:
    :param minSupport:
    :return: 返回频繁项集及支持度
    '''
    C1 = get_C1(Data)
    Dataset = [set(items) for items in Data]
    L1, Support_items = Scan_Data(Dataset, C1, minSupport)
    L_all = [L1]
    k = 2
    while len(L_all[k-2]) > 0:
        Ck = get_Ck(L_all[k-2], k)
        Lk, Lk_support_items = Scan_Data(Dataset, Ck, minSupport)
        L_all.append(Lk)
        Support_items.update(Lk_support_items)
        k += 1
    return L_all, Support_items

def calculation_conf(fre_item, H, support_items, brl, minconf):
    '''
    该函数输出关联规则
    :param fre_item: 频繁项集中的一个频繁项
    :param H: 频繁项中每个元素组成的子集列表
    :param support_items: 支持度集
    :param brl: 关联规则列表
    :param minconf: 最小置信度
    :return:
    '''

    for conseq in H:
        conf = support_items[fre_item] / support_items[fre_item - conseq]
        if conf >= minconf:
            print(list(fre_item - conseq), '---->', list(conseq),
                  '置信度：%0.3f'%conf,
                  '支持度：%0.3f'%support_items[fre_item])
            brl.append((fre_item, conseq, conf))
    return None

def rulesFromCons(fre_item, H, support_items, brl, minconf):
    '''
    增加H中子集的项数，输出关联规则
    :param fre_items:
    :param H:
    :param support_items:
    :param brl:
    :param minconf:
    :return:
    '''

    m = len(H[0])
    while len(fre_item) > m:
        calculation_conf(fre_item, H, support_items, brl, minconf)
        H = get_Ck(H, m+1)
        m = len(H[0])

def GenerateRule(L, support_items, minconf = 0.7):
    '''
    产生所有频繁项集的关联规则
    :param L: 所有频繁项集列表
    :param support_items: 频繁项集的支持度字典
    :param minconf: 最小置信度
    :return: 所有符合条件的关联规则列表
    '''

    BigRuleList = []
    for i in range(1, len(L)):
        for fre_item in L[i]:
            H1 = [ frozenset([item]) for item in fre_item]
            if i > 1:
                rulesFromCons(fre_item, H1, support_items, BigRuleList, minconf)
            else:
                calculation_conf(fre_item, H1, support_items, BigRuleList, minconf)
    return BigRuleList

if __name__ == '__main__':
    mydata = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
               ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
               ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    L, support_items = apriori(mydata, 0.2)
    rules = GenerateRule(L, support_items, minconf=0.75)
