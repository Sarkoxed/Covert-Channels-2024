from statistics import median

times = [
    -4.5299530029296875e-06,
    -0.44110655784606934,
    -0.6215136051177979,
    -0.2872605323791504,
    -0.5799140930175781,
    -0.3745911121368408,
    -0.05566000938415527,
    -0.8918814659118652,
    -0.79793381690979,
    -0.842993974685669,
    -0.10771656036376953,
    -0.055684566497802734,
    -0.864163875579834,
    -0.38006067276000977,
    -0.8176486492156982,
    -0.7125747203826904,
    -0.1012272834777832,
    -0.4170081615447998,
    -0.5657095909118652,
    -0.9181170463562012,
    -0.4489562511444092,
    -0.9327576160430908,
    -0.07800626754760742,
    -0.050377607345581055,
    -0.1988987922668457,
    -0.26348328590393066,
    -0.11394166946411133,
    -0.08508014678955078,
    -0.4036588668823242,
    -0.5687506198883057,
    -0.37176012992858887,
    -0.10276961326599121,
    -0.5041286945343018,
    -0.6163711547851562,
    -0.7839405536651611,
    -0.9087867736816406,
    -0.3825831413269043,
    -0.40723514556884766,
    -0.9445085525512695,
    -0.7058355808258057,
    -0.061180830001831055,
    -0.18532156944274902,
    -0.8039860725402832,
    -0.7783448696136475,
    -0.7974128723144531,
    -0.9872455596923828,
    -0.5487837791442871,
    -0.01424264907836914,
    -0.4742112159729004,
    -0.28615784645080566,
    -0.8942222595214844,
    -0.8490810394287109,
    -0.716881513595581,
    -0.773334264755249,
    -0.5484018325805664,
    -0.48769211769104004,
    -0.5888779163360596,
    -0.5660400390625,
    -0.2639892101287842,
    -0.0029659271240234375,
    -0.2468271255493164,
    -0.0016503334045410156,
    -0.4957239627838135,
    -0.20171046257019043,
    -0.6970715522766113,
    -0.1700448989868164,
    -0.14959168434143066,
    -0.7045655250549316,
    -0.885737419128418,
    -0.9449143409729004,
    -0.4111907482147217,
    -0.1107485294342041,
    -0.07441926002502441,
    -0.44134044647216797,
    -0.05954122543334961,
    -0.048737525939941406,
    -0.46045470237731934,
    -0.9974503517150879,
    -0.3063943386077881,
    -0.26959967613220215,
    -0.988116979598999,
    -0.25245189666748047,
    -0.30680108070373535,
    -0.5623133182525635,
    -0.6262009143829346,
    -0.21662259101867676,
    -0.27277278900146484,
    -0.2955601215362549,
    -0.6745612621307373,
    -0.2925114631652832,
    -0.32515406608581543,
    -0.5487918853759766,
    -0.18476581573486328,
    -0.7931442260742188,
    -0.3999440670013428,
    -0.23666000366210938,
    -0.019815444946289062,
    -0.9191780090332031,
    -0.8611922264099121,
    -0.058727264404296875,
    -0.7670230865478516,
]

times = sorted([-x for x in times])

print("Avg: ", sum(times) / len(times))
m = len(times)
print("Median: ", median(times))