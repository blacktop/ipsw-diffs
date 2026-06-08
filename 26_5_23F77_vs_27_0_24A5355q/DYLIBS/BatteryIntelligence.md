## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-195.100.3.0.0
-  __TEXT.__text: 0x4478
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x62c
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x595
-  __TEXT.__oslogstring: 0x3e1
-  __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0x149
-  __TEXT.__objc_methname: 0xccb
-  __TEXT.__objc_methtype: 0x2cf
-  __TEXT.__objc_stubs: 0xa00
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x40
+208.0.0.0.0
+  __TEXT.__text: 0x5be4
+  __TEXT.__objc_methlist: 0x804
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x7c3
+  __TEXT.__oslogstring: 0x702
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__unwind_info: 0x278
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1f8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x1020
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0xd8
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__objc_const: 0x1448
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x6c
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF668AF2-E5D6-3D26-A2AB-A44B0D3B1C28
-  Functions: 150
-  Symbols:   646
-  CStrings:  327
+  UUID: 3344B64A-A509-36E9-9AE6-91BBF87A9E3B
+  Functions: 206
+  Symbols:   848
+  CStrings:  137
 
Symbols:
+ +[BIAccessoryEstimateInfo supportsSecureCoding]
+ -[BIAccessoryEstimateInfo .cxx_destruct]
+ -[BIAccessoryEstimateInfo description]
+ -[BIAccessoryEstimateInfo deviceName]
+ -[BIAccessoryEstimateInfo encodeWithCoder:]
+ -[BIAccessoryEstimateInfo estimate]
+ -[BIAccessoryEstimateInfo initWithCoder:]
+ -[BIAccessoryEstimateInfo nsuuid]
+ -[BIAccessoryEstimateInfo setDeviceName:]
+ -[BIAccessoryEstimateInfo setEstimate:]
+ -[BIAccessoryEstimateInfo setNsuuid:]
+ -[BIBatteryAnalysisAccessoryEstimateContainer .cxx_destruct]
+ -[BIBatteryAnalysisAccessoryEstimateContainer description]
+ -[BIBatteryAnalysisAccessoryEstimateContainer estimateInfo]
+ -[BIBatteryAnalysisAccessoryEstimateContainer lastUpdatedMonotonicTime]
+ -[BIBatteryAnalysisAccessoryEstimateContainer setEstimateInfo:]
+ -[BIBatteryAnalysisAccessoryEstimateContainer setLastUpdatedMonotonicTime:]
+ -[BIBatteryAnalysisClient accessoryEstimatesFetchError]
+ -[BIBatteryAnalysisClient accessoryEstimatesFromCache:]
+ -[BIBatteryAnalysisClient accessoryEstimatesFromCache:].cold.1
+ -[BIBatteryAnalysisClient accessoryEstimatesWithError:]
+ -[BIBatteryAnalysisClient accessoryEstimatesWithError:].cold.1
+ -[BIBatteryAnalysisClient accessoryEstimatesWithError:].cold.2
+ -[BIBatteryAnalysisClient accessoryEstimates]
+ -[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]
+ -[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:].cold.1
+ -[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:].cold.2
+ -[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:].cold.3
+ -[BIBatteryAnalysisClient registerForAccessoryEstimateUpdates]
+ -[BIBatteryAnalysisClient registerForAccessoryEstimateUpdates].cold.1
+ -[BIBatteryAnalysisClient setAccessoryEstimates:]
+ -[BIBatteryAnalysisClient setAccessoryEstimatesFetchError:]
+ -[BIBatteryAnalysisClient setTrackAccessoryEstimates:]
+ -[BIBatteryAnalysisClient trackAccessoryEstimates]
+ -[BIBatteryAnalysisClient updateAccessoryEstimates]
+ -[BIConnectedAccessoryInfo .cxx_destruct]
+ -[BIConnectedAccessoryInfo currentCapacity]
+ -[BIConnectedAccessoryInfo friendlyName]
+ -[BIConnectedAccessoryInfo nsuuid]
+ -[BIConnectedAccessoryInfo setCurrentCapacity:]
+ -[BIConnectedAccessoryInfo setFriendlyName:]
+ -[BIConnectedAccessoryInfo setNsuuid:]
+ GCC_except_table1
+ GCC_except_table11
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table6
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFRelease
+ _IOPSCopyPowerSourcesByTypePrecise
+ _IOPSCopyPowerSourcesList
+ _IOPSGetPowerSourceDescription
+ _OBJC_CLASS_$_BIAccessoryEstimateInfo
+ _OBJC_CLASS_$_BIBatteryAnalysisAccessoryEstimateContainer
+ _OBJC_CLASS_$_BIConnectedAccessoryInfo
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_BIAccessoryEstimateInfo._deviceName
+ _OBJC_IVAR_$_BIAccessoryEstimateInfo._estimate
+ _OBJC_IVAR_$_BIAccessoryEstimateInfo._nsuuid
+ _OBJC_IVAR_$_BIBatteryAnalysisAccessoryEstimateContainer._estimateInfo
+ _OBJC_IVAR_$_BIBatteryAnalysisAccessoryEstimateContainer._lastUpdatedMonotonicTime
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._accessoryEstimates
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._accessoryEstimatesFetchError
+ _OBJC_IVAR_$_BIBatteryAnalysisClient._trackAccessoryEstimates
+ _OBJC_IVAR_$_BIConnectedAccessoryInfo._currentCapacity
+ _OBJC_IVAR_$_BIConnectedAccessoryInfo._friendlyName
+ _OBJC_IVAR_$_BIConnectedAccessoryInfo._nsuuid
+ _OBJC_METACLASS_$_BIAccessoryEstimateInfo
+ _OBJC_METACLASS_$_BIBatteryAnalysisAccessoryEstimateContainer
+ _OBJC_METACLASS_$_BIConnectedAccessoryInfo
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_CLASS_METHODS_BIAccessoryEstimateInfo
+ __OBJC_$_CLASS_PROP_LIST_BIAccessoryEstimateInfo
+ __OBJC_$_INSTANCE_METHODS_BIAccessoryEstimateInfo
+ __OBJC_$_INSTANCE_METHODS_BIBatteryAnalysisAccessoryEstimateContainer
+ __OBJC_$_INSTANCE_METHODS_BIConnectedAccessoryInfo
+ __OBJC_$_INSTANCE_VARIABLES_BIAccessoryEstimateInfo
+ __OBJC_$_INSTANCE_VARIABLES_BIBatteryAnalysisAccessoryEstimateContainer
+ __OBJC_$_INSTANCE_VARIABLES_BIConnectedAccessoryInfo
+ __OBJC_$_PROP_LIST_BIAccessoryEstimateInfo
+ __OBJC_$_PROP_LIST_BIBatteryAnalysisAccessoryEstimateContainer
+ __OBJC_$_PROP_LIST_BIConnectedAccessoryInfo
+ __OBJC_CLASS_PROTOCOLS_$_BIAccessoryEstimateInfo
+ __OBJC_CLASS_RO_$_BIAccessoryEstimateInfo
+ __OBJC_CLASS_RO_$_BIBatteryAnalysisAccessoryEstimateContainer
+ __OBJC_CLASS_RO_$_BIConnectedAccessoryInfo
+ __OBJC_METACLASS_RO_$_BIAccessoryEstimateInfo
+ __OBJC_METACLASS_RO_$_BIBatteryAnalysisAccessoryEstimateContainer
+ __OBJC_METACLASS_RO_$_BIConnectedAccessoryInfo
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.194
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.194.cold.1
+ ___51-[BIBatteryAnalysisClient updateAccessoryEstimates]_block_invoke
+ ___51-[BIBatteryAnalysisClient updateAccessoryEstimates]_block_invoke.117
+ ___51-[BIBatteryAnalysisClient updateAccessoryEstimates]_block_invoke.117.cold.1
+ ___51-[BIBatteryAnalysisClient updateAccessoryEstimates]_block_invoke.cold.1
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.111
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.111.cold.1
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.198
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.198.cold.1
+ ___55-[BIBatteryAnalysisClient accessoryEstimatesWithError:]_block_invoke
+ ___62-[BIBatteryAnalysisClient registerForAccessoryEstimateUpdates]_block_invoke
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke.106
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke.106.cold.1
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke.108
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke.cold.1
+ ___67-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:]_block_invoke_2
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.196
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.196.cold.1
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_64_e8_32s40r48r56w_e5_v8?0lw56l8r40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16ls32l8r40l8r48l8
+ ___block_literal_global.37
+ ___block_literal_global.39
+ ___block_literal_global.43
+ ___getLogger_block_invoke
+ __logger
+ _getConnectedAccessoriesInfo
+ _getConnectedAccessoriesInfo.cold.1
+ _getConnectedAccessoriesInfo.cold.2
+ _getConnectedAccessoriesInfo.cold.3
+ _getConnectedAccessoryInfo
+ _getConnectedAccessoryInfo.cold.1
+ _getConnectedAccessoryInfo.cold.2
+ _getLogger
+ _getLogger.cold.1
+ _getLogger.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$accessoryEstimatesFromCache:
+ _objc_msgSend$accessoryEstimatesWithHandler:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$array
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$currentCapacity
+ _objc_msgSend$deviceName
+ _objc_msgSend$dictionary
+ _objc_msgSend$didUpdateAccessoryEstimates:error:
+ _objc_msgSend$estimateInfo
+ _objc_msgSend$initWithTargets:trackAccessoryEstimates:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$length
+ _objc_msgSend$nsuuid
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$registerForAccessoryEstimateUpdates
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setAccessoryEstimatesFetchError:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setCurrentCapacity:
+ _objc_msgSend$setDeviceName:
+ _objc_msgSend$setEstimateInfo:
+ _objc_msgSend$setNsuuid:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$updateAccessoryEstimates
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
- -[BIBatteryAnalysisClient initWithTargets:].cold.1
- -[BIBatteryAnalysisClient initWithTargets:].cold.2
- -[BIBatteryAnalysisClient initWithTargets:].cold.3
- GCC_except_table0
- GCC_except_table21
- GCC_except_table24
- GCC_except_table29
- GCC_except_table31
- GCC_except_table4
- GCC_except_table9
- ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.172
- ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.172.cold.1
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.87
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.87.cold.1
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.89
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.cold.1
- ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.92
- ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.92.cold.1
- ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.176
- ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.176.cold.1
- ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.174
- ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.174.cold.1
- ___block_literal_global.3
- ___block_literal_global.5
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "("
+ "<BIAccessoryEstimateInfo: nsuuid: %@, deviceName: %@, estimate: %@>"
+ "<BIBatteryAnalysisAccessoryEstimateContainer: estimateInfo: %@, lastUpdatedMonotonicTime: %lld ns>"
+ "Accessory '%@' not found"
+ "Accessory Identifier"
+ "Accessory Source"
+ "Accessory estimate for nsuuid %@ is stale (%.0f seconds old, threshold: %.0f seconds)"
+ "Accessory estimate tracking not enabled. Initialize with trackAccessoryEstimates:YES"
+ "Accessory estimate: %@, additionalInformation: %ld"
+ "Accessory estimates fetch error: %@"
+ "Accessory estimates updated - %lu devices"
+ "BIFrameworkUtilities"
+ "Called with nil/empty nsuuid"
+ "Client output for accessory estimates - %lu devices"
+ "Current Capacity"
+ "Failed to get power sources list"
+ "Failed to get power sources: status=%d"
+ "Failed to register for accessory estimate notifications with status 0x%x"
+ "Name"
+ "Notification received for accessory estimate update"
+ "Passing updated accessory estimates to delegate method"
+ "Skipping accessory - missing required fields"
+ "Type"
+ "Unknown Device"
+ "Wait time exceeded for accessory estimates"
+ "com.apple.batteryintelligenced.battery-analysis-client-accessory-estimate-update"
+ "com.apple.batteryintelligenced.battery-analysis-client-accessory-estimates"
+ "com.apple.batteryintelligenced.batteryanalysisaccessoryestimateupdated"
+ "deviceName"
+ "getConnectedAccessoriesInfo: Returning %lu accessories"
+ "nsuuid"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BIBatteryAnalysisDelegate>\""
- "@\"BIBatteryAnalysisOutput\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8q16^@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8q16"
- "B40@0:8q16d24^@32"
- "BIBatteryAnalysisContainer"
- "BIBatteryAnalysisManagerProtocol"
- "BIBatteryAnalysisOutput"
- "BIBatteryAnalysisProtocol"
- "BIBatteryAnalysisSharedResources"
- "BIBatteryAnalysisTargetDetails"
- "BIChargeTimeEstimatorOutput"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<BIBatteryAnalysisDelegate>\",W,N,V_delegate"
- "T@\"BIBatteryAnalysisOutput\",&,N,V_estimateObj"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSMutableDictionary\",&,N,V_targetOutputs"
- "T@\"NSMutableSet\",&,N,V_notificationTokens"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_logger"
- "T@\"NSSet\",&,N,V_targets"
- "T@\"NSString\",&,N,V_formattedEstimate"
- "T@\"NSString\",&,N,V_friendlyName"
- "T@\"NSString\",&,N,V_notificationName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,N,V_isEstimateOverridden"
- "TB,N,V_isFirstEstimate"
- "TB,R"
- "TQ,R"
- "Td,N,V_confidenceScore"
- "Td,N,V_estimate"
- "Tq,N,V_additionalInformation"
- "Tq,N,V_endSOC"
- "Tq,N,V_lastUpdatedMonotonicTime"
- "Tq,N,V_socAtEstimateTime"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_additionalInformation"
- "_confidenceScore"
- "_connection"
- "_delegate"
- "_endSOC"
- "_error"
- "_estimate"
- "_estimateObj"
- "_formattedEstimate"
- "_friendlyName"
- "_isEstimateOverridden"
- "_isFirstEstimate"
- "_lastUpdatedMonotonicTime"
- "_logger"
- "_notificationName"
- "_notificationTokens"
- "_queue"
- "_socAtEstimateTime"
- "_targetOutputs"
- "_targets"
- "activate"
- "adHocRunWithError:"
- "addObject:"
- "allKeys"
- "allowedUnits"
- "areTargetsValid:"
- "autorelease"
- "bundleForClass:"
- "chargeTime"
- "class"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didUpdateEstimateFor:newEstimate:error:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "estimateForTarget:withError:"
- "estimateForTarget:withHandler:"
- "estimateFromCache:withError:"
- "formattedEstimateForOutput:"
- "friendlyName"
- "getLocalizedStringForKey:"
- "hash"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithTargets:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTargetValid:"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "logger"
- "notificationName"
- "notificationTokens"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "queue"
- "registerForUpdatesToTarget:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "runAndReply:"
- "self"
- "set"
- "setAdditionalInformation:"
- "setAllowedUnits:"
- "setConfidenceScore:"
- "setConnection:"
- "setDelegate:"
- "setEndSOC:"
- "setError:"
- "setEstimate:"
- "setEstimateObj:"
- "setFormattedEstimate:"
- "setFriendlyName:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsEstimateOverridden:"
- "setIsFirstEstimate:"
- "setLastUpdatedMonotonicTime:"
- "setLogger:"
- "setNotificationName:"
- "setNotificationTokens:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setSocAtEstimateTime:"
- "setTargetOutputs:"
- "setTargets:"
- "setUnitsStyle:"
- "sharedEstimator"
- "sharedTargetDetails"
- "stringFromNumber:"
- "stringFromTimeInterval:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "targetOutputs"
- "targets"
- "unsignedIntValue"
- "updateEstimateForTarget:"
- "updateTarget:withEstimate:andReply:"
- "updateTarget:withEstimate:withError:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"BIBatteryAnalysisOutput\"@\"NSError\">24"
- "v40@0:8q16d24@?32"
- "v40@0:8q16d24@?<v@?B@\"NSError\">32"
- "zone"

```
