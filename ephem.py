# There is a package called pyephem which has this interface.
# But it's a pain to install (requires special wheels or python-dev
# headers to build C content). So let's just fake it out to make
# installation a lot easier.
# To generate the dates values, install pyephem and run the following:
"""
import ephem

years = range(1900, 2030)

def dd(y):
    print('({}, {}, {}, {}),'.format(repr(ephem.next_spring_equinox(y).datetime()),
                                     repr(ephem.next_summer_solstice(y).datetime()),
                                     repr(ephem.next_autumn_equinox(y).datetime()),
                                     repr(ephem.next_winter_solstice(y).datetime())
                                    )
    )

for y in years:
    dd(str(y))
"""

import datetime


class Date:
    def __init__(self, dt):
        """Some kind of custom date class, but it has a .datetime() method
        """
        self.dt = dt

    def datetime(self):
        return self.dt


dates = [
    # next_spring_equinox, next_summer_solstice, next_autumn_equinox, next_winter_solstice
(datetime.datetime(1900, 3, 21, 1, 39, 7, 976095), datetime.datetime(1900, 6, 21, 21, 40, 2, 348619), datetime.datetime(1900, 9, 23, 12, 20, 24, 281446), datetime.datetime(1900, 12, 22, 6, 41, 31, 826147)),
(datetime.datetime(1901, 3, 21, 7, 23, 46, 930161), datetime.datetime(1901, 6, 22, 3, 28, 2, 293623), datetime.datetime(1901, 9, 23, 18, 9, 0, 68192), datetime.datetime(1901, 12, 22, 12, 36, 32, 810161)),
(datetime.datetime(1902, 3, 21, 13, 16, 32, 865200), datetime.datetime(1902, 6, 22, 9, 15, 22, 571542), datetime.datetime(1902, 9, 23, 23, 55, 29, 891868), datetime.datetime(1902, 12, 22, 18, 35, 29, 71976)),
(datetime.datetime(1903, 3, 21, 19, 14, 54, 385729), datetime.datetime(1903, 6, 22, 15, 5, 9, 784173), datetime.datetime(1903, 9, 24, 5, 43, 39, 843508), datetime.datetime(1903, 12, 23, 0, 20, 21, 733463)),
(datetime.datetime(1904, 3, 21, 0, 58, 27, 950825), datetime.datetime(1904, 6, 21, 20, 51, 35, 470958), datetime.datetime(1904, 9, 23, 11, 40, 15, 656063), datetime.datetime(1904, 12, 22, 6, 13, 53, 50516)),
(datetime.datetime(1905, 3, 21, 6, 57, 34, 772533), datetime.datetime(1905, 6, 22, 2, 51, 35, 934075), datetime.datetime(1905, 9, 23, 17, 30, 8, 772049), datetime.datetime(1905, 12, 22, 12, 3, 37, 316971)),
(datetime.datetime(1906, 3, 21, 12, 52, 54, 915325), datetime.datetime(1906, 6, 22, 8, 42, 2, 761109), datetime.datetime(1906, 9, 23, 23, 15, 3, 859792), datetime.datetime(1906, 12, 22, 17, 53, 12, 682750)),
(datetime.datetime(1907, 3, 21, 18, 33, 3, 893290), datetime.datetime(1907, 6, 22, 14, 23, 14, 749149), datetime.datetime(1907, 9, 24, 5, 9, 9, 559758), datetime.datetime(1907, 12, 22, 23, 51, 27, 997587)),
(datetime.datetime(1908, 3, 21, 0, 27, 26, 473915), datetime.datetime(1908, 6, 21, 20, 19, 17, 202068), datetime.datetime(1908, 9, 23, 10, 58, 15, 731073), datetime.datetime(1908, 12, 22, 5, 33, 21, 661313)),
(datetime.datetime(1909, 3, 21, 6, 12, 55, 42459), datetime.datetime(1909, 6, 22, 2, 5, 47, 516413), datetime.datetime(1909, 9, 23, 16, 44, 40, 780755), datetime.datetime(1909, 12, 22, 11, 19, 44, 650244)),
(datetime.datetime(1910, 3, 21, 12, 3, 0, 173602), datetime.datetime(1910, 6, 22, 7, 48, 56, 292030), datetime.datetime(1910, 9, 23, 22, 30, 47, 420859), datetime.datetime(1910, 12, 22, 17, 11, 40, 875459)),
(datetime.datetime(1911, 3, 21, 17, 54, 20, 2239), datetime.datetime(1911, 6, 22, 13, 35, 45, 638687), datetime.datetime(1911, 9, 24, 4, 17, 33, 812219), datetime.datetime(1911, 12, 22, 22, 53, 7, 808014)),
(datetime.datetime(1912, 3, 20, 23, 29, 22, 36174), datetime.datetime(1912, 6, 21, 19, 17, 7, 436990), datetime.datetime(1912, 9, 23, 10, 8, 13, 157304), datetime.datetime(1912, 12, 22, 4, 44, 37, 389790)),
(datetime.datetime(1913, 3, 21, 5, 18, 2, 329948), datetime.datetime(1913, 6, 22, 1, 9, 41, 914500), datetime.datetime(1913, 9, 23, 15, 52, 46, 790460), datetime.datetime(1913, 12, 22, 10, 34, 47, 954479)),
(datetime.datetime(1914, 3, 21, 11, 10, 42, 253636), datetime.datetime(1914, 6, 22, 6, 55, 16, 192096), datetime.datetime(1914, 9, 23, 21, 33, 59, 940980), datetime.datetime(1914, 12, 22, 16, 22, 18, 856331)),
(datetime.datetime(1915, 3, 21, 16, 51, 25, 150242), datetime.datetime(1915, 6, 22, 12, 29, 35, 856874), datetime.datetime(1915, 9, 24, 3, 23, 49, 330401), datetime.datetime(1915, 12, 22, 22, 15, 41, 27563)),
(datetime.datetime(1916, 3, 20, 22, 46, 49, 833701), datetime.datetime(1916, 6, 21, 18, 24, 38, 329188), datetime.datetime(1916, 9, 23, 9, 14, 49, 26318), datetime.datetime(1916, 12, 22, 3, 58, 27, 554508)),
(datetime.datetime(1917, 3, 21, 4, 37, 20, 994265), datetime.datetime(1917, 6, 22, 0, 14, 33, 103004), datetime.datetime(1917, 9, 23, 15, 0, 17, 859868), datetime.datetime(1917, 12, 22, 9, 45, 33, 731303)),
(datetime.datetime(1918, 3, 21, 10, 25, 36, 704352), datetime.datetime(1918, 6, 22, 5, 59, 50, 525137), datetime.datetime(1918, 9, 23, 20, 45, 40, 282595), datetime.datetime(1918, 12, 22, 15, 41, 24, 712278)),
(datetime.datetime(1919, 3, 21, 16, 19, 8, 414803), datetime.datetime(1919, 6, 22, 11, 53, 47, 532627), datetime.datetime(1919, 9, 24, 2, 35, 28, 910904), datetime.datetime(1919, 12, 22, 21, 26, 58, 964999)),
(datetime.datetime(1920, 3, 20, 21, 59, 19, 512460), datetime.datetime(1920, 6, 21, 17, 40, 1, 741640), datetime.datetime(1920, 9, 23, 8, 28, 3, 965044), datetime.datetime(1920, 12, 22, 3, 16, 53, 664427)),
(datetime.datetime(1921, 3, 21, 3, 50, 54, 119872), datetime.datetime(1921, 6, 21, 23, 35, 50, 622979), datetime.datetime(1921, 9, 23, 14, 19, 51, 518405), datetime.datetime(1921, 12, 22, 9, 7, 20, 925870)),
(datetime.datetime(1922, 3, 21, 9, 48, 42, 183038), datetime.datetime(1922, 6, 22, 5, 26, 55, 565051), datetime.datetime(1922, 9, 23, 20, 9, 34, 431521), datetime.datetime(1922, 12, 22, 14, 56, 48, 35675)),
(datetime.datetime(1923, 3, 21, 15, 28, 40, 468289), datetime.datetime(1923, 6, 22, 11, 2, 57, 849674), datetime.datetime(1923, 9, 24, 2, 3, 39, 780387), datetime.datetime(1923, 12, 22, 20, 53, 8, 618835)),
(datetime.datetime(1924, 3, 20, 21, 20, 13, 673213), datetime.datetime(1924, 6, 21, 16, 59, 34, 120167), datetime.datetime(1924, 9, 23, 7, 58, 26, 14057), datetime.datetime(1924, 12, 22, 2, 45, 19, 166245)),
(datetime.datetime(1925, 3, 21, 3, 12, 11, 807413), datetime.datetime(1925, 6, 21, 22, 50, 10, 291437), datetime.datetime(1925, 9, 23, 13, 43, 24, 353163), datetime.datetime(1925, 12, 22, 8, 36, 31, 520742)),
(datetime.datetime(1926, 3, 21, 9, 1, 5, 363896), datetime.datetime(1926, 6, 22, 4, 30, 11, 763566), datetime.datetime(1926, 9, 23, 19, 26, 42, 59872), datetime.datetime(1926, 12, 22, 14, 33, 13, 762969)),
(datetime.datetime(1927, 3, 21, 14, 59, 7, 708158), datetime.datetime(1927, 6, 22, 10, 22, 20, 699384), datetime.datetime(1927, 9, 24, 1, 16, 47, 854008), datetime.datetime(1927, 12, 22, 20, 18, 20, 506453)),
(datetime.datetime(1928, 3, 20, 20, 44, 5, 466361), datetime.datetime(1928, 6, 21, 16, 6, 36, 434860), datetime.datetime(1928, 9, 23, 7, 5, 34, 216429), datetime.datetime(1928, 12, 22, 2, 3, 33, 17997)),
(datetime.datetime(1929, 3, 21, 2, 34, 53, 948736), datetime.datetime(1929, 6, 21, 22, 0, 48, 905207), datetime.datetime(1929, 9, 23, 12, 52, 20, 272078), datetime.datetime(1929, 12, 22, 7, 52, 36, 728379)),
(datetime.datetime(1930, 3, 21, 8, 29, 42, 704137), datetime.datetime(1930, 6, 22, 3, 53, 1, 398976), datetime.datetime(1930, 9, 23, 18, 36, 2, 186213), datetime.datetime(1930, 12, 22, 13, 39, 24, 633133)),
(datetime.datetime(1931, 3, 21, 14, 6, 21, 816737), datetime.datetime(1931, 6, 22, 9, 28, 14, 91207), datetime.datetime(1931, 9, 24, 0, 23, 29, 911865), datetime.datetime(1931, 12, 22, 19, 29, 26, 801515)),
(datetime.datetime(1932, 3, 20, 19, 53, 39, 356632), datetime.datetime(1932, 6, 21, 15, 22, 47, 606261), datetime.datetime(1932, 9, 23, 6, 15, 50, 412187), datetime.datetime(1932, 12, 22, 1, 14, 8, 359653)),
(datetime.datetime(1933, 3, 21, 1, 43, 0, 519748), datetime.datetime(1933, 6, 21, 21, 11, 58, 168031), datetime.datetime(1933, 9, 23, 12, 1, 17, 376567), datetime.datetime(1933, 12, 22, 6, 57, 23, 149965)),
(datetime.datetime(1934, 3, 21, 7, 27, 57, 347639), datetime.datetime(1934, 6, 22, 2, 48, 4, 549932), datetime.datetime(1934, 9, 23, 17, 45, 6, 720560), datetime.datetime(1934, 12, 22, 12, 49, 17, 776477)),
(datetime.datetime(1935, 3, 21, 13, 17, 36, 427442), datetime.datetime(1935, 6, 22, 8, 38, 4, 280989), datetime.datetime(1935, 9, 23, 23, 38, 12, 790490), datetime.datetime(1935, 12, 22, 18, 36, 58, 402852)),
(datetime.datetime(1936, 3, 20, 18, 57, 52, 90986), datetime.datetime(1936, 6, 21, 14, 21, 47, 357218), datetime.datetime(1936, 9, 23, 5, 26, 2, 174434), datetime.datetime(1936, 12, 22, 0, 26, 32, 921931)),
(datetime.datetime(1937, 3, 21, 0, 44, 58, 132775), datetime.datetime(1937, 6, 21, 20, 12, 10, 915064), datetime.datetime(1937, 9, 23, 11, 12, 56, 127565), datetime.datetime(1937, 12, 22, 6, 21, 33, 84979)),
(datetime.datetime(1938, 3, 21, 6, 43, 3, 410616), datetime.datetime(1938, 6, 22, 2, 3, 46, 69016), datetime.datetime(1938, 9, 23, 16, 59, 38, 367341), datetime.datetime(1938, 12, 22, 12, 13, 17, 718330)),
(datetime.datetime(1939, 3, 21, 12, 28, 31, 326575), datetime.datetime(1939, 6, 22, 7, 39, 34, 574443), datetime.datetime(1939, 9, 23, 22, 49, 24, 22222), datetime.datetime(1939, 12, 22, 18, 5, 51, 39943)),
(datetime.datetime(1940, 3, 20, 18, 23, 40, 77051), datetime.datetime(1940, 6, 21, 13, 36, 35, 470321), datetime.datetime(1940, 9, 23, 4, 45, 42, 389328), datetime.datetime(1940, 12, 21, 23, 54, 39, 200428)),
(datetime.datetime(1941, 3, 21, 0, 20, 29, 916233), datetime.datetime(1941, 6, 21, 19, 33, 28, 520626), datetime.datetime(1941, 9, 23, 10, 32, 47, 531146), datetime.datetime(1941, 12, 22, 5, 44, 2, 778104)),
(datetime.datetime(1942, 3, 21, 6, 10, 32, 276962), datetime.datetime(1942, 6, 22, 1, 16, 24, 928283), datetime.datetime(1942, 9, 23, 16, 16, 33, 202039), datetime.datetime(1942, 12, 22, 11, 39, 26, 888120)),
(datetime.datetime(1943, 3, 21, 12, 2, 40, 711718), datetime.datetime(1943, 6, 22, 7, 12, 28, 155931), datetime.datetime(1943, 9, 23, 22, 11, 48, 440771), datetime.datetime(1943, 12, 22, 17, 28, 59, 397483)),
(datetime.datetime(1944, 3, 20, 17, 48, 32, 126770), datetime.datetime(1944, 6, 21, 13, 2, 28, 851947), datetime.datetime(1944, 9, 23, 4, 1, 34, 433879), datetime.datetime(1944, 12, 21, 23, 14, 42, 168798)),
(datetime.datetime(1945, 3, 20, 23, 37, 5, 820175), datetime.datetime(1945, 6, 21, 18, 52, 14, 33515), datetime.datetime(1945, 9, 23, 9, 49, 53, 803814), datetime.datetime(1945, 12, 22, 5, 3, 27, 487739)),
(datetime.datetime(1946, 3, 21, 5, 32, 43, 289040), datetime.datetime(1946, 6, 22, 0, 44, 30, 737566), datetime.datetime(1946, 9, 23, 15, 40, 34, 695785), datetime.datetime(1946, 12, 22, 10, 53, 12, 312824)),
(datetime.datetime(1947, 3, 21, 11, 12, 35, 641184), datetime.datetime(1947, 6, 22, 6, 18, 59, 287966), datetime.datetime(1947, 9, 23, 21, 28, 47, 327595), datetime.datetime(1947, 12, 22, 16, 42, 38, 963920)),
(datetime.datetime(1948, 3, 20, 16, 56, 55, 898232), datetime.datetime(1948, 6, 21, 12, 10, 44, 958179), datetime.datetime(1948, 9, 23, 3, 21, 44, 103992), datetime.datetime(1948, 12, 21, 22, 33, 8, 370601)),
(datetime.datetime(1949, 3, 20, 22, 47, 59, 326256), datetime.datetime(1949, 6, 21, 18, 2, 55, 942158), datetime.datetime(1949, 9, 23, 9, 5, 53, 207670), datetime.datetime(1949, 12, 22, 4, 22, 45, 620690)),
(datetime.datetime(1950, 3, 21, 4, 35, 8, 928168), datetime.datetime(1950, 6, 21, 23, 36, 11, 684314), datetime.datetime(1950, 9, 23, 14, 43, 37, 584877), datetime.datetime(1950, 12, 22, 10, 13, 12, 950229)),
(datetime.datetime(1951, 3, 21, 10, 25, 41, 381532), datetime.datetime(1951, 6, 22, 5, 24, 59, 723070), datetime.datetime(1951, 9, 23, 20, 36, 41, 986526), datetime.datetime(1951, 12, 22, 15, 59, 56, 778226)),
(datetime.datetime(1952, 3, 20, 16, 13, 35, 71141), datetime.datetime(1952, 6, 21, 11, 12, 42, 661684), datetime.datetime(1952, 9, 23, 2, 23, 46, 498445), datetime.datetime(1952, 12, 21, 21, 43, 2, 422571)),
(datetime.datetime(1953, 3, 20, 22, 0, 32, 217127), datetime.datetime(1953, 6, 21, 17, 0, 6, 638447), datetime.datetime(1953, 9, 23, 8, 5, 51, 369853), datetime.datetime(1953, 12, 22, 3, 31, 19, 988440)),
(datetime.datetime(1954, 3, 21, 3, 53, 19, 704298), datetime.datetime(1954, 6, 21, 22, 54, 13, 874491), datetime.datetime(1954, 9, 23, 13, 55, 23, 797381), datetime.datetime(1954, 12, 22, 9, 24, 13, 388727)),
(datetime.datetime(1955, 3, 21, 9, 35, 12, 325554), datetime.datetime(1955, 6, 22, 4, 31, 32, 689608), datetime.datetime(1955, 9, 23, 19, 40, 57, 694471), datetime.datetime(1955, 12, 22, 15, 10, 46, 545856)),
(datetime.datetime(1956, 3, 20, 15, 20, 16, 240647), datetime.datetime(1956, 6, 21, 10, 23, 56, 181880), datetime.datetime(1956, 9, 23, 1, 35, 3, 597842), datetime.datetime(1956, 12, 21, 20, 59, 22, 318651)),
(datetime.datetime(1957, 3, 20, 21, 16, 29, 561430), datetime.datetime(1957, 6, 21, 16, 20, 42, 218611), datetime.datetime(1957, 9, 23, 7, 26, 11, 980027), datetime.datetime(1957, 12, 22, 2, 48, 30, 876594)),
(datetime.datetime(1958, 3, 21, 3, 5, 48, 203197), datetime.datetime(1958, 6, 21, 21, 57, 3, 550154), datetime.datetime(1958, 9, 23, 13, 8, 45, 526585), datetime.datetime(1958, 12, 22, 8, 39, 36, 285449)),
(datetime.datetime(1959, 3, 21, 8, 54, 24, 727168), datetime.datetime(1959, 6, 22, 3, 49, 55, 970793), datetime.datetime(1959, 9, 23, 19, 8, 33, 627616), datetime.datetime(1959, 12, 22, 14, 34, 13, 514605)),
(datetime.datetime(1960, 3, 20, 14, 42, 44, 756701), datetime.datetime(1960, 6, 21, 9, 42, 25, 922658), datetime.datetime(1960, 9, 23, 0, 58, 50, 930763), datetime.datetime(1960, 12, 21, 20, 25, 48, 416421)),
(datetime.datetime(1961, 3, 20, 20, 31, 59, 231579), datetime.datetime(1961, 6, 21, 15, 30, 15, 957633), datetime.datetime(1961, 9, 23, 6, 42, 30, 288462), datetime.datetime(1961, 12, 22, 2, 19, 20, 533394)),
(datetime.datetime(1962, 3, 21, 2, 29, 35, 996393), datetime.datetime(1962, 6, 21, 21, 24, 15, 963298), datetime.datetime(1962, 9, 23, 12, 35, 17, 78784), datetime.datetime(1962, 12, 22, 8, 15, 7, 994742)),
(datetime.datetime(1963, 3, 21, 8, 19, 40, 833880), datetime.datetime(1963, 6, 22, 3, 4, 10, 655508), datetime.datetime(1963, 9, 23, 18, 23, 28, 437362), datetime.datetime(1963, 12, 22, 14, 1, 45, 177047)),
(datetime.datetime(1964, 3, 20, 14, 9, 51, 698134), datetime.datetime(1964, 6, 21, 8, 56, 58, 283246), datetime.datetime(1964, 9, 23, 0, 16, 48, 969101), datetime.datetime(1964, 12, 21, 19, 49, 25, 13533)),
(datetime.datetime(1965, 3, 20, 20, 4, 51, 71659), datetime.datetime(1965, 6, 21, 14, 55, 50, 666380), datetime.datetime(1965, 9, 23, 6, 5, 59, 563594), datetime.datetime(1965, 12, 22, 1, 40, 18, 947414)),
(datetime.datetime(1966, 3, 21, 1, 52, 49, 449472), datetime.datetime(1966, 6, 21, 20, 33, 32, 238026), datetime.datetime(1966, 9, 23, 11, 43, 15, 587824), datetime.datetime(1966, 12, 22, 7, 28, 3, 810448)),
(datetime.datetime(1967, 3, 21, 7, 36, 53, 661995), datetime.datetime(1967, 6, 22, 2, 22, 59, 817386), datetime.datetime(1967, 9, 23, 17, 38, 0, 373520), datetime.datetime(1967, 12, 22, 13, 16, 11, 511479)),
(datetime.datetime(1968, 3, 20, 13, 21, 52, 392668), datetime.datetime(1968, 6, 21, 8, 13, 24, 887013), datetime.datetime(1968, 9, 22, 23, 26, 9, 474692), datetime.datetime(1968, 12, 21, 18, 59, 39, 692293)),
(datetime.datetime(1969, 3, 20, 19, 8, 5, 229175), datetime.datetime(1969, 6, 21, 13, 55, 12, 482830), datetime.datetime(1969, 9, 23, 5, 6, 57, 294015), datetime.datetime(1969, 12, 22, 0, 43, 35, 537993)),
(datetime.datetime(1970, 3, 21, 0, 56, 17, 789578), datetime.datetime(1970, 6, 21, 19, 42, 48, 319113), datetime.datetime(1970, 9, 23, 10, 58, 55, 504169), datetime.datetime(1970, 12, 22, 6, 35, 34, 201079)),
(datetime.datetime(1971, 3, 21, 6, 38, 7, 512387), datetime.datetime(1971, 6, 22, 1, 19, 43, 452537), datetime.datetime(1971, 9, 23, 16, 45, 6, 374728), datetime.datetime(1971, 12, 22, 12, 23, 46, 336326)),
(datetime.datetime(1972, 3, 20, 12, 21, 33, 925941), datetime.datetime(1972, 6, 21, 7, 6, 20, 494651), datetime.datetime(1972, 9, 22, 22, 32, 46, 428795), datetime.datetime(1972, 12, 21, 18, 12, 47, 858175)),
(datetime.datetime(1973, 3, 20, 18, 12, 22, 612705), datetime.datetime(1973, 6, 21, 13, 0, 45, 643515), datetime.datetime(1973, 9, 23, 4, 21, 14, 396073), datetime.datetime(1973, 12, 22, 0, 7, 36, 337295)),
(datetime.datetime(1974, 3, 21, 0, 6, 39, 616004), datetime.datetime(1974, 6, 21, 18, 37, 46, 889786), datetime.datetime(1974, 9, 23, 9, 58, 23, 631818), datetime.datetime(1974, 12, 22, 5, 55, 49, 529268)),
(datetime.datetime(1975, 3, 21, 5, 56, 33, 578912), datetime.datetime(1975, 6, 22, 0, 26, 35, 943179), datetime.datetime(1975, 9, 23, 15, 55, 7, 395066), datetime.datetime(1975, 12, 22, 11, 45, 26, 575561)),
(datetime.datetime(1976, 3, 20, 11, 49, 32, 848767), datetime.datetime(1976, 6, 21, 6, 24, 22, 357365), datetime.datetime(1976, 9, 22, 21, 48, 15, 317625), datetime.datetime(1976, 12, 21, 17, 35, 0, 61049)),
(datetime.datetime(1977, 3, 20, 17, 42, 15, 410431), datetime.datetime(1977, 6, 21, 12, 13, 55, 688633), datetime.datetime(1977, 9, 23, 3, 29, 11, 425631), datetime.datetime(1977, 12, 21, 23, 23, 1, 531094)),
(datetime.datetime(1978, 3, 20, 23, 33, 28, 736899), datetime.datetime(1978, 6, 21, 18, 9, 43, 537850), datetime.datetime(1978, 9, 23, 9, 25, 33, 779023), datetime.datetime(1978, 12, 22, 5, 20, 51, 486379)),
(datetime.datetime(1979, 3, 21, 5, 22, 4, 264637), datetime.datetime(1979, 6, 21, 23, 56, 19, 472315), datetime.datetime(1979, 9, 23, 15, 16, 23, 193335), datetime.datetime(1979, 12, 22, 11, 9, 38, 471221)),
(datetime.datetime(1980, 3, 20, 11, 9, 36, 131923), datetime.datetime(1980, 6, 21, 5, 47, 10, 79462), datetime.datetime(1980, 9, 22, 21, 8, 44, 697918), datetime.datetime(1980, 12, 21, 16, 55, 59, 641365)),
(datetime.datetime(1981, 3, 20, 17, 2, 55, 460693), datetime.datetime(1981, 6, 21, 11, 44, 50, 973531), datetime.datetime(1981, 9, 23, 3, 5, 14, 538073), datetime.datetime(1981, 12, 21, 22, 50, 25, 510994)),
(datetime.datetime(1982, 3, 20, 22, 55, 45, 645026), datetime.datetime(1982, 6, 21, 17, 23, 9, 876199), datetime.datetime(1982, 9, 23, 8, 46, 9, 342940), datetime.datetime(1982, 12, 22, 4, 38, 0, 913921)),
(datetime.datetime(1983, 3, 21, 4, 38, 42, 757247), datetime.datetime(1983, 6, 21, 23, 8, 50, 886215), datetime.datetime(1983, 9, 23, 14, 41, 43, 959122), datetime.datetime(1983, 12, 22, 10, 29, 47, 6056)),
(datetime.datetime(1984, 3, 20, 10, 24, 20, 21746), datetime.datetime(1984, 6, 21, 5, 2, 24, 433409), datetime.datetime(1984, 9, 22, 20, 32, 50, 727212), datetime.datetime(1984, 12, 21, 16, 22, 42, 73783)),
(datetime.datetime(1985, 3, 20, 16, 13, 34, 894879), datetime.datetime(1985, 6, 21, 10, 44, 18, 383759), datetime.datetime(1985, 9, 23, 2, 7, 32, 362292), datetime.datetime(1985, 12, 21, 22, 7, 35, 184596)),
(datetime.datetime(1986, 3, 20, 22, 2, 46, 457677), datetime.datetime(1986, 6, 21, 16, 30, 7, 638984), datetime.datetime(1986, 9, 23, 7, 58, 48, 718426), datetime.datetime(1986, 12, 22, 4, 2, 1, 635909)),
(datetime.datetime(1987, 3, 21, 3, 51, 54, 693872), datetime.datetime(1987, 6, 21, 22, 10, 54, 669230), datetime.datetime(1987, 9, 23, 13, 45, 18, 271552), datetime.datetime(1987, 12, 22, 9, 45, 46, 586096)),
(datetime.datetime(1988, 3, 20, 9, 38, 43, 336231), datetime.datetime(1988, 6, 21, 3, 56, 42, 658974), datetime.datetime(1988, 9, 22, 19, 28, 58, 656648), datetime.datetime(1988, 12, 21, 15, 27, 47, 219306)),
(datetime.datetime(1989, 3, 20, 15, 28, 19, 528036), datetime.datetime(1989, 6, 21, 9, 53, 11, 596182), datetime.datetime(1989, 9, 23, 1, 19, 38, 459535), datetime.datetime(1989, 12, 21, 21, 21, 53, 722638)),
(datetime.datetime(1990, 3, 20, 21, 19, 14, 732835), datetime.datetime(1990, 6, 21, 15, 32, 56, 52522), datetime.datetime(1990, 9, 23, 6, 55, 40, 636009), datetime.datetime(1990, 12, 22, 3, 6, 51, 869019)),
(datetime.datetime(1991, 3, 21, 3, 2, 1, 133276), datetime.datetime(1991, 6, 21, 21, 18, 56, 310057), datetime.datetime(1991, 9, 23, 12, 48, 0, 626807), datetime.datetime(1991, 12, 22, 8, 53, 31, 485137)),
(datetime.datetime(1992, 3, 20, 8, 47, 53, 503118), datetime.datetime(1992, 6, 21, 3, 14, 17, 570903), datetime.datetime(1992, 9, 22, 18, 42, 47, 980557), datetime.datetime(1992, 12, 21, 14, 43, 7, 361728)),
(datetime.datetime(1993, 3, 20, 14, 40, 38, 646254), datetime.datetime(1993, 6, 21, 8, 59, 53, 847835), datetime.datetime(1993, 9, 23, 0, 22, 22, 759183), datetime.datetime(1993, 12, 21, 20, 25, 40, 571612)),
(datetime.datetime(1994, 3, 20, 20, 27, 53, 633113), datetime.datetime(1994, 6, 21, 14, 47, 42, 314853), datetime.datetime(1994, 9, 23, 6, 19, 11, 903217), datetime.datetime(1994, 12, 22, 2, 22, 34, 993460)),
(datetime.datetime(1995, 3, 21, 2, 14, 29, 41079), datetime.datetime(1995, 6, 21, 20, 34, 31, 161684), datetime.datetime(1995, 9, 23, 12, 13, 7, 562921), datetime.datetime(1995, 12, 22, 8, 16, 37, 680400)),
(datetime.datetime(1996, 3, 20, 8, 3, 8, 91631), datetime.datetime(1996, 6, 21, 2, 23, 52, 843205), datetime.datetime(1996, 9, 22, 18, 0, 5, 641763), datetime.datetime(1996, 12, 21, 14, 5, 45, 117337)),
(datetime.datetime(1997, 3, 20, 13, 54, 36, 776802), datetime.datetime(1997, 6, 21, 8, 20, 3, 758737), datetime.datetime(1997, 9, 22, 23, 55, 56, 109425), datetime.datetime(1997, 12, 21, 20, 6, 55, 80102)),
(datetime.datetime(1998, 3, 20, 19, 54, 36, 904383), datetime.datetime(1998, 6, 21, 14, 2, 42, 102878), datetime.datetime(1998, 9, 23, 5, 37, 5, 608242), datetime.datetime(1998, 12, 22, 1, 56, 18, 601763)),
(datetime.datetime(1999, 3, 21, 1, 45, 41, 458376), datetime.datetime(1999, 6, 21, 19, 49, 15, 526073), datetime.datetime(1999, 9, 23, 11, 31, 30, 826444), datetime.datetime(1999, 12, 22, 7, 43, 40, 697948)),
(datetime.datetime(2000, 3, 20, 7, 35, 17, 37334), datetime.datetime(2000, 6, 21, 1, 47, 51, 106317), datetime.datetime(2000, 9, 22, 17, 27, 35, 497414), datetime.datetime(2000, 12, 21, 13, 37, 17, 993991)),
(datetime.datetime(2001, 3, 20, 13, 30, 37, 680245), datetime.datetime(2001, 6, 21, 7, 37, 54, 257428), datetime.datetime(2001, 9, 22, 23, 4, 26, 742552), datetime.datetime(2001, 12, 21, 19, 21, 21, 259775)),
(datetime.datetime(2002, 3, 20, 19, 16, 5, 757600), datetime.datetime(2002, 6, 21, 13, 24, 34, 142225), datetime.datetime(2002, 9, 23, 4, 55, 30, 774556), datetime.datetime(2002, 12, 22, 1, 14, 13, 938224)),
(datetime.datetime(2003, 3, 21, 0, 59, 49, 355040), datetime.datetime(2003, 6, 21, 19, 10, 37, 44539), datetime.datetime(2003, 9, 23, 10, 46, 47, 767616), datetime.datetime(2003, 12, 22, 7, 3, 38, 273172)),
(datetime.datetime(2004, 3, 20, 6, 48, 33, 172398), datetime.datetime(2004, 6, 21, 0, 57, 2, 200884), datetime.datetime(2004, 9, 22, 16, 29, 58, 577140), datetime.datetime(2004, 12, 21, 12, 41, 28, 706118)),
(datetime.datetime(2005, 3, 20, 12, 33, 31, 27063), datetime.datetime(2005, 6, 21, 6, 46, 16, 871377), datetime.datetime(2005, 9, 22, 22, 23, 8, 334234), datetime.datetime(2005, 12, 21, 18, 34, 47, 958619)),
(datetime.datetime(2006, 3, 20, 18, 25, 25, 962442), datetime.datetime(2006, 6, 21, 12, 26, 1, 64509), datetime.datetime(2006, 9, 23, 4, 3, 25, 512042), datetime.datetime(2006, 12, 22, 0, 21, 56, 802567)),
(datetime.datetime(2007, 3, 21, 0, 7, 28, 222175), datetime.datetime(2007, 6, 21, 18, 6, 33, 927453), datetime.datetime(2007, 9, 23, 9, 51, 17, 535803), datetime.datetime(2007, 12, 22, 6, 7, 40, 289544)),
(datetime.datetime(2008, 3, 20, 5, 48, 12, 815450), datetime.datetime(2008, 6, 20, 23, 59, 31, 371461), datetime.datetime(2008, 9, 22, 15, 44, 24, 294264), datetime.datetime(2008, 12, 21, 12, 3, 36, 526087)),
(datetime.datetime(2009, 3, 20, 11, 43, 30, 282357), datetime.datetime(2009, 6, 21, 5, 45, 40, 729041), datetime.datetime(2009, 9, 22, 21, 18, 39, 121810), datetime.datetime(2009, 12, 21, 17, 46, 38, 654911)),
(datetime.datetime(2010, 3, 20, 17, 32, 11, 253196), datetime.datetime(2010, 6, 21, 11, 28, 34, 304689), datetime.datetime(2010, 9, 23, 3, 8, 53, 820463), datetime.datetime(2010, 12, 21, 23, 38, 18, 714026)),
(datetime.datetime(2011, 3, 20, 23, 20, 34, 415258), datetime.datetime(2011, 6, 21, 17, 16, 40, 99839), datetime.datetime(2011, 9, 23, 9, 4, 43, 103012), datetime.datetime(2011, 12, 22, 5, 29, 53, 701035)),
(datetime.datetime(2012, 3, 20, 5, 14, 30, 138280), datetime.datetime(2012, 6, 20, 23, 8, 57, 328766), datetime.datetime(2012, 9, 22, 14, 49, 0, 44567), datetime.datetime(2012, 12, 21, 11, 11, 28, 880285)),
(datetime.datetime(2013, 3, 20, 11, 1, 51, 961078), datetime.datetime(2013, 6, 21, 5, 4, 7, 607677), datetime.datetime(2013, 9, 22, 20, 44, 13, 329441), datetime.datetime(2013, 12, 21, 17, 10, 53, 27918)),
(datetime.datetime(2014, 3, 20, 16, 57, 6, 156335), datetime.datetime(2014, 6, 21, 10, 51, 23, 474435), datetime.datetime(2014, 9, 23, 2, 29, 11, 236259), datetime.datetime(2014, 12, 21, 23, 2, 52, 276507)),
(datetime.datetime(2015, 3, 20, 22, 45, 7, 586142), datetime.datetime(2015, 6, 21, 16, 38, 3, 981391), datetime.datetime(2015, 9, 23, 8, 20, 26, 656868), datetime.datetime(2015, 12, 22, 4, 47, 48, 767922)),
(datetime.datetime(2016, 3, 20, 4, 30, 2, 619070), datetime.datetime(2016, 6, 20, 22, 34, 20, 426802), datetime.datetime(2016, 9, 22, 14, 21, 12, 688971), datetime.datetime(2016, 12, 21, 10, 44, 2, 367104)),
(datetime.datetime(2017, 3, 20, 10, 28, 37, 516239), datetime.datetime(2017, 6, 21, 4, 24, 17, 882888), datetime.datetime(2017, 9, 22, 20, 1, 41, 290341), datetime.datetime(2017, 12, 21, 16, 27, 48, 281359)),
(datetime.datetime(2018, 3, 20, 16, 15, 17, 118823), datetime.datetime(2018, 6, 21, 10, 7, 23, 784557), datetime.datetime(2018, 9, 23, 1, 54, 9, 172752), datetime.datetime(2018, 12, 21, 22, 22, 34, 552479)),
(datetime.datetime(2019, 3, 20, 21, 58, 31, 295596), datetime.datetime(2019, 6, 21, 15, 54, 21, 207206), datetime.datetime(2019, 9, 23, 7, 50, 13, 586471), datetime.datetime(2019, 12, 22, 4, 19, 15, 205256)),
(datetime.datetime(2020, 3, 20, 3, 49, 32, 938651), datetime.datetime(2020, 6, 20, 21, 43, 46, 545771), datetime.datetime(2020, 9, 22, 13, 30, 38, 27446), datetime.datetime(2020, 12, 21, 10, 2, 9, 31953)),
(datetime.datetime(2021, 3, 20, 9, 37, 26, 124175), datetime.datetime(2021, 6, 21, 3, 32, 14, 899194), datetime.datetime(2021, 9, 22, 19, 21, 8, 964079), datetime.datetime(2021, 12, 21, 15, 59, 5, 437947)),
(datetime.datetime(2022, 3, 20, 15, 33, 19, 379630), datetime.datetime(2022, 6, 21, 9, 13, 55, 15271), datetime.datetime(2022, 9, 23, 1, 3, 31, 341610), datetime.datetime(2022, 12, 21, 21, 47, 58, 459759)),
(datetime.datetime(2023, 3, 20, 21, 24, 13, 141724), datetime.datetime(2023, 6, 21, 14, 57, 53, 550960), datetime.datetime(2023, 9, 23, 6, 49, 58, 211650), datetime.datetime(2023, 12, 22, 3, 27, 7, 203441)),
(datetime.datetime(2024, 3, 20, 3, 6, 20, 137267), datetime.datetime(2024, 6, 20, 20, 51, 1, 96369), datetime.datetime(2024, 9, 22, 12, 43, 29, 907911), datetime.datetime(2024, 12, 21, 9, 20, 18, 280768)),
(datetime.datetime(2025, 3, 20, 9, 1, 12, 558547), datetime.datetime(2025, 6, 21, 2, 42, 16, 305785), datetime.datetime(2025, 9, 22, 18, 19, 14, 850568), datetime.datetime(2025, 12, 21, 15, 2, 48, 616863)),
(datetime.datetime(2026, 3, 20, 14, 45, 50, 775462), datetime.datetime(2026, 6, 21, 8, 24, 28, 624660), datetime.datetime(2026, 9, 23, 0, 5, 6, 589644), datetime.datetime(2026, 12, 21, 20, 49, 56, 973975)),
(datetime.datetime(2027, 3, 20, 20, 24, 29, 98241), datetime.datetime(2027, 6, 21, 14, 10, 47, 446673), datetime.datetime(2027, 9, 23, 6, 1, 29, 774416), datetime.datetime(2027, 12, 22, 2, 41, 50, 402167)),
(datetime.datetime(2028, 3, 20, 2, 16, 54, 528525), datetime.datetime(2028, 6, 20, 20, 1, 56, 876655), datetime.datetime(2028, 9, 22, 11, 45, 13, 347840), datetime.datetime(2028, 12, 21, 8, 19, 20, 434894)),
(datetime.datetime(2029, 3, 20, 8, 1, 48, 230613), datetime.datetime(2029, 6, 21, 1, 48, 13, 625820), datetime.datetime(2029, 9, 22, 17, 38, 14, 868302), datetime.datetime(2029, 12, 21, 14, 13, 45, 620356)),
    ]

    
def next_spring_equinox(year):
    """@param year: a string
    @returns: Date
    """
    year = int(year)
    idx = year - 1900
    return Date(dates[idx][0])


def next_summer_solstice(year):
    year = int(year)
    idx = year - 1900
    return Date(dates[idx][1])


def next_autumn_equinox(year):
    year = int(year)
    idx = year - 1900
    return Date(dates[idx][2])


def next_winter_solstice(year):
    year = int(year)
    idx = year - 1900
    return Date(dates[idx][3])
