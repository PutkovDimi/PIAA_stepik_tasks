# PIAA_stepik_tasks

## Cyclic shift

It's about solution of the [task](https://stepik.org/lesson/81429/step/5?unit=58105)

For run the program, run "main.py". From command line it's as:
`python3 main.py`

For tun tests, run the next command in command line:
`pytest-3 -q --pattern="val" --text="val" --answer="val" tests/test_cyclic_shift.py`

## Knutt_Morris_Pratt

It's about solution of the [task](https://stepik.org/lesson/81429/step/4?unit=58105)

For run the program, run "main.py". From command line it's as:
`python3 main.py`

For tun tests, run the next command in command line(note on whitespaces in answer's parameter):
`pytest-3 -q --pattern="val" --text="val" --answer="[ans1, ans2, ans3]" tests/test_find_substr.py`

## Aho_Korasik

It's about solution of the [task](https://stepik.org/lesson/85333/step/1?unit=61850)

For run the program, run "main.py". From command line it's as:
`python3 main.py`

For tun tests, run the command in command line as on the example below(note on whitespaces in answer's parameter):
`pytest-3 -q --text='your text' --count='count of patterns' --patterns='your patterns' --answer="[(1, 'C'), (2, 'C'), (3, 'C'), (2, 'CCA'), (3, 'CA')]" tests/AK_test.py`

Example of answer was represented for correct input's format.


## Wild_card

It's about solution of the [task](https://stepik.org/lesson/85333/step/2?unit=61850)

For run the program, run "main.py". From command line it's as:
`python3 main.py`

For tun tests, run the command in command line as on the example below(note on whitespaces in answer's parameter):
`pytest -q --text='your text' --wild_card='your wild card' --pattern='your pattern' --answer='your answer' tests/WC_test.py`
