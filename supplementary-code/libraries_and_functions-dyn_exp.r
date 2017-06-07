#### libraries_and_functions-dyn_exp.r: Part of the `dyn_exp` project ####
#
# This script loads libraries and creates a number of 
# additional functions to facilitate data prep and analysis.
#
# Written by: A. Paxton (University of California, Berkeley)
# Date last modified: 26 July 2016
#
#####################################################################################

#### Import libraries ####

library(crqa)
library(lme4)
library(plyr)
library(dplyr)
library(stringr)
library(ggplot2)
library(beepr)
library(reshape2)
library(LSAfun)

#####################################################################################

#### Identify global variables ####

# target the variables from the raw gaze files that we want to keep
gaze_columns_to_keep = c('time','r_time','r_mins',
                    'type','trial','timing','frame',
                    'pupil_confidence','stimulus',
                    'l_dia_x','r_dia_x',
                    'l_aoi_hit','r_aoi_hit',
                    'l_event_info','r_event_info')

# target the variables from the raw transcript files that we want to keep
transcript_columns = c('nr','begin_time','end_time','duration','word')

#####################################################################################

#### Create custom functions ####

# "%notin%": Identify values from one list (x) not included in another (y)
'%notin%' <- function(x,y) !(x %in% y) 

# "import_gaze_files": Import a standardized version of the gaze files
import_gaze_files = function(gaze_file){
    
    # import libraries we'll need
    library(dplyr)
    library(stringr)
    
    # load in gaze file and identify its default header
    gaze_data_frame = data.frame(read.csv(gaze_file,header = FALSE, skip = 3))
    original_header = strsplit(readLines(gaze_file, n = 1, warn = FALSE),split=',')[[1]]
    
    # clean up the original columns a bit
    original_header = tolower(trimws(str_replace(string=original_header, 
                                                 pattern = "\\[(mm|px)\\]",
                                                 replacement="")))
    original_header = str_replace_all(original_header,pattern=' ','_')
    names(gaze_data_frame) = original_header
    
    # specify the ORIGINAL NAMES of the columns we want to have
    gaze_columns_to_keep = c('time','r_time','r_mins',
                    'type','trial','timing','frame',
                    'pupil_confidence','stimulus',
                    'l_dia_x','r_dia_x',
                    'l_aoi_hit','r_aoi_hit',
                    'l_event_info','r_event_info')
    
    # find overlap between current columns and keep columns
    final_columns = original_header[original_header %in% gaze_columns_to_keep]
    
    # keep only the columns in that list and return it
    gaze_data_frame = select(gaze_data_frame,one_of(final_columns))
    return(gaze_data_frame)
}
    
# "import_transcript_files": Import a standardized version of the transcript files
import_transcript_files = function(transcript_file){
    
    # import libraries we'll need
    library(dplyr)
    
    # load in transcript file and identify its default header
    transcript_data_frame = data.frame(read.csv(transcript_file,header = FALSE, skip = 3))
    original_header = strsplit(readLines(transcript_file, n = 1, warn = FALSE),split=',')[[1]]
    
    # clean up the original columns a bit
    original_header = tolower(trimws(original_header))
    original_header = str_replace_all(original_header,pattern=' ','_')
    names(transcript_data_frame) = original_header
    
    # clean up the data a bit
    transcript_data_frame = dplyr::mutate_each(transcript_data_frame, funs(sub(" ", "" , .)))
    transcript_data_frame = dplyr::mutate_each(transcript_data_frame, funs(tolower(trimws(.))))
    
    # convert hh:mm.ss time format for duration to just seconds
    transcript_data_frame$duration = str_replace(transcript_data_frame$duration,"00:0",'')   
    
    # find overlap between current columns and keep columns
    final_columns = original_header[original_header %in% transcript_columns]
    
    # keep only the columns in that list and return it
    transcript_data_frame = select(transcript_data_frame,one_of(final_columns))
    
    # convert the "nr" column to an integer
    transcript_data_frame$nr = strtoi(transcript_data_frame$nr)
    
    # return cleaned transcript file
    return(transcript_data_frame)
}
    
    
# "lookfor": Identify variables within a dataframe that appear within a specified list
lookfor = function(d,p) names(d)[grep(p,names(d))]