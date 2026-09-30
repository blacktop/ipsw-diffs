## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.4.0.0
-  __TEXT.__text: 0x25d24
+1598.0.6.0.0
+  __TEXT.__text: 0x25e18
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_stubs: 0x1b20
   __TEXT.__objc_methlist: 0x780
   __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x95e4
-  __TEXT.__objc_methname: 0x1c73
+  __TEXT.__cstring: 0x9661
+  __TEXT.__objc_methname: 0x1c3d
   __TEXT.__oslogstring: 0x284d
   __TEXT.__objc_classname: 0x128
   __TEXT.__objc_methtype: 0x52c
   __TEXT.__gcc_except_tab: 0x764
   __TEXT.__unwind_info: 0x5c0
   __DATA_CONST.__const: 0x7e0
-  __DATA_CONST.__cfstring: 0x1ae0
+  __DATA_CONST.__cfstring: 0x1b40
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x98
   __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x848
+  __DATA.__objc_selrefs: 0x838
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x19a0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 349
   Symbols:   310
-  CStrings:  2284
+  CStrings:  2287
 
Functions:
~ sub_100008d18 : 824 -> 996
~ sub_100012430 -> sub_1000124dc : 68076 -> 68148
CStrings:
+ "BatteryHealth"
+ "BatteryPacks"
+ "Power source %d health info:\n%@\n"
+ "Power source %u pack %u health info:\n%@\n"
+ "dictionaryWithValuesForKeys:"
+ "gcSlowInlineWritesMigration"
+ "gcSlowInlineWritesTotal"
- "Battery %d health info:\n%@\n"
- "addObjectsFromArray:"
- "dictionaryWithObjects:forKeys:"
- "objectsForKeys:notFoundMarker:"
```
