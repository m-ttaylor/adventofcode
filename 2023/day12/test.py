from solution import countContig


def test_countContig_a():
    spring = "#.#.##"
    assert countContig(spring) == [1, 1, 2]


def test_countContig_b():
    spring = "###.#.####"
    assert countContig(spring) == [3, 1, 4]


def test_countContig_c():
    spring = "."
    assert countContig(spring) == [0]


def test_countContig_d():
    spring = "#####.###.#.##.###.##"
    assert countContig(spring) == [5, 3, 1, 2, 3, 2]


def test_countContig_e():
    spring = "#?.##.###"
    assert countContig(spring) == [1, 2, 3]
