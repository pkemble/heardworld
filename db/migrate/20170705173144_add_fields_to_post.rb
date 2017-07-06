class AddFieldsToPost < ActiveRecord::Migration[5.1]
  def change
		add_column :posts, :title, :string
		add_column :posts, :content, :string
		add_column :posts, :date, :datetime
		add_column :posts, :audio, :string
  end
end
