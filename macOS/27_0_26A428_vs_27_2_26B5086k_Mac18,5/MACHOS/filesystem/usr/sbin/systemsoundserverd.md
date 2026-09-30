## systemsoundserverd

> `/usr/sbin/systemsoundserverd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1638.104.3.0.0
-  __TEXT.__text: 0x12750
+1638.208.0.0.0
+  __TEXT.__text: 0x128b8
   __TEXT.__realtime: 0x8e4
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x1064
+  __TEXT.__gcc_except_tab: 0x1098
   __TEXT.__cstring: 0xb6a
-  __TEXT.__oslogstring: 0x319b
+  __TEXT.__oslogstring: 0x3210
   __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x32
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__unwind_info: 0x6b8
   __DATA_CONST.__const: 0x638
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 233
   Symbols:   224
-  CStrings:  335
+  CStrings:  337
 
Functions:
~ sub_100007b14 : 2980 -> 3280
~ sub_10000fb1c -> sub_10000fc48 : 2016 -> 2076
CStrings:
+ "%25s:%-5d Could not successfully allocate magic cookie buffer"
+ "%25s:%-5d Could not successfully allocate packet table"
```
