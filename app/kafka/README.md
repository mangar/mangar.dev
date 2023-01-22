
__Run__

    docker-compose up -d



__Access__


    http://localhost:19000



__Python__


    # Criando um tópico
    
    docker exec kafka-broker kafka-topics --create --topic purchases --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1



