# GitHub Pages supplies its trusted origin and base path through configure-pages.
require 'jekyll'
require 'uri'

origin = ENV.fetch('PAGE_ORIGIN')
uri = URI.parse(origin)
abort 'PAGE_ORIGIN must be an HTTPS origin' unless uri.scheme == 'https' && uri.host && ['', '/'].include?(uri.path)
options = { 'url' => origin.chomp('/'), 'baseurl' => ENV.fetch('PAGE_BASE_PATH', '') }
options['destination'] = ENV['JEKYLL_DESTINATION'] if ENV['JEKYLL_DESTINATION']
Jekyll::Site.new(Jekyll.configuration(options)).process
puts 'Built the Jekyll homepage for GitHub Pages.'
