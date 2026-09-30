## afscexpand

> `usr/bin/afscexpand`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

 174.160.2.0.0
-  __TEXT.__text: 0x13df8
+  __TEXT.__text: 0x13808
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__const: 0x235a0
+  __TEXT.__const: 0x235c0
   __TEXT.__cstring: 0xbca
   __TEXT.__unwind_info: 0x218
   __TEXT.__eh_frame: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 120
+  Functions: 121
   Symbols:   61
   CStrings:  67
 
```
