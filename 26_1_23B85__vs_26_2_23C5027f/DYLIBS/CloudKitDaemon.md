## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2320.14.0.0.0
-  __TEXT.__text: 0x39e9c0
-  __TEXT.__auth_stubs: 0x4030
+2330.13.0.0.0
+  __TEXT.__text: 0x39ef0c
+  __TEXT.__auth_stubs: 0x4010
   __TEXT.__objc_methlist: 0x2f734
   __TEXT.__const: 0x4608
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x1d68
-  __TEXT.__oslogstring: 0x2ec56
+  __TEXT.__oslogstring: 0x2ee09
   __TEXT.__swift5_capture: 0x6a0
-  __TEXT.__cstring: 0x287d1
+  __TEXT.__cstring: 0x2880a
   __TEXT.__constg_swiftt: 0x19b8
   __TEXT.__swift5_reflstr: 0x1059
   __TEXT.__swift5_fieldmd: 0x11e0

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xd960
+  __TEXT.__gcc_except_tab: 0xd95c
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xc0a0
+  __TEXT.__unwind_info: 0xc0b0
   __TEXT.__eh_frame: 0x30e0
   __TEXT.__objc_classname: 0x5589
-  __TEXT.__objc_methname: 0x5af36
-  __TEXT.__objc_methtype: 0x8bdd
-  __TEXT.__objc_stubs: 0x38880
+  __TEXT.__objc_methname: 0x5b006
+  __TEXT.__objc_methtype: 0x8be0
+  __TEXT.__objc_stubs: 0x388a0
   __DATA_CONST.__got: 0x1c50
   __DATA_CONST.__const: 0x8c98
   __DATA_CONST.__objc_classlist: 0x1450
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12120
+  __DATA_CONST.__objc_selrefs: 0x12130
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x1318
   __DATA_CONST.__objc_arraydata: 0x14e8
-  __AUTH_CONST.__auth_got: 0x2028
+  __AUTH_CONST.__auth_got: 0x2018
   __AUTH_CONST.__const: 0x4bc8
-  __AUTH_CONST.__cfstring: 0x21440
-  __AUTH_CONST.__objc_const: 0x48078
+  __AUTH_CONST.__cfstring: 0x21460
+  __AUTH_CONST.__objc_const: 0x48080
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0xb90

   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x1830
   __DATA.__data: 0x3f68
-  __DATA.__bss: 0x2e40
+  __DATA.__bss: 0x2e48
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_ivar: 0x1944
   __DATA_DIRTY.__objc_data: 0x79a8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 376965BF-6352-3B4F-B502-88B1735AC46E
-  Functions: 19655
-  Symbols:   2730
-  CStrings:  27867
+  UUID: E5071E3E-D602-341D-AD90-55510938BF0A
+  Functions: 19653
+  Symbols:   2728
+  CStrings:  27875
 
Symbols:
- _dispatch_assert_queue_barrier
- _dispatch_barrier_sync
CStrings:
+ "AccountDataSecurityObserver gets deallocated"
+ "CoreCDP is now reporting that manatee is available for the logged in account."
+ "CoreCDP reports that manatee availability has changed from %{public}@ to %{public}@ for account ID %@."
+ "CoreCDP reports that manatee availability has changed from %{public}@ to %{public}@ for account ID %@. Posting a notification for it"
+ "CoreCDP reports that manatee availability is %@ for the logged in account.%{public}@%@"
+ "CoreCDP reports that walrus has changed from %{public}@ to %{public}@ for accountID %@"
+ "CoreCDP reports that walrus has changed from %{public}@ to %{public}@ for accountID %@. Posting a notification about it..."
+ "T@\"NSError\",R,C,N,V_cachedCDPErrorForManateeStatus"
+ "T@\"NSError\",R,C,N,V_cachedCDPErrorForWalrusStatus"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_notificationQueue"
+ "Tq,R,N,V_cachedManateeAvailableForLoggedInAccount"
+ "Tq,R,N,V_cachedWalrusStatusForLoggedInAccount"
+ "_cachedCDPErrorForManateeStatus"
+ "_cachedCDPErrorForWalrusStatus"
+ "_cachedManateeAvailableForLoggedInAccount"
+ "_fetchAndUpdateManateeAvailability"
+ "_postAccountChangeNotificationForAccountID:"
+ "_requestWillComplete:"
+ "_setCachedManateeAvailableForLoggedInAccount:CDPErrorForManatee:shouldNotifyIfChanged:"
+ "_setCachedWalrusStatusForLoggedInAccount:CDPErrorForWalrusStatus:shouldNotifyIfChanged:"
+ "altDSIDsToManateeAvailabilitiesOverrides"
+ "cachedCDPErrorForManateeStatus"
+ "cachedCDPErrorForWalrusStatus"
+ "cachedManateeAvailableForLoggedInAccount"
+ "com.apple.cloudkit.account.manateeWalrusNotificationQueue"
+ "handleDaemonRequestWillCompleteWithClassName:testRequestProperties:replyBlock:"
+ "req: %{public}@, \"%{public}@ Relinquishing zone gatekeeper on successful response\""
+ "setNotificationQueue:"
+ "v36@0:8q16@24B32"
- "!A"
- "CoreCDP is now reporting that manatee is%{public}@ available for the logged in account.%{public}@%@"
- "CoreCDP reports that manatee is%{public}@ available for the logged in account.%{public}@%@"
- "CoreCDP reports that walrus is changing from %{public}@ to enabled."
- "T@\"NSError\",C,N,V_lastCDPErrorForManateeStatus"
- "T@\"NSError\",C,N,V_lastCDPErrorForWalrusStatus"
- "Tq,N,S_lockedSetManateeAvailableForLoggedInAccount:,V_manateeAvailableForLoggedInAccount"
- "Tq,N,V_cachedWalrusStatusForLoggedInAccount"
- "_lastCDPErrorForManateeStatus"
- "_lastCDPErrorForWalrusStatus"
- "_lockedFetchAndUpdateManateeAvailability"
- "_lockedSetManateeAvailableForLoggedInAccount:"
- "_manateeAvailableForLoggedInAccount"
- "_setCachedWalrusStatusForLoggedInAccount:shouldNotifyIfChanged:"
- "com.apple.cloudkit.account.manateeStatusQueue"
- "lastCDPErrorForManateeStatus"
- "lastCDPErrorForWalrusStatus"
- "manateeAvailableForLoggedInAccount"
- "setCachedWalrusStatusForLoggedInAccount:"
- "setLastCDPErrorForManateeStatus:"
- "setLastCDPErrorForWalrusStatus:"
- "v28@0:8q16B24"

```
