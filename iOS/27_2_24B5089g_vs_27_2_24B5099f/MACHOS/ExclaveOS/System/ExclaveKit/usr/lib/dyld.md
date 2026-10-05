## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27102.0.0.0.0
-  __TEXT.__text: 0x5c7a8
+27104.0.0.0.0
+  __TEXT.__text: 0x5c954
   __TEXT.__const: 0x1c0ac
-  __TEXT.__cstring: 0xe6f7
-  __TEXT.__unwind_info: 0x2368
+  __TEXT.__cstring: 0xe781
+  __TEXT.__unwind_info: 0x2378
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0xb50
   __AUTH_CONST.__const: 0x3f20

   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x550
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2762
-  Symbols:   2438
-  CStrings:  1475
+  Functions: 2766
+  Symbols:   2441
+  CStrings:  1478
 
Symbols:
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
+ __process_panicv
+ _process_panicv.panic
+ _xrt__process_panic_exception
- xrt_process_panicv.panic
CStrings:
+ "27104"
+ "load command #%d %.*s name offset too small"
+ "load command #%d %.*s not a dylib load command"
+ "load command #%d string start offset too small"
- "27102"
```
