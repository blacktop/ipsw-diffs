## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-493.100.2.0.0
-  __TEXT.__text: 0x17dad0
+493.100.4.0.0
+  __TEXT.__text: 0x181be4
   __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_stubs: 0x17060
-  __TEXT.__objc_methlist: 0x88f4
-  __TEXT.__const: 0x2ce0
-  __TEXT.__cstring: 0xab73
+  __TEXT.__objc_stubs: 0x17200
+  __TEXT.__objc_methlist: 0x8974
+  __TEXT.__const: 0x2be0
+  __TEXT.__cstring: 0xae33
   __TEXT.__objc_classname: 0x1817
-  __TEXT.__objc_methname: 0x207f8
-  __TEXT.__objc_methtype: 0x5873
+  __TEXT.__objc_methname: 0x20a76
+  __TEXT.__objc_methtype: 0x59bc
   __TEXT.__gcc_except_tab: 0x2270
-  __TEXT.__oslogstring: 0x1f0d8
+  __TEXT.__oslogstring: 0x1f2b8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1580
   __TEXT.__swift5_fieldmd: 0xb6c

   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x4ef0
+  __TEXT.__unwind_info: 0x4f20
   __TEXT.__eh_frame: 0x6df0
   __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x15b0
-  __DATA_CONST.__auth_ptr: 0x508
-  __DATA_CONST.__const: 0xbbd8
-  __DATA_CONST.__cfstring: 0x6ae0
+  __DATA_CONST.__auth_ptr: 0x4d8
+  __DATA_CONST.__const: 0xc3b0
+  __DATA_CONST.__cfstring: 0x6ca0
   __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2b0

   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA.__objc_const: 0x24b90
-  __DATA.__objc_selrefs: 0x6cb0
+  __DATA.__objc_selrefs: 0x6d18
   __DATA.__objc_ivar: 0x9ac
   __DATA.__objc_data: 0x5330
   __DATA.__data: 0x3c28

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6613
+  Functions: 6660
   Symbols:   1299
-  CStrings:  9233
+  CStrings:  9276
 
CStrings:
+ "_contextFromSRPServerResponse:maxTTLInMins:"
+ "ak_analyticsEventWithContext:eventName:error:"
+ "createOSAttestationDataWithContext:attestationNonce:completion:"
+ "com.apple.authkit.serverUIStart"
+ "Anisette fetch retry succeeded!"
+ "Not required to set _shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "_getDCRTWithContext:completion:"
+ "_sendAttestedOSVersionWithContext:attestationNonce:"
+ "v16@?0@\"AKAuthorizationContext\"8"
+ "Setting credential: %!@(MISSING) on account: %!@(MISSING)"
+ "v32@?0@\"NSDictionary\"8@\"NSError\"16@\"AAFAnalyticsEvent\"24"
+ "contextFromSRPServerResponseWithShorterTTL:"
+ "_timeToLive:maxTTLInMins:"
+ "v40@0:8@\"AKAppleIDAuthenticationContext\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">32"
+ "_getAttestationData:rk:dak:error:"
+ "_fetchAuthContextWithUserResponse:client:completion:"
+ "com.apple.authkit.serverUIFinish"
+ "com.apple.authkit.sendLivenessNonce"
+ "Walrus Enabled, attaching arming info to SRP CPD"
+ "_handleRecoverCredentialsError:withContext:event:andCompletion:"
+ "_handleCheckInResponse:data:context:account:error:completion:"
+ "v48@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32^@40"
+ "com.apple.authkit.retrieveDAK"
+ "attestationDataForOSVersionWithContext:attestationNonce:completion:"
+ "set_shouldRequestToArmDeviceToAllowPCSKeyUpload:"
+ "com.apple.authkit.nativeRecoveryFinish"
+ "q32@0:8q16q24"
+ "Received nil flowId in AKAppleIDAuthenticationContext"
+ "com.apple.authkit.generateOSBoundRefKey"
+ "Retrieved DAK with error %!@(MISSING)"
+ "Not Setting _shouldRequestToArmDeviceToAllowPCSKeyUpload, isFirstPartyWebLogin is NO"
+ "ak_attestationErrorWithCode:underlyingError:"
+ "com.apple.authkit.sendAttestedOSVersion"
+ "com.apple.authkit.osVersionAttestationReq"
+ "Failed to fetch anisette data, attempting a one shot immediate retry... Error: %!@(MISSING)"
+ "_shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "_sendAnalyticsEvent:withError:"
+ "_retrieveDAK:error:"
+ "_updateRefKeyWithNonce:context:refkey:error:"
+ "Attested RK to DAK with error: %!@(MISSING)"
+ "com.apple.authkit.accountRecoveryFinish"
+ "@48@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32^@40"
+ "com.apple.authkit.generateOSVersionAttestationData"
+ "createOSVersionAttestationRefKeyWithContext:accessControl:error:"
+ "v40@?0@\"NSHTTPURLResponse\"8@\"NSDictionary\"16@\"NSError\"24@\"AAFAnalyticsEvent\"32"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8@16^@24"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}40@0:8@16^{__SecAccessControl=}24^@32"
+ "com.apple.authkit.generateDCRT"
+ "com.apple.authkit.nativeRecoveryStart"
+ "_shouldRequestToArmDeviceToAllowPCSKeyUpload %!d(MISSING)"
+ "com.apple.authkit.accountRecoveryStart"
+ "com.apple.authkit.updateRefkeyWithNonce"
+ "_isFirstPartyWebLogin: %!d(MISSING)"
- "createOSAttestationData:completion:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24"
- "_handleRecoverCredentialsError:withContext:andCompletion:"
- "attestationDataForOSVersion:completion:"
- "Failed to copy DAK: %!@(MISSING)"
- "Failed to attest RK to DAK with error: %!@(MISSING)"
- "_handleCheckInResponse:data:account:error:completion:"
- "sendAttestedOSVersion:"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8^{__SecAccessControl=}16^@24"
- "createOSVersionAttestationRefKey:error:"

```
