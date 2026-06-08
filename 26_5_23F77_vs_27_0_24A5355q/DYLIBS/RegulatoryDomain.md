## RegulatoryDomain

> `/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain`

```diff

-69.0.0.0.0
-  __TEXT.__text: 0x1197c
-  __TEXT.__auth_stubs: 0x960
+73.0.0.0.0
+  __TEXT.__text: 0x11288
   __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x92b
-  __TEXT.__swift5_typeref: 0x224
+  __TEXT.__cstring: 0x934
+  __TEXT.__swift5_typeref: 0x234
   __TEXT.__oslogstring: 0x259c
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_fieldmd: 0x50

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x34
+  __TEXT.__swift_as_cont: 0x50
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__unwind_info: 0x400
-  __TEXT.__eh_frame: 0x4e8
-  __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0x10ad
-  __TEXT.__objc_methtype: 0x32c
-  __TEXT.__objc_stubs: 0xec0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x218
+  __TEXT.__unwind_info: 0x410
+  __TEXT.__eh_frame: 0x4e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x1c0
   __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x728
   __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH.__objc_data: 0xb0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x248
+  __DATA.__data: 0x280
   __DATA.__common: 0x18
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x288
-  __DATA_DIRTY.__data: 0x88
+  __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 01564275-436A-3F23-8905-3FC63DCA3F3F
-  Functions: 271
-  Symbols:   197
-  CStrings:  477
+  UUID: 0EC7D8AE-E59E-38A3-BA2D-D9367C3A31F5
+  Functions: 275
+  Symbols:   211
+  CStrings:  245
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
CStrings:
- ".cxx_destruct"
- "@\"<RDXPCProtocol>\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@\"_TtC16RegulatoryDomain16RDStatusListener\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@40@0:8@16I24@28B36"
- "@92@0:8@16@24@32@40@48@56@64@72B80@84"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8I16"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "RDCachedData"
- "RDCommClient"
- "RDEstimate"
- "RDStatusShareWrapper"
- "RDXPCProtocol"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSString\",R,N,V_countryCode"
- "T@\"_TtC16RegulatoryDomain16RDStatusListener\",&,V_listener"
- "TB,R"
- "TB,R,N,V_isInDisputedArea"
- "UTF8String"
- "_TtC16RegulatoryDomain16RDStatusListener"
- "_TtC16RegulatoryDomain20RDStatusAvailability"
- "_combinedEstimate"
- "_countryCode"
- "_estimatesFromGeoIP"
- "_estimatesFromLocation"
- "_estimatesFromNearbyCells"
- "_estimatesFromServingCell"
- "_estimatesFromWiFiAPs"
- "_isInDisputedArea"
- "_lastKnownCombinedEstimate"
- "_listener"
- "_localOnlyEstimates"
- "_locationLocalEstimateIsInDisputedArea"
- "_peerDeviceLocalEstimates"
- "_priority"
- "_timestamp"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "allValues"
- "allocWithZone:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "clearDataCache"
- "clearStatusSharedWithPeers"
- "componentsJoinedByString:"
- "computeLocalCountryCode"
- "connection"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createCacheAtPath:"
- "createCacheDirAtPath:"
- "createCacheDirectoryIfNeeded:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentEstimates"
- "dataWithContentsOfFile:options:error:"
- "dealloc"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "defaultTimeZone"
- "description"
- "deviceIDs"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "estimateArrayFromStrings:withPriority:andTimestamp:disputed:"
- "estimatesForMontara"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "firstObject"
- "getCacheDirPath"
- "getCacheDirPathForUnitTest"
- "getCacheDirPathLegacy"
- "getCombinedEstimate"
- "getEstimateForPeerDeviceWithID:"
- "getGeoIPLocalEstimates"
- "getLastKnownCombinedEstimate"
- "getLocalOnlyEstimates"
- "getPriority"
- "getUserPath:"
- "hasLocalStatusKit"
- "hash"
- "init"
- "initWithCoder:"
- "initWithCountryCode:priority:timestamp:inDisputedArea:"
- "initWithCountryCodeFromLocation:fromServingCell:fromNearbyCell:fromWiFi:fromGeoIP:localEstimates:combinedEstimate:lastKnownCombinedEstimate:locationLocalEstimateInDisputedArea:peerEstimates:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "isInDisputedArea"
- "lastKnownEstimates"
- "length"
- "listenForStatus:"
- "listenForStatusWithHandler:completionHandler:"
- "listenForStatuses:"
- "listenForStatusesWithHandler:completionHandler:"
- "listener"
- "loadCache"
- "loadCache:"
- "loadCacheForUnitTest"
- "localEstimatesForPriority:"
- "localizedDescription"
- "localizedFailureReason"
- "mutableCopy"
- "now"
- "numberWithBool:"
- "numberWithLong:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "pathWithComponents:"
- "ping"
- "postResultsToEligibilityEngine"
- "priorityIsAtLeast:"
- "recompute"
- "recompute:"
- "remoteObjectProxyWithErrorHandler:"
- "removeEstimateForPeerDeviceWithID:"
- "removeEstimateForPeerDeviceWithIDForUnitTest:"
- "removeObjectForKey:"
- "resume"
- "saveCache"
- "saveCache:"
- "saveCacheForUnitTest"
- "server"
- "set"
- "setAttributes:ofItemAtPath:error:"
- "setCacheLockState:"
- "setCountriesFromGeoIP:"
- "setCountriesFromGeoIP:forUnitTest:"
- "setCountriesFromGeoIPForUnitTest:"
- "setCountriesFromLocation:"
- "setCountriesFromLocation:forUnitTest:isDisputed:"
- "setCountriesFromLocation:isInDisputedArea:"
- "setCountriesFromLocationForUnitTest:isDisputed:"
- "setCountriesFromNearbyCells:"
- "setCountriesFromNearbyCells:forUnitTest:"
- "setCountriesFromNearbyCellsForUnitTest:"
- "setCountriesFromServingCell:"
- "setCountriesFromServingCell:forUnitTest:"
- "setCountriesFromServingCellForUnitTest:"
- "setCountriesFromWiFiAPs:"
- "setCountriesFromWiFiAPs:forUnitTest:"
- "setCountriesFromWiFiAPsForUnitTest:"
- "setCountryFromLocation:"
- "setCountryFromMCC:"
- "setCountryFromWiFiAPs:"
- "setDateFormat:"
- "setEstimate:forPeerDeviceWithID:"
- "setEstimate:forPeerDeviceWithID:isUnitTest:"
- "setEstimateForUnitTest:forPeerDeviceWithID:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setListener:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setTimeZone:"
- "setWithObjects:"
- "shareStatusWithPeers"
- "sortPreferredOrder:"
- "sortUsingComparator:"
- "statusClient"
- "statusKey"
- "statusesKey"
- "stopListening"
- "stringFromDate:"
- "stringWithFormat:"
- "stringsFromRDEstimateArray:"
- "supportsSecureCoding"
- "timestamp"
- "triggerUpdateToEligibilityEngine"
- "unarchivedObjectOfClasses:fromData:error:"
- "update:withCountryCode:"
- "update:withDict:"
- "update:withListOfCountryCodes:"
- "updatePeer:withCountryCode:priority:andTimestamp:"
- "updatePeer:withEstimate:"
- "updatePeer:withInfo:"
- "uppercaseString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSString\"16@\"NSArray\"24"
- "v32@0:8@\"NSString\"16@\"RDEstimate\"24"
- "v32@0:8@16@24"
- "v32@0:8@16B24B28"
- "v32@0:8@?<v@?@\"NSString\"@\"NSArray\">16@?<v@?@\"NSError\">24"
- "v32@0:8@?<v@?@\"NSString\"@\"NSDictionary\">16@?<v@?@\"NSError\">24"
- "v32@0:8q16@\"NSArray\"24"
- "v32@0:8q16@\"NSDictionary\"24"
- "v32@0:8q16@\"NSString\"24"
- "v32@0:8q16@24"
- "v36@0:8@16@24B32"
- "v44@0:8@\"NSString\"16@\"NSString\"24i32@\"NSDate\"36"
- "v44@0:8@16@24i32@36"
- "writeToFile:options:error:"

```
