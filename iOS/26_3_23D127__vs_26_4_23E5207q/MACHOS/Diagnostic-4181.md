## Diagnostic-4181

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4181.appex/Diagnostic-4181`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x5d8
-  __TEXT.__auth_stubs: 0x110
+1066.100.26.0.0
+  __TEXT.__text: 0x620
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x44
   __TEXT.__objc_classname: 0x33

   __TEXT.__cstring: 0x14
   __TEXT.__oslogstring: 0x3e
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96AC8511-236C-30DD-A621-4F2945050A6C
+  UUID: A8C0643E-C302-37CC-A419-0003280B6551
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
~ sub_100000c50 : 264 -> 284
~ sub_100000d58 -> sub_100000d6c : 452 -> 468
~ sub_100000f1c -> sub_100000f40 : 380 -> 396
~ sub_100001098 -> sub_1000010cc : 280 -> 300

```
