## Diagnostic-3741

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3741.appex/Diagnostic-3741`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x274
-  __TEXT.__auth_stubs: 0x90
+1066.100.26.0.0
+  __TEXT.__text: 0x2d0
+  __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__const: 0x8

   __TEXT.__objc_classname: 0x23
   __TEXT.__objc_methname: 0xf3
   __TEXT.__objc_methtype: 0x47
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x50
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x58
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE043BFE-E653-30F3-B493-63305DF70AE4
+  UUID: EB652691-4BF1-30D5-815F-BA1CA5635E1B
   Functions: 8
-  Symbols:   21
+  Symbols:   22
   CStrings:  24
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_100000bf0 : 276 -> 296
~ sub_100000d04 -> sub_100000d18 : 68 -> 72
~ sub_100000d48 -> sub_100000d60 : 64 -> 68
~ sub_100000d88 -> sub_100000da4 : 76 -> 80
~ sub_100000de4 -> sub_100000e04 : 20 -> 80

```
