import pandas as pd

def load_ratings(filename):

    # Using Pandas with a column specification
    col_specification = [
        (  0,  14), # 15 ID Number
        ( 15,  75), # 61 Name
        ( 76,  79), #  4 Fed
        ( 80,  83), #  4 Sex
        ( 84,  88), #  5 Tit
        ( 89,  93), #  5 WTit
        ( 94, 108), # 15 OTit
        (109, 112), #  4 FOA
        (113, 118), #  6 SRtng
        (119, 122), #  4 SGm
        (123, 125), #  3 SK
        (126, 131), #  6 RRtng
        (132, 135), #  4 RGm
        (136, 138), #  3 Rk
        (139, 144), #  6 BRtng
        (145, 148), #  4 BGm
        (149, 151), #  3 BK
        (152, 157)  #  6 B-day
    ]

    col_names = [
        "ID Number",
        "Name",
        "Fed",
        "Sex",
        "Tit",
        "WTit",
        "OTit",
        "FOA",
        "SRtng",
        "SGm",
        "SK",
        "RRtng",
        "RGm",
        "Rk",
        "BRtng",
        "BGm",
        "BK",
        "B-day"
    ]

    data = pd.read_fwf(
        filename,
        colspecs=col_specification,
        names=col_names,
        na_values='',
        skiprows=1
    )

    data.sort_values(by=['SRtng'], ascending=False)

    return data
