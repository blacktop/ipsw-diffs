## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-3.1.6.0.0
-  __TEXT.__text: 0x76b54
+3.2.4.0.0
+  __TEXT.__text: 0x76ebc
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x5454
+  __TEXT.__objc_methlist: 0x545c
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0xd62f
+  __TEXT.__oslogstring: 0xd709
   __TEXT.__cstring: 0x5938
   __TEXT.__gcc_except_tab: 0x818
   __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x1c58
+  __TEXT.__unwind_info: 0x1c5c
   __TEXT.__objc_classname: 0x1c0e
-  __TEXT.__objc_methname: 0xf8d0
+  __TEXT.__objc_methname: 0xf8e2
   __TEXT.__objc_methtype: 0x3e81
-  __TEXT.__objc_stubs: 0x8f20
+  __TEXT.__objc_stubs: 0x8f40
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_classlist: 0x4a0

   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xfdc0
-  __DATA_CONST.__objc_selrefs: 0x2a88
+  __DATA_CONST.__objc_selrefs: 0x2a90
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__objc_const: 0x39c0
   __AUTH_CONST.__cfstring: 0x5860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2899
-  Symbols:   9938
-  CStrings:  4469
+  Functions: 2901
+  Symbols:   9943
+  CStrings:  4473
 
Symbols:
+ -[BLSHBacklightDisplayStateMachine resumeDisplayMode:]
+ ___54-[BLSHBacklightDisplayStateMachine resumeDisplayMode:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64r72r80w_e5_v8?0lr64l8w80l8r72l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72w_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20lw72l8s32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_97_e8_32s40s48s56s64r72r80w_e5_v8?0lw80l8s32l8s40l8s48l8s56l8r64l8r72l8
+ _objc_msgSend$resumeDisplayMode:
- ___block_descriptor_80_e8_32s40s48s56r64w_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20lw64l8s32l8s40l8s48l8r56l8
- ___block_descriptor_89_e8_32s40s48s56s64r72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_96_e8_32s40s48s56s64r72w_e5_v8?0lr64l8w72l8s32l8s40l8s48l8s56l8
CStrings:
+ "DSM:%p resumed display mode:%{public}@ did not match current target:%{public}@"
+ "DSM:%p resumed transition to display mode:%{public}@"
+ "TSM:%p will resume (if needed) and wait for display operation to complete: %{public}@"
+ "resumeDisplayMode:"

```
