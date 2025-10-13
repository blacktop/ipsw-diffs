## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.2.11.2.0
-  __TEXT.__text: 0x7920f8
+6200.2.12.0.0
+  __TEXT.__text: 0x792128
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43afc
+  __TEXT.__objc_methlist: 0x43b1c
   __TEXT.__const: 0x1df7c
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7d12f
+  __TEXT.__cstring: 0x7d130
   __TEXT.__constg_swiftt: 0x14dc
   __TEXT.__swift5_typeref: 0xd9d
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__gcc_except_tab: 0x383b4
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1cd28
+  __TEXT.__unwind_info: 0x1cd30
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8ebec
-  __TEXT.__objc_methtype: 0x16b0a
-  __TEXT.__objc_stubs: 0x50520
+  __TEXT.__objc_methname: 0x8ec70
+  __TEXT.__objc_methtype: 0x16b56
+  __TEXT.__objc_stubs: 0x50560
   __DATA_CONST.__got: 0x5668
   __DATA_CONST.__const: 0x1d2a0
   __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19ed8
+  __DATA_CONST.__objc_selrefs: 0x19ef0
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
   __AUTH_CONST.__const: 0x10018
   __AUTH_CONST.__cfstring: 0x3d5e0
-  __AUTH_CONST.__objc_const: 0x7d960
+  __AUTH_CONST.__objc_const: 0x7d948
   __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xd120
   __AUTH.__data: 0x760
-  __DATA.__objc_ivar: 0x43b8
+  __DATA.__objc_ivar: 0x43b4
   __DATA.__data: 0x81c8
   __DATA.__common: 0x64
   __DATA.__bss: 0x18c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CDC5C05D-D0A4-3374-B824-8E1ECAAA3885
-  Functions: 34762
-  Symbols:   103898
-  CStrings:  44260
+  UUID: CE312F8F-AA13-31A6-BA5D-B8B20C7D8607
+  Functions: 34764
+  Symbols:   103903
+  CStrings:  44264
 
Symbols:
+ -[HDDeviceKeyValueStoreManager registerObserver:]
+ -[HDDeviceKeyValueStoreManager unregisterObserver:]
+ -[HDWorkoutManager _performFinishAllDetachedWorkoutBuilders]
+ -[HDWorkoutManager _scheduleFinishForDetachedWorkoutBuilders]
+ ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_finishAllDetachedWorkoutBuilders
+ _objc_msgSend$_scheduleFinishForDetachedWorkoutBuilders
- -[HDDeviceKeyValueStoreManager addObserver:]
- -[HDDeviceKeyValueStoreManager removeObserver:]
- _OBJC_IVAR_$_HDDeviceKeyValueStoreManager._lock
- ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
CStrings:
+ "Multiple storage groups retrieved while fetching the most recent entry."
+ "_finishAllDetachedWorkoutBuilders"
+ "_scheduleFinishForDetachedWorkoutBuilders"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "Multiple storage groups retrived while fetching the most recent entry."

```
