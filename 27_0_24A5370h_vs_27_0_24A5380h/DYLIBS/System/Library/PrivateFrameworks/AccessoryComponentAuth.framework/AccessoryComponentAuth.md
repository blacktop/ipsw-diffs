## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

-  __TEXT.__text: 0x12380
-  __TEXT.__objc_methlist: 0x4cc
-  __TEXT.__const: 0xd710
-  __TEXT.__cstring: 0x14e6
-  __TEXT.__oslogstring: 0x11f1
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__text: 0x1240c
+  __TEXT.__objc_methlist: 0x4e4
+  __TEXT.__const: 0xd700
+  __TEXT.__cstring: 0x14b6
+  __TEXT.__oslogstring: 0x11d7
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1620
+  __DATA_CONST.__const: 0x1640
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0xc48
-  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__cfstring: 0x1420
   __AUTH_CONST.__objc_const: 0x6d0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 475
-  Symbols:   2264
-  CStrings:  496
+  Functions: 479
+  Symbols:   2277
+  CStrings:  499
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[ACCHWComponentAuthService _signChallengeForModuleType:challenge:componentIndex:completionHandler:]
+ -[ACCHWComponentAuthServiceParams dealloc]
+ GCC_except_table67
+ _ACCUserDefaultsKey_EnableManager2ForTransport
+ _ACCUserDefaultsKey_OverrideMPPAuthSupported
+ _kCFACCUserDefaultsKey_EnableManager2ForTransport
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
+ _objc_msgSend$_signChallengeForModuleType:challenge:componentIndex:completionHandler:
+ _objc_msgSend$createVeridianNonce:withChallenge:
+ _objc_msgSendSuper2
+ _objc_retain_x3
- GCC_except_table66
- _objc_msgSend$createNoAuthICNonce:withChallenge:
CStrings:
+ "ERROR No auth io_service_t is found!"
+ "EnableManager2ForTransport"
+ "IDSN length %zu exceeds buffer"
+ "OverrideMPPAuthSupported"
+ "_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d"
+ "cpClearCertificate failed: 0x%x"
- "###ELEE###: %s:%d: idsnStringRef: %@"
- "###ELEE###: %s:%d: test multiInstanceDataArray: %@"
- "-[ACCHWComponentAuthService _findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:]"
- "ERROR No batteryAuth io_service_t is found!"
- "signVeridianChallenge Replying with signature=%@, deviceNonce=%@, authError = %d"

```
