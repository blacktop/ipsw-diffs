## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.80.3.0.0
-  __TEXT.__text: 0x50834
+638.100.48.0.0
+  __TEXT.__text: 0x52284
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x64c0
-  __TEXT.__objc_methlist: 0x26fc
+  __TEXT.__objc_stubs: 0x6740
+  __TEXT.__objc_methlist: 0x2e58
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x176c
-  __TEXT.__cstring: 0x37e5
-  __TEXT.__objc_methname: 0x6e8f
-  __TEXT.__oslogstring: 0x735e
-  __TEXT.__objc_classname: 0x70d
-  __TEXT.__objc_methtype: 0xf96
-  __TEXT.__unwind_info: 0xc00
+  __TEXT.__gcc_except_tab: 0x1800
+  __TEXT.__cstring: 0x3995
+  __TEXT.__objc_methname: 0x738e
+  __TEXT.__oslogstring: 0x730a
+  __TEXT.__objc_classname: 0x74c
+  __TEXT.__objc_methtype: 0x10cd
+  __TEXT.__unwind_info: 0xc68
   __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__got: 0x678
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1438
-  __DATA_CONST.__cfstring: 0x3480
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__const: 0x14f8
+  __DATA_CONST.__cfstring: 0x35a0
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
-  __DATA.__objc_selrefs: 0x1c78
-  __DATA.__objc_ivar: 0x294
-  __DATA.__objc_data: 0x10e0
+  __DATA.__objc_const: 0x5138
+  __DATA.__objc_selrefs: 0x1df8
+  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_data: 0x1180
   __DATA.__data: 0x5a8
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x110
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/Versions/A/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/Versions/A/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8BB32006-02E4-3BC6-8EAB-A808FF9BC469
-  Functions: 1315
-  Symbols:   427
-  CStrings:  3099
+  UUID: 40231DFC-7ADA-3E28-A8AF-D944611E64C9
+  Functions: 1362
+  Symbols:   432
+  CStrings:  3164
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_AAFAnalyticsReporter
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
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
