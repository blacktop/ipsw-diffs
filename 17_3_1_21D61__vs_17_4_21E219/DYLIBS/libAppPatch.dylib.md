## libAppPatch.dylib

> `/usr/lib/libAppPatch.dylib`

```diff

-1270.80.2.0.0
-  __TEXT.__text: 0x12f6c
+1270.102.7.0.0
+  __TEXT.__text: 0x13254
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x44c
-  __TEXT.__cstring: 0x55ae
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__cstring: 0x562a
   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x23a
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__unwind_info: 0x314
+  __TEXT.__unwind_info: 0x31c
   __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x15fe
-  __TEXT.__objc_methtype: 0x405
-  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methname: 0x1654
+  __TEXT.__objc_methtype: 0x3ed
+  __TEXT.__objc_stubs: 0xea0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x118
-  __DATA_CONST.__objc_selrefs: 0x4f8
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__cfstring: 0x35e0
+  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_arraydata: 0xc8
+  __AUTH_CONST.__cfstring: 0x3600
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x160
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x690
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0xa8
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x38
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 203
-  Symbols:   882
-  CStrings:  792
+  Functions: 205
+  Symbols:   886
+  CStrings:  795
 
Symbols:
+ -[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
+ -[MIFileManager removeExtendedAttributeNamed:fromURL:error:]
+ GCC_except_table3
+ GCC_except_table91
+ _MIArrayFilteredToContainOnlyClass
+ __unnamed_array_storage.341
+ _objc_msgSend$arrayWithCapacity:
- -[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:]
- GCC_except_table90
- __unnamed_array_storage.325
- __unnamed_array_storage.342
CStrings:
+ "-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]"
+ "-[MIFileManager removeExtendedAttributeNamed:fromURL:error:]"
+ "Couldn't get data from EA named %s on \"%s\": %s"
+ "Failed to remove extended attribute named %@ from %s: %s"
+ "arrayWithCapacity:"
+ "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
+ "removeExtendedAttributeNamed:fromURL:error:"
- "-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:]"
- "B48@0:8@16@24B32B36^@40"
- "Couldn't get install session UUID from EA named %s on \"%s\": %s"
- "captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:withError:"

```
