def reverseParentheses(s):
    """
    You have a string s that consists of English letters, punctuation marks, 
    whitespace characters, and brackets. It is guaranteed that the parentheses 
    in s form a regular bracket sequence.

    Your task is to reverse the strings contained in each pair of matching parentheses, 
    starting from the innermost pair. The results string should not contain any parentheses.

    For string s = "a(bc)de", the output should be reverseParentheses(s) = "acbde".
    """

    # test
    # a(bcdefghijkl(mno)p)q - apmnolkjihgfedcbq
    # co(de(fight)s) - cosfighted
    # Code(Cha(lle)nge) - CodeegnlleahC
    # Where are the parentheses? - Where are the parentheses?
    # abc(cba)ab(bac)c - abcabcabcabc
    # The ((quick (brown) (fox) jumps over the lazy) dog) - The god quick nworb xof jumps over the lazy