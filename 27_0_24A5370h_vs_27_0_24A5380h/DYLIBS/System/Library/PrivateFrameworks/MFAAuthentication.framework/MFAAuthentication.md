## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-  __TEXT.__text: 0x4263c
+  __TEXT.__text: 0x429ac
   __TEXT.__objc_methlist: 0x494
   __TEXT.__const: 0x69773
-  __TEXT.__cstring: 0x1aa8
+  __TEXT.__cstring: 0x1adc
   __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__oslogstring: 0x4d7c
+  __TEXT.__oslogstring: 0x4e24
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x7d8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5278
+  __DATA_CONST.__const: 0x5298
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x1c30
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x1b80
   __AUTH_CONST.__objc_const: 0x648
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x208
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 850
-  Symbols:   3316
-  CStrings:  934
+  Functions: 853
+  Symbols:   3326
+  CStrings:  941
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[MFAACertificateManager createVeridianNonce:withChallenge:]
+ _ACCUserDefaultsKey_EnableManager2ForTransport
+ _ACCUserDefaultsKey_OverrideMPPAuthSupported
+ _CFErrorGetCode
+ _SecTrustGetTrustResult
+ _kCFACCUserDefaultsKey_EnableManager2ForTransport
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
- -[MFAACertificateManager createNoAuthICNonce:withChallenge:]
- _SecTrustEvaluate
- _kIOMainPortDefault
CStrings:
+ "EnableManager2ForTransport"
+ "MFAADeviceIdentity: _findValidIndex: Failed to create date objects\n"
+ "OverrideMPPAuthSupported"
+ "SecTrustEvaluateWithError failed: %@"
+ "SecTrustEvaluateWithError failed: %@\n"
+ "SecTrustGetTrustResult failed: %d"
+ "SecTrustGetTrustResult failed: %d\n"
+ "validateCertificateChain: SecTrustEvaluateWithError failed: %@\n"
+ "validateCertificateChain: SecTrustGetTrustResult failed: %d\n"
- "SecTrustEvaluate failed osStatus:%02X\n"
- "SecTrustSetAnchorCertificates fail osStatus:%02X\n"
- "trustError: %@"
- "validateCertificateChain: SecTrustEvaluate failed osStatus:%02X\n"

```
