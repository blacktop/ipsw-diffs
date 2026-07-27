## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__helper`
- `__AUTH_CONST.__const`

```diff

-1385.0.0.0.0
-  __TEXT.__text: 0x2e97c
+1387.0.0.0.0
+  __TEXT.__text: 0x2e9a4
   __TEXT.__auth_stubs: 0x670
   __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x4b68
+  __TEXT.__cstring: 0x4b89
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x970
   __DATA_CONST.__helper: 0x8

   - /usr/lib/system/libxpc.dylib
   Functions: 1173
   Symbols:   1618
-  CStrings:  554
+  CStrings:  555
 
Functions:
~ __ZNK6mach_o9Universal5validEy : 860 -> 864
~ __ZNK6mach_o9Universal12forEachSliceEU13block_pointerFvNS_12ArchitectureEyyhRbE : 464 -> 468
~ __ZNK6mach_o9Universal9bestSliceERKNS_19GradedArchitecturesEbRNS0_5SliceE : 432 -> 436
~ __ZNK6mach_o12UnsafeHeader22validSemanticsSegmentsERKNS_6PolicyEy : 1464 -> 1492
CStrings:
+ "too many segments %llu (max 255)"
```
