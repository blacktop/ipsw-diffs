## Diagnostic-4180

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4180.appex/Diagnostic-4180`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x71c
-  __TEXT.__auth_stubs: 0x120
+1066.100.26.0.0
+  __TEXT.__text: 0x7e4
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x8

   __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methtype: 0x13a
   __TEXT.__objc_methname: 0x4b9
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x98
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x80

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA020779-11F5-399E-BD6A-3A5EE867F6E2
+  UUID: 11A513C2-2969-3E13-B780-2A14FACC3426
   Functions: 13
-  Symbols:   40
+  Symbols:   41
   CStrings:  103
 
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
~ sub_100000d40 : 452 -> 468
~ sub_100000f04 -> sub_100000f14 : 380 -> 396
~ sub_100001080 -> sub_1000010a0 : 280 -> 300
~ sub_10000119c -> sub_1000011d0 : 304 -> 332
~ sub_1000012dc -> sub_10000132c : 20 -> 80
~ sub_100001304 -> sub_100001390 : 192 -> 200
~ sub_1000013cc -> sub_100001460 : 12 -> 64

```
