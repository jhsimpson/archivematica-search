# University of Saskatchewan search use cases

Sponsor: Tim Hutchinson, University of Saskatchewan

Given a digital object that has been ingested into Archivematica from an external system like Islandora, and stored in an AIP, 
As an archivist  
I want to be able to find and possibly download the digital object by searching using an identifier from that external system  
And I want to be able to find and possibly download the AIP that contains that digital object.
And I want to be able to find the object using other information I have in Islandora about this object.
An example:

An Islandora object is ingested into Archivematica and stored in an AIP. Information in Islandora about the object is listed below.  The archivist wants to u

islandora identifier: usaskarchives:37058

MODS file for this object:
# University of Saskatchewan search use cases

Sponsor: Tim Hutchinson, University of Saskatchewan

Given a digital object that has been ingested into Archivematica from an external system like Islandora, and stored in an AIP, 
As an archivist  
I want to be able to find and possibly download the digital object by searching using an identifier from that external system  
And I want to be able to find and possibly download the AIP that contains that digital object.
And I want to be able to find the object using other information I have in Islandora about this object.

An example:

An Islandora object is ingested into Archivematica and stored in an AIP. Information in Islandora about the object is listed below.  The archivist wants to be able to search for this file using the any identifiers listed in the MODS, at a minimum.  Optionally, the archivist wants to be able to search using other tags in the mods file (e.g.,  subject, holdingSimple, typeOfResource).  Also optionally, the archivist wants to be able to search using information stored in the rdf assertions (e.g., edora:isMemberOfCollection or fedora-model:hasModel).

islandora identifier: usaskarchives:37058

MODS file for this object:
.. code-block:: xml

<mods>
	<titleInfo>
		<title>Ultrabred Allons, Apollo Canola and Caster Rapeseed - Saskatchewan Wheat Pool</title>
		<subTitle/>
	</titleInfo>
	<name type="corporate">
		<namePart>Saskatchewan Wheat Pool</namePart>
		<role>
			<roleTerm authority="marcrelator" type="text">Publisher</roleTerm>
		</role>
	</name>
	<typeOfResource>still image</typeOfResource>
	<genre authority="lctgm">Images, Photographic</genre>
	<originInfo>
		<dateIssued>1997</dateIssued>
		<publisher>Saskatchewan Wheat Pool</publisher>
		<place>
			<placeTerm authority="marccountry" type="code">Canada</placeTerm>
		</place>
		<place>
			<placeTerm type="text">Saskatchewan</placeTerm>
		</place>
	</originInfo>
	<location>
		<physicalLocation>University Library, University of Saskatchewan</physicalLocation>
		<shelfLocator/>
		<url/>
		<holdingSimple>
			<copyInformation>
				<sublocation>University Archives</sublocation>
				<shelfLocator>Saskatchewan Wheat Pool fonds</shelfLocator>
				<electronicLocator>http://www.usask.ca/archives/</electronicLocator>
				<note/>
			</copyInformation>
		</holdingSimple>
	</location>
	<identifier type="local">MG247_Box 249_SWP_SWP image binders_feeds flowers seeds</identifier>
	<language>
		<languageTerm authority="iso639-2b" type="code">eng</languageTerm>
	</language>
	<abstract>Image of several test plots labeled with signs reading "Ultrabred Allens Canola - Saskatchewan Wheat Pool ", "Ultrabred Apollo Canola - Saskatchewan Wheat Pool" and Ultrabred Caster Rapeseed - Saskatchewan Wheat Pool" - two more signs in distance- cultivated fields, farms and grain elevators in background </abstract>
	<physicalDescription>
		<form authority="marcform">projected graphic</form>
		<extent>1 photograph: col. positive; 35 mm</extent>
	</physicalDescription>
	<note/>
	<accessCondition/>
	<subject>
		<topic/>
		<topic>grain (seed)</topic>
		<topic>test sites</topic>
		<topic>fields</topic>
		<topic>farms</topic>
		<topic>grain elevators</topic>
		<topic>agricultural cooperatives</topic>
		<topic>producer cooperatives</topic>
		<topic>signs (declatory or advertising artifacts)</topic>
		<geographic/>
		<temporal/>
		<temporal>1990-1999</temporal>
		<hierarchicalGeographic>
			<continent>North America</continent>
			<country>Canada</country>
			<province>Saskatchewan</province>
			<region/>
			<county/>
			<city/>
			<citySection/>
		</hierarchicalGeographic>
		<cartographics>
			<coordinates>52.939916,-106.450864</coordinates>
		</cartographics>
	</subject>
	<identifier type="local">usaskarchives:37058</identifier>
</mods>

fileSec from this objects Fedora METS file:

.. code-block:: xml

<METS:fileSec>
	<METS:fileGrp ID="DATASTREAMS">
		<METS:fileGrp ID="OBJ" STATUS="A" VERSIONABLE="true">
			<METS:file ID="OBJ.0" CREATED="2013-06-14T21:37:31.256Z" MIMETYPE="image/tif" SIZE="65137470" OWNERID="M">
				<METS:FLocat xlink:title="uofs_archives_mg247_swp_imagebinders_feedsflowersseeds_012.tif" LOCTYPE="URL" xlink:href="http://islandorasev-dev.usask.ca:8080/fedora/get/usaskarchives:37058/OBJ/2013-06-14T21:37:31.256Z"/>
			</METS:file>
		</METS:fileGrp>
		<METS:fileGrp ID="JP2" STATUS="A" VERSIONABLE="true">
			<METS:file ID="JP2.0" CREATED="2013-06-14T21:37:31.256Z" MIMETYPE="image/jp2" SIZE="679447" OWNERID="M">
				<METS:FLocat xlink:title="chives_mg247_swp_imagebinders_feedsflowersseeds_012.tif_JP2.jp2" LOCTYPE="URL" xlink:href="http://islandorasev-dev.usask.ca:8080/fedora/get/usaskarchives:37058/JP2/2013-06-14T21:37:31.256Z"/>
			</METS:file>
		</METS:fileGrp>
		<METS:fileGrp ID="JPG" STATUS="A" VERSIONABLE="true">
			<METS:file ID="JPG.0" CREATED="2013-06-14T21:37:31.256Z" MIMETYPE="image/jpeg" SIZE="68571" OWNERID="M">
				<METS:FLocat xlink:title="chives_mg247_swp_imagebinders_feedsflowersseeds_012.tif-med.jpg" LOCTYPE="URL" xlink:href="http://islandorasev-dev.usask.ca:8080/fedora/get/usaskarchives:37058/JPG/2013-06-14T21:37:31.256Z"/>
			</METS:file>
		</METS:fileGrp>
		<METS:fileGrp ID="TN" STATUS="A" VERSIONABLE="true">
			<METS:file ID="TN.0" CREATED="2013-06-14T21:37:31.256Z" MIMETYPE="image/jpeg" SIZE="49273" OWNERID="M">
				<METS:FLocat xlink:title="rchives_mg247_swp_imagebinders_feedsflowersseeds_012.tif-tn.jpg" LOCTYPE="URL" xlink:href="http://islandorasev-dev.usask.ca:8080/fedora/get/usaskarchives:37058/TN/2013-06-14T21:37:31.256Z"/>
			</METS:file>
		</METS:fileGrp>
		<METS:fileGrp ID="EXIF" STATUS="A" VERSIONABLE="true">
			<METS:file ID="EXIF.0" CREATED="2013-06-14T21:37:31.256Z" MIMETYPE="text/xml" SIZE="4504" OWNERID="M">
				<METS:FLocat xlink:title="_archives_mg247_swp_imagebinders_feedsflowersseeds_012_EXIF.xml" LOCTYPE="URL" xlink:href="http://islandorasev-dev.usask.ca:8080/fedora/get/usaskarchives:37058/EXIF/2013-06-14T21:37:31.256Z"/>
			</METS:file>
		</METS:fileGrp>
	</METS:fileGrp>
</METS:fileSec>

RDF statements in Islandora about this object:

.. code-block:: xml

<rdf:RDF>
	<rdf:Description rdf:about="info:fedora/usaskarchives:37058">
		<fedora:isMemberOfCollection rdf:resource="info:fedora/usaskarchives:32404"/>
		<fedora-model:hasModel rdf:resource="info:fedora/islandora:sp_large_image_cmodel"/>
		<islandora:isManageableByUser>fedoraAdmin</islandora:isManageableByUser>
		<islandora:isManageableByUser>pmd306</islandora:isManageableByUser>
		<islandora:isManageableByUser>uasc</islandora:isManageableByUser>
		<islandora:isManageableByRole>administrator</islandora:isManageableByRole>
		<islandora:isManageableByRole>usaskcontributor</islandora:isManageableByRole>
	</rdf:Description>
</rdf:RDF>

