## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x1fbd0
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x17f4
+61439.100.301.0.0
+  __TEXT.__text: 0x20dc0
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x1844
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0xa04
-  __TEXT.__cstring: 0x14d2
+  __TEXT.__gcc_except_tab: 0xa6c
+  __TEXT.__cstring: 0x1534
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x2891
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__oslogstring: 0x284e
+  __TEXT.__unwind_info: 0x718
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x3b10
-  __TEXT.__objc_methtype: 0x583
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__objc_methname: 0x3bf7
+  __TEXT.__objc_methtype: 0x580
+  __TEXT.__objc_stubs: 0x25e0
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe30
+  __DATA_CONST.__objc_selrefs: 0xe58
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x360
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x22d0
+  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x2258
   __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x138
   __DATA.__bss: 0x168

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 617
-  Symbols:   886
-  CStrings:  1104
+  Functions: 613
+  Symbols:   903
+  CStrings:  1111
 
Symbols:
+ _MetricsOverrideTestsAreEnabled
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
+ _kSecurityRTCEventCategoryAccountDataAccessRecovery
+ _kSecurityRTCEventNameHandleRecoveryResults
+ _kSecurityRTCEventNameHandleRecoveryResultsResetAndEstablish
+ _kSecurityRTCEventNamePerformEscrowRecovery
+ _kSecurityRTCEventNamePerformSilentEscrowRecovery
+ _kSecurityRTCEventNameRecoverSilentWithCDPContext
+ _kSecurityRTCEventNameRecoverWithCDPContext
+ _kSecurityRTCEventNameRecoverWithInfo
+ _kSecurityRTCEventNameRestoreFromBottleEvent
+ _kSecurityRTCEventNameRestoreKeychainAsyncWithPassword
+ _kSecurityRTCFieldMissingDigest
+ _kSecurityRTCFieldMissingPassword
+ _kSecurityRTCFieldRecordDataMissing
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "@52@0:8@16@24@32B40^@44"
+ "Failed to handle recovery results"
+ "Failed to recover using CDP context"
+ "Failed to recover with info"
+ "addMetrics:"
+ "deviceSessionID"
+ "flowID"
+ "handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:error:"
+ "recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:error:"
+ "sendMetricWithEvent:success:error:"
- "@60@0:8@16@24@32B40@44^@52"
- "handleRecoveryResults:recoveredInformation:record:performedSilentBurn:recoverError:error:"
- "octagontrust-handleRecoveryResults: sbd escrow recovery failed: %@"
- "recoverSilentWithCDPContext:allRecords:error:"
- "recoverWithCDPContext:escrowRecord:error:"

```
