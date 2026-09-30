## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1017.0.0.0.0
-  __TEXT.__text: 0x3a170
-  __TEXT.__auth_stubs: 0xe80
+1017.2.1.0.0
+  __TEXT.__text: 0x3b378
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x5e1e1
-  __TEXT.__cstring: 0x167e
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__oslogstring: 0x470a
+  __TEXT.__cstring: 0x17e0
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__oslogstring: 0x4873
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x680
   __TEXT.__eh_frame: 0x4c
   __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methname: 0xfdf
+  __TEXT.__objc_methname: 0xff6
   __TEXT.__objc_methtype: 0x3dc
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x2770
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x2780
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x1670
+  __AUTH_CONST.__const: 0x1690
   __AUTH_CONST.__cfstring: 0x18a0
   __AUTH_CONST.__objc_const: 0x6e8
   __AUTH_CONST.__objc_intobj: 0xa8

   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x60
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x158
   __DATA_DIRTY.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 729
-  Symbols:   1617
-  CStrings:  818
+  Functions: 736
+  Symbols:   1629
+  CStrings:  849
 
Symbols:
+ _ACCUserDefaultsKey_IdentityCertIsClassD
+ _MFAADeviceIdentityInitCertStates
+ _SecAccessControlCreate
+ _SecAccessControlSetProtection
+ __storeIsClassDToDisk
+ _kCFACCUserDefaultsKey_IdentityCertIsClassD
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
- _MFAADeviceIdentityRefreshCertificate
CStrings:
+ "%!s(MISSING): !framework"
+ "%!s(MISSING): %!@(MISSING), ENTER"
+ "%!s(MISSING): %!@(MISSING), options %!@(MISSING)\n\n"
+ "%!s(MISSING): Failed to create access control! error %!@(MISSING)"
+ "%!s(MISSING): Failed to obtain valid certificates from server: %!s(MISSING)\n"
+ "%!s(MISSING): Failed to set ACL protection to %!@(MISSING)! error %!@(MISSING)"
+ "%!s(MISSING): _copyCertificateForIndex: error %!d(MISSING)\n"
+ "%!s(MISSING): _scheduleRefreshCertificates %!@(MISSING)"
+ "%!s(MISSING): call _storeRefreshStateToDisk label %!@(MISSING)"
+ "%!s(MISSING): cert:%!d(MISSING), key:%!d(MISSING)"
+ "%!s(MISSING): count %!l(MISSING)ld, gCertificateRefreshPolicy %!@(MISSING)\n"
+ "%!s(MISSING): do once"
+ "%!s(MISSING): error: %!s(MISSING)\n"
+ "%!s(MISSING): i %!d(MISSING), call _copyCertificateForIndex %!@(MISSING)"
+ "%!s(MISSING): interval:%!f(MISSING)\n"
+ "%!s(MISSING): label %!@(MISSING), requestNew %!d(MISSING), refreshPolicy %!@(MISSING)\n"
+ "%!s(MISSING): no valid certs, schedule refresh"
+ "%!s(MISSING): request cert: %!d(MISSING)\n"
+ "%!s(MISSING): success:%!d(MISSING)\n"
+ "%!s(MISSING): unexpected count %!l(MISSING)ld\n"
+ "%!s(MISSING):%!d(MISSING) %!@(MISSING), EXIT success %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) %!@(MISSING), IssueClientCertificate response took too long!!! %!f(MISSING) seconds."
+ "%!s(MISSING):%!d(MISSING) %!@(MISSING), got IssueClientCertificate response in %!f(MISSING) seconds. error %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) %!@(MISSING), requestInit %!d(MISSING), requestNew %!d(MISSING), needInitCertKeyCache %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING) index %!d(MISSING), requestNew %!d(MISSING), %!@(MISSING), error %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING) localAccessControl %!@(MISSING)"
+ "%!s(MISSING)[%!l(MISSING)u]: data: (%!z(MISSING)u bytes)\n%!{(MISSING)coreacc:bytes}.*P"
+ "%!s(MISSING)[%!l(MISSING)u]: desc: %!s(MISSING)\n\n"
+ "DeviceIdentity: %!s(MISSING): !numberedLabel\n"
+ "IdentityCertIsClassD"
+ "MFAADeviceIdentity: %!s(MISSING): gCertificateIsClassD[%!d(MISSING)]:%!d(MISSING)\n"
+ "MFAADeviceIdentity: %!s(MISSING): gCertificateRefreshState[%!d(MISSING)]:%!d(MISSING)\n"
+ "MFAADeviceIdentity: %!s(MISSING): gCertificateUseTimestamp[%!d(MISSING)]:%!f(MISSING)\n"
+ "MFAADeviceIdentity: _storeIsClassDToDisk\n"
+ "MFAADeviceIdentity: _storeIsClassDToDisk: !isClassDArray\n"
+ "MFAADeviceIdentityCopyCertificate"
+ "MFAADeviceIdentityCopyCertificate_block_invoke"
+ "MFAADeviceIdentityInitCertStates"
+ "MFAADeviceIdentityRequestCertificate"
+ "MFAADeviceIdentityRequestCertificate_block_invoke"
+ "__initMFAADeviceIdentity_block_invoke"
+ "_copyCertificateForIndex"
+ "_fetchAllCertificates"
+ "_readStateFromDisk"
+ "kMAOptionsBAAAccessControls"
+ "kMAOptionsBAASkipNetworkRequest"
+ "timeIntervalSinceDate:"
- "AllowInvalidNetworkCertificates"
- "DeviceIdentity: _copyCertificateForIndex: !numberedLabel\n"
- "DeviceIdentity: _fetchAllCertificates: MFAADeviceIdentityRequestCertificate: error\n"
- "MFAADeviceIdentityCopyCertificate: MFAADeviceIdentityRequestCertificate: unexpected count\n"
- "MFAADeviceIdentityCopyCertificate: gCertificateRefreshState[%!d(MISSING)]:%!d(MISSING)\n"
- "MFAADeviceIdentityCopyCertificate: gCertificateUseTimestamp[%!d(MISSING)]:%!f(MISSING)\n"
- "MFAADeviceIdentityCopyCertificate: interval:%!f(MISSING)\n"
- "MFAADeviceIdentityCopyCertificate: request cert: %!d(MISSING)\n"
- "MFAADeviceIdentityCopyCertificate: start\n"
- "MFAADeviceIdentityCopyCertificate: success:%!d(MISSING)\n"
- "MFAADeviceIdentityCopyCertificate:%!d(MISSING): cert:%!d(MISSING), key:%!d(MISSING)\n"
- "MFAADeviceIdentityRequestCertificate: !framework"
- "MFAADeviceIdentityRequestCertificate: Failed to obtain valid certificates from server: %!s(MISSING)\n"
- "MFAADeviceIdentityRequestCertificate: error: %!s(MISSING)\n"
- "MFAADeviceIdentityRequestCertificate[%!l(MISSING)u]: data: (%!z(MISSING)u bytes)\n%!{(MISSING)coreacc:bytes}.*P"
- "MFAADeviceIdentityRequestCertificate[%!l(MISSING)u]: desc: %!s(MISSING)\n\n"

```
