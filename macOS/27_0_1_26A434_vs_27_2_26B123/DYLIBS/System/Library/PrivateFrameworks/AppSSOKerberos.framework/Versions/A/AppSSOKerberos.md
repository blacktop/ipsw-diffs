## AppSSOKerberos

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/Versions/A/AppSSOKerberos`

```diff

-643.1.2.0.0
-  __TEXT.__text: 0x2d9ec
-  __TEXT.__objc_methlist: 0x2298
+643.40.34.0.0
+  __TEXT.__text: 0x2e720
+  __TEXT.__objc_methlist: 0x22f8
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x285a
-  __TEXT.__oslogstring: 0x3b8f
+  __TEXT.__cstring: 0x28d7
+  __TEXT.__oslogstring: 0x3c8a
   __TEXT.__gcc_except_tab: 0xa70
   __TEXT.__dlopen_cstrs: 0xcb
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1888
+  __DATA_CONST.__objc_selrefs: 0x18d8
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
+  Functions: 1284
+  Symbols:   2445
+  CStrings:  736
 
Symbols:
+ +[SOKerberosAuthentication updateADPasswordHighWaterMark:]
+ +[SOKerberosExtensionData(MenuExtra) menuExtraProfileFromProfiles:]
+ +[SOKerberosExtensionData(MenuExtra) menuExtraRankForProfile:]
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
+ __OBJC_$_CLASS_METHODS_SOKerberosExtensionData(MenuExtra)
+ ___67+[SOKerberosExtensionData(MenuExtra) menuExtraProfileFromProfiles:]_block_invoke
+ ___block_descriptor_40_e41_q24?0"SOFullProfile"8"SOFullProfile"16l
+ _objc_msgSend$compare:
+ _objc_msgSend$dateADPasswordCanChange
+ _objc_msgSend$dateADPasswordLastChangedHighWaterMark
+ _objc_msgSend$menuExtraRankForProfile:
+ _objc_msgSend$setDateADPasswordLastChangedHighWaterMark:
+ _objc_msgSend$setUserPrincipalNameForADPasswordHighWaterMark:
+ _objc_msgSend$sortedArrayWithOptions:usingComparator:
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
+ "q24@?0@\"SOFullProfile\"8@\"SOFullProfile\"16"
+ "userPrincipalNameForADPasswordHighWaterMark"
```
