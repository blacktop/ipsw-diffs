## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-  __TEXT.__text: 0x2c100
+  __TEXT.__text: 0x2c128
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x4ab9
+  __TEXT.__cstring: 0x4ada
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x1708
   __DATA_CONST.__helper: 0x8

   - /usr/lib/system/libxpc.dylib
   Functions: 1101
   Symbols:   3062
-  CStrings:  550
+  CStrings:  551
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__helper : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ __ZNK6mach_o9Universal5validEy : 860 -> 864
~ __ZNK6mach_o9Universal12forEachSliceEU13block_pointerFvNS_12ArchitectureEyyhRbE : 464 -> 468
~ __ZNK6mach_o9Universal9bestSliceERKNS_19GradedArchitecturesEbRNS0_5SliceE : 432 -> 436
~ __ZNK6mach_o12UnsafeHeader22validSemanticsSegmentsERKNS_6PolicyEy : 1464 -> 1492
CStrings:
+ "too many segments %llu (max 255)"

```
