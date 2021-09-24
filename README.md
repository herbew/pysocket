# pysocket
python socket
-------------------------------------------------------------------------------
1. APP SERVER SOCKET
-------------------------------------------------------------------------------
- Goto ../python-socket-server/
- Create Image Docker
  docker build -t python-socket-server:0.0.1 .

  REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
  python-socket-server   0.0.1               613e437d3f5f        49 minutes ago      911MB

- RUN App
  docker run -it -v /tmp:/tmp 613e437d3f5f 


- Example:
  connection accepted
  Data Recieved : hallo
  
  Data Recieved : {"id":"one","from":0,"to":5,"fizz":"zzif","buzz":"zzub"}\n    
                  {"id":"two","from":6,"to":10,"fizz":"zzif2","buzz":"zzub2"}\n



-------------------------------------------------------------------------------
2. APP CLIENT SOCKET
-------------------------------------------------------------------------------
- Goto ../python-socket-client/
- Create Image Docker
  docker build -t python-socket-server:0.0.1 

  REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
  python-socket-client   0.0.1               c5cc52a4db73        36 minutes ago      911MB
  
- RUN App
  docker run -it -v /tmp:/tmp c5cc52a4db73 

- Example:
  Send message:hallo
  Response : Not JSON Format

  Send message:{"id":"one","from":0,"to":5,"fizz":"zzif","buzz":"zzub"}\n 
               {"id":"two","from":6,"to":10,"fizz":"zzif2","buzz":"zzub2"}\n
  
  Response : {"one": ["zzifzzub", 1, 2, "zzif", 4], "two": ["zzif2", 7, 8, "zzif2"]}
