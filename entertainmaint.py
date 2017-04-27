import fresh_tomatoes
import media
#list of my favoriate movies
toy_story = media.Movie("Toy Story" , "story about toys" ,"https://en.wikipedia.org/wiki/File:Toy_Story.jpg" , "https://www.youtube.com/watch?v=KYz2wyBy3kc" ) 

avatar = media.Movie ("Avatar" , "Blue Humans" , "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg" ,
"https://www.youtube.com/watch?v=d1_JBMrrYw8")

the_departed = media.Movie ("The Departed" , "Internal Affairs" , "https://en.wikipedia.org/wiki/The_Departed#/media/File:Departed234.jpg" , "https://www.youtube.com/watch?v=auYbpnEwBBg")

inception =media.Movie ("Inception" , "Dream Palace" , "https://en.wikipedia.org/wiki/Inception#/media/File:Inception_(2010)_theatrical_poster.jpg" , "https://www.youtube.com/watch?v=YoHD9XEInc0" )



movies =[toy_story, avatar, the_departed , inception]
fresh_tomatoes.open_movies_page(movies)


