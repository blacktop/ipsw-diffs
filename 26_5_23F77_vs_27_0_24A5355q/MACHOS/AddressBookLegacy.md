## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12851.600.11.0.0
-  __TEXT.__text: 0x2758
-  __TEXT.__auth_stubs: 0x460
+12872.100.1.0.0
+  __TEXT.__text: 0x2558
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__gcc_except_tab: 0x94
   __TEXT.__objc_methname: 0x554
-  __TEXT.__cstring: 0x30a
+  __TEXT.__cstring: 0x30f
   __TEXT.__oslogstring: 0x71a
-  __TEXT.__objc_classname: 0x19
+  __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xad
   __TEXT.__dlopen_cstrs: 0xa3
   __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x130
   __DATA.__objc_selrefs: 0x180
   __DATA.__objc_ivar: 0xc

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48828758-3E6C-3977-9CA7-C2715804B529
-  Functions: 44
-  Symbols:   90
+  UUID: E5E0053A-E54D-3E20-ACB4-81122CD4CC58
+  Functions: 43
+  Symbols:   93
   CStrings:  139
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
CStrings:
+ "CNBackgroundColorAnalyzer"
+ "Class getCNBackgroundColorAnalyzerClass(void)_block_invoke"
- "CNDominantColorAnalyzer"
- "Class getCNDominantColorAnalyzerClass(void)_block_invoke"

```
