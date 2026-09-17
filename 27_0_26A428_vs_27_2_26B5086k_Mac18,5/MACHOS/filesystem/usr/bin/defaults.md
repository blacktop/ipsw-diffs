## defaults

> `/usr/bin/defaults`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-5027.0.69.0.0
-  __TEXT.__text: 0x3238
-  __TEXT.__auth_stubs: 0x570
+5027.1.2.0.0
+  __TEXT.__text: 0x3240
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_stubs: 0x760
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x20

   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xe0
   __DATA.__objc_selrefs: 0x1e0
   __DATA.__data: 0x8

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 44
-  Symbols:   232
+  Symbols:   233
   CStrings:  188
 
Symbols:
+ __CFPreferencesSetPathErrorsAreFatal
Functions:
~ _main : 2520 -> 2528
```
