

class Hello
    attr_accessor :name 

    def initialize(name)
        @name = name.capitalize
    end


    def hello
        puts "Hello #{@name}"
    end
end




if __FILE__ == $0

    hello = Hello.new("Mangar")
    hello.hello


    puts hello.name

end