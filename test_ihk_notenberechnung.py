import pytest

testdata_prozente__positive_test = [
    (100, 100, 100),
    (0, 100, 0),
    (0, 6, 0)
]

testdata_prozente__negative_test = [
    (-1, 100, 'ValueError'),
    (0, 5, 'ValueError'),
    (11, 10, 'ValueError'),
    ('text', 100, 'TypeError'),
    (10, 'text', 'TypeError')
]

testdata_note__positive_test = [
    (100, 'sehr gut')
    (92, 'sehr gut')
    (91, 'gut')
    (81, 'gut')
    (80, 'befriedigend')
    (67, 'befriedigend')
    (66, 'ausreichend')
    (50, 'ausreichend')
    (49, 'mangelhaft')
    (30, 'mangelhaft')
    (29, 'ungenügend')
    (0, 'ungenügend')
]

testdata_note__negative_test = [
    (-1, 'ValueError')
    (101, 'ValueError')
    ('text', 'TypeError')
]

@pytest.mark.parametrize('punkte, max_punkte, expected', test_data_prozente__positive_test)
def test_berechne_prozente__positive_test(punkte, max_punkte, expected):
    percentage = berechne_prozente(punkte, max_punkte)
    assert percentage == expected

@pytest.mark.parametrize('punkte, max_punkte, expected', test_data_prozente__negative_test)
def test_berechne_prozente__negative_test(punkte, max_punkte, expected):
    percentage = berechne_prozente(punkte, max_punkte)
    assert percentage == expected

@pytest.mark.parametrize('prozent_werte, expected', test_note__positive_test)
def test_note__positive_test(prozent_werte, expected):
    note = berechne_prozente(prozent_werte)
    assert note == expected

@pytest.mark.parametrize('prozent_werte, expected', test_note__negative_test)
def test_note__positive_test(prozent_werte, expected):
    note = berechne_prozente(prozent_werte)
    assert note == expected