## deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-819.160.6.0.0
-  __TEXT.__text: 0x47ec
-  __TEXT.__auth_stubs: 0x420
+819.160.7.0.0
+  __TEXT.__text: 0x4a40
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x104
   __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__objc_methname: 0x31b
-  __TEXT.__cstring: 0x42b
-  __TEXT.__oslogstring: 0xaf4
+  __TEXT.__cstring: 0x479
+  __TEXT.__oslogstring: 0xbc3
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methtype: 0x7a
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x220
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x160
   __DATA.__objc_selrefs: 0x158
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 46
-  Symbols:   192
-  CStrings:  158
+  Functions: 47
+  Symbols:   196
+  CStrings:  165
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ ___block_descriptor_32_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16l
+ ___periodic_block_invoke
+ _os_variant_has_internal_diagnostics
Functions:
~ _fsPurge : 3332 -> 3360
~ ___main_block_invoke_2 : 220 -> 728
CStrings:
+ "/Library/AutoBugCapture/"
+ "/Library/Logs/AutoBugCapture/"
+ "Customer build, clearing %@"
+ "com.apple.cache_delete"
+ "customerReleaseBuild IS INTERNAL BUILD"
+ "customerReleaseBuild IS NOT INTERNAL BUILD"
+ "customerReleaseBuild IS NOT SEED BUILD"
+ "fsPurge: amountPurged %llu actuallyFreed %llu postPurgeFreespace %llu prePurgeFreespace %llu"
- "customerReleaseBuild IS SEED BUILD"
```
