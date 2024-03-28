from main.app.services.genarateUI_service import  GenrateUiService

def main():

    iface = GenrateUiService.generate_ui()
    iface.launch(share=True)



if __name__ == "__main__":
    
    main()