## aidearlyboot

> `/usr/libexec/aidearlyboot`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-10100.41.0.0.0
-  __TEXT.__text: 0xa1e4
+10110.1.0.0.0
+  __TEXT.__text: 0xa250
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0xb40
   __TEXT.__objc_methlist: 0x32c
-  __TEXT.__cstring: 0xee5
+  __TEXT.__cstring: 0xf1d
   __TEXT.__const: 0xd672
-  __TEXT.__objc_methname: 0xab1
+  __TEXT.__objc_methname: 0xabd
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methtype: 0x220
+  __TEXT.__objc_methtype: 0x21f
   __TEXT.__unwind_info: 0x460
   __DATA_CONST.__const: 0x1840
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 287
   Symbols:   135
-  CStrings:  295
+  CStrings:  296
 
Symbols:
+ _CFErrorCopyDescription
+ _objc_retain_x25
- _objc_autorelease
- _objc_retain_x23
Functions:
~ sub_100002afc : 976 -> 952
~ sub_100002efc -> sub_100002ee4 : 1192 -> 1324
CStrings:
+ "%s: failed to retrieve localData for key (%@) dataInstance (%@) error (%@)"
+ "%s: failed to retrieve localDict for key (%@) dataInstance (%@) error (%@)"
+ "-[AIDFirmwareUpdateController extractFDRDataWithClassKey:usesMultiInstance:]"
+ "@28@0:8@16B24"
+ "Error finding FDR data collection for class '%@'"
+ "extractFDRDataWithClassKey:usesMultiInstance:"
+ "nil"
- "%s: localData is NULL for key (%@) dataInstance (%@)"
- "%s: localDict is NULL for key (%@) dataInstance (%@)"
- "-[AIDFirmwareUpdateController extractFDRDataWithClassKey:error:]"
- "@32@0:8@16^@24"
- "Error finding FDR data collection for class '%@': %@"
- "extractFDRDataWithClassKey:error:"
```
