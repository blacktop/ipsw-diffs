## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService`

```diff

-1138.600.21.0.0
-  __TEXT.__text: 0x21168
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x16a4
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1e02
+1157.100.1.0.0
+  __TEXT.__text: 0x1fb74
+  __TEXT.__objc_methlist: 0x172c
+  __TEXT.__const: 0xae
+  __TEXT.__cstring: 0x1edb
   __TEXT.__oslogstring: 0x268f
-  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__gcc_except_tab: 0x100
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x8c8
-  __TEXT.__objc_classname: 0x19d
-  __TEXT.__objc_methname: 0x3293
-  __TEXT.__objc_methtype: 0x50b
-  __TEXT.__objc_stubs: 0x2200
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeb0
+  __DATA_CONST.__objc_selrefs: 0xed0
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__const: 0x748
-  __AUTH_CONST.__cfstring: 0x1fc0
-  __AUTH_CONST.__objc_const: 0x28f0
-  __AUTH.__objc_data: 0x320
+  __DATA_CONST.__got: 0x238
+  __AUTH_CONST.__const: 0x7a8
+  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__objc_const: 0x2a70
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x390
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x13c
-  __DATA.__data: 0x200
-  __DATA.__bss: 0x309
+  __DATA.__data: 0x220
+  __DATA.__bss: 0x338
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
-  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 643036C0-22C4-354D-9339-7069E3EE5558
-  Functions: 825
-  Symbols:   2732
-  CStrings:  1554
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 8667E46A-E4EF-3F20-A066-F5934191E6F7
+  Functions: 853
+  Symbols:   2797
+  CStrings:  831
 
Symbols:
+ +[APSConnection lastReceivedSecureTimestamp]
+ +[APSConnection lastReceivedSecureTimestamp].cold.1
+ -[APSIdentityUtilities deviceIdentitySupported].cold.1
+ GCC_except_table214
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table299
+ _OBJC_CLASS_$_APSSecureTimestamp
+ _OBJC_METACLASS_$_APSSecureTimestamp
+ __CLASS_METHODS_APSSecureTimestamp
+ __CLASS_PROPERTIES_APSSecureTimestamp
+ __DATA_APSSecureTimestamp
+ __IVARS_APSSecureTimestamp
+ __METACLASS_DATA_APSSecureTimestamp
+ __OBJC_$_INSTANCE_METHODS_APSSecureTimestamp(Private)
+ __PROPERTIES_APSSecureTimestamp
+ __PROTOCOLS_APSSecureTimestamp
+ __PROTOCOLS_APSSecureTimestamp.2
+ ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.44
+ ___29+[APSConnection copyIdentity]_block_invoke.128
+ ___31+[APSConnection _setTokenState]_block_invoke.227
+ ___33-[APSConnection _deliverMessage:]_block_invoke.152
+ ___39-[APSConnection _deliverToken:forInfo:]_block_invoke.167
+ ___40-[APSConnection rollTokensAndReconnect:]_block_invoke.142
+ ___42-[APSConnection _deliverURLToken:forInfo:]_block_invoke.170
+ ___43-[APSConnection _sendOutgoingMessage:fake:]_block_invoke.246
+ ___44+[APSConnection lastReceivedSecureTimestamp]_block_invoke
+ ___44+[APSConnection lastReceivedSecureTimestamp]_block_invoke_2
+ ___44+[APSConnection lastReceivedSecureTimestamp]_block_invoke_3
+ ___44+[APSConnection lastReceivedSecureTimestamp]_block_invoke_4
+ ___44-[APSConnection rollBAACertsWithCompletion:]_block_invoke.141
+ ___47-[APSConnection _deliverURLTokenError:forInfo:]_block_invoke.173
+ ___47-[APSIdentityUtilities deviceIdentitySupported]_block_invoke
+ ___50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.290
+ ___50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.291
+ ___51-[APSConnection _deliverToken:forTopic:identifier:]_block_invoke.164
+ ___51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.262
+ ___51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.262.cold.1
+ ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.269
+ ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.269.cold.1
+ ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.273
+ ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.273.cold.1
+ ___59-[APSConnection signDataWithDeviceIdentity:withCompletion:]_block_invoke.136
+ ___60-[APSConnection _deliverFailedChannelSubscriptions:onTopic:]_block_invoke.298
+ ___62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.289
+ ___63-[APSConnection forceClientIdentityProviderSwapWithCompletion:]_block_invoke.133
+ ___65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.179
+ ___65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.182
+ ___65-[APSConnection _asyncOnDelegateQueueWithBlock:requiresDelegate:]_block_invoke.58
+ ___80-[APSConnection _deliverOutgoingMessageResultWithID:error:sendRTT:ackTimestamp:]_block_invoke.159
+ ___APSConnectionInterruptedHandlerBlock_block_invoke.60
+ ___APSConnectionInvalidationHandlerBlock_block_invoke.63
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.14
+ ___block_literal_global.178
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.189
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.199
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.216
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.62
+ ___block_literal_global.90
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_ApplePushService
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_ApplePushService
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_ApplePushService
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_ApplePushService
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_ApplePushService
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_ApplePushService
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_ApplePushService
+ __swift_stdlib_reportUnimplementedInitializer
+ _deviceIdentitySupported._DeviceIdentityIsSupported
+ _deviceIdentitySupported._pred_DeviceIdentityIsSupportedDeviceIdentity
+ _lastReceivedSecureTimestamp.onceToken
+ _lastReceivedSecureTimestamp.sQueue
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$init
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithTimestamp:
+ _objc_msgSend$initWith_timestamp:
+ _objc_msgSend$timestampData
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _swift_bridgeObjectRelease
+ _swift_deallocPartialClassInstance
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_release
+ _swift_retain
- GCC_except_table222
- GCC_except_table225
- GCC_except_table294
- _DeviceIdentityIsSupported
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.45
- ___29+[APSConnection copyIdentity]_block_invoke.129
- ___31+[APSConnection _setTokenState]_block_invoke.220
- ___33-[APSConnection _deliverMessage:]_block_invoke.153
- ___39-[APSConnection _deliverToken:forInfo:]_block_invoke.168
- ___40-[APSConnection rollTokensAndReconnect:]_block_invoke.143
- ___42-[APSConnection _deliverURLToken:forInfo:]_block_invoke.171
- ___43-[APSConnection _sendOutgoingMessage:fake:]_block_invoke.239
- ___44-[APSConnection rollBAACertsWithCompletion:]_block_invoke.142
- ___47-[APSConnection _deliverURLTokenError:forInfo:]_block_invoke.174
- ___50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.283
- ___50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.284
- ___51-[APSConnection _deliverToken:forTopic:identifier:]_block_invoke.165
- ___51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.255
- ___51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.255.cold.1
- ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.262
- ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.262.cold.1
- ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.266
- ___54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.266.cold.1
- ___59-[APSConnection signDataWithDeviceIdentity:withCompletion:]_block_invoke.137
- ___60-[APSConnection _deliverFailedChannelSubscriptions:onTopic:]_block_invoke.291
- ___62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.275
- ___63-[APSConnection forceClientIdentityProviderSwapWithCompletion:]_block_invoke.134
- ___65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.180
- ___65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.183
- ___65-[APSConnection _asyncOnDelegateQueueWithBlock:requiresDelegate:]_block_invoke.59
- ___80-[APSConnection _deliverOutgoingMessageResultWithID:error:sendRTT:ackTimestamp:]_block_invoke.160
- ___APSConnectionInterruptedHandlerBlock_block_invoke.61
- ___APSConnectionInvalidationHandlerBlock_block_invoke.65
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.185
- ___block_literal_global.190
- ___block_literal_global.194
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.91
- _objc_retain_x26
CStrings:
+ " timestampData: "
+ "<APSSecureTimestamp: "
+ "ApplePushService.APSSecureTimestamp"
+ "DeviceIdentity"
+ "DeviceIdentityIsSupported"
+ "init()"
+ "requestSecureTimestamp"
+ "secureTimestampData"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"CUTWeakReference\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8r*16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16d24q32@?40"
- "@52@0:8@16@24B32@36@44"
- "@?"
- "@?16@0:8"
- "APSAdditions"
- "APSAppTokenInfo"
- "APSChannelSubscriptionFailure"
- "APSConnection"
- "APSDNSRequest"
- "APSDNSResponse"
- "APSIdentityUtilities"
- "APSIncomingMessage"
- "APSLog"
- "APSMessage"
- "APSMultiUserFS"
- "APSMultiUserMode"
- "APSOutgoingMessage"
- "APSPair"
- "APSSignDataWithIdentityRequest"
- "APSSignDataWithIdentityResponse"
- "APSTokenInfo"
- "APSURLToken"
- "APSURLTokenInfo"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HomeKit"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<APSConnectionDelegate>\",N"
- "T@\"NSArray\",&,N,S_setEnabledTopics:,V_enabledTopics"
- "T@\"NSArray\",&,N,S_setIgnoredTopics:,V_ignoredTopics"
- "T@\"NSArray\",&,N,S_setNonWakingTopics:,V_nonWakingTopics"
- "T@\"NSArray\",&,N,S_setOpportunisticTopics:,V_opportunisticTopics"
- "T@\"NSArray\",&,N,V_certificates"
- "T@\"NSArray\",R,N,V_ipv4Address"
- "T@\"NSArray\",R,N,V_ipv6Address"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_baseToken"
- "T@\"NSData\",&,N,V_data"
- "T@\"NSData\",&,N,V_nonce"
- "T@\"NSData\",&,N,V_signature"
- "T@\"NSData\",&,N,V_token"
- "T@\"NSData\",&,N,V_vapidPublicKey"
- "T@\"NSData\",C,N"
- "T@\"NSData\",R,&,N"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",&,N,V_expirationDate"
- "T@\"NSDate\",&,N,V_requestStartTime"
- "T@\"NSDate\",C,N"
- "T@\"NSDate\",R,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSMutableArray\",&,N,V_accumulatedTopicMoves"
- "T@\"NSMutableArray\",&,N,V_subscribedChannels"
- "T@\"NSNumber\",&,N,V_time"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_delegateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_ivarQueue"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_channelID"
- "T@\"NSString\",&,N,V_environment"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_pushTopic"
- "T@\"NSString\",&,N,V_tokenURL"
- "T@\"NSString\",&,N,V_topic"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_hostname"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_hostname"
- "T@,&,N,V_first"
- "T@,&,N,V_second"
- "T@?,R,C,V_responseBlock"
- "TB,N"
- "TB,N,GisCritical"
- "TB,N,GisTracingEnabled"
- "TB,N,GwasFromStorage"
- "TB,N,GwasLastMessageFromStorage"
- "TB,N,V_ackReceived"
- "TB,N,V_isUnextended"
- "TB,N,V_usesAppLaunchStats"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isLoggedInUser"
- "TB,R,N,V_isMultiUser"
- "TB,R,N,V_isShutdown"
- "TB,R,V_isMultiUser"
- "TI,N"
- "TQ,N"
- "TQ,N,V_fromListID"
- "TQ,N,V_toListID"
- "TQ,R"
- "Td,R,N,V_timeout"
- "Ti,N,V_failureReason"
- "Tq,N"
- "Tq,R,N"
- "T{os_unfair_lock_s=I},N,V_lock"
- "T{os_unfair_lock_s=I},N,V_topicMoveLock"
- "UTF8String"
- "Vv16@0:8"
- "^v"
- "^{_NSZone=}16@0:8"
- "^{__SecIdentity=}16@0:8"
- "_APSTopicMove"
- "_accumulatedTopicMoves"
- "_ackReceived"
- "_addEnableCriticalReliabilityToXPCMessage:"
- "_addEnableStatusNotificationsToXPCMessage:"
- "_addPushWakeTopicsToXPCMessage:"
- "_addTrackActivityPresenceToXPCMessage:"
- "_addUltraConstrainedTopicsToXPCMessage:"
- "_asyncOnDelegateQueueWithBlock:"
- "_asyncOnDelegateQueueWithBlock:requiresDelegate:"
- "_baseToken"
- "_blockingXPCCallWithArgumentBlock:resultHandler:"
- "_cancelConnection"
- "_cancelConnectionOnIvarQueue"
- "_certificates"
- "_channelID"
- "_connectIfNecessary"
- "_connectIfNecessaryOnIvarQueue"
- "_connection"
- "_connectionPort"
- "_connectionPortName"
- "_createXPCConnectionWithQueueName:"
- "_data"
- "_delegateQueue"
- "_delegateReference"
- "_deliverConnectionStatusChange:"
- "_deliverConnectionStatusFromDealloc:"
- "_deliverDidReconnectOnIvarQueue"
- "_deliverFailedChannelSubscriptions:onTopic:"
- "_deliverMessage:"
- "_deliverOutgoingMessageResultWithID:error:sendRTT:"
- "_deliverOutgoingMessageResultWithID:error:sendRTT:ackTimestamp:"
- "_deliverPublicToken:withCompletionBlock:"
- "_deliverPublicTokenOnIvarQueue:withCompletionBlock:"
- "_deliverToken:forInfo:"
- "_deliverToken:forTopic:identifier:"
- "_deliverURLToken:forInfo:"
- "_deliverURLTokenError:forInfo:"
- "_disconnect"
- "_disconnectFromDealloc"
- "_disconnectOnIvarQueue"
- "_dispatch_async_to_ivarQueue:"
- "_dispatch_async_to_ivarQueue:shutdownBlock:"
- "_dispatch_sync_to_ivarQueue:shutdownBlock:"
- "_effectiveSendTimeout"
- "_enableCriticalReliability"
- "_enableStatusNotifications"
- "_enabledTopics"
- "_environment"
- "_environmentName"
- "_everHadDelegate"
- "_expirationDate"
- "_failureReason"
- "_first"
- "_flags"
- "_flushIdentityCache"
- "_fromListID"
- "_getIsCurrentlyLoggedIn"
- "_getMultiUserMode"
- "_handleEvent:withHandler:"
- "_handleEvent:withHandler:errorHandler:"
- "_hostname"
- "_identifier"
- "_idsToOutgoingMessages"
- "_ignoredTopics"
- "_initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:"
- "_insertURLTokenBlock:forInfo:"
- "_ipv4Address"
- "_ipv6Address"
- "_isConnected"
- "_isDeallocing"
- "_isDisconnected"
- "_isLoggedInUser"
- "_isMultiUser"
- "_isReconnectScheduled"
- "_isShutdown"
- "_isUnextended"
- "_ivarQueue"
- "_largeMessageSize"
- "_lock"
- "_machQueue"
- "_mach_source"
- "_messageSize"
- "_nextOutgoingMessageID"
- "_nonWakingTopics"
- "_nonce"
- "_noteDisconnectedFromDaemonOnIvarQueue"
- "_onIvarQueue_setEnabledTopics:ignoredTopics:opportunisticTopics:nonWakingTopics:sendToDaemon:completion:"
- "_onIvarQueue_setPushWakeTopics:"
- "_onIvarQueue_setUltraConstrainedTopics:"
- "_onIvarQueue_subscribeToChannels:onTopic:"
- "_opportunisticTopics"
- "_pendingURLTokenBlocks"
- "_plist"
- "_processName"
- "_processQueuedTopicMovesOnIvarQueue"
- "_properties"
- "_publicToken"
- "_pushTopic"
- "_pushWakeTopics"
- "_queuedDelegateBlocks"
- "_reconnectDelay"
- "_reconnectIfNecessaryOnIvarQueueAfterDelay"
- "_removeURLTokenBlocksForInfo:"
- "_requestStartTime"
- "_resendPubSubSubscriptions"
- "_responseBlock"
- "_safelyCancelAndReleaseConnection:"
- "_second"
- "_sendOutgoingMessage:fake:"
- "_setEnableCriticalReliability:sendToDaemon:"
- "_setEnableStatusNotifications:sendToDaemon:"
- "_setEnabledTopics:"
- "_setEnabledTopics:ignoredTopics:opportunisticTopics:nonWakingTopics:sendToDaemon:completion:"
- "_setIgnoredTopics:"
- "_setNonWakingTopics:"
- "_setOpportunisticTopics:"
- "_setTokenState"
- "_setTrackActivityPresence:sendToDaemon:"
- "_shutdownFromDealloc"
- "_shutdownOnIvarQueue"
- "_signature"
- "_subscribedChannels"
- "_systemPathCache"
- "_time"
- "_timeout"
- "_toListID"
- "_token"
- "_tokenURL"
- "_topic"
- "_topicListNameForLogging:"
- "_topicMoveLock"
- "_trackActivityPresence"
- "_ultraConstrainedTopics"
- "_usesAppLaunchStats"
- "_vapidPublicKey"
- "_xpcMessage"
- "accumulatedTopicMoves"
- "ackReceived"
- "addObject:"
- "addObjectsFromArray:"
- "albertIdentitySupported"
- "allKeys"
- "allObjects"
- "allValues"
- "allowMultipleTokens"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "apsStringGUID"
- "aps_prettyDescription"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "baaPushIdentityEnabled"
- "base64EncodedStringWithOptions:"
- "baseToken"
- "boolValue"
- "bytes"
- "calloutToDelegatesForURLTokenError:forInfo:completion:"
- "calloutToInvalidateCompletion:withSuccess:error:"
- "cancelOutgoingMessage:"
- "certificates"
- "channelTopic"
- "characterAtIndex:"
- "class"
- "code"
- "compare:"
- "componentsSeparatedByString:"
- "confirmReceiptForMessage:"
- "conformsToProtocol:"
- "connection:channelSubscriptionsFailedWithFailures:"
- "connection:didChangeConnectedStatus:"
- "connection:didFailToSendOutgoingMessage:error:"
- "connection:didReceiveIncomingMessage:"
- "connection:didReceiveMessageForTopic:userInfo:"
- "connection:didReceivePublicToken:"
- "connection:didReceiveToken:forInfo:"
- "connection:didReceiveToken:forTopic:identifier:"
- "connection:didReceiveURLToken:forInfo:"
- "connection:didReceiveURLTokenError:forInfo:"
- "connection:didSendOutgoingMessage:"
- "connectionDidReconnect:"
- "connectionsDebuggingStateOfStyle:"
- "containsObject:"
- "containsValueForKey:"
- "copy"
- "copyIdentity"
- "copyWithZone:"
- "correlationIdentifier"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "courierOversized"
- "critical"
- "currentHandler"
- "currentTokenForInfo:"
- "currentURLTokenForInfo:"
- "currentUser"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "delegateQueue"
- "description"
- "deviceIdentitySupported"
- "dictionary"
- "dictionaryRepresentation"
- "doubleValue"
- "eagernessTimeoutTime"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "environment"
- "errorWithDomain:code:userInfo:"
- "expirationDate"
- "failureReason"
- "first"
- "forceClientIdentityProviderSwapWithCompletion:"
- "forcedProviderDefault"
- "fromListID"
- "fromStorage"
- "getCFRunLoop"
- "getCString:maxLength:encoding:"
- "getRegisteredChannelsForTopic:completion:"
- "getRegisteredChannelsForTopic:withCompletion:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasTimedOut"
- "hash"
- "hostname"
- "i"
- "i16@0:8"
- "incomingInterface"
- "init"
- "initResponseForHostname:ipv4Address:ipv6Address:"
- "initUnextendedAppTokenWithTopic:identifier:"
- "initWithArray:"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:"
- "initWithCString:encoding:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithDictionary:xpcMessage:"
- "initWithEnvironmentName:"
- "initWithEnvironmentName:namedDelegatePort:"
- "initWithEnvironmentName:namedDelegatePort:personaUniqueString:queue:"
- "initWithEnvironmentName:namedDelegatePort:queue:"
- "initWithEnvironmentName:queue:"
- "initWithFirst:second:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithHostname:timeoutInSeconds:requestFlags:responseBlock:"
- "initWithInt:"
- "initWithIsMultiUserMode:"
- "initWithIsMultiUserMode:loggedInUser:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithTokenURL:token:"
- "initWithTopic:"
- "initWithTopic:identifier:"
- "initWithTopic:userInfo:"
- "initWithTopic:vapidPublicKey:"
- "initWithTopic:vapidPublicKey:expirationDate:"
- "instanceObjectForKey:"
- "intValue"
- "integerValue"
- "invalidateTokenForInfo:"
- "invalidateTokenForTopic:identifier:"
- "invalidateURLTokenForInfo:"
- "invalidateURLTokenForInfo:completion:"
- "ipv4Address"
- "ipv6Address"
- "isCritical"
- "isEager"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToData:"
- "isEqualToDate:"
- "isEqualToDictionary:"
- "isEqualToSet:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLoggedInUser"
- "isLoginUser"
- "isMainThread"
- "isMemberOfClass:"
- "isMultiAndLoggedIn"
- "isMultiUser"
- "isProxy"
- "isShutdown"
- "isTracingEnabled"
- "isUnextended"
- "isValidEnvironment:"
- "ivarQueue"
- "keepAliveIntervalForEnvironmentName:"
- "lastMessageFromStorage"
- "length"
- "lock"
- "mainRunLoop"
- "minusSet:"
- "moveTopic:fromList:toList:"
- "moveTopics:fromList:toList:"
- "mutableCopy"
- "notifySafeToSendFilter"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedShort:"
- "object"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offloader"
- "originator"
- "pairWithFirst:second:"
- "payloadFormat"
- "payloadLength"
- "perAppToken"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "priority"
- "processInfo"
- "propertyListWithData:options:format:error:"
- "protocolParserDetailed"
- "pushFlags"
- "pushType"
- "q"
- "q16@0:8"
- "raise:format:"
- "rawTimeoutTime"
- "reduceLogging"
- "registeredChannelsForTopic:error:"
- "release"
- "removeFromRunLoop"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "requestKeepAlive"
- "requestStartTime"
- "requestTokenForInfo:"
- "requestTokenForTopic:identifier:"
- "requestURLTokenForInfo:"
- "requestURLTokenForInfo:completion:"
- "respondsToSelector:"
- "responseBlock"
- "retain"
- "retainCount"
- "rollBAACertsWithCompletion:"
- "rollTokensAndReconnect:"
- "scheduleInRunLoop:"
- "second"
- "self"
- "sendFakeMessage:"
- "sendInterfaceIdentifier"
- "sendOutgoingMessage:"
- "sendRetried"
- "sendTimeoutTime"
- "sentTimestamp"
- "serverTimeInNanoSeconds"
- "setAccumulatedTopicMoves:"
- "setAckReceived:"
- "setAckTimestamp:"
- "setBaseToken:"
- "setCancelled:"
- "setCertificates:"
- "setChannelID:"
- "setChannelTopic:"
- "setCorrelationIdentifier:"
- "setCritical:"
- "setData:"
- "setDelegate:"
- "setEnableCriticalReliability:"
- "setEnableStatusNotifications:"
- "setEnabledTopics:"
- "setEnabledTopics:ignoredTopics:"
- "setEnabledTopics:ignoredTopics:opportunisticTopics:"
- "setEnabledTopics:ignoredTopics:opportunisticTopics:nonWakingTopics:"
- "setEnabledTopics:ignoredTopics:opportunisticTopics:nonWakingTopics:completion:"
- "setEnvironment:"
- "setExpirationDate:"
- "setFailureReason:"
- "setFirst:"
- "setFromListID:"
- "setFromStorage:"
- "setGuid:"
- "setIdentifier:"
- "setIgnoredTopics:"
- "setIncomingInterface:"
- "setInstanceObject:forKey:"
- "setIsUnextended:"
- "setLargeMessageSize:"
- "setLastMessageFromStorage:"
- "setLock:"
- "setMessageID:"
- "setMessageSize:"
- "setNonWakingTopics:"
- "setNonce:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOpportunisticTopics:"
- "setOriginator:"
- "setPayloadFormat:"
- "setPayloadLength:"
- "setPerAppToken:"
- "setPriority:"
- "setPushFlags:"
- "setPushTopic:"
- "setPushType:"
- "setPushWakeTopics:"
- "setRequestStartTime:"
- "setSecond:"
- "setSendInterfaceIdentifier:"
- "setSendRTT:"
- "setSendRetried:"
- "setSent:"
- "setSentTimestamp:"
- "setSignature:"
- "setSubscribedChannels:"
- "setTime:"
- "setTimedOut:"
- "setTimeout:"
- "setTimestamp:"
- "setToListID:"
- "setToken:"
- "setTokenURL:"
- "setTopic:"
- "setTopicMoveLock:"
- "setTracingEnabled:"
- "setTracingUUID:"
- "setTrackActivityPresence:"
- "setUltraConstrainedTopics:"
- "setUserInfo:"
- "setUsesAppLaunchStats:"
- "setVapidPublicKey:"
- "setWithCapacity:"
- "setWithObjects:"
- "sharedInstance"
- "sharedManager"
- "shouldPowerLogEvent:"
- "shouldReduceLogging"
- "shutdown"
- "signDataWithDeviceIdentity:withCompletion:"
- "signature"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subscribeToChannel:forTopic:"
- "subscribeToChannels:forTopic:"
- "superclass"
- "supportsSecureCoding"
- "systemPath"
- "time"
- "timeIntervalSince1970"
- "timeIntervalSinceReferenceDate"
- "timeout"
- "timestamp"
- "toListID"
- "tokenURL"
- "topicManagerOversized"
- "topicMoveLock"
- "tracingEnabled"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedShortValue"
- "unsubscribeFromChannel:forTopic:"
- "unsubscribeFromChannels:forTopic:"
- "useMultiIdentityProvider"
- "userInfo"
- "usesAppLaunchStats"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8@?16B24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@24"
- "v32@0:8@?16@?24"
- "v36@0:8@?16B24@28"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16Q24Q32"
- "v40@0:8Q16@24Q32"
- "v48@0:8@16@24@32@40"
- "v48@0:8Q16@24Q32Q40"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@16@24@32@40B48@?52"
- "vapidPublicKey"
- "wasCancelled"
- "wasFromStorage"
- "wasLastMessageFromStorage"
- "wasSent"
- "weakRefWithObject:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
