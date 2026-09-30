## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2349.0.11.0.5
-  __TEXT.__text: 0x895e4
+2349.0.31.0.2
+  __TEXT.__text: 0x896b8
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0xce20
+  __TEXT.__objc_stubs: 0xce60
   __TEXT.__objc_methlist: 0x6050
   __TEXT.__const: 0x408
-  __TEXT.__cstring: 0x19b10
-  __TEXT.__oslogstring: 0xbe87
-  __TEXT.__objc_methname: 0xee8b
+  __TEXT.__cstring: 0x19b55
+  __TEXT.__oslogstring: 0xbeb9
+  __TEXT.__objc_methname: 0xeed6
   __TEXT.__objc_classname: 0xa50
-  __TEXT.__objc_methtype: 0x2265
+  __TEXT.__objc_methtype: 0x2283
   __TEXT.__gcc_except_tab: 0x1eac
   __TEXT.__unwind_info: 0x1708
   __DATA_CONST.__auth_got: 0xc30

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0xac20
-  __DATA.__objc_selrefs: 0x4028
+  __DATA.__objc_selrefs: 0x4038
   __DATA.__objc_ivar: 0x61c
   __DATA.__objc_data: 0x2260
   __DATA.__data: 0x8d8

   - /usr/lib/libsqlite3.dylib
   Functions: 2316
   Symbols:   572
-  CStrings:  7093
+  CStrings:  7098
 
CStrings:
+ "+[MBFileOperation rename:sourceRpath:destinationBasePath:destinationBaseFD:destinationRpath:flags:error:]"
+ "B60@0:8i16@20@28i36@40i48^@52"
+ "Not restoring because this is a local restore: %!@(MISSING)"
+ "Not restoring because this is a local restore: %!@(MISSING)"
+ "relativePathsNotToBackupToLocal"
+ "relativePathsNotToRestoreFromLocal"
+ "rename:sourceRpath:destinationBasePath:destinationBaseFD:destinationRpath:flags:error:"
+ "renameatx_np() flags:0x%!x(MISSING) failure %!d(MISSING)"
- "+[MBFileOperation move:sourceRpath:destinationBasePath:destinationBaseFD:destinationRpath:error:]"
- "move:sourceRpath:destinationBasePath:destinationBaseFD:destinationRpath:error:"
- "renameatx_np() failure %!d(MISSING)"

```
