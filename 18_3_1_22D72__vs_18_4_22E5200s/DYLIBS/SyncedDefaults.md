## SyncedDefaults

> `/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults`

```diff

-2230.13.0.0.0
-  __TEXT.__text: 0xdd6c
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x8f0
-  __TEXT.__const: 0x1d6
-  __TEXT.__cstring: 0xd22
-  __TEXT.__oslogstring: 0x1b91
-  __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__swift5_typeref: 0x36
+2250.19.0.0.0
+  __TEXT.__text: 0xffdc
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_methlist: 0xb68
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0xe52
+  __TEXT.__oslogstring: 0x1ec1
+  __TEXT.__gcc_except_tab: 0x960
+  __TEXT.__swift5_typeref: 0x46
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x5e
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__unwind_info: 0x658
   __TEXT.__eh_frame: 0xd8
-  __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methname: 0x1b81
-  __TEXT.__objc_methtype: 0x6d5
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x560
+  __TEXT.__objc_classname: 0xfc
+  __TEXT.__objc_methname: 0x214b
+  __TEXT.__objc_methtype: 0x86d
+  __TEXT.__objc_stubs: 0x18e0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x9e0
-  __AUTH_CONST.__objc_const: 0xb60
+  __AUTH_CONST.__const: 0x528
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_const: 0xa98
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x238
-  __DATA.__bss: 0x2d0
-  __DATA.__common: 0x40
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x298
+  __DATA.__bss: 0x2e0
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 423
-  Symbols:   568
-  CStrings:  584
+  Functions: 499
+  Symbols:   659
+  CStrings:  679
 
Symbols:
+ _CKErrorUserInfoClasses
+ _OBJC_CLASS_$_CKContainerID
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_opt_respondsToSelector
+ _objc_retain_x4
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_arrayDestroy
- _swift_bridgeObjectRetain
- _swift_retain
CStrings:
+ "\x02\x12"
+ "\x03"
+ "\x11"
+ " containerID=%@"
+ " entitlementOverrides=%@"
+ "'"
+ "@\"<SYDClientToDaemonConnectionDelegate>\""
+ "@\"CKContainerID\""
+ "@\"NSDictionary\""
+ "B16@?0@\"NSError\"8"
+ "C20@0:8B16"
+ "Deleting data from disk for %@"
+ "Error obtaining %{public}@ remote object proxy: %@"
+ "Error obtaining synchronous remote object proxy to fetch if a UI framework is linked: %@"
+ "Error obtaining synchronous remote object proxy to fetch persona unique string: %@"
+ "Error obtaining synchronous remote object proxy to fetch value for containerID: %@"
+ "Failed to set fake CloudKit request error with error: %@"
+ "Finished deleting data from disk"
+ "Not syncing on first initialization because we're in the tests"
+ "Removed unit test sync managers"
+ "Removing unit test sync managers"
+ "Retrying XPC message on interruption"
+ "SYDTestDaemonProtocol"
+ "T@\"<SYDClientToDaemonConnectionDelegate>\",W,V_delegate"
+ "T@\"CKContainerID\",C,N"
+ "T@\"NSDictionary\",C,N,V_entitlementOverrides"
+ "T@\"SYDStoreConfiguration\",R,N,V_storeConfiguration"
+ "TB,N,V_useTestServer"
+ "Telling daemon to exit"
+ "Telling daemon to post fake account change notification"
+ "Telling daemon to post fake sync manager change notification"
+ "Telling daemon to set fake CloudKit request error"
+ "Using test server service name"
+ "_cachedObjectForKey:"
+ "_containerID"
+ "_daemonWithOptions:retries:errorHandler:daemonHandler:"
+ "_delegate"
+ "_entitlementOverrides"
+ "_synchronize:"
+ "_useTestServer"
+ "asynchronous"
+ "boolValue"
+ "com.apple.CloudKeyValuesTestingService"
+ "com.apple.KeyValueService"
+ "com.apple.KeyValueService.Encrypted"
+ "com.apple.KeyValueService.EndToEndEncrypted"
+ "com.apple.KeyValueService.EndToEndEncrypted.AllPlatforms"
+ "connection"
+ "connection:didRemoveObjectForKey:"
+ "connection:didSetObject:forKey:"
+ "connection:didSynchronize:error:"
+ "connection:willGetObjectForKey:"
+ "connection:willRemoveObjectForKey:"
+ "connection:willSetObject:forKey:"
+ "connectionStoreWillChange:"
+ "connectionUsingTestServer:"
+ "connectionWillGetDictionaryRepresentation:"
+ "connectionWillSynchronize:"
+ "container"
+ "containerID"
+ "containerIDFromDaemonWithError:"
+ "containerIDWithConfiguration:reply:"
+ "daemonWithOptions:errorHandler:daemonHandler:"
+ "decodeObjectOfClasses:forKey:"
+ "delegate"
+ "deleteDataFromDisk"
+ "deleteDataFromDiskForStoreWithConfiguration:reply:"
+ "e"
+ "entitlementOverrides"
+ "exit"
+ "exit:"
+ "initWithContainerIdentifier:environment:"
+ "initWithServiceName:options:"
+ "isUIFrameworkLinkedInDaemon"
+ "isUIFrameworkLinkedInDaemonWithReply:"
+ "kvs/exit"
+ "kvs/post-fake-account-change"
+ "kvs/post-fake-sync-manager-change"
+ "kvs/set-fake-cloudkit-error"
+ "personaUniqueStringWithReply:"
+ "postFakeAccountChangeNotificationWithCompletionHandler:"
+ "postFakeAccountChangeNotificationWithPreviousID:currentID:completionHandler:"
+ "postFakeSyncManagerChangeNotificationForStoreWithConfiguration:completionHandler:"
+ "postFakeSyncManagerChangeNotificationWithCompletionHandler:"
+ "removeUnitTestSyncManagers"
+ "removeUnitTestSyncManagersWithReply:"
+ "setContainerID:"
+ "setDelegate:"
+ "setEntitlementOverrides:"
+ "setFakeError:forNextCloudKitRequestOfClassName:inStoreWithConfiguration:"
+ "setUseTestServer:"
+ "setUseTestServerByDefault:"
+ "synchronous"
+ "useTestServer"
+ "useTestServerByDefault"
+ "v16@?0@\"<SYDDaemonProtocol>\"8"
+ "v16@?0@\"CKContainerID\"8"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"NSString\">16"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8@\"SYDStoreConfiguration\"16@?<v@?>24"
+ "v32@0:8@\"SYDStoreConfiguration\"16@?<v@?@\"CKContainerID\">24"
+ "v40@0:8@\"NSError\"16@\"NSString\"24@\"SYDStoreConfiguration\"32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8q16@?24@?32"
+ "v48@0:8q16Q24@?32@?40"
- "\x01\x12"
- "\x17"
- "@24@0:8@?16"
- "Error obtaining asynchronous remote object proxy: %@"
- "Error obtaining synchronous remote object proxy: %@"
- "Expected non-nil XPC connection"
- "Expected non-nil XPC connection queue"
- "T@\"SYDStoreConfiguration\",&,N,V_storeConfiguration"
- "asyncDaemonWithErrorHandler:"
- "machServiceName"
- "machServiceNameUsingTestServer:"
- "setStoreConfiguration:"
- "synchronousDaemonWithErrorHandler:"

```
