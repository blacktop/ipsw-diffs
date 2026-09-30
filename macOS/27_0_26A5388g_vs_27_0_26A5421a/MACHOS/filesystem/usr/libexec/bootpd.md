## bootpd

> `/usr/libexec/bootpd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x1dc78
+557.0.0.0.0
+  __TEXT.__text: 0x1de1c
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__const: 0x148
+  __TEXT.__const: 0x158
   __TEXT.__cstring: 0x2d38
-  __TEXT.__oslogstring: 0x20f7
+  __TEXT.__oslogstring: 0x2119
   __TEXT.__unwind_info: 0x450
   __DATA_CONST.__const: 0x14d8
   __DATA_CONST.__cfstring: 0x12e0

   - /usr/lib/libresolv.9.dylib
   Functions: 308
   Symbols:   292
-  CStrings:  950
+  CStrings:  951
 
Functions:
~ sub_100001a6c : 7588 -> 7596
~ sub_100003e48 -> sub_100003e50 : 836 -> 840
~ sub_100006e08 -> sub_100006e14 : 5440 -> 5456
~ sub_100013fb4 -> sub_100013fd0 : 1020 -> 1412
CStrings:
+ "frame_length %zu > sendbuf_len %u"
```
