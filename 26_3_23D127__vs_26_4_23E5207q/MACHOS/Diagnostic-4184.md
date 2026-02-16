## Diagnostic-4184

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4184.appex/Diagnostic-4184`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x5d8
-  __TEXT.__auth_stubs: 0x110
+1066.100.26.0.0
+  __TEXT.__text: 0x620
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x8

   __TEXT.__objc_methtype: 0x24
   __TEXT.__objc_methname: 0x20b
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D91A04D-DCC0-33B3-93BF-7EB4BA001EE7
+  UUID: 5CB6E58F-68A3-3990-94F5-5E33C6B230A1
   Functions: 5
-  Symbols:   37
+  Symbols:   38
   CStrings:  40
 
Symbols:
+ _objc_release_x19
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ sub_100000c50 : 452 -> 468
~ sub_100000e14 -> sub_100000e24 : 380 -> 396
~ sub_100000f90 -> sub_100000fb0 : 280 -> 300
~ sub_1000010a8 -> sub_1000010dc : 264 -> 284

```
