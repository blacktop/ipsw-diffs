## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 740.63.1.2.0
-  __TEXT.__text: 0xb8c4c
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_stubs: 0xf060
+  __TEXT.__text: 0xb929c
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_stubs: 0xf0e0
   __TEXT.__objc_methlist: 0x73c8
   __TEXT.__const: 0x3e4
-  __TEXT.__gcc_except_tab: 0xfbc
+  __TEXT.__gcc_except_tab: 0xfc8
   __TEXT.__objc_methname: 0x15d0c
-  __TEXT.__oslogstring: 0x1626c
-  __TEXT.__cstring: 0x17a78
+  __TEXT.__oslogstring: 0x1634a
+  __TEXT.__cstring: 0x17b48
   __TEXT.__objc_classname: 0xa44
   __TEXT.__objc_methtype: 0x4403
-  __TEXT.__unwind_info: 0x22f8
-  __DATA_CONST.__const: 0x2a98
-  __DATA_CONST.__cfstring: 0x5cc0
+  __TEXT.__unwind_info: 0x2310
+  __DATA_CONST.__const: 0x2ab8
+  __DATA_CONST.__cfstring: 0x5ce0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xc98
+  __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x11310

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3634
-  Symbols:   801
-  CStrings:  7335
+  Functions: 3639
+  Symbols:   802
+  CStrings:  7343
 
Symbols:
+ _MGGetProductType
CStrings:
+ " [INFO] %{public}s:%d Captured initial displayID: %u"
+ " [INFO] %{public}s:%d Captured recording displayID: %u"
+ " [INFO] %{public}s:%d Display changed from %u to %u"
+ " [INFO] %{public}s:%d Display configuration changed: %u -> %u"
+ "-[RPSession setUpFrontBoardServices]_block_invoke"
+ "-[SCSystemServicesManager captureDidStartForSession:withConfig:]_block_invoke"
+ "-[SCSystemServicesManager setUpFrontBoardServices]_block_invoke"
+ "Localizable-V68"
```
