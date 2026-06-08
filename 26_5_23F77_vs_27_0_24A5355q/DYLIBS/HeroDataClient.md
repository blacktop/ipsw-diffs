## HeroDataClient

> `/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient`

```diff

-627.13.0.1.0
-  __TEXT.__text: 0x5228
-  __TEXT.__auth_stubs: 0x2e0
+658.0.9.0.0
+  __TEXT.__text: 0x5168
   __TEXT.__objc_methlist: 0x7f4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x20a
+  __TEXT.__cstring: 0x211
   __TEXT.__oslogstring: 0xef
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methname: 0xfc4
-  __TEXT.__objc_methtype: 0x43b
-  __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0xbc0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46EBF2B8-B40F-3401-9EC6-727A4F27096D
-  Functions: 153
-  Symbols:   600
-  CStrings:  316
+  UUID: 946E3B6A-E1D2-37A0-956C-FEC80A7BD550
+  Functions: 149
+  Symbols:   594
+  CStrings:  54
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retain_x22
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CPSClipMetadata\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"PBCodable\"16@0:8"
- "@100@0:8Q16@24d32d40Q48Q56B64d68@76@84@92"
- "@108@0:8Q16@24d32d40Q48Q56B64d68@76@84@92@100"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSData\"16"
- "@24@0:8@\"PBCodable\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@60@0:8@16d24d32Q40Q48B56"
- "@60@0:8Q16d24d32Q40Q48B56"
- "@92@0:8Q16@24d32d40Q48Q56B64d68@76@84"
- "ATXHeroData"
- "ATXHeroDataClient"
- "ATXHeroDataXPCInterface"
- "ATXPBHeroAppPrediction"
- "ATXProtoBufWrapper"
- "ATXSuggestionExecutableProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B52@0:8B16@20@28@36q44"
- "B56@0:8@16@24@32@40q48"
- "B56@0:8d16@24@32@40q48"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"CPSClipMetadata\",&,N,V_clipMetadata"
- "T@\"NSData\",&,N,V_clipMetadata"
- "T@\"NSNumber\",&,N,V_poiMuid"
- "T@\"NSString\",&,N,V_bundleId"
- "T@\"NSString\",&,N,V_poiCategory"
- "T@\"NSString\",&,N,V_urlHash"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N"
- "TB,N,V_isTouristApp"
- "TB,R"
- "TB,R,N"
- "TQ,N,V_adamId"
- "TQ,N,V_poiMuid"
- "TQ,N,V_radiusInMeters"
- "TQ,N,V_rank"
- "TQ,R"
- "Td,N,V_latitude"
- "Td,N,V_latitudeAtPredictionTime"
- "Td,N,V_longitude"
- "Td,N,V_longitudeAtPredictionTime"
- "Td,N,V_score"
- "Tq,N,V_adamId"
- "Tq,N,V_radius"
- "Tq,N,V_rank"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_adamId"
- "_bundleId"
- "_clipMetadata"
- "_has"
- "_isTouristApp"
- "_latitude"
- "_latitudeAtPredictionTime"
- "_longitude"
- "_longitudeAtPredictionTime"
- "_poiCategory"
- "_poiMuid"
- "_radius"
- "_radiusInMeters"
- "_rank"
- "_score"
- "_setError"
- "_urlHash"
- "_xpcConnection"
- "addConfirmForAppClipWithHeroAppPrediction:completion:"
- "addHardRejectForAppClipWithHeroAppPrediction:completion:"
- "addSoftRejectForAppClipWithHeroAppPrediction:completion:"
- "allocWithZone:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autorelease"
- "checkAndReportDecodingFailureIfNeededForBOOL:key:coder:errorDomain:errorCode:"
- "checkAndReportDecodingFailureIfNeededFordouble:key:coder:errorDomain:errorCode:"
- "checkAndReportDecodingFailureIfNeededForid:key:coder:errorDomain:errorCode:"
- "class"
- "clipBundleID"
- "clipURL"
- "conformsToProtocol:"
- "containsValueForKey:"
- "copy"
- "copyClipMetadata:"
- "copyTo:"
- "copyWithZone:"
- "d"
- "d16@0:8"
- "data"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "donateHeroAppPredictions:completion:"
- "encodeAsProto"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error"
- "failWithError:"
- "feedbackScoreForAppClipWithHeroAppPrediction:completion:"
- "getBytes:range:"
- "getCurrentHeroPoiCategoryWithCompletion:"
- "hasAdamId"
- "hasBundleId"
- "hasClipMetadata"
- "hasError"
- "hasIsTouristApp"
- "hasLatitude"
- "hasLatitudeAtPredictionTime"
- "hasLongitude"
- "hasLongitudeAtPredictionTime"
- "hasPoiCategory"
- "hasPoiMuid"
- "hasRadius"
- "hasRank"
- "hasScore"
- "hasUrlHash"
- "hash"
- "init"
- "initWithCoder:"
- "initWithData:"
- "initWithDomain:code:userInfo:"
- "initWithFloat:"
- "initWithFormat:"
- "initWithMachServiceName:options:"
- "initWithPredictedAdamId:bundleId:latitude:longitude:radiusInMeters:rank:isTouristApp:score:urlHash:clipMetadata:"
- "initWithPredictedAdamId:bundleId:latitude:longitude:radiusInMeters:rank:isTouristApp:score:urlHash:clipMetadata:poiCategory:"
- "initWithPredictedAdamId:bundleId:latitude:longitude:radiusInMeters:rank:isTouristApp:score:urlHash:clipMetadata:poiCategory:poiMuid:"
- "initWithPredictedAdamId:latitude:longitude:radiusInMeters:rank:isTouristApp:"
- "initWithPredictedBundleId:latitude:longitude:radiusInMeters:rank:isTouristApp:"
- "initWithProto:"
- "initWithProtoData:"
- "interfaceWithProtocol:"
- "invalidate"
- "isClipMetadataEqual:other:"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "mergeFrom:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "openAppClipWithHeroAppPrediction:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "position"
- "proto"
- "q"
- "q16@0:8"
- "radiusInMeters"
- "readFrom:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAdamId:"
- "setBundleId:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClipMetadata:"
- "setHasAdamId:"
- "setHasIsTouristApp:"
- "setHasLatitude:"
- "setHasLatitudeAtPredictionTime:"
- "setHasLongitude:"
- "setHasLongitudeAtPredictionTime:"
- "setHasPoiMuid:"
- "setHasRadius:"
- "setHasRank:"
- "setHasScore:"
- "setInterruptionHandler:"
- "setIsTouristApp:"
- "setLatitude:"
- "setLatitudeAtPredictionTime:"
- "setLongitude:"
- "setLongitudeAtPredictionTime:"
- "setObject:forKey:"
- "setPoiCategory:"
- "setPoiMuid:"
- "setPosition:"
- "setRadius:"
- "setRadiusInMeters:"
- "setRank:"
- "setRemoteObjectInterface:"
- "setScore:"
- "setUrlHash:"
- "setWithObjects:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"ATXHeroData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"ATXHeroData\"16@?<v@?@\"NSError\"d>24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "writeTo:"
- "zone"
- "{?=\"adamId\"b1\"latitude\"b1\"latitudeAtPredictionTime\"b1\"longitude\"b1\"longitudeAtPredictionTime\"b1\"poiMuid\"b1\"radius\"b1\"rank\"b1\"score\"b1\"isTouristApp\"b1}"

```
