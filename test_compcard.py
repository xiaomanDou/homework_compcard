import pytest

def compcard(str1):
    Black=str1[7:21]  #将输入字符串中的牌值和花色分别放入BLACK和WHITE
    White=str1[29:34]
    type_Black=judge_type(Black)
    type_White=judge_type(White)
    if type_Black>type_White:
        result='Black wins'
    elif type_Black<type_White:
        result='White wins'
    else:
        result=Judge_Size(type_White,Black,White) #同类牌比较大小
    return result


#将牌面提取出来并转换为int类型

def translate(list):                                      
    list1 = [list[0], list[3], list[6],list[9],list[12]]
    if ('T' in list1):                                    # 将英文字符转换为数字
        list1 = [c.replace('T', '10') for c in list1];
    if ('J' in list1):  
        list1 = [c.replace('J', '11') for c in list1];
    if ('Q' in list1):  
        list1 = [c.replace('Q', '12') for c in list1];
    if ('K' in list1): 
        list1 = [c.replace('K', '13') for c in list1];
    if ('A' in list1):  
        list1 = [c.replace('A', '14') for c in list1];
    list1 = [int(x) for x in list1]
    return list1


def judge_type(player):
    #对牌进行分类判断
    type=1
    list1=translate(player)   

    count=[0]*5   
    for i in range(0,len(list1)):
        count[i]=list1.count(list1[i])
    if count.count(2)==2:
        type=2                                   #是对子的情况还有可能是葫芦
    if count.count(2)==4:
        type=3                                   #两对
    if 3 in count :
        type=4                                   #三条，但还有可能是葫芦
    if 4 in count:
        type=8
        return type                              #铁支
    if (3 in count) & (2 in count):
        type=7
        return type                             #葫芦

    straight = 1                                  #判断是否为顺子
    for index, val in enumerate(list1[:4]):
        j = list1[index + 1]
        if j - val != 1:
            straight = 0
    if straight==1:
        type=5 #是顺子还有可能是同花顺，在这不返回


    if ((player[1] == player[4]) &( player[1] == player[7]) & (player[1] == player[10]) &( player[1] == player[13])): ##判断是否为相同花色
        if straight!=1:
            type = 6  ##同花
        else:
            type = 9  ##同花顺

    return type

def Judge_Size(type,Black,White):
    list_Black=translate(Black)
    list_White=translate(White) 

    count_Black = [0] * 5
    count_White = [0] * 5
    for i in range(0, len(list_Black)):
        count_Black[i] = list_Black.count(list_Black[i])
        count_White[i] = list_White.count(list_White[i]) #计算其中每个字符出现的次数

    if type==1:
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Black_wins=1
        tie=1
        for i in range(0,len(list_White)):
            if list_Black[i]!=list_White[i]:
                tie=0
            if list_Black[i]<list_White[i]:
                Black_wins=0
        if tie==1:
            result='Tie'
        elif Black_wins==1:
            result='Black wins'
        else:
            result='White wins'
        return result

    elif type==2:
        for i in range(0,len(count_Black)):
            if count_Black[i]==2:
                common_Black=list_Black[i]                   #找出对子
        for i in range(0,len(count_White)):
            if count_White[i]==2:
                common_White=list_White[i]
        if common_White>common_Black:
            result='White wins'
        elif common_White<common_Black:
            result='Black wins'
        else:
            list_White.remove(common_White)
            list_Black.remove(common_Black)
            list_Black.sort(reverse=True)
            list_White.sort(reverse=True)
            Tie=1
            Black_wins=1
            for i in range(0,len(list_Black)):
                if list_Black[i]!=list_White[i]:
                    Tie=0
                if list_Black[i]<list_White[i]:
                    Black_wins=0
            if Tie==1:
                result='Tie'
            elif Black_wins==1:
                result='Black wins'
            else:
                result='White wins'
        return result
    elif type==3:
        list_Black=list(set(list_Black))
        list_White=list(set(list_White))
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Tie=1
        Black_wins=1
        for i in range(0,len(list_White)):
            if list_Black[i]!=list_White[i]:
                Tie=0
            if list_Black[i]<list_White[i]:
                Black_wins=0
        if Tie==1:
            result='Tie'
        elif Black_wins==1:
            result='Black wins'
        else:
            result='White wins'
        return result
    elif type==4:
        for i in range(0,len(count_Black)):
            if count_Black[i]==3:
                common_Black=list_Black[i]                  #找出三张同样大小的牌
        for i in range(0,len(count_White)):
            if count_White[i]==3:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==5:
        list_White.sort(reverse=True)
        list_Black.sort(reverse=True)
        if list_Black[0]>list_White[0]:
            result='Black wins'
        elif list_Black[0]<list_White[0]:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==6:
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Black_wins = 1
        tie = 1
        for i in range(0, len(list_White)):
            if list_Black[i] != list_White[i]:
                tie = 0
            if list_Black[i] < list_White[i]:
                Black_wins = 0
        if tie == 1:
            result = 'Tie'
        elif Black_wins == 1:
            result = 'Black wins'
        else:
            result = 'White wins'
        return result
    elif type==7:
        for i in range(0,len(count_Black)):
            if count_Black[i]==3:
                common_Black=list_Black[i]                #找出三张同样大小的牌
        for i in range(0,len(count_White)):
            if count_White[i]==3:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==8:
        for i in range(0,len(count_Black)):
            if count_Black[i]==4:
                common_Black=list_Black[i]                 #找出四张同样大小的牌
        for i in range(0,len(count_White)):
            if count_White[i]==4:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    else:
        list_White.sort(reverse=True)
        list_Black.sort(reverse=True)
        if list_Black[0] > list_White[0]:
            result = 'Black wins'
        elif list_Black[0] < list_White[0]:
            result = 'White wins'
        else:
            result = 'Tie'
        return result




    


#测试部分

#对判断类型的测试

def test_judge_type9():
    assert judge_type('4H 5H 6H 7H 8H')==9

def test_judge_type9():
    assert judge_type('9H TH JH QH KH')==9

def test_judge_type8():
    assert judge_type('3D 3S 3H 3C KH')==8

def test_judge_type7():
    assert judge_type('8D 8S 8H KC KH')==7

def test_judge_type6():
    assert judge_type('2H 3H 7H TH KH')==6

def test_judge_type5():
    assert judge_type('2H 3S 4C 5H 6D')==5

def test_judge_type5():
    assert judge_type('TD JH QH KH AH')==5

def test_judge_type4():
    assert judge_type('TD TS TH KC AH')==4

def test_judge_type3():
    assert judge_type('8D 8H KS KH AH')==3

def test_judge_type2():
    assert judge_type('TD TH QH KH AH')==2    

def test_judge_type1():
    assert judge_type('2D 4D 6H TS JD')==1



#当两副牌面类型不同时的测试

def test_different_whitewins():
    input='Black: 2H 3D 7S 8C TH White: 3H 4H 5H 6H 7H'
    assert poker(input)=='White wins'

def test_different_blackwins():
    input='Black: 2H 3D 4S 5C 6D White: 2C 3H 4S 8C KH'
    assert poker(input)=='Black wins'


#当牌面相同时，比较大小的测试

def test_same_type1_BlackWins():
    assert Judge_Size(1,'2H 3D 5S 9C KD','2C 3H 4S 8C KH')=='Black wins'

def test_same_type1_WhiteWins():
    assert Judge_Size(1,'2C 3H 4S 8C KH','2H 3D 5S 9C KD')=='White wins'

def test_same_type1_Tie():
    assert Judge_Size(1,'2H 3D 5S 9C KD','2D 3H 5C 9S KH')=='Tie'

def test_same_type2_BlackWins():
    assert Judge_Size(2,'2H 4D 5S 9C 9D','2D 3H 3C 9S KH')=='Black wins'

def test_same_type2_Whitewins():
    assert Judge_Size(2,'2H 2D 5S 9C KD','2D 3H 3C 9S KH')=='White wins'

def test_same_type2_Tie():
    assert Judge_Size(2,'2H 3D 5S 9C 9D','2D 3H 5C 9S 9H')=='Tie'

def test_same_type3_BlackWins():
    assert Judge_Size(3,'2H 2D 5S TC TD','2D 2H 5C 9S 9H')=='Black wins'

def test_same_type4_BlackWins():
    assert Judge_Size(4,'5H 5D 5S TC AD','2D 2H 2C TS QH')=='Black wins'

def test_same_type5_BlackWins():
    assert Judge_Size(5,'4H 5D 6S 7C 8D','3D 4H 5C 6S 7H')=='Black wins'

def test_same_type5_Tie():
    assert Judge_Size(5,'4H 5D 6S 7C 8D','4D 5H 6C 7S 8H')=='Tie'

def test_same_type6_BlackWins():
    assert Judge_Size(6,'4H 5H 6H 8H JH','3D 4D 7D 8D 9D')=='Black wins'

def test_same_type7_WhiteWins():
    assert Judge_Size(6,'4H 4D 4S 8H JH','2D 5D 5S 5C KH')=='White wins'

def test_same_type8_BlackWins():
    assert Judge_Size(8,'4H 4D 4S 4C 8D','2D 2H 2C 2S 4H')=='Black wins'

def test_same_type9_BlackWins():
    assert Judge_Size(9,'4H 5H 6H 7H 8H','2D 3D 4D 5D 6D')=='Black wins'

def test_same_type9_Tie():
    assert Judge_Size(9,'5H 6H 7H 8H 9H','5D 6D 7D 8D 9D')=='Tie'

    
#compcard函数测试

def test_main_BlackWins():
    assert compcard('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S')=='Black wins'

def test_main_WhiteWins():
    assert compcard('Black: 2D 4C 5S 8H JD White: 2C 4S 5H 9C AH')=='White wins'

def test_main_Tie():
    assert compcard('Black: 2H 3D 6S JC KD White: 2D 3H 6C JS KC') == 'Tie'

#测试结束

if __name__ =="__main__":
    pytest.main()
