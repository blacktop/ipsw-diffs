## Diagnostic-8441

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Diagnostic-8441`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x448
+1066.100.26.0.0
+  __TEXT.__text: 0x46c
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x20

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 479BBD73-5B20-39DA-8D1F-1289387BAC79
+  UUID: ABD8188C-4048-30A8-AF60-D977C0D3EB3F
   Functions: 4
   Symbols:   36
   CStrings:  24
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ sub_100000c40 : 324 -> 340
~ sub_100000d84 -> sub_100000d94 : 528 -> 544
~ sub_100000f94 -> sub_100000fb4 : 92 -> 96

```
