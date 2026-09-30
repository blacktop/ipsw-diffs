## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

 27102.0.0.0.0
-  __TEXT.__text: 0x5c798
+  __TEXT.__text: 0x5c7a8
   __TEXT.__const: 0x1c0ac
   __TEXT.__cstring: 0xe6f7
   __TEXT.__unwind_info: 0x2368
Functions:
~ ___liblibc_aligned_memcmp_secure : 96 -> 100
~ _xrt__log_write_prefixed_lines : 252 -> 264
```
