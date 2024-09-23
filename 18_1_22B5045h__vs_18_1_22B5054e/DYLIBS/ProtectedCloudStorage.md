## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1037.40.12.0.0
-  __TEXT.__text: 0x4ab90
+1037.40.65.0.0
+  __TEXT.__text: 0x4be7c
   __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_methlist: 0x19c8
-  __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x87dd
-  __TEXT.__oslogstring: 0x16e4
-  __TEXT.__gcc_except_tab: 0x1714
-  __TEXT.__dlopen_cstrs: 0x19e
-  __TEXT.__unwind_info: 0x11b8
-  __TEXT.__objc_classname: 0x2ab
-  __TEXT.__objc_methname: 0x47be
-  __TEXT.__objc_methtype: 0x144b
-  __TEXT.__objc_stubs: 0x37a0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x1fd0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__objc_methlist: 0x1a68
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x87c3
+  __TEXT.__oslogstring: 0x16f9
+  __TEXT.__gcc_except_tab: 0x17d8
+  __TEXT.__dlopen_cstrs: 0x29a
+  __TEXT.__unwind_info: 0x1218
+  __TEXT.__objc_classname: 0x2d8
+  __TEXT.__objc_methname: 0x49a5
+  __TEXT.__objc_methtype: 0x1479
+  __TEXT.__objc_stubs: 0x39c0
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x2060
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1210
+  __DATA_CONST.__objc_selrefs: 0x1278
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0xc50
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0x3790
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__const: 0x900
+  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__objc_const: 0x38c0
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x878
-  __DATA.__bss: 0x2a9
+  __DATA.__data: 0x870
+  __DATA.__bss: 0x2f8
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x1068
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x110
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1556
-  Symbols:   2346
-  CStrings:  2369
+  Functions: 1585
+  Symbols:   2385
+  CStrings:  2388
 
Symbols:
+ _SecureBackupGetAccountInfoWithInfo
+ _SecureBackupRecoverWithInfo
+ _kSecureBackupStingrayMetadataKey
+ _SecureBackupEnableWithInfo
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ ___PCSUpdateStingrayMetadata
+ _kSecureBackupMetadataKey
+ _SecureBackupUpdateMetadataWithInfo
+ ___PCS_WAITING_FOR_COM_APPLE_SBD
+ _SecureBackupDisableWithInfo
+ _kSecureBackupStingrayMetadataHashKey
+ __PCSStingrayCreateRandom
- _kPCSSecureBackupCFStingrayMetadataKey
- ___PCS_WAITING_FOR_COM_APPLE_SDB
- ___PCSStoreStingrayIdentity
- ___PCSGetStingrayDeathMarker
- ___PCSCopyStingrayIdentity
CStrings:
+ "failed to softlink AuthKit"
+ "authKitAccountWithAltDSID returned error: %!@(MISSING)"
+ "AAFAnalyticsTransportRTC"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "isAAAFoundationAvailable"
+ "_areTestsEnabled"
+ "TB,V_isAAAFoundationAvailable"
+ "AAFAnalyticsReporter"
+ "accountAccessTelemetryOptInForAccount:"
+ "T@\"AAFAnalyticsEvent\",&,V_event"
+ "com.apple.aaa.dnu"
+ "addMetrics:"
+ "kAAFDeviceSessionId"
+ "authKitAccountWithAltDSID:error:"
+ "canSendMetrics"
+ "initWithPCSMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "areTestsEnabled"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
+ "_isAuthKitAvailable"
+ "isAuthKitAvailable"
+ "setIsAAAFoundationAvailable:"
+ "initWithEventName:eventCategory:initData:"
+ "_canSendMetrics"
+ "analyticsReporterWithTransport:"
+ "TB,V_isAuthKitAvailable"
+ "v36@0:8@16B24@28"
+ "@\"AAFAnalyticsEvent\""
+ "PCSAnalyticsReporterRTC"
+ "telemetryDeviceSessionIDForAccount:"
+ "getEvent"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "setCanSendMetrics:"
+ "primaryAuthKitAccount"
+ "permittedToSendMetrics"
+ "aafanalyticsevent-pcs"
+ "fetchDeviceSessionIDFromAuthKit:"
+ "_event"
+ "kAAFFlowId"
+ "BackupKeybagSHA256"
+ "TB,V_canSendMetrics"
+ "sendMetricWithEvent:success:error:"
+ "KeybagSHA256/KeybagDigest missing"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "TB,V_areTestsEnabled"
+ "com.apple.pcs.aafanalyticsevent.queue"
+ "setIsAuthKitAvailable:"
+ "AAFAnalyticsEventPCS"
+ "failed to softlink AAAFoundation"
+ "setAreTestsEnabled:"
+ "event"
+ "sendEvent:"
+ "rtcAnalyticsReporter"
+ "_isAAAFoundationAvailable"
+ "__PCSUpdateStingrayMetadata: %!{(MISSING)bool}d"
+ "setEvent:"
+ "AAFAnalyticsEvent"
+ "didSucceed"
- "T^{__CFData=},V_brHSMContent"
- "authKitAccountWithAltDSID:"
- "/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices"
- "_brHSMContent"
- "setFDEKey:"
- "SecureBackupDisableWithInfo"
- "SecureBackupEnableWithInfo"
- "SecureBackupRecoverWithInfo"
- "T^{__CFData=},V_hsmContent"
- "_hsmContent"
- "_metadataHashKey"
- "T^{__CFData=},V_FDEKey"
- "newKeychainContent"
- "externalEscrow"
- "_FDEKey"
- "^v"
- "PCSStoreStingrayIdentity: %!@(MISSING)"
- "^v16@0:8"
- "IUseiCloudKeychain"
- "setHsmContent:"
- "FDEKey"
- "_externalEscrow"
- "PCSStoreStingrayIdentity: %!{(MISSING)public}s"
- "SecureBackupGetAccountInfoWithInfo"
- "metadataHashKey"
- "T^v,V_metadataHashKey"
- "T^{__CFData=},V_externalEscrow"
- "_newKeychainContent"
- "hsmContent"
- "brHSMContent"
- "setMetadataHashKey:"
- "SecureBackupUpdateMetadataWithInfo"
- "T^{__CFData=},V_newKeychainContent"
- "setNewKeychainContent:"
- "KeybagDigest missing"
- "setExternalEscrow:"
- "PCSCopyStingrayIdentity: %!{(MISSING)public}@ (error: %!{(MISSING)public}@)"
- "setBrHSMContent:"
- "v24@0:8^v16"

```
