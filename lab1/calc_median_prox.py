from statistics import median

times = [
    3.814697265625e-06,
    0.49725937843322754,
    0.007894515991210938,
    0.5096449851989746,
    0.12497806549072266,
    0.3156318664550781,
    0.7250444889068604,
    0.7978808879852295,
    0.005709648132324219,
    0.4034433364868164,
    0.42781877517700195,
    0.5377652645111084,
    0.318378210067749,
    0.7365555763244629,
    0.13646411895751953,
    0.9769473075866699,
    0.1526203155517578,
    0.9332847595214844,
    0.2617068290710449,
    0.0895843505859375,
    0.08203649520874023,
    0.8712637424468994,
    0.6689846515655518,
    0.9049220085144043,
    0.8972985744476318,
    0.7647233009338379,
    0.7858395576477051,
    0.266080379486084,
    0.3182682991027832,
    0.2614603042602539,
    0.9705579280853271,
    0.5632593631744385,
    0.15147733688354492,
    0.5455999374389648,
    0.5413439273834229,
    0.8970959186553955,
    0.3490488529205322,
    0.10630249977111816,
    0.25987672805786133,
    0.4069514274597168,
    0.14008855819702148,
    0.936373233795166,
    0.8976821899414062,
    0.9344339370727539,
    0.5073091983795166,
    0.7286021709442139,
    0.4693796634674072,
    0.8249111175537109,
    0.48871803283691406,
    0.5557758808135986,
    0.08901166915893555,
    0.869516134262085,
    0.34758663177490234,
    0.11266827583312988,
    0.5900702476501465,
    0.17524313926696777,
    0.2602698802947998,
    0.2332780361175537,
    0.7215538024902344,
    0.66257643699646,
    0.3893587589263916,
    0.13695645332336426,
    0.7957961559295654,
    0.8919887542724609,
    0.2094414234161377,
    0.7342562675476074,
    0.12407350540161133,
    0.5569777488708496,
    0.2974364757537842,
    0.8183259963989258,
    0.6618919372558594,
    0.796442985534668,
    0.7656724452972412,
    0.9930877685546875,
    0.3621089458465576,
    0.13202333450317383,
    0.4050414562225342,
    0.7264583110809326,
    0.7567036151885986,
    0.15727972984313965,
    0.6487958431243896,
    0.3401672840118408,
    0.17973971366882324,
    0.21496891975402832,
    0.5043456554412842,
    0.09654831886291504,
    0.2594156265258789,
    0.961306095123291,
    0.645226240158081,
    0.6777606010437012,
    0.7045252323150635,
    0.08158636093139648,
    0.021897077560424805,
    0.4632296562194824,
    0.6346805095672607,
    0.8102953433990479,
    0.26897597312927246,
    0.025141000747680664,
    0.16373848915100098,
    0.04675126075744629,
    0.5083894729614258,
]

times = sorted(times)

print("Avg: ", sum(times) / len(times))
m = len(times)
print("Median: ", median(times))