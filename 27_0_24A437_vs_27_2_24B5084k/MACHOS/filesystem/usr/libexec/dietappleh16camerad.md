## dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-6.21.0.0.0
-  __TEXT.__text: 0x1accc
-  __TEXT.__auth_stubs: 0xed0
+6.103.0.0.0
+  __TEXT.__text: 0x1af10
+  __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__const: 0x15c0
-  __TEXT.__cstring: 0x3287
+  __TEXT.__cstring: 0x3288
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__oslogstring: 0x21af
+  __TEXT.__oslogstring: 0x223b
   __TEXT.__objc_methname: 0x343
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__unwind_info: 0x790
   __DATA_CONST.__const: 0x9b68
   __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x778
+  __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x138

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 393
-  Symbols:   289
-  CStrings:  629
+  Functions: 397
+  Symbols:   291
+  CStrings:  631
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "6.103"
+ "Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n"
+ "Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n"
- "6.21"
```
