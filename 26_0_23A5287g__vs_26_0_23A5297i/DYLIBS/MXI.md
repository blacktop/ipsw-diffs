## MXI

> `/System/Library/PrivateFrameworks/MXI.framework/MXI`

```diff

-29.0.18.0.1
-  __TEXT.__text: 0x40264
+29.0.19.0.0
+  __TEXT.__text: 0x402e8
   __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0xe68
   __TEXT.__const: 0x9d40
-  __TEXT.__gcc_except_tab: 0x5d60
-  __TEXT.__cstring: 0x397c
-  __TEXT.__oslogstring: 0x2b58
+  __TEXT.__gcc_except_tab: 0x5d78
+  __TEXT.__cstring: 0x3a0e
+  __TEXT.__oslogstring: 0x2b57
   __TEXT.__unwind_info: 0xc00
   __TEXT.__objc_classname: 0x16c
   __TEXT.__objc_methname: 0x3ce3

   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__cfstring: 0x3440
   __AUTH_CONST.__objc_const: 0x1e88
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH.__objc_data: 0x550

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7353533B-4779-3C70-843B-A08F5516A798
+  UUID: 137870CD-F0BE-38E0-B908-7C5287772A04
   Functions: 726
   Symbols:   450
-  CStrings:  1977
+  CStrings:  1979
 
Functions:
~ sub_265c80eb0 -> sub_266c08eb0 : 1640 -> 1708
~ sub_265c8ebec -> sub_266c16c30 : 2828 -> 2824
~ sub_265c948c0 -> sub_266c1c900 : 452 -> 456
~ sub_265c96618 -> sub_266c1e65c : 620 -> 640
~ sub_265c969bc -> sub_266c1ea14 : 1936 -> 1944
~ sub_265c971a0 -> sub_266c1f200 : 540 -> 576
CStrings:
+ "Atlas slice count (%d) exceeds the limit of 32. You can try to set MXISceneBuilderConfigurationAtlasSliceSize option to use fewer, larger slices."
+ "Number of slices: %u\nResolution: %u x %u"
+ "[Core/CoreSerialization.mm:495] Error while reading from compression stream. (source length: %d, read source length: %d, dest length: %d, written dest length: %d)"
+ "[MXI.framework/MXIScene.mm:1024] "
+ "[MXI.framework/MXIScene.mm:988] %@"
- "Number of slices: %lu\nResolution: %u x %u"
- "[Core/CoreSerialization.mm:489] Error while reading from compression stream. (source length: %d, read source length: %d, dest length: %d, written dest length: %d)"
- "[MXI.framework/MXIScene.mm:1021] "
- "[MXI.framework/MXIScene.mm:985] %@"

```
