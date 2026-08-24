## PackageKit

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit`

```diff

-1524.0.0.0.0
-  __TEXT.__text: 0x8be40
-  __TEXT.__objc_methlist: 0x7b4c
+1525.0.1.0.0
+  __TEXT.__text: 0x8bc6c
+  __TEXT.__objc_methlist: 0x7b34
   __TEXT.__const: 0x390
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_typeref: 0x7c
   __TEXT.__swift5_reflstr: 0x21
   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x12902
-  __TEXT.__gcc_except_tab: 0x1574
+  __TEXT.__cstring: 0x128f4
+  __TEXT.__gcc_except_tab: 0x1560
   __TEXT.__oslogstring: 0x39
   __TEXT.__dof_PackageKi: 0x1ba4
-  __TEXT.__unwind_info: 0x2108
+  __TEXT.__unwind_info: 0x2110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x46a0
+  __DATA_CONST.__objc_selrefs: 0x4680
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x68

   __AUTH_CONST.__objc_const: 0xc328
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x10c8
+  __AUTH_CONST.__auth_got: 0x10d8
   __AUTH.__objc_data: 0x13d0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xa18

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2887
-  Symbols:   7586
+  Functions: 2886
+  Symbols:   7583
   CStrings:  2155
 
Symbols:
+ _PKSIPWriteDataSafely
+ ___snprintf_chk
+ _fsync
+ _renameatx_np
+ _xar_get_safe_path
- +[PKInstallHistory _errorWithCode:posixErrno:]
- -[PKInstallHistory _renameInstallHistoryAtDir:fileName:returningError:]
- _fcopyfile
- _objc_msgSend$_errorWithCode:posixErrno:
- _objc_msgSend$_renameInstallHistoryAtDir:fileName:returningError:
- _objc_msgSend$synchronizeAndReturnError:
- _objc_msgSend$writeData:error:
- _xar_get_path
CStrings:
+ ".%s.XXXXXX"
+ "PackageKit: Could not write locked-apps state to %s (%s)"
+ "Successfully wrote install history to %s"
- "Failed to cleanup temporary InstallHistory file at %s/%s"
- "InstallHistory-XXXXXX"
- "Successfully wrote install history to %s/%s"
```
