class Post < ApplicationRecord
	before_save do
		self.date = Time.now
end
