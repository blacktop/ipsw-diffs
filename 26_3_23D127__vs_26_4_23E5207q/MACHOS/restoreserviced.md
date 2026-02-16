## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 46.0.0.0.0
-  __TEXT.__text: 0x14880
-  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__text: 0x14150
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_stubs: 0x17a0
   __TEXT.__objc_methlist: 0xcc4
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x79b5
+  __TEXT.__cstring: 0x7931
   __TEXT.__oslogstring: 0x3a5
-  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__gcc_except_tab: 0x204
   __TEXT.__objc_methname: 0x1823
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x789
-  __TEXT.__unwind_info: 0x588
-  __DATA_CONST.__auth_got: 0x760
+  __TEXT.__unwind_info: 0x568
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__cfstring: 0x3a60

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23CAA371-4253-3598-BCAB-E6989B09682C
-  Functions: 532
-  Symbols:   294
-  CStrings:  1899
+  UUID: 45F5AA9B-F008-3845-9A3D-E7CD33B6153D
+  Functions: 552
+  Symbols:   290
+  CStrings:  1895
 
Symbols:
+ _objc_release_x25
+ _objc_retain_x20
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_release_x27
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x21
- _objc_retain_x24
- _objc_retain_x8
CStrings:
- "CHECKPOINT_INTERNAL_ERROR(%s): invalid outcome=%d\n"
- "checkpoint_get_outcome_attributes"
- "checkpoint_nvram_store_set_string"
- "dest == NULL"

```
