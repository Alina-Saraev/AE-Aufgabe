import math

def subnetze_berechnen(basis_netz, anzahl_subnetze):
    oktetten = list(map(int, basis_netz.split('.')))
    if len(oktetten) != 4:
        raise ValueError("Bitte geben Sie eine IP-Adresse mit genau vier Oktetten an.")
    if oktetten[3] != 0:
        raise ValueError("Das letzte Oktett muss 0 sein für ein /24 Netz.")

    benoetigte_bits = math.ceil(math.log2(anzahl_subnetze))
    if benoetigte_bits > 8:
        raise ValueError("Zu viele Subnetze")

    neue_subnetz_maske = 24 + benoetigte_bits
    host_bits = 32 - neue_subnetz_maske
    max_hosts = (2 ** host_bits) - 2

    if max_hosts < 2:
        raise ValueError("Zu viele Subnetze, nicht genug Hosts pro Subnetz.")

    inkrement = 2 ** (8 - benoetigte_bits)
    subnetze = []
    for i in range(anzahl_subnetze):
        oktetten[3] = i * inkrement
        subnetze.append('.'.join(map(str, oktetten)))

    return neue_subnetz_maske, max_hosts, subnetze

def bei_berechnen_klicken():
    print('WOOF')
    basis_netz = input('Basisnetz (z. B. 192.168.1.0) > ')
    anzahl_subnetze = int(input('Anzahl der Subnetze > '))

    try:
        neue_subnetz_maske, max_hosts, subnetze = subnetze_berechnen(basis_netz, anzahl_subnetze)
        ergebnis = f"Max. {max_hosts} Hosts adressierbar, Neue Subnetzmaske: 255.255.255.{256 - 2 ** (32 - neue_subnetz_maske)}"
        for i, subnet in enumerate(subnetze):
            ergebnis += f"\n{i + 1}. Netz {subnet}"
        print(ergebnis)
    except ValueError as e:
        print(f"Fehler: {str(e)}")

art = """
                                                .///*.                                                                                                
                                               *///***                                                                                                
                                               #((/(                                                           . ,     #%%%%#                         
                                    #%%%#     (                              (#//(               (%##/      *(******///**.  #*                        
                .%%%%#.  ( //     **#   #%.                                   (***#/*,          /%/  //**/**************/.  //                        
                ## .##///**********/   ./*(                                     ,,,**(*         .%(    /****************%/,(*.                        
                #*   (**************** .(/(                                                      ./( . ******#(**************(*                       
                /* .,******************///                    #                                    (/(/*****************&*/*****,                     
                 ,**&(*******************//(.             .(*((                                   /////******(**#***(, ..////***                      
                  (*************&/******///((             ,,*//                                    #///*********/(   *&/      (                       
                *****%&**//**************//(             /*,/*.                                    ,///////(.        #.    (            **            
               /******( &*&%          (*/#                **/                                            .#.           ,               .*,*#          
                 #*/       ##          *                  *                     .////((.                   ,           (.              .,,//#         
                     ,((,            (*(                                       (/(****                    ,(             ,              /,/#*         
                            /       ,***///(*                                   (*//                     #/**             #               ,,*         
                           ,         *******//////#.                                                   (//*/.            (,                 (         
           ((*           ,.         ,*************/////                                             .(//******#*         /                            
         /**///            (       (*****************///*                                          (//**/****(.        (**#                           
         *////             ///(     .*/****************//*                                       ////***/(*****(     //**/*(                          
          ((              ,**//(      ,**********/******/#   *(***(#(((#(,                      (///*****/(****(     /*(.      .***                   
          *              .**///.((    .******/(*********/#**************(    .(                .///*******//***( */                   .               
                        .**//(  (///(,,*************////(**********(.            (             ////*****/((/*,*********(*         .//                 
                       ***/(   ,,(////(****((******///(**********//                 ,          .///****************(.              /                  
                     (%%%(    *(#(/   #***(  (****//#(////****////****#          #.  (          ,///**************(,*((*,        * .                  
                  (#%%#               #%%#  (##%%(        ,(///////(*    .*((/,..,*//(            (///***///**********(**((.   /                      
                                    #%%%*  ##(                                                      .#////////////////////. #.                        
 """
print(art)
bei_berechnen_klicken()
