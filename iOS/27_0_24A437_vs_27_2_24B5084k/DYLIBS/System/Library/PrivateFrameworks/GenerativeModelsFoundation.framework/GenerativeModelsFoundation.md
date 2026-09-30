## GenerativeModelsFoundation

> `/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation`

```diff

-291.6.0.5.102
-  __TEXT.__text: 0x54b0c
-  __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0xae48
-  __TEXT.__cstring: 0x12b7
-  __TEXT.__swift5_typeref: 0x263c
-  __TEXT.__oslogstring: 0xd73
-  __TEXT.__swift5_reflstr: 0x1433
-  __TEXT.__swift5_assocty: 0x1f8
-  __TEXT.__swift5_fieldmd: 0x2198
-  __TEXT.__constg_swiftt: 0x2114
+297.6.0.5.0
+  __TEXT.__text: 0x5b054
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__const: 0xbeb8
+  __TEXT.__cstring: 0x13a7
+  __TEXT.__swift5_typeref: 0x2924
+  __TEXT.__oslogstring: 0xec3
+  __TEXT.__swift5_reflstr: 0x14f3
+  __TEXT.__swift5_assocty: 0x228
+  __TEXT.__swift5_fieldmd: 0x23c8
+  __TEXT.__constg_swiftt: 0x2348
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_capture: 0x320
-  __TEXT.__swift5_proto: 0x9ac
-  __TEXT.__swift5_types: 0x310
-  __TEXT.__swift_as_entry: 0x90
-  __TEXT.__swift_as_ret: 0x70
-  __TEXT.__swift_as_cont: 0x124
+  __TEXT.__swift5_capture: 0x340
+  __TEXT.__swift5_proto: 0xab8
+  __TEXT.__swift5_types: 0x354
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0x74
+  __TEXT.__swift_as_cont: 0x12c
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x2fd0
-  __TEXT.__eh_frame: 0x2f30
+  __TEXT.__unwind_info: 0x33c8
+  __TEXT.__eh_frame: 0x3258
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x128
+  __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x5ce0
-  __AUTH_CONST.__objc_const: 0x1010
-  __AUTH_CONST.__auth_got: 0xdd8
+  __AUTH_CONST.__const: 0x6568
+  __AUTH_CONST.__objc_const: 0x1018
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH.__objc_data: 0x1d8
   __AUTH.__data: 0xa90
-  __DATA.__data: 0x1b00
+  __DATA.__data: 0x1df0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x68
   __DATA_DIRTY.__data: 0x14c0

   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation
   - /System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4060
-  Symbols:   236
-  CStrings:  166
+  Functions: 4381
+  Symbols:   243
+  CStrings:  178
 
Symbols:
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _notify_cancel
+ _notify_register_dispatch
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
CStrings:
+ "FirstUnlockGate: device already unlocked, invoking handler"
+ "FirstUnlockGate: device locked, registering handler to run on first unlock"
+ "FirstUnlockGate: notify_register_dispatch failed (%{public}u); firing handlers inline"
+ "FirstUnlockGate: received first_unlock notification, draining all the waiting handlers"
+ "awaitFirstUnlock()"
+ "com.apple.GenerativeModels.firstUnlockGate"
+ "com.apple.mobile.keybagd.first_unlock"
+ "contentSafetyMode"
+ "inputPolicies"
+ "outputPolicies"
+ "outputProcessingPolicies"
+ "promptInjectionUntrustedContent"
```
