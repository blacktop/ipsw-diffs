## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine`

```diff

-  __TEXT.__text: 0x6d244
-  __TEXT.__objc_methlist: 0x8464
+  __TEXT.__text: 0x6d378
+  __TEXT.__objc_methlist: 0x847c
   __TEXT.__const: 0x278
   __TEXT.__oslogstring: 0x3131
-  __TEXT.__cstring: 0x72ec
+  __TEXT.__cstring: 0x7364
   __TEXT.__gcc_except_tab: 0x374
   __TEXT.__unwind_info: 0x1df8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29a8
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0x1540
-  __AUTH_CONST.__cfstring: 0x5e40
-  __AUTH_CONST.__objc_const: 0xf078
+  __AUTH_CONST.__cfstring: 0x5e80
+  __AUTH_CONST.__objc_const: 0xf0d8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x890
+  __AUTH.__objc_data: 0x1090
+  __DATA.__objc_ivar: 0x898
   __DATA.__data: 0x2d0
   __DATA_DIRTY.__objc_ivar: 0x150
-  __DATA_DIRTY.__objc_data: 0x1c20
+  __DATA_DIRTY.__objc_data: 0x1d60
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2968
-  Symbols:   6277
-  CStrings:  1882
+  Functions: 2970
+  Symbols:   6283
+  CStrings:  1886
 
Sections:
~ __TEXT.__unwind_info : content changed
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
+ OBJC_IVAR_$_RTBluePOITile._disableDistancePriorForHighDensity
+ OBJC_IVAR_$_RTBluePOITile._distancePriorWeight
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
