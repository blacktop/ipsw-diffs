## uarphidd

> `/usr/libexec/uarphidd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.60.11.0.0
-  __TEXT.__text: 0x5ab4
+1587.60.14.0.0
+  __TEXT.__text: 0x5b64
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_stubs: 0xdc0
   __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x9c
   __TEXT.__cstring: 0x846
-  __TEXT.__objc_methname: 0xf00
-  __TEXT.__oslogstring: 0x96c
+  __TEXT.__objc_methname: 0xf19
+  __TEXT.__oslogstring: 0x9ca
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x26a
   __TEXT.__unwind_info: 0x268

   __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xc0
   __DATA.__objc_const: 0xa08
-  __DATA.__objc_selrefs: 0x420
+  __DATA.__objc_selrefs: 0x428
   __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180

   - /usr/lib/libobjc.A.dylib
   Functions: 157
   Symbols:   126
-  CStrings:  392
+  CStrings:  394
 
Functions:
~ sub_1000026b8 : 256 -> 432
CStrings:
+ "%s: %@; activeFirmwareVersion = %@, availableFirmwareVersion = %@, stagedFirmwareVersion = %@"
+ "availableFirmwareVersion"
```
