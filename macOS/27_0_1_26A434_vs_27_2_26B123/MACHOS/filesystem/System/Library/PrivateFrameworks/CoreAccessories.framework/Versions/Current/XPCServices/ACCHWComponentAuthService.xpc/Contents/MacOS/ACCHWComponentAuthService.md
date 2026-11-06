## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/Current/XPCServices/ACCHWComponentAuthService.xpc/Contents/MacOS/ACCHWComponentAuthService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x4934c
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x1f3d3
-  __TEXT.__cstring: 0x35f8
+1219.40.10.0.0
+  __TEXT.__text: 0x4af20
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_stubs: 0x12c0
+  __TEXT.__objc_methlist: 0x72c
+  __TEXT.__const: 0x1f453
+  __TEXT.__cstring: 0x375a
+  __TEXT.__oslogstring: 0x6fff
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x192d
-  __TEXT.__objc_methtype: 0x873
-  __TEXT.__oslogstring: 0x6aaf
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x1428
-  __DATA_CONST.__const: 0x8228
-  __DATA_CONST.__cfstring: 0x1720
+  __TEXT.__objc_methname: 0x1a94
+  __TEXT.__objc_methtype: 0x89d
+  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__unwind_info: 0x1458
+  __DATA_CONST.__const: 0x8288
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_got: 0x7b8
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA.__objc_const: 0xb10
-  __DATA.__objc_selrefs: 0x608
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0xb68
+  __DATA.__objc_selrefs: 0x640
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x940
-  __DATA.__bss: 0x118
+  __DATA.__data: 0x968
+  __DATA.__bss: 0x128
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1612
-  Symbols:   3593
-  CStrings:  1512
+  Functions: 1639
+  Symbols:   3653
+  CStrings:  1558
 
Symbols:
+ -[ACCHWComponentAuthService _mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:]
+ -[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateLASWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService signRCAMChallenge:completionHandler:]
+ -[ACCHWComponentAuthService signTouchControllerChallenge:completionHandler:componentIndex:]
+ -[ACCHWComponentAuthService signVeridianChallenge:completionHandler:]
+ -[ACCHWComponentAuthServiceParams setSigningHandler:]
+ -[ACCHWComponentAuthServiceParams signingHandler]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCHWComponentAuthService.build/Objects-normal/arm64e/acc_internal_settings.o
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table93
+ OBJC_IVAR_$_ACCHWComponentAuthServiceParams._signingHandler
+ _CFDictionaryCreate
+ _NSUnderlyingErrorKey
+ ___acc_internalSettings_isInternalBuild_block_invoke
+ ___block_descriptor_32_e15_v24?0^v8B16i20l
+ ___block_descriptor_32_e55_B32?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16^^{__CFError}24l
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ __createError
+ __mfi4_clearStaleSessionHandlers
+ __mfi4_readSignature
+ __mfi4_sendAndWaitForResponse
+ __mfi4_wrapProtocolError
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _acc_internalSettings_boolForKey
+ _acc_internalSettings_integerForKey
+ _acc_internalSettings_isInternalBuild
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _kACCInfo_PPIDVersionUID
+ _kCFACCInfo_PPIDVersionUID
+ _kCFErrorUnderlyingErrorKey
+ _mfi4_clearStaleSessionHandlers
+ _mfi4_readSignature
+ _mfi4_sendAndWaitForResponse
+ _objc_msgSend$_mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:
+ _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$setSigningHandler:
+ _objc_msgSend$signRCAMChallenge:completionHandler:componentIndex:
+ _objc_msgSend$signVeridianChallenge:completionHandler:componentIndex:
+ _objc_msgSend$signingHandler
+ _objc_msgSend$verifyModuleCertificate:forModule:forAuthFlags:forIndex:
+ _oidAppleExtendedKeyUsageSWUpdateSigning
+ acc_internalSettings_boolForKey
+ acc_internalSettings_integerForKey
+ acc_internalSettings_isInternalBuild
+ acc_internalSettings_isInternalBuild.isInternalBuild
+ acc_internalSettings_isInternalBuild.onceToken
+ acc_internal_settings.c
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- GCC_except_table67
- GCC_except_table71
- GCC_except_table77
- ___block_descriptor_32_e12_v20?0^v8B16l
- ___block_descriptor_32_e40_v24?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16l
- __mfi4_waitForResponse
- _mfi4_waitForResponse
CStrings:
+ "%s: !sendOutgoingHandler"
+ "%s: AuthCPI2CWrite failed: %d"
+ "%s: I2CRead failed after retries: %x"
+ "%s: IOServiceOpen failed: %d"
+ "%s: authSession(%d), keepOpen %d, error %d"
+ "%s: clearing stale handlers (open:%d nvmW:%d nvmR:%d refresh:%d completion:%d signing:%d)"
+ "%s: keepOpen(%d), error(%d)"
+ "%s: outgoingDataHandler failed: %@"
+ "%s: timed out waiting for response"
+ "(moduleType=%d) Error: expecting 16-byte challenge argument"
+ "(moduleType=%d) _mfi4_readSignature failed: %@"
+ "6)"
+ "ACCHWComponentAuthService.io"
+ "ACCHWComponentAuthService.mfi4Auth"
+ "B32@?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16^^{__CFError}24"
+ "PPIDVersionUID"
+ "T@?,C,V_signingHandler"
+ "T^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v},V_authSession"
+ "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}"
+ "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}16@0:8"
+ "_mfi4_clearStaleSessionHandlers"
+ "_mfi4_sendAndWaitForResponse"
+ "_mfi4_sessionCloseHandler"
+ "_mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:"
+ "_signingHandler"
+ "acc_internalSettings: internal-only setting %{public}@ active"
+ "acc_internalSettings: internal-only setting %{public}@ active (%ld)"
+ "authSetupStart: initMessage_RequestAuthSetup failed: %d"
+ "authenticateTouchControllerWithChallenge:completionHandler:"
+ "com.apple.mfi4Auth.decrypt"
+ "com.apple.mfi4Auth.encrypt"
+ "com.apple.mfi4Auth.process"
+ "com.apple.mfi4Auth.protocol"
+ "com.apple.mfi4Auth.receive"
+ "com.apple.mfi4Auth.send"
+ "decryptIncomingData: decryptPayload rc=%d"
+ "decryptIncomingData: failed: %d"
+ "encryptOutgoingData: encryptPayload rc=%d"
+ "failed to handle refresh access state response"
+ "mfi4Auth_protocol_handle_AuthCert: Accessory did NOT provide PrivacyPrefix!"
+ "mfi4Auth_protocol_processIncomingMessage: error: %d"
+ "mfi4Auth_protocol_processIncomingMessageExtra: error: %d"
+ "mfi4Error"
+ "numberWithInt:"
+ "processIncomingMessageExtra: non-Extra message id 0x%04x — falling through to relay"
+ "processIncomingMessageRelay: error: %d"
+ "processIncomingMessageRelay: non-relay message id 0x%04x — no relay action"
+ "processOutgoingSecureTunnelDataForClient: sendOutgoingData failed"
+ "publicManufacturerNVMRead: initMessage_RequestManufacturerNVMRead failed: %d"
+ "receiveIncomingData: sendOutgoingData failed"
+ "requestRefreshAccessState: !authSession"
+ "requestRefreshAccessState: !outMessage"
+ "requestRefreshAccessState: authSession shutting down"
+ "requestRefreshAccessState: initMessage_RequestRefreshAccessState failed: %d"
+ "setSigningHandler:"
+ "signTouchControllerChallenge:completionHandler:componentIndex:"
+ "signingHandler"
+ "userNVMRead: initMessage_RequestUserNVMRead failed: %d"
+ "userNVMWrite: initMessage_RequestUserNVMWrite failed: %d"
+ "v24@0:8^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}16"
+ "v24@?0^v8B16i20"
+ "v52@0:8i16@20@28@36@?44"
+ "verifyModuleCertificate:forModule:forAuthFlags:forIndex:"
- "%s: AuthCPI2CWrite failed"
- "%s: IOServiceOpen failed"
- "%s: authSession(%d), keepOpen %d"
- "6("
- "Data not passed in"
- "T^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v},V_authSession"
- "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}"
- "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}16@0:8"
- "decryptIncomingData: failed"
- "encryptOutgoingData: encryptPayload: error: %d"
- "failed to handle auth failed"
- "mfi4Auth_protocol_processIncomingMessage: error"
- "mfi4Auth_protocol_processIncomingMessageExtra: error"
- "processIncomingMessageRelay: error"
- "v20@?0^v8B16"
- "v24@0:8^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}16"
- "v24@?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16"
```
