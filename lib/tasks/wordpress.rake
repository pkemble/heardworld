namespace :wordpress do
  desc "import wordpress data"
  task import: :environment do
	data = WordPress::Data.new
	data.posts.each do |data|
		post = Post.new
		post.title = data.title
		post.body = data.content
		post.date = data.date
		post.save!
	end
  end

end
