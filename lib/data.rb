attr_reader :doc

def initialize
	file = File.expand_path("wp_posts.xml")
	file = File.open(file)
	doc = Nokogiri::XML(file.read().gsub("\u000g", ""))
end

def posts
	doc.xpath("//item[wp:post_type = 'post']").collect do |post|
		WordPress::Post.new(post)
	end
end


module WordPress
	class Post
		def initialize(doc)
			@doc = doc
		end
		def title
			@doc.xpath("post_title").text
		end
		def content
			@doc.xpath("post_content").text
		end
		def date
			@doc.xpath("post_date").text
		end
	end
end

