## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService`

```diff

-1100.600.33.0.0
-  __TEXT.__text: 0x1ef30
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x16a4
+1128.100.2.0.0
+  __TEXT.__text: 0x1e2a8
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x168c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1dea
-  __TEXT.__oslogstring: 0x26bb
-  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__cstring: 0x1da8
+  __TEXT.__oslogstring: 0x264a
+  __TEXT.__gcc_except_tab: 0x180
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x32db
-  __TEXT.__objc_methtype: 0x567
-  __TEXT.__objc_stubs: 0x2340
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xf18
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__unwind_info: 0x788
+  __TEXT.__objc_classname: 0x19d
+  __TEXT.__objc_methname: 0x3271
+  __TEXT.__objc_methtype: 0x50b
+  __TEXT.__objc_stubs: 0x21a0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0xe88
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x728
-  __AUTH_CONST.__cfstring: 0x1f40
-  __AUTH_CONST.__objc_const: 0x2c90
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x260
-  __DATA.__bss: 0x2f1
+  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__cfstring: 0x1f60
+  __AUTH_CONST.__objc_const: 0x28e0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x13c
+  __DATA.__data: 0x200
+  __DATA.__bss: 0x301
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E4A67E7-B526-3849-8BEE-E019E70FD8C0
-  Functions: 827
-  Symbols:   2781
-  CStrings:  1551
+  UUID: 53504ECD-5BD1-3D19-B910-C1C48F777FA8
+  Functions: 815
+  Symbols:   2714
+  CStrings:  1543
 
Symbols:
+ +[APSLog offloader]
+ +[APSLog offloader].cold.1
+ -[APSConnection _onIvarQueue_subscribeToChannels:onTopic:]
+ -[APSConnection _resendPubSubSubscriptions]
+ -[APSConnection setSubscribedChannels:]
+ -[APSConnection subscribedChannels]
+ -[APSIdentityUtilities forcedProviderDefault]
+ -[APSMessage lock]
+ -[APSMessage setLock:]
+ GCC_except_table294
+ _APSForceAOPConnnection
+ _APSForceIdentityProvider
+ _APSHardwareSupportsAOP
+ _APSLastFullHandshakeTime
+ _APSPowerLog.cold.2
+ _OBJC_IVAR_$_APSConnection._subscribedChannels
+ _OBJC_IVAR_$_APSMessage._lock
+ ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.44
+ ___19+[APSLog offloader]_block_invoke
+ ___block_literal_global.154
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.169
+ ___block_literal_global.44
+ ___block_literal_global.87
+ __os_log_debug_impl
+ _objc_msgSend$_onIvarQueue_subscribeToChannels:onTopic:
+ _objc_msgSend$_resendPubSubSubscriptions
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allKeys
+ _objc_msgSend$channelTopic
+ _objc_msgSend$dictionary
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$setChannelTopic:
+ _objc_msgSend$setSubscribedChannels:
+ _objc_msgSend$subscribedChannels
+ _offloader.__log
+ _offloader.onceToken
- -[APSTaskClient .cxx_destruct]
- -[APSTaskClient _clearOutstandingTasks:]
- -[APSTaskClient _findDNSRequestForHostname:]
- -[APSTaskClient _timeoutOutstandingRequests]
- -[APSTaskClient dealloc]
- -[APSTaskClient initWithEnvironment:queue:]
- -[APSTaskClient resolveDNS:]
- GCC_except_table0
- GCC_except_table293
- OBJC_IVAR_$_APSTaskClient._clientQueue
- OBJC_IVAR_$_APSTaskClient._connection
- OBJC_IVAR_$_APSTaskClient._environment
- OBJC_IVAR_$_APSTaskClient._outstandingDNSRequests
- _NSCocoaErrorDomain
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_APSTaskClient
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_IVAR_$_APSMessage._ivarQueue
- _OBJC_METACLASS_$_APSTaskClient
- __OBJC_$_INSTANCE_METHODS_APSTaskClient
- __OBJC_$_INSTANCE_VARIABLES_APSTaskClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_APSTaskManagerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_APSTaskManagerInterface
- __OBJC_$_PROTOCOL_REFS_APSTaskManagerInterface
- __OBJC_CLASS_RO_$_APSTaskClient
- __OBJC_LABEL_PROTOCOL_$_APSTaskManagerInterface
- __OBJC_METACLASS_RO_$_APSTaskClient
- __OBJC_PROTOCOL_$_APSTaskManagerInterface
- __OBJC_PROTOCOL_REFERENCE_$_APSTaskManagerInterface
- ___108-[APSConnection _initWithEnvironmentName:namedDelegatePort:enablePushDuringSleep:personaUniqueString:queue:]_block_invoke.43
- ___27-[APSMessage objectForKey:]_block_invoke
- ___28-[APSTaskClient resolveDNS:]_block_invoke
- ___28-[APSTaskClient resolveDNS:]_block_invoke.56
- ___28-[APSTaskClient resolveDNS:]_block_invoke_2
- ___28-[APSTaskClient resolveDNS:]_block_invoke_2.cold.1
- ___28-[APSTaskClient resolveDNS:]_block_invoke_2.cold.2
- ___30-[APSMessage encodeWithCoder:]_block_invoke
- ___31-[APSMessage setObject:forKey:]_block_invoke
- ___35-[APSMessage instanceObjectForKey:]_block_invoke
- ___38-[APSMessage dictionaryRepresentation]_block_invoke
- ___39-[APSMessage setInstanceObject:forKey:]_block_invoke
- ___43-[APSTaskClient initWithEnvironment:queue:]_block_invoke
- ___43-[APSTaskClient initWithEnvironment:queue:]_block_invoke.46
- ___43-[APSTaskClient initWithEnvironment:queue:]_block_invoke.46.cold.1
- ___43-[APSTaskClient initWithEnvironment:queue:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32s_e49_v32?0"NSString"8"APSDNSResponse"16"NSError"24ls32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_literal_global.149
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.164
- ___block_literal_global.47
- _dispatch_assert_queue$V2
- _kAPSTaskClientServiceName
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$_clearOutstandingTasks:
- _objc_msgSend$_setQueue:
- _objc_msgSend$_timeoutOutstandingRequests
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$environment
- _objc_msgSend$hostname
- _objc_msgSend$indexOfObject:
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$invalidate
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$requestStartTime
- _objc_msgSend$resolveDNS:reply:
- _objc_msgSend$responseBlock
- _objc_msgSend$resume
- _objc_msgSend$setEnvironment:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$setRequestStartTime:
- _objc_msgSend$taskManager
- _objc_msgSend$timeIntervalSinceDate:
CStrings:
+ "%@ Removing in-memory subscription for failed channel"
+ "%@: Re-sending all pubsub subscriptions for correctness"
+ "APSForceAOP"
+ "APSForceIdentityProvider"
+ "APSLastFullHandshake"
+ "APSPowerLog: {event: %@}"
+ "T@\"NSMutableArray\",&,N,V_subscribedChannels"
+ "T@\"NSNumber\",R,N"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "_lock"
+ "_onIvarQueue_subscribeToChannels:onTopic:"
+ "_resendPubSubSubscriptions"
+ "_subscribedChannels"
+ "addObjectsFromArray:"
+ "allKeys"
+ "channelTopic"
+ "dictionary"
+ "forcedProviderDefault"
+ "lock"
+ "offload"
+ "offloader"
+ "removeObjectsInArray:"
+ "setChannelTopic:"
+ "setLock:"
+ "setSubscribedChannels:"
- "@\"NSXPCConnection\""
- "APSMessage-ivarQueue"
- "APSTaskClient"
- "APSTaskManagerInterface"
- "DNS Request timed out"
- "NSXPC error encountered while resolving DNS: %@"
- "Removing hostname %@ DNS request %@ from list of outstanding DNS requests"
- "Starting DNS resolution for hostname %@ timeout %f environment %@"
- "XPC connection is interrupted"
- "XPC connection is invalidated"
- "_clearOutstandingTasks:"
- "_clientQueue"
- "_findDNSRequestForHostname:"
- "_outstandingDNSRequests"
- "_setQueue:"
- "_timeoutOutstandingRequests"
- "com.apple.apsd.nsxpc"
- "dictionaryWithObjects:forKeys:count:"
- "indexOfObject:"
- "initWithDomain:code:userInfo:"
- "initWithEnvironment:queue:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "remoteObjectProxyWithErrorHandler:"
- "resolveDNS:"
- "resolveDNS:reply:"
- "resume"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "timeIntervalSinceDate:"
- "v16@?0@\"NSError\"8"
- "v32@0:8@\"APSDNSRequest\"16@?<v@?@\"NSString\"@\"APSDNSResponse\"@\"NSError\">24"
- "v32@?0@\"NSString\"8@\"APSDNSResponse\"16@\"NSError\"24"

```
