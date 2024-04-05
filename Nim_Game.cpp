class Solution {
public:
    bool canWinNim(int n) {
     //T(C(N)=O(1)) and S(C(N)=O(1)) as it requires not addiitonal space with in unit Time        
        if (n%4==0)return false;//Printing False to the stone heap last
        else return true;}};//Printing False to the First stone heap 
