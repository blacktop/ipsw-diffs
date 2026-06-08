## Diagnostic-4181

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4181.appex/Diagnostic-4181`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x620
-  __TEXT.__auth_stubs: 0x120
+1351.0.0.0.0
+  __TEXT.__text: 0x5b0
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x44
   __TEXT.__objc_classname: 0x33

   __TEXT.__cstring: 0x14
   __TEXT.__oslogstring: 0x3e
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
-  UUID: 82D85C50-4E01-3721-8944-D858F8584B35
+  UUID: E219FEC1-87AE-378F-BCB6-D8D8A6022E29
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
~ sub_100000c50 : 284 -> 264
~ sub_100000d6c -> sub_100000d58 : 468 -> 452
~ sub_100000f40 -> sub_100000f1c : 396 -> 384
~ sub_1000010cc -> sub_10000109c : 300 -> 280
~ sub_1000011f8 -> sub_1000011b4 : 120 -> 76

```
