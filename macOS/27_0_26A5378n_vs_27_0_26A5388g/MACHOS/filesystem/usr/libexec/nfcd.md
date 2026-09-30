## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-370.38.2.0.0
-  __TEXT.__text: 0x170f08
+370.40.2.0.0
+  __TEXT.__text: 0x1710b8
   __TEXT.__auth_stubs: 0x13f0
   __TEXT.__delay_helper: 0x1f4
   __TEXT.__objc_stubs: 0x9ee0
-  __TEXT.__objc_methlist: 0x7598
+  __TEXT.__objc_methlist: 0x75c8
   __TEXT.__const: 0x10cc
-  __TEXT.__cstring: 0x18769
+  __TEXT.__cstring: 0x18777
   __TEXT.__oslogstring: 0x18567
   __TEXT.__objc_classname: 0x14f5
-  __TEXT.__objc_methname: 0x10a14
-  __TEXT.__objc_methtype: 0x3d9e
+  __TEXT.__objc_methname: 0x10a44
+  __TEXT.__objc_methtype: 0x3dbf
   __TEXT.__unwind_info: 0x1e58
   __DATA_CONST.__const: 0x6d70
   __DATA_CONST.__cfstring: 0xe920

   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__auth_got: 0xa00
   __DATA_CONST.__got: 0x708
-  __DATA.__objc_const: 0x100e0
-  __DATA.__objc_selrefs: 0x3a68
-  __DATA.__objc_ivar: 0xcf8
+  __DATA.__objc_const: 0x10120
+  __DATA.__objc_selrefs: 0x3a78
+  __DATA.__objc_ivar: 0xcfc
   __DATA.__objc_data: 0x3020
   __DATA.__data: 0x1df4
   __DATA.__bss: 0x200

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3115
+  Functions: 3118
   Symbols:   509
-  CStrings:  8788
+  CStrings:  8791
 
CStrings:
+ "%@ { applet=%@ endpoint=%@ didError=%@ result=%@ brandCode=%@ background=%@ }"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "NFCD built from (B&I) Stockholm_Base-370.40.2"
+ "Vv24@0:8@?<v@?@\"NSDictionary\">16"
+ "currentDeviceCAParametersWithCompletion:"
+ "endSessionWithReason:completion:"
+ "localDeviceCAParameters"
- "%@ { applet=%@ endpoint=%@ didError=%@ result=%@ brandCode=%@ }"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "NFCD built from (B&I) Stockholm_Base-370.38.2"
- "unarchivedArrayOfObjectsOfClasses:fromData:error:"
```
