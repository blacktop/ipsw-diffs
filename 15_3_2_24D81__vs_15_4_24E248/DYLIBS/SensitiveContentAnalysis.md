## SensitiveContentAnalysis

> `/System/Library/Frameworks/SensitiveContentAnalysis.framework/Versions/A/SensitiveContentAnalysis`

```diff

-88.1.0.0.0
-  __TEXT.__text: 0x139fc
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x55c
+91.14.0.0.0
+  __TEXT.__text: 0x1390c
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x11c0
-  __TEXT.__cstring: 0xa8e
+  __TEXT.__cstring: 0x99e
   __TEXT.__oslogstring: 0x4df
   __TEXT.__gcc_except_tab: 0x270
   __TEXT.__dlopen_cstrs: 0xc2
+  __TEXT.__swift5_typeref: 0x6f6
   __TEXT.__constg_swiftt: 0x368
-  __TEXT.__swift5_typeref: 0x6cc
   __TEXT.__swift5_reflstr: 0x1d1
   __TEXT.__swift5_fieldmd: 0x228
   __TEXT.__swift5_types: 0x64
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_capture: 0x158
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x138
-  __TEXT.__unwind_info: 0x7f8
-  __TEXT.__eh_frame: 0x8fc
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__eh_frame: 0x9dc
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methname: 0x1199
   __TEXT.__objc_methtype: 0x28d
   __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x6b0
-  __AUTH_CONST.__const: 0xab0
+  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__const: 0xb00
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0xba0
+  __AUTH_CONST.__objc_const: 0xb48
   __AUTH.__objc_data: 0x360
   __AUTH.__data: 0x280
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x4d8
+  __DATA.__data: 0x4e8
   __DATA.__bss: 0x1f60
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FC9D1CE7-7030-37CA-9138-A1CA38237AE2
-  Functions: 680
-  Symbols:   744
-  CStrings:  347
+  UUID: 35D7255E-0F0F-3F8B-8F14-6DC094C2A2B5
+  Functions: 693
+  Symbols:   761
+  CStrings:  342
 
Symbols:
+ +[SCAnalytics sharedInstance].cold.1
+ +[SCLog clientUI].cold.1
+ +[SCLog client].cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_0
+ _symbolic SccySo21SCSensitivityAnalysisC______pG s5ErrorP
+ _symbolic So7NSErrorCSgIeyBy_Sg
+ block_copy_helper.1
+ block_copy_helper.11
+ block_descriptor.13
+ block_descriptor.3
+ block_destroy_helper.12
+ block_destroy_helper.2
- _swift_arrayDestroy
- _symbolic So7NSErrorCSgIeyBy_
- block_descriptor.1
- block_descriptor.9
CStrings:
+ "init()"
- "Division by zero"
- "Division results in an overflow"
- "Swift/IntegerTypes.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"

```
