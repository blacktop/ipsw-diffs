## PackageKit

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit`

```diff

-1491.160.2.700.1
-  __TEXT.__text: 0x87148
-  __TEXT.__auth_stubs: 0x2120
-  __TEXT.__objc_methlist: 0x785c
+1491.160.2.701.2
+  __TEXT.__text: 0x86f18
+  __TEXT.__auth_stubs: 0x2140
+  __TEXT.__objc_methlist: 0x7844
   __TEXT.__const: 0x380
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_typeref: 0x7c
   __TEXT.__swift5_reflstr: 0x21
   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x11c2d
-  __TEXT.__gcc_except_tab: 0x14cc
+  __TEXT.__cstring: 0x11c1f
+  __TEXT.__gcc_except_tab: 0x146c
   __TEXT.__oslogstring: 0x19
   __TEXT.__dof_PackageKi: 0x1ba4
-  __TEXT.__unwind_info: 0x20a8
+  __TEXT.__unwind_info: 0x2098
   __TEXT.__objc_classname: 0x1098
-  __TEXT.__objc_methname: 0x11f08
-  __TEXT.__objc_methtype: 0x257a
-  __TEXT.__objc_stubs: 0xe020
-  __DATA_CONST.__got: 0x998
+  __TEXT.__objc_methname: 0x11e8d
+  __TEXT.__objc_methtype: 0x2559
+  __TEXT.__objc_stubs: 0xdfa0
+  __DATA_CONST.__got: 0x9a8
   __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4578
+  __DATA_CONST.__objc_selrefs: 0x4558
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x10a0
+  __AUTH_CONST.__auth_got: 0x10b0
   __AUTH_CONST.__const: 0x17a0
   __AUTH_CONST.__cfstring: 0xb760
   __AUTH_CONST.__objc_const: 0xbc00

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2809
-  Symbols:   7403
-  CStrings:  5435
+  Functions: 2808
+  Symbols:   7402
+  CStrings:  5429
 
Symbols:
+ _PKSIPWriteDataSafely
+ _SANDBOX_STORAGE_CLASS_GROUP_ANY
+ _SANDBOX_STORAGE_CLASS_PROPERTY_WRITE_RESTRICTED
+ ___snprintf_chk
+ _fsync
+ _renameatx_np
+ _sandbox_check_storage_class
- +[PKInstallHistory _errorWithCode:posixErrno:]
- -[PKInstallHistory _renameInstallHistoryAtDir:fileName:returningError:]
- _fcopyfile
- _objc_msgSend$_errorWithCode:posixErrno:
- _objc_msgSend$_renameInstallHistoryAtDir:fileName:returningError:
- _objc_msgSend$synchronizeAndReturnError:
- _objc_msgSend$writeData:error:
- _renameat
CStrings:
+ ".%s.XXXXXX"
+ "PackageKit: Could not write locked-apps state to %s (%s)"
+ "Successfully wrote install history to %s"
- "@28@0:8q16i24"
- "B36@0:8i16*20o^@28"
- "Failed to cleanup temporary InstallHistory file at %s/%s"
- "InstallHistory-XXXXXX"
- "Successfully wrote install history to %s/%s"
- "_errorWithCode:posixErrno:"
- "_renameInstallHistoryAtDir:fileName:returningError:"
- "synchronizeAndReturnError:"
- "writeData:error:"
```
