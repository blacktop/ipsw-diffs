## libHSFilerDynamic.dylib

> `/usr/lib/libHSFilerDynamic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-1576.0.0.0.0
-  __TEXT.__text: 0x34720
+1580.0.0.0.0
+  __TEXT.__text: 0x347a0
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2158
+  __TEXT.__const: 0x2160
   __TEXT.__gcc_except_tab: 0x240c
   __TEXT.__cstring: 0xa20
-  __TEXT.__oslogstring: 0x2bb0
+  __TEXT.__oslogstring: 0x2c14
   __TEXT.__unwind_info: 0x1090
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x5e0

   - /usr/lib/libcompression.dylib
   Functions: 793
   Symbols:   1419
-  CStrings:  379
+  CStrings:  380
 
Functions:
~ __ZN22HSFilerRT_Internal_INT13readFile_syncENSt3__110shared_ptrIN18HSFilerRT_Internal7SessionEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEmNS0_8functionIFvPKvmEEE : 2412 -> 2540
CStrings:
+ "error: BB reported actual_file_size_bytes_t7 (%zu) > preallocated fileSize (%zu) for session (%llu)"
```
