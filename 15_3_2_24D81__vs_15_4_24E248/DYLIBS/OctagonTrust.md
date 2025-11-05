## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/Versions/A/OctagonTrust`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x21ec0
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x17f4
+61439.101.1.0.0
+  __TEXT.__text: 0x23244
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x1844
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xa04
-  __TEXT.__cstring: 0x1529
+  __TEXT.__gcc_except_tab: 0xa70
+  __TEXT.__cstring: 0x158b
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x2891
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__oslogstring: 0x284e
+  __TEXT.__unwind_info: 0x728
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x3b10
-  __TEXT.__objc_methtype: 0x583
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__objc_methname: 0x3bf7
+  __TEXT.__objc_methtype: 0x580
+  __TEXT.__objc_stubs: 0x25e0
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe30
+  __DATA_CONST.__objc_selrefs: 0xe58
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x22d0
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x2258
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x138

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
+  - /System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E6008D4-861C-3A58-965C-297B8A8C8B22
-  Functions: 625
-  Symbols:   1420
-  CStrings:  1249
+  UUID: 15594C6E-67F4-30FD-9C23-E218C8895BFC
+  Functions: 621
+  Symbols:   1441
+  CStrings:  1259
 
Symbols:
+ +[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:]
+ CloudServicesLibrary.678
+ CloudServicesLibraryCore.frameworkLibrary.679
+ _MetricsOverrideTestsAreEnabled
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
+ __64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.150
+ __64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.159
+ __72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.110
+ __CloudServicesLibraryCore_block_invoke.680
+ ___99+[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:]_block_invoke
+ ___block_descriptor_65_e8_32s40r_e17_v16?0"NSError"8l
+ __getkSecureBackupRecordIDKeySymbolLoc_block_invoke.703
+ __getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.701
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
+ _objc_msgSend$addMetrics:
+ _objc_msgSend$deviceSessionID
+ _objc_msgSend$flowID
+ _objc_msgSend$handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:
+ _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:
+ _objc_msgSend$recoverSilentWithCDPContext:allRecords:altDSID:flowID:deviceSessionID:error:
+ _objc_msgSend$recoverWithCDPContext:escrowRecord:altDSID:flowID:deviceSessionID:error:
+ _objc_msgSend$sendMetricWithEvent:success:error:
+ getkSecureBackupRecordIDKeySymbolLoc.ptr.702
+ getkSecureBackupRecordLabelKeySymbolLoc.ptr.700
- +[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:recoverError:error:]
- CloudServicesLibrary.677
- CloudServicesLibraryCore.frameworkLibrary.678
- __64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.122
- __64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.129
- __72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.82
- __CloudServicesLibraryCore_block_invoke.679
- ___112+[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:recoverError:error:]_block_invoke
- ___block_descriptor_57_e8_32r_e17_v16?0"NSError"8l
- __getkSecureBackupRecordIDKeySymbolLoc_block_invoke.704
- __getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.702
- _objc_msgSend$handleRecoveryResults:recoveredInformation:record:performedSilentBurn:recoverError:error:
- _objc_msgSend$recoverSilentWithCDPContext:allRecords:error:
- _objc_msgSend$recoverWithCDPContext:escrowRecord:error:
- getkSecureBackupRecordIDKeySymbolLoc.ptr.703
- getkSecureBackupRecordLabelKeySymbolLoc.ptr.701
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
