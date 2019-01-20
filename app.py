myMovieCollection = []

# Function to Add a New Movie to Collection


def addMovie():
    movieName = input("Movie Name: ")
    movieDirector = input("Director: ")
    movieYear = int(input("Release Year: "))
    myMovie = {
        "name": movieName,
        "director": movieDirector,
        "year": movieYear,
    }
    myMovieCollection.append(myMovie)

# Function to print Movie details


def showMovieDetails(movie):
    print("***************************")
    print(f"Movie Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")
    print("***************************")


# Function to Show all Movies


def showCollection():

    for movie in myMovieCollection:
        showMovieDetails(movie)


# Function to Select the Search the Movie By Name


def searchMovieByName():
    nameInput = input("Movie Name : ")
    for movie in myMovieCollection:
        if movie["name"].lower() == nameInput.lower():
            showMovieDetails(movie)
        else:
            print(f"Movie not in the Collection")

# Function to Select the Search the Movie By Director


def searchMovieByDirector():
    directorInput = input("Director : ")
    for movie in myMovieCollection:
        if movie["director"].lower() == directorInput.lower():
            showMovieDetails(movie)

        else:
            print(f"No {directorInput} movies in the Collection")

# Function to Select the Search the Movie By Release Year


def searchMovieByYear():
    yearInput = int(input("Release Year : "))
    for movie in myMovieCollection:
        if movie["year"] == yearInput:
            showMovieDetails(movie)

        else:
            print(f"No {str(yearInput)} Movies in the Collection")

# Function to Select the Search Cirteria


def searchMovie():
    searchCriteria = input(
        """Search Movie By?\n
        1 - Name\n
        2 - Director\n
        3 - Release Year\n
        0 - Back\n
        Please Confirm your choice: """
    )
    while searchCriteria != "0":
        if searchCriteria == "1":
            searchMovieByName()
        elif searchCriteria == "2":
            searchMovieByDirector()
        elif searchCriteria == "3":
            searchMovieByYear()
        else:
            print("Try Again...")
        searchCriteria = input(
            """Search Movie By?\n
            1 - Name\n
            2 - Director\n
            3 - Release Year\n
            0 - Back\n
            Please Confirm your choice: """
        )
    else:
        print("Back to Main Menu...")


# Main Menu Function


def mainMenu():
    appStart = input(
        """What Do You Want to Do?\n
        1 - Add movie\n
        2 - View Collecton\n
        3 - Search Movie\n
        0 - Quit\n
        Please Confirm your choice: """
    )
    while appStart != "0":
        if appStart == "1":
            addMovie()
        elif appStart == "2":
            showCollection()
        elif appStart == "3":
            searchMovie()
        else:
            print("Try Again...")

        appStart = input(
            """What Do You Want to Do?\n
            1 - Add movie\n
            2 - View Collecton\n
            3 - Find Movie\n
            0 - Quit\n
            Please Confirm your choice: """
        )
    else:
        print("Stopping Program...")


# Main Menu Function Call
mainMenu()
