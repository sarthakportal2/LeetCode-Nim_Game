class Solution:
    def canWinNim(self, n: int) -> bool:
        #T(C(N)==O(1)) and S(C(N)=O(1)) as it requires non additional Space in Unit time 
        if n%4==0: return False#printing false to the UNoptimal stone's heeap
        else: return True#Pritning True to FIrst Stone heap
