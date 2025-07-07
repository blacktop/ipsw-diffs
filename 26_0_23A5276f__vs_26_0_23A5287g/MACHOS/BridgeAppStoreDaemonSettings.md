## BridgeAppStoreDaemonSettings

> `/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings`

```diff

-12.0.48.0.0
-  __TEXT.__text: 0x16584
-  __TEXT.__auth_stubs: 0x1000
+12.0.54.2.1
+  __TEXT.__text: 0x14c88
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x5e8
+  __TEXT.__objc_methlist: 0x600
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__const: 0x5e8
-  __TEXT.__cstring: 0xad3
-  __TEXT.__objc_methname: 0x14c6
-  __TEXT.__constg_swiftt: 0x288
-  __TEXT.__swift5_typeref: 0x439
-  __TEXT.__swift5_reflstr: 0x58
-  __TEXT.__swift5_fieldmd: 0xe0
-  __TEXT.__swift5_capture: 0x1e4
-  __TEXT.__oslogstring: 0x676
+  __TEXT.__const: 0x578
+  __TEXT.__cstring: 0xab5
+  __TEXT.__objc_methname: 0x14ed
+  __TEXT.__constg_swiftt: 0x264
+  __TEXT.__swift5_typeref: 0x3eb
+  __TEXT.__swift5_reflstr: 0x69
+  __TEXT.__swift5_fieldmd: 0xc4
+  __TEXT.__swift5_capture: 0x2f0
+  __TEXT.__oslogstring: 0x666
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x20
   __TEXT.__objc_classname: 0x83
   __TEXT.__objc_methtype: 0x2bc
-  __TEXT.__swift_as_entry: 0x54
-  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x48
   __TEXT.__gcc_except_tab: 0x2c0
-  __TEXT.__unwind_info: 0x648
-  __TEXT.__eh_frame: 0xa28
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x2b8
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__eh_frame: 0x9f8
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x200
-  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_selrefs: 0x798
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x648
-  __DATA.__data: 0x3a0
-  __DATA.__bss: 0x600
-  __DATA.__common: 0x178
+  __DATA.__data: 0x380
+  __DATA.__bss: 0x590
+  __DATA.__common: 0x160
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F821CAC-395A-3D2F-8907-9AD84D9C3EA2
-  Functions: 433
-  Symbols:   224
-  CStrings:  528
+  UUID: D8AEE09D-88DC-3CDD-A806-5E3762BC7A29
+  Functions: 404
+  Symbols:   220
+  CStrings:  529
 
Symbols:
+ _AMSAccountMediaTypeAppStore
+ _AMSAccountMediaTypeAppStoreBeta
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
- _OBJC_CLASS_$_AMSBag
- _OBJC_CLASS_$_AMSSnapshotBag
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_continuation_await
- _swift_continuation_init
- _swift_deallocPartialClassInstance
- _swift_isaMask
CStrings:
+ "Fatal error"
+ "Returning bag from persistence"
+ "Sync bag load from network"
+ "Sync bag load from persistence"
+ "ams_DSID"
+ "ams_createEphemeralAccount"
+ "appstoredServiceForAccount:"
+ "appstoredServiceForSandboxAccount:"
+ "lastRecentBagMutex"
+ "persistedBagOnQueue:completionHandler:"
+ "unsignedLongLongValue"
- "Failed to load bag from network or storage"
- "_createCheckedThrowingContinuation(_:)"
- "bagForProfile:profileVersion:processInfo:"
- "doubleValue"
- "initWithAccount:"
- "integerValue"
- "lastRecentBag"
- "setAccountMediaType:"
- "v24@?0@\"AMSSnapshotBag\"8@\"NSError\"16"
- "valueWithError:"

```
