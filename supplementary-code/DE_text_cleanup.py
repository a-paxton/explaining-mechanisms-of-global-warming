# clean up transcripts
def DE_questionnaire_cleanup(text_input,answer_col):
    
    # import all necessary modules
    import re, string
    import pandas as pd

    # grab the utterance column, rename it, and begin text prep
    unnamed_column = text_input.columns[text_input.columns.str.contains('nnamed')][0]
    text_input = text_input.drop(unnamed_column,axis=1)
    
    # assign numeric codes to Wilson-Patternson text-only variables
    text_input[answer_col] = text_input[answer_col].str.replace('^Disagree$', 'Disagree (1)')
    text_input[answer_col] = text_input[answer_col].str.replace('^Agree$', 'Agree (5)')
    text_input[answer_col] = text_input[answer_col].str.replace('^Uncertain$', 'Uncertain (3)')
    
    # assign numeric codes to some questions (Pol1-2, CC1, CC10)
    text_input[answer_col] = text_input[answer_col].str.replace('^Yes$', 'Yes (5)')
    text_input[answer_col] = text_input[answer_col].str.replace('^No$', 'No (1)')

    # assign numeric codes to climate change questions (CC1-2)
    text_input[answer_col] = text_input[answer_col].str.replace('^Don\'t Know$', 'Don''t Know (3)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Extremely sure$', 'Extremely sure (5)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Very sure$', 'Very sure (4)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Somewhat sure$', 'Somewhat sure (2)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Not at all sure$', 'Not at all sure (1)',case=False)

    # assign numeric codes to climate change questions (CC3)
    text_input[answer_col] = text_input[answer_col].str.replace('^Caused mostly by human activity$', 'human (5)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Caused by both human activities and natural changes$', 'human_and_natural (4)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Caused mostly by natural changes in the environment$', 'nature (2)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Other$', 'other (1)',case=False)

    # assign numeric codes to climate change questions (CC4)
    text_input[answer_col] = text_input[answer_col].str.replace('^Most scientists think global warming is happening$', 'sci_agree (103)',case=False)    
    text_input[answer_col] = text_input[answer_col].str.replace('^There is a lot of disagreement among the scientists about whether or not global warming is happening', 'sci_unsure (102)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Most scientists think global warming is not happening$', 'sci_disagree (101)',case=False) 
    text_input[answer_col] = text_input[answer_col].str.replace('^Don.t know enough to say$', 'too_little_info (100)',case=False)    

    # assign numeric codes to climate change questions (CC5)
    text_input[answer_col] = text_input[answer_col].str.replace('^Very worried$', 'Very worried (5)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Somewhat worried$', 'Somewhat worried (4)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Not very worried$', 'Not very worried (2)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Not at all worried$', 'Not at all worried (1)',case=False)
    
    # assign numeric codes to climate change questions (CC6-9)
    text_input[answer_col] = text_input[answer_col].str.replace('^Very well informed$', 'Very well informed (5)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Fairly well informed$', 'Fairly well informed (4)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Not very well informed$', 'Not very well informed (2)',case=False)
    text_input[answer_col] = text_input[answer_col].str.replace('^Not at all informed$', 'Not at all informed (1)',case=False)

    # create a numeric-only column
    text_input['answer_number'] = text_input[answer_col].str.extract('(\d+)')
    text_input['participant_number'] = text_input['Subject'].str.extract('(\d+)')

    # clean up spelling errors
    text_only = text_input[text_input['Source'] == 'CC11'][answer_col].iloc[0].lower()
    text_only = re.sub('contribtuting','contributing',text_only)
    text_only = re.sub('weaking','weakening',text_only)
    text_only = re.sub('tempature','temperature',text_only)
    text_only = re.sub('electronnics','electronics',text_only)
    text_only = re.sub('(?!<=e)radication','radiation',text_only)
    text_only = re.sub('rlease','release',text_only)
    text_only = re.sub('methan(?!=e)','methane',text_only)
    text_only = re.sub('methanee','methane',text_only)
    text_only = re.sub('atmpshere','atmosphere',text_only)
    text_only = re.sub('erroding','eroding',text_only)
    text_only = re.sub('sunds','sun''s',text_only)
    text_only = re.sub('enviornment','environment',text_only)
    text_only = re.sub('polution','pollution',text_only)
    text_only = re.sub('findin','finding',text_only)
    text_only = re.sub('excessivew','excessive',text_only)
    text_only = re.sub('peirced','pierced',text_only)

    # strip out abbreviations
    text_only = re.sub('\'ll',' will',text_only)
    text_only = re.sub('(it|there)\'s','\\1 is',text_only)
    text_only = re.sub('i\'?m ','i am ',text_only)
    text_only = re.sub('(do|are|is)n\'?t','\\1 not',text_only)
    text_only = re.sub('won\'?t','will not',text_only)
    text_only = re.sub('\'(.)',' \\1',text_only)

    # remove punctuation
    text_only = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text_only)

    # clean up spelling errors
    # text_only['word'] = text_only['word'].str.replace('alot','a lot').str.replace('becasue','because')
    # text_only['word'] = text_only['word'].str.replace('eviroment','environment').str.replace('callled','called')
    # text_only['word'] = text_only['word'].str.replace('fourty','forty').str.replace('mmmonoxide','monoxide')
    # text_only['word'] = text_only['word'].str.replace('gasses','gases').str.replace('rayes','rays')
    # text_only['word'] = text_only['word'].str.replace('grenhouse','greenhouse')
    
    # clean up text-only variable and transcript dataframe
    text_only = re.sub(' +',' ',text_only)
    #text_only = ','.join(text_only.split(' '))
    #text_input = text_input.drop(utterance_column,axis=1)
    
    # spit out the transcript and the transcript text
    return text_input, text_only