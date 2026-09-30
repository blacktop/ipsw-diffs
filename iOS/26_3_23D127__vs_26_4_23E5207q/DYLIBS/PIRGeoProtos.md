## PIRGeoProtos

> `/System/Library/PrivateFrameworks/PIRGeoProtos.framework/PIRGeoProtos`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0x3f00
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_methlist: 0x654
+2418.4.8.2.100
+  __TEXT.__text: 0x682c
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_methlist: 0x95c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x123
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0xa25
-  __TEXT.__objc_methtype: 0x125
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__cstring: 0x1e4
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_classname: 0x75
+  __TEXT.__objc_methname: 0xf56
+  __TEXT.__objc_methtype: 0x1fe
+  __TEXT.__objc_stubs: 0x6e0
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x368
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x100
-  __AUTH_CONST.__cfstring: 0x2e0
-  __AUTH_CONST.__objc_const: 0x940
-  __DATA.__objc_ivar: 0x60
+  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x118
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0xdd0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB310021-CB6B-3617-B906-D22DCA3CA9D8
-  Functions: 132
-  Symbols:   423
-  CStrings:  233
+  UUID: 9B5E6D50-6191-307F-B8EB-5020667D8904
+  Functions: 199
+  Symbols:   588
+  CStrings:  334
 
Symbols:
+ -[PIRGeoPoi administrativeAreaEncryptedMuid]
+ -[PIRGeoPoi boundingBox]
+ -[PIRGeoPoi countryEncryptedMuid]
+ -[PIRGeoPoi encryptedMuid]
+ -[PIRGeoPoi hasAdministrativeAreaEncryptedMuid]
+ -[PIRGeoPoi hasBoundingBox]
+ -[PIRGeoPoi hasCountryEncryptedMuid]
+ -[PIRGeoPoi hasEncryptedMuid]
+ -[PIRGeoPoi hasPrefName]
+ -[PIRGeoPoi hasSubAdministrativeAreaEncryptedMuid]
+ -[PIRGeoPoi hasTimezone]
+ -[PIRGeoPoi prefName]
+ -[PIRGeoPoi setAdministrativeAreaEncryptedMuid:]
+ -[PIRGeoPoi setBoundingBox:]
+ -[PIRGeoPoi setCountryEncryptedMuid:]
+ -[PIRGeoPoi setEncryptedMuid:]
+ -[PIRGeoPoi setHasAdministrativeAreaEncryptedMuid:]
+ -[PIRGeoPoi setHasCountryEncryptedMuid:]
+ -[PIRGeoPoi setHasEncryptedMuid:]
+ -[PIRGeoPoi setHasSubAdministrativeAreaEncryptedMuid:]
+ -[PIRGeoPoi setPrefName:]
+ -[PIRGeoPoi setSubAdministrativeAreaEncryptedMuid:]
+ -[PIRGeoPoi setTimezone:]
+ -[PIRGeoPoi subAdministrativeAreaEncryptedMuid]
+ -[PIRGeoPoi timezone]
+ -[PIRMapRegion copyTo:]
+ -[PIRMapRegion copyWithZone:]
+ -[PIRMapRegion description]
+ -[PIRMapRegion dictionaryRepresentation]
+ -[PIRMapRegion eastLng]
+ -[PIRMapRegion hasEastLng]
+ -[PIRMapRegion hasNorthLat]
+ -[PIRMapRegion hasSouthLat]
+ -[PIRMapRegion hasWestLng]
+ -[PIRMapRegion hash]
+ -[PIRMapRegion isEqual:]
+ -[PIRMapRegion mergeFrom:]
+ -[PIRMapRegion northLat]
+ -[PIRMapRegion readFrom:]
+ -[PIRMapRegion setEastLng:]
+ -[PIRMapRegion setHasEastLng:]
+ -[PIRMapRegion setHasNorthLat:]
+ -[PIRMapRegion setHasSouthLat:]
+ -[PIRMapRegion setHasWestLng:]
+ -[PIRMapRegion setNorthLat:]
+ -[PIRMapRegion setSouthLat:]
+ -[PIRMapRegion setWestLng:]
+ -[PIRMapRegion southLat]
+ -[PIRMapRegion westLng]
+ -[PIRMapRegion writeTo:]
+ -[PIRTimezone .cxx_destruct]
+ -[PIRTimezone copyTo:]
+ -[PIRTimezone copyWithZone:]
+ -[PIRTimezone description]
+ -[PIRTimezone dictionaryRepresentation]
+ -[PIRTimezone hasIdentifier]
+ -[PIRTimezone hash]
+ -[PIRTimezone identifier]
+ -[PIRTimezone isEqual:]
+ -[PIRTimezone mergeFrom:]
+ -[PIRTimezone readFrom:]
+ -[PIRTimezone setIdentifier:]
+ -[PIRTimezone writeTo:]
+ OBJC_IVAR_$_PIRGeoPoi._administrativeAreaEncryptedMuid
+ OBJC_IVAR_$_PIRGeoPoi._boundingBox
+ OBJC_IVAR_$_PIRGeoPoi._countryEncryptedMuid
+ OBJC_IVAR_$_PIRGeoPoi._encryptedMuid
+ OBJC_IVAR_$_PIRGeoPoi._prefName
+ OBJC_IVAR_$_PIRGeoPoi._subAdministrativeAreaEncryptedMuid
+ OBJC_IVAR_$_PIRGeoPoi._timezone
+ OBJC_IVAR_$_PIRMapRegion._eastLng
+ OBJC_IVAR_$_PIRMapRegion._has
+ OBJC_IVAR_$_PIRMapRegion._northLat
+ OBJC_IVAR_$_PIRMapRegion._southLat
+ OBJC_IVAR_$_PIRMapRegion._westLng
+ OBJC_IVAR_$_PIRTimezone._identifier
+ _OBJC_CLASS_$_PIRMapRegion
+ _OBJC_CLASS_$_PIRTimezone
+ _OBJC_METACLASS_$_PIRMapRegion
+ _OBJC_METACLASS_$_PIRTimezone
+ _PBDataWriterWriteFloatField
+ _PIRMapRegionReadFrom
+ _PIRTimezoneReadFrom
+ __OBJC_$_INSTANCE_METHODS_PIRMapRegion
+ __OBJC_$_INSTANCE_METHODS_PIRTimezone
+ __OBJC_$_INSTANCE_VARIABLES_PIRMapRegion
+ __OBJC_$_INSTANCE_VARIABLES_PIRTimezone
+ __OBJC_$_PROP_LIST_PIRMapRegion
+ __OBJC_$_PROP_LIST_PIRTimezone
+ __OBJC_CLASS_PROTOCOLS_$_PIRMapRegion
+ __OBJC_CLASS_PROTOCOLS_$_PIRTimezone
+ __OBJC_CLASS_RO_$_PIRMapRegion
+ __OBJC_CLASS_RO_$_PIRTimezone
+ __OBJC_METACLASS_RO_$_PIRMapRegion
+ __OBJC_METACLASS_RO_$_PIRTimezone
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$setBoundingBox:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setPrefName:
+ _objc_msgSend$setTimezone:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x8
CStrings:
+ "@\"PIRMapRegion\""
+ "@\"PIRTimezone\""
+ "PIRMapRegion"
+ "PIRTimezone"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",&,N,V_prefName"
+ "T@\"PIRMapRegion\",&,N,V_boundingBox"
+ "T@\"PIRTimezone\",&,N,V_timezone"
+ "TQ,N,V_administrativeAreaEncryptedMuid"
+ "TQ,N,V_countryEncryptedMuid"
+ "TQ,N,V_encryptedMuid"
+ "TQ,N,V_subAdministrativeAreaEncryptedMuid"
+ "Tf,N,V_eastLng"
+ "Tf,N,V_northLat"
+ "Tf,N,V_southLat"
+ "Tf,N,V_westLng"
+ "_administrativeAreaEncryptedMuid"
+ "_boundingBox"
+ "_countryEncryptedMuid"
+ "_eastLng"
+ "_encryptedMuid"
+ "_identifier"
+ "_northLat"
+ "_prefName"
+ "_southLat"
+ "_subAdministrativeAreaEncryptedMuid"
+ "_timezone"
+ "_westLng"
+ "administrativeAreaEncryptedMuid"
+ "administrative_area_encrypted_muid"
+ "boundingBox"
+ "bounding_box"
+ "countryEncryptedMuid"
+ "country_encrypted_muid"
+ "eastLng"
+ "east_lng"
+ "encryptedMuid"
+ "encrypted_muid"
+ "f"
+ "f16@0:8"
+ "h"
+ "hasAdministrativeAreaEncryptedMuid"
+ "hasBoundingBox"
+ "hasCountryEncryptedMuid"
+ "hasEastLng"
+ "hasEncryptedMuid"
+ "hasIdentifier"
+ "hasNorthLat"
+ "hasPrefName"
+ "hasSouthLat"
+ "hasSubAdministrativeAreaEncryptedMuid"
+ "hasTimezone"
+ "hasWestLng"
+ "identifier"
+ "northLat"
+ "north_lat"
+ "numberWithFloat:"
+ "prefName"
+ "pref_name"
+ "setAdministrativeAreaEncryptedMuid:"
+ "setBoundingBox:"
+ "setCountryEncryptedMuid:"
+ "setEastLng:"
+ "setEncryptedMuid:"
+ "setHasAdministrativeAreaEncryptedMuid:"
+ "setHasCountryEncryptedMuid:"
+ "setHasEastLng:"
+ "setHasEncryptedMuid:"
+ "setHasNorthLat:"
+ "setHasSouthLat:"
+ "setHasSubAdministrativeAreaEncryptedMuid:"
+ "setHasWestLng:"
+ "setIdentifier:"
+ "setNorthLat:"
+ "setPrefName:"
+ "setSouthLat:"
+ "setSubAdministrativeAreaEncryptedMuid:"
+ "setTimezone:"
+ "setWestLng:"
+ "southLat"
+ "south_lat"
+ "subAdministrativeAreaEncryptedMuid"
+ "sub_administrative_area_encrypted_muid"
+ "timezone"
+ "v20@0:8f16"
+ "westLng"
+ "west_lng"
+ "{?=\"administrativeAreaEncryptedMuid\"b1\"countryEncryptedMuid\"b1\"encryptedMuid\"b1\"popularityCartoScore\"b1\"subAdministrativeAreaEncryptedMuid\"b1\"zioId\"b1}"
+ "{?=\"eastLng\"b1\"northLat\"b1\"southLat\"b1\"westLng\"b1}"
- "%"
- "{?=\"popularityCartoScore\"b1\"zioId\"b1}"

```
