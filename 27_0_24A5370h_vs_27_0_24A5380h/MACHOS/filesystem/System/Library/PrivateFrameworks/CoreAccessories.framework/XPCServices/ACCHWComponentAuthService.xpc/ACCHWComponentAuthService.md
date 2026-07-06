## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-  __TEXT.__text: 0x38310
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x604
+  __TEXT.__text: 0x3958c
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x61c
   __TEXT.__const: 0x19b63
-  __TEXT.__cstring: 0x1f6d
+  __TEXT.__cstring: 0x1f3d
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x1626
-  __TEXT.__objc_methtype: 0x5f2
-  __TEXT.__oslogstring: 0x62e8
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__unwind_info: 0x7f8
-  __DATA_CONST.__const: 0x64f8
-  __DATA_CONST.__cfstring: 0x1620
+  __TEXT.__objc_methname: 0x1676
+  __TEXT.__objc_methtype: 0x607
+  __TEXT.__oslogstring: 0x6675
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__unwind_info: 0x818
+  __DATA_CONST.__const: 0x6518
+  __DATA_CONST.__cfstring: 0x1660
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x710
+  __DATA_CONST.__auth_got: 0x720
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0xa70
-  __DATA.__objc_selrefs: 0x598
+  __DATA.__objc_selrefs: 0x5a8
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1204
-  Symbols:   7979
-  CStrings:  1392
+  Functions: 1216
+  Symbols:   8065
+  CStrings:  1420
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[ACCHWComponentAuthService _signChallengeForModuleType:challenge:componentIndex:completionHandler:]
+ -[ACCHWComponentAuthServiceParams dealloc]
+ GCC_except_table67
+ _ACCUserDefaultsKey_EnableManager2ForTransport
+ _ACCUserDefaultsKey_OverrideMPPAuthSupported
+ _CFDataCreateWithBytesNoCopy
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _kCFACCUserDefaultsKey_EnableManager2ForTransport
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
+ _objc_msgSend$_signChallengeForModuleType:challenge:componentIndex:completionHandler:
+ _objc_msgSend$createVeridianNonce:withChallenge:
+ _objc_msgSendSuper2
- GCC_except_table66
- _objc_msgSend$createNoAuthICNonce:withChallenge:
CStrings:
+ "ERROR No auth io_service_t is found!"
+ "EnableManager2ForTransport"
+ "IDSN length %zu exceeds buffer"
+ "NVMReadResponse: paramID %d exceeds maximum expected value"
+ "OverrideMPPAuthSupported"
+ "UserPublicKey %@"
+ "_replyGetNVMKey: !dictionary"
+ "_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d"
+ "_signChallengeForModuleType:challenge:componentIndex:completionHandler:"
+ "copyUserPrivateKey: error:%d"
+ "cpClearCertificate failed: 0x%x"
+ "createVeridianNonce:withChallenge:"
+ "dealloc"
+ "handle_NVMAuthFinish: paramID %d exceeds maximum expected value"
+ "handle_NVMAuthStart: !serialNumberString"
+ "handle_NVMAuthStart: !userKey"
+ "handle_NVMAuthStart: !userPublicKey"
+ "handle_NVMAuthStart: U_c0: %@"
+ "handle_NVMAuthStart: U_sig: %@"
+ "handle_NVMAuthStart: ccsigma_seal error"
+ "handle_NVMAuthStart: ccsigma_sign: error"
+ "handle_NVMAuthStart: initMessage_RequestNVMAuthFinish error"
+ "handle_NVMAuthStart: paramID %d exceeds maximum expected value"
+ "handle_NVMEraseResponse: paramID %d exceeds maximum expected value"
+ "handle_NVMOperationResponse: paramID %d exceeds maximum expected value"
+ "handle_NVMPublicKeyChallenge: paramID %d exceeds maximum expected value"
+ "initSigmaContextNvm: !userKey"
+ "initSigmaContextNvm: ccsigma_export_key_share: error"
+ "initSigmaContextNvm: ccsigma_set_signing_function"
+ "initSigmaContextNvm: key_share_size != 33"
+ "nvmDhPublicKeyX %@"
+ "nvmDhPublicKeyY %@"
+ "v44@0:8i16@20@28@?36"
- "###ELEE###: %s:%d: idsnStringRef: %@"
- "###ELEE###: %s:%d: test multiInstanceDataArray: %@"
- "-[ACCHWComponentAuthService _findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:]"
- "ERROR No batteryAuth io_service_t is found!"
- "_convertNVMReadResponse: Unsupported read response ID: %d"
- "createNoAuthICNonce:withChallenge:"
- "signVeridianChallenge Replying with signature=%@, deviceNonce=%@, authError = %d"

```
