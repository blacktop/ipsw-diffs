## AppleLatticeSupport

> `/System/Library/PrivateFrameworks/AppleLatticeSupport.framework/AppleLatticeSupport`

```diff

-154.0.0.0.0
-  __TEXT.__text: 0xeb4
-  __TEXT.__auth_stubs: 0x2e0
+156.0.0.0.0
+  __TEXT.__text: 0xf88
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__cstring: 0x1f8
+  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__cstring: 0x20c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x180
+  __TEXT.__objc_methname: 0x162
   __TEXT.__objc_methtype: 0xeb
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x48
+  __TEXT.__objc_stubs: 0x100
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x180
-  __AUTH_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5BD43E57-8840-30C7-AA4A-1DDE0DFAD2E4
-  Functions: 21
-  Symbols:   138
-  CStrings:  73
+  UUID: 71FD5E91-E5A1-35BE-AFCD-D3CBEBDBC60B
+  Functions: 22
+  Symbols:   142
+  CStrings:  75
 
Symbols:
+ GCC_except_table15
+ GCC_except_table18
+ GCC_except_table7
+ _OBJC_CLASS_$_NSConstantDictionary
+ ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke_3
+ ___block_descriptor_40_ea8_32bs_e5_v8?0ls32l8
+ ___kCFBooleanTrue
+ _objc_release_x22
+ _objc_retain_x20
+ _objc_retain_x22
+ _objc_retain_x24
- GCC_except_table14
- GCC_except_table17
- GCC_except_table6
- _OBJC_CLASS_$_NSMutableArray
- _objc_msgSend$addObject:
- _objc_msgSend$arrayWithCapacity:
- _objc_release_x24
- _objc_retain_x19
Functions:
~ -[AppleLatticeServiceRef init] : 176 -> 172
~ -[AppleLatticeServiceRef getInterfaceUpdateEvents:] : 820 -> 968
+ ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke_3
~ __ZNSt3__110unique_ptrIN12_GLOBAL__N_113LatticeClientENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_ : 132 -> 140
~ __ZN12_GLOBAL__N_113LatticeClient14onNotificationEy : 468 -> 504
CStrings:
+ "instanceId"
+ "upToDate"
- "addObject:"
- "arrayWithCapacity:"

```
