import xlrd
from nltk import FreqDist
import inflect # plural to singular, indefinite articles


def analysis():
    workbook = xlrd.open_workbook("static/files/Book1.xls","rb")
    sheets = workbook.sheet_names()
    p = inflect.engine()
    target = []
    source = []
    target_source = []
    abstractness = []
    for sheet_name in sheets:
        sh = workbook.sheet_by_name(sheet_name)
        for rownum in range(sh.nrows):
            row_values = sh.row_values(rownum)
            for i in range(1,3):
                if p.singular_noun(row_values[i]) != False:
                    row_values[i] = p.singular_noun(row_values[i])
            target.append(row_values[1])
            source.append(row_values[2])
            target_source.append((row_values[1], row_values[2]))
            abstractness.append(row_values[3])
    target = target[1:]   
    source = source[1:]         
    target_source = target_source[1:]
    abstractness = abstractness[1:]
    abst_target = [list(x)[0] for x in abstractness]
    abst_source = [list(x)[1] for x in abstractness]
    fdist1 = FreqDist(target_source)
    fdist_ts = fdist1.most_common(25)
    fdist2 = FreqDist(abstractness)
    fdist_abst = fdist2.most_common(25)
    fdist3 = FreqDist(target)
    fdist_t = fdist3.most_common(25)
    fdist4 = FreqDist(source)
    fdist_s = fdist4.most_common(25)
    fdist5 = FreqDist(abst_target)
    fdist_abst_t = fdist5.most_common(25)
    fdist6 = FreqDist(abst_source)
    fdist_abst_s = fdist6.most_common(25)
    ts_with_mapping = []

    for a_tuple in fdist_ts:
        temp = []
        temp.append(a_tuple)
        temp.append(str(a_tuple[0][0] + " IS " + p.an(a_tuple[0][1].lower()).upper()))
        ts_with_mapping.append(temp)
    all_requirements = [ts_with_mapping, fdist_abst, fdist_t, fdist_s, fdist_abst_t, fdist_abst_s]

    return all_requirements