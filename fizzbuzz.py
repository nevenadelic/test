def fizzbuzz num

    answer = []

    answer.push 'fizz' if num % 3 == 0
    answer.push 'buzz' if num % 5 == 0
    answer.push num if num % 3 != 0 and num % 5 != 0
    
    puts answer.join
end

(1..100).each {|x| fizzbuzz x }