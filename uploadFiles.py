import dropbox


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def uploadFile(self, source, destination):
        dbx = dropbox.Dropbox(self.accessToken)
        
        f = open(source,'rb')
        dbx.files_upload(f.read(), destination)

def main():
    accessToken = 'h8RkK3WDzK8AAAAAAAAAAVMyAjp_mhjrhdtaezYEVQVHDcAUDO3qJz_yxfXgzhPD'
    obj = TransferData(accessToken)

    source = input("Enter the file path to transfer ")
    destination = input("Enter the path to upload to dropbox ")
    
    obj.uploadFile( source, destination)

    print("File has been moved successfully")

main()