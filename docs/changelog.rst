Changelog
=========


v3.12.0 - 2020-08-08

.. warning::

    This is the last release of DSMR-reader ``v3.x``. New features will only be added to ``v4.x``. See `the v4 upgrade guide <https://dsmr-reader.readthedocs.io/en/v4/faq/v4_upgrade.html>`_ for more information.

.. warning:: **API endpoint deprecation**

    The ``/api/v2/application/status`` endpoint has been deprecated and will be removed in DSMR-reader ``v4.x``,

- [`#1036 <https://github.com/dennissiemensma/dsmr-reader/issues/1036>`_] Deprecate API support for Status
- [`#1037 <https://github.com/dennissiemensma/dsmr-reader/issues/1037>`_] Laatste v3.x release
- [`#1034 <https://github.com/dennissiemensma/dsmr-reader/issues/1034>`_] Live weergave en live teller wijken af


----


v3.11.0 - 2020-06-17

- [`#1009 <https://github.com/dennissiemensma/dsmr-reader/issues/1009>`_] dsmr_stats_recalculate_prices neemt teruglevering niet mee
- [`#1017 <https://github.com/dennissiemensma/dsmr-reader/issues/1017>`_] Updated eCharts to v4.8


----


v3.10.1 - 2020-06-15

- [`#1023 <https://github.com/dennissiemensma/dsmr-reader/issues/1023>`_] Django security update


----


v3.10.0 - 2020-05-29

- [`#996 <https://github.com/dennissiemensma/dsmr-reader/issues/996>`_] Refer HA add-on by Sander de Wildt
- [`#997 <https://github.com/dennissiemensma/dsmr-reader/issues/997>`_] Zoeken naar specifieke dagen in admin
- [`#994 <https://github.com/dennissiemensma/dsmr-reader/issues/994>`_] FAQ bijwerken voor meterwissel
- [`#1001 <https://github.com/dennissiemensma/dsmr-reader/issues/1001>`_] Fixed link in docs - by denniswo
- [`#1002 <https://github.com/dennissiemensma/dsmr-reader/issues/1002>`_] Improve datalogger installation docs


----


v3.9.1 - 2020-05-05

- [`#947 <https://github.com/dennissiemensma/dsmr-reader/issues/947>`_] Standaard zoom live grafieken zelf kunnen instellen


----


v3.9.0 - 2020-05-04

- [`#947 <https://github.com/dennissiemensma/dsmr-reader/issues/947>`_] Tijdsrange live grafieken zelf kunnen instellen
- [`#969 <https://github.com/dennissiemensma/dsmr-reader/issues/969>`_] In- en uitknijpen van de grafieken werkt niet meer
- [`#966 <https://github.com/dennissiemensma/dsmr-reader/issues/966>`_] Error in dsmr_backup_create --compact


----


v3.8.0 - 2020-04-03

- [`#934 <https://github.com/dennissiemensma/dsmr-reader/issues/934>`_] Spelling - by Phyxion
- [`#940 <https://github.com/dennissiemensma/dsmr-reader/issues/940>`_] Postgresql backup is ignoring port setting - by FrankTimmers
- [`#937 <https://github.com/dennissiemensma/dsmr-reader/issues/937>`_] Dashboard €/uur houdt geen rekening met teruglevering
- [`#943 <https://github.com/dennissiemensma/dsmr-reader/issues/943>`_] NonExistentTimeError for DST change in backup module
- [`#930 <https://github.com/dennissiemensma/dsmr-reader/issues/930>`_] Soms afrondingsfout in grafieken-tooltip
- [`#954 <https://github.com/dennissiemensma/dsmr-reader/issues/954>`_] Retention op 3 maanden kunnen zetten
- [`#955 <https://github.com/dennissiemensma/dsmr-reader/issues/955>`_] Resetten van meter statistieken
- [`#953 <https://github.com/dennissiemensma/dsmr-reader/issues/953>`_] Update to Django 3.0.5


----


v3.7.0 - 2020-03-19

- [`#919 <https://github.com/dennissiemensma/dsmr-reader/issues/919>`_] Parsing telegram 3-fasige Fluvius meter faalt
- [`#921 <https://github.com/dennissiemensma/dsmr-reader/issues/921>`_] Notificaties bekijken zonder login
- [`#774 <https://github.com/dennissiemensma/dsmr-reader/issues/774>`_] Retentie omzetten naar geplande taak
- [`#565 <https://github.com/dennissiemensma/dsmr-reader/issues/565>`_] Melding bij onvolledige vergelijking
- [`#923 <https://github.com/dennissiemensma/dsmr-reader/issues/923>`_] Backups compressie level configureerbaar maken
- [`#924 <https://github.com/dennissiemensma/dsmr-reader/issues/924>`_] Dagtotalen herberekenen op basis van uurtotalen


----


v3.6.0 - 2020-03-06

- [`#911 <https://github.com/dennissiemensma/dsmr-reader/issues/911>`_] Weer inzoomen in gas/temperatuur-grafieken
- [`#912 <https://github.com/dennissiemensma/dsmr-reader/issues/912>`_] Layout verbeteren
- [`#916 <https://github.com/dennissiemensma/dsmr-reader/issues/916>`_] Gecombineerd verbruik teruggeven in API's "Retrieve today's consumption"
- [`#875 <https://github.com/dennissiemensma/dsmr-reader/issues/875>`_] Actuele Amperes weergeven via MQTT
- [`#918 <https://github.com/dennissiemensma/dsmr-reader/issues/918>`_] Django 3.0.4 update


----


v3.5.0 - 2020-02-29

- [`#894 <https://github.com/dennissiemensma/dsmr-reader/issues/894>`_] Wijzigingen in datalogger terugdraaien
- [`#891 <https://github.com/dennissiemensma/dsmr-reader/issues/891>`_] Overzichtelijke tussenpagina admin-interface
- [`#875 <https://github.com/dennissiemensma/dsmr-reader/issues/875>`_] Actuele Amperes weergeven
- [`#901 <https://github.com/dennissiemensma/dsmr-reader/issues/901>`_] Layout voor mobiele/kleine schermen verbeteren
- [`#904 <https://github.com/dennissiemensma/dsmr-reader/issues/904>`_] Kleuren van grafieken omgewisseld
- [`#622 <https://github.com/dennissiemensma/dsmr-reader/issues/622>`_] Hoogste/laagste dagtotalen inzien
- [`#902 <https://github.com/dennissiemensma/dsmr-reader/issues/902>`_] Requirements update (February 2020)


----


v3.4.0 - 2020-02-20

- [`#879 <https://github.com/dennissiemensma/dsmr-reader/issues/879>`_] Soms 100% CPU load datalogger
- [`#885 <https://github.com/dennissiemensma/dsmr-reader/issues/885>`_] Herindeling dashboard
- [`#883 <https://github.com/dennissiemensma/dsmr-reader/issues/883>`_] Show electricity usage as stacked bar chart
- [`#858 <https://github.com/dennissiemensma/dsmr-reader/issues/858>`_] Tarieven zelf naamgeven
- [`#878 <https://github.com/dennissiemensma/dsmr-reader/issues/878>`_] Huidig tarief aangeven op het dashboard
- [`#887 <https://github.com/dennissiemensma/dsmr-reader/issues/887>`_] Django-colorfield update


----


v3.3.0 - 2020-02-12


- [`#860 <https://github.com/dennissiemensma/dsmr-reader/issues/860>`_] Gasgrafiek handmatig instellen op staaf of lijn
- [`#862 <https://github.com/dennissiemensma/dsmr-reader/issues/862>`_] Hogere backend process sleep toestaan
- [`#864 <https://github.com/dennissiemensma/dsmr-reader/issues/864>`_] Requirements upgrade (2020-1)
- [`#847 <https://github.com/dennissiemensma/dsmr-reader/issues/847>`_] Datalogger improvements
- [`#869 <https://github.com/dennissiemensma/dsmr-reader/issues/869>`_] Sqlsequencereset versimpelen


----


v3.2.1 - 2020-02-09


- [`#870 <https://github.com/dennissiemensma/dsmr-reader/issues/870>`_]  Django security releases issued: 3.0.3


----


v3.2.0 - 2020-01-31


- [`#841 <https://github.com/dennissiemensma/dsmr-reader/issues/841>`_] Dropbox: Foutafhandeling ongeldig token werkt niet meer
- [`#842 <https://github.com/dennissiemensma/dsmr-reader/issues/841>`_] Gasgrafiek als staafdiagram
- [`#844 <https://github.com/dennissiemensma/dsmr-reader/issues/844>`_] Gas optioneel kunnen groeperen per uur
- [`#854 <https://github.com/dennissiemensma/dsmr-reader/issues/854>`_] Fixed doc version link on status page - by martijnb92


----


v3.1.1 - 2020-01-25

- [`#850 <https://github.com/dennissiemensma/dsmr-reader/issues/850>`_] No matching distribution found for PyCRC==1.21


----


v3.1.0 - 2020-01-18

- [`#836 <https://github.com/dennissiemensma/dsmr-reader/issues/836>`_] Correct background of inactive icons in Archive - by JeanMiK
- [`#828 <https://github.com/dennissiemensma/dsmr-reader/issues/828>`_] Status page displays disabled capabilities
- [`#833 <https://github.com/dennissiemensma/dsmr-reader/issues/833>`_] Mqtt verbindt niet opnieuw na herstart mosquitto
- [`#820 <https://github.com/dennissiemensma/dsmr-reader/issues/820>`_] Meterstatistieken doorgeven via API
- [`#839 <https://github.com/dennissiemensma/dsmr-reader/issues/839>`_] Convert API docs to OpenAPI format
- [`#839 <https://github.com/dennissiemensma/dsmr-reader/issues/839>`_] Deprecated API endpoint `/api/v2/application/status`


----


v3.0.0 - 2020-01-15

.. warning:: **Change in Python support**

  Support for ``Python 3.5`` has been **dropped** due to the Django upgrade (`#735 <https://github.com/dennissiemensma/dsmr-reader/issues/735>`_).

- [`#735 <https://github.com/dennissiemensma/dsmr-reader/issues/735>`_] Drop support for Python 3.5
- [`#734 <https://github.com/dennissiemensma/dsmr-reader/issues/734>`_] Upgrade to Django 3.x
- [`#829 <https://github.com/dennissiemensma/dsmr-reader/issues/829>`_] Several Dutch translation fixes - by mjanssens
- [`#823 <https://github.com/dennissiemensma/dsmr-reader/issues/823>`_] Remove custom configuration in settings.py


----


.. warning::

    This is the last release of DSMR-reader ``v2.x``. New features will only be added to ``v3.x``. See `the v3 upgrade guide <https://dsmr-reader.readthedocs.io/en/v3/faq/v3_upgrade.html>`_ for more information.


v2.15.0 - 2020-01-15


- [`#825 <https://github.com/dennissiemensma/dsmr-reader/issues/825>`_] Last v2.x release


----


v2.14.0 - 2020-01-07

.. note::

    Some configuration options inside ``settings.py`` were relocated or removed from the application. See `the docs <https://dsmr-reader.readthedocs.io/en/latest/settings.html>`_ for the changes.

- [`#822 <https://github.com/dennissiemensma/dsmr-reader/issues/822>`_] Move custom configuration in settings.py to database
- [`#793 <https://github.com/dennissiemensma/dsmr-reader/issues/793>`_] Alle meldingen in 1x sluiten


----


v2.13.0 - 2020-01-05

- [`#819 <https://github.com/dennissiemensma/dsmr-reader/issues/819>`_] Add mail_from option and changed help text - by jbrunink
- [`#730 <https://github.com/dennissiemensma/dsmr-reader/issues/730>`_] Standaard-range dashboard grafieken instelbaar maken
- [`#818 <https://github.com/dennissiemensma/dsmr-reader/issues/818>`_] Dataverwerking loopt achter bij wisselen naar woning zonder gasmeter


----


v2.12.1 - 2019-12-19

- [`#780 <https://github.com/dennissiemensma/dsmr-reader/issues/780>`_] REVERTED: Backup direct comprimeren


----


v2.12.0 - 2019-12-17

- [`#761 <https://github.com/dennissiemensma/dsmr-reader/issues/761>`_] Home Assistant automatische integratie - by depl0y
- [`#784 <https://github.com/dennissiemensma/dsmr-reader/issues/784>`_] Unpin requirements patches
- [`#780 <https://github.com/dennissiemensma/dsmr-reader/issues/780>`_] Backup direct comprimeren
- [`#790 <https://github.com/dennissiemensma/dsmr-reader/issues/790>`_] Updated graph library


----


v2.11.3 - 2019-12-08

- [`#794 <https://github.com/dennissiemensma/dsmr-reader/issues/794>`_] Django security releases issued: 2.2.8


----


v2.11.2 - 2019-11-13

- [`#783 <https://github.com/dennissiemensma/dsmr-reader/issues/783>`_] Gunicorn 20.x breaks use of docker Alpine Linux


----


v2.11.1 - 2019-11-12

- [`#782 <https://github.com/dennissiemensma/dsmr-reader/issues/782>`_] Failed to export to MinderGas: Unexpected status code received


----


v2.11.0 - 2019-11-09

- [`#774 <https://github.com/dennissiemensma/dsmr-reader/issues/774>`_] Generic performance improvements
- [`#776 <https://github.com/dennissiemensma/dsmr-reader/issues/776>`_] Meerdere foutmeldingen Buienradar API
- [`#777 <https://github.com/dennissiemensma/dsmr-reader/issues/777>`_] Requirements update (November 2019)
- [`#778 <https://github.com/dennissiemensma/dsmr-reader/issues/778>`_] Gas-metingen werken niet bij meerdere apparaten op m-bus


----


v2.10.0 - 2019-11-05

- [`#766 <https://github.com/dennissiemensma/dsmr-reader/issues/766>`_] (1/2) Uurstatistieken missen de laatste minuut of seconde - by JeanMiK
- [`#766 <https://github.com/dennissiemensma/dsmr-reader/issues/766>`_] (2/2) Verkeerd aantal uren per dag bij wisseling zomertijd/wintertijd - by JeanMiK
- [`#765 <https://github.com/dennissiemensma/dsmr-reader/issues/765>`_] Requirements update (November 2019)
- [`#750 <https://github.com/dennissiemensma/dsmr-reader/issues/750>`_] Piek- en dalmetingen omgedraaid (Belgische slimme meter)
- [`#764 <https://github.com/dennissiemensma/dsmr-reader/issues/764>`_] Dataverwerking loopt achter


----


v2.9.0 - 2019-10-25

- [`#755 <https://github.com/dennissiemensma/dsmr-reader/issues/755>`_] Buienradar API bron/foutafhandeling verbeteren
- [`#752 <https://github.com/dennissiemensma/dsmr-reader/issues/752>`_] Configurable plugins by environmental variables - by jorkzijlstra
- [`#743 <https://github.com/dennissiemensma/dsmr-reader/issues/743>`_] Nginx: Sites-available gebruiken
- [`#757 <https://github.com/dennissiemensma/dsmr-reader/issues/757>`_] Retentie op elk moment van de dag doorvoeren


----


v2.7.0 - 2019-10-10

- [`#733 <https://github.com/dennissiemensma/dsmr-reader/issues/733>`_] Fixed weird field formatting for MQTT
- [`#736 <https://github.com/dennissiemensma/dsmr-reader/issues/736>`_] Requirements upgrade (October 2019)
- [`#637 <https://github.com/dennissiemensma/dsmr-reader/issues/637>`_] Live gas gebruik via MQTT


----


v2.6.0 - 2019-10-07

- [`#718 <https://github.com/dennissiemensma/dsmr-reader/issues/718>`_] Improve docs for restoring backups
- [`#543 <https://github.com/dennissiemensma/dsmr-reader/issues/543>`_] MQTT alleen starten wanneer nodig
- [`#723 <https://github.com/dennissiemensma/dsmr-reader/issues/723>`_] MQTT-waardes cachen
- [`#581 <https://github.com/dennissiemensma/dsmr-reader/issues/581>`_] Voltages via MQTT
- [`#584 <https://github.com/dennissiemensma/dsmr-reader/issues/584>`_] Foutmeldingen tonen in interface
- [`#726 <https://github.com/dennissiemensma/dsmr-reader/issues/726>`_] Requirements update (October 2019)
- [`#615 <https://github.com/dennissiemensma/dsmr-reader/issues/615>`_] Dagstatistieken voor DSMR-v5 eerder genereren


----


v2.5.0 - 2019-10-01

- [`#717 <https://github.com/dennissiemensma/dsmr-reader/issues/717>`_] Fixed the accuracy of rounding prices
- [`#518 <https://github.com/dennissiemensma/dsmr-reader/issues/518>`_] Aflezen gegevens over voltages
- [`#722 <https://github.com/dennissiemensma/dsmr-reader/issues/722>`_] Minimale backup (sinds v2.3.0) laat processen stoppen bij MySQL gebruikers


----


v2.4.0 - 2019-09-19

- [`#699 <https://github.com/dennissiemensma/dsmr-reader/issues/699>`_] Hergenereren dagtotalen verbeteren
- [`#625 <https://github.com/dennissiemensma/dsmr-reader/issues/625>`_] Meter statistieken weergeven wanneer leeg
- [`#710 <https://github.com/dennissiemensma/dsmr-reader/issues/710>`_] Waarschuwingen risico's SD-kaartjes
- [`#712 <https://github.com/dennissiemensma/dsmr-reader/issues/712>`_] Requirements update (September 2019)
- [`#711 <https://github.com/dennissiemensma/dsmr-reader/issues/711>`_] Check backup exit codes


----


v2.3.0 - 2019-09-03

- [`#681 <https://github.com/dennissiemensma/dsmr-reader/issues/681>`_] Refactoring backups: improved/simplified Dropbox sync, added extra minimal backup
- [`#638 <https://github.com/dennissiemensma/dsmr-reader/issues/638>`_] Dropbox / back-up sync per direct kunnen resetten
- [`#682 <https://github.com/dennissiemensma/dsmr-reader/issues/682>`_] Updated help text for tracking phases
- [`#696 <https://github.com/dennissiemensma/dsmr-reader/issues/696>`_] API-docs broke after upgrade
- [`#697 <https://github.com/dennissiemensma/dsmr-reader/issues/697>`_] Gas wordt niet verwerkt uit telegram bij digitale meters in België - by floyson-reference
- [`#693 <https://github.com/dennissiemensma/dsmr-reader/issues/693>`_] Check backup creation path
- [`#702 <https://github.com/dennissiemensma/dsmr-reader/issues/702>`_] MQTT-berichten stapelen zich op zonder MQTT-proces


----


v2.2.3 - 2019-08-04

- [`#679 <https://github.com/dennissiemensma/dsmr-reader/issues/679>`_] Django 2.2.4 released


----


v2.2.2 - 2019-08-02

- [`#667 <https://github.com/dennissiemensma/dsmr-reader/issues/667>`_] Add default value(s) for PORT - by xirixiz
- [`#672 <https://github.com/dennissiemensma/dsmr-reader/issues/672>`_] Requirements update (July 2019)
- [`#674 <https://github.com/dennissiemensma/dsmr-reader/issues/674>`_] Use CircleCI for tests


----


v2.2.1 - 2019-07-03

- [`#665 <https://github.com/dennissiemensma/dsmr-reader/issues/665>`_] Django security releases issued: 2.2.3
- [`#660 <https://github.com/dennissiemensma/dsmr-reader/issues/660>`_] Add a timeout to the datalogger web request - by Helmo


----


v2.2.0 - 2019-06-14

- [`#647 <https://github.com/dennissiemensma/dsmr-reader/issues/647>`_] Fix for retroactivily inserting reading data - by drvdijk
- [`#646 <https://github.com/dennissiemensma/dsmr-reader/issues/646>`_] Inladen oude gegevens gaat mis met live gas consumption
- [`#652 <https://github.com/dennissiemensma/dsmr-reader/issues/652>`_] Django security releases issued: 2.2.2


----


v2.1.0 - 2019-05-20

- [`#635 <https://github.com/dennissiemensma/dsmr-reader/issues/635>`_] Requirements update (May 2019)
- [`#518 <https://github.com/dennissiemensma/dsmr-reader/issues/518>`_] Aflezen telegram in GUI
- [`#574 <https://github.com/dennissiemensma/dsmr-reader/issues/574>`_] Add Telegram notification support - by thommy101
- [`#562 <https://github.com/dennissiemensma/dsmr-reader/issues/562>`_] API voor live gas verbruik
- [`#555 <https://github.com/dennissiemensma/dsmr-reader/issues/555>`_] Ondersteuning voor back-up per e-mail
- [`#613 <https://github.com/dennissiemensma/dsmr-reader/issues/613>`_] Eenduidige tijdzones voor back-ups in Docker
- [`#606 <https://github.com/dennissiemensma/dsmr-reader/issues/606>`_] Authenticatie API browser

----


v2.0.2 - 2019-04-19


- [`#620 <https://github.com/dennissiemensma/dsmr-reader/issues/620>`_] CVE-2019-11324 (urllib3)


----


v2.0.1 - 2019-04-19


- [`#619 <https://github.com/dennissiemensma/dsmr-reader/issues/619>`_] Add missing API calls in documentation


----


v2.0.0 - 2019-04-16

.. warning:: **Change in Python support** 

  - The support for ``Python 3.4`` has been **dropped** due to the Django upgrade (`#512 <https://github.com/dennissiemensma/dsmr-reader/issues/512>`_).


- [`#512 <https://github.com/dennissiemensma/dsmr-reader/issues/512>`_] Drop support for Python 3.4
- [`#510 <https://github.com/dennissiemensma/dsmr-reader/issues/510>`_] Django 2.1 released
- [`#616 <https://github.com/dennissiemensma/dsmr-reader/issues/616>`_] Requirements update (April 2019)
- [`#596 <https://github.com/dennissiemensma/dsmr-reader/issues/596>`_] Update django to 2.0.13 - by Timdebruijn
- [`#580 <https://github.com/dennissiemensma/dsmr-reader/issues/580>`_] Django security releases issued: 2.0.10 - by mjanssens


----


v1.28.0 - 2019-01-04

.. note::

	This will be the last release for a few months until spring 2019.

- [`#571 <https://github.com/dennissiemensma/dsmr-reader/issues/571>`_] Trends klok omdraaien
- [`#570 <https://github.com/dennissiemensma/dsmr-reader/issues/570>`_] Herinstallatie/verwijdering documenteren
- [`#442 <https://github.com/dennissiemensma/dsmr-reader/issues/442>`_] Documentation: Development environment
- Requirements update


----


v1.27.0 - 2018-12-23

- [`#557 <https://github.com/dennissiemensma/dsmr-reader/issues/557>`_] Plugin/hook voor doorsturen telegrammen
- [`#560 <https://github.com/dennissiemensma/dsmr-reader/issues/560>`_] Added boundaryGap to improve charts - by jbrunink / Tijs van Noije
- [`#561 <https://github.com/dennissiemensma/dsmr-reader/issues/561>`_] Arrows on status page will now be hidden on small screens where they don't make sense anymore - by jbrunink
- [`#426 <https://github.com/dennissiemensma/dsmr-reader/issues/426>`_] Temperatuurmetingen per uur inzichtelijk als CSV
- [`#558 <https://github.com/dennissiemensma/dsmr-reader/issues/558>`_] Custom backup storage location


----


v1.26.1 - 2018-10-31

- [`#545 <https://github.com/dennissiemensma/dsmr-reader/issues/545>`_] Requirements update (October 2018)


----


v1.26.0 - 2018-10-28

- [`#541 <https://github.com/dennissiemensma/dsmr-reader/issues/541>`_] AmbiguousTimeError causes excessive notifications
- [`#535 <https://github.com/dennissiemensma/dsmr-reader/issues/535>`_] "All time low" implementeren
- [`#536 <https://github.com/dennissiemensma/dsmr-reader/issues/536>`_] Retentie-verbeteringen


----


v1.25.1 - 2018-10-22

- [`#537 <https://github.com/dennissiemensma/dsmr-reader/issues/537>`_] Fix screenshot urls - by pyrocumulus


----


v1.25.0 - 2018-10-18

- [`#514 <https://github.com/dennissiemensma/dsmr-reader/issues/514>`_] Fixed a Javascript bug in Archive and Compare pages, causing the selection to glitch
- [`#527 <https://github.com/dennissiemensma/dsmr-reader/issues/527>`_] Docker DSMR Datalogger - by trizz
- [`#533 <https://github.com/dennissiemensma/dsmr-reader/issues/533>`_] General English language fixes - by Oliver Payne
- [`#514 <https://github.com/dennissiemensma/dsmr-reader/issues/514>`_] Convert Archive page to eCharts
- [`#514 <https://github.com/dennissiemensma/dsmr-reader/issues/514>`_] Simplified Compare page
- [`#526 <https://github.com/dennissiemensma/dsmr-reader/issues/526>`_] Logging refactoring (datalogger)
- [`#523 <https://github.com/dennissiemensma/dsmr-reader/issues/523>`_] Automatische gas consumption dashboard
- [`#532 <https://github.com/dennissiemensma/dsmr-reader/issues/532>`_] Update documentation (complete overhaul)


----


v1.24.0 - 2018-09-29

.. warning::

    The default logging level of the backend has been lowered to reduce I/O.
    See ``Logging`` on `this documentation page <https://dsmr-reader.readthedocs.io/nl/v2/troubleshooting.html>`_ for more information.

- [`#494 <https://github.com/dennissiemensma/dsmr-reader/issues/494>`_] Extend Usage statistics to include return
- [`#467 <https://github.com/dennissiemensma/dsmr-reader/issues/467>`_] PVO uploadtijden in sync houden
- [`#513 <https://github.com/dennissiemensma/dsmr-reader/issues/513>`_] Data being ignored in telegram grouping
- [`#514 <https://github.com/dennissiemensma/dsmr-reader/issues/514>`_] Convert archive & comparison pages to eCharts
- [`#512 <https://github.com/dennissiemensma/dsmr-reader/issues/512>`_] Drop support for Python 3.4
- [`#511 <https://github.com/dennissiemensma/dsmr-reader/issues/511>`_] Add support for Python 3.7
- [`#526 <https://github.com/dennissiemensma/dsmr-reader/issues/526>`_] Logging refactoring (backend)


----


v1.23.1 - 2018-08-26

- [`#515 <https://github.com/dennissiemensma/dsmr-reader/issues/515>`_] Missing mqtt values


----


v1.23.1 - 2018-08-26

- [`#515 <https://github.com/dennissiemensma/dsmr-reader/issues/515>`_] Missing mqtt values


----


v1.23.1 - 2018-08-26

- [`#515 <https://github.com/dennissiemensma/dsmr-reader/issues/515>`_] Missing mqtt values


----


v1.23.0 - 2018-08-02

.. warning::

    Support for **MQTT** has been completely reworked in this release and now **requires** a new ``dsmr_mqtt`` process in Supervisor.
    `Additional steps for upgrading can be found here <https://dsmr-reader.readthedocs.io/en/v3/faq.html#how-do-i-retain-mqtt-support-when-upgrading-to-v1-23-0-or-higher>`_.

- [`#509 <https://github.com/dennissiemensma/dsmr-reader/issues/509>`_] MQTT refactoring
- [`#417 <https://github.com/dennissiemensma/dsmr-reader/issues/417>`_] --- MQTT does connect/publish/disconnect for EACH message - every second
- [`#505 <https://github.com/dennissiemensma/dsmr-reader/issues/505>`_] --- SSL/TLS support for MQTT
- [`#481 <https://github.com/dennissiemensma/dsmr-reader/issues/481>`_] --- Memory Leak in dsmr_datalogger / MQTT
- [`#463 <https://github.com/dennissiemensma/dsmr-reader/issues/463>`_] MQTT: Telegram als JSON, tijdzones
- [`#508 <https://github.com/dennissiemensma/dsmr-reader/issues/508>`_] Trend-grafiek kan niet gegenereerd worden
- [`#292 <https://github.com/dennissiemensma/dsmr-reader/issues/292>`_] Statuspagina: onderdelen 'backup' en 'mindergas upload' toevoegen
- [`#499 <https://github.com/dennissiemensma/dsmr-reader/issues/499>`_] Upgrade Font Awesome to v5


----


v1.22.1 - 2018-07-22

- [`#506 <https://github.com/dennissiemensma/dsmr-reader/issues/506>`_] Fasen-grafiek hangt op 'loading'


----


v1.22.0 - 2018-07-22

- [`#296 <https://github.com/dennissiemensma/dsmr-reader/issues/296>`_] 3 fasen teruglevering
- [`#501 <https://github.com/dennissiemensma/dsmr-reader/issues/501>`_] Lijn grafiek bij geen teruglevering
- [`#495 <https://github.com/dennissiemensma/dsmr-reader/issues/495>`_] Update documentation screenshots
- [`#498 <https://github.com/dennissiemensma/dsmr-reader/issues/498>`_] Frontend improvements
- [`#493 <https://github.com/dennissiemensma/dsmr-reader/issues/493>`_] Requirements update (July 2018)


----


v1.21.1 - 2018-07-16

- [`#492 <https://github.com/dennissiemensma/dsmr-reader/issues/492>`_] Fixed some issues with eCharts (improvements)
- [`#497 <https://github.com/dennissiemensma/dsmr-reader/issues/497>`_] Kleinigheidje: missende vertalingen


----


v1.21.0 - 2018-07-11

- [`#489 <https://github.com/dennissiemensma/dsmr-reader/issues/489>`_] eCharts improved graphs for data zooming/scrolling
- [`#434 <https://github.com/dennissiemensma/dsmr-reader/issues/434>`_] Omit gas readings all together
- [`#264 <https://github.com/dennissiemensma/dsmr-reader/issues/264>`_] Check Dropbox API token and display error messages in GUI


----


v1.20.0 - 2018-07-04

- [`#484 <https://github.com/dennissiemensma/dsmr-reader/issues/484>`_] API call om huidige versie terug te geven
- [`#291 <https://github.com/dennissiemensma/dsmr-reader/issues/291>`_] API option to get status info
- [`#485 <https://github.com/dennissiemensma/dsmr-reader/issues/485>`_] Retrieve the current energycontract for the statistics page - helmo
- [`#486 <https://github.com/dennissiemensma/dsmr-reader/issues/486>`_] Plugin documentation
- [`#487 <https://github.com/dennissiemensma/dsmr-reader/issues/487>`_] Requirements update (July 2018)


----


v1.19.0 - 2018-06-12

- [`#390 <https://github.com/dennissiemensma/dsmr-reader/issues/390>`_] Gas- en elektriciteitsverbruik vanaf start energie contract
- [`#482 <https://github.com/dennissiemensma/dsmr-reader/issues/482>`_] Aantal items op X-as in dashboardgrafiek variabel maken
- [`#407 <https://github.com/dennissiemensma/dsmr-reader/issues/407>`_] Plugin System (More than one pvoutput account) 
- [`#462 <https://github.com/dennissiemensma/dsmr-reader/issues/462>`_] Get live usage trough API


----


v1.18.0 - 2018-06-05

- [`#246 <https://github.com/dennissiemensma/dsmr-reader/issues/246>`_] Add support for Pushover
- [`#479 <https://github.com/dennissiemensma/dsmr-reader/issues/479>`_] Tijdsnotatie grafieken gelijktrekken
- [`#480 <https://github.com/dennissiemensma/dsmr-reader/issues/480>`_] Requirements update (June 2018) 


----


v1.17.0 - 2018-05-25

- [`#475 <https://github.com/dennissiemensma/dsmr-reader/issues/475>`_] Notify my android service ended
- [`#471 <https://github.com/dennissiemensma/dsmr-reader/issues/471>`_] Requirements update (May 2018)


----


v1.16.0 - 2018-04-04

- [`#458 <https://github.com/dennissiemensma/dsmr-reader/issues/458>`_] DSMR v2.x parse-fout - by mrvanes 
- [`#455 <https://github.com/dennissiemensma/dsmr-reader/issues/455>`_] DOCS: Handleiding Nginx authenticatie uitbreiden - by FutureCow 
- [`#461 <https://github.com/dennissiemensma/dsmr-reader/issues/461>`_] Requirements update April 2018
- Fixed some missing names on the contribution page in the DOCS


----


v1.15.0 - 2018-03-21

- [`#449 <https://github.com/dennissiemensma/dsmr-reader/issues/449>`_] Meterstatistieken via MQTT beschikbaar
- [`#208 <https://github.com/dennissiemensma/dsmr-reader/issues/208>`_] Notificatie bij uitblijven gegevens uit slimme meter
- [`#342 <https://github.com/dennissiemensma/dsmr-reader/issues/342>`_] Backup to dropbox never finish (free plan no more space)


----


v1.14.0 - 2018-03-11

- [`#441 <https://github.com/dennissiemensma/dsmr-reader/issues/441>`_] PVOutput exports schedulen naar ingestelde upload interval - by pyrocumulus
- [`#436 <https://github.com/dennissiemensma/dsmr-reader/issues/436>`_] Update docs: authentication method for public webinterface
- [`#449 <https://github.com/dennissiemensma/dsmr-reader/issues/449>`_] Meterstatistieken via MQTT beschikbaar
- [`#445 <https://github.com/dennissiemensma/dsmr-reader/issues/445>`_] Upload/export to PVoutput doesn't work
- [`#432 <https://github.com/dennissiemensma/dsmr-reader/issues/432>`_] [API] Gas cost missing at start of day 
- [`#367 <https://github.com/dennissiemensma/dsmr-reader/issues/367>`_] Dagverbruik en teruglevering via MQTT
- [`#447 <https://github.com/dennissiemensma/dsmr-reader/issues/447>`_] Kosten via MQTT


----


v1.13.2 - 2018-02-02

- [`#431 <https://github.com/dennissiemensma/dsmr-reader/issues/431>`_] Django security releases issued: 2.0.2


----


v1.13.1 - 2018-01-28

- [`#428 <https://github.com/dennissiemensma/dsmr-reader/issues/428>`_] Django 2.0: Null characters are not allowed in telegram (esp8266)


----


v1.13.0 - 2018-01-23

- [`#203 <https://github.com/dennissiemensma/dsmr-reader/issues/203>`_] One-click installer
- [`#396 <https://github.com/dennissiemensma/dsmr-reader/issues/396>`_] Gecombineerd tarief tonen op 'Statistieken'-pagina
- [`#268 <https://github.com/dennissiemensma/dsmr-reader/issues/268>`_] Data preservation/backups - by WatskeBart
- [`#425 <https://github.com/dennissiemensma/dsmr-reader/issues/425>`_] Requests for donating a beer or coffee
- [`#427 <https://github.com/dennissiemensma/dsmr-reader/issues/427>`_] Reconnect to postgresql
- [`#394 <https://github.com/dennissiemensma/dsmr-reader/issues/394>`_] Django 2.0 

----


v1.12.0 - 2018-01-14

- [`#72 <https://github.com/dennissiemensma/dsmr-reader/issues/72>`_] Source data retention
- [`#414 <https://github.com/dennissiemensma/dsmr-reader/issues/414>`_] add systemd service files - by meijjaa
- [`#405 <https://github.com/dennissiemensma/dsmr-reader/issues/405>`_] More updates to the Dutch translation of the documentation - by lckarssen
- [`#404 <https://github.com/dennissiemensma/dsmr-reader/issues/404>`_] Fix minor typo in Dutch translation - by lckarssen
- [`#398 <https://github.com/dennissiemensma/dsmr-reader/issues/398>`_] iOS Web App: prevent same-window links from being opened externally - by Joris Vervuurt
- [`#399 <https://github.com/dennissiemensma/dsmr-reader/issues/399>`_] Veel calls naar api.buienradar
- [`#406 <https://github.com/dennissiemensma/dsmr-reader/issues/406>`_] Spelling correction trends page
- [`#413 <https://github.com/dennissiemensma/dsmr-reader/issues/413>`_] Hoge CPU belasting op rpi 2 icm DSMR 5.0 meter
- [`#419 <https://github.com/dennissiemensma/dsmr-reader/issues/419>`_] Requirements update (January 2018)


----


v1.11.0 - 2017-11-24

- [`#382 <https://github.com/dennissiemensma/dsmr-reader/issues/382>`_] Archief klopt niet
- [`#385 <https://github.com/dennissiemensma/dsmr-reader/issues/385>`_] Ververs dagverbruik op dashboard automatisch - by HugoDaBosss
- [`#387 <https://github.com/dennissiemensma/dsmr-reader/issues/387>`_] There are too many unprocessed telegrams - by HugoDaBosss
- [`#368 <https://github.com/dennissiemensma/dsmr-reader/issues/368>`_] Gebruik van os.environ.get - by ju5t
- [`#370 <https://github.com/dennissiemensma/dsmr-reader/issues/370>`_] Pvoutput upload zonder teruglevering
- [`#371 <https://github.com/dennissiemensma/dsmr-reader/issues/371>`_] fonts via https laden
- [`#378 <https://github.com/dennissiemensma/dsmr-reader/issues/378>`_] Processing of telegrams stalled


----


v1.10.0 - 2017-10-19

.. note::

   This releases turns telegram logging **off by default**.


----

- [`#363 <https://github.com/dennissiemensma/dsmr-reader/issues/363>`_] Show electricity_merged in the Total row for current month - by helmo
- [`#305 <https://github.com/dennissiemensma/dsmr-reader/issues/305>`_] Trend staafdiagrammen afgelopen week / afgelopen maand altijd gelijk
- [`#194 <https://github.com/dennissiemensma/dsmr-reader/issues/194>`_] Add timestamp to highest and lowest Watt occurance
- [`#365 <https://github.com/dennissiemensma/dsmr-reader/issues/365>`_] Turn telegram logging off by default
- [`#366 <https://github.com/dennissiemensma/dsmr-reader/issues/366>`_] Restructure docs


----


v1.9.0 - 2017-10-08

.. note::

    This release contains an update for the API framework, which `has a fix for some timezone issues <https://github.com/encode/django-rest-framework/issues/3732>`_.
    You may experience different output regarding to datetime formatting when using the API.

- [`#9 <https://github.com/dennissiemensma/dsmr-reader/issues/9>`_] Data export: PVOutput
- [`#163 <https://github.com/dennissiemensma/dsmr-reader/issues/163>`_] Allow separate prices/costs for electricity returned
- [`#337 <https://github.com/dennissiemensma/dsmr-reader/issues/337>`_] API mogelijkheid voor ophalen 'dashboard' waarden
- [`#284 <https://github.com/dennissiemensma/dsmr-reader/issues/284>`_] Automatische backups geven alleen lege bestanden
- [`#279 <https://github.com/dennissiemensma/dsmr-reader/issues/279>`_] Weather report with temperature '-' eventually results in stopped dsmr_backend
- [`#245 <https://github.com/dennissiemensma/dsmr-reader/issues/245>`_] Grafiek gasverbruik doet wat vreemd na aantal uur geen nieuwe data
- [`#272 <https://github.com/dennissiemensma/dsmr-reader/issues/272>`_] Dashboard - weergave huidig verbruik bij smalle weergave
- [`#273 <https://github.com/dennissiemensma/dsmr-reader/issues/273>`_] Docker (by xirixiz) reference in docs
- [`#286 <https://github.com/dennissiemensma/dsmr-reader/issues/286>`_] Na gebruik admin-pagina's geen (eenvoudige) mogelijkheid voor terugkeren naar de site
- [`#332 <https://github.com/dennissiemensma/dsmr-reader/issues/332>`_] Launch full screen on iOS device when opening from homescreen
- [`#276 <https://github.com/dennissiemensma/dsmr-reader/issues/276>`_] Display error compare page on mobile
- [`#288 <https://github.com/dennissiemensma/dsmr-reader/issues/288>`_] Add info to FAQ
- [`#320 <https://github.com/dennissiemensma/dsmr-reader/issues/320>`_] auto refresh op statussen op statuspagina
- [`#314 <https://github.com/dennissiemensma/dsmr-reader/issues/314>`_] Add web-applicatie mogelijkheid ala pihole
- [`#358 <https://github.com/dennissiemensma/dsmr-reader/issues/358>`_] Requirements update (September 2017)
- [`#270 <https://github.com/dennissiemensma/dsmr-reader/issues/270>`_] Public Webinterface Warning (readthedocs.io)
- [`#231 <https://github.com/dennissiemensma/dsmr-reader/issues/231>`_] Contributors update
- [`#300 <https://github.com/dennissiemensma/dsmr-reader/issues/300>`_] Upgrade to Django 1.11 LTS
 

----


v1.8.2 - 2017-08-12

- [`#346 <https://github.com/dennissiemensma/dsmr-reader/issues/346>`_] Defer statistics page XHR 


----


v1.8.1 - 2017-07-04

- [`#339 <https://github.com/dennissiemensma/dsmr-reader/issues/339>`_] Upgrade Dropbox-client to v8.x 


----


v1.8.0 - 2017-06-14

- [`#141 <https://github.com/dennissiemensma/dsmr-reader/issues/141>`_] Add MQTT support to publish readings
- [`#331 <https://github.com/dennissiemensma/dsmr-reader/issues/331>`_] Requirements update (June 2016)
- [`#299 <https://github.com/dennissiemensma/dsmr-reader/issues/299>`_] Support Python 3.6


----


v1.7.0 - 2017-05-04

.. warning::

    Please note that the ``dsmr_datalogger.0007_dsmrreading_timestamp_index`` migration **will take quite some time**, as it adds an index on one of the largest database tables!
    
    It takes **around two minutes** on a RaspberryPi 2 & 3 with ``> 4.3 million`` readings on PostgreSQL. Results may differ on **slower RaspberryPi's** or **with MySQL**.


.. note::

    The API-docs for the new v2 API `can be found here <https://dsmr-reader.readthedocs.io/en/v2/api.html>`_.

- [`#230 <https://github.com/dennissiemensma/dsmr-reader/issues/230>`_] Support for exporting data via API


----


v1.6.2 - 2017-04-23

- [`#269 <https://github.com/dennissiemensma/dsmr-reader/issues/269>`_] x-as gasgrafiek geeft rare waarden aan
- [`#303 <https://github.com/dennissiemensma/dsmr-reader/issues/303>`_] Archive page's default day sorting


----


v1.6.1 - 2017-04-06

- [`#298 <https://github.com/dennissiemensma/dsmr-reader/issues/298>`_] Update requirements (Django 1.10.7)


----


v1.6.0 - 2017-03-18

.. warning::

    Support for ``MySQL`` has been **deprecated** since ``DSMR-reader v1.6`` and will be discontinued completely in a later release.
    Please use a PostgreSQL database instead. Users already running MySQL will be supported in easily migrating to PostgreSQL in the future.

.. note::

    **Change in API:**
    The telegram creation API now returns an ``HTTP 201`` response when successful.
    An ``HTTP 200`` was returned in former versions.
    :doc:`View API docs<api>`.

- [`#221 <https://github.com/dennissiemensma/dsmr-reader/issues/221>`_] Support for DSMR-firmware v5.0.
- [`#237 <https://github.com/dennissiemensma/dsmr-reader/issues/237>`_] Redesign: Status page.
- [`#249 <https://github.com/dennissiemensma/dsmr-reader/issues/249>`_] Req: Add iOS icon for Bookmark.
- [`#232 <https://github.com/dennissiemensma/dsmr-reader/issues/232>`_] Docs: Explain settings/options.
- [`#260 <https://github.com/dennissiemensma/dsmr-reader/issues/260>`_] Add link to readthedocs in Django for Dropbox instructions.
- [`#211 <https://github.com/dennissiemensma/dsmr-reader/issues/211>`_] API request should return HTTP 201 instead of HTTP 200.
- [`#191 <https://github.com/dennissiemensma/dsmr-reader/issues/191>`_] Deprecate MySQL support.
- [`#251 <https://github.com/dennissiemensma/dsmr-reader/issues/251>`_] Buienradar Uncaught exception.
- [`#257 <https://github.com/dennissiemensma/dsmr-reader/issues/257>`_] Requirements update (February 2017).
- [`#274 <https://github.com/dennissiemensma/dsmr-reader/issues/274>`_] Requirements update (March 2017).


----


v1.5.5 - 2017-01-19

- Remove readonly restriction for editing statistics in admin interface (`#242 <https://github.com/dennissiemensma/dsmr-reader/issues/242>`_).


----


v1.5.4 - 2017-01-12

- Improve datalogger for DSMR v5.0 (`#212 <https://github.com/dennissiemensma/dsmr-reader/issues/212>`_).
- Fixed another bug in MinderGas API client implementation (`#228 <https://github.com/dennissiemensma/dsmr-reader/issues/228>`_).


----


v1.5.5 - 2017-01-19

- Remove readonly restriction for editing statistics in admin interface (`#242 <https://github.com/dennissiemensma/dsmr-reader/issues/242>`_).


----


v1.5.4 - 2017-01-12

- Improve datalogger for DSMR v5.0 (`#212 <https://github.com/dennissiemensma/dsmr-reader/issues/212>`_).
- Fixed another bug in MinderGas API client implementation (`#228 <https://github.com/dennissiemensma/dsmr-reader/issues/228>`_).


----


v1.5.3 - 2017-01-11

- Improve MinderGas API client implementation (`#228 <https://github.com/dennissiemensma/dsmr-reader/issues/228>`_).


----


v1.5.2 - 2017-01-09

- Automatic refresh of dashboard charts (`#210 <https://github.com/dennissiemensma/dsmr-reader/issues/210>`_).
- Mindergas.nl API: Tijdstip van verzending willekeurig maken (`#204 <https://github.com/dennissiemensma/dsmr-reader/issues/204>`_).
- Extend API docs with additional example (`#185 <https://github.com/dennissiemensma/dsmr-reader/issues/185>`_).
- Docs: How to restore backup (`#190 <https://github.com/dennissiemensma/dsmr-reader/issues/190>`_).
- Log errors occured to file (`#181 <https://github.com/dennissiemensma/dsmr-reader/issues/181>`_).


----


v1.5.1 - 2017-01-04

.. note::

    This patch contains no new features and **only solves upgrading issues** for some users.

- Fix for issues `#200 <https://github.com/dennissiemensma/dsmr-reader/issues/200>`_ & `#217 <https://github.com/dennissiemensma/dsmr-reader/issues/217>`_, which is caused by omitting the switch to the VirtualEnv. This was not documented well enough in early versions of this project, causing failed upgrades. 


----


v1.5.0 - 2017-01-01

.. warning:: **Change in Python support** 

  - The support for ``Python 3.3`` has been **dropped** due to the Django upgrade (`#103 <https://github.com/dennissiemensma/dsmr-reader/issues/103>`_).
  - There is **experimental support** for ``Python 3.6`` and ``Python 3.7 (nightly)`` as the unittests are `now built against those versions <https://travis-ci.org/dennissiemensma/dsmr-reader/branches>`_ as well (`#167 <https://github.com/dennissiemensma/dsmr-reader/issues/167>`_). 

.. warning:: **Legacy warning**

  - The migrations that were squashed together in (`#31 <https://github.com/dennissiemensma/dsmr-reader/issues/31>`_) have been **removed**. This will only affect you when you are currently still running a dsmrreader-version of **before** ``v0.13 (β)``. 
  - If you are indeed still running ``< v0.13 (β)``, please upgrade to ``v1.4`` first (!), followed by an upgrade to ``v1.5``. 

- Verify telegrams' CRC (`#188 <https://github.com/dennissiemensma/dsmr-reader/issues/188>`_).
- Display last 24 hours on dashboard (`#164 <https://github.com/dennissiemensma/dsmr-reader/issues/164>`_).
- Status page visualisation (`#172 <https://github.com/dennissiemensma/dsmr-reader/issues/172>`_).
- Store and display phases consumption (`#161 <https://github.com/dennissiemensma/dsmr-reader/issues/161>`_).
- Weather graph not showing when no gas data is available (`#170 <https://github.com/dennissiemensma/dsmr-reader/issues/170>`_).
- Upgrade to ChartJs 2.0 (`#127 <https://github.com/dennissiemensma/dsmr-reader/issues/127>`_).
- Improve Statistics page performance (`#173 <https://github.com/dennissiemensma/dsmr-reader/issues/173>`_).
- Version checker at github (`#166 <https://github.com/dennissiemensma/dsmr-reader/issues/166>`_).
- Remove required login for dismissal of in-app notifications (`#179 <https://github.com/dennissiemensma/dsmr-reader/issues/179>`_).
- Round numbers displayed in GUI to 2 decimals (`#183 <https://github.com/dennissiemensma/dsmr-reader/issues/183>`_).
- Switch Nosetests to Pytest (+ pytest-cov) (`#167 <https://github.com/dennissiemensma/dsmr-reader/issues/167>`_).
- PyLama code audit (+ pytest-cov) (`#158 <https://github.com/dennissiemensma/dsmr-reader/issues/158>`_).
- Double upgrade of Django framework ``Django 1.8`` -> ``Django 1.9`` -> ``Django 1.10`` (`#103 <https://github.com/dennissiemensma/dsmr-reader/issues/103>`_).
- Force ``PYTHONUNBUFFERED`` for supervisor commands (`#176 <https://github.com/dennissiemensma/dsmr-reader/issues/176>`_).
- Documentation updates for v1.5 (`#171 <https://github.com/dennissiemensma/dsmr-reader/issues/171>`_).
- Requirements update for v1.5 (december 2016) (`#182 <https://github.com/dennissiemensma/dsmr-reader/issues/182>`_).
- Improved backend process logging (`#184 <https://github.com/dennissiemensma/dsmr-reader/issues/184>`_).


----


v1.4.1 - 2016-12-12

- Consumption chart hangs due to unique_key violation (`#174 <https://github.com/dennissiemensma/dsmr-reader/issues/174>`_).
- NoReverseMatch at / Reverse for 'docs' (`#175 <https://github.com/dennissiemensma/dsmr-reader/issues/175>`_).


----


v1.4.0 - 2016-11-28
.. warning:: **Change in Python support**

  - Support for ``Python 3.5`` has been added officially (`#55 <https://github.com/dennissiemensma/dsmr-reader/issues/55>`_).

- Push notifications for Notify My Android / Prowl (iOS), written by Jeroen Peters (`#152 <https://github.com/dennissiemensma/dsmr-reader/issues/152>`_).
- Support for both single and high/low tariff (`#130 <https://github.com/dennissiemensma/dsmr-reader/issues/130>`_).
- Add new note from Dashboard has wrong time format (`#159 <https://github.com/dennissiemensma/dsmr-reader/issues/159>`_).
- Display estimated price for current usage in Dashboard (`#155 <https://github.com/dennissiemensma/dsmr-reader/issues/155>`_).
- Dropbox API v1 deprecated in June 2017 (`#142 <https://github.com/dennissiemensma/dsmr-reader/issues/142>`_).
- Improve code coverage (`#151 <https://github.com/dennissiemensma/dsmr-reader/issues/151>`_).
- Restyle configuration overview (`#156 <https://github.com/dennissiemensma/dsmr-reader/issues/156>`_).
- Capability based push notifications (`#165 <https://github.com/dennissiemensma/dsmr-reader/issues/165>`_).


----


v1.3.2 - 2016-11-08

- Requirements update (november 2016) (`#150 <https://github.com/dennissiemensma/dsmr-reader/issues/150>`_).


----


v1.3.1 - 2016-08-16

- CSS large margin-bottom (`#144 <https://github.com/dennissiemensma/dsmr-reader/issues/144>`_).
- Django security releases issued: 1.8.14 (`#147 <https://github.com/dennissiemensma/dsmr-reader/issues/147>`_).
- Requirements update (August 2016) (`#148 <https://github.com/dennissiemensma/dsmr-reader/issues/148>`_).
- Query performance improvements (`#149 <https://github.com/dennissiemensma/dsmr-reader/issues/149>`_).


----


v1.3.0 - 2016-07-15

- API endpoint for datalogger (`#140 <https://github.com/dennissiemensma/dsmr-reader/issues/140>`_).
- Colors for charts (`#137 <https://github.com/dennissiemensma/dsmr-reader/issues/137>`_).
- Data export: Mindergas.nl (`#10 <https://github.com/dennissiemensma/dsmr-reader/issues/10>`_).
- Requirement upgrade (`#143 <https://github.com/dennissiemensma/dsmr-reader/issues/143>`_).
- Installation wizard for first time use (`#139 <https://github.com/dennissiemensma/dsmr-reader/issues/139>`_).


----


v1.2.0 - 2016-05-18

- Energy supplier prices does not indicate tariff type (Django admin) (`#126 <https://github.com/dennissiemensma/dsmr-reader/issues/126>`_).
- Requirements update (`#128 <https://github.com/dennissiemensma/dsmr-reader/issues/128>`_).
- Force backup (`#123 <https://github.com/dennissiemensma/dsmr-reader/issues/123>`_).
- Update clean-install.md (`#131 <https://github.com/dennissiemensma/dsmr-reader/issues/131>`_).
- Improve data export field names (`#132 <https://github.com/dennissiemensma/dsmr-reader/issues/132>`_).
- Display average temperature in archive (`#122 <https://github.com/dennissiemensma/dsmr-reader/issues/122>`_).
- Pie charts on trends page overlap their canvas (`#136 <https://github.com/dennissiemensma/dsmr-reader/issues/136>`_).
- 'Slumber' consumption (`#115 <https://github.com/dennissiemensma/dsmr-reader/issues/115>`_).
- Show lowest & highest Watt peaks (`#138 <https://github.com/dennissiemensma/dsmr-reader/issues/138>`_).
- Allow day & hour statistics reset due to changing energy prices (`#95 <https://github.com/dennissiemensma/dsmr-reader/issues/95>`_).



v1.1.2 - 2016-05-01

- Trends page giving errors (when lacking data) (`#125 <https://github.com/dennissiemensma/dsmr-reader/issues/125>`_).


----


v1.1.1 - 2016-04-27

- Improve readme (`#124 <https://github.com/dennissiemensma/dsmr-reader/issues/124>`_).


----


v1.1.0 - 2016-04-23

- Autorefresh dashboard (`#117 <https://github.com/dennissiemensma/dsmr-reader/issues/117>`_).
- Improve line graphs' visibility (`#111 <https://github.com/dennissiemensma/dsmr-reader/issues/111>`_).
- Easily add notes (`#110 <https://github.com/dennissiemensma/dsmr-reader/issues/110>`_).
- Export data points in CSV format (`#2 <https://github.com/dennissiemensma/dsmr-reader/issues/2>`_).
- Allow day/month/year comparison (`#94 <https://github.com/dennissiemensma/dsmr-reader/issues/94>`_).
- Docs: Add FAQ and generic application info (`#113 <https://github.com/dennissiemensma/dsmr-reader/issues/113>`_).
- Support for Iskra meter (DSMR 2.x) (`#120 <https://github.com/dennissiemensma/dsmr-reader/issues/120>`_).


----


v1.0.1 - 2016-04-07

- Update licence to OSI compatible one (`#119 <https://github.com/dennissiemensma/dsmr-reader/issues/119>`_).


----


v1.0.0 - 2016-04-07

- First official stable release.


----


[β] v0.1 (2015-10-29) to 0.16 (2016-04-06)

.. note::

    All previous beta releases/changes have been combined to a single list below.

- Move documentation to wiki or RTD (`#90 <https://github.com/dennissiemensma/dsmr-reader/issues/90>`_).
- Translate README to Dutch (`#16 <https://github.com/dennissiemensma/dsmr-reader/issues/16>`_).
- Delete (recent) history page (`#112 <https://github.com/dennissiemensma/dsmr-reader/issues/112>`_).
- Display most recent temperature in dashboard (`#114 <https://github.com/dennissiemensma/dsmr-reader/issues/114>`_).
- Upgrade Django to 1.8.12 (`#118 <https://github.com/dennissiemensma/dsmr-reader/issues/118>`_).

- Redesign trends page (`#97 <https://github.com/dennissiemensma/dsmr-reader/issues/97>`_).
- Support for summer time (`#105 <https://github.com/dennissiemensma/dsmr-reader/issues/105>`_).
- Support for Daylight Saving Time (DST) transition (`#104 <https://github.com/dennissiemensma/dsmr-reader/issues/104>`_).
- Add (error) hints to status page (`#106 <https://github.com/dennissiemensma/dsmr-reader/issues/106>`_).
- Keep track of version (`#108 <https://github.com/dennissiemensma/dsmr-reader/issues/108>`_).

- Django 1.8.11 released (`#82 <https://github.com/dennissiemensma/dsmr-reader/issues/82>`_).
- Prevent tests from failing due to moment of execution (`#88 <https://github.com/dennissiemensma/dsmr-reader/issues/88>`_).
- Statistics page meter positions are broken (`#93 <https://github.com/dennissiemensma/dsmr-reader/issues/93>`_).
- Archive only shows graph untill 23:00 (11 pm) (`#77 <https://github.com/dennissiemensma/dsmr-reader/issues/77>`_).
- Trends page crashes due to nullable fields average (`#100 <https://github.com/dennissiemensma/dsmr-reader/issues/100>`_).
- Trends: Plot peak and off-peak relative to each other (`#99 <https://github.com/dennissiemensma/dsmr-reader/issues/99>`_).
- Monitor requirements with requires.io (`#101 <https://github.com/dennissiemensma/dsmr-reader/issues/101>`_).
- Terminology (`#41 <https://github.com/dennissiemensma/dsmr-reader/issues/41>`_).
- Obsolete signals in dsmr_consumption (`#63 <https://github.com/dennissiemensma/dsmr-reader/issues/63>`_).
- Individual app testing coverage (`#64 <https://github.com/dennissiemensma/dsmr-reader/issues/64>`_).
- Support for extra devices on other M-bus (0-n:24.1) (`#92 <https://github.com/dennissiemensma/dsmr-reader/issues/92>`_).
- Separate post-deployment commands (`#102 <https://github.com/dennissiemensma/dsmr-reader/issues/102>`_).

- Show exceptions in production (webinterface) (`#87 <https://github.com/dennissiemensma/dsmr-reader/issues/87>`_).
- Keep Supervisor processes running (`#79 <https://github.com/dennissiemensma/dsmr-reader/issues/79>`_).
- Hourly stats of 22:00:00+00 every day lack gas (`#78 <https://github.com/dennissiemensma/dsmr-reader/issues/78>`_).
- Test Travis-CI with MySQL + MariaDB + PostgreSQL (`#54 <https://github.com/dennissiemensma/dsmr-reader/issues/54>`_).
- PostgreSQL tests + nosetests + coverage failure: unrecognized configuration parameter "foreign_key_checks" (`#62 <https://github.com/dennissiemensma/dsmr-reader/issues/62>`_).
- Performance check (`#83 <https://github.com/dennissiemensma/dsmr-reader/issues/83>`_).
- Allow month & year archive (`#66 <https://github.com/dennissiemensma/dsmr-reader/issues/66>`_).
- Graphs keep increasing height on tablet (`#89 <https://github.com/dennissiemensma/dsmr-reader/issues/89>`_).

- Delete StatsSettings(.track) settings model (`#71 <https://github.com/dennissiemensma/dsmr-reader/issues/71>`_).
- Drop deprecated commands (`#22 <https://github.com/dennissiemensma/dsmr-reader/issues/22>`_).
- Datalogger doesn't work properly with DSMR 4.2 (KAIFA-METER) (`#73 <https://github.com/dennissiemensma/dsmr-reader/issues/73>`_).
- Dashboard month statistics costs does not add up (`#75 <https://github.com/dennissiemensma/dsmr-reader/issues/75>`_).
- Log unhandled exceptions and errors (`#65 <https://github.com/dennissiemensma/dsmr-reader/issues/65>`_).
- Datalogger crashes with IntegrityError because 'timestamp' is null (`#74 <https://github.com/dennissiemensma/dsmr-reader/issues/74>`_).
- Trends are always shown in UTC (`#76 <https://github.com/dennissiemensma/dsmr-reader/issues/76>`_).
- Squash migrations (`#31 <https://github.com/dennissiemensma/dsmr-reader/issues/31>`_).
- Display 'electricity returned' graph in dashboard (`#81 <https://github.com/dennissiemensma/dsmr-reader/issues/81>`_).
- Optional gas (and electricity returned) capabilities tracking (`#70 <https://github.com/dennissiemensma/dsmr-reader/issues/70>`_).
- Add 'electricity returned' to trends page (`#84 <https://github.com/dennissiemensma/dsmr-reader/issues/84>`_).

- Archive: View past days details (`#61 <https://github.com/dennissiemensma/dsmr-reader/issues/61>`_).
- Dashboard: Consumption total for current month (`#60 <https://github.com/dennissiemensma/dsmr-reader/issues/60>`_).
- Check whether gas readings are optional (`#34 <https://github.com/dennissiemensma/dsmr-reader/issues/34>`_).
- Django security releases issued: 1.8.10 (`#68 <https://github.com/dennissiemensma/dsmr-reader/issues/68>`_).
- Notes display in archive (`#69 <https://github.com/dennissiemensma/dsmr-reader/issues/69>`_).

- Status page/alerts when features are disabled/unavailable (`#45 <https://github.com/dennissiemensma/dsmr-reader/issues/45>`_).
- Integrate Travis CI (`#48 <https://github.com/dennissiemensma/dsmr-reader/issues/48>`_).
- Testing coverage (`#38 <https://github.com/dennissiemensma/dsmr-reader/issues/38>`_).
- Implement automatic backups & Dropbox cloud storage (`#44 <https://github.com/dennissiemensma/dsmr-reader/issues/44>`_).
- Link code coverage service to repository (`#56 <https://github.com/dennissiemensma/dsmr-reader/issues/56>`_).
- Explore timezone.localtime() as replacement for datetime.astimezone() (`#50 <https://github.com/dennissiemensma/dsmr-reader/issues/50>`_).
- Align GasConsumption.read_at to represent the start of hour (`#40 <https://github.com/dennissiemensma/dsmr-reader/issues/40>`_).

- Cleanup unused static files (`#47 <https://github.com/dennissiemensma/dsmr-reader/issues/47>`_).
- Investigated mysql_tzinfo_to_sql — Load the Time Zone Tables (`#35 <https://github.com/dennissiemensma/dsmr-reader/issues/35>`_).
- Make additional DSMR data optional (`#46 <https://github.com/dennissiemensma/dsmr-reader/issues/46>`_).
- Localize graph x-axis (`#42 <https://github.com/dennissiemensma/dsmr-reader/issues/42>`_).
- Added graph formatting string to gettext file (`#42 <https://github.com/dennissiemensma/dsmr-reader/issues/42>`_).
- Different colors for peak & off-peak electricity (`#52 <https://github.com/dennissiemensma/dsmr-reader/issues/52>`_).
- Admin: Note widget (`#51 <https://github.com/dennissiemensma/dsmr-reader/issues/51>`_).
- Allow GUI to run without data (`#26 <https://github.com/dennissiemensma/dsmr-reader/issues/26>`_).

- Moved project to GitHub (`#28 <https://github.com/dennissiemensma/dsmr-reader/issues/28>`_).
- Added stdout to dsmr_backend to reflect progress.
- Restore note usage in GUI (`#39 <https://github.com/dennissiemensma/dsmr-reader/issues/39>`_).

- Store daily, weekly, monthly and yearly statistics (`#3 <https://github.com/dennissiemensma/dsmr-reader/issues/3>`_).
- Improved Recent History page performance a bit. (as result of `#3 <https://github.com/dennissiemensma/dsmr-reader/issues/3>`_)
- Updates ChartJS library tot 1.1, disposing django-chartjs plugin. Labels finally work! (as result of `#3 <https://github.com/dennissiemensma/dsmr-reader/issues/3>`_)
- Added trends page. (as result of `#3 <https://github.com/dennissiemensma/dsmr-reader/issues/3>`_)

- Recent history setting: set range (`#29 <https://github.com/dennissiemensma/dsmr-reader/issues/29>`_).
- Mock required for test: dsmr_weather.test_weather_tracking (`#32 <https://github.com/dennissiemensma/dsmr-reader/issues/32>`_).

- Massive refactoring: Separating apps & using signals (`#19 <https://github.com/dennissiemensma/dsmr-reader/issues/19>`_).
- README update: Exit character for cu (`#27 <https://github.com/dennissiemensma/dsmr-reader/issues/27>`_, by Jeroen Peters).
- Fixed untranslated strings in admin interface.
- Upgraded Django to 1.8.9.
