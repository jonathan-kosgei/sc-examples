require 'sinatra'

get '/hi' do
  return "ciao"
end

run Sinatra::Application