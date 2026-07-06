## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-  __TEXT.__text: 0x6de58
-  __TEXT.__objc_methlist: 0x8c58
+  __TEXT.__text: 0x6dfac
+  __TEXT.__objc_methlist: 0x8c70
   __TEXT.__const: 0x2c8
   __TEXT.__oslogstring: 0x35c8
-  __TEXT.__cstring: 0x76c3
+  __TEXT.__cstring: 0x773b
   __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__unwind_info: 0x2060
+  __TEXT.__unwind_info: 0x2070
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bf8
+  __DATA_CONST.__objc_selrefs: 0x2c08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__got: 0x550
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x6520
-  __AUTH_CONST.__objc_const: 0xff48
+  __AUTH_CONST.__cfstring: 0x6560
+  __AUTH_CONST.__objc_const: 0xffa8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1630
-  __DATA.__objc_ivar: 0x92c
+  __AUTH.__objc_data: 0x14f0
+  __DATA.__objc_ivar: 0x934
   __DATA.__data: 0x2e8
   __DATA_DIRTY.__objc_ivar: 0x160
-  __DATA_DIRTY.__objc_data: 0x1a40
+  __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3111
-  Symbols:   9732
-  CStrings:  2025
+  Functions: 3113
+  Symbols:   9740
+  CStrings:  2029
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[RTBluePOITile disableDistancePriorForHighDensity]
+ -[RTBluePOITile distancePriorWeight]
+ -[RTBluePOITile initWithIdentifier:apToModelMapping:date:disableDistancePriorForHighDensity:distancePriorWeight:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
+ _OBJC_IVAR_$_RTBluePOITile._disableDistancePriorForHighDensity
+ _OBJC_IVAR_$_RTBluePOITile._distancePriorWeight
+ _objc_msgSend$disableDistancePriorForHighDensity
+ _objc_msgSend$distancePriorWeight
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:disableDistancePriorForHighDensity:distancePriorWeight:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
- -[RTBluePOITile initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
CStrings:
+ "disableDistancePriorForHighDensity"
+ "distancePriorWeight"
+ "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, distance priors, %@, distancePriorWeight, %f, disableDistancePriorForHighDensity, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, hashedApToModelMappingDataURL, %@, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
- "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, distance priors, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, hashedApToModelMappingDataURL, %@, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"

```
