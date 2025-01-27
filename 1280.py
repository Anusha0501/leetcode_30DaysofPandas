#1280. Students and Examinations

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged_df = students.merge(subjects, how = 'cross')
    df = examinations.groupby(['student_id','subject_name'])['subject_name'].size().reset_index(name = 'attended_exams')
    final_df = merged_df.merge(df, how = 'left')
    final_df.sort_values(by = ['student_id','subject_name'], ascending = True, inplace = True)
    final_df['attended_exams'] = final_df['attended_exams'].fillna(0)
    return final_df
