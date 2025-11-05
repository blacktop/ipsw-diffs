## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x29dcc
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x18e4
+61439.101.1.0.0
+  __TEXT.__text: 0x2c570
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x1d44
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x2518
-  __TEXT.__gcc_except_tab: 0x1320
-  __TEXT.__oslogstring: 0x33af
   __TEXT.__dlopen_cstrs: 0x1aa
+  __TEXT.__gcc_except_tab: 0x15f0
+  __TEXT.__cstring: 0x2de2
+  __TEXT.__oslogstring: 0x3822
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__unwind_info: 0x8b8
   __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x3df5
-  __TEXT.__objc_methtype: 0xec7
-  __TEXT.__objc_stubs: 0x2e60
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x8b8
+  __TEXT.__objc_methname: 0x40d5
+  __TEXT.__objc_methtype: 0xf52
+  __TEXT.__objc_stubs: 0x2ea0
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe70
+  __DATA_CONST.__objc_selrefs: 0xfe8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x29e0
-  __AUTH_CONST.__objc_const: 0x2ea8
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x3240
+  __AUTH_CONST.__objc_const: 0x2ac0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x318
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1a8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A3EE7D7-5761-35FD-82D2-8ADA72D86F24
-  Functions: 801
-  Symbols:   2176
-  CStrings:  1854
+  UUID: C7F56997-EE36-33CA-8F34-98BCF5C5E116
+  Functions: 815
+  Symbols:   2230
+  CStrings:  2013
 
Symbols:
+ +[KCJoiningAcceptSession sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:error:]
+ +[KCJoiningRequestCircleSession sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:]
+ +[KCJoiningRequestSecretSession sessionWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:]
+ -[KCAESGCMDuplexSession deviceSessionID]
+ -[KCAESGCMDuplexSession flowID]
+ -[KCAESGCMDuplexSession setDeviceSessionID:]
+ -[KCAESGCMDuplexSession setFlowID:]
+ -[KCJoiningAcceptSession altDSID]
+ -[KCJoiningAcceptSession deviceSessionID]
+ -[KCJoiningAcceptSession flowID]
+ -[KCJoiningAcceptSession initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:]
+ -[KCJoiningAcceptSession setAltDSID:]
+ -[KCJoiningAcceptSession setDeviceSessionID:]
+ -[KCJoiningAcceptSession setFlowID:]
+ -[KCJoiningRequestCircleSession altDSID]
+ -[KCJoiningRequestCircleSession deviceSessionID]
+ -[KCJoiningRequestCircleSession flowID]
+ -[KCJoiningRequestCircleSession initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:]
+ -[KCJoiningRequestCircleSession initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:]
+ -[KCJoiningRequestCircleSession setAltDSID:]
+ -[KCJoiningRequestCircleSession setDeviceSessionID:]
+ -[KCJoiningRequestCircleSession setFlowID:]
+ -[KCJoiningRequestSecretSession deviceSessionID]
+ -[KCJoiningRequestSecretSession flowID]
+ -[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:]
+ -[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:]
+ -[KCJoiningRequestSecretSession setDeviceSessionID:]
+ -[KCJoiningRequestSecretSession setFlowID:]
+ -[KCPairingChannel allPCSItemPersistentRefs]
+ -[KCPairingChannel fetchItemForPersistentRef:error:]
+ -[KCPairingChannel fetchPCSItemPersistentRefs:error:]
+ -[KCPairingChannel setAllPCSItemPersistentRefs:]
+ -[KCPairingChannelContext accountIsGuitarfish]
+ -[KCPairingChannelContext setAccountIsGuitarfish:]
+ AAAFoundationLibrary.1204
+ AAAFoundationLibraryCore.frameworkLibrary.1208
+ GCC_except_table100
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table157
+ GCC_except_table159
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table226
+ GCC_except_table236
+ GCC_except_table354
+ GCC_except_table422
+ GCC_except_table429
+ GCC_except_table559
+ GCC_except_table568
+ GCC_except_table570
+ GCC_except_table620
+ GCC_except_table624
+ GCC_except_table629
+ OBJC_IVAR_$_KCAESGCMDuplexSession._deviceSessionID
+ OBJC_IVAR_$_KCAESGCMDuplexSession._flowID
+ OBJC_IVAR_$_KCJoiningAcceptSession._altDSID
+ OBJC_IVAR_$_KCJoiningAcceptSession._deviceSessionID
+ OBJC_IVAR_$_KCJoiningAcceptSession._flowID
+ OBJC_IVAR_$_KCJoiningRequestCircleSession._altDSID
+ OBJC_IVAR_$_KCJoiningRequestCircleSession._deviceSessionID
+ OBJC_IVAR_$_KCJoiningRequestCircleSession._flowID
+ OBJC_IVAR_$_KCJoiningRequestSecretSession._deviceSessionID
+ OBJC_IVAR_$_KCJoiningRequestSecretSession._flowID
+ OBJC_IVAR_$_KCPairingChannel._allPCSItemPersistentRefs
+ OBJC_IVAR_$_KCPairingChannelContext._accountIsGuitarfish
+ __34-[KCPairingChannel validateStart:]_block_invoke.426
+ __34-[KCPairingChannel validateStart:]_block_invoke.429
+ __37-[KCPairingChannel fetchEpoch:error:]_block_invoke.279
+ __44-[KCPairingChannel initAsInitiator:version:]_block_invoke.200
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.273
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.274
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.275
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.276
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.277
+ __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.278
+ __49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.291
+ __49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.292
+ __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.282
+ __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.283
+ __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.284
+ __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.285
+ __50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.219
+ __50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.220
+ __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.240
+ __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.241
+ __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.242
+ __51-[KCPairingChannel fetchPrepare:application:error:]_block_invoke.234
+ __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.244
+ __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.247
+ __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.248
+ __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.221
+ __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.222
+ __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.224
+ __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.226
+ __66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.227
+ __66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.228
+ __84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.286
+ __84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.287
+ __88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.238
+ __88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.239
+ __AAAFoundationLibraryCore_block_invoke.1209
+ __Block_byref_object_copy_.386
+ __Block_byref_object_copy_.936
+ __Block_byref_object_dispose_.387
+ __Block_byref_object_dispose_.937
+ __block_descriptor_tmp.1496
+ __block_descriptor_tmp.1617
+ __block_descriptor_tmp.1652
+ __block_descriptor_tmp.1687
+ __block_descriptor_tmp.17.1526
+ __block_descriptor_tmp.73.1528
+ __block_literal_global.1224
+ __block_literal_global.1459
+ __block_literal_global.1525
+ __block_literal_global.1651
+ __block_literal_global.209
+ __block_literal_global.236
+ __block_literal_global.286
+ __block_literal_global.417
+ _compare
+ _kSecMatchLimitOne
+ _kSecReturnPersistentRef
+ _kSecValuePersistentRef
+ _kSecurityRTCEventNameEstablish
+ _kSecurityRTCEventNameEstablishOperation
+ _kSecurityRTCEventNameFetchAfterEstablish
+ _kSecurityRTCEventNameFetchRecoverableTLKShares
+ _kSecurityRTCEventNameHandleRecoveryResults
+ _kSecurityRTCEventNameHandleRecoveryResultsResetAndEstablish
+ _kSecurityRTCEventNameJoinWithVoucherInTPH
+ _kSecurityRTCEventNameJoinWithVoucherOperation
+ _kSecurityRTCEventNameOnqueueEstablishTPH
+ _kSecurityRTCEventNamePairingFailedToFetchItemForPersistentRef
+ _kSecurityRTCEventNamePerformEscrowRecovery
+ _kSecurityRTCEventNamePerformSilentEscrowRecovery
+ _kSecurityRTCEventNamePiggybackingAcceptorInitialMessage
+ _kSecurityRTCEventNamePiggybackingAcceptorProcessApplication
+ _kSecurityRTCEventNamePiggybackingAcceptorProcessMessage
+ _kSecurityRTCEventNamePiggybackingCircleInitiatorHandleCircleBlobMessage
+ _kSecurityRTCEventNamePiggybackingCircleInitiatorInitialMessage
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorHandleChallenge
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorHandleVerification
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorInitialMessage
+ _kSecurityRTCEventNamePreflightVouchWithBottle
+ _kSecurityRTCEventNameRecoverSilentWithCDPContext
+ _kSecurityRTCEventNameRecoverWithCDPContext
+ _kSecurityRTCEventNameRecoverWithInfo
+ _kSecurityRTCEventNameRestoreFromBottleEvent
+ _kSecurityRTCEventNameRestoreKeychainAsyncWithPassword
+ _kSecurityRTCEventNameVouchWithBottle
+ _kSecurityRTCEventNameVouchWithBottleTPH
+ _kSecurityRTCFieldMissingDigest
+ _kSecurityRTCFieldMissingPassword
+ _kSecurityRTCFieldRecordDataMissing
+ _kSecurityRTCFieldTotalNumberOfCustodians
+ _kSecurityRTCFieldTotalNumberOfDistrustedRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfPeers
+ _kSecurityRTCFieldTotalNumberOfPreapprovals
+ _kSecurityRTCFieldTotalNumberOfRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfTrustedCustodians
+ _kSecurityRTCFieldTotalNumberOfTrustedRecoveryKeys
+ _objc_msgSend$accountIsGuitarfish
+ _objc_msgSend$allPCSItemPersistentRefs
+ _objc_msgSend$fetchItemForPersistentRef:error:
+ _objc_msgSend$fetchPCSItemPersistentRefs:error:
+ _objc_msgSend$initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:
+ _objc_msgSend$initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:
+ _objc_msgSend$initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:
+ _objc_msgSend$initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:
+ _objc_msgSend$initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:
+ _objc_msgSend$setAllPCSItemPersistentRefs:
+ _objc_msgSend$setDeviceSessionID:
+ _objc_msgSend$setFlowID:
+ apply_block_1.1503
+ apply_block_2.1538
+ audit_stringAAAFoundation.1210
- -[KCJoiningAcceptSession initWithSecretDelegate:circleDelegate:dsid:rng:error:]
- -[KCJoiningRequestCircleSession initWithCircleDelegate:session:error:]
- -[KCJoiningRequestCircleSession initWithCircleDelegate:session:otcontrol:error:]
- -[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:error:]
- -[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:rng:error:]
- -[KCPairingChannel allPCSItems]
- -[KCPairingChannel fetchPCSItems:]
- -[KCPairingChannel setAllPCSItems:]
- AAAFoundationLibrary.1129
- AAAFoundationLibraryCore.frameworkLibrary.1133
- GCC_except_table115
- GCC_except_table120
- GCC_except_table134
- GCC_except_table136
- GCC_except_table140
- GCC_except_table148
- GCC_except_table149
- GCC_except_table154
- GCC_except_table156
- GCC_except_table165
- GCC_except_table166
- GCC_except_table170
- GCC_except_table182
- GCC_except_table184
- GCC_except_table189
- GCC_except_table191
- GCC_except_table195
- GCC_except_table196
- GCC_except_table202
- GCC_except_table203
- GCC_except_table207
- GCC_except_table209
- GCC_except_table215
- GCC_except_table223
- GCC_except_table230
- GCC_except_table346
- GCC_except_table404
- GCC_except_table411
- GCC_except_table534
- GCC_except_table543
- GCC_except_table545
- GCC_except_table594
- GCC_except_table598
- GCC_except_table603
- GCC_except_table98
- OBJC_IVAR_$_KCPairingChannel._allPCSItems
- _IOConnectCallMethod
- _IOObjectRelease
- _IORegistryEntryFromPath
- _IOServiceClose
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- __34-[KCPairingChannel validateStart:]_block_invoke.410
- __34-[KCPairingChannel validateStart:]_block_invoke.413
- __37-[KCPairingChannel fetchEpoch:error:]_block_invoke.272
- __44-[KCPairingChannel initAsInitiator:version:]_block_invoke.193
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.266
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.267
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.268
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.269
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.270
- __49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.271
- __49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.284
- __49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.285
- __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.275
- __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.276
- __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.277
- __50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.278
- __50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.212
- __50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.213
- __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.233
- __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.234
- __50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.235
- __51-[KCPairingChannel fetchPrepare:application:error:]_block_invoke.227
- __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.237
- __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.240
- __51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.241
- __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.214
- __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.215
- __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.217
- __51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.219
- __66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.220
- __66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.221
- __84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.279
- __84-[KCPairingChannel fetchVoucher:prepare:eventS:finishedPairing:maxCapability:error:]_block_invoke.280
- __88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.231
- __88-[KCPairingChannel join:voucher:eventS:setupPairingChannelSignPost:finishPairing:error:]_block_invoke.232
- __AAAFoundationLibraryCore_block_invoke.1134
- __Block_byref_object_copy_.360
- __Block_byref_object_copy_.874
- __Block_byref_object_dispose_.361
- __Block_byref_object_dispose_.875
- ___get_aks_client_connection_block_invoke
- ___get_aks_client_dispatch_queue_block_invoke
- ___stdoutp
- __block_descriptor_tmp.141
- __block_descriptor_tmp.1418
- __block_descriptor_tmp.1537
- __block_descriptor_tmp.1576
- __block_descriptor_tmp.160
- __block_descriptor_tmp.1612
- __block_descriptor_tmp.17.1448
- __block_descriptor_tmp.73.1450
- __block_literal_global.1149
- __block_literal_global.1381
- __block_literal_global.1447
- __block_literal_global.1574
- __block_literal_global.162
- __block_literal_global.175
- __block_literal_global.202
- __block_literal_global.258
- __block_literal_global.391
- __copy_aks_client_connection
- __create_bag
- _calloc
- _fprintf
- _get_aks_client_connection
- _kIOMasterPortDefault
- _kSecurityRTCEventNameJoin
- _kSecurityRTCEventNameTrustedDeviceListRefresh
- _mach_task_self_
- _memcpy
- _objc_msgSend$allPCSItems
- _objc_msgSend$fetchPCSItems:
- _objc_msgSend$initWithCircleDelegate:session:error:
- _objc_msgSend$initWithCircleDelegate:session:otcontrol:error:
- _objc_msgSend$initWithSecretDelegate:circleDelegate:dsid:rng:error:
- _objc_msgSend$initWithSecretDelegate:dsid:error:
- _objc_msgSend$initWithSecretDelegate:dsid:rng:error:
- _objc_msgSend$setAllPCSItems:
- _objc_msgSend$setCircleDelegate:
- _objc_msgSend$setSecretDelegate:
- apply_block_1.1425
- apply_block_2.1461
- audit_stringAAAFoundation.1136
- get_aks_client_connection.connection
- get_aks_client_dispatch_queue.connection_queue
- get_aks_client_dispatch_queue.onceToken
CStrings:
+ "@64@0:8@16@24@32@40@48^@56"
+ "@64@0:8@16Q24@32@40@48^@56"
+ "@72@0:8@16@24@32@40@48@56^@64"
+ "@72@0:8@16Q24@32@40@48^{ccrng_state=^?}56^@64"
+ "@80@0:8@16@24@32Q40@48@56@64^@72"
+ "@80@0:8@16@24Q32@40@48@56^{ccrng_state=^?}64^@72"
+ "Failed to copy srpMessage"
+ "Failed to copy start message"
+ "Failed to create challenge message"
+ "Failed to create circle blob response message"
+ "Failed to create error response message"
+ "Failed to create response message"
+ "Failed to create response message: %@"
+ "Failed to create tlk request response message"
+ "Failed to decrypt and verify circleBlob"
+ "Failed to decrypt and verify message"
+ "Failed to encode data"
+ "Failed to encrypt encoded data"
+ "Failed to extract startMessage"
+ "Failed to process SOS Application"
+ "Failed to process circle join data"
+ "L"
+ "SecItemCopyMatching: %d"
+ "T@\"NSArray\",&,N,V_allPCSItemPersistentRefs"
+ "T@\"NSString\",&,N,V_altDSID"
+ "T@\"NSString\",&,N,V_deviceSessionID"
+ "T@\"NSString\",&,N,V_flowID"
+ "T@\"NSString\",&,V_deviceSessionID"
+ "T@\"NSString\",&,V_flowID"
+ "TB,N,V_accountIsGuitarfish"
+ "Voucher creation failed"
+ "_accountIsGuitarfish"
+ "_allPCSItemPersistentRefs"
+ "accountIsGuitarfish"
+ "allPCSItemPersistentRefs"
+ "com.apple.security.establish"
+ "com.apple.security.establishOperation"
+ "com.apple.security.fetchAfterEstablish"
+ "com.apple.security.fetchRecoverableTLKShares"
+ "com.apple.security.handleRecoveryResults"
+ "com.apple.security.joinWithVoucherInTPH"
+ "com.apple.security.joinWithVoucherOperation"
+ "com.apple.security.onqueueEstablishTPH"
+ "com.apple.security.pairingFailedToFetchItemForPersistentRef"
+ "com.apple.security.performEscrowRecovery"
+ "com.apple.security.performSilentEscrowRecovery"
+ "com.apple.security.piggybackingAcceptorInitialMessage"
+ "com.apple.security.piggybackingAcceptorProcessApplication"
+ "com.apple.security.piggybackingAcceptorProcessMessage"
+ "com.apple.security.piggybackingCircleInitiatorHandleCircleBlobMessage"
+ "com.apple.security.piggybackingCircleInitiatorInitialMessage"
+ "com.apple.security.piggybackingSessionInitiatorHandleChallenge"
+ "com.apple.security.piggybackingSessionInitiatorHandleVerification"
+ "com.apple.security.piggybackingSessionInitiatorInitialMessage"
+ "com.apple.security.preflightVouchWithBottle"
+ "com.apple.security.recoverSilentWithCDPContext"
+ "com.apple.security.recoverWithCDPContext"
+ "com.apple.security.recoverWithInfo"
+ "com.apple.security.recoveryResultsResetAndEstablish"
+ "com.apple.security.restoreFromBottleEvent"
+ "com.apple.security.restoreKeychainAsyncWithPassword"
+ "com.apple.security.vouchWithBottle"
+ "com.apple.security.vouchWithBottleTPH"
+ "decode from der failed"
+ "decrypt and verify failed"
+ "errorData is nil"
+ "failed to copy response"
+ "failed to create initial message"
+ "failed to create peerinfo response"
+ "failed to create response message"
+ "failed to create version 1 message"
+ "failed to create version 2 message: %@"
+ "failed to create version initial message: %@"
+ "failed to encrypt initial message"
+ "failed to encrypt peer info"
+ "failed to fetch dsid"
+ "failed to fetch persistent ref %@, error: %@, continuing"
+ "failed to handle challenge data"
+ "failed to initial peerinfo message"
+ "fetchItemForPersistentRef: failed to fetch persistent ref: %@"
+ "fetchItemForPersistentRef: unexpected keychain item type fetched for persistent ref: %@, type: %lu"
+ "fetchItemForPersistentRef:error:"
+ "fetchPCSItemPersistentRefs:error:"
+ "i32@0:8r^^v16^@24"
+ "initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:"
+ "initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:"
+ "initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:"
+ "initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:"
+ "joining: Failed to copy response message: %@"
+ "joining: Verification failed: %@, error: %@"
+ "joining: decode from der failed: %@"
+ "joining: decrypt and verify failed: %@"
+ "joining: error preparing identity: %@"
+ "joining: error producing octagon voucher: %@"
+ "joining: expected acceptor epoch! returning nil. error: %@"
+ "joining: expected vertification message type: %@"
+ "joining: failed to create challenge message: %@"
+ "joining: failed to create encrypted peer info: %@"
+ "joining: failed to decrypt and verify circle blob message failed %@"
+ "joining: failed to encrypt initial message: %@"
+ "joining: failed to handle challenge data: %@"
+ "joining: failed to join octagon: %@"
+ "joining: failed to prepare identity: %@"
+ "joining: failed to process SOS circle: %@"
+ "joining: initial message creation failed: %@"
+ "joining: next secret is nil: %@"
+ "missingDigest"
+ "missingPassword"
+ "next secret is nil"
+ "octagon, failed to create pairing message from JoiningMessage: %@"
+ "processResponse: errorData is nil, error: %@"
+ "processResponse: failed to create error response message: %@"
+ "processResponse: successfully created response message"
+ "recordDataMissing"
+ "sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:"
+ "sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "sessionWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "setAccountIsGuitarfish:"
+ "setAllPCSItemPersistentRefs:"
+ "successfully copied response message"
+ "successfully handled challenge data"
+ "totalNumberOfCustodians"
+ "totalNumberOfDistrustedRecoveryKeys"
+ "totalNumberOfPeers"
+ "totalNumberOfPreapprovals"
+ "totalNumberOfRecoveryKeys"
+ "totalNumberOfTrustedCustodians"
+ "totalNumberOfTrustedRecoveryKeys"
+ "unexpected keychain item type fetched for persistent ref"
- "\v"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- ":"
- "@48@0:8@16Q24^{ccrng_state=^?}32^@40"
- "@56@0:8@16@24Q32^{ccrng_state=^?}40^@48"
- "AppleKeyStore"
- "Failed to decrypt circleBlob"
- "IOService:/IOResources/AppleKeyStore"
- "T@\"NSArray\",&,N,V_allPCSItems"
- "Verification failed: %@"
- "_allPCSItems"
- "_create_bag"
- "aks"
- "aks-client-queue"
- "aks_assert_drop"
- "aks_assert_hold"
- "aks_save_bag"
- "aks_unload_bag"
- "allPCSItems"
- "com.apple.security.joinWithVoucher"
- "com.apple.security.trustedDeviceListRefresh"
- "error producing octagon voucher: %@"
- "failed to open connection to %s\n"
- "fetchPCSItems:"
- "i24@0:8r^^v16"
- "initWithCircleDelegate:session:error:"
- "initWithCircleDelegate:session:otcontrol:error:"
- "initWithSecretDelegate:circleDelegate:dsid:rng:error:"
- "initWithSecretDelegate:dsid:error:"
- "initWithSecretDelegate:dsid:rng:error:"
- "joining: circleBlob is nil"
- "joining: expected acceptor epoch! returning nil."
- "joining: failed to process SOS circle"
- "octagon, failed to create pairing message from JoiningMessage"
- "octagon: error preparing identity: %@"
- "request-session"
- "setAllPCSItems:"

```
