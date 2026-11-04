## duetexpertd

> `/usr/libexec/duetexpertd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__objc_selrefs`

```diff

-678.0.1.0.0
-  __TEXT.__text: 0x454
+678.2.1.0.3
+  __TEXT.__text: 0x440
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x160
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x35e
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x330
   __TEXT.__oslogstring: 0x4e
   __TEXT.__objc_methname: 0xf1
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__auth_got: 0xc8

   - /usr/lib/libsqlite3.dylib
   Functions: 3
   Symbols:   43
-  CStrings:  34
+  CStrings:  33
 
Functions:
~ sub_100000c28 : 828 -> 808
CStrings:
- "com.apple.MobileStoreDemo.ShallowRefreshReady"
```
