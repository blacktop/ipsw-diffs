## coreimportd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/A/Support/coreimportd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x7bdc
+2465.1.9.0.0
+  __TEXT.__text: 0x7bb0
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_stubs: 0x400
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x228
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x7d9
-  __TEXT.__oslogstring: 0xa6e
+  __TEXT.__cstring: 0x7d0
+  __TEXT.__oslogstring: 0xa5d
   __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__objc_methname: 0x327
   __TEXT.__objc_classname: 0x60

   - /usr/lib/libobjc.A.dylib
   Functions: 295
   Symbols:   234
-  CStrings:  236
+  CStrings:  235
 
Functions:
~ sub_100004208 : 2236 -> 2192
CStrings:
+ "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, plugin:%s"
+ "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s typeExtension:%d bundleId:%s"
- "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, mail2:%s, plugin:%s"
- "_MAIL_V2"
- "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s MV2:%s typeExtension:%d bundleId:%s"
```
