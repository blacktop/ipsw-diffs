## ShazamInsights

> `/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights`

```diff

-426.5.3.0.0
-  __TEXT.__text: 0x3a9c
-  __TEXT.__auth_stubs: 0x2c0
+427.0.33.0.0
+  __TEXT.__text: 0x394c
   __TEXT.__objc_methlist: 0x5d0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x386
+  __TEXT.__cstring: 0x390
   __TEXT.__oslogstring: 0xb5
   __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0x159
-  __TEXT.__objc_methname: 0x10d9
-  __TEXT.__objc_methtype: 0x3a2
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 904D4066-8EAF-35C3-A0A4-47F940683013
+  UUID: 2FA9272A-EA50-3A67-A8E9-DD25F9B1E967
   Functions: 107
-  Symbols:   538
-  CStrings:  328
+  Symbols:   542
+  CStrings:  69
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
Functions:
~ +[SHInsightsConfiguration fetchSharedInstanceWithCompletion:] : 268 -> 264
~ ___61+[SHInsightsConfiguration fetchSharedInstanceWithCompletion:]_block_invoke.38 : 216 -> 168
~ +[SHInsightsConfiguration bagContract] : 84 -> 68
~ -[SHInsightsConfiguration init] : 108 -> 104
~ -[SHInsightsConfiguration initWithBagContract:] : 108 -> 116
~ -[SHInsightsConfiguration tracksClusterEndpointForStorefront:completionHandler:] : 188 -> 196
~ ___80-[SHInsightsConfiguration tracksClusterEndpointForStorefront:completionHandler:]_block_invoke : 176 -> 164
~ ___71-[SHInsightsConfiguration artistsClusterEndpointWithCompletionHandler:]_block_invoke : 128 -> 124
~ -[SHInsightsConfiguration geoChartsEndpointForDate:geoHash:completionHandler:] : 216 -> 236
~ ___78-[SHInsightsConfiguration geoChartsEndpointForDate:geoHash:completionHandler:]_block_invoke : 168 -> 164
~ -[SHInsightsConfiguration fillInTokenizedURL:date:geoHash:] : 352 -> 344
~ -[SHInsightsConfiguration tokenizedURLForBagPathKey:completionHandler:] : 216 -> 224
~ ___71-[SHInsightsConfiguration tokenizedURLForBagPathKey:completionHandler:]_block_invoke_2 : 264 -> 248
~ -[SHCDNDataFetcher initWithNetworkRequester:] : 108 -> 116
~ -[SHCDNDataFetcher clusterDataAtURL:forLocation:date:completionHandler:] : 244 -> 256
~ -[SHDataFetcherFileInfo initWithData:suggestedFileName:] : 144 -> 152
~ -[SHDataFetcherFileInfo initWithDataURL:suggestedFileName:] : 144 -> 152
~ -[SHDataFetcherFileInfo initWithDataURL:] : 100 -> 92
~ -[SHDataFetcherFileInfo compressionType] : 144 -> 132
~ -[SHDataFetcherFileInfo suggestedExtension] : 128 -> 116
~ -[SHDataFetcherFileInfo data] : 116 -> 112
~ -[SHDataFetcherFileInfo setCreationDate:] : 64 -> 12
~ -[SHInsightsNetworkRequester response:data:error:] : 436 -> 388
~ -[SHLocalDataFetcher clusterDataAtURL:forLocation:date:completionHandler:] : 296 -> 288
~ -[CLLocation(Geohash) sh_roundCoordinateValuesToGeohashOfLength:] : 88 -> 84
~ -[CLLocation(Geohash) sh_geohashOfLength:] : 384 -> 388
~ -[CLLocation(Geohash) sh_geoHashToCoordinates:] : 524 -> 472
~ -[SHTimeAndPlaceAffinityGroup initWithRegions:affinityGroup:] : 144 -> 152
~ -[SHTimeAndPlaceAffinityGroup geohashKeyedRegions] : 444 -> 424
~ -[SHTimeAndPlaceAffinityGroup regionsForGeohash:] : 552 -> 532
~ -[SHTimeAndPlaceController affinityGroupsFromData:atLocation:onDate:configuration:completionHandler:] : 344 -> 352
~ ___101-[SHTimeAndPlaceController affinityGroupsFromData:atLocation:onDate:configuration:completionHandler:]_block_invoke : 492 -> 484
~ +[SHTimeAndPlaceServerResponseParser regionAffinityGroupsFromServerData:error:] : 1184 -> 1148
~ -[SHAffinityGroup initWithType:cohesionLevel:] : 128 -> 124
~ -[SHAffinityGroup appendMediaItem:] : 100 -> 96
~ -[SHAffinityGroup mediaItems] : 76 -> 72
~ -[SHAffinityGroup setMutableMediaItems:] : 64 -> 12
~ +[SHAffinityGroupQuery affinityGroupsForLocation:atDate:completionHandler:] : 224 -> 232
~ +[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:] : 228 -> 256
~ ___89+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:]_block_invoke : 320 -> 304
~ ___89+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:]_block_invoke_2 : 312 -> 308
~ ___89+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:]_block_invoke_3 : 184 -> 172
~ -[SHStubbedNetworkRequester initWithHTTPResponse:requestData:downloadFileURL:] : 172 -> 188
~ +[SHInsightsError errorWithCode:underlyingError:keyOverrides:] : 252 -> 244
~ -[SHRegion initWithGeohash:] : 108 -> 116
~ -[SHRegion initWithLocation:] : 108 -> 116
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SHDataFetcher>\""
- "@\"<SHNetworkRequester>\""
- "@\"CLLocation\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSHTTPURLResponse\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"SHAffinityGroup\""
- "@\"SHBagContract\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@32@0:8q16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8q16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Geohash"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "Q16@0:8"
- "SHAffinityGroup"
- "SHAffinityGroupQuery"
- "SHCDNDataFetcher"
- "SHDataFetcher"
- "SHDataFetcherFileInfo"
- "SHInsightsConfiguration"
- "SHInsightsError"
- "SHInsightsNetworkRequester"
- "SHLocalDataFetcher"
- "SHNetworkRequester"
- "SHRegion"
- "SHStubbedNetworkRequester"
- "SHTimeAndPlaceAffinityGroup"
- "SHTimeAndPlaceController"
- "SHTimeAndPlaceServerResponseParser"
- "T#,R"
- "T@\"<SHDataFetcher>\",R,N,V_dataFetcher"
- "T@\"<SHNetworkRequester>\",R,N,V_networkRequester"
- "T@\"CLLocation\",R,N,V_location"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_regions"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSData\",R,N,V_requestData"
- "T@\"NSDate\",&,N,V_creationDate"
- "T@\"NSDictionary\",R,N,V_geohashKeyedRegions"
- "T@\"NSHTTPURLResponse\",R,N,V_httpResponse"
- "T@\"NSMutableArray\",&,N,V_mutableMediaItems"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_mimeType"
- "T@\"NSString\",C,N,V_storefront"
- "T@\"NSString\",C,N,V_uniqueHash"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_geohash"
- "T@\"NSString\",R,C,N,V_suggestedFileName"
- "T@\"NSURL\",R,N,V_dataFilePathURL"
- "T@\"NSURL\",R,N,V_downloadFileURL"
- "T@\"SHAffinityGroup\",R,N,V_affinityGroup"
- "T@\"SHBagContract\",R,N,V_bagContract"
- "TQ,R"
- "Ti,R,N"
- "Tq,R,N,V_cohesionLevel"
- "Tq,R,N,V_groupType"
- "URLRepresentation"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_affinityGroup"
- "_bagContract"
- "_cohesionLevel"
- "_creationDate"
- "_data"
- "_dataFetcher"
- "_dataFilePathURL"
- "_downloadFileURL"
- "_geohash"
- "_geohashKeyedRegions"
- "_groupType"
- "_httpResponse"
- "_location"
- "_mimeType"
- "_mutableMediaItems"
- "_networkRequester"
- "_regions"
- "_requestData"
- "_storefront"
- "_suggestedFileName"
- "_uniqueHash"
- "addBagKey:defaultValue:"
- "addObject:"
- "affinityGroup"
- "affinityGroupsForLocation:atDate:completionHandler:"
- "affinityGroupsForLocation:atDate:configuration:completionHandler:"
- "affinityGroupsFromData:atLocation:onDate:configuration:completionHandler:"
- "appendMediaItem:"
- "array"
- "artistsCachedDataMaxAgeWithCompletionHandler:"
- "artistsClusterEndpointWithCompletionHandler:"
- "artistsEnabledWithCompletionHandler:"
- "autorelease"
- "bagContract"
- "booleanBackedByStringForKey:completionHandler:"
- "class"
- "clusterDataAtURL:forLocation:date:completionHandler:"
- "cohesionLevel"
- "components:fromDate:"
- "compressionType"
- "conformsToProtocol:"
- "coordinate"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creationDate"
- "data"
- "dataFetcher"
- "dataFetcherForSourceURL:"
- "dataFilePathURL"
- "dataTaskWithRequest:completionHandler:"
- "dataWithContentsOfURL:"
- "debugDescription"
- "description"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleBackedByStringForKey:completionHandler:"
- "downloadFileURL"
- "downloadResourceFromRequest:completionHandler:"
- "downloadTaskWithRequest:completionHandler:"
- "errorWithCode:underlyingError:"
- "errorWithCode:underlyingError:keyOverrides:"
- "errorWithDomain:code:userInfo:"
- "fetchSharedInstanceWithCompletion:"
- "fileURLWithPath:isDirectory:"
- "fillInTokenizedURL:date:geoHash:"
- "geoChartsEndpointForDate:geoHash:completionHandler:"
- "geoHashLengthsWithCompletionHandler:"
- "geohash"
- "geohashKeyedRegions"
- "groupType"
- "hasPrefix:"
- "hash"
- "httpResponse"
- "i16@0:8"
- "init"
- "initWithBagContract:"
- "initWithBaseDictionaryKey:profile:profileVersion:"
- "initWithCString:encoding:"
- "initWithCalendarIdentifier:"
- "initWithData:encoding:"
- "initWithData:suggestedFileName:"
- "initWithDataURL:"
- "initWithDataURL:suggestedFileName:"
- "initWithGeohash:"
- "initWithHTTPResponse:requestData:downloadFileURL:"
- "initWithLocation:"
- "initWithNetworkRequester:"
- "initWithRegions:affinityGroup:"
- "initWithString:"
- "initWithType:cohesionLevel:"
- "integerBackedByStringForKey:completionHandler:"
- "isEqual:"
- "isFileURL"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastPathComponent"
- "length"
- "loadBaseDictionary:"
- "location"
- "mediaItemWithProperties:"
- "mediaItems"
- "messageForCode:"
- "mimeType"
- "mutableMediaItems"
- "networkRequester"
- "objectForKeyedSubscript:"
- "pathExtension"
- "performRequest:completionHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "regionAffinityGroupsFromServerData:error:"
- "regions"
- "regionsForGeohash:"
- "release"
- "requestData"
- "requestWithURL:"
- "respondsToSelector:"
- "response:data:error:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setCreationDate:"
- "setMimeType:"
- "setMutableMediaItems:"
- "setObject:forKeyedSubscript:"
- "setStorefront:"
- "setUniqueHash:"
- "setValue:forKey:"
- "setValuesForKeysWithDictionary:"
- "sh_geoHashToCoordinates:"
- "sh_geohashOfLength:"
- "sh_roundCoordinateValuesToGeohashOfLength:"
- "sh_toGeohash"
- "sharedSession"
- "statusCode"
- "storefront"
- "stringForKey:withCompletionHandler:"
- "stringWithFormat:"
- "substringToIndex:"
- "suggestedExtension"
- "suggestedFileName"
- "suggestedFilename"
- "superclass"
- "supportedCompressionTypeFromFilePathExtension:"
- "tokenizedURLForBagPathKey:completionHandler:"
- "tracksCachedDataMaxAgeWithCompletionHandler:"
- "tracksClusterEndpointForStorefront:completionHandler:"
- "tracksEnabledWithCompletionHandler:"
- "uniqueHash"
- "updateToken:withValue:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSURLRequest\"16@?<v@?@\"NSHTTPURLResponse\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSURLRequest\"16@?<v@?@\"NSHTTPURLResponse\"@\"NSURL\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURL\"16@\"CLLocation\"24@\"NSDate\"32@?<v@?@\"SHDataFetcherFileInfo\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "valueForHTTPHeaderField:"
- "weekOfYear"
- "year"
- "zone"
- "{CLLocationCoordinate2D=dd}24@0:8@16"
- "{CLLocationCoordinate2D=dd}24@0:8Q16"

```
