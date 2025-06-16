## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x7373e8
+5200.6.2.0.0
+  __TEXT.__text: 0x737730
   __TEXT.__auth_stubs: 0x3ea0
-  __TEXT.__objc_methlist: 0x4232c
+  __TEXT.__objc_methlist: 0x4233c
   __TEXT.__const: 0x1c684
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x76e83
+  __TEXT.__cstring: 0x76eb4
   __TEXT.__swift5_typeref: 0x3d4
   __TEXT.__swift5_capture: 0x168
   __TEXT.__constg_swiftt: 0x558

   __TEXT.__swift5_reflstr: 0x242
   __TEXT.__swift5_fieldmd: 0x28c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__oslogstring: 0x3fa08
+  __TEXT.__oslogstring: 0x3fa96
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__gcc_except_tab: 0x38144
+  __TEXT.__gcc_except_tab: 0x38180
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1bd80
+  __TEXT.__unwind_info: 0x1bd98
   __TEXT.__eh_frame: 0x920
   __TEXT.__objc_classname: 0xc77f
-  __TEXT.__objc_methname: 0x8d273
+  __TEXT.__objc_methname: 0x8d2c1
   __TEXT.__objc_methtype: 0x17845
   __TEXT.__objc_stubs: 0x4f900
   __DATA_CONST.__got: 0x52c0
-  __DATA_CONST.__const: 0x1d168
+  __DATA_CONST.__const: 0x1d190
   __DATA_CONST.__objc_classlist: 0x28d0
   __DATA_CONST.__objc_catlist: 0x490
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19a08
+  __DATA_CONST.__objc_selrefs: 0x19a10
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x1dd0
   __DATA_CONST.__objc_arraydata: 0x8720
   __AUTH_CONST.__auth_got: 0x1f68
   __AUTH_CONST.__const: 0xdee8
   __AUTH_CONST.__cfstring: 0x3cb60
-  __AUTH_CONST.__objc_const: 0x7bcd8
+  __AUTH_CONST.__objc_const: 0x7bcf8
   __AUTH_CONST.__objc_arrayobj: 0x1f08
   __AUTH_CONST.__objc_intobj: 0x4458
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xb7b0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x432c
+  __DATA.__objc_ivar: 0x4330
   __DATA.__data: 0x78c0
   __DATA.__common: 0x24
   __DATA.__bss: 0x480

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5BA8BBE4-0810-36E8-9190-28BDD4414392
-  Functions: 33202
-  Symbols:   102938
-  CStrings:  43586
+  UUID: 4E05E6D7-71B3-3B42-ADCF-B0FCB9B481B5
+  Functions: 33206
+  Symbols:   102949
+  CStrings:  43591
 
Symbols:
+ -[HDDatabase _protectedDataQueue_handleSpringboardLockoutNotification]
+ -[HDDatabase unitTest_triggerSpringboardLockout]
+ GCC_except_table152
+ _OBJC_IVAR_$_HDDatabase._protectedDataLock_protectedDataState
+ _OBJC_IVAR_$_HDDatabase._springboardLockoutToken
+ ___48-[HDDatabase unitTest_triggerSpringboardLockout]_block_invoke
+ ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.555
+ ___65-[HDDatabase _protectedDataQueue_beginObservingContentProtection]_block_invoke
+ ___78-[HDDatabase _protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.530
+ ___block_descriptor_40_ea8_32w_e8_v12?0i8lw32l8
+ ___block_literal_global.520
+ ___block_literal_global.537
+ ___block_literal_global.607
+ ___block_literal_global.632
- _OBJC_IVAR_$_HDDatabase._protectedDataState
- ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.554
- ___78-[HDDatabase _protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.529
- ___block_literal_global.519
- ___block_literal_global.536
- ___block_literal_global.631
CStrings:
+ "%{public}@: Received biolockout notification; flushing protected data"
+ "Ignoring invalid protection state transition (%{public}@ -> %{public}@)"
+ "_protectedDataLock_protectedDataState"
+ "_springboardLockoutToken"
+ "com.apple.springboard.lock-with-force-biolockout"
+ "unitTest_triggerSpringboardLockout"
- "_protectedDataState"

```
