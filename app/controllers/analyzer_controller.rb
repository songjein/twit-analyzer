class AnalyzerController < ApplicationController
	skip_before_filter  :verify_authenticity_token 

  def index
		require 'open-uri'
		db_url = "http://192.9.81.151:19002/query?query=" + params['query']
		render json: open(db_url).read
  end

	def analyzer
		render :layout => false
	end

	def store
		t = Tweet.new 
		t.tweet = params[:tmp]	
		t.is_new = true
		t.save
		render text: params[:tmp] 
	end

	def get_stream 
			
	end

end
