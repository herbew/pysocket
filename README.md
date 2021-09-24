# pysocket
python socket

https://github.com/settings/tokens
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
-------------------------------------------------------------------------------
1. APP SERVER SOCKET
-------------------------------------------------------------------------------
- Goto ../python-socket-server/
- Create Image Docker
  docker build -t python-socket-server:0.0.1 .
  docker build -t python-socket-server:manifest-arm64v8 --build-arg ARCH=arm64v8/ .

  REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
  python-socket-server   0.0.1               aab153020cf1        52 seconds ago      911MB
  python-socket-server   manifest-arm64v8    aab153020cf1        42 minutes ago      911MB

  docker login -u herbew
  password : #!Kevinvania!!23 

  docker tag python-socket-server:0.0.1 herbew/landx:python-socket-server_0.0.1
  docker push herbew/landx:python-socket-server_0.0.1
  
  docker tag python-socket-server:manifest-arm64v8 herbew/landx:python-socket-server_arm64v8
  docker push herbew/landx:python-socket-server_arm64v8
  
  python-socket-server_0.0.1: digest: sha256:55867af39d9c026da34eaa926e9622abc890251085644f29b16736103d364bf6 size: 2425
	
- RUN App
  docker run -it -v /tmp:/tmp aab153020cf1 


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
  docker build -t python-socket-client:manifest-arm64v8 --build-arg ARCH=arm64v8/ .

  REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
  python-socket-client   0.0.1               c5cc52a4db73        36 minutes ago      911MB
  python-socket-client   manifest-arm64v8    c5cc52a4db73        3 hours ago         911MB
  
- RUN App
  docker run -it -v /tmp:/tmp c5cc52a4db73 
  
  docker tag python-socket-client:0.0.1 herbew/landx:python-socket-client_0.0.1
  docker push herbew/landx:python-socket-client_0.0.1

  docker tag python-socket-client:manifest-arm64v8 herbew/landx:python-socket-client_arm64v8
  docker push herbew/landx:python-socket-client_arm64v8

- Example:
  Send message:hallo
  Response : Not JSON Format

  Send message:{"id":"one","from":0,"to":5,"fizz":"zzif","buzz":"zzub"}\n 
               {"id":"two","from":6,"to":10,"fizz":"zzif2","buzz":"zzub2"}\n
  
  Response : {"one": ["zzifzzub", 1, 2, "zzif", 4], "two": ["zzif2", 7, 8, "zzif2"]}
