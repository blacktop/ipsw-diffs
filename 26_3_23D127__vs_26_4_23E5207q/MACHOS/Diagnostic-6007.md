## Diagnostic-6007

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6007.appex/Diagnostic-6007`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x28cc
+1066.100.26.0.0
+  __TEXT.__text: 0x2830
   __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x204
-  __TEXT.__const: 0x105
-  __TEXT.__objc_methname: 0x31e
-  __TEXT.__cstring: 0x39c
+  __TEXT.__const: 0x106
+  __TEXT.__objc_classname: 0x81
+  __TEXT.__objc_methname: 0x6b3
+  __TEXT.__objc_methtype: 0x182
   __TEXT.__constg_swiftt: 0x1c0
   __TEXT.__swift5_typeref: 0xbd
   __TEXT.__swift5_reflstr: 0x2cc
   __TEXT.__swift5_fieldmd: 0x198
   __TEXT.__swift5_capture: 0x64
   __TEXT.__oslogstring: 0x139
+  __TEXT.__cstring: 0x10c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__objc_classname: 0x31
-  __TEXT.__objc_methtype: 0x120
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F9A01772-34A9-33F1-9568-8383A9D1E662
+  UUID: 502AD1A1-904C-381B-9F85-13DDD51C06B8
   Functions: 67
   Symbols:   82
-  CStrings:  106
+  CStrings:  107
 
Symbols:
+ _objc_release_x24
+ _objc_retain_x22
- __swift_FORCE_LOAD_$_swiftAccelerate
- _objc_retain_x26
Functions:
~ sub_100001498 -> sub_1000014a0 : 1276 -> 1268
~ sub_100001994 : 252 -> 236
~ sub_100001b2c -> sub_100001b1c : 24 -> 16
~ sub_100001b44 -> sub_100001b2c : 568 -> 576
~ sub_10000225c -> sub_10000224c : 1652 -> 1568
~ sub_1000028d0 -> sub_10000286c : 324 -> 292
~ sub_100002a58 -> sub_1000029d4 : 140 -> 128
~ sub_100002c60 -> sub_100002bd0 : 16 -> 20
~ sub_100002f00 -> sub_100002e74 : 76 -> 68
~ sub_100002f4c -> sub_100002eb8 : 268 -> 276
~ sub_100003058 -> sub_100002fcc : 92 -> 84
~ sub_100003100 -> sub_10000306c : 304 -> 312
~ sub_100003230 -> sub_1000031a4 : 236 -> 244
~ sub_1000034b8 -> sub_100003434 : 676 -> 668
~ sub_100003b34 -> sub_100003aa8 : 184 -> 176
CStrings:
+ "OnDemandAudioDiagnosticTriggerController"
+ "OnDemandAudioDiagnosticTriggerInputs"

```
