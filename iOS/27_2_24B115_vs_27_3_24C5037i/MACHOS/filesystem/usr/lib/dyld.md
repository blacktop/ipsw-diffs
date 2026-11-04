## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27104.0.0.0.0
-  __TEXT.__text: 0x9a4b0
-  __TEXT.__const: 0x1998
-  __TEXT.__cstring: 0x1263d
-  __TEXT.__unwind_info: 0x3648
-  __DATA_CONST.__const: 0x5618
+27200.1.0.0.0
+  __TEXT.__text: 0x9a990
+  __TEXT.__const: 0x19c8
+  __TEXT.__cstring: 0x126a2
+  __TEXT.__unwind_info: 0x3668
+  __DATA_CONST.__const: 0x5668
   __AUTH_CONST.__const: 0x2760
   __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3423
-  Symbols:   3271
-  CStrings:  2260
+  Functions: 3430
+  Symbols:   3277
+  CStrings:  2262
 
Symbols:
+ __ZN3lsl6VectorIN5dyld417InterposeTupleAllEE9push_backERKS2_
+ __ZN5dyld35ArrayIN5dyld417InterposeTupleAllEE9push_backERKS2_
+ __ZNK15DyldSharedCache12inTPRORegionEPKv
+ __ZNK15DyldSharedCache17forEachTPRORegionEU13block_pointerFvPKvyyRbE
+ __ZNK5dyld46Loader6headerERKNS_12RuntimeStateE
+ ____ZNK15DyldSharedCache12inTPRORegionEPKv_block_invoke
CStrings:
+ "  cache dylib rooted, so also interposed cache binds to 0x%08lX with 0x%08lX\n"
+ "27200.1"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Oct 24 01:08:15 PDT 2026; root:libignition-64~30250/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sat Oct 24 01:08:15 PDT 2026; root:libignition-64~30250/libignition_core/RELEASE_ARM64E"
+ "v40@?0r^v8Q16Q24^B32"
- "27104"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Oct 13 20:59:49 PDT 2026; root:libignition-64~29988/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Oct 13 20:59:49 PDT 2026; root:libignition-64~29988/libignition_core/RELEASE_ARM64E"
```
