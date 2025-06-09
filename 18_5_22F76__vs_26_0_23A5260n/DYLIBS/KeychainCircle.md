## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x28ecc
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0x1d44
+61901.0.9.0.1
+  __TEXT.__text: 0x28de0
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_methlist: 0x1d64
   __TEXT.__const: 0xd8
-  __TEXT.__dlopen_cstrs: 0x200
+  __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__gcc_except_tab: 0x15d8
-  __TEXT.__cstring: 0x2cbc
-  __TEXT.__oslogstring: 0x383b
+  __TEXT.__cstring: 0x308c
+  __TEXT.__oslogstring: 0x38aa
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x858
+  __TEXT.__unwind_info: 0x848
   __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x40d5
-  __TEXT.__objc_methtype: 0xf52
-  __TEXT.__objc_stubs: 0x2ea0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x10a0
+  __TEXT.__objc_methname: 0x4146
+  __TEXT.__objc_methtype: 0xf55
+  __TEXT.__objc_stubs: 0x2f80
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x1170
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe8
+  __DATA_CONST.__objc_selrefs: 0x1020
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0x2ac0
+  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__objc_const: 0x2af0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x1f8
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x318
-  __DATA.__bss: 0x170
+  __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CBC7C28-B01F-30C7-A98F-C781D27130D5
+  UUID: BC2B29E0-DBA2-35AC-B806-D017B932417D
   Functions: 777
-  Symbols:   2906
-  CStrings:  1992
+  Symbols:   2937
+  CStrings:  2055
 
Symbols:
+ -[AAFAnalyticsEventSecurity dealloc]
+ -[AAFAnalyticsEventSecurity metricSent]
+ -[AAFAnalyticsEventSecurity sendMetricWithResult:error:]
+ -[AAFAnalyticsEventSecurity setMetricSent:]
+ GCC_except_table375
+ GCC_except_table382
+ GCC_except_table512
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table554
+ GCC_except_table584
+ GCC_except_table587
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._metricSent
+ _SecIsInternalRelease
+ ___37-[KCPairingChannel fetchEpoch:error:]_block_invoke.281
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.279
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.280
+ ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.292
+ ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.293
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.286
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.287
+ ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.223
+ ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.224
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.245
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.246
+ ___51-[KCPairingChannel fetchPrepare:application:error:]_block_invoke.238
+ ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.249
+ ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.250
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.225
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.230
+ ___56-[AAFAnalyticsEventSecurity sendMetricWithResult:error:]_block_invoke
+ ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.231
+ ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.232
+ ___84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.288
+ ___84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.289
+ ___88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.242
+ ___88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.243
+ ___Block_byref_object_copy_.386
+ ___Block_byref_object_copy_.912
+ ___Block_byref_object_dispose_.387
+ ___Block_byref_object_dispose_.913
+ ___block_descriptor_tmp.1484
+ ___block_descriptor_tmp.1547
+ ___block_descriptor_tmp.1585
+ ___block_descriptor_tmp.1622
+ ___block_descriptor_tmp.71.1541
+ ___block_literal_global.1134
+ ___block_literal_global.1447
+ ___block_literal_global.1513
+ ___block_literal_global.1583
+ ___block_literal_global.214
+ ___block_literal_global.260
+ ___block_literal_global.31
+ ___block_literal_global.34.1408
+ ___block_literal_global.422
+ __os_log_default
+ __os_log_fault_impl
+ _apply_block_1.1491
+ _apply_block_2.1523
+ _kSecurityRTCErrorDomain
+ _kSecurityRTCEventNameClearCliqueFromAccount
+ _kSecurityRTCEventNameEscrowPasscodeCacheAvailable
+ _kSecurityRTCEventNameEscrowPasscodeEnableCacheFlow
+ _kSecurityRTCEventNameEscrowRepairOperation
+ _kSecurityRTCEventNameFetchAccountWideSettings
+ _kSecurityRTCEventNameFetchAccountWideSettingsTPH
+ _kSecurityRTCEventNameOTBecomeReadyOperation
+ _kSecurityRTCEventNameOTLocalCKKSResetOperation
+ _kSecurityRTCEventNameOTResetOperation
+ _kSecurityRTCEventNameOTSetCDPBitOperation
+ _kSecurityRTCEventNameOTTriggerEscrowUpdateOperation
+ _kSecurityRTCEventNameOctagonTrustLost
+ _kSecurityRTCEventNamePerformCKServerUnreadableDataRemoval
+ _kSecurityRTCEventNamePerformCKServerUnreadableDataRemovalTPH
+ _kSecurityRTCEventNameResetCKKSZonesLackingTLKsOperation
+ _kSecurityRTCEventNameResetProtectedData
+ _kSecurityRTCEventNameResetSOS
+ _kSecurityRTCEventNameResetTPH
+ _kSecurityRTCFieldAccountIsG
+ _kSecurityRTCFieldAccountIsW
+ _kSecurityRTCFieldEgoMachineIDEvictedFromTDL
+ _kSecurityRTCFieldEgoMachineIDGhosted
+ _kSecurityRTCFieldEgoMachineIDUnknown
+ _kSecurityRTCFieldEgoMachineIDUnknownRemovalReasonFromTDL
+ _kSecurityRTCFieldEgoMachineIDUserInitiatedRemovalFromTDL
+ _objc_msgSend$_setError
+ _objc_msgSend$eventName
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
+ _objc_msgSend$metricSent
+ _objc_msgSend$position
+ _objc_msgSend$sendMetricWithResult:error:
+ _objc_msgSend$setMetricSent:
+ _objc_msgSend$setPosition:
- +[SecurityAnalyticsReporterRTC sendMetricWithEvent:success:error:]
- -[AAFAnalyticsEventSecurity getEvent]
- GCC_except_table315
- GCC_except_table383
- GCC_except_table390
- GCC_except_table520
- GCC_except_table529
- GCC_except_table531
- GCC_except_table581
- GCC_except_table585
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AAAFoundationLibrary.1180
- _AAAFoundationLibraryCore.frameworkLibrary.1184
- ___37-[KCPairingChannel fetchEpoch:error:]_block_invoke.279
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.273
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.274
- ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.290
- ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.291
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.282
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.283
- ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.221
- ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.222
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.242
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.243
- ___51-[KCPairingChannel fetchPrepare:application:error:]_block_invoke.236
- ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.246
- ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.247
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.223
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.224
- ___66+[SecurityAnalyticsReporterRTC sendMetricWithEvent:success:error:]_block_invoke
- ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.229
- ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.230
- ___84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.286
- ___84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.287
- ___88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.240
- ___88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.241
- ___AAAFoundationLibraryCore_block_invoke.1185
- ___Block_byref_object_copy_.387
- ___Block_byref_object_copy_.924
- ___Block_byref_object_dispose_.388
- ___Block_byref_object_dispose_.925
- ___block_descriptor_tmp.1466
- ___block_descriptor_tmp.1530
- ___block_descriptor_tmp.1568
- ___block_descriptor_tmp.1604
- ___block_descriptor_tmp.71.1524
- ___block_literal_global.1198
- ___block_literal_global.1441
- ___block_literal_global.1495
- ___block_literal_global.1566
- ___block_literal_global.211
- ___block_literal_global.233
- ___block_literal_global.28
- ___block_literal_global.283
- ___block_literal_global.416
- _apply_block_1.1473
- _apply_block_2.1507
- _audit_stringAAAFoundation.1186
- _objc_msgSend$getEvent
- _objc_msgSend$initWithEventName:eventCategory:initData:
- _objc_msgSend$sendMetricWithEvent:success:error:
CStrings:
+ "@48@0:8@16r^{ccdigest_info=QQQQ*^v^?^?i^?}24^{ccdh_gp=QQ^{cczp_funcs}[1Q]}32^{ccrng_state=^?}40"
+ "@56@0:8@16@24r^{ccdigest_info=QQQQ*^v^?^?i^?}32^{ccdh_gp=QQ^{cczp_funcs}[1Q]}40^{ccrng_state=^?}48"
+ "@64@0:8@16@24@32r^{ccdigest_info=QQQQ*^v^?^?i^?}40^{ccdh_gp=QQ^{cczp_funcs}[1Q]}48^{ccrng_state=^?}56"
+ "TB,V_metricSent"
+ "_metricSent"
+ "_setError"
+ "accountIsG"
+ "accountIsW"
+ "com.apple.security.clearCliqueFromAccount"
+ "com.apple.security.escrowPasscodeCacheAvailable"
+ "com.apple.security.escrowPasscodeEnableCacheFlow"
+ "com.apple.security.escrowRepairOperation"
+ "com.apple.security.fetchAccountWideSettings"
+ "com.apple.security.fetchAccountWideSettingsTPH"
+ "com.apple.security.oTBecomeReadyOperation"
+ "com.apple.security.oTLocalCKKSResetOperation"
+ "com.apple.security.oTResetOperation"
+ "com.apple.security.oTSetCDPBitOperation"
+ "com.apple.security.oTTriggerEscrowUpdateOperation"
+ "com.apple.security.octagonTrustLost"
+ "com.apple.security.performCKServerUnreadableDataRemoval"
+ "com.apple.security.performCKServerUnreadableDataRemovalTPH"
+ "com.apple.security.resetCKKSZonesLackingTLKsOperation"
+ "com.apple.security.resetProtectedData"
+ "com.apple.security.resetSOS"
+ "com.apple.security.resetTPH"
+ "egoMachineIDEvictedFromTDL"
+ "egoMachineIDGhosted"
+ "egoMachineIDUnknown"
+ "egoMachineIDUnknownRemovalReasonFromTDL"
+ "egoMachineIDUserInitiatedRemovalFromTDL"
+ "failed to send metric event %@ before deallocation"
+ "getBytes:range:"
+ "hasError"
+ "initWithEventName:eventCategory:initData:altDSID:"
+ "kSecurityRTCErrorDomain"
+ "metricSent"
+ "metrics: failed to send metric event %@ before deallocation"
+ "position"
+ "sendMetricWithResult:error:"
+ "setMetricSent:"
+ "setPosition:"
+ "v28@0:8B16@20"
- "@48@0:8@16r^{ccdigest_info=QQQQ*^v^?^?i}24^{ccdh_gp=QQ^{cczp_funcs}[1Q]}32^{ccrng_state=^?}40"
- "@56@0:8@16@24r^{ccdigest_info=QQQQ*^v^?^?i}32^{ccdh_gp=QQ^{cczp_funcs}[1Q]}40^{ccrng_state=^?}48"
- "@64@0:8@16@24@32r^{ccdigest_info=QQQQ*^v^?^?i}40^{ccdh_gp=QQ^{cczp_funcs}[1Q]}48^{ccrng_state=^?}56"
- "getEvent"
- "initWithEventName:eventCategory:initData:"
- "sendMetricWithEvent:success:error:"
- "v36@0:8@16B24@28"

```
