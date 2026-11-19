## FileVault2

> `/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/FileVault2.profileDomainPlugin/Contents/MacOS/FileVault2`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1842.1.1.0.0
-  __TEXT.__text: 0x6054
+1847.40.6.0.0
+  __TEXT.__text: 0x61c8
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0xb00
+  __TEXT.__objc_stubs: 0xb40
   __TEXT.__objc_methlist: 0xa4
-  __TEXT.__cstring: 0x2805
+  __TEXT.__cstring: 0x287f
   __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x1094
+  __TEXT.__oslogstring: 0x110e
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__objc_methname: 0x97f
+  __TEXT.__objc_methname: 0x9d8
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methtype: 0xbc
   __TEXT.__unwind_info: 0x1f8

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_selrefs: 0x318
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8
   __DATA.__common: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 100
-  Symbols:   156
-  CStrings:  399
+  Symbols:   159
+  CStrings:  402
 
Symbols:
+ _NSFileGroupOwnerAccountID
+ _NSFileOwnerAccountID
+ _NSFilePosixPermissions
Functions:
~ sub_56ac : 3160 -> 3532
CStrings:
+ "FileVault2Plugin.enableFDESetup unable to create fdesetup output parent '%s' (%s) - aborting to avoid a lost recovery key"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "localizedDescription"
```
