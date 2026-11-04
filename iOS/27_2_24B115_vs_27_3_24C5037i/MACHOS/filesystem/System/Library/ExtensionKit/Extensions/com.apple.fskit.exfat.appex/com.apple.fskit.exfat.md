## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-561.40.5.0.0
-  __TEXT.__text: 0x12778
+561.60.2.0.0
+  __TEXT.__text: 0x127c4
   __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x204
   __TEXT.__const: 0x4d03
-  __TEXT.__cstring: 0x3e6b
+  __TEXT.__cstring: 0x3e96
   __TEXT.__oslogstring: 0x5f3
   __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__objc_methname: 0x741

   - /usr/lib/libutil.dylib
   Functions: 284
   Symbols:   416
-  CStrings:  579
+  CStrings:  580
 
Functions:
~ _read_boot_region : 1816 -> 1892
CStrings:
+ "FAT (%u sectors) too small for %u clusters"
```
