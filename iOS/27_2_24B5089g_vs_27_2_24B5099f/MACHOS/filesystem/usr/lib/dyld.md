## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27102.0.0.0.0
-  __TEXT.__text: 0x9a61c
+27104.0.0.0.0
+  __TEXT.__text: 0x9a4b0
   __TEXT.__const: 0x1998
-  __TEXT.__cstring: 0x12587
-  __TEXT.__unwind_info: 0x3650
+  __TEXT.__cstring: 0x1263d
+  __TEXT.__unwind_info: 0x3648
   __DATA_CONST.__const: 0x5618
   __AUTH_CONST.__const: 0x2760
   __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0
-  __DATA_DIRTY.__data: 0x6c
   __DATA_DIRTY.__all_image_info: 0x170
+  __DATA_DIRTY.__data: 0x64
   __DATA_DIRTY.__common: 0x1160
   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3425
-  Symbols:   3673
-  CStrings:  2256
+  Functions: 3423
+  Symbols:   3667
+  CStrings:  2260
 
Symbols:
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _ZNK6mach_o6Header29stringFromOffsetInLoadCommandERKNS0_15LoadCommandInfoEjPNS_5ErrorE
- __ZZ16get_xprr_versionvE19cached_xprr_version
CStrings:
+ "27104"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Sep 30 20:51:37 PDT 2026; root:libignition-64~29579/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Wed Sep 30 20:51:37 PDT 2026; root:libignition-64~29579/libignition_core/RELEASE_ARM64E"
+ "load command #%d %.*s name offset too small"
+ "load command #%d %.*s not a dylib load command"
+ "load command #%d %.*s path offset too small"
+ "load command #%d string start offset too small"
- "27102"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Sep 13 19:37:18 PDT 2026; root:libignition-64~27375/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sun Sep 13 19:37:18 PDT 2026; root:libignition-64~27375/libignition_core/RELEASE_ARM64E"
```
