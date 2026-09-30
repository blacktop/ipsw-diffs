## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/XPCServices/ACCHWComponentAuthService.xpc/Contents/MacOS/ACCHWComponentAuthService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x4934c
+1219.40.5.0.0
+  __TEXT.__text: 0x49bc4
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x1f3d3
-  __TEXT.__cstring: 0x35f8
+  __TEXT.__objc_stubs: 0x11a0
+  __TEXT.__objc_methlist: 0x6bc
+  __TEXT.__const: 0x1f443
+  __TEXT.__cstring: 0x3618
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x192d
-  __TEXT.__objc_methtype: 0x873
-  __TEXT.__oslogstring: 0x6aaf
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x1428
-  __DATA_CONST.__const: 0x8228
+  __TEXT.__objc_methname: 0x1a10
+  __TEXT.__objc_methtype: 0x89d
+  __TEXT.__oslogstring: 0x6b45
+  __TEXT.__gcc_except_tab: 0x2c8
+  __TEXT.__unwind_info: 0x1430
+  __DATA_CONST.__const: 0x8238
   __DATA_CONST.__cfstring: 0x1720
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__auth_got: 0x7b0
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA.__objc_const: 0xb10
-  __DATA.__objc_selrefs: 0x608
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0xb68
+  __DATA.__objc_selrefs: 0x628
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x940
+  __DATA.__data: 0x968
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1612
-  Symbols:   3593
-  CStrings:  1512
+  Functions: 1618
+  Symbols:   3618
+  CStrings:  1522
 
Symbols:
+ -[ACCHWComponentAuthService _mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:]
+ -[ACCHWComponentAuthService signTouchControllerChallenge:completionHandler:componentIndex:]
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
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table86
+ OBJC_IVAR_$_ACCHWComponentAuthServiceParams._signingHandler
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ __mfi4_clearStaleSessionHandlers
+ __mfi4_readSignature
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _mfi4_clearStaleSessionHandlers
+ _mfi4_readSignature
+ _objc_msgSend$_mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:
+ _objc_msgSend$setSigningHandler:
+ _objc_msgSend$signingHandler
+ _oidAppleExtendedKeyUsageSWUpdateSigning
+ systemInfo_isDeveloperBuild.developerBuild
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
- GCC_except_table75
- GCC_except_table79
- GCC_except_table83
CStrings:
+ "%s: clearing stale handlers (open:%d nvmW:%d nvmR:%d refresh:%d completion:%d signing:%d)"
+ "(moduleType=%d) Error: expecting 16-byte challenge argument"
+ "6)"
+ "T@?,C,V_signingHandler"
+ "T^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v},V_authSession"
+ "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}"
+ "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}16@0:8"
+ "_mfi4_clearStaleSessionHandlers"
+ "_mfi4_signChallengeForModuleType:authParams:challenge:componentIndex:signingHandler:"
+ "_signingHandler"
+ "setSigningHandler:"
+ "signTouchControllerChallenge:completionHandler:componentIndex:"
+ "signingHandler"
+ "v24@0:8^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C]B[16C][16C][64C]Ci[32C]Q*Q^v}16"
+ "v52@0:8i16@20@28@36@?44"
- "6("
- "T^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v},V_authSession"
- "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}"
- "^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}16@0:8"
- "v24@0:8^{mfi4AuthProtocolSession_s=^v^{iAP2MsgParser_st}*ISBBBBiiBB^{__CFData}*Q*Qii^S^*^i^vQQCB^v^viCC[4C]Q[3C]QC[3C]Qi[3@?]@?@?@?@?@?@?@?@?@?@?SSS[33C][33C][16C][16C]i[32C]*Q*Q*Q^vi[32C]*Q*Q*Q[64C][16C][16C][64C]Ci[32C]Q*Q^v}16"
```
