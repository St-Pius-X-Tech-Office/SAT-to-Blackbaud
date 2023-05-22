import ids
import pandas as pd

export_columns = [
    "student_id",
    "host_id",
    "user_id",
    "test_description",
    "test_date_time",
    "comment",
    "overall_score",
    "registered_date",
    "registered_location",
    "rescheduled",
    "no_show",
    "proctor_id",
    "proctor_other",
    "print_on_report_card",
    "print_on_transcript",
    "subtest_description",
    "score",
    "percentile",
    "scale",
    "stanine",
    "subtest_comment",
]

final_df = pd.DataFrame(columns=export_columns)

master_list = pd.read_csv("SAT Master.csv")


def main():
    for i in range(len(master_list)):
        student_name = (
            f"{master_list.loc[i, 'NAME_LAST']} {master_list.loc[i, 'NAME_FIRST']}"
        )
        if student_name.title() not in ids.student_ids:
            final_name = student_name.title()
        else:
            final_name = ids.student_ids[f"{student_name.title()}"]
        count = 0

        while count != 3:
            if count == 0:
                test = "EBRW"
                test_score = master_list.loc[i, "LATEST_SAT_EBRW"]
                test_percentile = master_list.loc[i, "PERCENTILE_NATREP_SAT_EBRW"]
            elif count == 1:
                test = "MATH"
                test_score = master_list.loc[i, "LATEST_SAT_MATH_SECTION"]
                test_percentile = master_list.loc[
                    i, "PERCENTILE_NATREP_SAT_MATH_SECTION"
                ]
            elif count == 2:
                test = "TOTAL"
                test_score = master_list.loc[i, "LATEST_SAT_TOTAL"]
                test_percentile = master_list.loc[i, "PERCENTILE_NATREP_SAT_TOTAL"]

            final_df.loc[-1] = [
                final_name,
                " ",
                " ",
                "SAT",
                str(master_list.loc[i, "LATEST_SAT_DATE"]),
                " ",  # comment
                " ",  # overall_score
                " ",  # registered_data
                " ",  # registered_location
                " ",
                " ",
                " ",  # proctor_id
                " ",  # proctor_other
                "No",  # print on report
                "Yes",  # print on transc
                test,
                test_score,
                test_percentile,
                " ",  # Scale
                " ",  # Stanine
                " ",  # Subtest_Comment
            ]

            final_df.index += 1
            final_df.sort_index()
            count += 1


main()
final_df.to_csv("sat_test_validator.csv", index=False)
