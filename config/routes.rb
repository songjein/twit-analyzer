Rails.application.routes.draw do

  root'analyzer#analyzer'
	get 'analyzer/index'
	post 'analyzer/store'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
