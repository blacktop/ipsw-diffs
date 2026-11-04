## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

 3696.40.14.0.1
-  __TEXT.__text: 0xee08c
+  __TEXT.__text: 0xee0ec
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__cstring: 0x2bd87
+  __TEXT.__cstring: 0x2bdaa
   __TEXT.__const: 0x79130
   __TEXT.__gcc_except_tab: 0xb6c
   __TEXT.__oslogstring: 0xb92

   __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x20b8
-  __AUTH_CONST.__cfstring: 0xc400
+  __AUTH_CONST.__cfstring: 0xc440
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
   Functions: 2870
   Symbols:   1894
-  CStrings:  6377
+  CStrings:  6379
 
Functions:
~ _persistent_hardware_files_create : 1308 -> 1372
~ sub_adb40 -> sub_adb80 : 2856 -> 2880
~ sub_d3328 -> sub_d3380 : 632 -> 640
CStrings:
+ "%@/tbics_gain_map"
+ "%@/tbics_history"
```
