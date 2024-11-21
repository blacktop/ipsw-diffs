## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-11.2.19.0.0
-  __TEXT.__text: 0x41f6ec
-  __TEXT.__auth_stubs: 0x3c50
-  __TEXT.__objc_stubs: 0x129c0
-  __TEXT.__objc_methlist: 0xb38c
-  __TEXT.__cstring: 0x21aed
-  __TEXT.__objc_methname: 0x1b13a
+11.2.25.2.2
+  __TEXT.__text: 0x423ba0
+  __TEXT.__auth_stubs: 0x3c60
+  __TEXT.__objc_stubs: 0x12a80
+  __TEXT.__objc_methlist: 0xb3d4
+  __TEXT.__cstring: 0x21b1e
+  __TEXT.__objc_methname: 0x1b20e
   __TEXT.__const: 0x19d98
   __TEXT.__constg_swiftt: 0x21c0
   __TEXT.__swift5_typeref: 0x21d4

   __TEXT.__swift5_assocty: 0x3c0
   __TEXT.__swift5_proto: 0x37c
   __TEXT.__swift5_types: 0x234
-  __TEXT.__objc_classname: 0x4289
-  __TEXT.__objc_methtype: 0x79f1
+  __TEXT.__objc_classname: 0x428d
+  __TEXT.__objc_methtype: 0x7a44
   __TEXT.__swift5_capture: 0x175c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__oslogstring: 0x37e33
+  __TEXT.__oslogstring: 0x37e60
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__gcc_except_tab: 0xacc8
-  __TEXT.__dlopen_cstrs: 0x4b8
-  __TEXT.__unwind_info: 0x9ee0
-  __TEXT.__eh_frame: 0x7edc
-  __DATA_CONST.__auth_got: 0x1e38
+  __TEXT.__gcc_except_tab: 0xaaec
+  __TEXT.__dlopen_cstrs: 0x45e
+  __TEXT.__unwind_info: 0x9fb8
+  __TEXT.__eh_frame: 0x819c
+  __DATA_CONST.__auth_got: 0x1e40
   __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__auth_ptr: 0x7f0
-  __DATA_CONST.__const: 0x1d9e0
-  __DATA_CONST.__cfstring: 0x1b100
+  __DATA_CONST.__auth_ptr: 0x7d8
+  __DATA_CONST.__const: 0x1dcf8
+  __DATA_CONST.__cfstring: 0x1b0a0
   __DATA_CONST.__objc_classlist: 0x1630
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x518

   __DATA_CONST.__objc_arrayobj: 0x4c8
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x3ad30
-  __DATA.__objc_selrefs: 0x5d90
+  __DATA.__objc_const: 0x3ad60
+  __DATA.__objc_selrefs: 0x5dc0
   __DATA.__objc_ivar: 0x24f4
   __DATA.__objc_data: 0xff70
-  __DATA.__data: 0x6ce8
-  __DATA.__bss: 0x77e8
+  __DATA.__data: 0x6cd8
+  __DATA.__bss: 0x77d0
   __DATA.__common: 0xb6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12076
-  Symbols:   1916
-  CStrings:  15014
+  Functions: 12139
+  Symbols:   1917
+  CStrings:  15026
 
Symbols:
+ _BYSetupAssistantFinishedDarwinNotification
+ _BYSetupAssistantNeedsToRun
+ _objc_release_x13
+ _objc_release_x5
- _AMSSnapshotBagExpiredValueAccessedNotification
- _objc_release_x11
- _objc_release_x12
CStrings:
+ "\x01\x12\x12\x12"
+ "\x12\x11"
+ "\x14%\x17\x11\"\x11\x12"
+ "19:29:29"
+ "@\"AMSPromise\"16@?0@\"AMSSnapshotBag\"8"
+ "Adding pending push action type %ld"
+ "Consumer missing for action type %ld"
+ "Content restore attributing network to: %{public}@"
+ "DSPersonID"
+ "Error reading key %{public}@: %{public}@"
+ "Failed to prefetch bag snapshot: %{public}@"
+ "Failed to process push message: %{public}@"
+ "Nov 15 2024"
+ "PendingPushActionTypes"
+ "Prefetched bag snapshot"
+ "[%@] Failed to create event: %{public}@"
+ "[%@] Failed to determine if metrics should be collected: %{public}@"
+ "[%@] Metrics should not be collected"
+ "[%@] No user selection was made"
+ "[%@] Unable to install system app with no item ID mapping"
+ "_asyncLock"
+ "_asyncLock_completionHandlers"
+ "_asyncLock_snapshotBag"
+ "_pendingActionTypeCount"
+ "_systemAppMappingsForWatchUpToDate"
+ "_systemAppMappingsUpToDate"
+ "_systemApps"
+ "bagValueWithKey:valueType:valuePromise:"
+ "isManagedAccount"
+ "loadURLEventPromiseWithContext:"
+ "pushService:didReceiveMessage:completionHandler:"
+ "pushService:recoverFromDroppedMessagesOfActionType:completionHandler:"
+ "setShouldPendInSetupIfNotAllowed:"
+ "shouldCollectMetricsPromiseForContext:"
+ "shouldPendInSetupIfNotAllowed"
+ "v24@?0@\"AMSMetricsLoadURLEvent\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@?0@8B16@\"NSError\"20"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "v40@0:8@\"PushService\"16@\"PushMessage\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"PushService\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
- "\x02\x11\x13"
- "\x13%\x17\x11\"\x11\x12"
- "%lu message(s) pending but no consumer available for action type: %{public}@"
- "23:46:19"
- "A consumer was never registered for action type: %ld"
- "BYSetupAssistantFinishedDarwinNotification"
- "BYSetupAssistantNeedsToRun"
- "Cleaning up idle cached session: %{public}@ with identifier: %{public}@"
- "Flushing %lu message(s) for action type: %{public}@"
- "Nov  3 2024"
- "RecordMetrics"
- "T@\"NSDate\",R,N,VexpirationDate"
- "T@\"NSString\",R,C,N,Vprofile"
- "T@\"NSString\",R,C,N,VprofileVersion"
- "TB,R,N,GisExpired,Vexpired"
- "Timed out attempting to update subscription entitlements"
- "Timed out while waiting for snapshot bag to load"
- "[%{public}@] Timed out attempting to update subscription entitlements"
- "[Bag] Error creating snapshot of bag: %{public}@"
- "[Bag] Error reading key %{public}@: %{public}@"
- "[Bag] Invalidating snapshot bag"
- "_locked_snapshotBag"
- "_snapshotBagChangedObserver"
- "catalog start up"
- "creating app"
- "failingBagValueWithKey:valueType:error:"
- "pushService:didReceiveMessage:"
- "shouldCollectMetricsForContext:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
- "v32@0:8@\"PushService\"16@\"PushMessage\"24"

```
