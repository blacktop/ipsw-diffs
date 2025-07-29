## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61040.42.1.0.0
-  __TEXT.__text: 0x18398
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x14ec
-  __TEXT.__const: 0x5c
-  __TEXT.__gcc_except_tab: 0xa70
-  __TEXT.__cstring: 0xa28
-  __TEXT.__oslogstring: 0x297f
+61040.62.1.0.0
+  __TEXT.__text: 0x1a62c
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x164c
+  __TEXT.__const: 0x64
+  __TEXT.__gcc_except_tab: 0xb04
+  __TEXT.__cstring: 0x17be
+  __TEXT.__oslogstring: 0x29f3
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x580
-  __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x2e83
-  __TEXT.__objc_methtype: 0xbd2
-  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__dlopen_cstrs: 0xfc
+  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__objc_classname: 0x2e3
+  __TEXT.__objc_methname: 0x33c3
+  __TEXT.__objc_methtype: 0xd94
+  __TEXT.__objc_stubs: 0x25e0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x490
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2090
-  __DATA_CONST.__objc_selrefs: 0xb00
+  __DATA_CONST.__objc_const: 0x2268
+  __DATA_CONST.__objc_selrefs: 0xbf0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0x928
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_const: 0xa00
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH.__objc_data: 0x5a0
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH.__objc_data: 0x640
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x110
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x17c
+  __DATA.__objc_classrefs: 0x120
+  __DATA.__objc_superrefs: 0x88
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x2c8
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53E5B4C7-0D78-3002-BD9F-5443BAEB29AB
-  Functions: 516
-  Symbols:   1823
-  CStrings:  1126
+  UUID: 3D885DF0-DFF8-33BB-945E-CD04042F70A4
+  Functions: 558
+  Symbols:   2085
+  CStrings:  1407
 
Symbols:
+ +[AAFAnalyticsEventSecurity isAAAFoundationAvailable]
+ +[AAFAnalyticsEventSecurity isAuthKitAvailable]
+ +[SecurityAnalyticsReporterRTC rtcAnalyticsReporter]
+ +[SecurityAnalyticsReporterRTC sendMetricWithEvent:success:error:]
+ -[AAFAnalyticsEventSecurity .cxx_destruct]
+ -[AAFAnalyticsEventSecurity addMetrics:]
+ -[AAFAnalyticsEventSecurity areTestsEnabled]
+ -[AAFAnalyticsEventSecurity event]
+ -[AAFAnalyticsEventSecurity getEvent]
+ -[AAFAnalyticsEventSecurity initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:]
+ -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:eventName:category:]
+ -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:]
+ -[AAFAnalyticsEventSecurity isAAAFoundationAvailable]
+ -[AAFAnalyticsEventSecurity isAuthKitAvailable]
+ -[AAFAnalyticsEventSecurity populateUnderlyingErrorsStartingWithRootError:]
+ -[AAFAnalyticsEventSecurity queue]
+ -[AAFAnalyticsEventSecurity setAreTestsEnabled:]
+ -[AAFAnalyticsEventSecurity setEvent:]
+ -[AAFAnalyticsEventSecurity setIsAAAFoundationAvailable:]
+ -[AAFAnalyticsEventSecurity setIsAuthKitAvailable:]
+ -[AAFAnalyticsEventSecurity setQueue:]
+ -[KCPairingChannel altDSID]
+ -[KCPairingChannel setAltDSID:]
+ -[KCPairingChannelContext deviceSessionID]
+ -[KCPairingChannelContext flowID]
+ -[KCPairingChannelContext setDeviceSessionID:]
+ -[KCPairingChannelContext setFlowID:]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table238
+ GCC_except_table296
+ GCC_except_table303
+ GCC_except_table425
+ GCC_except_table434
+ GCC_except_table436
+ GCC_except_table66
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table94
+ _AAAFoundationLibrary
+ _AAAFoundationLibraryCore.frameworkLibrary
+ _AAAFoundationLibraryCore.frameworkLibrary.1061
+ _AuthKitLibraryCore.frameworkLibrary
+ _MetricsDisable
+ _MetricsEnable
+ _MetricsOverrideTestsAreEnabled
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._areTestsEnabled
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._event
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._isAAAFoundationAvailable
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._isAuthKitAvailable
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._queue
+ _OBJC_IVAR_$_KCPairingChannel._altDSID
+ _OBJC_IVAR_$_KCPairingChannelContext._deviceSessionID
+ _OBJC_IVAR_$_KCPairingChannelContext._flowID
+ _OBJC_METACLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_METACLASS_$_SecurityAnalyticsReporterRTC
+ __OBJC_$_CLASS_METHODS_AAFAnalyticsEventSecurity
+ __OBJC_$_CLASS_METHODS_SecurityAnalyticsReporterRTC
+ __OBJC_$_INSTANCE_METHODS_AAFAnalyticsEventSecurity
+ __OBJC_$_INSTANCE_VARIABLES_AAFAnalyticsEventSecurity
+ __OBJC_$_PROP_LIST_AAFAnalyticsEventSecurity
+ __OBJC_CLASS_RO_$_AAFAnalyticsEventSecurity
+ __OBJC_CLASS_RO_$_SecurityAnalyticsReporterRTC
+ __OBJC_METACLASS_RO_$_AAFAnalyticsEventSecurity
+ __OBJC_METACLASS_RO_$_SecurityAnalyticsReporterRTC
+ ___40-[AAFAnalyticsEventSecurity addMetrics:]_block_invoke
+ ___47+[AAFAnalyticsEventSecurity isAuthKitAvailable]_block_invoke
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.206
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.207
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.208
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.209
+ ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.210
+ ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.221
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.214
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.215
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.216
+ ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.217
+ ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.160
+ ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.169
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.199
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.200
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.201
+ ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.202
+ ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.204
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.177
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.178
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.180
+ ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.182
+ ___52+[SecurityAnalyticsReporterRTC rtcAnalyticsReporter]_block_invoke
+ ___53+[AAFAnalyticsEventSecurity isAAAFoundationAvailable]_block_invoke
+ ___62-[KCPairingChannel acceptorFirstOctagonPacket:reply:complete:]_block_invoke.211
+ ___63-[KCPairingChannel acceptorSecondOctagonPacket:reply:complete:]_block_invoke.218
+ ___66+[SecurityAnalyticsReporterRTC sendMetricWithEvent:success:error:]_block_invoke
+ ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.183
+ ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.187
+ ___75-[AAFAnalyticsEventSecurity populateUnderlyingErrorsStartingWithRootError:]_block_invoke
+ ___78-[KCPairingChannel initiatorCompleteSecondPacketOctagon:application:complete:]_block_invoke.194
+ ___AAAFoundationLibraryCore_block_invoke
+ ___AAAFoundationLibraryCore_block_invoke.1062
+ ___AuthKitLibraryCore_block_invoke
+ ___Block_byref_object_copy_.391
+ ___Block_byref_object_copy_.822
+ ___Block_byref_object_dispose_.392
+ ___Block_byref_object_dispose_.823
+ ___block_descriptor_112_e8_32s40s48bs56r64r72w_e20_v20?0B8"NSError"12lr56l8s32l8r64l8s40l8s48l8w72l8
+ ___block_descriptor_112_e8_32s40s48s56bs64r72r_e20_v20?0B8"NSError"12lr64l8s32l8r72l8s40l8s56l8s48l8
+ ___block_descriptor_128_e8_32s40s48s56bs64r72r80r88w_e28_v24?0"NSData"8"NSError"16lr64l8s32l8r72l8s40l8r80l8s48l8s56l8w88l8
+ ___block_descriptor_128_e8_32s40s48s56s64bs72r80r88w_e28_v24?0"NSData"8"NSError"16lr72l8s32l8s40l8s48l8r80l8s56l8s64l8w88l8
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r_e37_v28?0B8"NSDictionary"12"NSError"20lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e39_v32?0"NSData"8"NSData"16"NSError"24ls32l8s40l8s56l8w64l8s48l8
+ ___block_descriptor_80_e8_32s40s48bs56r_e20_v20?0B8"NSError"12ls32l8r56l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48bs56r64w_e17_v16?0"NSError"8ls32l8r56l8s40l8s48l8w64l8
+ ___block_descriptor_96_e8_32s40bs48r56r_e17_v16?0"NSError"8lr48l8r56l8s32l8s40l8
+ ___block_literal_global.1059
+ ___block_literal_global.19
+ ___block_literal_global.409
+ ___getAAFAnalyticsReporterClass_block_invoke
+ ___getAAFAnalyticsTransportRTCClass_block_invoke
+ __sl_dlopen
+ __unnamed_array_storage.155
+ __unnamed_array_storage.157
+ __unnamed_array_storage.158
+ __unnamed_array_storage.162
+ __unnamed_array_storage.163
+ __unnamed_array_storage.166
+ __unnamed_array_storage.167
+ __unnamed_array_storage.171
+ __unnamed_array_storage.172
+ _abort_report_np
+ _audit_stringAAAFoundation
+ _audit_stringAAAFoundation.1065
+ _audit_stringAuthKit
+ _dispatch_sync
+ _getAAFAnalyticsReporterClass.softClass
+ _getAAFAnalyticsTransportRTCClass.softClass
+ _isAAAFoundationAvailable.available
+ _isAAAFoundationAvailable.onceToken
+ _isAuthKitAvailable.available
+ _isAuthKitAvailable.onceToken
+ _kSecurityRTCClientBundleIdentifier
+ _kSecurityRTCClientName
+ _kSecurityRTCClientNameDNU
+ _kSecurityRTCClientType
+ _kSecurityRTCEventCategoryAccountDataAccessRecovery
+ _kSecurityRTCEventNameAcceptorCreatesPacket2
+ _kSecurityRTCEventNameAcceptorCreatesPacket4
+ _kSecurityRTCEventNameAcceptorCreatesPacket5
+ _kSecurityRTCEventNameAcceptorCreatesVoucher
+ _kSecurityRTCEventNameAcceptorFetchesInitialSyncData
+ _kSecurityRTCEventNameCKAccountLogin
+ _kSecurityRTCEventNameCKKSTlkFetch
+ _kSecurityRTCEventNameCloudKitAccountAvailability
+ _kSecurityRTCEventNameContentSyncFinish
+ _kSecurityRTCEventNameCreateMissingTLKShares
+ _kSecurityRTCEventNameCreateSOSCircleBlob
+ _kSecurityRTCEventNameCreatesSOSApplication
+ _kSecurityRTCEventNameDeviceLocked
+ _kSecurityRTCEventNameDeviceUnlocked
+ _kSecurityRTCEventNameFetchAndPersistChanges
+ _kSecurityRTCEventNameFetchMachineID
+ _kSecurityRTCEventNameFetchPolicyDocument
+ _kSecurityRTCEventNameFirstManateeKeyFetch
+ _kSecurityRTCEventNameFixMismatchedViewItems
+ _kSecurityRTCEventNameFlush
+ _kSecurityRTCEventNameHealBrokenRecords
+ _kSecurityRTCEventNameHealKeyHierarchy
+ _kSecurityRTCEventNameHealTLKShares
+ _kSecurityRTCEventNameIdMSSecurityLevel
+ _kSecurityRTCEventNameInitiatorCreatesPacket1
+ _kSecurityRTCEventNameInitiatorCreatesPacket3
+ _kSecurityRTCEventNameInitiatorImportsInitialSyncData
+ _kSecurityRTCEventNameInitiatorJoinsSOS
+ _kSecurityRTCEventNameInitiatorJoinsTrustSystems
+ _kSecurityRTCEventNameInitiatorWaitsForUpgrade
+ _kSecurityRTCEventNameJoin
+ _kSecurityRTCEventNameKVSSyncAndWait
+ _kSecurityRTCEventNameLaunchStart
+ _kSecurityRTCEventNameLoadAndProcessIQEs
+ _kSecurityRTCEventNameLocalReset
+ _kSecurityRTCEventNameLocalSyncFinish
+ _kSecurityRTCEventNameNumberOfTrustedOctagonPeers
+ _kSecurityRTCEventNameOnboardMissingItems
+ _kSecurityRTCEventNamePreApprovedJoin
+ _kSecurityRTCEventNamePrepareIdentityInTPH
+ _kSecurityRTCEventNamePrimaryAccountAdded
+ _kSecurityRTCEventNameProcessIncomingQueue
+ _kSecurityRTCEventNameProcessOutgoingQueue
+ _kSecurityRTCEventNameProcessReceivedKeys
+ _kSecurityRTCEventNameQuerySyncableItems
+ _kSecurityRTCEventNameSaveCKMirrorEntries
+ _kSecurityRTCEventNameScanLocalItems
+ _kSecurityRTCEventNameSyncingPolicySet
+ _kSecurityRTCEventNameTrustGain
+ _kSecurityRTCEventNameTrustLoss
+ _kSecurityRTCEventNameTrustedDeviceListRefresh
+ _kSecurityRTCEventNameUpdateTDL
+ _kSecurityRTCEventNameUpdateTrust
+ _kSecurityRTCEventNameUploadHealedTLKShares
+ _kSecurityRTCEventNameUploadMissingTLKShares
+ _kSecurityRTCEventNameUploadOQEsToCK
+ _kSecurityRTCEventNameValidatedStashedAccountCredential
+ _kSecurityRTCEventNameVerifySOSApplication
+ _kSecurityRTCEventNameZoneChangeFetch
+ _kSecurityRTCEventNameZoneCreation
+ _kSecurityRTCFieldAccountAvailability
+ _kSecurityRTCFieldDidSucceed
+ _kSecurityRTCFieldErrorItemsProcessed
+ _kSecurityRTCFieldEventName
+ _kSecurityRTCFieldFetchReasons
+ _kSecurityRTCFieldFullFetch
+ _kSecurityRTCFieldFullRefetchNeeded
+ _kSecurityRTCFieldIsFullUpload
+ _kSecurityRTCFieldIsLocked
+ _kSecurityRTCFieldIsPrioritized
+ _kSecurityRTCFieldItemsScanned
+ _kSecurityRTCFieldItemsToAdd
+ _kSecurityRTCFieldItemsToDelete
+ _kSecurityRTCFieldItemsToModify
+ _kSecurityRTCFieldMissingKey
+ _kSecurityRTCFieldNeedsReencryption
+ _kSecurityRTCFieldNewItemsScanned
+ _kSecurityRTCFieldNewTLKShares
+ _kSecurityRTCFieldNumCKRecords
+ _kSecurityRTCFieldNumKeychainItems
+ _kSecurityRTCFieldNumLocalRecords
+ _kSecurityRTCFieldNumMismatchedItems
+ _kSecurityRTCFieldNumRemoteKeys
+ _kSecurityRTCFieldNumViews
+ _kSecurityRTCFieldNumViewsWithNewEntries
+ _kSecurityRTCFieldNumberOfBluetoothMigrationItemsFetched
+ _kSecurityRTCFieldNumberOfKeychainItemsAdded
+ _kSecurityRTCFieldNumberOfKeychainItemsCollected
+ _kSecurityRTCFieldNumberOfPCSItemsFetched
+ _kSecurityRTCFieldNumberOfTLKsFetched
+ _kSecurityRTCFieldNumberOfTrustedPeers
+ _kSecurityRTCFieldOctagonSignInResult
+ _kSecurityRTCFieldPartialFailure
+ _kSecurityRTCFieldPendingClassA
+ _kSecurityRTCFieldPolicyFreshness
+ _kSecurityRTCFieldRetryAttemptCount
+ _kSecurityRTCFieldSecurityLevel
+ _kSecurityRTCFieldSuccessfulItemsProcessed
+ _kSecurityRTCFieldSupportedTrustSystem
+ _kSecurityRTCFieldSyncingPolicy
+ _kSecurityRTCFieldTotalRetryDuration
+ _kSecurityRTCFieldTrustStatus
+ _metricsAreEnabled
+ _objc_enumerationMutation
+ _objc_getClass
+ _objc_msgSend$addMetrics:
+ _objc_msgSend$allKeys
+ _objc_msgSend$analyticsReporterWithTransport:
+ _objc_msgSend$analyticsTransportRTCWithClientType:clientBundleId:clientName:
+ _objc_msgSend$areTestsEnabled
+ _objc_msgSend$circleJoiningBlob:flowID:deviceSessionID:applicant:complete:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$deviceSessionID
+ _objc_msgSend$event
+ _objc_msgSend$flowID
+ _objc_msgSend$getEvent
+ _objc_msgSend$initWithAltDSID:flowID:deviceSessionID:
+ _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:
+ _objc_msgSend$initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:
+ _objc_msgSend$isAAAFoundationAvailable
+ _objc_msgSend$isAuthKitAvailable
+ _objc_msgSend$joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:
+ _objc_msgSend$myPeerInfo:flowID:deviceSessionID:complete:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$peerVersionContext
+ _objc_msgSend$populateUnderlyingErrorsStartingWithRootError:
+ _objc_msgSend$queue
+ _objc_msgSend$rtcAnalyticsReporter
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$sendMetricWithEvent:success:error:
+ _objc_msgSend$stashAccountCredential:altDSID:flowID:deviceSessionID:complete:
+ _objc_msgSend$validatedStashedAccountCredential:flowID:deviceSessionID:complete:
+ _objc_setProperty_nonatomic_copy
+ _rtcAnalyticsReporter.onceToken
+ _rtcAnalyticsReporter.rtcReporter
- GCC_except_table103
- GCC_except_table107
- GCC_except_table124
- GCC_except_table282
- GCC_except_table289
- GCC_except_table408
- GCC_except_table417
- GCC_except_table419
- GCC_except_table60
- GCC_except_table71
- GCC_except_table74
- GCC_except_table75
- GCC_except_table79
- GCC_except_table84
- GCC_except_table86
- GCC_except_table88
- GCC_except_table93
- GCC_except_table96
- GCC_except_table98
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.187
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.188
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.189
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.190
- ___49-[KCPairingChannel acceptorFirstPacket:complete:]_block_invoke.191
- ___49-[KCPairingChannel acceptorThirdPacket:complete:]_block_invoke.202
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.195
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.196
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.197
- ___50-[KCPairingChannel acceptorSecondPacket:complete:]_block_invoke.198
- ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.140
- ___50-[KCPairingChannel initiatorFirstPacket:complete:]_block_invoke.149
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.180
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.181
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.182
- ___50-[KCPairingChannel initiatorThirdPacket:complete:]_block_invoke.183
- ___51-[KCPairingChannel initiatorFourthPacket:complete:]_block_invoke.185
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.157
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.158
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.160
- ___51-[KCPairingChannel initiatorSecondPacket:complete:]_block_invoke.162
- ___62-[KCPairingChannel acceptorFirstOctagonPacket:reply:complete:]_block_invoke.192
- ___63-[KCPairingChannel acceptorSecondOctagonPacket:reply:complete:]_block_invoke.199
- ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.163
- ___66-[KCPairingChannel initiatorCompleteSecondPacketWithSOS:complete:]_block_invoke.168
- ___78-[KCPairingChannel initiatorCompleteSecondPacketOctagon:application:complete:]_block_invoke.175
- ___Block_byref_object_copy_.398
- ___Block_byref_object_copy_.714
- ___Block_byref_object_dispose_.399
- ___Block_byref_object_dispose_.715
- ___block_descriptor_104_e8_32s40bs48r56r64w_e20_v20?0B8"NSError"12lr48l8s32l8r56l8s40l8w64l8
- ___block_descriptor_104_e8_32s40s48bs56r64r_e20_v20?0B8"NSError"12lr56l8s32l8r64l8s48l8s40l8
- ___block_descriptor_120_e8_32s40s48bs56r64r72r80w_e28_v24?0"NSData"8"NSError"16lr56l8s32l8r64l8s40l8r72l8s48l8w80l8
- ___block_descriptor_120_e8_32s40s48s56bs64r72r80w_e28_v24?0"NSData"8"NSError"16lr64l8s32l8s40l8s48l8r72l8s56l8w80l8
- ___block_descriptor_64_e8_32bs40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
- ___block_descriptor_64_e8_32bs40r_e37_v28?0B8"NSDictionary"12"NSError"20lr40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e39_v32?0"NSData"8"NSData"16"NSError"24ls32l8s48l8w56l8s40l8
- ___block_descriptor_72_e8_32s40bs48r_e20_v20?0B8"NSError"12ls32l8r48l8s40l8
- ___block_descriptor_80_e8_32s40bs48r56w_e17_v16?0"NSError"8ls32l8r48l8s40l8w56l8
- ___block_descriptor_88_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
- ___block_literal_global.416
- __unnamed_array_storage.135
- __unnamed_array_storage.137
- __unnamed_array_storage.138
- __unnamed_array_storage.142
- __unnamed_array_storage.143
- __unnamed_array_storage.146
- __unnamed_array_storage.147
- __unnamed_array_storage.151
- __unnamed_array_storage.152
- _objc_msgSend$circleJoiningBlob:complete:
- _objc_msgSend$initialSyncCredentials:complete:
- _objc_msgSend$joinCircleWithBlob:version:complete:
- _objc_msgSend$myPeerInfo:
- _objc_msgSend$stashAccountCredential:complete:
- _objc_msgSend$validatedStashedAccountCredential:
CStrings:
+ "\n"
+ "\x12"
+ "%s"
+ "("
+ "@\"AAFAnalyticsEvent\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@48@0:8@16@24@32@40"
+ "@52@0:8@16@24@32B40@44"
+ "@68@0:8@16@24@32@40@48B56@60"
+ "AAFAnalyticsEventSecurity"
+ "AAFAnalyticsReporter"
+ "AAFAnalyticsTransportRTC"
+ "SecurityAnalyticsReporterRTC"
+ "T@\"AAFAnalyticsEvent\",&,V_event"
+ "T@\"KCPairingChannelContext\",&,N,V_peerVersionContext"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSString\",C,N,V_altDSID"
+ "T@\"NSString\",C,N,V_deviceSessionID"
+ "T@\"NSString\",C,N,V_flowID"
+ "T@\"NSString\",C,N,V_intent"
+ "T@\"NSString\",C,N,V_model"
+ "T@\"NSString\",C,N,V_modelClass"
+ "T@\"NSString\",C,N,V_modelVersion"
+ "T@\"NSString\",C,N,V_osVersion"
+ "T@\"NSString\",C,N,V_uniqueClientID"
+ "T@\"NSString\",C,N,V_uniqueDeviceID"
+ "TB,V_areTestsEnabled"
+ "TB,V_isAAAFoundationAvailable"
+ "TB,V_isAuthKitAvailable"
+ "Unable to find class %s"
+ "_areTestsEnabled"
+ "_deviceSessionID"
+ "_event"
+ "_flowID"
+ "_isAAAFoundationAvailable"
+ "_isAuthKitAvailable"
+ "_queue"
+ "aafanalyticsevent-security: failed to softlink AAAFoundation"
+ "aafanalyticsevent-security: failed to softlink AuthKit"
+ "accountAvailability"
+ "addMetrics:"
+ "allKeys"
+ "analyticsReporterWithTransport:"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "areTestsEnabled"
+ "circleJoiningBlob:flowID:deviceSessionID:applicant:complete:"
+ "com.apple.aaa"
+ "com.apple.aaa.dnu"
+ "com.apple.security.acceptorCreatesPacket2"
+ "com.apple.security.acceptorCreatesPacket4"
+ "com.apple.security.acceptorCreatesPacket5"
+ "com.apple.security.acceptorCreatesVoucher"
+ "com.apple.security.acceptorFetchesInitialSyncData"
+ "com.apple.security.cKKSTLKFetch"
+ "com.apple.security.ckks.CKAccountLogin"
+ "com.apple.security.ckks.contentSyncFinish"
+ "com.apple.security.ckks.deviceLocked"
+ "com.apple.security.ckks.deviceUnlocked"
+ "com.apple.security.ckks.firstManateeKeyFetch"
+ "com.apple.security.ckks.healKeyHierarchy"
+ "com.apple.security.ckks.healKeyHierarchy.healBrokenRecords"
+ "com.apple.security.ckks.healKeyHierarchy.uploadHealedTLKShares"
+ "com.apple.security.ckks.healTLKShares"
+ "com.apple.security.ckks.healTLKShares.createMissingTLKShares"
+ "com.apple.security.ckks.healTLKShares.uploadMissingTLKShares"
+ "com.apple.security.ckks.launchStart"
+ "com.apple.security.ckks.localReset"
+ "com.apple.security.ckks.localSyncFinish"
+ "com.apple.security.ckks.processIncomingQueue"
+ "com.apple.security.ckks.processIncomingQueue.fixMismatchedViewItems"
+ "com.apple.security.ckks.processIncomingQueue.loadAndProcessIQEs"
+ "com.apple.security.ckks.processOutgoingQueue"
+ "com.apple.security.ckks.processOutgoingQueue.saveCKMirrorEntries"
+ "com.apple.security.ckks.processOutgoingQueue.uploadOQEstoCK"
+ "com.apple.security.ckks.processReceivedKeys"
+ "com.apple.security.ckks.scanLocalItems"
+ "com.apple.security.ckks.scanLocalItems.onboardMissingItems"
+ "com.apple.security.ckks.scanLocalItems.querySyncableItems"
+ "com.apple.security.ckks.syncingPolicySet"
+ "com.apple.security.ckks.trustGain"
+ "com.apple.security.ckks.trustLoss"
+ "com.apple.security.ckks.zoneChangeFetch"
+ "com.apple.security.ckks.zoneCreation"
+ "com.apple.security.cloudKitAccountAvailability"
+ "com.apple.security.createSOSApplication"
+ "com.apple.security.createSOSCircleBlob"
+ "com.apple.security.fetchAndPersistChanges"
+ "com.apple.security.fetchMachineID"
+ "com.apple.security.fetchPolicyDocument"
+ "com.apple.security.flush"
+ "com.apple.security.idMSSecurityLevel"
+ "com.apple.security.initiatorCreatesPacket1"
+ "com.apple.security.initiatorCreatesPacket3"
+ "com.apple.security.initiatorImportsInitialSyncData"
+ "com.apple.security.initiatorJoinSOS"
+ "com.apple.security.initiatorJoinsTrustSystems"
+ "com.apple.security.initiatorWaitsForUpgrade"
+ "com.apple.security.joinWithVoucher"
+ "com.apple.security.kVSSyncAndWait"
+ "com.apple.security.numberOfTrustedOctagonPeers"
+ "com.apple.security.preApprovedJoin"
+ "com.apple.security.prepareIdentityInTPH"
+ "com.apple.security.primaryAccountAdded"
+ "com.apple.security.trustedDeviceListRefresh"
+ "com.apple.security.updateTDL"
+ "com.apple.security.updateTrust"
+ "com.apple.security.validatedStashedAccountCredential"
+ "com.apple.security.verifySOSApplication"
+ "com.apple.securityd"
+ "countByEnumeratingWithState:objects:count:"
+ "deviceSessionID"
+ "didSucceed"
+ "errorItemsProcessed"
+ "event"
+ "eventName"
+ "fetchReasons"
+ "flowID"
+ "fullFetch"
+ "fullRefetchNeeded"
+ "getEvent"
+ "initWithAltDSID:flowID:deviceSessionID:"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
+ "initWithKeychainCircleMetrics:altDSID:eventName:category:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
+ "initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:"
+ "isAAAFoundationAvailable"
+ "isAuthKitAvailable"
+ "isFullUpload"
+ "isLocked"
+ "isPrioritized"
+ "itemsScanned"
+ "itemsToAdd"
+ "itemsToDelete"
+ "itemsToModify"
+ "joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:"
+ "missingKey"
+ "myPeerInfo:flowID:deviceSessionID:complete:"
+ "needsReencryption"
+ "newItemsScanned"
+ "newTLKShares"
+ "numCKRecords"
+ "numKeychainItems"
+ "numLocalRecords"
+ "numMismatchedItems"
+ "numRemoteKeys"
+ "numViews"
+ "numViewsWithNewEntries"
+ "numberOfBluetoothMigrationItemsFetched"
+ "numberOfKeychainItemsAdded"
+ "numberOfKeychainItemsCollected"
+ "numberOfPCSItemsFetched"
+ "numberOfTLKsFetched"
+ "numberOfTrustedPeers"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "octagonSignInResult"
+ "partialFailure"
+ "pendingClassAEntries"
+ "policyFreshness"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "queue"
+ "retryAttemptCount"
+ "rtcAnalyticsReporter"
+ "securityLevel"
+ "sendEvent:"
+ "sendMetricWithEvent:success:error:"
+ "setAreTestsEnabled:"
+ "setDeviceSessionID:"
+ "setEvent:"
+ "setFlowID:"
+ "setIsAAAFoundationAvailable:"
+ "setIsAuthKitAvailable:"
+ "setQueue:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "stashAccountCredential:altDSID:flowID:deviceSessionID:complete:"
+ "successfulItemsProcessed"
+ "supportedTrustSystem"
+ "syncingPolicy"
+ "totalRetryDuration"
+ "trustStatus"
+ "v36@0:8@16B24@28"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36@?<v@?@\"NSArray\"@\"NSError\">44"
+ "v52@0:8I16@20@28@36@?44"
+ "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40i48@?<v@?B@\"NSError\">52"
+ "v60@0:8@16@24@32@40i48@?52"
+ "validatedStashedAccountCredential:flowID:deviceSessionID:complete:"
- "\b"
- "6"
- "T@\"KCPairingChannelContext\",V_peerVersionContext"
- "T@\"NSString\",&,V_intent"
- "T@\"NSString\",&,V_model"
- "T@\"NSString\",&,V_modelClass"
- "T@\"NSString\",&,V_modelVersion"
- "T@\"NSString\",&,V_osVersion"
- "T@\"NSString\",&,V_uniqueClientID"
- "T@\"NSString\",&,V_uniqueDeviceID"
- "circleJoiningBlob:complete:"
- "initialSyncCredentials:complete:"
- "joinCircleWithBlob:version:complete:"
- "myPeerInfo:"
- "stashAccountCredential:complete:"
- "v28@0:8I16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSData\"16i24@?<v@?B@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "validatedStashedAccountCredential:"

```
