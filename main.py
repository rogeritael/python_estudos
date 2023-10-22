import os
import platform

class OperatingSystem:
    def __init__(self):
        self.operatingSystem = platform.system()
        self.environment = os.environ
        self.filePath = __file__

    #windows, linux
    def getMyOS(self):
        print(self.operatingSystem)

    #informaçoes do systema operacional
    def getEnvironmentInfos(self):
        print(f'informaçoes do sistema: \n{self.environment}')
        print(f'\nsistema operacional: {self.environment['OS']}')
        print(f'numero de processadores: {self.environment['NUMBER_OF_PROCESSORS']}')

    #pega o id do processo atual que estamos realizando
    def getCurrentTaskProcessId(self):
        processId = os.getpid()
        print(processId)

    #informaçoes do arquivo atual
    def getCurrentPath(self):
        fileName = os.path.basename(self.filePath)
        fileFolder = os.path.dirname(self.filePath)
        absolutePath = os.path.abspath(self.filePath)

        print(f'arquivo atual esta no diretorio: {self.filePath}')
        print(f'nome do arquivo: {fileName}')
        print(f'nome do diretorio do arquivo: {fileFolder}')
        print(f'caminho absoluto do arquivo: {absolutePath}')

    # Listar diretorios
    def folderInfo(self):
        current_dir = os.listdir() #diretorio atual
        dir_files = os.listdir('dir_files/')
        print(f'arquivos do diretorio atual: {current_dir}')
        print(f'arquivos da pasta dir_files: {dir_files}')
    
    # criar pasta
    def createFolder(self, folder_name: str):
        # osUserName = self.environment['USERNAME']
        # os.mkdir(f'C:/Users/{osUserName}/Desktop/{folder_name}') 
        
        #nao consegue criar varias pastas de uma so vez
        os.mkdir(folder_name)

        #cria multiplas pastas
        os.makedirs(f'{folder_name}/{folder_name}/{folder_name}')


    def isFolderAlreadyCreated(self):
        pass




system = OperatingSystem()
system.createFolder('newfolder')