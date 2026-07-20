## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-403.0.0.0.0
-  __TEXT.__text: 0x169f4
-  __TEXT.__objc_methlist: 0xd8c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x1294
-  __TEXT.__oslogstring: 0x7b1
+405.0.0.0.1
+  __TEXT.__text: 0x16e0c
+  __TEXT.__objc_methlist: 0xd9c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x12ba
+  __TEXT.__oslogstring: 0x7f6
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__unwind_info: 0x650
+  __TEXT.__unwind_info: 0x658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x920
+  __DATA_CONST.__objc_selrefs: 0x928
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1140
+  __AUTH_CONST.__cfstring: 0x1160
   __AUTH_CONST.__objc_const: 0x1730
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x4b0
   __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 455
-  Symbols:   1123
-  CStrings:  234
+  Functions: 459
+  Symbols:   1129
+  CStrings:  236
 
Symbols:
+ -[GSStorageManager _listAdditionsInNamespace:underPath:error:]
+ GCC_except_table30
+ GCC_except_table40
+ _GSAdditionProviderContentVersionPreviousBaseKey
+ ___62-[GSStorageManager _listAdditionsInNamespace:underPath:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSArray"816"NSError"24ls32l8
+ _makeGSProviderContentVersion
- GCC_except_table28
CStrings:
+ "[ERROR] Provider-content-version V2 build failed, falling back to V1"
+ "kGSProviderContentVersionPreviousBase"
```
