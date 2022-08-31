from datetime import datetime, timedelta

import pytest

from wodpy import wodnc
from testData import sample_data


@pytest.fixture
def profile():
    """Sample profile

    example from pp 124 of http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    with IQuOD flags
    """
    profile = wodnc.Ragged(sample_data("ocldb1570984477.6279_OSD.nc"))
    return wodnc.Profile(profile, 55)


def test_latitude(profile):
    """
    check latitude == 61.93
    """

    latitude = profile.latitude()
    assert round(latitude, 2) == 61.93, (
        "latitude should have been approx 61.93, instead read %f" % latitude
    )


def test_longitude(profile):
    """
    check latitude == -172.270
    """

    longitude = profile.longitude()
    assert round(longitude, 2) == -172.270, (
        "longitude should have been approx -172.270, instead read %f" % latitude
    )


def test_uid(profile):
    """
    check profile ID == 67064
    """

    uid = profile.uid()
    assert uid == 67064, "uid should have been 67064, instead read %f" % uid


def test_n_levels(profile):
    """
    check the number of levels == 4
    """

    levels = profile.n_levels()
    assert levels == 4, "levels should have been 4, instead read %f" % levels


def test_year(profile):
    """
    check year == 1934
    """

    year = profile.year()
    assert year == 1934, "year should have been 1934, instead read %f" % year


def test_month(profile):
    """
    check month == 8
    """

    month = profile.month()
    assert month == 8, "month should have been 8, instead read %f" % month


def test_day(profile):
    """
    check day == 7
    """

    day = profile.day()
    assert day == 7, "day should have been 7, instead read %f" % day


def test_time(profile):
    """
    check time == 10.37
    """

    time = profile.time()
    assert round(time, 2) == 10.37, (
        "time should have been 10.37, instead read %f" % time
    )


def test_datetime(profile):
    """
    check datetime is close to 1934-8-7 10:22:12
    allow a 36 second (== 0.01 hour) deviation for round off error in the time
    """

    d = profile.datetime()
    assert (
        timedelta(seconds=-18)
        < (d - datetime(1934, 8, 7, 10, 22, 12))
        < timedelta(seconds=18)
    ), ("time should have been close to 1934-08-07 10:22:12, instead read %s" % d)


def test_probe_type(profile):
    """
    check probe type == 7
    """

    probe = profile.probe_type()
    assert probe == 7, "probe should have been 7, instead read %f" % probe


def test_depth(profile):
    """
    check depths == [0.0, 10.0, 25.0, 50.0]
    """

    truth = [0.0, 10.0, 25.0, 50.0]
    truth = [numpy.float32(t) for t in truth]
    z = profile.z()
    assert numpy.array_equal(z, truth), (
        "depths should have been [0, 10, 25, 50], instead read %s" % z.__str__()
    )


def test_temperature(profile):
    """
    check temperatures == [8.960, 8.950, 0.900, -1.230]
    """

    truth = [8.960, 8.950, 0.900, -1.230]
    truth = [numpy.float32(t) for t in truth]
    t = profile.t()
    assert numpy.array_equal(t, truth), (
        "temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s"
        % t.__str__()
    )


def test_salinity(profile):
    """
    check salinities == [30.900, 30.900, 31.910, 32.410]
    """

    truth = [30.900, 30.900, 31.910, 32.410]
    truth = [numpy.float32(t) for t in truth]
    s = profile.s()
    assert numpy.array_equal(s, truth), (
        "salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s"
        % s.__str__()
    )
