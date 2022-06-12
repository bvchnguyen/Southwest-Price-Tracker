from pprint import pprint
from pydoc import describe
from turtle import left
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID
from spotify_client import SpotifyClient
from helper_func import genreator_print
from helper_func import inputValidation

# yt = YT_stats(YT_API_KEY, channelID)

def main():
    menuItem = {'Description': '01',
                'Transfer From Youtube': '02',
                'Create a playlist': '03' ,
                'Quit Program': '04'}

    genreator_print.print_welcome(31,8)

    user_ID = input('Enter your spotify username to proceed: ')

    spfy = SpotifyClient(clientId, clientSec, user_ID)

    genreator_print.print_menu(menuItem, 31,8)

    # Validating the menu input
    menu_input = ''
    while (menu_input not in menuItem.values()):
        menu_input= input("Enter the number of the option here: ")
        if menu_input in menuItem.values():        
            if (menu_input == '01'):
                pass
                # print description

            elif (menu_input == '02'):
                # print('Transfering from Youtube...')
                channel_id = input("Enter the channel ID: ")

                yt = YT_stats(YT_API_KEY, channel_id)
                yt.get_channel_id(channel_id)
                yt.get_channel_stats()
                channel_name = yt.get_channel_name()
                print('Extracting song info from', channel_name)
                title_list = yt.get_channel_video_title()
                filtered_title = yt.filter_name(title_list)
                genreator_print.print_list(filtered_title, channel_name, 31, 8)
                
                createPlaylist_YN = input('Make a new playlist to store the returned items?(Y/N): ')
                
                if inputValidation.YN_validation(createPlaylist_YN) == True:
                    spfy.create_playlist()
                else:
                    print('Adding to most recent')
                # yt.get_channel_id(channel_id)

            elif(menu_input == '03'):
                pass
            else:
                print('Quiting program. Goodbye!')
                break
        print('Invalid choice, please try again.')
    # If validation is successful, we move onto sub-menus

if __name__ == '__main__':
    main()