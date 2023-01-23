public class Solution {
    public string solution(string s) {
        bool LenCheckFlag = s.Length%2 == 0;
        string answer = s.Substring(LenCheckFlag ? s.Length/2-1 : s.Length/2, LenCheckFlag ? 2:1);
        return answer;
    }
}