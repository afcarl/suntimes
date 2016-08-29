import datetime
import math


def truncate(m):
    return float(int(m))


def sign(m):
    if m > 0:
        return 1
    return -1


def sin(x):
    return math.degrees(math.sin(math.radians(x)))


def arcsine(x):
    return math.degrees(math.asin(math.radians(x)))


def arccos(x):
    return math.degrees(math.acos(math.radians(x)))


def cos(x):
    return math.degrees(math.cos(math.radians(x)))


def calculateSunrise():
    # http://williams.best.vwh.net/sunrise_sunset_algorithm.htm
    lw = 80.85  # longitude west
    phi = 37.72
    Jdate = calculateJulianDate()
    print(Jdate)
    n = Jdate - 2451545.0 + 0.0008
    print(n)
    Jstar = lw / 360 + n
    print(Jstar)
    M = (357.5291 + 0.98560028 * Jstar) % 360
    C = 1.9148 * sin(M) + 0.02 * sin(2 * M) + \
        0.0003 * sin(3 * M)
    lmbda = (M + C + 180 + 102.9372) % 360
    Jtransit = Jstar + 0.0053 * sin(M) - 0.0069 * sin(2 * lmbda)
    print(Jtransit)
    delta = arcsine(math.degrees(math.radians(
        sin(lmbda)) * math.radians(sin(23.44))))
    wnot = arccos((sin(-0.83) - math.degrees(math.radians(sin(phi)) * math.radians(sin(delta)))) /
                  math.degrees(math.radians(cos(phi)) * math.radians(cos(delta))))
    print(wnot)
    print(Jtransit + wnot / 360)


def calculateJulianDate():
    # Introduction:
    # The Julian date (JD) is a continuous count of days from 1 January 4713 BC (= -4712 January 1),
    # Greenwich mean noon (= 12h UT). For example, AD 1978 January 1, 0h UT is JD 2443509.5 and AD 1978 July 21, 15h UT, is JD 2443711.125.
    #
    # Formula for Conversion:
    # Conversion of Gregorian calendar date to Julian date for years AD 1801–2099 can be carried out with the following formula:
    #
    # JD =	367K - <(7(K+<(M+9)/12>))/4> + <(275M)/9> + I + 1721013.5 + UT/24
    # - 0.5sign(100K+M-190002.5) + 0.5
    # where K is the year (1801 <= K <= 2099), M is the month (1 <= M <= 12), I is the day of the month (1 <= I <= 31),
    # and UT is the universal time in hours ("<=" means "less than or equal to"). The last two terms in the formula add up
    # to zero for all dates after 1900 February 28, so these two terms can be omitted for subsequent dates.
    # This formula makes use of the sign and truncation functions described below:
    #
    # The sign function serves to extract the algebraic sign from a number.
    # Examples: sign(247) = 1; sign(-6.28) = -1.
    #
    # The truncation function < > extracts the integral part of a number.
    # Examples: <17.835> = 17; <-3.14> = -3.
    #
    # The formula given above was taken from the 1990 edition of the U.S. Naval Observatory's Almanac for Computers (discontinued).
    #
    # Example: Compute the JD corresponding to 1877 August 11, 7h30m UT.
    # Substituting K = 1877, M = 8, I = 11 and UT = 7.5,
    # JD = 688859 - 3286 + 244 + 11 + 1721013.5 + 0.3125 + 0.5 + 0.5
    # = 2406842.8125
    today = datetime.datetime.today()
    K = today.year
    M = today.month
    I = today.day
    UT = today.hour + today.minute / 60.0 + today.second / 60.0 / 60.0
    JD = 367.0 * K - truncate(7.0 * (K + truncate((M + 9.0) / 12.0)) / 4) + \
        truncate(275.0 * M / 9.0) + I + 1721013.5 + \
        UT / 24 - 0.5 * sign(100 * K + M - 190002.5) + 0.5
    return JD


calculateSunrise()
