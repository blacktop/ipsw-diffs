## addressbooksyncd

> `/usr/libexec/addressbooksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-307.0.0.0.0
-  __TEXT.__text: 0x3bf0c
+308.0.0.0.0
+  __TEXT.__text: 0x3c090
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x7940
   __TEXT.__objc_methlist: 0x4578
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x924
   __TEXT.__objc_methname: 0x84b6
-  __TEXT.__cstring: 0x2d76
+  __TEXT.__cstring: 0x2dac
   __TEXT.__objc_classname: 0x5fb
   __TEXT.__objc_methtype: 0x13f2
-  __TEXT.__oslogstring: 0x25f2
-  __TEXT.__unwind_info: 0xd18
+  __TEXT.__oslogstring: 0x263e
+  __TEXT.__unwind_info: 0xd20
   __DATA_CONST.__const: 0xe98
-  __DATA_CONST.__cfstring: 0x3300
+  __DATA_CONST.__cfstring: 0x3340
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_nlcatlist: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 1627
   Symbols:   407
-  CStrings:  2700
+  CStrings:  2704
 
Functions:
~ sub_100025fb8 : 100 -> 300
~ sub_100032a40 -> sub_100032b08 : 564 -> 752
CStrings:
+ "== Started AddressBookSync-308"
+ "Forcing census alert via %@ override"
+ "Forcing favorites sync via %@ override"
+ "internal_forceCensusAlert"
+ "internal_forceFavoritesSync"
- "== Started AddressBookSync-307"
```
