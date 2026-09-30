## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`

```diff

-328.0.6.0.0
-  __TEXT.__text: 0x26c3c0
-  __TEXT.__const: 0x175e80
-  __TEXT.__cstring: 0x169c2
+328.0.9.0.0
+  __TEXT.__text: 0x270608
+  __TEXT.__const: 0x175e90
+  __TEXT.__cstring: 0x16acf
   __TEXT.__oslogstring: 0xaa5
   __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__unwind_info: 0x3110
+  __TEXT.__unwind_info: 0x3120
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x2ffe0
+  __DATA_CONST.__const: 0x30000
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
   __DATA_CONST.__got: 0x0

   __AUTH_CONST.__auth_got: 0xb00
   __AUTH.__data: 0x18
   __DATA.__objc_classrefs: 0x18
-  __DATA.__data: 0x50
+  __DATA.__data: 0x70
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xac0
   __DATA.__common: 0x178

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4803
+  Functions: 4820
   Symbols:   587
-  CStrings:  4309
+  CStrings:  4319
 
CStrings:
+ "Compression-"
+ "DSC::__stub_region"
+ "__TEXT"
+ "__stub_region_"
+ "__text"
+ "dyld_shared_cache_for_each_unattributed_range"
+ "dyld_shared_cache_get_cpu_subtype"
+ "dyld_shared_cache_get_cpu_type"
+ "dyld_shared_cache_range_type_all_code"
+ "libhwtrace @ tag libhwtrace-328.0.9"
+ "libhwtrace @ tag libhwtrace-328.0.9\n"
+ "tag libhwtrace-328.0.9"
+ "v32@?0Q8Q16^{dispatch_data_s=}24"
- "libhwtrace @ tag libhwtrace-328.0.6"
- "libhwtrace @ tag libhwtrace-328.0.6\n"
- "tag libhwtrace-328.0.6"
```
