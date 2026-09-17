## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27062.0.0.0.0
-  __TEXT.__text: 0x5c654
-  __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xec46
-  __TEXT.__unwind_info: 0x2368
+27102.0.0.0.0
+  __TEXT.__text: 0x5c8d8
+  __TEXT.__const: 0x1c0ac
+  __TEXT.__cstring: 0xeca4
+  __TEXT.__unwind_info: 0x2380
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0xb50
-  __AUTH_CONST.__const: 0x3f18
+  __AUTH_CONST.__const: 0x3f50
   __AUTH.__data: 0x470
   __DATA.__data: 0x1448
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x550
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2758
-  Symbols:   2433
-  CStrings:  1472
+  Functions: 2763
+  Symbols:   2441
+  CStrings:  1477
 
Symbols:
+ __ZN5dyld44APIs28_dyld_with_active_atlas_PRIVEPvPFvS1_PKvmE
+ __ZN6mach_o12ArchitectureC1EPK11mach_header
+ __ZN6mach_o6PolicyC1ERKNS_6HeaderEbbb
+ __ZN6mach_o6PolicyC2ENS_12ArchitectureENS_19PlatformAndVersionsEjbbb
+ __ZN6mach_o8Platform5Epoch8fall2026E
+ __ZNK6mach_o5Image19maxAuthRebaseOffsetEv
+ __ZNK6mach_o6Header4archEv
+ __ZNK6mach_o6Header8fileTypeEv
+ __ZNK6mach_o6Policy34enforceAuthRebasesPointWithinImageEv
+ __ZNK6mach_o8Platform5epochENS_9Version32E
+ ____ZNK6mach_o5Image19maxAuthRebaseOffsetEv_block_invoke
+ ___memmove_chk
- _OUTLINED_FUNCTION_14
- ___liblibc_stream_error
- _append_char
- _xrt__platform_init_stack
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.MacOSX.platform/Developer/SDKs/ExclaveKit.MacOSX27.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
+ "27102"
+ "__memmove_chk"
+ "_insecure_random_buf"
+ "rebase out of range"
+ "s[0] || s[1]"
+ "src/libc/string/memmove.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.MacOSX.platform/Developer/SDKs/ExclaveKit.MacOSX27.0.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "27062"
```
