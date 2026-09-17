## afscexpand

> `/usr/bin/afscexpand`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`

```diff

-182.0.0.0.0
-  __TEXT.__text: 0x1620c
+182.40.3.0.0
+  __TEXT.__text: 0x15b3c
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__const: 0x23888
-  __TEXT.__cstring: 0xbf3
+  __TEXT.__const: 0x238a8
+  __TEXT.__cstring: 0xc29
   __TEXT.__unwind_info: 0x260
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0x11d8
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10

   - /usr/lib/libz.1.dylib
   Functions: 129
   Symbols:   61
-  CStrings:  68
+  CStrings:  69
 
CStrings:
+ "%s:%d: chunk %u produced %lld of %lld expected bytes\n"
```
