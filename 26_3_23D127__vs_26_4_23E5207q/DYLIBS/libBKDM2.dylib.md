## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-873.60.2.0.0
-  __TEXT.__text: 0x7dd2c
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x5b64
-  __TEXT.__const: 0x8d47
-  __TEXT.__cstring: 0x6696
-  __TEXT.__oslogstring: 0x400e
-  __TEXT.__gcc_except_tab: 0x1690
+877.100.21.0.0
+  __TEXT.__text: 0x79748
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x5bfc
+  __TEXT.__const: 0x8dff
+  __TEXT.__cstring: 0x6bc5
+  __TEXT.__oslogstring: 0x42ae
+  __TEXT.__gcc_except_tab: 0x1688
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xd40
+  __TEXT.__unwind_info: 0xdc8
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x379
-  __TEXT.__objc_methname: 0x145e6
-  __TEXT.__objc_methtype: 0x2946
-  __TEXT.__objc_stubs: 0x7c20
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x13b8
+  __TEXT.__objc_classname: 0x37a
+  __TEXT.__objc_methname: 0x1495d
+  __TEXT.__objc_methtype: 0x297f
+  __TEXT.__objc_stubs: 0x7e20
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__const: 0x1528
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3be8
+  __DATA_CONST.__objc_selrefs: 0x3c78
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x328
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH_CONST.__const: 0x9a8
-  __AUTH_CONST.__cfstring: 0x5ec0
-  __AUTH_CONST.__objc_const: 0x91b8
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH_CONST.__const: 0x968
+  __AUTH_CONST.__cfstring: 0x5f80
+  __AUTH_CONST.__objc_const: 0x92c8
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xa0c
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0x890
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0x63
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 9026E52B-BC75-33F5-B6CE-C43723C89D80
-  Functions: 2751
-  Symbols:   8317
-  CStrings:  5370
+  UUID: 1CFA71D1-D2F5-36EF-B5C6-C322D402981D
+  Functions: 2812
+  Symbols:   8520
+  CStrings:  5446
 
Symbols:
+ +[BiometricKitXPCServerPearl getDummyModeForOperationKey:]
+ -[BiometricKitXPCServerPearl archiveCatacombDataForComponent:toArchiver:]
+ -[BiometricKitXPCServerPearl archiveCatacombDataForComponent:toArchiver:].cold.1
+ -[BiometricKitXPCServerPearl archiveCatacombDataForComponent:toArchiver:].cold.2
+ -[BiometricKitXPCServerPearl archiveCatacombDataForComponent:toArchiver:].cold.3
+ -[BiometricKitXPCServerPearl dummyModeEnabled]
+ -[BiometricKitXPCServerPearl getDummyModeEnrollment]
+ -[BiometricKitXPCServerPearl getDummyModeFaceOn]
+ -[BiometricKitXPCServerPearl getDummyModeMatch]
+ -[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]
+ -[BiometricKitXPCServerPearl init].cold.14
+ -[BiometricKitXPCServerPearl performEnrollCommand:].cold.3
+ -[BiometricKitXPCServerPearl performEnrollCommand:].cold.4
+ -[BiometricKitXPCServerPearl performMatchCommand:].cold.5
+ -[BiometricKitXPCServerPearl performMatchCommand:].cold.6
+ -[BiometricKitXPCServerPearl startNewMatchAttemptWithClient:].cold.3
+ -[BiometricKitXPCServerPearl unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:]
+ -[BiometricKitXPCServerPearl unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:].cold.1
+ -[BiometricKitXPCServerPearl unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:].cold.2
+ -[BiometricKitXPCServerPearl unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:].cold.3
+ -[BiometricKitXPCServerPearl unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:].cold.4
+ -[BiometricKitXPCServerPearl updateDummyModeEnabledFromNotification:]
+ -[BiometricKitXPCServerPearl updateSecureFaceDetectInterruption]
+ -[BiometricKitXPCServerPearl wakeGestureManager:didUpdateWakeGesture:].cold.2
+ -[BiometricPresenceDetectOperationPearl secureFaceDetectInterrupted]
+ -[BiometricPresenceDetectOperationPearl setSecureFaceDetectInterrupted:]
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table212
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table50
+ GCC_except_table65
+ GCC_except_table81
+ _OBJC_CLASS_$_BiometricKitCoreAnalyticsLogger
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._dummyModeEnabled
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._dummyModeLock
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._dummyModeTimerSource
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectInterruptionDispatchSource
+ _OBJC_IVAR_$_BiometricPresenceDetectOperationPearl._secureFaceDetectInterrupted
+ _OBJC_IVAR_$_PearlCoreAnalytics._logger
+ _OUTLINED_FUNCTION_51
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.225
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.228
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke_2.251
+ ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.269
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.873
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.874
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.875
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.878
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.879
+ ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.744
+ ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.789
+ ___75-[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]_block_invoke
+ ___75-[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]_block_invoke.cold.1
+ ___75-[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]_block_invoke.cold.2
+ ___75-[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]_block_invoke.cold.3
+ ___75-[BiometricKitXPCServerPearl handleActiveDummyModeWithBioOpType:withDelay:]_block_invoke.cold.4
+ ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.274
+ ___DummyModeNotificationCallback
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.161
+ ___block_literal_global.207
+ ___block_literal_global.253
+ ___block_literal_global.518
+ ___block_literal_global.877
+ ___block_literal_global.881
+ ___block_literal_global.925
+ ___block_literal_global.927
+ __oidMldsa44EcdsaP256Sha256
+ __oidMldsa44Ed25519Sha512
+ __oidMldsa44Rsa2048Pkcs15Sha256
+ __oidMldsa44Rsa2048PssSha256
+ __oidMldsa65EcdsaBrainpoolP256r1Sha512
+ __oidMldsa65EcdsaP256Sha512
+ __oidMldsa65EcdsaP384Sha512
+ __oidMldsa65Ed25519Sha512
+ __oidMldsa65Rsa3072Pkcs15Sha512
+ __oidMldsa65Rsa3072PssSha512
+ __oidMldsa65Rsa4096Pkcs15Sha512
+ __oidMldsa65Rsa4096PssSha512
+ __oidMldsa87EcdsaBrainpoolP384r1Sha512
+ __oidMldsa87EcdsaP384Sha512
+ __oidMldsa87EcdsaP521Sha512
+ __oidMldsa87Ed448Shake256
+ __oidMldsa87Rsa3072PssSha512
+ __oidMldsa87Rsa4096PssSha512
+ _dispatch_source_cancel
+ _dispatch_source_testcancel
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$catacombFileAccessed
+ _objc_msgSend$clearTemplateList
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$dummyModeEnabled
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$getDummyModeEnrollment
+ _objc_msgSend$getDummyModeFaceOn
+ _objc_msgSend$getDummyModeForOperationKey:
+ _objc_msgSend$getDummyModeMatch
+ _objc_msgSend$handleActiveDummyModeWithBioOpType:withDelay:
+ _objc_msgSend$isMasterComponent
+ _objc_msgSend$secureFaceDetectInterrupted
+ _objc_msgSend$setSecureFaceDetectInterrupted:
+ _objc_msgSend$updateDummyModeEnabledFromNotification:
+ _objc_msgSend$updateSecureFaceDetectInterruption
+ _oidMldsa44EcdsaP256Sha256
+ _oidMldsa44Ed25519Sha512
+ _oidMldsa44Rsa2048Pkcs15Sha256
+ _oidMldsa44Rsa2048PssSha256
+ _oidMldsa65EcdsaBrainpoolP256r1Sha512
+ _oidMldsa65EcdsaP256Sha512
+ _oidMldsa65EcdsaP384Sha512
+ _oidMldsa65Ed25519Sha512
+ _oidMldsa65Rsa3072Pkcs15Sha512
+ _oidMldsa65Rsa3072PssSha512
+ _oidMldsa65Rsa4096Pkcs15Sha512
+ _oidMldsa65Rsa4096PssSha512
+ _oidMldsa87EcdsaBrainpoolP384r1Sha512
+ _oidMldsa87EcdsaP384Sha512
+ _oidMldsa87EcdsaP521Sha512
+ _oidMldsa87Ed448Shake256
+ _oidMldsa87Rsa3072PssSha512
+ _oidMldsa87Rsa4096PssSha512
- GCC_except_table100
- GCC_except_table103
- GCC_except_table104
- GCC_except_table106
- GCC_except_table107
- GCC_except_table119
- GCC_except_table205
- GCC_except_table224
- GCC_except_table227
- GCC_except_table230
- GCC_except_table236
- GCC_except_table237
- GCC_except_table243
- GCC_except_table246
- GCC_except_table48
- GCC_except_table61
- GCC_except_table77
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.218
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.221
- ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.258
- ___47+[BLHelper median:count:queue:completionBlock:]_block_invoke.cold.3
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.846
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.847
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.850
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.853
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.856
- ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.741
- ___61-[BioLog logSequenceInfo:withContext:orientation:identities:]_block_invoke.786
- ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.263
- ___block_literal_global.158
- ___block_literal_global.204
- ___block_literal_global.242
- ___block_literal_global.492
- ___block_literal_global.849
- ___block_literal_global.852
- ___block_literal_global.855
- ___block_literal_global.858
- ___block_literal_global.898
- ___block_literal_global.900
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "!_dummyModeTimerSource"
+ "!dispatch_source_testcancel(strongSelf->_dummyModeTimerSource)"
+ "(bioOpType == kBioOpTypeEnroll) || (bioOpType == kBioOpTypeMatch)"
+ "(self.dummyModeEnabled && dummyModeCatacomb) || (!self.dummyModeEnabled && !dummyModeCatacomb)"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/BioLog/BLHelper.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/BioLog/BLScoreData.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/BioLog/BioLog.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/BioLog/BioLogDiagnosticPipeline.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsDailyTemplateMatchCountsEvent.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsEvent.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsMatchEvent.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsSecureFaceDetectEvent.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/PearlCoreAnalytics/PearlCoreAnalytics.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/SecureCameraIndicator/SecureCameraIndicator.m"
+ "/Library/Caches/com.apple.xbs/BFA12832-3A91-4220-8A11-27AE1798E34C/TemporaryDirectory.fpaH5X/Sources/Pearl/pearld/BiometricKitXPCServerPearl.m"
+ "@\"BiometricKitCoreAnalyticsLogger\""
+ "BKStatusDetailCaptureInterruption"
+ "DISABLED"
+ "Dummy Mode %s\n"
+ "DummyModeCatacomb"
+ "ENABLED"
+ "T@\"NSNumber\",R,N,GgetDummyModeEnrollment"
+ "T@\"NSNumber\",R,N,GgetDummyModeFaceOn"
+ "T@\"NSNumber\",R,N,GgetDummyModeMatch"
+ "TB,N,V_secureFaceDetectInterrupted"
+ "TB,R,N,V_dummyModeEnabled"
+ "[dummyModeDict[operationKey] isKindOfClass:[NSNumber class]]"
+ "__DummyModeNotificationCallback %p %p %@ %p %@\n"
+ "_dummyModeEnabled"
+ "_dummyModeLock"
+ "_dummyModeTimerSource"
+ "_logger"
+ "_secureFaceDetectInterrupted"
+ "_secureFaceDetectInterruptionDispatchSource"
+ "archiveCatacombDataForComponent:\n"
+ "archiveCatacombDataForComponent: -> (%{errno}d)\n"
+ "archiveCatacombDataForComponent:toArchiver:"
+ "archiver"
+ "arrayWithArray:"
+ "blockErr == 0 "
+ "catacombFileAccessed"
+ "clearTemplateList"
+ "com.apple.biometrickitd.dummyModeEnabledChanged"
+ "decodeObjectOfClass:forKey:"
+ "dummyModeEnabled"
+ "dummyModeEnrollment"
+ "dummyModeFaceOn"
+ "dummyModeMatch"
+ "encodeObject:forKey:"
+ "enrollment"
+ "faceOn"
+ "getDummyModeEnrollment"
+ "getDummyModeFaceOn"
+ "getDummyModeForOperationKey:"
+ "getDummyModeMatch"
+ "handleActiveDummyModeWithBioOpType:withDelay:"
+ "handleActiveDummyModeWithBioOpType:withDelay: %d %u\n"
+ "handleActiveDummyModeWithBioOpType:withDelay: %d %u (handler)\n"
+ "handleActiveDummyModeWithBioOpType:withDelay: (handler) -> err:0x%x\n"
+ "handleActiveDummyModeWithBioOpType:withDelay: -> err:0x%x\n"
+ "i48@0:8@16@24^@32^@40"
+ "isMasterComponent"
+ "operationKey"
+ "performCancelCommand: Cancel Dummy Mode handler dispatch source\n"
+ "secureFaceDetectInterrupted"
+ "self.dummyModeEnrollment"
+ "self.dummyModeMatch"
+ "sending status message %u (%u) to %@\n"
+ "setSecureFaceDetectInterrupted:"
+ "strongSelf.dummyModeEnrollment"
+ "strongSelf.dummyModeMatch"
+ "unarchiveCatacombDataForComponent:\n"
+ "unarchiveCatacombDataForComponent: -> (%{errno}d)\n"
+ "unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities:"
+ "unarchiver"
+ "updateDummyModeEnabledFromNotification -> void\n"
+ "updateDummyModeEnabledFromNotification:"
+ "updateDummyModeEnabledFromNotification: %d\n"
+ "updateSecureFaceDetectInterruption"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/BioLog/BLHelper.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/BioLog/BLScoreData.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/BioLog/BioLog.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/BioLog/BioLogDiagnosticPipeline.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsDailyTemplateMatchCountsEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsMatchEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/PearlCoreAnalytics/CoreAnalyticsEvents/PearlCoreAnalyticsSecureFaceDetectEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/PearlCoreAnalytics/PearlCoreAnalytics.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/SecureCameraIndicator/SecureCameraIndicator.m"
- "/Library/Caches/com.apple.xbs/Sources/Pearl/pearld/BiometricKitXPCServerPearl.m"
- "first <= nth"

```
