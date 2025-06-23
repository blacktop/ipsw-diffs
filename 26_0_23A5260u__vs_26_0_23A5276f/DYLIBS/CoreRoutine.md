## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1044.0.2.0.0
-  __TEXT.__text: 0x6156c
+1048.0.0.0.0
+  __TEXT.__text: 0x62974
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x7aa4
-  __TEXT.__const: 0x2b0
-  __TEXT.__oslogstring: 0x31c5
-  __TEXT.__cstring: 0x62d6
+  __TEXT.__objc_methlist: 0x7d6c
+  __TEXT.__const: 0x2b8
+  __TEXT.__oslogstring: 0x3226
+  __TEXT.__cstring: 0x63ca
   __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__unwind_info: 0x1d58
-  __TEXT.__objc_classname: 0xf3b
-  __TEXT.__objc_methname: 0xe9f8
-  __TEXT.__objc_methtype: 0x2696
-  __TEXT.__objc_stubs: 0x73a0
-  __DATA_CONST.__got: 0x490
+  __TEXT.__unwind_info: 0x1de0
+  __TEXT.__objc_classname: 0xf9a
+  __TEXT.__objc_methname: 0xec12
+  __TEXT.__objc_methtype: 0x26d0
+  __TEXT.__objc_stubs: 0x7480
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x11a0
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27f0
+  __DATA_CONST.__objc_selrefs: 0x2838
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x410
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5820
-  __AUTH_CONST.__objc_const: 0xdd08
+  __AUTH_CONST.__cfstring: 0x5920
+  __AUTH_CONST.__objc_const: 0xe180
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x7dc
+  __AUTH.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x800
   __DATA.__data: 0x308
-  __DATA_DIRTY.__objc_ivar: 0x124
+  __DATA_DIRTY.__objc_ivar: 0x12c
   __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E58356B-FAF1-348C-88A6-B38E05301059
-  Functions: 2751
-  Symbols:   8593
-  CStrings:  4363
+  UUID: 3A22D609-4322-3BD1-B92F-E85FDBF8A478
+  Functions: 2804
+  Symbols:   8745
+  CStrings:  4405
 
Symbols:
+ +[NSDate(RTExtensions) isDateWithinLast24Hours:]
+ +[RTBluePOIModel supportsSecureCoding]
+ +[RTTripClusterWaypointEnumerationContext supportsSecureCoding]
+ +[RTTripClusterWaypointEnumerationOptions supportsSecureCoding]
+ -[RTBluePOIModel .cxx_destruct]
+ -[RTBluePOIModel copyWithZone:]
+ -[RTBluePOIModel description]
+ -[RTBluePOIModel encodeWithCoder:]
+ -[RTBluePOIModel featureToHashedApMapping]
+ -[RTBluePOIModel hash]
+ -[RTBluePOIModel identifier]
+ -[RTBluePOIModel initWithCoder:]
+ -[RTBluePOIModel initWithIdentifier:featureToHashedApMapping:url:]
+ -[RTBluePOIModel init]
+ -[RTBluePOIModel isEqual:]
+ -[RTBluePOIModel url]
+ -[RTBluePOITile hashSalt]
+ -[RTBluePOITile hashedApToModelMapping]
+ -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
+ -[RTBluePOITile models]
+ -[RTPredictedContextOptions creationDate]
+ -[RTPredictedContextOptions initWithCreationDate:forecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:]
+ -[RTPredictedContextOptions setCreationDate:]
+ -[RTTripClusterWaypointEnumerationContext .cxx_destruct]
+ -[RTTripClusterWaypointEnumerationContext copyWithZone:]
+ -[RTTripClusterWaypointEnumerationContext description]
+ -[RTTripClusterWaypointEnumerationContext encodeWithCoder:]
+ -[RTTripClusterWaypointEnumerationContext hash]
+ -[RTTripClusterWaypointEnumerationContext initWithCoder:]
+ -[RTTripClusterWaypointEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterWaypointEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterWaypointEnumerationContext init]
+ -[RTTripClusterWaypointEnumerationContext isEqual:]
+ -[RTTripClusterWaypointEnumerationContext isEqualToContext:]
+ -[RTTripClusterWaypointEnumerationContext offset]
+ -[RTTripClusterWaypointEnumerationContext options]
+ -[RTTripClusterWaypointEnumerationOptions .cxx_destruct]
+ -[RTTripClusterWaypointEnumerationOptions batchSize]
+ -[RTTripClusterWaypointEnumerationOptions clusterID]
+ -[RTTripClusterWaypointEnumerationOptions copyWithZone:]
+ -[RTTripClusterWaypointEnumerationOptions description]
+ -[RTTripClusterWaypointEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterWaypointEnumerationOptions enumeratedType]
+ -[RTTripClusterWaypointEnumerationOptions hash]
+ -[RTTripClusterWaypointEnumerationOptions initWithClusterID:]
+ -[RTTripClusterWaypointEnumerationOptions initWithCoder:]
+ -[RTTripClusterWaypointEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterWaypointEnumerationOptions init]
+ -[RTTripClusterWaypointEnumerationOptions isEqual:]
+ -[RTTripClusterWaypointEnumerationOptions isEqualToOptions:]
+ -[RTTripClusterWaypointEnumerationOptions processingBlock]
+ -[RTTripClusterWaypointEnumerationOptions setBatchSize:]
+ -[RTTripClusterWaypointEnumerationOptions setClusterID:]
+ -[RTTripSegment setTripSegmentSequence:]
+ -[RTTripSegment setTripSegmentSequenceMax:]
+ _OBJC_CLASS_$_RTBluePOIModel
+ _OBJC_CLASS_$_RTTripClusterWaypointEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterWaypointEnumerationOptions
+ _OBJC_IVAR_$_RTBluePOIModel._featureToHashedApMapping
+ _OBJC_IVAR_$_RTBluePOIModel._identifier
+ _OBJC_IVAR_$_RTBluePOIModel._url
+ _OBJC_IVAR_$_RTBluePOITile._hashSalt
+ _OBJC_IVAR_$_RTBluePOITile._hashedApToModelMapping
+ _OBJC_IVAR_$_RTBluePOITile._models
+ _OBJC_IVAR_$_RTPredictedContextOptions._creationDate
+ _OBJC_IVAR_$_RTTripClusterWaypointEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterWaypointEnumerationContext._options
+ _OBJC_METACLASS_$_RTBluePOIModel
+ _OBJC_METACLASS_$_RTTripClusterWaypointEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterWaypointEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTBluePOIModel
+ __OBJC_$_CLASS_METHODS_RTTripClusterWaypointEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterWaypointEnumerationOptions
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOIModel
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterWaypointEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTBluePOIModel
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterWaypointEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterWaypointEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOIModel
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterWaypointEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterWaypointEnumerationOptions
+ __OBJC_$_PROP_LIST_RTBluePOIModel
+ __OBJC_$_PROP_LIST_RTTripClusterWaypointEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterWaypointEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOIModel
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterWaypointEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterWaypointEnumerationOptions
+ __OBJC_CLASS_RO_$_RTBluePOIModel
+ __OBJC_CLASS_RO_$_RTTripClusterWaypointEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterWaypointEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTBluePOIModel
+ __OBJC_METACLASS_RO_$_RTTripClusterWaypointEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterWaypointEnumerationOptions
+ _objc_msgSend$creationDate
+ _objc_msgSend$featureToHashedApMapping
+ _objc_msgSend$hashSalt
+ _objc_msgSend$hashedApToModelMapping
+ _objc_msgSend$initWithCreationDate:forecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithIdentifier:featureToHashedApMapping:url:
+ _objc_msgSend$models
+ _objc_msgSend$url
- -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:]
- -[RTPredictedContextOptions initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:]
- _objc_msgSend$initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:
CStrings:
+ "@\"RTTripClusterWaypointEnumerationOptions\""
+ "@128@0:8@16@24@32@40@48Q56@64@72@80@88@96@104Q112d120"
+ "@64@0:8@16@24d32Q40@48@56"
+ "Invalid parameter not satisfying: featureToHashedApMapping"
+ "Invalid parameter not satisfying: url"
+ "RTBluePOIModel"
+ "RTTripClusterWaypointEnumerationContext"
+ "RTTripClusterWaypointEnumerationOptions"
+ "T@\"NSData\",R,N,V_hashSalt"
+ "T@\"NSDictionary\",R,N,V_featureToHashedApMapping"
+ "T@\"NSDictionary\",R,N,V_hashedApToModelMapping"
+ "T@\"NSSet\",R,N,V_models"
+ "T@\"NSString\",R,N,V_url"
+ "T@\"RTTripClusterWaypointEnumerationOptions\",R,N,V_options"
+ "Ti,N,V_tripSegmentSequence"
+ "Ti,N,V_tripSegmentSequenceMax"
+ "_featureToHashedApMapping"
+ "_hashSalt"
+ "_hashedApToModelMapping"
+ "_models"
+ "_url"
+ "batch size,%ld,end date,%@"
+ "creationDate, %@, forecastWindowDateInterval, %@, forecastWindowTimeInterval %f, filterContextTypeMask, %lu, filterLocations, %@, resultSortDescriptors, %@"
+ "featureToHashedApMapping"
+ "hashSalt"
+ "hashedApToModelMapping"
+ "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
+ "identifier, %@, muid, %lu, location, %@, applyPaySupport, %@, filtered, %@, fullyCoversTile, %@"
+ "identifier, %@, url, %@, featureToHashedApMapping count, %lu"
+ "initWithCreationDate:forecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
+ "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "initWithIdentifier:featureToHashedApMapping:url:"
+ "isDateWithinLast24Hours:"
+ "models"
+ "options,%@,offset,%lu"
+ "setTripSegmentSequence:"
+ "setTripSegmentSequenceMax:"
+ "url"
- "@104@0:8@16@24@32@40@48Q56@64@72@80Q88d96"
- "@56@0:8@16d24Q32@40@48"
- "Ti,R,N,V_tripSegmentSequence"
- "Ti,R,N,V_tripSegmentSequenceMax"
- "forecastWindowDateInterval, %@, forecastWindowTimeInterval %f, filterContextTypeMask, %lu, filterLocations, %@, resultSortDescriptors, %@"
- "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, apToModelMapping count, %lu, singlePOIMuid, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
- "identifier, %@, muid, %lu, location, %@, applyPaySupport, %@, filtered, %@, fullyCoversTile, %@, polygon, %@"
- "initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
- "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:"

```
