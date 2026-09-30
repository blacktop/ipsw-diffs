## Diagnostic-3744

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0xa18
-  __TEXT.__auth_stubs: 0x170
+1066.100.26.0.0
+  __TEXT.__text: 0xa84
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__gcc_except_tab: 0x54
   __TEXT.__cstring: 0x131
   __TEXT.__objc_classname: 0x1d
   __TEXT.__objc_methname: 0x22b
   __TEXT.__objc_methtype: 0x21
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__auth_got: 0xb8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x200

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C58DDFD-ECCD-3156-AFAD-303B792C7C40
+  UUID: 1F48DDF3-A713-3ED6-BEAE-96A112F58062
   Functions: 6
-  Symbols:   45
+  Symbols:   43
   CStrings:  72
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x8
Functions:
~ sub_100000be8 : 236 -> 240
~ sub_100000cd4 -> sub_100000cd8 : 1056 -> 1092
~ sub_10000110c -> sub_100001134 : 1040 -> 1104
~ sub_10000151c -> sub_100001584 : 228 -> 232

```
