## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27059.3.0.0.0
-  __TEXT.__text: 0x5bb58
+27060.1.0.0.0
+  __TEXT.__text: 0x5bc38
   __TEXT.__const: 0x1c0a8
   __TEXT.__cstring: 0xe51e
-  __TEXT.__unwind_info: 0x1e80
+  __TEXT.__unwind_info: 0x1e88
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0xaf0
   __AUTH_CONST.__const: 0x3ee8

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x550
-  __DATA.__bss: 0xba3f8
+  __DATA.__bss: 0xba408
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2744
-  Symbols:   2420
+  Functions: 2746
+  Symbols:   2422
   CStrings:  1461
 
Symbols:
+ _plat_common_initialize_stdio
+ _xrt_dyld_setup_stdio
CStrings:
+ "27060.1"
- "27059.3"
```
