import pytest
import polar as pol


def test_polarFunction():
    vrPolar = pol.polarFunction("polar.pol")

    # Test for values given in the polar file
    assert float(vrPolar(30, 2)) == pytest.approx(0.993, abs=0.001)
    assert float(vrPolar(90, 10)) == pytest.approx(11.585, abs=0.001)

    # Test for values not given by the file
    assert float(vrPolar(50, 11.2)) == pytest.approx(10.7, abs=0.1)

    # Test for extreme values
    assert float(vrPolar(0, 13)) == pytest.approx(0)
    assert float(vrPolar(20, 8)) == pytest.approx(2)


if __name__ == "__main__":
    pytest.main(["test.py"])
