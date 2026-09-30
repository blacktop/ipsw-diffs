## CoreDuetContext

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x33f60
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x2dfc
+1892.17.0.2.0
+  __TEXT.__text: 0x34254
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x3408
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x24cc
-  __TEXT.__oslogstring: 0x3169
-  __TEXT.__gcc_except_tab: 0x1100
+  __TEXT.__cstring: 0x2507
+  __TEXT.__oslogstring: 0x3334
+  __TEXT.__gcc_except_tab: 0x1138
   __TEXT.__dlopen_cstrs: 0xbb
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__unwind_info: 0xec8
   __TEXT.__objc_classname: 0x59f
-  __TEXT.__objc_methname: 0x8a61
+  __TEXT.__objc_methname: 0x8b34
   __TEXT.__objc_methtype: 0x15a7
   __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0x348

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2020
+  __DATA_CONST.__objc_selrefs: 0x2138
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0xe20
-  __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_const: 0x4e98
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x4428
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x840
   __DATA.__bss: 0x441
   __DATA_DIRTY.__objc_data: 0x870

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1406
-  Symbols:   1736
-  CStrings:  2241
+  Functions: 1504
+  Symbols:   1840
+  CStrings:  2252
 
Symbols:
+ __CDProcessNameForXPCConnection
+ __cdcontextstore_signpost_deprecated_api
+ _cd_dispatch_async_xpc
+ _dispatch_block_create
CStrings:
+ "\x1d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1104"
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:156"
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:343"
+ "CoreDuet: ClientContext activateDevices:remoteUserContextProxySourceDeviceUUID:"
+ "CoreDuet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:"
+ "CoreDuet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext addObjects:toArrayAtKeyPath:"
+ "CoreDuet: ClientContext addObjects:toArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext deactivateDevices:remoteUserContextProxySourceDeviceUUID:"
+ "CoreDuet: ClientContext deregisterCallback:"
+ "CoreDuet: ClientContext evaluatePredicate:"
+ "CoreDuet: ClientContext handleContextualChange:info:handler:"
+ "CoreDuet: ClientContext handleRegistrationCompleted:handler:"
+ "CoreDuet: ClientContext lastModifiedDateForContextualKeyPath:"
+ "CoreDuet: ClientContext lastModifiedDateForContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext objectForContextualKeyPath:"
+ "CoreDuet: ClientContext objectForContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext re-register"
+ "CoreDuet: ClientContext registerCallback:"
+ "CoreDuet: ClientContext removeObjects:fromArrayAtKeyPath:"
+ "CoreDuet: ClientContext removeObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext setObject:forContextualKeyPath:"
+ "CoreDuet: ClientContext setObject:forContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext setObject:lastModifiedDate:forContextualKeyPath:"
+ "CoreDuet: ClientContext setupXPCConnection:"
+ "CoreDuet: ClientContext valuesForKeyPaths:"
+ "CoreDuet: ClientContext valuesForKeyPaths:inContextsMatchingPredicate:"
+ "CoreDuet: ClientContext valuesForKeyPaths:responseQueue:withCompletion:"
+ "CoreDuet: ContextStore Callback"
+ "CoreDuet: ContextStore Deregister"
+ "CoreDuet: ContextStore Region State Change"
+ "CoreDuet: ContextStore Register"
+ "CoreDuet: ContextStore com.apple.alarm handler"
+ "CoreDuet: ContextStore setObject:forContextualKeyPath:"
+ "Dispatching call to deprecated registration callback for %@, this may lead to priority problems. Switch to non-deprecated _CDContextualChangeRegistration APIs."
+ "Dispatching call to informative registration callback for %@"
+ "Fetching uncached value for %@"
+ "Sending fired registration %@ to %{public}@"
+ "Sending previously fired registration %@ to %{public}@"
+ "Sending registration completed for registration %@ to %{public}@"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_concurrentRegistrationCallbackQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialRegistrationCallbackQueue"
+ "_CDContextualChangeRegistration.callback"
+ "_concurrentRegistrationCallbackQueue"
+ "_serialRegistrationCallbackQueue"
+ "com.apple.CoreDuetContext.clientBlock"
+ "com.apple.CoreDuetContext.dispatchingCallback"
+ "com.apple.cdclientcontext.concurrentRegistrationCallbackQueue"
+ "com.apple.cdclientcontext.serialRegistrationCallbackQueue"
+ "com.apple.coreduet"
+ "concurrentRegistrationCallbackQueue"
+ "contextstored.client.activateMonitorQueue [%@]"
+ "contextstored.client.queue [%@]"
+ "serialRegistrationCallbackQueue"
+ "setConcurrentRegistrationCallbackQueue:"
+ "setSerialRegistrationCallbackQueue:"
- "\x1c"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDInMemoryContext.m:651"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1098"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:155"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:342"
- "Duet: ClientContext activateDevices:remoteUserContextProxySourceDeviceUUID:"
- "Duet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:"
- "Duet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext addObjects:toArrayAtKeyPath:"
- "Duet: ClientContext addObjects:toArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext deactivateDevices:remoteUserContextProxySourceDeviceUUID:"
- "Duet: ClientContext deregisterCallback:"
- "Duet: ClientContext evaluatePredicate:"
- "Duet: ClientContext handleContextualChange:info:handler:"
- "Duet: ClientContext handleRegistrationCompleted:handler:"
- "Duet: ClientContext lastModifiedDateForContextualKeyPath:"
- "Duet: ClientContext lastModifiedDateForContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext objectForContextualKeyPath:"
- "Duet: ClientContext objectForContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext re-register"
- "Duet: ClientContext registerCallback:"
- "Duet: ClientContext removeObjects:fromArrayAtKeyPath:"
- "Duet: ClientContext removeObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:"
- "Duet: ClientContext setObject:forContextualKeyPath:"
- "Duet: ClientContext setObject:forContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext setObject:lastModifiedDate:forContextualKeyPath:"
- "Duet: ClientContext setupXPCConnection:"
- "Duet: ClientContext valuesForKeyPaths:"
- "Duet: ClientContext valuesForKeyPaths:inContextsMatchingPredicate:"
- "Duet: ClientContext valuesForKeyPaths:responseQueue:withCompletion:"
- "Duet: ContextStore Callback"
- "Duet: ContextStore Deregister"
- "Duet: ContextStore Region State Change"
- "Duet: ContextStore Register"
- "Duet: ContextStore com.apple.alarm handler"
- "Duet: ContextStore setObject:forContextualKeyPath:"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_registrationCallbackQueue"
- "Uncached value for %@"
- "Unexpected NSCompoundPredicateType after already checking (%@)"
- "_registrationCallbackQueue"
- "client"
- "com.apple.cdclientcontext.registrationCallbackQueue"
- "com.apple.coreduet.context"
- "com.apple.coreduetd.contextserverclient.activateMonitorQueue"
- "com.apple.coreduetd.service.client.workQueue"
- "registrationCallbackQueue"
- "setRegistrationCallbackQueue:"

```
