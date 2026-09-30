## PerformanceLoggingDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x80b8
-  __TEXT.__auth_stubs: 0x540
+430.0.0.0.0
+  __TEXT.__text: 0x8104
+  __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x8cc
-  __TEXT.__const: 0x1e0
+  __TEXT.__objc_methlist: 0x8d4
+  __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x12c9
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0xba0
-  __TEXT.__objc_methname: 0x34d4
+  __TEXT.__objc_methname: 0x34e8
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methtype: 0x641
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x248
   __DATA_CONST.__const: 0x560
   __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0x17e0
-  __DATA.__objc_selrefs: 0x788
+  __DATA.__objc_selrefs: 0x790
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x30

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 250
-  Symbols:   273
-  CStrings:  755
+  Functions: 251
+  Symbols:   274
+  CStrings:  756
 
Symbols:
+ _objc_opt_new
Functions:
~ sub_100002ccc : 7684 -> 7656
+ sub_100004ab4
CStrings:
+ "allTaskingPrefNames"
```
