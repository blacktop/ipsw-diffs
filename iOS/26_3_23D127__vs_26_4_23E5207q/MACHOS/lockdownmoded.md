## lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

-80.0.5.0.0
-  __TEXT.__text: 0x2d948
-  __TEXT.__auth_stubs: 0x1200
-  __TEXT.__objc_stubs: 0x380
-  __TEXT.__objc_methlist: 0x4dc
-  __TEXT.__const: 0x10a8
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__objc_methname: 0x151d
-  __TEXT.__cstring: 0x16d3
-  __TEXT.__oslogstring: 0x2772
-  __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methtype: 0xaa7
+80.100.8.0.0
+  __TEXT.__text: 0x2c184
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__const: 0x1098
+  __TEXT.__cstring: 0xd21
   __TEXT.__swift5_typeref: 0x6e3
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__objc_classname: 0x491
+  __TEXT.__objc_methname: 0x16c9
+  __TEXT.__objc_methtype: 0xc75
   __TEXT.__constg_swiftt: 0xb94
   __TEXT.__swift5_reflstr: 0x424
   __TEXT.__swift5_fieldmd: 0x438
+  __TEXT.__oslogstring: 0x2692
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x94

   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6c8
-  __TEXT.__eh_frame: 0x798
-  __DATA_CONST.__auth_got: 0x910
-  __DATA_CONST.__got: 0x340
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__unwind_info: 0x680
+  __TEXT.__eh_frame: 0x760
+  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__auth_ptr: 0x310
-  __DATA_CONST.__const: 0xe80
-  __DATA_CONST.__cfstring: 0x160
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1168
-  __DATA.__objc_selrefs: 0x608
-  __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x558
-  __DATA.__data: 0x135a
-  __DATA.__bss: 0x11b0
+  __DATA.__objc_const: 0x1018
+  __DATA.__objc_selrefs: 0x540
+  __DATA.__objc_data: 0x508
+  __DATA.__data: 0x13aa
+  __DATA.__bss: 0x11a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 56A432D2-FC0E-3493-82DA-41996B4D8578
-  Functions: 599
-  Symbols:   509
-  CStrings:  643
+  UUID: 30761C6E-C0C1-348C-9D60-20D72B9C4E45
+  Functions: 590
+  Symbols:   479
+  CStrings:  566
 
Symbols:
+ _swift_unknownObjectRelease_n
+ _swift_willThrowTypedImpl
- _AnalyticsSendEventLazy
- _NSStringFromClass
- _OBJC_CLASS_$_FLFollowUpController
- _OBJC_CLASS_$_LockdownModeManager
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDictionary
- __NSConcreteGlobalBlock
- ___CFConstantStringClassReference
- ___kCFBooleanTrue
- __os_log_error_impl
- _dispatch_assert_queue$V2
- _dispatch_async
- _dispatch_once
- _dispatch_queue_create
- _notify_cancel
- _notify_register_dispatch
- _objc_alloc
- _objc_autoreleaseReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_copyWeak
- _objc_destroyWeak
- _objc_enumerationMutation
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_opt_class
- _objc_opt_new
- _objc_release_x1
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_storeStrong
- _os_log_create
CStrings:
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "lockdownmoded"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "@\"FLFollowUpController\""
- "@\"NSDictionary\"8@?0"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSUserDefaults\""
- "CFU Receipt already exists"
- "CFU framework not available"
- "Did receive CFU update notification"
- "Failed to post CFU: %@"
- "No Threat Notification CFU"
- "No pending items"
- "T@\"TNUIManager\",R,N"
- "TNUIManager"
- "Threat Notification CFU configured correctly"
- "ThreatNotification"
- "UTF8String"
- "Updated CFU to omit badge: %d"
- "_cfuNotifyToken"
- "_cfuViewed"
- "_clearCache"
- "_controller"
- "_dispatchQueue"
- "_logger"
- "_modifyThreatNotificationCFU"
- "_registerCFUReceiptIfNeededWithLDMEnabled:"
- "_startListener"
- "_userDefaults"
- "analyticsEnabled"
- "com.apple.ThreatNotificationUI.FollowUpEvent"
- "com.apple.ThreatNotificationUI.FollowUpExtension"
- "com.apple.ThreatNotificationUI.FollowUpItem.general"
- "com.apple.ThreatNotificationUI.storage.analyticsCache"
- "com.apple.ThreatNotificationUI.storage.cfuViewed"
- "com.apple.ThreatNotificationUI.storage.threatNotificationTimestamp"
- "com.apple.authkit"
- "com.apple.corefollowup.items_changed"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dictionaryWithObjects:forKeys:count:"
- "displayStyle"
- "elapsedTime"
- "enabled"
- "i"
- "initWithClientIdentifier:"
- "initWithSuiteName:"
- "isEqualToString:"
- "ldmEnabled"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "pendingFollowUpItems:"
- "postFollowUpItem:error:"
- "removeObjectForKey:"
- "setDisplayStyle:"
- "setObject:forKey:"
- "shared"
- "timeIntervalSince1970"
- "type"
- "uniqueIdentifier"
- "v12@?0i8"
- "v20@0:8B16"

```
