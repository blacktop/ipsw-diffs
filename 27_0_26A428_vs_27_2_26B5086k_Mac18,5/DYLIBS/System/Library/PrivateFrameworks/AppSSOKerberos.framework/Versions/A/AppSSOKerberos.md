## AppSSOKerberos

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/Versions/A/AppSSOKerberos`

```diff

-643.1.1.0.0
-  __TEXT.__text: 0x2cf48
-  __TEXT.__objc_methlist: 0x2298
+643.40.23.0.0
+  __TEXT.__text: 0x2d96c
+  __TEXT.__objc_methlist: 0x22d8
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x285a
-  __TEXT.__oslogstring: 0x3b8f
+  __TEXT.__cstring: 0x28ad
+  __TEXT.__oslogstring: 0x3c8a
   __TEXT.__gcc_except_tab: 0xa70
   __TEXT.__dlopen_cstrs: 0xcb
-  __TEXT.__unwind_info: 0x1050
+  __TEXT.__unwind_info: 0x1070
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1888
+  __DATA_CONST.__objc_selrefs: 0x18c0
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0xab0
-  __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x3cb0
+  __AUTH_CONST.__cfstring: 0x1c00
+  __AUTH_CONST.__objc_const: 0x3cd0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1272
-  Symbols:   2423
-  CStrings:  730
+  Functions: 1281
+  Symbols:   2438
+  CStrings:  735
 
Symbols:
+ +[SOKerberosAuthentication updateADPasswordHighWaterMark:]
+ -[SOKerberosRealmSettings dateADPasswordLastChangedHighWaterMark]
+ -[SOKerberosRealmSettings setDateADPasswordLastChangedHighWaterMark:]
+ -[SOKerberosRealmSettings setUserPrincipalNameForADPasswordHighWaterMark:]
+ -[SOKerberosRealmSettings userPrincipalNameForADPasswordHighWaterMark]
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table71
+ _objc_msgSend$compare:
+ _objc_msgSend$dateADPasswordCanChange
+ _objc_msgSend$dateADPasswordLastChangedHighWaterMark
+ _objc_msgSend$setDateADPasswordLastChangedHighWaterMark:
+ _objc_msgSend$setUserPrincipalNameForADPasswordHighWaterMark:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updateADPasswordHighWaterMark:
+ _objc_msgSend$userPrincipalNameForADPasswordHighWaterMark
- GCC_except_table25
- GCC_except_table58
- GCC_except_table59
- GCC_except_table65
CStrings:
+ "AD password high water mark: %@ -> %@"
+ "Ignoring stale AD password data: KDC returned passwordLastSet %@ which is older than the newest value seen for this user %@"
+ "Using AD password high water mark %@ as the sync baseline instead of the stored value %@"
+ "dateADPasswordLastChangedHighWaterMark"
+ "userPrincipalNameForADPasswordHighWaterMark"
```
