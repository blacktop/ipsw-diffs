## mdimport

> `/usr/bin/mdimport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x2951c
+2465.1.9.0.0
+  __TEXT.__text: 0x294f0
   __TEXT.__auth_stubs: 0x1de0
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x14f4
-  __TEXT.__cstring: 0x6a02
-  __TEXT.__oslogstring: 0x927
+  __TEXT.__cstring: 0x69f9
+  __TEXT.__oslogstring: 0x916
   __TEXT.__gcc_except_tab: 0x288
   __TEXT.__objc_methname: 0xdae
   __TEXT.__objc_classname: 0x2e

   - /usr/lib/libz.1.dylib
   Functions: 660
   Symbols:   614
-  CStrings:  1564
+  CStrings:  1563
 
Functions:
~ sub_100013664 : 2236 -> 2192
CStrings:
+ "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, plugin:%s"
+ "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s typeExtension:%d bundleId:%s"
- "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, mail2:%s, plugin:%s"
- "_MAIL_V2"
- "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s MV2:%s typeExtension:%d bundleId:%s"
```
