require 'curb'
require 'nokogiri'
require 'csv'

require 'byebug'

puts 'Enter an url please: '
URL = gets.chop
puts 'Enter name of csv file: '
FILE = gets.chop


def get_product_html(url)
	
	c = Curl::Easy.perform(url)

	doc = Nokogiri::HTML.parse(c.body_str)

	html_list = doc.xpath(
		'//a[@class="product_img_link pro_img_hover_scale product-list-category-img"]/@href'
		).map{ |href| href.text}
	return html_list
end


def get_content(html)

	c = Curl.post(html)

	doc = Nokogiri::HTML(c.body)

	result = []
 	full_name = ''
	idx = 0

	product_Weight = doc.xpath('//span[@class="radio_label"]').map { |radio_label| radio_label.text }
	product_Name = doc.xpath('//h1[@class="product_main_name"]').text
	product_Price = doc.xpath('//span[@class="price_comb"]').map { |price_comb| price_comb.text  }
	product_Img = doc.xpath('//img[@id="bigpic"]/@src').to_s

	if product_Weight.empty?
		result.push(
			'Name' => product_Name,
			'Price' => 'Check on site',
			'Img' => product_Img
		)
	else
		product_Weight.each do |weight|
			full_name = product_Name + ' - ' + weight
			price = product_Price[idx]
			result.push(
				'Name' => full_name,
				'Price' => price,
				'Img' => product_Img
			)
			idx = idx + 1
		end
	end
	return result
end


def save_file(filename, arr)
	arr.each do |item|
		if File.exist?(filename)
			CSV.open(filename, 'a') do |csv|
				item.each do |wr|
					csv << wr.values
				end
			end
		else
			CSV.open(filename, 'a', write_headers: true, headers: item.first.keys) do |csv|
				item.each do |wr|
					csv << wr.values
				end
			end
		end
	end
end


def parse
	html = get_product_html(URL)

	result = Array.new
	html.each do |html|
		puts 'Parsing ' + html + '...'
		result.push(get_content(html))
	end
		puts 'Write hash to csv'
		save_file(FILE, result)
		puts 'Done'
end


parse