## Diagnostic-3907

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3907.appex/Diagnostic-3907`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0xb4c
+1066.100.26.0.0
+  __TEXT.__text: 0xc80
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x480
   __TEXT.__objc_methlist: 0x20c

   __TEXT.__objc_methname: 0x50c
   __TEXT.__objc_methtype: 0x126
   __TEXT.__oslogstring: 0x54
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27B29257-A675-30FD-92B9-460FA9069AA7
+  UUID: 460A1FDB-9722-3B5E-91BC-417D740B8EE9
   Functions: 21
   Symbols:   54
   CStrings:  119
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
Functions:
~ _stringOrNull : 92 -> 100
~ sub_100000e54 -> sub_100000e5c : 200 -> 208
~ sub_100000f1c -> sub_100000f2c : 256 -> 268
~ sub_100001024 -> sub_100001040 : 12 -> 64
~ sub_100001048 -> sub_100001098 : 12 -> 64
~ sub_10000109c -> sub_100001120 : 872 -> 916
~ sub_100001414 -> sub_1000014c4 : 476 -> 500
~ sub_1000015f0 -> sub_1000016b8 : 500 -> 536
~ sub_1000017f4 -> sub_1000018e0 : 20 -> 80
~ sub_10000181c -> sub_100001944 : 176 -> 184
~ sub_1000018cc -> sub_1000019fc : 120 -> 124

```
