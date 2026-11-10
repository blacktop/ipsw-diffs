## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__info_plist`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__auth_ptr`
- `__DATA_DIRTY.__all_image_info`

```diff

-27062.0.0.0.0
-  __TEXT.__text: 0xa0ec8
-  __TEXT.__const: 0x1a38
-  __TEXT.__cstring: 0x13886
+27104.0.0.0.0
+  __TEXT.__text: 0xa136c
+  __TEXT.__const: 0x1a68
+  __TEXT.__cstring: 0x13950
   __TEXT.__info_plist: 0x4e3
-  __TEXT.__unwind_info: 0x3578
+  __TEXT.__unwind_info: 0x3590
   __DATA_CONST.__const: 0x2bd0
-  __AUTH_CONST.__const: 0x6310
+  __AUTH_CONST.__const: 0x6348
   __AUTH_CONST.__auth_ptr: 0x98
-  __DATA.__data: 0x1c8
+  __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0
   __DATA.__bss: 0x518
-  __DATA_DIRTY.__data: 0x1c20
   __DATA_DIRTY.__all_image_info: 0x170
+  __DATA_DIRTY.__data: 0x1c18
   __DATA_DIRTY.__common: 0x1980
   __DATA_DIRTY.__bss: 0x48
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3369
-  Symbols:   3762
-  CStrings:  2376
+  Functions: 3376
+  Symbols:   3769
+  CStrings:  2381
 
Symbols:
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ __ZN5dyld44APIs28_dyld_with_active_atlas_PRIVEPvPFvS1_PKvmE
+ __ZNK6mach_o5Image19maxAuthRebaseOffsetEv
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
+ __ZNK6mach_o6Policy34enforceAuthRebasesPointWithinImageEv
+ ____ZNK6mach_o5Image19maxAuthRebaseOffsetEv_block_invoke
- __ZZ16get_xprr_versionvE19cached_xprr_version
CStrings:
+ "27104"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Oct 10 00:30:20 PDT 2026; root:libignition-64~29901/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sat Oct 10 00:30:20 PDT 2026; root:libignition-64~29901/libignition_core/RELEASE_ARM64E"
+ "load command #%d %.*s name offset too small"
+ "load command #%d %.*s not a dylib load command"
+ "load command #%d %.*s path offset too small"
+ "load command #%d string start offset too small"
+ "rebase out of range"
- "27062"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Aug 11 20:40:24 PDT 2026; root:libignition-64~19252/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Aug 11 20:40:24 PDT 2026; root:libignition-64~19252/libignition_core/RELEASE_ARM64E"
```
