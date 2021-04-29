import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.Av004e0hKhiP7K14EcZ1RSSvVU779qp5PKIOteirRZLFebBmDAoSmSl3TppT0Org4wGUhBHEqzr9UJDbQdO-OoGcilgWOEufN1qGrrcN1RwkMIa2VuEB7p1jZFEyVm004SlogQRA'
    transferData = TransferData(access_token)

    file_from =  input("Enter the file path to transfer ")
    file_to = input("Enter the path to upload to dropbox ")

    transferData.upload_files(file_from,file_to)

    print('File has been moved')

main()