class CreateTempTweets < ActiveRecord::Migration[5.0]
  def change
    create_table :temp_tweets do |t|
      t.string :tweet

      t.timestamps
    end
  end
end
