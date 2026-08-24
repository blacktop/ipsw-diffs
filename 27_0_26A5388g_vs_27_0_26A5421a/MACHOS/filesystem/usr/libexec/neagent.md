## neagent

> `/usr/libexec/neagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2331.0.0.0.1
-  __TEXT.__text: 0x1ddc8
+2340.1.2.0.0
+  __TEXT.__text: 0x1dedc
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x2620
   __TEXT.__objc_methlist: 0x1320
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x6c0
   __TEXT.__objc_methname: 0x2e42
-  __TEXT.__oslogstring: 0x4111
+  __TEXT.__oslogstring: 0x414d
   __TEXT.__cstring: 0x1975
   __TEXT.__objc_classname: 0x365
   __TEXT.__objc_methtype: 0x1019

   - /usr/lib/libobjc.A.dylib
   Functions: 415
   Symbols:   203
-  CStrings:  1209
+  CStrings:  1210
 
Functions:
~ sub_10000e864 : 964 -> 1064
~ sub_10001bf3c -> sub_10001bfa0 : 2540 -> 2716
CStrings:
+ "%@: %s - Filter not started, skipping reporting timer setup"
```
