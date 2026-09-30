## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-403.0.0.0.0
-  __TEXT.__text: 0x1a884
-  __TEXT.__objc_methlist: 0xe04
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x15be
+405.0.0.0.1
+  __TEXT.__text: 0x1acdc
+  __TEXT.__objc_methlist: 0xe14
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x15e4
   __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__oslogstring: 0x81f
-  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__oslogstring: 0x864
+  __TEXT.__unwind_info: 0x6a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x188
-  __AUTH_CONST.__const: 0x790
-  __AUTH_CONST.__cfstring: 0x1460
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0x1480
   __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x4d8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xec

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 500
-  Symbols:   1237
-  CStrings:  262
+  Functions: 504
+  Symbols:   1244
+  CStrings:  264
 
Symbols:
+ -[GSStorageManager _listAdditionsInNamespace:underPath:error:]
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table52
+ GSSetProviderContentVersion
+ _GSAdditionProviderContentVersionPreviousBaseKey
+ ___62-[GSStorageManager _listAdditionsInNamespace:underPath:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSArray"816"NSError"24l
+ _makeGSProviderContentVersion
- GCC_except_table35
- GCC_except_table39
- GCC_except_table48
CStrings:
+ "[ERROR] Provider-content-version V2 build failed, falling back to V1"
+ "kGSProviderContentVersionPreviousBase"
```
