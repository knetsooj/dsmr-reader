��          �      L      �  �   �     �     �     �     �  z   �    U     t  �   �     �     �  �   �  	   K  �   U  �   �  u   �  k     �   p  v  	    z
     �     �     �     �  �   �    o     �  -  �     �     �  �   �     �  �   �  �   o  y     H   �  �   �                                            	   
                                                     By default all DSMR-readings read by of sent to the application are stored indefinitely. DSMR v5 smart meters allow DSMR-readings to be recorded every second, resulting in over 30 million readings each year. DSMR-readings Data affected Data kept/unaffected Electricity Consumption Enabling retention will prevent you from regenerating past day statistics with different prices (due to loss of accuracy). Eventually this **will cause degraded performance** in the application/database and for that reason you might want to apply retention to this data. Please note that enabling this feature will **not discard all readings**, as it will **preserve the first and last reading of each hour**. Gas Consumption Historic data, such as Hour and Day Statistics are unaffected. These are aggregated from the Electricity & Gas Consumption data above. This is also the only data that should matter when you want to look back to a specific day, month or year in the past. How to enable Notes / warnings PostgreSQL does not free up unused disk space immediately. If you've enabled retention for the first time, make sure to run the following command once after a few days:: Retention The admin configuration has a section called "Retention configuration". You can specify whether you want retention at all and set the lifetime of the data being stored. The application will **slowly** apply retention **during night**, cleaning up a maximum of 24 hours worth of data on each backend run executed. The source of all data. It is, however, only read and processed once, so it can be discarded safely after processing. This data type is aggregated from any differences in 'extra device timestamp' occurrences in DSMR-readings. This is aggregated data either created from a single DSMR-reader or a minute worth of DSMR-readings, depending on whether you've enabled grouping. Project-Id-Version: DSMR Reader 1.x
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2018-01-14 12:56+0100
PO-Revision-Date: 2018-01-14 13:02+0100
Last-Translator: 
Language: nl
Language-Team: 
Plural-Forms: nplurals=2; plural=(n != 1);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.5.1
X-Generator: Poedit 1.8.7.1
 Standaard worden alle DSMR-metingen oneindig bewaard. Deze zijn gelezen door (of opgestuurd naar) de applicatie. DSMR v5 slimme meters staan toe dat er elke seconde een meting gedaan wordt, waardoor er tot meer dan 30 miljoen metingen per jaar opgeslagen worden. DSMR-metingen Geraakte gegevens Uitgesloten gegevens Elektriciteitsconsumptie Het inschakelen van retentie heeft als gevolg dat je oude dagstatistieken niet opnieuw kan hergenereren met een andere prijs (door verlies van nauwkeurigheid). Uiteindelijk zorgt dit voor **slechtere performance** in ofwel de applicatie of database. Daarom zul je wellicht retentie willen inschakelen. Let op: Het inschakelen van retentie **gooi niet alle metingen weg**, want **van elk uur wordt de eerste en laatste meting bewaard**. Gasconsumptie Historische gegevens, zoals Dag- en Uurstatistieken worden buiten beschouwing gelaten. Deze gegevens stammen af van bovenstaande consumptie en zijn tevens de enige belangrijke data die er voor de lange termijn toe doen. Bijvoorbeeld wanneer je terug wilt kijken naar een specifieke dag, maand of jaar. Hoe in te schakelen Opmerkingen / waarschuwingen PostgreSQL geeft ongebruikte schijfruimte niet direct vrij. Wanneer je voor het eerst retentie hebt ingeschakeld, zorg er voor dat je na een aantal dagen het volgende ten minste één keer uitvoert:: Retentie Het beheerder-paneel heeft een sectie genaamd "Retentieconfiguratie". Daar kun je aangeven of je überhaupt retentie wilt inschakelen, en zo ja, hoelang data bewaard blijft. Let op: De applicatie zal **langzaam** dataretentie toepassen **tijdens de nacht**, waarbij er telkens maximaal 24 uur aan gegevens wordt opgeschoond. De bron van alle gegevens. Ze worden echter slechts eenmaal ingelezen en kunnen, na verwerking, veilig worden verwijderd. Dit data type is afkomstig van de gasmetergegevens uit de DSMR-metingen. Geaggregeerde gegevens van ofwel een enkele DSMR-meting of een groep van DSMR-metingen, afhankelijk van je groeperingsinstellingen. 