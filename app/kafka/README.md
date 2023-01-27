
__Run__

    docker-compose up -d



__Access__


    http://localhost:19000



__Python__


    # Criando um tópico
    
    docker exec kafka-broker kafka-topics --create --topic purchases --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1




__Kafka UI__


docker run -p 8080:8088 -e KAFKA_CLUSTERS_0_NAME=kafka-broker -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094  --name kafka-ui-aws -d provectuslabs/kafka-ui:latest

b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094




docker run -p 8080:8080 -e KAFKA_CLUSTERS_0_NAME=local -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094 -e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG=software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="PROD"; -d provectuslabs/kafka-ui:latest 



docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-Staging \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="PROD";' \
-d provectuslabs/kafka-ui:latest 




docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-Staging \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_PLAINTEXT \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=PLAIN \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="PROD";' \
-d provectuslabs/kafka-ui:latest 




docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-Staging \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094,b-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:9094 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="PROD";' \
-d provectuslabs/kafka-ui:latest 



docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=ZooKeeper-Staging \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=z-2.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:2181,z-3.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:2181,z-1.as-ue2-stage-kafka.roask3.c2.kafka.us-east-2.amazonaws.com:2181 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="PROD";' \
-d provectuslabs/kafka-ui:latest 







docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-Staging \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098,b-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098,b-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="DEV";' \
-d provectuslabs/kafka-ui:latest 



<!-- AWS: Development Environment -->
<!-- Public endpoint  -->

docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-DEV \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-3-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-2-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198 \
-e KAFKA_CLUSTERS_0_ZOOKEEPER=z-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="DEV";' \
-d provectuslabs/kafka-ui:latest 



docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-DEV \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-3-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-2-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198 \
-e KAFKA_CLUSTERS_0_ZOOKEEPER=z-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
provectuslabs/kafka-ui:latest 




ssh -i '~/.aws/bastion-kafka.pem' ubuntu@ec2-18-191-247-30.us-east-2.compute.amazonaws.com





docker run -p 8080:8080 \
    -e KAFKA_CLUSTERS_0_NAME=local \
    -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-3-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-2-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198 \
    -e KAFKA_CLUSTERS_0_ZOOKEEPER=z-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181 \
    -e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
    -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
    -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
    -e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG=software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="<PROFILE_NAME>"; \
    -d provectuslabs/kafka-ui:latest 




docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-DEV \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-3-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-2-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SASL_SSL \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="DEV";' \
-d provectuslabs/kafka-ui:latest 





KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: "b-1.xyx:9094,b-2.xyc:9094"
KAFKA_CLUSTERS_0_ZOOKEEPER: "z-1.xyvcom:2181,z-2.xyvcom:2181"
KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL: "SSL"



docker run -p 19000:9001 -e KAFKA_BROKERCONNECT: kafka:29092
-d obsidiandynamics/kafdrop:latest

  kafdrop:
    image: obsidiandynamics/kafdrop:latest
    networks: 
      - broker-kafka
    depends_on:
      - kafka
    ports:
      - 19000:9000
    environment:
      KAFKA_BROKERCONNECT: kafka:29092


aws kafka get-bootstrap-brokers --cluster-arn arn:aws:kafka:us-east-2:126270846923:cluster/demo-cluster-1/3810bd20-e2ca-4367-abb6-7785e0ac01bb-3


{
    "BootstrapBrokerStringSaslIam": "b-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098,b-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098,b-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9098",
    "BootstrapBrokerStringPublicSaslIam": "b-3-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-2-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198,b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198"
}



<!--  -->
<!--  -->


ssh -i ~/.ssh/keys/bastion-kafka.pem" ubuntu@18.221.113.252

sudo docker run -p 8080:8080 \
-e KAFKA_CLUSTERS_0_NAME=AWS-DEV \
-e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:9198 \
-e KAFKA_CLUSTERS_0_ZOOKEEPER=z-2.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-1.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181,z-3.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:2181 \
-e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SSL \
provectuslabs/kafka-ui:latest 


-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM=AWS_MSK_IAM \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_CLIENT_CALLBACK_HANDLER_CLASS=software.amazon.msk.auth.iam.IAMClientCallbackHandler \
-e KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG='software.amazon.msk.auth.iam.IAMLoginModule required awsProfileName="DEV";' \
provectuslabs/kafka-ui:latest 



KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: "b-1.xyx:9094,b-2.xyc:9094"
KAFKA_CLUSTERS_0_ZOOKEEPER: "z-1.xyvcom:2181,z-2.xyvcom:2181"
KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL: "SSL"



<!-- Kafdrop -->
<!-- 18.221.113.252:9000 -->
sudo docker run -p 19000:9000 \
-e KAFKA_BROKERCONNECT=b-1-public.democluster1.gzw51k.c3.kafka.us-east-2.amazonaws.com:29092 \
obsidiandynamics/kafdrop:latest

  kafdrop:
    image: obsidiandynamics/kafdrop:latest
    networks: 
      - broker-kafka
    depends_on:
      - kafka
    ports:
      - 19000:9000
    environment:
      KAFKA_BROKERCONNECT: kafka:29092