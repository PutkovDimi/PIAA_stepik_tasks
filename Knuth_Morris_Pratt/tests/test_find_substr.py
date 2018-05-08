from ..src.find_substr_in_str import process_answer as kmp


#    kmp('a', 'bbb')== -1
#    kmp('ab', 'abababababababab')== '0,2,4,6,8,10,12,14'
#    kmp(' ', 'alkcskvlskvlsv')== -1
#    kmp('s', '') == -1
#    kmp('', 'aaa') == '1,2,3'

def test_valid_string(pattern, answer, text):
    assert str(answer) == str(kmp(pattern=pattern,
                         text=text))
