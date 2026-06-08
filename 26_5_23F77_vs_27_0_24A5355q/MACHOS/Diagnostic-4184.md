## Diagnostic-4184

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4184.appex/Diagnostic-4184`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x620
-  __TEXT.__auth_stubs: 0x120
+1351.0.0.0.0
+  __TEXT.__text: 0x5b0
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x8

   __TEXT.__objc_methtype: 0x24
   __TEXT.__objc_methname: 0x20b
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x98
-  __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x20
   __DATA.__objc_const: 0x120
   __DATA.__objc_selrefs: 0xd8
   __DATA.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFA43EE3-32D5-32EC-B354-F59A3CBFA2BA
+  UUID: F5C1EB7B-13CB-3849-A71C-509B0B6613F9
   Functions: 5
-  Symbols:   38
+  Symbols:   37
   CStrings:  40
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x19
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
Functions:
~ sub_100000c50 : 468 -> 452
~ sub_100000e24 -> sub_100000e14 : 396 -> 384
~ sub_100000fb0 -> sub_100000f94 : 300 -> 280
~ sub_1000010dc -> sub_1000010ac : 284 -> 264
~ sub_1000011f8 -> sub_1000011b4 : 120 -> 76

```
