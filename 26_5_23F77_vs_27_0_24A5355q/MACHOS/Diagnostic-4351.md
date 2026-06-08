## Diagnostic-4351

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4351.appex/Diagnostic-4351`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xe54
-  __TEXT.__auth_stubs: 0x200
+1351.0.0.0.0
+  __TEXT.__text: 0xd44
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x320
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__const: 0x18

   __TEXT.__objc_methname: 0x258
   __TEXT.__objc_methtype: 0x36
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x160
   __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 877FB3E7-9BAF-3C5E-A26E-73B9138907B8
-  Functions: 21
-  Symbols:   58
+  UUID: 8586DD64-D774-341B-A390-99FD2907B616
+  Functions: 19
+  Symbols:   59
   CStrings:  62
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
- _objc_retain_x26

```
