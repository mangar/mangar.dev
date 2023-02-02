

require "kafka"

kafka = Kafka.new(["192.168.1.113:9092"], client_id: "app_01_rb")

msg = '{
	"request_id": "4f72d0bf01a2de7ae95a59637a43f2ab40de1c42f60763cfc2d67fadc3f32614",
	"action": "data_requests_orders_by_user",
	"params": [
		{
			"name": "user_id",
			"value": "451"
		}
	]
}'


kafka.deliver_message(msg, topic: "data_requests")

consumer = kafka.consumer(group_id: "app_01_rb")
consumer.subscribe("data_requests")

consumer.each_message do |message|
    puts "#{message.topic}, #{message.partition}, #{message.offset}, #{message.key}, #{message.value}"
end


# if __FILE__ == $0

#     hello = Hello.new("Mangar")
#     hello.hello


#     puts hello.name

# end