## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.80.2.0.1
-  __TEXT.__text: 0x4c29c
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_stubs: 0x67a0
-  __TEXT.__objc_methlist: 0x270c
+638.100.48.0.0
+  __TEXT.__text: 0x4da14
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_stubs: 0x6a40
+  __TEXT.__objc_methlist: 0x2e60
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x1b64
-  __TEXT.__cstring: 0x3d34
-  __TEXT.__objc_methname: 0x7037
-  __TEXT.__oslogstring: 0x7d87
-  __TEXT.__objc_classname: 0x70d
-  __TEXT.__objc_methtype: 0xfab
-  __TEXT.__unwind_info: 0xc10
-  __DATA_CONST.__auth_got: 0x7f0
-  __DATA_CONST.__got: 0x6b0
+  __TEXT.__gcc_except_tab: 0x1bfc
+  __TEXT.__cstring: 0x3ee4
+  __TEXT.__objc_methname: 0x7536
+  __TEXT.__oslogstring: 0x7d33
+  __TEXT.__objc_classname: 0x74c
+  __TEXT.__objc_methtype: 0x10e2
+  __TEXT.__unwind_info: 0xc70
+  __DATA_CONST.__auth_got: 0x7f8
+  __DATA_CONST.__got: 0x6d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__cfstring: 0x3800
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__const: 0x1488
+  __DATA_CONST.__cfstring: 0x3920
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x59c8
-  __DATA.__objc_selrefs: 0x1d00
-  __DATA.__objc_ivar: 0x294
-  __DATA.__objc_data: 0x10e0
+  __DATA.__objc_const: 0x5138
+  __DATA.__objc_selrefs: 0x1e80
+  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1300
-  Symbols:   479
-  CStrings:  2793
+  Functions: 1344
+  Symbols:   485
+  CStrings:  2849
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_AAFAnalyticsReporter
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
+ _objc_retain_x7
CStrings:
+ "-[SecureBackupDaemon _recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:reply:]"
+ "-[SecureBackupDaemon _recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:reply:]"
+ "@\"AAFAnalyticsEvent\""
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "AAFAnalyticsEventSecureBackup"
+ "Can't move to Federation %@"
+ "Failed to recover escrow record"
+ "SecureBackupAnalyticsReporterRTC"
+ "T@\"AAFAnalyticsEvent\",&,V_event"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "TB,V_areTestsEnabled"
+ "TB,V_canSendMetrics"
+ "TB,V_isAAAFoundationAvailable"
+ "TB,V_isAuthKitAvailable"
+ "_areTestsEnabled"
+ "_canSendMetrics"
+ "_event"
+ "_isAAAFoundationAvailable"
+ "_isAuthKitAvailable"
+ "_recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:reply:"
+ "_recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:reply:"
+ "accountAccessTelemetryOptInForAccount:"
+ "addMetrics:"
+ "analyticsReporterWithTransport:"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "areTestsEnabled"
+ "authKitAccountWithAltDSID returned error: %@"
+ "canSendMetrics"
+ "com.apple.aaa.dnu"
+ "com.apple.sbd.aafanalyticsevent.queue"
+ "com.apple.sbd.recoverEscrowWithRequest"
+ "com.apple.sbd.recoverWithRequest"
+ "com.apple.sbd.remoteEscrowRestore"
+ "com.apple.sbd.silentBurn"
+ "com.apple.sbd.sortEscrowRecordsForMatchingPassphrase"
+ "didSucceed"
+ "event"
+ "fetchDeviceSessionIDFromAuthKit:"
+ "getEvent"
+ "initWithEventName:eventCategory:initData:"
+ "initWithMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "isAAAFoundationAvailable"
+ "isAuthKitAvailable"
+ "permittedToSendMetrics"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "primaryAuthKitAccount"
+ "recoverEscrowWithRequest failed, didn't return status dictionary"
+ "recoverSilentWithCDPContextInDaemon:allRecords:altDSID:flowID:deviceSessionID:reply:"
+ "recoverWithCDPContextInDaemon:escrowRecord:altDSID:flowID:deviceSessionID:reply:"
+ "recoverWithRequest failed, didn't return result dictionary"
+ "rtcAnalyticsReporter"
+ "sendEvent:"
+ "sendMetricWithEvent:success:error:"
+ "setAreTestsEnabled:"
+ "setCanSendMetrics:"
+ "setEvent:"
+ "setIsAAAFoundationAvailable:"
+ "setIsAuthKitAvailable:"
+ "sharedInstance"
+ "telemetryDeviceSessionIDForAccount:"
+ "v36@0:8@16B24@28"
+ "v64@0:8@\"OTICDPRecordContext\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@\"OTICDPRecordContext\"16@\"OTEscrowRecord\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\"@\"NSError\">56"
- "-[SecureBackupDaemon _recoverSilentWithCDPContext:allRecords:reply:]"
- "-[SecureBackupDaemon _recoverWithCDPContext:escrowRecord:reply:]"
- "Certificate requested for federation %@; terms not accepted"
- "NSUbiquitousKeyValueStore synchronize failed: %@"
- "NSUbiquitousKeyValueStore synchronize succeeded"
- "Terms not accepted for federation %@"
- "doSynchronize"

```
