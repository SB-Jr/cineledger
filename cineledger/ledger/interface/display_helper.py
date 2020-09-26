from ledger.config import console

def show_results(results, mutliple=False, interval=10):
    if not mutliple:
        if len(results) == 1:
            return
        table = console.get_table()
        table.add_column('Index')
        table.add_column('Title')
        table.add_column('Year')
        for i, result in enumerate(results):
            table.add_row(str(i+1), result.title, str(result.year))
        console.print(table)
    else:
        counter = 0
        while True:
            results_trunc = results[counter*interval : (counter+1)*interval]
            show_results(results_trunc)
            cont = get_choice(results_trunc)
            if cont == 'q':
                exit()
            counter +=1


def show_choice(choice, imdb_info):
    console.print('Name: ' + choice.title)
    console.print('Genres: ' + str(imdb_info.get('genres')))
    console.print('Director: '+ imdb_info.get('director')[0].get('name'))
    console.print('Runtime: '+ imdb_info.get('runtimes')[0] + 'min')
    console.print('Year: ' + str(imdb_info.get('year')))
    console.print('IMDb Rating: '+ str(imdb_info.get('rating')))
    console.print('Trakt Rating: ' + str(choice.ratings['rating']))


def get_choice(results):
    if len(results) == 1:
        return results[0]
    else:
        while(True):
            choice_index = input('Enter your choice(q to quit): ')
            if choice_index == 'q':
                exit()
            if not choice_index.isdigit():
                console.print('This is not a number!\nEnter a valid Number....')
                continue
            else:
                choice_index = int(choice_index)
                if choice_index <= len(results) and choice_index > 0:
                    return results[choice_index-1]
                else:
                    console.print('Numer is out of range!! \nPlease enter a number withing the range....')