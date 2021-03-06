# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20161113151648) do

  create_table "articles", force: :cascade do |t|
    t.string   "title"
    t.text     "text"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer  "x"
    t.integer  "y"
  end

  create_table "goals", force: :cascade do |t|
    t.string   "title"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "news", force: :cascade do |t|
    t.string   "title"
    t.text     "text"
    t.string   "news_name"
    t.string   "news_url"
    t.datetime "news_time"
    t.boolean  "polarity"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "temp_tweets", force: :cascade do |t|
    t.string   "tweet"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "tweets", force: :cascade do |t|
    t.string   "tweet"
    t.boolean  "is_new"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
