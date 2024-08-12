## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1200.0.0.0.0
-  __TEXT.__text: 0x40728
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x7380
-  __TEXT.__objc_methlist: 0x2250
+1206.0.0.0.0
+  __TEXT.__text: 0x40a90
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__objc_methlist: 0x2270
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x1290
-  __TEXT.__cstring: 0x2203
-  __TEXT.__objc_methname: 0xb446
-  __TEXT.__oslogstring: 0x8c8f
+  __TEXT.__gcc_except_tab: 0x1298
+  __TEXT.__cstring: 0x22e2
+  __TEXT.__objc_methname: 0xb4d6
+  __TEXT.__oslogstring: 0x8dcc
   __TEXT.__objc_classname: 0x6c1
-  __TEXT.__objc_methtype: 0x31fc
+  __TEXT.__objc_methtype: 0x3230
   __TEXT.__info_plist: 0x455
   __TEXT.__unwind_info: 0xda8
-  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__const: 0x1dd0
   __DATA_CONST.__cfstring: 0x1120

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x75d8
-  __DATA.__objc_selrefs: 0x23f0
+  __DATA.__objc_const: 0x75f8
+  __DATA.__objc_selrefs: 0x2410
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc00

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1081
-  Symbols:   432
-  CStrings:  2540
+  Functions: 1083
+  Symbols:   433
+  CStrings:  2549
 
Symbols:
+ _NPKGetRemoteBiometricAuthenticationStatusTrustLost
CStrings:
+ "-[NPDCompanionPassLibrary isWatchIssuerAppProvisioningSupportedWithHandler:]"
+ "-[NPDCompanionPassLibrary unexpiredPassesOrderedByGroup:]"
+ "-[NPKRemoteAdminConnectionServiceAgent handleCredentialsUpdate:forUniqueID:completion:]"
+ "Notice: NPKIDVRemoteDeviceService: Found trustLost:%!@(MISSING) for remoteBiometricAuthenticationStatusForCredentialType:%!@(MISSING)"
+ "Notice: NPKIDVRemoteDeviceService: Requested remoteBiometricAuthenticationStatusForCredentialType:%!@(MISSING)"
+ "Warning: NPKIDVRemoteDeviceService: Requested remote biometric authentication status for unknown credential type:%!@(MISSING)"
+ "Warning: cannot handle credentials update due to nil delegate in %!s(MISSING)"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:"
+ "remoteDevicesManager:remoteBiometricAuthenticationStatusForCredentialType:completion:"
+ "v40@0:8@\"NPKIDVRemoteDevicesManager\"16Q24@?<v@?B>32"
- "Notice: Updated credentials: %!@(MISSING) for pass with unique ID %!@(MISSING); error: %!@(MISSING); sent to %!@(MISSING)"

```
