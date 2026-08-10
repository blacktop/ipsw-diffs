## bootpd

> `/usr/libexec/bootpd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x110f4
+557.0.0.0.0
+  __TEXT.__text: 0x11288
   __TEXT.__auth_stubs: 0x970
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1f14
-  __TEXT.__oslogstring: 0x11a2
+  __TEXT.__oslogstring: 0x11c4
   __TEXT.__unwind_info: 0x2f8
   __DATA_CONST.__const: 0x1318
   __DATA_CONST.__cfstring: 0xcc0

   - /usr/lib/libresolv.9.dylib
   Functions: 213
   Symbols:   199
-  CStrings:  651
+  CStrings:  652
 
Functions:
~ sub_1000019bc : 6864 -> 6872
~ sub_100003ac4 -> sub_100003acc : 832 -> 836
~ sub_1000110e8 -> sub_1000110f4 : 1020 -> 1412
CStrings:
+ "frame_length %zu > sendbuf_len %u"
```
