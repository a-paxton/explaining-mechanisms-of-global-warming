# clean up transcripts
def DE_transcript_cleanup(transcript_df):
    
    # import all necessary modules
    import re
    import pandas as pd

    # grab the utterance column, rename it, and begin text prep
    utterance_column = transcript_df.columns[transcript_df.columns.str.contains('tteranc')][0]
    transcript_df['word'] = transcript_df[utterance_column].str.strip().str.lower().str.replace('-',' ')
    
    # strip out abbreviations
    transcript_df['word'] = transcript_df['word'].replace('^arn\'t$','are not',regex=True).replace('^uhm+$','um',regex=True)
    transcript_df['word'] = transcript_df['word'].str.replace('\'ll',' will')
    transcript_df['word'] = transcript_df['word'].replace('^(it|there)\'s$','\\1 is',regex=True)
    transcript_df['word'] = transcript_df['word'].replace('^i\'?m$','i am',regex=True)
    transcript_df['word'] = transcript_df['word'].replace('(do|are|is)n\'?t','\\1 not',regex=True)
    transcript_df['word'] = transcript_df['word'].replace('won\'?t','will not',regex=True)
    transcript_df['word'] = transcript_df['word'].str.replace('\'(.)',' \\1')
    
    # clean up spelling errors
    transcript_df['word'] = transcript_df['word'].str.replace('alot','a lot').str.replace('becasue','because')
    transcript_df['word'] = transcript_df['word'].str.replace('eviroment','environment').str.replace('callled','called')
    transcript_df['word'] = transcript_df['word'].str.replace('fourty','forty').str.replace('mmmonoxide','monoxide')
    transcript_df['word'] = transcript_df['word'].str.replace('gasses','gases').str.replace('rayes','rays')
    transcript_df['word'] = transcript_df['word'].str.replace('grenhouse','greenhouse')
    
    # clean up text-only variable and transcript dataframe
    transcript_content = re.sub(' +',' ',' '.join(transcript_df['word']))
    transcript_content = transcript_content.split(' ')
    transcript_df = transcript_df.drop(utterance_column,axis=1)
    
    # spit out the transcript and the transcript text
    return transcript_df, transcript_content