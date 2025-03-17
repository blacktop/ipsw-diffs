## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-588.11.0.0.0
-  __TEXT.__text: 0x438f14
-  __TEXT.__auth_stubs: 0x31a0
-  __TEXT.__objc_methlist: 0x38124
+588.11.1.0.0
+  __TEXT.__text: 0x43c65c
+  __TEXT.__auth_stubs: 0x31f0
+  __TEXT.__objc_methlist: 0x381dc
   __TEXT.__const: 0x2b72
-  __TEXT.__cstring: 0x577c2
-  __TEXT.__oslogstring: 0x39ff6
-  __TEXT.__gcc_except_tab: 0xef0c
+  __TEXT.__cstring: 0x57a72
+  __TEXT.__oslogstring: 0x3a056
+  __TEXT.__gcc_except_tab: 0xeed0
   __TEXT.__dlopen_cstrs: 0x23c
   __TEXT.__ustring: 0x90
-  __TEXT.__swift5_typeref: 0xdfe
+  __TEXT.__swift5_typeref: 0xf62
   __TEXT.__constg_swiftt: 0x162c
   __TEXT.__swift5_reflstr: 0x6eb
   __TEXT.__swift5_fieldmd: 0xa10
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x128
   __TEXT.__swift5_assocty: 0x210
-  __TEXT.__swift5_capture: 0x430
+  __TEXT.__swift5_capture: 0x520
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift_as_entry: 0xc8
   __TEXT.__swift_as_ret: 0xb4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xd840
+  __TEXT.__unwind_info: 0xd900
   __TEXT.__eh_frame: 0x1bd4
   __TEXT.__objc_classname: 0x8b6b
-  __TEXT.__objc_methname: 0xac53d
-  __TEXT.__objc_methtype: 0x1951d
+  __TEXT.__objc_methname: 0xac656
+  __TEXT.__objc_methtype: 0x19545
   __TEXT.__objc_stubs: 0x4c4c0
-  __DATA_CONST.__got: 0x3668
-  __DATA_CONST.__const: 0xb910
-  __DATA_CONST.__objc_classlist: 0x1ef8
+  __DATA_CONST.__got: 0x3670
+  __DATA_CONST.__const: 0xb8f0
+  __DATA_CONST.__objc_classlist: 0x1f00
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8d0
+  __DATA_CONST.__objc_selrefs: 0x1b918
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x1500
   __DATA_CONST.__objc_arraydata: 0x1370
-  __AUTH_CONST.__auth_got: 0x18e8
-  __AUTH_CONST.__auth_ptr: 0x4c0
-  __AUTH_CONST.__const: 0x7660
-  __AUTH_CONST.__cfstring: 0x39a60
-  __AUTH_CONST.__objc_const: 0x816b0
+  __AUTH_CONST.__auth_got: 0x1910
+  __AUTH_CONST.__auth_ptr: 0x4b8
+  __AUTH_CONST.__const: 0x79d0
+  __AUTH_CONST.__cfstring: 0x39a40
+  __AUTH_CONST.__objc_const: 0x81858
   __AUTH_CONST.__objc_intobj: 0x33c0
   __AUTH_CONST.__objc_arrayobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x4b40
-  __AUTH.__data: 0x1c08
+  __AUTH.__objc_data: 0x4bb0
+  __AUTH.__data: 0x1c28
   __DATA.__objc_ivar: 0x4a70
-  __DATA.__data: 0x3b60
-  __DATA.__bss: 0x1bb0
-  __DATA.__common: 0x58
+  __DATA.__data: 0x3bb0
+  __DATA.__bss: 0x1bd0
+  __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0xed90
-  __DATA_DIRTY.__data: 0x8f8
+  __DATA_DIRTY.__data: 0x8e8
   __DATA_DIRTY.__bss: 0xb20
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24536
-  Symbols:   29309
-  CStrings:  34922
+  Functions: 24623
+  Symbols:   29324
+  CStrings:  34955
 
Symbols:
+ _OBJC_CLASS_$_ATXNotificationNextAppLaunchRecorder
+ _OBJC_METACLASS_$_ATXNotificationNextAppLaunchRecorder
+ _swift_projectBox
- _kATXNotificationAndSuggestionAppLaunchTimestampDefaultsKey
CStrings:
+ "$__lazy_storage_$_appLaunchTimestampKey"
+ "-AppLaunchTimestamp"
+ ":receivedDateAfter"
+ "@\"ATXNotificationNextAppLaunchRecorder\""
+ "@\"NSSet\"8@?0"
+ "@56@0:8@16@24@32@?40@?48"
+ "ATXNotificationNextAppLaunchRecorder"
+ "AppPredictionInternal_Private.NotificationNextAppLaunchRecorder"
+ "NotificationNextAppLaunchRecorder"
+ "NotificationNextAppLaunchRecorder.queue"
+ "NotificationNextAppLaunchRecorder: Could not fetch app launch stream, error: %s"
+ "NotificationNextAppLaunchRecorder: startDate: %s"
+ "T@\"ATXNotificationAndSuggestionDatastore\",N,R,VdataStore"
+ "T@\"NSString\",N,C"
+ "T@\"NSUserDefaults\",N,R,Vdefaults"
+ "T@\"OS_dispatch_queue\",N,&"
+ "T@?,N,C"
+ "T@?,N,R"
+ "UPDATE notifications SET nextAppLaunchTimestamp = :nextAppLaunchTimestamp WHERE bundleId = :bundleId AND receiveTimestamp >= :receivedDateAfter AND receiveTimestamp < :nextAppLaunchTimestamp"
+ "_notificationNextAppLaunchRecorder"
+ "appLaunchPublisherProvider"
+ "appLaunchTimestampKey"
+ "defaultsKeyPrefix"
+ "initWithDefaults:dataStore:defaultsKeyPrefix:appLaunchPublisherProvider:installedAppsProvider:"
+ "installedAppsProvider"
+ "resetDefaults"
+ "setAppLaunchPublisherProvider:"
+ "setAppLaunchTimestampKey:"
+ "setQueue:"
+ "updateNotificationsWithNextAppLaunch"
+ "updateNotificationsWithNextAppLaunchDate:receivedDateAfter:forBundleId:"
- "ATXNotificationAndSuggestionDatastoreAppLaunchTimestamp"
- "UPDATE notifications SET nextAppLaunchTimestamp = :nextAppLaunchTimestamp WHERE bundleId = :bundleId AND receiveTimestamp > :startTimestamp AND receiveTimestamp < :nextAppLaunchTimestamp"
- "[%@] Could not fetch app launch stream with error: %@"
- "updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:"
- "updateNotificationsWithNextAppLaunchTimestamp:bundleId:startTimestamp:"

```
