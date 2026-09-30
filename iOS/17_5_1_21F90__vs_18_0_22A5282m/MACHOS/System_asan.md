## System_asan

> `/System/Library/Frameworks/System.framework/System_asan`

```diff

-1345.120.2.0.0
-  __TEXT.__text: 0x758
+1351.0.0.0.0
+  __TEXT.__text: 0x718
   __TEXT.__auth_stubs: 0x450
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x172
   __TEXT.__oslogstring: 0x35
-  __TEXT.__unwind_info: 0x68
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xe0
-  __DATA.__data: 0x8
   __DATA.__common: 0x408
+  __DATA_DIRTY.__data: 0x8
   - /usr/lib/system/libcache.dylib
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
   Symbols:   99
-  Functions: 9
+  Functions: 8
 

```
