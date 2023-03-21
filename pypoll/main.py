import os
import csv
# path to collect file
poll_results=r'C:/Users/klw4b/OneDrive/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv'

candidates_list=[]
vote_count={}
Final_votes=[]
vote_perct=[]
with open(poll_results,"r") as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    total=0
    
    

    for row in reader:
        total+=1
        candidates=row[2]
        
        if candidates not in candidates_list:
            candidates_list.append(candidates)
            vote_count[candidates]=0         
    
        vote_count[candidates]=vote_count[candidates]+1  
top_vote=0
top_win=""       
for names in candidates_list:
    percentage=round(((vote_count[names]/total)*100),2)
    vote_count[names]=[vote_count[names],percentage]
    Final_votes.append(vote_count[names][0])
    vote_perct.append(str(vote_count[names][1])+ "%")
    if percentage>top_vote:
        top_vote=percentage
        top_win=names
  
        
       
     


   
       
       
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total}")
print("------------------------------")
print(f"{vote_count}")
print("------------------------------")
print(f"Winner : {top_win}")


cleaned_csv=zip(candidates_list,Final_votes,vote_perct)       
   
output_file=os.path.join("Analysis","election_results.csv")
with open(output_file,'w') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    
    csvwriter.writerow(["Total Votes",total])
    csvwriter.writerow(["Candidate","Total Votes","Total Vote %"])
    csvwriter.writerows(cleaned_csv)
    csvwriter.writerow(["Winner",top_win])