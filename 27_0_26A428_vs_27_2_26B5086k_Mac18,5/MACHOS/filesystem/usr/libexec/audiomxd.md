## audiomxd

> `/usr/libexec/audiomxd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1638.104.3.0.0
-  __TEXT.__text: 0x12c80
+1638.208.0.0.0
+  __TEXT.__text: 0x12de8
   __TEXT.__realtime: 0x8e4
   __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x10ec
+  __TEXT.__gcc_except_tab: 0x1120
   __TEXT.__cstring: 0xbbd
-  __TEXT.__oslogstring: 0x32cb
+  __TEXT.__oslogstring: 0x3340
   __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x4e
-  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__unwind_info: 0x6b0
   __DATA_CONST.__const: 0x638
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 232
   Symbols:   238
-  CStrings:  353
+  CStrings:  355
 
Functions:
~ sub_1000081d4 : 2980 -> 3280
~ sub_10000fee4 -> sub_100010010 : 2016 -> 2076
CStrings:
+ "%25s:%-5d Could not successfully allocate magic cookie buffer"
+ "%25s:%-5d Could not successfully allocate packet table"
```
