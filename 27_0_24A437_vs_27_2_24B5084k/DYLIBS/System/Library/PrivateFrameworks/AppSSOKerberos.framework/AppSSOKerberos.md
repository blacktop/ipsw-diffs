## AppSSOKerberos

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos`

```diff

-643.0.47.0.0
-  __TEXT.__text: 0x1f9a8
-  __TEXT.__objc_methlist: 0x1e74
+643.40.23.0.0
+  __TEXT.__text: 0x20174
+  __TEXT.__objc_methlist: 0x1eb4
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x1ac0
-  __TEXT.__oslogstring: 0x283b
-  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__cstring: 0x1b13
+  __TEXT.__oslogstring: 0x28dd
+  __TEXT.__gcc_except_tab: 0x824
   __TEXT.__dlopen_cstrs: 0x63
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__unwind_info: 0xc60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a8
+  __DATA_CONST.__objc_selrefs: 0x14d8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x3c0
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x34d0
+  __AUTH_CONST.__cfstring: 0x1840
+  __AUTH_CONST.__objc_const: 0x34f0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1010
-  Symbols:   1969
-  CStrings:  554
+  Functions: 1018
+  Symbols:   1984
+  CStrings:  558
 
Symbols:
+ +[SOKerberosAuthentication updateADPasswordHighWaterMark:]
+ -[SOKerberosRealmSettings dateADPasswordLastChangedHighWaterMark]
+ -[SOKerberosRealmSettings setDateADPasswordLastChangedHighWaterMark:]
+ -[SOKerberosRealmSettings setUserPrincipalNameForADPasswordHighWaterMark:]
+ -[SOKerberosRealmSettings userPrincipalNameForADPasswordHighWaterMark]
+ GCC_except_table21
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table69
+ _objc_msgSend$compare:
+ _objc_msgSend$dateADPasswordCanChange
+ _objc_msgSend$dateADPasswordLastChangedHighWaterMark
+ _objc_msgSend$dateADPasswordLastChangedWhenSynced
+ _objc_msgSend$dateLocalPasswordLastChangedWhenSynced
+ _objc_msgSend$setDateADPasswordLastChangedHighWaterMark:
+ _objc_msgSend$setDateADPasswordLastChangedWhenSynced:
+ _objc_msgSend$setDateLocalPasswordLastChangedWhenSynced:
+ _objc_msgSend$setUserPrincipalNameForADPasswordHighWaterMark:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updateADPasswordHighWaterMark:
+ _objc_msgSend$userPrincipalNameForADPasswordHighWaterMark
- GCC_except_table15
- GCC_except_table20
- GCC_except_table58
- GCC_except_table59
- GCC_except_table60
- GCC_except_table61
- _objc_msgSend$isEqualToDate:
CStrings:
+ "AD password high water mark: %@ -> %@"
+ "Ignoring stale AD password data: KDC returned passwordLastSet %@ which is older than the newest value seen for this user %@"
+ "dateADPasswordLastChangedHighWaterMark"
+ "userPrincipalNameForADPasswordHighWaterMark"
```
