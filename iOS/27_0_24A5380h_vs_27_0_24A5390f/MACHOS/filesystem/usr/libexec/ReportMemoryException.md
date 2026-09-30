## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-360.0.0.0.0
-  __TEXT.__text: 0x93ac
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x14
+364.0.0.0.0
+  __TEXT.__text: 0x9254
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x2c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0xf4a
-  __TEXT.__const: 0xf0
-  __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methtype: 0x31
+  __TEXT.__cstring: 0xf56
+  __TEXT.__const: 0xe8
+  __TEXT.__objc_classname: 0x18
+  __TEXT.__objc_methtype: 0x4f
   __TEXT.__oslogstring: 0x1f0d
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__objc_methname: 0xb83
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_methname: 0xb72
+  __TEXT.__unwind_info: 0x178
   __DATA_CONST.__const: 0x408
   __DATA_CONST.__cfstring: 0x1220
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x150
-  __DATA.__objc_const: 0x90
+  __DATA.__objc_const: 0x168
   __DATA.__objc_selrefs: 0x410
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0xa0
   __DATA.__data: 0x2a8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 63
-  Symbols:   488
-  CStrings:  406
+  Functions: 64
+  Symbols:   499
+  CStrings:  412
 
Symbols:
+ -[RMELogPath .cxx_destruct]
+ OBJC_IVAR_$_RMELogPath._fileCreationDate
+ OBJC_IVAR_$_RMELogPath._filePath
+ _OBJC_CLASS_$_RMELogPath
+ _OBJC_METACLASS_$_RMELogPath
+ _RMEGetTimeOrderedLogPaths
+ __OBJC_$_INSTANCE_METHODS_RMELogPath
+ __OBJC_$_INSTANCE_VARIABLES_RMELogPath
+ __OBJC_CLASS_RO_$_RMELogPath
+ __OBJC_METACLASS_RO_$_RMELogPath
+ ___RMEGetTimeOrderedLogPaths_block_invoke
+ ___block_descriptor_32_e35_q24?0"RMELogPath"8"RMELogPath"16l
+ _objc_getProperty
+ _objc_msgSendSuper2
+ _objc_retain_x28
+ _objc_storeStrong
- _RMEGetTimeOrderedLogPathsMatchingPrefs
- ___RMEGetTimeOrderedLogPathsMatchingPrefs_block_invoke
- ___block_descriptor_32_e25_q24?0"NSURL"8"NSURL"16l
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$keysSortedByValueUsingComparator:
CStrings:
+ ".cxx_destruct"
+ "@\"NSDate\""
+ "@\"NSString\""
+ "RMELogPath"
+ "_fileCreationDate"
+ "_filePath"
+ "init"
+ "q24@?0@\"RMELogPath\"8@\"RMELogPath\"16"
+ "v16@0:8"
- "dateWithTimeIntervalSinceNow:"
- "keysSortedByValueUsingComparator:"
- "q24@?0@\"NSURL\"8@\"NSURL\"16"
```
