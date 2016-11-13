class CreateTweets < ActiveRecord::Migration[5.0]
  def change
    create_table :tweets do |t|
      t.string :tweet
      t.boolean :is_new

      t.timestamps
    end
  end
end
