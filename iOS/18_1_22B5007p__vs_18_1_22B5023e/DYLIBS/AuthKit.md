## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-488.6.0.0.0
-  __TEXT.__text: 0xc3984
+491.0.0.0.0
+  __TEXT.__text: 0xc5a1c
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xaaf8
+  __TEXT.__objc_methlist: 0xad50
   __TEXT.__const: 0x2121
-  __TEXT.__cstring: 0xcdab
-  __TEXT.__oslogstring: 0xfd7d
-  __TEXT.__gcc_except_tab: 0x50cc
+  __TEXT.__cstring: 0xcf5b
+  __TEXT.__oslogstring: 0xff2c
+  __TEXT.__gcc_except_tab: 0x514c
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x37f0
-  __TEXT.__objc_classname: 0x176f
-  __TEXT.__objc_methname: 0x1da79
-  __TEXT.__objc_methtype: 0x3c64
-  __TEXT.__objc_stubs: 0xcf60
-  __DATA_CONST.__got: 0x908
-  __DATA_CONST.__const: 0x4e28
-  __DATA_CONST.__objc_classlist: 0x510
+  __TEXT.__unwind_info: 0x3888
+  __TEXT.__objc_classname: 0x17a6
+  __TEXT.__objc_methname: 0x1df8a
+  __TEXT.__objc_methtype: 0x3d8c
+  __TEXT.__objc_stubs: 0xd280
+  __DATA_CONST.__got: 0x920
+  __DATA_CONST.__const: 0x4f78
+  __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6090
+  __DATA_CONST.__objc_selrefs: 0x61b0
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x138
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0xd5a0
-  __AUTH_CONST.__objc_const: 0x21ef0
+  __AUTH_CONST.__const: 0x1050
+  __AUTH_CONST.__cfstring: 0xd860
+  __AUTH_CONST.__objc_const: 0x224c0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x1c48
-  __DATA.__objc_ivar: 0xe2c
+  __AUTH.__objc_data: 0x1748
+  __DATA.__objc_ivar: 0xe5c
   __DATA.__data: 0x1540
-  __DATA.__bss: 0x630
-  __DATA_DIRTY.__objc_data: 0x1658
-  __DATA_DIRTY.__bss: 0x228
+  __DATA.__bss: 0x620
+  __DATA_DIRTY.__objc_data: 0x1bf8
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5441
-  Symbols:   7375
-  CStrings:  8527
+  Functions: 5502
+  Symbols:   7463
+  CStrings:  8628
 
Symbols:
+ _AKAuthenticationNewAccountCreated
+ _AKHTTPHeaderLocalUserUUID
+ _AKHTTPHeaderMID
+ _AKHTTPHeaderOTP
+ _AKHTTPHeaderRoutingInfo
+ _AKTelemetryMissingDeviceSessionID
+ _AKUserBirthDayKey
+ _AKUserBirthMonthKey
+ _OBJC_CLASS_$_AKAttestationAnalyticsInfo
+ _OBJC_CLASS_$_AKPersistRecoveryKeyContext
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_METACLASS_$_AKAttestationAnalyticsInfo
+ _OBJC_METACLASS_$_AKPersistRecoveryKeyContext
+ _kAAAnalyticsDeviceRemovalReason
+ _kAKAnalyticsEventBAAStats
+ _kAKAnalyticsFieldBodySize
+ _kAKAnalyticsFieldEndPoint
+ _kAKAnalyticsFieldHeaderSize
+ _kAKAnalyticsFieldProcessName
+ _kAKAnalyticsFieldRequestMethod
+ _kAKAnalyticsFieldResponseCode
CStrings:
+ "\x0f\x01\x16!\x1f\x0f\f"
+ "%!@(MISSING): Attempting to remove PRK for account (%!@(MISSING))"
+ "%!@(MISSING): Overriding the telemetryFlowID: from recoveryContext.authContext.telemetryFlowID=%!@(MISSING) to flowID=%!@(MISSING)"
+ "AKAttestationAnalyticsInfo"
+ "AKAttestationAnalyticsInfo: host: %!@(MISSING), headerSize: %!l(MISSING)u, bodySize: %!l(MISSING)u"
+ "AKNewAccountCreated"
+ "AKPersistRecoveryKeyContext"
+ "AKPersistRecoveryKeyContext:\nVerifier: %!@(MISSING)\nKeyType: %!l(MISSING)u"
+ "Anisette fetch failed with XPC error, retrying..."
+ "Asking akd to persist recovery key with persistKeyContext: %!@(MISSING), authContext:%!@(MISSING)"
+ "Attestation fetch failed with XPC error, retrying..."
+ "Error posting attestation analytics - %!@(MISSING)"
+ "Failed to persist recovery key: %!@(MISSING)"
+ "Feature VMBAA enabled = %!@(MISSING)"
+ "HTTPMethod"
+ "Successfully posted analytics."
+ "T@\"NSDictionary\",C,N,V_verifier"
+ "T@\"NSNumber\",C,N,V_birthDay"
+ "T@\"NSNumber\",C,N,V_birthMonth"
+ "T@\"NSString\",C,N,V_endPointVIP"
+ "T@\"NSString\",C,N,V_errorDomain"
+ "T@\"NSString\",C,N,V_requestMethod"
+ "TB,R,N,GisBAASupportedForVirtualMachines"
+ "TQ,N,V_bodySize"
+ "TQ,N,V_headerSize"
+ "TQ,N,V_keyType"
+ "Tq,N,V_errorCode"
+ "Tq,N,V_responseCode"
+ "VMBAA"
+ "Vv24@0:8@?<v@?@\"NSError\">16"
+ "Vv32@0:8@\"AKAttestationAnalyticsInfo\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "_attestationDataForRequest:completion:"
+ "_attestationDataForRequest:error:"
+ "_baaSupportedForVirtualMachines"
+ "_birthDay"
+ "_birthDay"
+ "_birthMonth"
+ "_birthMonth"
+ "_bodySize"
+ "_bodySize"
+ "_endPointVIP"
+ "_endPointVIP"
+ "_errorDomain"
+ "_errorDomain"
+ "_fetchAnisetteDataAndProvisionIfNecessary:error:"
+ "_fetchAnisetteDataAndProvisionIfNecessary:withCompletion:"
+ "_headerSize"
+ "_headerSize"
+ "_keyType"
+ "_keyType"
+ "_reportOnRequest:response:attestationData:"
+ "_requestMethod"
+ "_requestMethod"
+ "_responseCode"
+ "_verifier"
+ "_verifier"
+ "ak_bucketWithSize:"
+ "ak_isXPCServiceError"
+ "ak_numberObject"
+ "authkit/persist-recovery-key"
+ "baaSupportedForVirtualMachines"
+ "birthDD"
+ "birthDay"
+ "birthMM"
+ "birthMonth"
+ "bodySize"
+ "bodySize"
+ "com.apple.authkit.baa.stats"
+ "deviceRemovalReason"
+ "device_session_id_missing"
+ "endPointVIP"
+ "endPointVIP"
+ "errorDomain"
+ "fetchBirthdayForAltDSID:completion:"
+ "headerSize"
+ "headerSize"
+ "initWithContext:uiProvider:flowID:"
+ "isBAASupportedForVirtualMachines"
+ "keyType"
+ "numberFromString:"
+ "persistRecoveryKeyWithContext:authContext:completion:"
+ "postAttestationAnalytics:completion:"
+ "postAttestationAnalyticsWithData:completion:"
+ "processName"
+ "q24@0:8q16"
+ "requestMethod"
+ "requestMethod"
+ "responseCode"
+ "responseCode"
+ "setBirthDay:"
+ "setBirthMonth:"
+ "setBodySize:"
+ "setEndPointVIP:"
+ "setErrorCode:"
+ "setErrorDomain:"
+ "setHeaderSize:"
+ "setKeyType:"
+ "setNumberStyle:"
+ "setRequestMethod:"
+ "setResponseCode:"
+ "setVerifier:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\">24"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16@\"NSError\"24"
+ "v40@0:8@\"AKPersistRecoveryKeyContext\"16@\"AKAppleIDAuthenticationContext\"24@?<v@?B@\"NSError\">32"
+ "verifier"
- "\x0f\x01\x16!\x1f\x0f\n"
- "Failed to persist master key: %!@(MISSING)"
- "Td,N"
- "_AKServerTimeAdjustmentKey"
- "authkit/persist-master-key"
- "serverTimeAdjustment"
- "setServerTimeAdjustment:"

```
