# Get Smart with Smarty 

Die Main idea ist: 

packe ein PDF hinein -> 

## 1:
daraus sollen karteikarten im Makrdown format erstellt werden Frage/Antwort
- anzahl ist egal // Prompts( ausführlich, 80/20, nur die Formeln)
- die wichtigsten Ifnroamtionen/Kernthemen sollen mit inbegriffen sein 
- für anki format importierbar sein 

Überlegungen 1: 
einfach umzustezen/ bestehendes LLm model, (Lokal/Cloud), Wie sieht die Pipeline aus. 


## 2
aus der PDF sollen die wichtigsten Informationen als Sprach datei extrahiert werden:
- Frage/ANtwort, Podcast format 


Überlegungen 2:
- die Ganze PDF als Datei? soll das LLM noch zusatz inforamtionen hinzufügen um das wie eine geschichte aufzubauen(da die Bilder fehlen) ?
- selektion der Wichtigsten Inhalte evtl auf redundante anbshcnitte wenn Sie wichtig sind 
- gestückelt oder als ganze Datei 


## TODOS:

- Ideen sammeln
- User Stories erstellen -> Pipeline Abastract()
- User Sotries umsetzten 
- be awesome 



## Modelle

pretrained:
Hugging_face 



## Steps:


### 1:
"ocr ** >- anreichner mit büchern " bild/ relvant? -> ja -> beschreiben  

datei einfügen -> kpis/ wichtigiste Stellen heruasfinden(llama index -> reinladen) -> Stellen speichern evtl mit zusätzlichen Informationen anreichern(prompt keine weiterene informationen hinzufügen -> halus verhindern)-> evtl. überflüssig -> nur fragen daraus erstellen und mit einem 2ten model die Antowrten auf die Fragen geben die gemappt in der datenbank speichern(tags, Title, und metadaten vergeben zu den karteikarten) ->  in markdown format ünbertragen 

### 2:
- didaktisch -> Lehrform 
pdf -> openai asssistant -> llm -> in podcast / fragen antwort/ affirmationen(formel wdh. 10 ) 
-> Datein als Stück oder ganz 

## 1 & 2 Strukur:
- abfrage
- natrüclihe Suche meta Daten Podcast Ts, Topic, Tags,  


## MVP:
pdf rein -> karteikartten in markdonw format anki importierbar
pdf rein -> ein Summary als mp4/mp3/wav devices (WIN,IOS,) 


### Vektor Datenbank
Suche  



### Pipeline 
pdf Sharepoint / OPEN Ai REST Assistan für PDf Db -> 



## Prompt engineering 
- beispiel mitgeben 

# Wie kann man Die richtigkeit prüfen antwort Fragne und ob es die wichtigsten stellen sind? 



