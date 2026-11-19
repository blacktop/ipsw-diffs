## mds_stores

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x339cc
+2465.1.9.0.0
+  __TEXT.__text: 0x3394c
   __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x2220
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x158c
   __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x36fd
-  __TEXT.__oslogstring: 0x2328
+  __TEXT.__cstring: 0x36f4
+  __TEXT.__oslogstring: 0x2317
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__objc_methname: 0x2741
   __TEXT.__objc_classname: 0x208

   - /usr/lib/libobjc.A.dylib
   Functions: 1687
   Symbols:   642
-  CStrings:  1335
+  CStrings:  1334
 
Functions:
~ sub_100009e28 : 2428 -> 2420
~ sub_100015c14 -> sub_100015c0c : 3972 -> 3912
~ sub_10002af24 -> sub_10002aee0 : 240 -> 224
~ sub_10002b33c -> sub_10002b2e8 : 2236 -> 2192
CStrings:
+ "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, plugin:%s"
+ "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s typeExtension:%d bundleId:%s"
- "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, mail2:%s, plugin:%s"
- "_MAIL_V2"
- "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s MV2:%s typeExtension:%d bundleId:%s"
```
