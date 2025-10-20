## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

 64572.149.1.0.0
-  __TEXT.__text: 0xb1054
+  __TEXT.__text: 0xb1098
   __TEXT.__auth_stubs: 0x2410
   __TEXT.__objc_methlist: 0x65e8
-  __TEXT.__const: 0x2c6
+  __TEXT.__const: 0x2e6
   __TEXT.__cstring: 0x10048
   __TEXT.__gcc_except_tab: 0x4ed8
   __TEXT.__oslogstring: 0x185c

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3A1AE7C3-E525-3DC7-BDEC-B0AE2369ADA8
+  UUID: 9E0A1A6A-3FEC-3820-A32F-A712DD501FBC
   Functions: 3128
   Symbols:   10561
   CStrings:  7765
Symbols:
+ ___swift_instantiateConcreteTypeFromMangledNameV2
- ___swift_instantiateConcreteTypeFromMangledName
Functions:
~ sub_1c62e2374 -> sub_1c6842374 : 312 -> 320
~ sub_1c62e24ac -> sub_1c68424b4 : 488 -> 496
~ sub_1c62e2694 -> sub_1c68426a4 : 540 -> 548
~ ___swift_instantiateConcreteTypeFromMangledName -> ___swift_instantiateConcreteTypeFromMangledNameV2 : 76 -> 72
~ sub_1c62e40a4 -> sub_1c68440b8 : 604 -> 612
~ sub_1c62e4300 -> sub_1c684431c : 608 -> 616
~ sub_1c62e47cc -> sub_1c68447f0 : 324 -> 332
~ sub_1c62e4910 -> sub_1c684493c : 340 -> 348
~ sub_1c62e4a64 -> sub_1c6844a98 : 244 -> 252
~ sub_1c62e4b58 -> sub_1c6844b94 : 212 -> 220

```
