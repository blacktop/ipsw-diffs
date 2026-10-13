## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4838.40.130.0.2
-  __TEXT.__text: 0x12940c
-  __TEXT.__objc_methlist: 0xeaa4
+4838.42.2.0.0
+  __TEXT.__text: 0x12949c
+  __TEXT.__objc_methlist: 0xeabc
   __TEXT.__const: 0x88a
-  __TEXT.__cstring: 0x14f9f
+  __TEXT.__cstring: 0x15005
   __TEXT.__gcc_except_tab: 0x8b64
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
-  __TEXT.__ustring: 0x25a
+  __TEXT.__ustring: 0x288
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x45

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x62a0
+  __DATA_CONST.__const: 0x62a8
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7150
+  __DATA_CONST.__objc_selrefs: 0x7160
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb20
   __AUTH_CONST.__const: 0x1dc8
-  __AUTH_CONST.__cfstring: 0x116c0
-  __AUTH_CONST.__objc_const: 0x250f8
+  __AUTH_CONST.__cfstring: 0x11720
+  __AUTH_CONST.__objc_const: 0x25128
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_data: 0x1a90
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10d4
+  __DATA.__objc_ivar: 0x10d8
   __DATA.__data: 0x23f0
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x2760

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7488
-  Symbols:   11246
-  CStrings:  4071
+  Functions: 7491
+  Symbols:   11249
+  CStrings:  4076
 
Symbols:
+ -[FPProviderDomain owningApplicationIsInstallationHeld]
+ -[FPProviderDomain setOwningApplicationIsInstallationHeld:]
+ _OBJC_IVAR_$_FPProviderDomain._owningApplicationIsInstallationHeld
Functions:
~ -[FPProviderDomain encodeWithCoder:] : 936 -> 956
~ -[FPProviderDomain initWithCoder:] : 1448 -> 1468
~ -[FPProviderDomain description] : 1512 -> 1548
~ -[FPProviderDomain isHidden] : 76 -> 88
+ sub_1a8fbfa6c
~ -[FPProviderDomain localizedDisconnectionBannerText] : 432 -> 416
- -[FPProviderDomain setSupportedSearchFilters:]
+ -[FPProviderDomain setSupportedSearchFilters:]
- -[FPProviderDomain setDomainUserInfo:]
+ -[FPProviderDomain setDomainUserInfo:]
- -[FPProviderDomain setProgress:]
+ -[FPProviderDomain progress]
+ -[FPProviderDomain setDomain:]
+ -[FPProviderDomain purposeIdentifier]
~ _FPConnectionStateToPrettyString : 272 -> 284
CStrings:
+ "(⏹  installation held)"
+ ",appHeld"
+ ",installationHeld"
+ "4838.42.2"
+ "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
+ "DISCONNECTION_REASON_INSTALLATION_HELD_%@"
+ "_owningApplicationIsInstallationHeld"
- "4838.40.130.0.2"
- "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
```
