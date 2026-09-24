#!/usr/bin/env ruby
line = ARGV[0]
if line =~ /\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/
  puts "#{$1},#{$2},#{$3}"
end
