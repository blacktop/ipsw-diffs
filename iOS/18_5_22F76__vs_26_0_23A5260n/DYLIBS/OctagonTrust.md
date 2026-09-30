## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x20dc0
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1844
+61901.0.9.0.1
+  __TEXT.__text: 0x22a64
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x193c
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0x1534
+  __TEXT.__gcc_except_tab: 0xb74
+  __TEXT.__cstring: 0x165c
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__oslogstring: 0x284e
-  __TEXT.__unwind_info: 0x718
-  __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x3bf7
-  __TEXT.__objc_methtype: 0x580
-  __TEXT.__objc_stubs: 0x25e0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x280
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__oslogstring: 0x293e
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__objc_classname: 0x203
+  __TEXT.__objc_methname: 0x3f0b
+  __TEXT.__objc_methtype: 0x5ca
+  __TEXT.__objc_stubs: 0x2840
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe58
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x2258
-  __DATA.__objc_ivar: 0x16c
+  __DATA_CONST.__objc_selrefs: 0xf20
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x2418
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x138
   __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 383E655E-1044-3A4A-80D3-D9ABCF30060D
-  Functions: 613
-  Symbols:   2061
-  CStrings:  1258
+  UUID: 3412BF02-1B26-39AD-8116-BFA931399908
+  Functions: 636
+  Symbols:   2141
+  CStrings:  1322
 
Symbols:
+ +[OTClique(Framework) escrowCheck:isBackgroundCheck:error:]
+ +[OTClique(Framework) trustedFullPeers:error:]
+ +[OTEscrowCheckCallResult supportsSecureCoding]
+ -[OTEscrowCheckCallResult .cxx_destruct]
+ -[OTEscrowCheckCallResult description]
+ -[OTEscrowCheckCallResult dictionaryRepresentation]
+ -[OTEscrowCheckCallResult encodeWithCoder:]
+ -[OTEscrowCheckCallResult initWithCoder:]
+ -[OTEscrowCheckCallResult initWithNeedsReenroll:octagonTrusted:secureTermsNeeded:moveRequest:repairReason:]
+ -[OTEscrowCheckCallResult moveRequest]
+ -[OTEscrowCheckCallResult needsReenroll]
+ -[OTEscrowCheckCallResult octagonTrusted]
+ -[OTEscrowCheckCallResult repairReason]
+ -[OTEscrowCheckCallResult secureTermsNeeded]
+ -[OTEscrowCheckCallResult setMoveRequest:]
+ -[OTEscrowCheckCallResult setNeedsReenroll:]
+ -[OTEscrowCheckCallResult setOctagonTrusted:]
+ -[OTEscrowCheckCallResult setRepairReason:]
+ -[OTEscrowCheckCallResult setSecureTermsNeeded:]
+ GCC_except_table384
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table394
+ GCC_except_table396
+ GCC_except_table398
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table419
+ GCC_except_table424
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table442
+ GCC_except_table445
+ GCC_except_table448
+ _CloudServicesLibrary.730
+ _CloudServicesLibraryCore.frameworkLibrary.731
+ _OBJC_CLASS_$_OTEscrowCheckCallResult
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._moveRequest
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._needsReenroll
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._octagonTrusted
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._repairReason
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._secureTermsNeeded
+ _OBJC_METACLASS_$_OTEscrowCheckCallResult
+ __OBJC_$_CLASS_METHODS_OTEscrowCheckCallResult
+ __OBJC_$_CLASS_PROP_LIST_OTEscrowCheckCallResult
+ __OBJC_$_INSTANCE_METHODS_OTEscrowCheckCallResult
+ __OBJC_$_INSTANCE_VARIABLES_OTEscrowCheckCallResult
+ __OBJC_$_PROP_LIST_OTEscrowCheckCallResult
+ __OBJC_CLASS_PROTOCOLS_$_OTEscrowCheckCallResult
+ __OBJC_CLASS_RO_$_OTEscrowCheckCallResult
+ __OBJC_METACLASS_RO_$_OTEscrowCheckCallResult
+ ___46+[OTClique(Framework) trustedFullPeers:error:]_block_invoke
+ ___59+[OTClique(Framework) escrowCheck:isBackgroundCheck:error:]_block_invoke
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.122
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.129
+ ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke_2
+ ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.84
+ ___99+[OTClique(Framework) handleRecoveryResults:recoveredInformation:record:performedSilentBurn:error:]_block_invoke.37
+ ___CloudServicesLibraryCore_block_invoke.732
+ ___block_descriptor_48_e8_32r40r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16lr32l8r40l8
+ ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.752
+ ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.750
+ _audit_stringCloudServices.733
+ _getkSecureBackupRecordIDKeySymbolLoc.ptr.751
+ _getkSecureBackupRecordLabelKeySymbolLoc.ptr.749
+ _objc_getProperty
+ _objc_msgSend$_setError
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$enabled
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$escrowCheck:isBackgroundCheck:reply:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hasWalrus
+ _objc_msgSend$moveRequest
+ _objc_msgSend$needsReenroll
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$octagonTrusted
+ _objc_msgSend$position
+ _objc_msgSend$repairReason
+ _objc_msgSend$resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:altDSID:flowID:deviceSessionID:canSendMetrics:error:
+ _objc_msgSend$resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:
+ _objc_msgSend$secureTermsNeeded
+ _objc_msgSend$sendMetricWithResult:error:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$trustedFullPeers:reply:
+ _objc_setProperty_atomic
- GCC_except_table362
- GCC_except_table367
- GCC_except_table373
- GCC_except_table375
- GCC_except_table377
- GCC_except_table381
- GCC_except_table383
- GCC_except_table385
- GCC_except_table387
- GCC_except_table389
- GCC_except_table391
- GCC_except_table393
- GCC_except_table397
- GCC_except_table407
- GCC_except_table416
- GCC_except_table418
- GCC_except_table420
- GCC_except_table423
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _CloudServicesLibrary.675
- _CloudServicesLibraryCore.frameworkLibrary.676
- _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.140
- ___64+[OTClique(Framework) recoverWithRecoveryKey:recoveryKey:error:]_block_invoke.147
- ___72+[OTClique(Framework) registerRecoveryKeyWithContext:recoveryKey:error:]_block_invoke.102
- ___CloudServicesLibraryCore_block_invoke.677
- ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.701
- ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.699
- _audit_stringCloudServices.678
- _getkSecureBackupRecordIDKeySymbolLoc.ptr.700
- _getkSecureBackupRecordLabelKeySymbolLoc.ptr.698
- _objc_msgSend$resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:error:
- _objc_msgSend$resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:reply:
- _objc_msgSend$sendMetricWithEvent:success:error:
CStrings:
+ "!"
+ "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld,"
+ "@\"OTEscrowMoveRequestContext\""
+ "@44@0:8B16B20B24@28q36"
+ "Number of trusted Octagon full peers: %@"
+ "OTEscrowCheckCallResult"
+ "T@\"OTEscrowMoveRequestContext\",&,V_moveRequest"
+ "TB,V_needsReenroll"
+ "TB,V_octagonTrusted"
+ "TB,V_secureTermsNeeded"
+ "Tq,V_repairReason"
+ "_moveRequest"
+ "_needsReenroll"
+ "_octagonTrusted"
+ "_repairReason"
+ "_secureTermsNeeded"
+ "_setError"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "escrowCheck errored: %@"
+ "escrowCheck invoked for context: %@"
+ "escrowCheck succeeded %@"
+ "escrowCheck:isBackgroundCheck:error:"
+ "escrowCheck:isBackgroundCheck:reply:"
+ "getBytes:range:"
+ "hasError"
+ "initWithNeedsReenroll:octagonTrusted:secureTermsNeeded:moveRequest:repairReason:"
+ "moveRequest"
+ "needsReenroll"
+ "numberWithInteger:"
+ "octagon-count-trusted-full-peers"
+ "octagon-escrow-check"
+ "octagonTrusted"
+ "position"
+ "q"
+ "q16@0:8"
+ "repairReason"
+ "resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:altDSID:flowID:deviceSessionID:canSendMetrics:error:"
+ "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:"
+ "secureTermsNeeded"
+ "sendMetricWithResult:error:"
+ "setMoveRequest:"
+ "setNeedsReenroll:"
+ "setOctagonTrusted:"
+ "setPosition:"
+ "setRepairReason:"
+ "setSecureTermsNeeded:"
+ "trustedFullPeers errored: %@"
+ "trustedFullPeers invoked for context: %@"
+ "trustedFullPeers succeeded, total count: %@"
+ "trustedFullPeers:error:"
+ "trustedFullPeers:reply:"
+ "v24@0:8q16"
+ "v24@?0@\"OTEscrowCheckCallResult\"8@\"NSError\"16"
- "resetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:error:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:reply:"
- "sendMetricWithEvent:success:error:"

```
