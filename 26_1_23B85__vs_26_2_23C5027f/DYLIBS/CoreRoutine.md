## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1069.0.4.0.0
-  __TEXT.__text: 0x641d4
+1070.0.1.0.1
+  __TEXT.__text: 0x64338
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x7d9c
+  __TEXT.__objc_methlist: 0x7db4
   __TEXT.__const: 0x2c8
-  __TEXT.__oslogstring: 0x331f
-  __TEXT.__cstring: 0x64a9
+  __TEXT.__oslogstring: 0x3342
+  __TEXT.__cstring: 0x652f
   __TEXT.__gcc_except_tab: 0x368
   __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf9a
-  __TEXT.__objc_methname: 0xee15
-  __TEXT.__objc_methtype: 0x26d7
-  __TEXT.__objc_stubs: 0x74c0
+  __TEXT.__objc_methname: 0xef35
+  __TEXT.__objc_methtype: 0x26db
+  __TEXT.__objc_stubs: 0x7500
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2858
+  __DATA_CONST.__objc_selrefs: 0x2868
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x59c0
-  __AUTH_CONST.__objc_const: 0xe260
+  __AUTH_CONST.__cfstring: 0x5a00
+  __AUTH_CONST.__objc_const: 0xe2c0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x810
+  __DATA.__objc_ivar: 0x818
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_ivar: 0x130
   __DATA_DIRTY.__objc_data: 0x16d0

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB576C4B-9F91-3F99-856D-42F97D877A96
-  Functions: 2808
-  Symbols:   8767
-  CStrings:  4435
+  UUID: 1D285B93-5590-3985-B038-585263E2D8DA
+  Functions: 2810
+  Symbols:   8775
+  CStrings:  4445
 
Symbols:
+ -[RTBluePOIModel featureToHashedApMappingDataURL]
+ -[RTBluePOIModel initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:]
+ -[RTBluePOITile hashedApToModelMappingDataURL]
+ -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
+ _OBJC_IVAR_$_RTBluePOIModel._featureToHashedApMappingDataURL
+ _OBJC_IVAR_$_RTBluePOITile._hashedApToModelMappingDataURL
+ _objc_msgSend$featureToHashedApMappingDataURL
+ _objc_msgSend$hashedApToModelMappingDataURL
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:
- -[RTBluePOIModel initWithIdentifier:featureToHashedApMapping:url:]
- -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
- _objc_msgSend$initWithIdentifier:featureToHashedApMapping:url:
CStrings:
+ "@136@0:8@16@24@32@40@48Q56@64@72@80@88@96@104@112Q120d128"
+ "Invalid parameter not satisfying: featureToHashedApMapping || featureToHashedApMappingDataURL"
+ "T@\"NSString\",R,N,V_featureToHashedApMappingDataURL"
+ "T@\"NSString\",R,N,V_hashedApToModelMappingDataURL"
+ "_featureToHashedApMappingDataURL"
+ "_hashedApToModelMappingDataURL"
+ "featureToHashedApMappingDataURL"
+ "hashedApToModelMappingDataURL"
+ "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, hashedApToModelMappingDataURL, %@, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
+ "identifier, %@, url, %@, featureToHashedApMapping count, %lu, featureToHashedApMappingDataURL, %@"
+ "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:"
- "@128@0:8@16@24@32@40@48Q56@64@72@80@88@96@104Q112d120"
- "Invalid parameter not satisfying: featureToHashedApMapping"
- "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
- "identifier, %@, url, %@, featureToHashedApMapping count, %lu"
- "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
- "initWithIdentifier:featureToHashedApMapping:url:"

```
