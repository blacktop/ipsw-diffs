## PIRGeoProtos

> `/System/Library/PrivateFrameworks/PIRGeoProtos.framework/PIRGeoProtos`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x682c
-  __TEXT.__auth_stubs: 0x220
+2444.104.0.0.0
+  __TEXT.__text: 0x68dc
   __TEXT.__objc_methlist: 0x95c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x1e4
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0xf56
-  __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0x1ec
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0xdd0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BB6FB77-A462-3D18-B2CC-3863D6478713
+  UUID: 0BBEEF44-A934-322B-BB77-689C0E62EAC0
   Functions: 199
-  Symbols:   588
-  CStrings:  334
+  Symbols:   586
+  CStrings:  72
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ -[PIRAspireResult hasGeoList] : 24 -> 28
~ -[PIRAspireResult hasCompressedGeoList] : 24 -> 28
~ -[PIRAspireResult description] : 176 -> 164
~ _PIRAspireResultReadFrom : 572 -> 564
~ -[PIRAspireResult writeTo:] : 124 -> 136
~ -[PIRAspireResult copyTo:] : 116 -> 128
~ -[PIRAspireResult copyWithZone:] : 132 -> 148
~ -[PIRAspireResult isEqual:] : 160 -> 176
~ -[PIRAspireResult hash] : 72 -> 80
~ -[PIRAspireResult mergeFrom:] : 148 -> 156
~ -[PIRAspireResult geoList] : 16 -> 20
~ -[PIRAspireResult setGeoList:] : 80 -> 20
~ -[PIRAspireResult compressedGeoList] : 16 -> 20
~ -[PIRAspireResult setCompressedGeoList:] : 80 -> 20
~ -[PIRGeoListSnippet clearPois] : 16 -> 20
~ -[PIRGeoListSnippet addPois:] : 120 -> 132
~ -[PIRGeoListSnippet poisCount] : 16 -> 20
~ -[PIRGeoListSnippet poisAtIndex:] : 16 -> 20
~ -[PIRGeoListSnippet description] : 176 -> 164
~ _PIRGeoListSnippetReadFrom : 508 -> 504
~ -[PIRGeoListSnippet writeTo:] : 268 -> 276
~ -[PIRGeoListSnippet copyTo:] : 168 -> 164
~ -[PIRGeoListSnippet copyWithZone:] : 308 -> 316
~ -[PIRGeoListSnippet isEqual:] : 128 -> 136
~ -[PIRGeoListSnippet hash] : 16 -> 20
~ -[PIRGeoListSnippet mergeFrom:] : 252 -> 260
~ -[PIRGeoListSnippet pois] : 16 -> 20
~ -[PIRGeoListSnippet setPois:] : 80 -> 20
~ -[PIRGeoPoi hasApolloId] : 24 -> 28
~ -[PIRGeoPoi hasTitle] : 24 -> 28
~ -[PIRGeoPoi hasPrefGeocode] : 24 -> 28
~ -[PIRGeoPoi hasAddress] : 24 -> 28
~ -[PIRGeoPoi setZioId:] : 36 -> 44
~ -[PIRGeoPoi setHasZioId:] : 40 -> 44
~ -[PIRGeoPoi hasZioId] : 20 -> 24
~ -[PIRGeoPoi hasTimezone] : 24 -> 28
~ -[PIRGeoPoi setPopularityCartoScore:] : 36 -> 44
~ -[PIRGeoPoi setHasPopularityCartoScore:] : 40 -> 44
~ -[PIRGeoPoi hasPopularityCartoScore] : 20 -> 24
~ -[PIRGeoPoi hasModernPrimaryCategoryId] : 24 -> 28
~ -[PIRGeoPoi hasBoundingBox] : 24 -> 28
~ -[PIRGeoPoi hasPrefName] : 24 -> 28
~ -[PIRGeoPoi setEncryptedMuid:] : 36 -> 44
~ -[PIRGeoPoi setHasEncryptedMuid:] : 40 -> 44
~ -[PIRGeoPoi hasEncryptedMuid] : 20 -> 24
~ -[PIRGeoPoi setCountryEncryptedMuid:] : 36 -> 44
~ -[PIRGeoPoi setHasCountryEncryptedMuid:] : 40 -> 44
~ -[PIRGeoPoi hasCountryEncryptedMuid] : 20 -> 24
~ -[PIRGeoPoi setAdministrativeAreaEncryptedMuid:] : 36 -> 44
~ -[PIRGeoPoi setHasAdministrativeAreaEncryptedMuid:] : 28 -> 32
~ -[PIRGeoPoi hasAdministrativeAreaEncryptedMuid] : 20 -> 24
~ -[PIRGeoPoi setSubAdministrativeAreaEncryptedMuid:] : 36 -> 44
~ -[PIRGeoPoi setHasSubAdministrativeAreaEncryptedMuid:] : 40 -> 44
~ -[PIRGeoPoi hasSubAdministrativeAreaEncryptedMuid] : 20 -> 24
~ -[PIRGeoPoi description] : 176 -> 164
~ -[PIRGeoPoi dictionaryRepresentation] : 856 -> 872
~ _PIRGeoPoiReadFrom : 2340 -> 2316
~ -[PIRGeoPoi writeTo:] : 556 -> 620
~ -[PIRGeoPoi copyTo:] : 524 -> 612
~ -[PIRGeoPoi copyWithZone:] : 572 -> 688
~ -[PIRGeoPoi isEqual:] : 628 -> 748
~ -[PIRGeoPoi hash] : 616 -> 664
~ -[PIRGeoPoi mergeFrom:] : 616 -> 712
~ -[PIRGeoPoi apolloId] : 16 -> 20
~ -[PIRGeoPoi setApolloId:] : 80 -> 20
~ -[PIRGeoPoi title] : 16 -> 20
~ -[PIRGeoPoi setTitle:] : 80 -> 20
~ -[PIRGeoPoi prefGeocode] : 16 -> 20
~ -[PIRGeoPoi setPrefGeocode:] : 80 -> 20
~ -[PIRGeoPoi address] : 16 -> 20
~ -[PIRGeoPoi setAddress:] : 80 -> 20
~ -[PIRGeoPoi zioId] : 16 -> 20
~ -[PIRGeoPoi timezone] : 16 -> 20
~ -[PIRGeoPoi setTimezone:] : 80 -> 20
~ -[PIRGeoPoi popularityCartoScore] : 16 -> 20
~ -[PIRGeoPoi modernPrimaryCategoryId] : 16 -> 20
~ -[PIRGeoPoi setModernPrimaryCategoryId:] : 80 -> 20
~ -[PIRGeoPoi boundingBox] : 16 -> 20
~ -[PIRGeoPoi setBoundingBox:] : 80 -> 20
~ -[PIRGeoPoi prefName] : 16 -> 20
~ -[PIRGeoPoi setPrefName:] : 80 -> 20
~ -[PIRGeoPoi encryptedMuid] : 16 -> 20
~ -[PIRGeoPoi countryEncryptedMuid] : 16 -> 20
~ -[PIRGeoPoi administrativeAreaEncryptedMuid] : 16 -> 20
~ -[PIRGeoPoi subAdministrativeAreaEncryptedMuid] : 16 -> 20
~ -[PIRMapRegion setSouthLat:] : 36 -> 44
~ -[PIRMapRegion setHasSouthLat:] : 40 -> 44
~ -[PIRMapRegion hasSouthLat] : 20 -> 24
~ -[PIRMapRegion setWestLng:] : 36 -> 44
~ -[PIRMapRegion setHasWestLng:] : 40 -> 44
~ -[PIRMapRegion hasWestLng] : 20 -> 24
~ -[PIRMapRegion setNorthLat:] : 36 -> 44
~ -[PIRMapRegion setHasNorthLat:] : 40 -> 44
~ -[PIRMapRegion hasNorthLat] : 20 -> 24
~ -[PIRMapRegion setEastLng:] : 36 -> 44
~ -[PIRMapRegion setHasEastLng:] : 28 -> 32
~ -[PIRMapRegion hasEastLng] : 20 -> 24
~ -[PIRMapRegion description] : 176 -> 164
~ -[PIRMapRegion writeTo:] : 220 -> 240
~ -[PIRMapRegion copyTo:] : 240 -> 256
~ -[PIRMapRegion copyWithZone:] : 220 -> 256
~ -[PIRMapRegion isEqual:] : 276 -> 316
~ -[PIRMapRegion hash] : 580 -> 568
~ -[PIRMapRegion mergeFrom:] : 240 -> 256
~ -[PIRMapRegion southLat] : 16 -> 20
~ -[PIRMapRegion westLng] : 16 -> 20
~ -[PIRMapRegion northLat] : 16 -> 20
~ -[PIRMapRegion eastLng] : 16 -> 20
~ -[PIRPoint setLat:] : 36 -> 44
~ -[PIRPoint setHasLat:] : 28 -> 32
~ -[PIRPoint hasLat] : 20 -> 24
~ -[PIRPoint setLng:] : 36 -> 44
~ -[PIRPoint setHasLng:] : 40 -> 44
~ -[PIRPoint hasLng] : 20 -> 24
~ -[PIRPoint description] : 176 -> 164
~ -[PIRPoint writeTo:] : 140 -> 156
~ -[PIRPoint copyWithZone:] : 132 -> 152
~ -[PIRPoint isEqual:] : 196 -> 220
~ -[PIRPoint hash] : 308 -> 296
~ -[PIRPoint lat] : 16 -> 20
~ -[PIRPoint lng] : 16 -> 20
~ -[PIRStructuredAddress hasCountry] : 24 -> 28
~ -[PIRStructuredAddress hasCountryCode] : 24 -> 28
~ -[PIRStructuredAddress hasAdministrativeArea] : 24 -> 28
~ -[PIRStructuredAddress hasAdministrativeAreaCode] : 24 -> 28
~ -[PIRStructuredAddress hasSubAdministrativeArea] : 24 -> 28
~ -[PIRStructuredAddress hasLocality] : 24 -> 28
~ -[PIRStructuredAddress hasPostCode] : 24 -> 28
~ -[PIRStructuredAddress hasThoroughfare] : 24 -> 28
~ -[PIRStructuredAddress hasSubThoroughfare] : 24 -> 28
~ -[PIRStructuredAddress clearDependentLocalitys] : 16 -> 20
~ -[PIRStructuredAddress addDependentLocality:] : 120 -> 132
~ -[PIRStructuredAddress dependentLocalitysCount] : 16 -> 20
~ -[PIRStructuredAddress dependentLocalityAtIndex:] : 16 -> 20
~ -[PIRStructuredAddress description] : 176 -> 164
~ -[PIRStructuredAddress dictionaryRepresentation] : 396 -> 432
~ _PIRStructuredAddressReadFrom : 768 -> 728
~ -[PIRStructuredAddress writeTo:] : 520 -> 564
~ -[PIRStructuredAddress copyTo:] : 384 -> 416
~ -[PIRStructuredAddress copyWithZone:] : 596 -> 676
~ -[PIRStructuredAddress isEqual:] : 416 -> 496
~ -[PIRStructuredAddress hash] : 252 -> 292
~ -[PIRStructuredAddress mergeFrom:] : 488 -> 532
~ -[PIRStructuredAddress country] : 16 -> 20
~ -[PIRStructuredAddress setCountry:] : 80 -> 20
~ -[PIRStructuredAddress countryCode] : 16 -> 20
~ -[PIRStructuredAddress setCountryCode:] : 80 -> 20
~ -[PIRStructuredAddress administrativeArea] : 16 -> 20
~ -[PIRStructuredAddress setAdministrativeArea:] : 80 -> 20
~ -[PIRStructuredAddress administrativeAreaCode] : 16 -> 20
~ -[PIRStructuredAddress setAdministrativeAreaCode:] : 80 -> 20
~ -[PIRStructuredAddress subAdministrativeArea] : 16 -> 20
~ -[PIRStructuredAddress setSubAdministrativeArea:] : 80 -> 20
~ -[PIRStructuredAddress locality] : 16 -> 20
~ -[PIRStructuredAddress setLocality:] : 80 -> 20
~ -[PIRStructuredAddress postCode] : 16 -> 20
~ -[PIRStructuredAddress setPostCode:] : 80 -> 20
~ -[PIRStructuredAddress thoroughfare] : 16 -> 20
~ -[PIRStructuredAddress setThoroughfare:] : 80 -> 20
~ -[PIRStructuredAddress subThoroughfare] : 16 -> 20
~ -[PIRStructuredAddress setSubThoroughfare:] : 80 -> 20
~ -[PIRStructuredAddress dependentLocalitys] : 16 -> 20
~ -[PIRStructuredAddress setDependentLocalitys:] : 80 -> 20
~ -[PIRTimezone hasIdentifier] : 24 -> 28
~ -[PIRTimezone description] : 176 -> 164
~ _PIRTimezoneReadFrom : 448 -> 444
~ -[PIRTimezone writeTo:] : 32 -> 36
~ -[PIRTimezone copyTo:] : 32 -> 36
~ -[PIRTimezone copyWithZone:] : 100 -> 108
~ -[PIRTimezone isEqual:] : 128 -> 136
~ -[PIRTimezone hash] : 16 -> 20
~ -[PIRTimezone mergeFrom:] : 24 -> 28
~ -[PIRTimezone identifier] : 16 -> 20
~ -[PIRTimezone setIdentifier:] : 80 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"PIRGeoListSnippet\""
- "@\"PIRMapRegion\""
- "@\"PIRPoint\""
- "@\"PIRStructuredAddress\""
- "@\"PIRTimezone\""
- "@16@0:8"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "B16@0:8"
- "B24@0:8@16"
- "NSCopying"
- "PIRAspireResult"
- "PIRGeoListSnippet"
- "PIRGeoPoi"
- "PIRMapRegion"
- "PIRPoint"
- "PIRStructuredAddress"
- "PIRTimezone"
- "Q"
- "Q16@0:8"
- "T@\"NSData\",&,N,V_compressedGeoList"
- "T@\"NSMutableArray\",&,N,V_dependentLocalitys"
- "T@\"NSMutableArray\",&,N,V_pois"
- "T@\"NSString\",&,N,V_administrativeArea"
- "T@\"NSString\",&,N,V_administrativeAreaCode"
- "T@\"NSString\",&,N,V_apolloId"
- "T@\"NSString\",&,N,V_country"
- "T@\"NSString\",&,N,V_countryCode"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_locality"
- "T@\"NSString\",&,N,V_modernPrimaryCategoryId"
- "T@\"NSString\",&,N,V_postCode"
- "T@\"NSString\",&,N,V_prefName"
- "T@\"NSString\",&,N,V_subAdministrativeArea"
- "T@\"NSString\",&,N,V_subThoroughfare"
- "T@\"NSString\",&,N,V_thoroughfare"
- "T@\"NSString\",&,N,V_title"
- "T@\"PIRGeoListSnippet\",&,N,V_geoList"
- "T@\"PIRMapRegion\",&,N,V_boundingBox"
- "T@\"PIRPoint\",&,N,V_prefGeocode"
- "T@\"PIRStructuredAddress\",&,N,V_address"
- "T@\"PIRTimezone\",&,N,V_timezone"
- "TB,N"
- "TB,R,N"
- "TQ,N,V_administrativeAreaEncryptedMuid"
- "TQ,N,V_countryEncryptedMuid"
- "TQ,N,V_encryptedMuid"
- "TQ,N,V_subAdministrativeAreaEncryptedMuid"
- "TQ,N,V_zioId"
- "Td,N,V_lat"
- "Td,N,V_lng"
- "Td,N,V_popularityCartoScore"
- "Tf,N,V_eastLng"
- "Tf,N,V_northLat"
- "Tf,N,V_southLat"
- "Tf,N,V_westLng"
- "_address"
- "_administrativeArea"
- "_administrativeAreaCode"
- "_administrativeAreaEncryptedMuid"
- "_apolloId"
- "_boundingBox"
- "_compressedGeoList"
- "_country"
- "_countryCode"
- "_countryEncryptedMuid"
- "_dependentLocalitys"
- "_eastLng"
- "_encryptedMuid"
- "_geoList"
- "_has"
- "_identifier"
- "_lat"
- "_lng"
- "_locality"
- "_modernPrimaryCategoryId"
- "_northLat"
- "_pois"
- "_popularityCartoScore"
- "_postCode"
- "_prefGeocode"
- "_prefName"
- "_setError"
- "_southLat"
- "_subAdministrativeArea"
- "_subAdministrativeAreaEncryptedMuid"
- "_subThoroughfare"
- "_thoroughfare"
- "_timezone"
- "_title"
- "_westLng"
- "_zioId"
- "addDependentLocality:"
- "addObject:"
- "addPois:"
- "administrativeAreaEncryptedMuid"
- "allocWithZone:"
- "apolloId"
- "boundingBox"
- "clearDependentLocalitys"
- "clearPois"
- "compressedGeoList"
- "copyTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryEncryptedMuid"
- "d"
- "d16@0:8"
- "data"
- "dependentLocalityAtIndex:"
- "dependentLocalityType"
- "dependentLocalitys"
- "dependentLocalitysCount"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "eastLng"
- "encryptedMuid"
- "f"
- "f16@0:8"
- "geoList"
- "getBytes:range:"
- "hasAddress"
- "hasAdministrativeArea"
- "hasAdministrativeAreaCode"
- "hasAdministrativeAreaEncryptedMuid"
- "hasApolloId"
- "hasBoundingBox"
- "hasCompressedGeoList"
- "hasCountry"
- "hasCountryCode"
- "hasCountryEncryptedMuid"
- "hasEastLng"
- "hasEncryptedMuid"
- "hasError"
- "hasGeoList"
- "hasIdentifier"
- "hasLat"
- "hasLng"
- "hasLocality"
- "hasModernPrimaryCategoryId"
- "hasNorthLat"
- "hasPopularityCartoScore"
- "hasPostCode"
- "hasPrefGeocode"
- "hasPrefName"
- "hasSouthLat"
- "hasSubAdministrativeArea"
- "hasSubAdministrativeAreaEncryptedMuid"
- "hasSubThoroughfare"
- "hasThoroughfare"
- "hasTimezone"
- "hasTitle"
- "hasWestLng"
- "hasZioId"
- "hash"
- "init"
- "initWithCapacity:"
- "isEqual:"
- "isMemberOfClass:"
- "length"
- "mergeFrom:"
- "modernPrimaryCategoryId"
- "northLat"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "poisAtIndex:"
- "poisCount"
- "poisType"
- "popularityCartoScore"
- "position"
- "prefGeocode"
- "prefName"
- "readFrom:"
- "removeAllObjects"
- "setAddress:"
- "setAdministrativeArea:"
- "setAdministrativeAreaCode:"
- "setAdministrativeAreaEncryptedMuid:"
- "setApolloId:"
- "setBoundingBox:"
- "setCompressedGeoList:"
- "setCountry:"
- "setCountryCode:"
- "setCountryEncryptedMuid:"
- "setDependentLocalitys:"
- "setEastLng:"
- "setEncryptedMuid:"
- "setGeoList:"
- "setHasAdministrativeAreaEncryptedMuid:"
- "setHasCountryEncryptedMuid:"
- "setHasEastLng:"
- "setHasEncryptedMuid:"
- "setHasLat:"
- "setHasLng:"
- "setHasNorthLat:"
- "setHasPopularityCartoScore:"
- "setHasSouthLat:"
- "setHasSubAdministrativeAreaEncryptedMuid:"
- "setHasWestLng:"
- "setHasZioId:"
- "setIdentifier:"
- "setLat:"
- "setLng:"
- "setLocality:"
- "setModernPrimaryCategoryId:"
- "setNorthLat:"
- "setObject:forKey:"
- "setPois:"
- "setPopularityCartoScore:"
- "setPosition:"
- "setPostCode:"
- "setPrefGeocode:"
- "setPrefName:"
- "setSouthLat:"
- "setSubAdministrativeArea:"
- "setSubAdministrativeAreaEncryptedMuid:"
- "setSubThoroughfare:"
- "setThoroughfare:"
- "setTimezone:"
- "setTitle:"
- "setWestLng:"
- "setZioId:"
- "southLat"
- "stringWithFormat:"
- "subAdministrativeAreaEncryptedMuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "westLng"
- "writeTo:"
- "zioId"
- "{?=\"administrativeAreaEncryptedMuid\"b1\"countryEncryptedMuid\"b1\"encryptedMuid\"b1\"popularityCartoScore\"b1\"subAdministrativeAreaEncryptedMuid\"b1\"zioId\"b1}"
- "{?=\"eastLng\"b1\"northLat\"b1\"southLat\"b1\"westLng\"b1}"
- "{?=\"lat\"b1\"lng\"b1}"

```
