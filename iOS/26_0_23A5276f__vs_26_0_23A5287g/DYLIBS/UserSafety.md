## UserSafety

> `/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety`

```diff

-117.0.0.0.0
+119.1.1.0.0
   __TEXT.__text: 0x3a90
   __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x2d0

   __TEXT.__cstring: 0x231
   __TEXT.__oslogstring: 0x229
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0x80
   __TEXT.__objc_methname: 0xb0a
   __TEXT.__objc_methtype: 0x1c9

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FDB0F91-82A8-39D1-85EE-462922DDD848
+  UUID: 150E39CC-A247-382C-8BAA-3C0677CB786D
   Functions: 99
   Symbols:   407
   CStrings:  166
Functions:
~ +[USSensitivityAnalyzer isNudityDetectionEnabled] -> +[USSensitivityAnalyzer settingsReaderClass] : 72 -> 12
~ +[USSensitivityAnalyzer settingsReaderClass] -> +[USSensitivityAnalyzer isNudityDetectionEnabled] : 12 -> 72

```
