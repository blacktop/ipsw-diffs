## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing`

```diff

-206.0.7.0.0
-  __TEXT.__text: 0xc034
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1078
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0xcfd
-  __TEXT.__oslogstring: 0x11df
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__unwind_info: 0x450
-  __TEXT.__objc_classname: 0x243
-  __TEXT.__objc_methname: 0x25bf
-  __TEXT.__objc_methtype: 0x2fc
-  __TEXT.__objc_stubs: 0x2300
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+255.0.0.0.0
+  __TEXT.__text: 0x105c8
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x150c
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x101b
+  __TEXT.__oslogstring: 0x1333
+  __TEXT.__gcc_except_tab: 0x328
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__objc_classname: 0x29e
+  __TEXT.__objc_methname: 0x30c1
+  __TEXT.__objc_methtype: 0x53b
+  __TEXT.__objc_stubs: 0x2920
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x500
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac8
+  __DATA_CONST.__objc_selrefs: 0xd88
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x1c80
+  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__objc_const: 0x2390
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x18
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x14c
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 60F22FDC-40ED-3DEF-ADAF-39F41604F370
-  Functions: 393
-  Symbols:   1537
-  CStrings:  921
+  UUID: F900ED6D-9173-33B3-894C-AB0EBA8BD6BF
+  Functions: 511
+  Symbols:   1924
+  CStrings:  1193
 
Symbols:
+ +[MOContextPredicate contextPredicateForContextType:withMetadata:startDate:endDate:]
+ +[MOContextPredicate contextPredicateForContextType:withMetadata:startDate:endDate:aroundLocation:withDistanceThreshold:]
+ +[MOContextPredicate supportsSecureCoding]
+ +[MOContextPredicateBuilder createAndPredicate:]
+ +[MOContextPredicateBuilder createNotPredicate:]
+ +[MOContextPredicateBuilder createOrPredicate:]
+ +[MOContextPredicateBuilder createPredicateForValue:inCollection:]
+ +[MOContextPredicateBuilder createPredicateWithLeftExpression:rightExpression:operation:]
+ +[MOContextPredicateBuilder disassemblePredicate:]
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.1
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.2
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.3
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.4
+ +[MOContextPredicateBuilder disassemblePredicate:].cold.5
+ +[MOContextPredicateBuilder extractFirstValueForKeyPath:fromPredicates:]
+ +[MOContextPredicateBuilder inspectExpression:]
+ +[MOContextPredicateBuilder inspectExpression:].cold.1
+ +[MOContextPredicateBuilder inspectExpression:].cold.2
+ +[MOContextPredicateBuilder inspectExpression:].cold.3
+ +[MOContextPredicateBuilder inspectExpression:].cold.4
+ +[MOContextPredicateBuilder inspectExpression:].cold.5
+ +[MOContextPredicateBuilder inspectExpression:].cold.6
+ +[MOContextPredicateBuilder inspectExpression:].cold.7
+ +[MOContextPredicateBuilder inspectExpression:].cold.8
+ +[MOContextPredicateBuilder inspectExpression:].cold.9
+ +[MOContextPredicateBuilder predicateOperatorFromType:]
+ +[MOContextPredicateBuilder stringForCompoundPredicateType:]
+ +[MOContextPredicateBuilder stringForOperatorType:]
+ +[MODefaultsManager isExtendedLogEnabled:forDetaultsManager:]
+ +[MODefaultsManager momentsDaemonDefaults]
+ +[MODefaultsManager momentsDaemonDefaults].cold.1
+ +[NSError(MOError) errorUsingError:withUnderyingError:]
+ -[MOConnection .cxx_destruct]
+ -[MOConnection callBlock:onInterruption:]
+ -[MOConnection delegate]
+ -[MOConnection getConnectionName]
+ -[MOConnection initWithName:]
+ -[MOConnection onConnectionInterrupted]
+ -[MOConnection runBlockCompleted:]
+ -[MOConnection runBlockStarted:withConnectionError:]
+ -[MOConnection setDelegate:]
+ -[MOConnectionManager .cxx_destruct]
+ -[MOConnectionManager _callProxy:usingBlock:onError:]
+ -[MOConnectionManager _callProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager _getActiveConnection]
+ -[MOConnectionManager _getActiveConnection].cold.1
+ -[MOConnectionManager _getActiveConnection].cold.2
+ -[MOConnectionManager _getActiveConnection].cold.3
+ -[MOConnectionManager _getSingleCallHandler:]
+ -[MOConnectionManager _makeConnectionErrorWithReason:]
+ -[MOConnectionManager _postProxy:usingBlock:onError:]
+ -[MOConnectionManager _postProxyProvider:usingBlock:onError:]
+ -[MOConnectionManager callAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager callSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager dealloc]
+ -[MOConnectionManager delegate]
+ -[MOConnectionManager getAsyncProxyProvider]
+ -[MOConnectionManager getConnectionName]
+ -[MOConnectionManager getSyncProxyProvider]
+ -[MOConnectionManager initWithName:usingDelegate:]
+ -[MOConnectionManager invalidate]
+ -[MOConnectionManager postAsyncProxyUsingBlock:onError:]
+ -[MOConnectionManager postSyncProxyUsingBlock:onError:]
+ -[MOConnectionManager setDelegate:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:]
+ -[MOConnectionManager withProxyProvider:proxyHandler:onError:].cold.1
+ -[MOContext isWithinDistanceFromLocation:maxDistance:]
+ -[MOContextActivityMetaData initWithActivityType:]
+ -[MOContextFetchOptions batchSize]
+ -[MOContextFetchOptions setBatchSize:]
+ -[MOContextLocationMetaData deserializeCLLocationObject:]
+ -[MOContextLocationMetaData initWithPlace:city:location:]
+ -[MOContextLocationMetaData location]
+ -[MOContextLocationMetaData serializeCLLocationObject]
+ -[MOContextPredicate .cxx_destruct]
+ -[MOContextPredicate copyWithZone:]
+ -[MOContextPredicate encodeWithCoder:]
+ -[MOContextPredicate fetchRequestPredicate]
+ -[MOContextPredicate filterCriteriaMap]
+ -[MOContextPredicate initWithCoder:]
+ -[MOContextPredicate initWithPredicate:filter:metadataTypes:]
+ -[MOContextPredicate metadataTypes]
+ -[MOContextPredicate setFetchRequestPredicate:]
+ -[MOContextPredicate setFilterCriteriaMap:]
+ -[MOContextPredicate setMetadataTypes:]
+ -[MOContextTimeMetaData endDate]
+ -[MOContextTimeMetaData initWithStartDate:endDate:timeReferenceString:]
+ -[MOContextTimeMetaData setEndDate:]
+ -[MOContextTimeMetaData setStartDate:]
+ -[MOContextTimeMetaData startDate]
+ -[MOPersonalizedSensingServiceManager fetchContextWithOptions:predicates:authorizedTypes:withReply:]
+ -[MOPersonalizedSensingServiceManager makeNewConnectionWithInterfaceFor:]
+ -[NSString(MOExtensions) mask]
+ GCC_except_table2
+ GCC_except_table24
+ GCC_except_table36
+ GCC_except_table9
+ _CLLocationCoordinate2DMake
+ _MOContextFilterKeyLocation
+ _MOErrorDomain
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_CLLocation
+ _OBJC_CLASS_$_MOConnection
+ _OBJC_CLASS_$_MOConnectionManager
+ _OBJC_CLASS_$_MOContextPredicate
+ _OBJC_CLASS_$_MOContextPredicateBuilder
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_NSExpression
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_IVAR_$_MOConnection._delegate
+ _OBJC_IVAR_$_MOConnection._interruptActive
+ _OBJC_IVAR_$_MOConnection._name
+ _OBJC_IVAR_$_MOConnection._pendingRequestCounter
+ _OBJC_IVAR_$_MOConnection._pendingRequests
+ _OBJC_IVAR_$_MOConnectionManager._connectionName
+ _OBJC_IVAR_$_MOConnectionManager._delegate
+ _OBJC_IVAR_$_MOConnectionManager._mo_connection
+ _OBJC_IVAR_$_MOConnectionManager._xpc_connection
+ _OBJC_IVAR_$_MOContextFetchOptions._batchSize
+ _OBJC_IVAR_$_MOContextLocationMetaData._location
+ _OBJC_IVAR_$_MOContextPredicate._fetchRequestPredicate
+ _OBJC_IVAR_$_MOContextPredicate._filterCriteriaMap
+ _OBJC_IVAR_$_MOContextPredicate._metadataTypes
+ _OBJC_IVAR_$_MOContextTimeMetaData._endDate
+ _OBJC_IVAR_$_MOContextTimeMetaData._startDate
+ _OBJC_IVAR_$_MOPersonalizedSensingServiceManager.connectionManager
+ _OBJC_METACLASS_$_MOConnection
+ _OBJC_METACLASS_$_MOConnectionManager
+ _OBJC_METACLASS_$_MOContextPredicate
+ _OBJC_METACLASS_$_MOContextPredicateBuilder
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_MOError
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_MOExtensions
+ __OBJC_$_CATEGORY_NSError_$_MOError
+ __OBJC_$_CATEGORY_NSString_$_MOExtensions
+ __OBJC_$_CLASS_METHODS_MOContext
+ __OBJC_$_CLASS_METHODS_MOContextDimension
+ __OBJC_$_CLASS_METHODS_MOContextPredicate
+ __OBJC_$_CLASS_METHODS_MOContextPredicateBuilder
+ __OBJC_$_CLASS_METHODS_MOContextString
+ __OBJC_$_CLASS_METHODS_MODefaultsManager
+ __OBJC_$_CLASS_PROP_LIST_MOContextPredicate
+ __OBJC_$_INSTANCE_METHODS_MOConnection
+ __OBJC_$_INSTANCE_METHODS_MOConnectionManager
+ __OBJC_$_INSTANCE_METHODS_MOContextPredicate
+ __OBJC_$_INSTANCE_VARIABLES_MOConnection
+ __OBJC_$_INSTANCE_VARIABLES_MOConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_MOContextPredicate
+ __OBJC_$_PROP_LIST_MOConnection
+ __OBJC_$_PROP_LIST_MOConnectionManager
+ __OBJC_$_PROP_LIST_MOContextPredicate
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOConnectionManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MOConnectionManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MOContextPredicate
+ __OBJC_CLASS_PROTOCOLS_$_MOPersonalizedSensingServiceManager
+ __OBJC_CLASS_RO_$_MOConnection
+ __OBJC_CLASS_RO_$_MOConnectionManager
+ __OBJC_CLASS_RO_$_MOContextPredicate
+ __OBJC_CLASS_RO_$_MOContextPredicateBuilder
+ __OBJC_LABEL_PROTOCOL_$_MOConnectionManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_MOConnection
+ __OBJC_METACLASS_RO_$_MOConnectionManager
+ __OBJC_METACLASS_RO_$_MOContextPredicate
+ __OBJC_METACLASS_RO_$_MOContextPredicateBuilder
+ __OBJC_PROTOCOL_$_MOConnectionManagerDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ ___100-[MOPersonalizedSensingServiceManager fetchContextWithOptions:predicates:authorizedTypes:withReply:]_block_invoke
+ ___100-[MOPersonalizedSensingServiceManager fetchContextWithOptions:predicates:authorizedTypes:withReply:]_block_invoke.70
+ ___100-[MOPersonalizedSensingServiceManager fetchContextWithOptions:predicates:authorizedTypes:withReply:]_block_invoke.70.cold.1
+ ___100-[MOPersonalizedSensingServiceManager fetchContextWithOptions:predicates:authorizedTypes:withReply:]_block_invoke_2
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.29
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.cold.1
+ ___39-[MOConnection onConnectionInterrupted]_block_invoke.cold.2
+ ___41-[MOConnection callBlock:onInterruption:]_block_invoke
+ ___42+[MODefaultsManager momentsDaemonDefaults]_block_invoke
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke
+ ___43-[MOConnectionManager _getActiveConnection]_block_invoke.8
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.34
+ ___43-[MOConnectionManager getSyncProxyProvider]_block_invoke.cold.1
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.36
+ ___44-[MOConnectionManager getAsyncProxyProvider]_block_invoke.cold.1
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke
+ ___45-[MOConnectionManager _getSingleCallHandler:]_block_invoke_2
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke.20
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.21
+ ___53-[MOConnectionManager _callProxy:usingBlock:onError:]_block_invoke_2.cold.1
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke
+ ___53-[MOConnectionManager _postProxy:usingBlock:onError:]_block_invoke_2
+ ___61-[MOConnectionManager _callProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke
+ ___61-[MOConnectionManager _postProxyProvider:usingBlock:onError:]_block_invoke_2
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.27.cold.1
+ ___62-[MOConnectionManager withProxyProvider:proxyHandler:onError:]_block_invoke.cold.1
+ ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke.100
+ ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke.101
+ ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke_2
+ ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke_2.cold.1
+ ___71-[MOPersonalizedSensingServiceManager notifyContextFeedback:withReply:]_block_invoke.73
+ ___71-[MOPersonalizedSensingServiceManager notifyContextFeedback:withReply:]_block_invoke.73.cold.1
+ ___71-[MOPersonalizedSensingServiceManager notifyContextFeedback:withReply:]_block_invoke_2
+ ___85-[MOPersonalizedSensingServiceManager fetchPersonalizedContextWithOptions:withReply:]_block_invoke.65
+ ___85-[MOPersonalizedSensingServiceManager fetchPersonalizedContextWithOptions:withReply:]_block_invoke.65.cold.1
+ ___85-[MOPersonalizedSensingServiceManager fetchPersonalizedContextWithOptions:withReply:]_block_invoke_2
+ ___93-[MOPersonalizedSensingServiceManager requestDBAccessForPersonalizedSensingServiceWithReply:]_block_invoke.75
+ ___93-[MOPersonalizedSensingServiceManager requestDBAccessForPersonalizedSensingServiceWithReply:]_block_invoke.75.cold.1
+ ___93-[MOPersonalizedSensingServiceManager requestDBAccessForPersonalizedSensingServiceWithReply:]_block_invoke_2
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32bs_e17_v24?08?<B?>16ls32l8
+ ___block_descriptor_40_e8_32s_e24_16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e14_v16?0?<B?>8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v24?08?<B?>16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v24?08?<B?>16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e55_v24?0"<PersonalizedSensingServiceProtocol>"8?<B?>16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48w_e17_v16?0"NSError"8lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e8_v16?08ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e17_v16?0"NSError"8lw56l8s40l8s48l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e55_v24?0"<PersonalizedSensingServiceProtocol>"8?<B?>16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.83
+ ___block_literal_global.99
+ _momentsDaemonDefaults.onceToken
+ _momentsDaemonDefaults.shared
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_callProxy:usingBlock:onError:
+ _objc_msgSend$_callProxyProvider:usingBlock:onError:
+ _objc_msgSend$_getActiveConnection
+ _objc_msgSend$_getSingleCallHandler:
+ _objc_msgSend$_makeConnectionErrorWithReason:
+ _objc_msgSend$_postProxy:usingBlock:onError:
+ _objc_msgSend$_postProxyProvider:usingBlock:onError:
+ _objc_msgSend$altitude
+ _objc_msgSend$andPredicateWithSubpredicates:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$arguments
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$callAsyncProxyUsingBlock:onError:
+ _objc_msgSend$callBlock:onInterruption:
+ _objc_msgSend$callSyncProxyUsingBlock:onError:
+ _objc_msgSend$collection
+ _objc_msgSend$compoundPredicateType
+ _objc_msgSend$constantValue
+ _objc_msgSend$coordinate
+ _objc_msgSend$createAndPredicate:
+ _objc_msgSend$createPredicateWithLeftExpression:rightExpression:operation:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$delegate
+ _objc_msgSend$deserializeCLLocationObject:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$disassemblePredicate:
+ _objc_msgSend$distanceFromLocation:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$endDate
+ _objc_msgSend$expressionForConstantValue:
+ _objc_msgSend$expressionForKeyPath:
+ _objc_msgSend$expressionType
+ _objc_msgSend$extractFirstValueForKeyPath:fromPredicates:
+ _objc_msgSend$fetchContextWithOptions:predicates:authorizedTypes:withReply:
+ _objc_msgSend$fetchRequestPredicate
+ _objc_msgSend$filterCriteriaMap
+ _objc_msgSend$function
+ _objc_msgSend$getAsyncProxyProvider
+ _objc_msgSend$getConnectionName
+ _objc_msgSend$getSyncProxyProvider
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$horizontalAccuracy
+ _objc_msgSend$initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithName:usingDelegate:
+ _objc_msgSend$initWithPlace:city:location:
+ _objc_msgSend$initWithPredicate:filter:metadataTypes:
+ _objc_msgSend$initWithStartDate:endDate:timeReferenceString:
+ _objc_msgSend$inspectExpression:
+ _objc_msgSend$keyPath
+ _objc_msgSend$leftExpression
+ _objc_msgSend$length
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$location
+ _objc_msgSend$makeNewConnectionWithInterfaceFor:
+ _objc_msgSend$metadataTypes
+ _objc_msgSend$notPredicateWithSubpredicate:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$onConnectionInterrupted
+ _objc_msgSend$orPredicateWithSubpredicates:
+ _objc_msgSend$predicateOperatorFromType:
+ _objc_msgSend$predicateOperatorType
+ _objc_msgSend$predicateWithLeftExpression:rightExpression:modifier:type:options:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$rightExpression
+ _objc_msgSend$runBlockCompleted:
+ _objc_msgSend$runBlockStarted:withConnectionError:
+ _objc_msgSend$serializeCLLocationObject
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$startDate
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$stringForCompoundPredicateType:
+ _objc_msgSend$stringForOperatorType:
+ _objc_msgSend$subpredicates
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$userInfo
+ _objc_msgSend$variable
+ _objc_msgSend$verticalAccuracy
+ _objc_msgSend$withProxyProvider:proxyHandler:onError:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
- +[MOContext(CrossPlatform) fromBiome:]
- +[MOContextDimension(BiomePersonalizedSensing) fromBiome:]
- +[MOContextString(BiomePersonalizedSensing) fromBiome:]
- -[MOContextHistoryReader _enumeratePublishersForStream:usingBlock:]
- -[MOContextHistoryReader _enumeratePublishersForStream:usingBlock:].cold.1
- -[MOContextHistoryReader _getLatestFetchIdForClient:usingPublisher:]
- -[MOContextHistoryReader _isFetchDetail:matchingBundleId:orAlternateId:]
- -[MOPersonalizedSensingServiceManager connection]
- -[MOPersonalizedSensingServiceManager createConnection]
- -[MOPersonalizedSensingServiceManager setConnection:]
- GCC_except_table20
- _BiomeLibrary
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_IVAR_$_MOPersonalizedSensingServiceManager._connection
- __OBJC_$_CLASS_METHODS_MOContext(CrossPlatform)
- __OBJC_$_CLASS_METHODS_MOContextDimension(BiomePersonalizedSensing)
- __OBJC_$_CLASS_METHODS_MOContextString(BiomePersonalizedSensing)
- ___55-[MOPersonalizedSensingServiceManager createConnection]_block_invoke
- ___55-[MOPersonalizedSensingServiceManager createConnection]_block_invoke.41
- ___68-[MOContextHistoryReader _getLatestFetchIdForClient:usingPublisher:]_block_invoke
- ___68-[MOContextHistoryReader _getLatestFetchIdForClient:usingPublisher:]_block_invoke.29
- ___68-[MOContextHistoryReader _getLatestFetchIdForClient:usingPublisher:]_block_invoke_2
- ___68-[MOContextHistoryReader _getLatestFetchIdForClient:usingPublisher:]_block_invoke_2.cold.1
- ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke.90
- ___70-[MOPersonalizedSensingServiceManager refreshMomentsContextWithReply:]_block_invoke.cold.1
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke.32
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke.32.cold.1
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke.33
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke_2
- ___71-[MOContextHistoryReader loadPersonalizedContextWithOptions:withReply:]_block_invoke_3
- ___71-[MOPersonalizedSensingServiceManager notifyContextFeedback:withReply:]_block_invoke.64
- ___85-[MOPersonalizedSensingServiceManager fetchPersonalizedContextWithOptions:withReply:]_block_invoke.59
- ___85-[MOPersonalizedSensingServiceManager fetchPersonalizedContextWithOptions:withReply:]_block_invoke.60
- ___93-[MOPersonalizedSensingServiceManager requestDBAccessForPersonalizedSensingServiceWithReply:]_block_invoke.66
- ___block_descriptor_32_e23_v16?0"BPSCompletion"8l
- ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
- ___block_descriptor_40_e8_32r_e57_"NSMutableArray"24?0"NSMutableArray"8"BMStoreEvent"16lr32l8
- ___block_descriptor_48_e8_32r40r_e22_v16?0"BMStoreEvent"8lr32l8r40l8
- ___block_descriptor_48_e8_32s40r_e23_v16?0"BPSCompletion"8ls32l8r40l8
- ___block_descriptor_56_e8_32r40r48r_e24_v16?0"NSMutableArray"8lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e46_v24?0"BMDevice"8"BMBookmarkablePublisher"16ls32l8s40l8s48l8s56l8r64l8r72l8r80l8
- ___block_literal_global.43
- ___block_literal_global.52
- ___block_literal_global.63
- ___block_literal_global.75
- _objc_msgSend$MomentsContext
- _objc_msgSend$PersonalizedSensing
- _objc_msgSend$_enumeratePublishersForStream:usingBlock:
- _objc_msgSend$_getFrameworkClientIdentity
- _objc_msgSend$_getLatestFetchIdForClient:usingPublisher:
- _objc_msgSend$_isFetchDetail:matchingBundleId:orAlternateId:
- _objc_msgSend$addObject:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$alternateClientIdentifier
- _objc_msgSend$batchContextReplyStartIndex
- _objc_msgSend$clientBundleIdentifier
- _objc_msgSend$connection
- _objc_msgSend$contexts
- _objc_msgSend$createConnection
- _objc_msgSend$deviceIdentifier
- _objc_msgSend$dimensions
- _objc_msgSend$error
- _objc_msgSend$eventBody
- _objc_msgSend$fetchDetails
- _objc_msgSend$fetchId
- _objc_msgSend$filterWithIsIncluded:
- _objc_msgSend$fromBiome:
- _objc_msgSend$initWithTimeReferenceString:
- _objc_msgSend$isAfterDate:
- _objc_msgSend$model
- _objc_msgSend$personalizedContext
- _objc_msgSend$platform
- _objc_msgSend$publisherForDevice:withUseCase:options:
- _objc_msgSend$reduceWithInitial:nextPartialResult:
- _objc_msgSend$remoteDevicesWithError:
- _objc_msgSend$removeAllObjects
- _objc_msgSend$setConnection:
- _objc_msgSend$sinkWithCompletion:receiveInput:
CStrings:
+ ""
+ "!="
+ "#16@0:8"
+ "%@ (due '%@')"
+ "%@%@%@"
+ "%@*"
+ "%@: proxy error, %@, %@, retrying..."
+ "%@: proxy error, %@, %@."
+ "%@:%@"
+ "*"
+ "-[MOConnectionManager _getActiveConnection]"
+ "-[MOConnectionManager withProxyProvider:proxyHandler:onError:]"
+ "1"
+ "<"
+ "<="
+ "=="
+ ">"
+ ">="
+ "@\"<MOConnectionDelegate>\""
+ "@\"<MOConnectionManagerDelegate>\""
+ "@\"CLLocation\""
+ "@\"MOConnection\""
+ "@\"MOConnectionManager\""
+ "@\"NSData\""
+ "@\"NSDictionary\""
+ "@\"NSSet\""
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCConnection\"24@0:8@\"MOConnectionManager\"16"
+ "@16@?0@?<v@?@\"NSError\">8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@?16@?24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24Q32"
+ "@48@0:8Q16@24@32@40"
+ "@64@0:8Q16@24@32@40@48d56"
+ "@?16@0:8"
+ "@?24@0:8@?16"
+ "A"
+ "AND"
+ "Activating connection '%@'"
+ "ActivityMetaData activityType,%@"
+ "Aggregate Expression (Array of expressions)"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B32@0:8@16d24"
+ "B8@?0"
+ "BEGINSWITH"
+ "BETWEEN"
+ "CONTAINS"
+ "Called async proxy provider"
+ "Called sync proxy provider"
+ "Can't activate connection '%@': nil delegate"
+ "Compound Predicate Type: %@"
+ "Connection '%@' Invalidated"
+ "Constant Value: %@"
+ "Context biome stream persistency unavailable"
+ "ENDSWITH"
+ "Evaluated Object (self reference)"
+ "Function Arguments:"
+ "Function: %@"
+ "IN"
+ "Invalid '%@' connection .remoteObjectInterface (in %s:%d)"
+ "Key Path: %@"
+ "LIKE"
+ "Left Expression: %@"
+ "MOConnection"
+ "MOConnection managed interrupted, retrying..."
+ "MOConnectionManager"
+ "MOConnectionManagerDelegate"
+ "MOContextPredicate"
+ "MOContextPredicateBuilder"
+ "MOError"
+ "MOErrorDomain"
+ "NOT"
+ "NSObject"
+ "No arguments for function"
+ "OR"
+ "Operator Type: %@"
+ "PSServiceMgr,fetchContextWithOptions"
+ "PSServiceMgr,requestDBAccessForPersonalizedSensingServiceWithReply,XPCService  error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "Q24@0:8Q16"
+ "Right Expression: %@"
+ "Should use valid sync proxy block handler (in %s:%d)"
+ "T#,R"
+ "T@\"<MOConnectionDelegate>\",W,N,V_delegate"
+ "T@\"<MOConnectionManagerDelegate>\",W,N,V_delegate"
+ "T@\"CLLocation\",R,N,V_location"
+ "T@\"NSData\",&,V_fetchRequestPredicate"
+ "T@\"NSDate\",&,N,V_endDate"
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSDictionary\",&,V_filterCriteriaMap"
+ "T@\"NSSet\",&,V_metadataTypes"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,N,V_batchSize"
+ "TQ,R"
+ "UNKNOWN"
+ "Unknown expression type"
+ "Unknown predicate type: %@"
+ "Variable: %@"
+ "Vv16@0:8"
+ "[%s] The connection has been interrupted with %lu pending tasks"
+ "[%s] The connection has been interrupted with zero pending tasks"
+ "^{_NSZone=}16@0:8"
+ "_batchSize"
+ "_callProxy:usingBlock:onError:"
+ "_callProxyProvider:usingBlock:onError:"
+ "_connectionName"
+ "_delegate"
+ "_endDate"
+ "_fetchRequestPredicate"
+ "_filterCriteriaMap"
+ "_getActiveConnection"
+ "_getSingleCallHandler:"
+ "_interruptActive"
+ "_location"
+ "_makeConnectionErrorWithReason:"
+ "_metadataTypes"
+ "_mo_connection"
+ "_pendingRequestCounter"
+ "_pendingRequests"
+ "_postProxy:usingBlock:onError:"
+ "_postProxyProvider:usingBlock:onError:"
+ "_xpc_connection"
+ "altitude"
+ "andPredicateWithSubpredicates:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "arguments"
+ "arrayWithObjects:count:"
+ "autorelease"
+ "batchSize"
+ "callAsyncProxyUsingBlock:onError:"
+ "callBlock:onInterruption:"
+ "callSyncProxyUsingBlock:onError:"
+ "class"
+ "collection"
+ "compoundPredicateType"
+ "conformsToProtocol:"
+ "connectionManager"
+ "constantValue"
+ "contextLocation,(%f,%f),targetLocation,(%f,%f),distance,%f"
+ "contextPredicateForContextType:withMetadata:startDate:endDate:"
+ "contextPredicateForContextType:withMetadata:startDate:endDate:aroundLocation:withDistanceThreshold:"
+ "contextType"
+ "coordinate"
+ "createAndPredicate:"
+ "createNotPredicate:"
+ "createOrPredicate:"
+ "createPredicateForValue:inCollection:"
+ "createPredicateWithLeftExpression:rightExpression:operation:"
+ "criteriaMap"
+ "currentHandler"
+ "dateWithTimeIntervalSince1970:"
+ "debugDescription"
+ "delegate"
+ "deserializeCLLocationObject:"
+ "dictionaryWithDictionary:"
+ "disassemblePredicate:"
+ "distanceFromLocation"
+ "distanceFromLocation:"
+ "doubleValue"
+ "due '%@'"
+ "endDate"
+ "errorUsingError:withUnderyingError:"
+ "expressionForConstantValue:"
+ "expressionForKeyPath:"
+ "expressionType"
+ "extractFirstValueForKeyPath:fromPredicates:"
+ "fetch Context: invalid contextRetrieval: %u"
+ "fetchContextWithOptions:predicates:authorizedTypes:withReply:"
+ "fetchRequestPredicate"
+ "filterCriteriaMap"
+ "function"
+ "getAsyncProxyProvider"
+ "getConnectionName"
+ "getSyncProxyProvider"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "hash"
+ "horizontalAccuracy"
+ "initWithActivityType:"
+ "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:"
+ "initWithInt:"
+ "initWithName:usingDelegate:"
+ "initWithPlace:city:location:"
+ "initWithPredicate:filter:metadataTypes:"
+ "initWithStartDate:endDate:timeReferenceString:"
+ "inspectExpression:"
+ "interruptionBlock"
+ "isExtendedLogEnabled:forDetaultsManager:"
+ "isKindOfClass:"
+ "isProxy"
+ "isWithinDistanceFromLocation:maxDistance:"
+ "keyPath"
+ "latitude"
+ "leftExpression"
+ "length"
+ "localizedFailureReason"
+ "location"
+ "longitude"
+ "makeNewConnectionWithInterfaceFor:"
+ "maxDistance"
+ "metadataTypes"
+ "momentsDaemonDefaults"
+ "nil proxy"
+ "nil proxy @1"
+ "nil proxy @2"
+ "notPredicateWithSubpredicate:"
+ "numberWithUnsignedLongLong:"
+ "onConnectionInterrupted"
+ "orPredicateWithSubpredicates:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "place, %@, city, %@, location %{sensitive}@"
+ "postAsyncProxyUsingBlock:onError:"
+ "postSyncProxyUsingBlock:onError:"
+ "predicateOperatorFromType:"
+ "predicateOperatorType"
+ "predicateWithLeftExpression:rightExpression:modifier:type:options:"
+ "release"
+ "remote process execution was interrupted"
+ "remoteObjectInterface"
+ "requestBlock"
+ "requestPredicate"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "rightExpression"
+ "runBlockCompleted:"
+ "runBlockStarted:withConnectionError:"
+ "self"
+ "serializeCLLocationObject"
+ "setBatchSize:"
+ "setDelegate:"
+ "setEndDate:"
+ "setFetchRequestPredicate:"
+ "setFilterCriteriaMap:"
+ "setMetadataTypes:"
+ "setStartDate:"
+ "startDate"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "stringForCompoundPredicateType:"
+ "stringForOperatorType:"
+ "subpredicates"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "superclass"
+ "targetLocation"
+ "timeIntervalSince1970"
+ "userInfo"
+ "v16@?0@8"
+ "v16@?0@?<B@?>8"
+ "v24@?0@\"<PersonalizedSensingServiceProtocol>\"8@?<B@?>16"
+ "v24@?0@8@?<B@?>16"
+ "v32@0:8@?16@?24"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8@?16@?24@?32"
+ "v48@0:8@\"MOContextFetchOptions\"16@\"NSArray\"24@\"NSSet\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "variable"
+ "verticalAccuracy"
+ "withProxyProvider:proxyHandler:onError:"
+ "zone"
- "@\"NSMutableArray\"24@?0@\"NSMutableArray\"8@\"BMStoreEvent\"16"
- "@32@0:8@16@?24"
- "B16@?0@\"BMStoreEvent\"8"
- "B40@0:8@16@24@32"
- "BiomePersonalizedSensing"
- "Can't get MomentContext remote devices: %@"
- "Can't load biome sync context from %@: %@"
- "Can't load biome sync context: %@"
- "Connection to XPC service interrupted"
- "Connection to XPC service invalidated"
- "CrossPlatform"
- "Fetching context from shared stream"
- "Found sync device: %@, %@, %ld"
- "MomentsContext"
- "PSServiceMgr,primeService, generative models unavailable, do nothing"
- "PSServiceMgr,requestDBAccessForPersonalizedSensingService, generative models unavailable, do nothing"
- "PersonalizedSensing"
- "PersonalizedSensingServiceManager,fetchPersonalizedContextWithOptions,XPCService asynchronous error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
- "PersonalizedSensingServiceManager,requestDBAccessForPersonalizedSensingService,XPCService asynchronous error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
- "PlatformInfoOverrideIsSeedBuild"
- "PromptsReader"
- "Q32@0:8@16@24"
- "Skip split fetch batch fetchId=%u, index=%u"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "_connection"
- "_enumeratePublishersForStream:usingBlock:"
- "_getLatestFetchIdForClient:usingPublisher:"
- "_isFetchDetail:matchingBundleId:orAlternateId:"
- "addObject:"
- "addObjectsFromArray:"
- "alternateClientIdentifier"
- "batchContextReplyStartIndex"
- "clientBundleIdentifier"
- "connection"
- "contexts"
- "createConnection"
- "deviceIdentifier"
- "dimensions"
- "error"
- "eventBody"
- "fetchDetails"
- "fetchId"
- "filterWithIsIncluded:"
- "fromBiome:"
- "model"
- "personalizedContext"
- "place, %@, city, %@, visit time window %@"
- "platform"
- "publisherForDevice:withUseCase:options:"
- "reduceWithInitial:nextPartialResult:"
- "remoteDevicesWithError:"
- "removeAllObjects"
- "setConnection:"
- "sinkWithCompletion:receiveInput:"
- "v16@?0@\"BMStoreEvent\"8"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@\"NSMutableArray\"8"
- "v24@?0@\"BMDevice\"8@\"BMBookmarkablePublisher\"16"

```
