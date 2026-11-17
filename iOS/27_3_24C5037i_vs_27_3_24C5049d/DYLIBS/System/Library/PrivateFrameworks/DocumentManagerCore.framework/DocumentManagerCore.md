## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

```diff

-403.2.4.0.0
-  __TEXT.__text: 0x7f214
-  __TEXT.__objc_methlist: 0x45f0
-  __TEXT.__const: 0x19ac
-  __TEXT.__cstring: 0x52a1
+403.2.6.0.0
+  __TEXT.__text: 0x7fde4
+  __TEXT.__objc_methlist: 0x4630
+  __TEXT.__const: 0x19bc
+  __TEXT.__cstring: 0x5391
   __TEXT.__gcc_except_tab: 0x6f8
-  __TEXT.__oslogstring: 0x4bb4
+  __TEXT.__oslogstring: 0x4c64
   __TEXT.__ustring: 0x98
-  __TEXT.__swift5_typeref: 0xd13
+  __TEXT.__swift5_typeref: 0xd3b
   __TEXT.__swift5_capture: 0x474
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_fieldmd: 0x334

   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_ret: 0x138
   __TEXT.__swift_as_cont: 0x258
-  __TEXT.__unwind_info: 0x2e48
+  __TEXT.__unwind_info: 0x2e80
   __TEXT.__eh_frame: 0x24c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a80
+  __DATA_CONST.__const: 0x1b20
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ae0
+  __DATA_CONST.__objc_selrefs: 0x2b18
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x778
   __AUTH_CONST.__const: 0x1c70
   __AUTH_CONST.__cfstring: 0x3220
-  __AUTH_CONST.__objc_const: 0x7020
+  __AUTH_CONST.__objc_const: 0x7030
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0xe98
   __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0xa20
+  __DATA.__data: 0xa40
   __DATA_DIRTY.__objc_data: 0x15d8
   __DATA_DIRTY.__data: 0xf08
   __DATA_DIRTY.__bss: 0xa10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3271
-  Symbols:   3139
-  CStrings:  927
+  Functions: 3287
+  Symbols:   3153
+  CStrings:  934
 
Symbols:
+ -[DOCAppProtectionManager _appIntentAccessToApplication:isFileProvider:completion:]
+ -[DOCAppProtectionManager _appIntentAccessToContentOfNode:completion:]
+ -[DOCAppProtectionManager appIntentAccessToNode:completion:]
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table79
+ _DOCDomainIsOffloadedOrInstallationHeld
+ _OUTLINED_FUNCTION_27
+ ___70-[DOCAppProtectionManager _appIntentAccessToContentOfNode:completion:]_block_invoke
+ ___70-[DOCAppProtectionManager _appIntentAccessToContentOfNode:completion:]_block_invoke_2
+ ___83-[DOCAppProtectionManager _appIntentAccessToApplication:isFileProvider:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e21_v20?0"NSString"8B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0Q8ls32l8s40l8s48l8
+ _symbolic _____ySo6FINodeCSgG s23_ContiguousArrayStorageC
+ _symbolic _____ySo6FPItemCSgG s23_ContiguousArrayStorageC
- GCC_except_table57
- GCC_except_table68
- GCC_except_table77
CStrings:
+ "-[DOCAppProtectionManager _appIntentAccessToApplication:isFileProvider:completion:]_block_invoke"
+ "-[DOCAppProtectionManager _appIntentAccessToContentOfNode:completion:]_block_invoke_2"
+ "[PROTECTED APPS] %s denying App Intent access (%lu) to node: %@ protected by: %@"
+ "[PROTECTED APPS] %s getIsChallengeCurrentlyRequiredForSubject: %@ failed with error: %@"
+ "v16@?0Q8"
+ "v20@?0@\"NSString\"8B16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
```
