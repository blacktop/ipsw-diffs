## seserviced

> `/usr/libexec/seserviced`

```diff

-63.2.1.0.0
-  __TEXT.__text: 0x3f81f8
-  __TEXT.__auth_stubs: 0x4a90
+64.20.2.0.0
+  __TEXT.__text: 0x4343a8
+  __TEXT.__auth_stubs: 0x4b70
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x33c
-  __TEXT.__objc_stubs: 0x9e00
-  __TEXT.__objc_methlist: 0x666c
-  __TEXT.__const: 0x114b8
-  __TEXT.__gcc_except_tab: 0x3734
-  __TEXT.__objc_methname: 0x13207
-  __TEXT.__oslogstring: 0x2ad2d
-  __TEXT.__cstring: 0x23922
-  __TEXT.__objc_classname: 0x11d8
-  __TEXT.__objc_methtype: 0x6722
-  __TEXT.__swift5_typeref: 0x4df8
-  __TEXT.__constg_swiftt: 0x5060
-  __TEXT.__swift5_reflstr: 0x562a
-  __TEXT.__swift5_fieldmd: 0x5588
-  __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_assocty: 0x768
-  __TEXT.__swift5_capture: 0x2444
-  __TEXT.__swift5_proto: 0x880
-  __TEXT.__swift5_types: 0x55c
-  __TEXT.__swift_as_entry: 0x384
-  __TEXT.__swift_as_ret: 0x518
+  __TEXT.__objc_stubs: 0xd5e0
+  __TEXT.__objc_methlist: 0x681c
+  __TEXT.__const: 0x119c8
+  __TEXT.__gcc_except_tab: 0x358c
+  __TEXT.__objc_methname: 0x1733b
+  __TEXT.__oslogstring: 0x2b690
+  __TEXT.__cstring: 0x1e539
+  __TEXT.__objc_classname: 0x2bca
+  __TEXT.__objc_methtype: 0x766f
+  __TEXT.__swift5_typeref: 0x4eb2
+  __TEXT.__constg_swiftt: 0x5164
+  __TEXT.__swift5_reflstr: 0x569a
+  __TEXT.__swift5_fieldmd: 0x5658
+  __TEXT.__swift5_builtin: 0x348
+  __TEXT.__swift5_assocty: 0x798
+  __TEXT.__swift5_capture: 0x248c
+  __TEXT.__swift5_proto: 0x8d4
+  __TEXT.__swift5_types: 0x574
+  __TEXT.__swift_as_entry: 0x398
+  __TEXT.__swift_as_ret: 0x53c
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0xa0
-  __TEXT.__unwind_info: 0x99c8
-  __TEXT.__eh_frame: 0x13414
-  __DATA_CONST.__auth_got: 0x2560
-  __DATA_CONST.__got: 0x15f8
-  __DATA_CONST.__auth_ptr: 0xe08
-  __DATA_CONST.__const: 0x122d0
-  __DATA_CONST.__cfstring: 0x8ea0
-  __DATA_CONST.__objc_classlist: 0x798
+  __TEXT.__unwind_info: 0x9cf8
+  __TEXT.__eh_frame: 0x12e84
+  __DATA_CONST.__auth_got: 0x25d0
+  __DATA_CONST.__got: 0x1d48
+  __DATA_CONST.__auth_ptr: 0xe88
+  __DATA_CONST.__const: 0x124e8
+  __DATA_CONST.__cfstring: 0x7ec0
+  __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x360
   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__objc_intobj: 0x810
-  __DATA.__objc_const: 0x15f58
-  __DATA.__objc_selrefs: 0x44c0
-  __DATA.__objc_ivar: 0xb3c
-  __DATA.__objc_data: 0x65f0
-  __DATA.__data: 0xc004
-  __DATA.__bss: 0xf300
-  __DATA.__common: 0x708
+  __DATA_CONST.__objc_intobj: 0x840
+  __DATA.__objc_const: 0x163e0
+  __DATA.__objc_selrefs: 0x4588
+  __DATA.__objc_ivar: 0xb7c
+  __DATA.__objc_data: 0x6750
+  __DATA.__data: 0xc214
+  __DATA.__bss: 0xfd90
+  __DATA.__common: 0x718
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess
+  - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Proximity.framework/Proximity
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SESShared.framework/SESShared
   - /System/Library/PrivateFrameworks/SESUIServiceCore.framework/SESUIServiceCore
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient

   - /usr/lib/libFDR.dylib
   - /usr/lib/libFDRDecode.dylib
   - /usr/lib/libMobileGestalt.dylib
-  - /usr/lib/libSESShared.dylib
   - /usr/lib/libSLAMDynamic.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyCapabilities.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 45B8E85A-3E10-3CCB-B074-B446F94F1CC2
-  Functions: 11711
-  Symbols:   2115
-  CStrings:  11954
+  UUID: 5F0444E6-C7AF-375D-B065-D84E071E04FA
+  Functions: 11890
+  Symbols:   2366
+  CStrings:  11824
 
Symbols:
+ _$s13OSEligibility0A6AnswerO11notEligibleyA2CmFWC
+ _$s13OSEligibility0A6AnswerO15notYetAvailableyA2CmFWC
+ _$s13OSEligibility0A6AnswerO5maybeyA2CmFWC
+ _$s13OSEligibility0A6AnswerOMn
+ _$s13OSEligibility0A6AnswerOSHAAMc
+ _$s13OSEligibility0A6AnswerOSQAAMc
+ _$s15FeedbackService17FBKSDraftLauncherC07collectA019launchConfigurationyAA010FBKSLaunchG0CSg_tYaKFTjTu
+ _$s15FeedbackService17FBKSDraftLauncherC12feedbackFormAcA8FBKSFormC_tcfc
+ _$s15FeedbackService17FBKSDraftLauncherCMa
+ _$s15FeedbackService17FBKSDraftLauncherCMn
+ _$s15FeedbackService23FBKSLaunchConfigurationC11promptStyleAA010FBKSPromptF0OvsTj
+ _$s15FeedbackService23FBKSLaunchConfigurationC17notifyImmediatelySbSgvsTj
+ _$s15FeedbackService23FBKSLaunchConfigurationC20localizedPromptTitleSSSgvsTj
+ _$s15FeedbackService23FBKSLaunchConfigurationC22localizedPromptMessageSSSgvsTj
+ _$s15FeedbackService23FBKSLaunchConfigurationCMa
+ _$s15FeedbackService23FBKSLaunchConfigurationCMn
+ _$s15FeedbackService8FBKSFormC10identifierACSS_tcfc
+ _$s15FeedbackService8FBKSFormC20authenticationMethodAC014AuthenticationE0OvsTj
+ _$s15FeedbackService8FBKSFormC7prefill8question6answeryAC8QuestionO_SStFTj
+ _$s15FeedbackService8FBKSFormC8QuestionO6customyAESScAEmFWC
+ _$s15FeedbackService8FBKSFormC8QuestionOMa
+ _$s15FeedbackService8FBKSFormCMa
+ _$s8Dispatch0A3QoSV7utilityACvgZ
+ _$s9SEService10MemoryTypeO5pHeapyA2CmFWC
+ _$s9SEService10MemoryTypeOMa
+ _$s9SEService10SESnapshotC12CanFitResultO7successyA2EmFWC
+ _$s9SEService10SESnapshotC12CanFitResultOMa
+ _$s9SEService10SESnapshotC12CanFitResultOSQAAMc
+ _$s9SEService10SESnapshotC16canFitWithReason13proposedUsageAC03CanD6ResultOAA06MemoryH0C_tF
+ _$s9SEService10SESnapshotC16canFitWithReason25proposedESimProfilesUsageAC03CanD6ResultOAA06MemoryJ0C_tF
+ _$s9SEService11ReservationC4typeAA14CredentialTypeOvg
+ _$s9SEService11ReservationC4uuid10Foundation4UUIDVvg
+ _$s9SEService11SECMetadataV15credentialTypes15appletInstances12friendlyName20isIdentityOnlineMdocACSS_SayAA17SECCredentialInfoVGSSSbtcfC
+ _$s9SEService11SECMetadataV20isIdentityOnlineMdocSbvg
+ _$s9SEService13StateInternalO12DiscriminantOSQAAMc
+ _$s9SEService14CredentialTypeO11descriptionSSvg
+ _$s9SEService14CredentialTypeO13packageMemory06memoryC08snapshotSiAA0eC0O_AA10SESnapshotCtKF
+ _$s9SEService14CredentialTypeO15containerMemory06memoryC08snapshotSiAA0eC0O_AA10SESnapshotCtKF
+ _$s9SEService14CredentialTypeO16selectableMemory06memoryC08snapshotSiAA0eC0O_AA10SESnapshotCtKF
+ _$s9SEService14CredentialTypeO18personalizedMemory06memoryC08snapshotSiAA0eC0O_AA10SESnapshotCtKF
+ _$s9SEService14SERXPCResponseO6canFityAcA10SESnapshotC03CanD6ResultOcACmFWC
+ _$s9SEService17SECCredentialInfoVSEAAMc
+ _$s9SEService17SECCredentialInfoVSeAAMc
+ _$s9SEService18CredentialInternalC10identifier12friendlyName17ownerApplications04userH05state10configUUID11accessLevel12lastUsedDate23supportsMdocPresentmentAC10Foundation0L0V_SSSayAA015ApplicationInfoC0CGArA05StateC0OAoA06AccessnC0OAM0Q0VSgSbtcfCTj
+ _$s9SEService18CredentialInternalC23supportsMdocPresentmentSbvg
+ _$s9SEService23ApplicationInfoInternalC16gdprShownVersionSivg
+ _$s9SEService6SETypeOSQAAMc
+ _$sSK17_StringProcessingSs11SubSequenceRtzrlE6starts4withSbqd___tAA14RegexComponentRd__lF
+ _$sSS17_StringProcessing14RegexComponent0C7BuilderMc
+ _$sSSSKsMc
+ _$sSo8NSObjectCs7CVarArg10ObjectiveCMc
+ _$ss15ContiguousArrayV28_allocateBufferUninitialized15minimumCapacitys01_abD0VyxGSi_tFZ
+ _CA_AliroAnalyticsBtConnectionDuration
+ _CA_AliroAnalyticsBtOutOfOrderMessageCount
+ _CA_AliroAnalyticsBtTimeExtensionInitiatedByDeviceCount
+ _CA_AliroAnalyticsBtTimeExtensionInitiatedByLockCount
+ _CA_AliroAnalyticsDeviceInitatedRangingAttemptsCount
+ _CA_AliroAnalyticsDeviceStatus
+ _CA_AliroAnalyticsDisconnectReason
+ _CA_AliroAnalyticsInfoFWVersion
+ _CA_AliroAnalyticsInfoProductID
+ _CA_AliroAnalyticsInfoVendorID
+ _CA_AliroAnalyticsIntentFallbackTriggered
+ _CA_AliroAnalyticsKeyType
+ _CA_AliroAnalyticsLockCapability
+ _CA_AliroAnalyticsLockSharingCapability
+ _CA_AliroAnalyticsLockStatus
+ _CA_AliroAnalyticsLockStatusAtConnection
+ _CA_AliroAnalyticsRangingAttemptsCount
+ _CA_AliroAnalyticsRangingDuration
+ _CA_AliroAnalyticsRangingExceptionBitmap
+ _CA_AliroAnalyticsStepUpDuration
+ _CA_AliroAnalyticsTimeSyncProcedure1Count
+ _CA_AliroAnalyticsTransactionMode
+ _CA_AliroAnalyticsUnlockCount
+ _CA_AliroAnalyticsUnlockFromOtherSourceCount
+ _CA_AliroAnalyticsUnlockSource
+ _CA_AliroSessionEvent
+ _CA_AliroTransactionEvent
+ _CA_AttemptedUrskPrefetches
+ _CA_AuxReaderKeyTxCount
+ _CA_AvgConnectionDurationPerLock
+ _CA_BtConnectionCount
+ _CA_BtConnectionDuration
+ _CA_ConnectionCount
+ _CA_DailyAliroTransactionEvent
+ _CA_DeviceInitiatedRangingCount
+ _CA_DeviceInitiatedSuspendRangingCount
+ _CA_DeviceIntentCount
+ _CA_DeviceStatus
+ _CA_DisconnectionCount
+ _CA_FailedUrskPrefetches
+ _CA_FastTxAttemptedCount
+ _CA_FidoEvent
+ _CA_Friend3rdPartyRKECount
+ _CA_FriendCarKeyCount
+ _CA_FriendDrivingSessionCount
+ _CA_FriendNoDIPassiveEntryTxCount
+ _CA_FriendPassiveEntryTxCount
+ _CA_FriendPassthroughCount
+ _CA_FriendWalkAwayLockCount
+ _CA_FriendWalletRKECount
+ _CA_GeneralStatisticsCancelledStorageSheetCount
+ _CA_GeneralStatisticsCompletedStorageSheetCount
+ _CA_GeneralStatisticsEvent
+ _CA_GeneralStatisticsSECSessionCount
+ _CA_GeneralStatisticsStorageSheetCount
+ _CA_GeneralStatiticsAssetCompatibilityVersion
+ _CA_GeneralStatiticsAssetContentVersion
+ _CA_GeneralStatiticsAssetWeeksTryingToDownload
+ _CA_GeneralTransactionEvent
+ _CA_HeadUnitPairingEvent
+ _CA_HeadUnitPairingEventBrand
+ _CA_HeadUnitPairingEventBtConfig
+ _CA_HeadUnitPairingEventDataCenterCode
+ _CA_HeadUnitPairingEventIsOwner
+ _CA_HeadUnitPairingEventManufacturer
+ _CA_HeadUnitPairingEventPairingResult
+ _CA_HeadUnitPairingEventVehicleCapabilities
+ _CA_KeyPairingEvent
+ _CA_KeyRevocationEvent
+ _CA_KeySharingEvent
+ _CA_KeySyncEvent
+ _CA_KeySyncStateStatistics
+ _CA_KeyTrackingEvent
+ _CA_KeyUpgradeEvent
+ _CA_LockInitiatedResumeRangingCount
+ _CA_LockInitiatedSuspendRangingCount
+ _CA_Owner3rdPartyRKECount
+ _CA_OwnerCarKeyCount
+ _CA_OwnerDrivingSessionCount
+ _CA_OwnerNoDIPassiveEntryTxCount
+ _CA_OwnerPassiveEntryTxCount
+ _CA_OwnerPassthroughCount
+ _CA_OwnerRevocationAccountRole
+ _CA_OwnerRevocationBrand
+ _CA_OwnerRevocationKeyVersion
+ _CA_OwnerRevocationManufacturer
+ _CA_OwnerRevocationNumFriendKeys
+ _CA_OwnerRevocationNumGroupIDs
+ _CA_OwnerRevocationNumSubTrees
+ _CA_OwnerRevocationRegion
+ _CA_OwnerRevocationStatus
+ _CA_OwnerRevocationTransportType
+ _CA_OwnerRevokesFriendKeysEvent
+ _CA_OwnerWalkAwayLockCount
+ _CA_OwnerWalletRKECount
+ _CA_PairingBrand
+ _CA_PairingCarSupportedFrameworkVersions
+ _CA_PairingDataExchangeStep
+ _CA_PairingHUPDataSource
+ _CA_PairingKeyClassOriginBitmap
+ _CA_PairingMailboxVersion
+ _CA_PairingManufacturer
+ _CA_PairingMaxOfflineAttestationCount
+ _CA_PairingPairedKeyVersion
+ _CA_PairingReaderSupportedTransportTypes
+ _CA_PairingRegion
+ _CA_PairingSeManagerState
+ _CA_PairingStatus
+ _CA_PairingStep
+ _CA_PairingTotalOwnerKeys
+ _CA_PairingTransportType
+ _CA_PairingType
+ _CA_PairingVehicleHeadUnitCapabilities
+ _CA_PassiveEntryCategoryInternal
+ _CA_PassiveEntryEvent
+ _CA_PassiveEntryEventBrand
+ _CA_PassiveEntryEventCurrentDeviceState
+ _CA_PassiveEntryEventDeviceIntent
+ _CA_PassiveEntryEventDeviceIntentConfidence
+ _CA_PassiveEntryEventManufacturer
+ _CA_PassiveEntryEventOptimalFlowStatus
+ _CA_PassiveEntryEventRecoveryFlowStatus
+ _CA_PassiveEntryEventRegion
+ _CA_PassiveEntryEventSuboptimalFlowStatus
+ _CA_PassiveEntryEventType
+ _CA_PassiveEntryInternalStatusDisconnected
+ _CA_PassiveEntryInternalStatusPhase4Completed
+ _CA_PassiveEntryInternalStatusRangingEnded
+ _CA_PassiveEntryInternalStatusVehicleLocked
+ _CA_PassiveEntryInternalStatusVehicleUnlocked
+ _CA_PrimaryReaderKeyTxCount
+ _CA_ProbingSessionCount
+ _CA_ProductionEnvironment
+ _CA_RKEEvent
+ _CA_RKEEventActionID
+ _CA_RKEEventBrand
+ _CA_RKEEventExecutionStatus
+ _CA_RKEEventFunctionID
+ _CA_RKEEventManufacturer
+ _CA_RKEEventRegion
+ _CA_RKEEventStatus
+ _CA_RKEEventSubType
+ _CA_RKEEventType
+ _CA_RangingDuration
+ _CA_RevocationBrand
+ _CA_RevocationDestination
+ _CA_RevocationManufacturer
+ _CA_RevocationRegion
+ _CA_RevocationStatus
+ _CA_RevocationTransportType
+ _CA_SESDGeneralStatistics
+ _CA_SeDuration
+ _CA_SharingAccessProfile
+ _CA_SharingAccountRole
+ _CA_SharingActivationOption
+ _CA_SharingAppleToApple
+ _CA_SharingAttestationChainLength
+ _CA_SharingBrand
+ _CA_SharingCarSupportedTransports
+ _CA_SharingCertificateChainLength
+ _CA_SharingDestination
+ _CA_SharingFlow
+ _CA_SharingFrameworkVersion
+ _CA_SharingHUPDataSource
+ _CA_SharingInviteCancelReason
+ _CA_SharingIsIntraAccountShare
+ _CA_SharingKeyClassOriginBitmap
+ _CA_SharingMailboxVersion
+ _CA_SharingManufacturer
+ _CA_SharingPinAttempts
+ _CA_SharingReceiverSupportedFrameworkVersions
+ _CA_SharingRegion
+ _CA_SharingSenderSupportedFrameworkVersions
+ _CA_SharingStatus
+ _CA_SharingStep
+ _CA_SharingTargetDeviceType
+ _CA_SharingTotalKeysForOwnerKey
+ _CA_SharingTotalKeysOnFriendsDevice
+ _CA_SharingType
+ _CA_SharingVehicleHeadUnitCapabilities
+ _CA_SharingWasUserAuthRequired
+ _CA_StandardTxAttemptedCount
+ _CA_StepUpTxAttemptedCount
+ _CA_SuccessfulAliroTxCount
+ _CA_SuccessfulFastTxCount
+ _CA_SuccessfulStandardTxCount
+ _CA_SuccessfulStepUpTxCount
+ _CA_SuspendedDuration
+ _CA_TimeSyncProcedure1Count
+ _CA_TrackingAccountRole
+ _CA_TrackingBrand
+ _CA_TrackingDidReceiveImmoToken
+ _CA_TrackingDidReceiveOnlineBLEKeys
+ _CA_TrackingDidReceiveProductPlanIdentifier
+ _CA_TrackingDidReceiveSlotIdentifier
+ _CA_TrackingErrorCode
+ _CA_TrackingIsOwner
+ _CA_TrackingKeyClassOriginBitmap
+ _CA_TrackingManufacturer
+ _CA_TrackingRequestDurationSeconds
+ _CA_TrackingTransportSupported
+ _CA_TxCountAttempted
+ _CA_UnifiedAccessHomeKeyCount
+ _CA_UnifiedAccessHydraKeyCount
+ _CA_UnknownBrand
+ _CA_UnknownDataCenter
+ _CA_UnknownManufacturer
+ _CA_UnlockNeededForCarActionCount
+ _CA_UpgradeBrand
+ _CA_UpgradeFromVersion
+ _CA_UpgradeIsOwner
+ _CA_UpgradeManufacturer
+ _CA_UpgradeStatus
+ _CA_UpgradeToVersion
+ _CA_UpgradeTransportSupported
+ _CA_UpgradeUpgradeType
+ _CA_UpgradeVersionType
+ _OBJC_CLASS_$_DAKeyPairingConfig
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_CLASS_$_SEEndPointConfigurationAlisha
+ _OBJC_CLASS_$_SEEndPointConfigurationLyon
+ _OBJC_CLASS_$_SEEndPointConfigurationUnifiedAccess
+ _OBJC_CLASS_$_SESAutoBugCapture
+ _OBJC_CLASS_$_SESShortLivedKeySignResult
+ _SESEndPointCreateAlisha
+ _kmlUtilIsVirtualDevice
+ _swift_unknownObjectRetain_n
+ _xpc_dictionary_create_empty
- _$s10Foundation13__DataStorageC27ensureUniqueBufferReference9growingTo5clearySi_SbtF
- _$s10Foundation4DataV11InlineSliceV21ensureUniqueReferenceyyF
- _$s13OSEligibility0A6AnswerO2eeoiySbAC_ACtFZ
- _$s9SEService10SESnapshotC6canFit13proposedUsageSbAA06MemoryF0C_tF
- _$s9SEService10SESnapshotC6canFit25proposedESimProfilesUsageSbAA06MemoryH0C_tF
- _$s9SEService10TCCContextC10TCCServiceO8rawValueSivg
- _$s9SEService10TCCContextC9TCCAccessO8rawValueSivg
- _$s9SEService11SECMetadataV15credentialTypes15appletInstances12friendlyNameACSS_SayAA17SECCredentialInfoVGSStcfC
- _$s9SEService13StateInternalO12DiscriminantOSYAAMc
- _$s9SEService14SERXPCResponseO6canFityACSbcACmFWC
- _$s9SEService18CredentialInternalC10identifier12friendlyName17ownerApplications04userH05state10configUUID11accessLevel12lastUsedDateAC10Foundation0L0V_SSSayAA015ApplicationInfoC0CGAqA05StateC0OAnA06AccessnC0OAL0Q0VSgtcfCTj
- _$s9SEService19AccessLevelInternalO8rawValueSivg
- _$s9SEService20InstanceTypeInternalO8rawValueSivg
- _$s9SEService6SETypeOSYAAMc
- _$sSo22NSManagedObjectContextC8CoreDataE17ScheduledTaskTypeO9immediateyA2EmFWC
- _$sSo22NSManagedObjectContextC8CoreDataE17ScheduledTaskTypeOMa
- _$sSo22NSManagedObjectContextC8CoreDataE7perform8schedule_xAbCE17ScheduledTaskTypeO_xyKctYaKlF
- _$sSo22NSManagedObjectContextC8CoreDataE7perform8schedule_xAbCE17ScheduledTaskTypeO_xyKctYaKlFTu
- _OBJC_CLASS_$_SEEndPointCA
- _OBJC_CLASS_$_SEEndPointConfiguration
- _OBJC_CLASS_$_SESXPCEventListener
- _SESEndPointConfigureMailBoxes
- _SESEndPointCreateForAlishaWithSession
- _TCCAccessPreflightWithAuditToken
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x12
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "\t\t : %@,\n"
+ "\t}\n}"
+ "%s : %i : %s : Simulating cross platform sharing, ignoring BA if received"
+ "%s : %i : No friend sharing manager that matches second factor config"
+ "%s : %i : No owner sharing manager that matches second factor config"
+ "%s : %i : PPID: %{private}@"
+ "%s : %i : Private Config Parameters:\n%@"
+ "%s : %i : Remove pending update for VehicleServer upgrade"
+ "%s : %i : Requesting Pairing to Start For Config:\n%@"
+ "%s : %i : SecureChannel: pairingPassword - %{private}@, salt - %@, pakeVersion - %@"
+ "%s : %i : Simulating cross platform share, not including OEM specific data even though we have it."
+ "%s : %i : Simulating cross platform share, not including sharing random"
+ "%s : %i : Unable to list endpoints on VM"
+ "%s : %i : Unable to read auth from cache: %@"
+ "%s : %i : finalizeVersionType called without matching upgradeVersionType. Expected pending upgrade to version 0x%04lx for type 0x%04lx, but found %@"
+ "%s : %i : listEndpoints call in stats reporting did not complete within timeout"
+ "%s is not available on non-application clients"
+ "%s unknown EligibilityAnswer case encountered, bail"
+ "(null)"
+ "+[KmlEndpointManager listEndpointsWithTimeoutAndError:]"
+ "+[KmlEndpointManager listEndpointsWithTimeoutAndError:]_block_invoke"
+ "-[EndpointConfigForSharing createDeviceConfigWithSupportedRadiosData:sharingConfig:]"
+ "-[KeySharingInvitation createInvitationFromEndpoint:supportedRadiosData:sharingConfig:versionInformation:]"
+ "-[KmlCachedAuthorizationManager readAuthCacheWithError:]"
+ "-[KmlEndpointManager upgradeVersionType:version:upgradeInformation:]_block_invoke_2"
+ "-[KmlOwnerPairingManager startOwnerPairingWithConfig:]_block_invoke"
+ "-[KmlOwnerPairingSession startKeyPairingWithConfig:callback:]_block_invoke"
+ "-[KmlSeManager createOwnerPairingKeysWithConfig:manufacturer:keyName:secureElementSession:bleIntroKey:bleOOBMasterKey:longTermSharedSecret:uwbSupported:versionInformation:preVehicleTransactionPPID:]_block_invoke"
+ "-[SESEndpointAndKeyXPCServer(SEEndPointXPC) createEndPointAuthorizationID:userAuth:forDeviceTransfer:reply:]"
+ "-[SESEndpointAndKeyXPCServer(SEKeyXPC) createSEKey:extractedACLs:keyType:shortLivedKeyType:shortLivedKeyTimerValue:reply:]"
+ "-[SESEndpointAndKeyXPCServer(SEKeyXPC) signWithSEShortLivedKey:data:algorithm:subjectIdentifier:nonce:OIDs:laExternalizedContext:reply:]"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/usr/standalone/firmware/SLAM/SLAM.sefw"
+ "00001111-2222-3333-4444-55556666FFFF"
+ "0x%04lx: 0x%04lx;"
+ "1.2.840.113635.100.6.65.6"
+ "81D292E4-332F-481C-B7DE-7E80973B07BF"
+ "?2"
+ "?4A"
+ "A0000008588100020100"
+ "A00000085881000241010A410200"
+ "A00000085885FE010000000000"
+ "App based client detected, checking background/suspended state"
+ "Attempting to decode legacy metadata for config %s"
+ "B20@0:8i16"
+ "BG Monitor is nil or sessionToStart for pid %d is backgrounded/suspended"
+ "BLESK: %{private}s)"
+ "BT IRK                      : %@\n"
+ "C4F6386A-332F-481C-B7DE-7E80973B07BF"
+ "Car Key Issue Detected!"
+ "Configuring None as default due to TCC revocation"
+ "Configuring Passbook as default due to ineligibility"
+ "Could not load a short-lived key"
+ "Default app %s TCC denied/unknown for fallback TCC"
+ "Default app ineligible for both services"
+ "Deleting Logger Applet"
+ "Eligibility Result %s for domain %s"
+ "Eligibility definite answer available"
+ "Eligibility definite answer not yet available."
+ "Error while listing keys in %@, but this shall not block the slot searching."
+ "Error: Unlock with no DI"
+ "Estimated reclaimable memory: %ld bytes"
+ "Failed to calculate memory for instance AID %s (MID: %s): %@"
+ "Failed to calculate memory for package PID %s: %@"
+ "Failed to copy random bytes with status "
+ "Failed to decode both new and legacy metadata for config %s"
+ "Failed to launch feedback form: %s"
+ "Failed to retrieve signature verification certificate"
+ "Failed to store migrated metadata for config %s: %s"
+ "Feedback level not met, ending launch."
+ "Get CASD Certificate"
+ "Hang"
+ "Identifier : %@ InstanceAID %@ : {\n\tsubjectIdentifier : %@\n\tsecureElementAttestation : %@\n\tcertificates (%lu) : {\n"
+ "Instance AID %s (MID: %s) -> %s (lifecycle: %s): %ld bytes"
+ "Instance AID %s not found in cleanup data"
+ "InstanceAID missing in CA, assuming legacy (CCC) AID"
+ "Invalidating presentment intent assertion for pid %d"
+ "Issue on get CASD certificate."
+ "Item"
+ "KMLCachedAuth"
+ "Logging applet not needed; may be deleted when next cleanup is requested"
+ "Nil passed to signWithSEShortLivedKey"
+ "No _reasonForInUseSession"
+ "No sessions to start"
+ "Nothing to revert"
+ "One of the out of region eligibility conditions not satisfied, default app candidates %s"
+ "PPID                        : %@\n"
+ "PTA is newer than iOS but not deleting applets due to debug option"
+ "Package PID %s -> %s: %ld bytes"
+ "Passive Entry: Error CF."
+ "Passive Entry: unlock without DI."
+ "Password                    : %@\n"
+ "PerformScriptWithNameWithResult:seHandle:logSink:"
+ "PerformScriptWithNameWithResult:sefwPath:seHandle:logSink:"
+ "Received event on stream %@ have %lu delegates"
+ "Received initiateRangingSessionResumeLater when in %s for %s"
+ "Received initiateRangingSessionSetupLater when in %s for %s"
+ "Registered client for stream %@ and returning %u pending events"
+ "Returning newly emptied keySlot %u"
+ "Returning short lived keySlot %u"
+ "Reverting domain for default app to %ld"
+ "SE request in progress for logging applet already"
+ "SEEndPointCA"
+ "SESEndPointListWithSession hung during general stats reporting"
+ "SESXPCEventListener"
+ "SLAM %s completed with outcome %lu"
+ "SLAMDeleteFTAMulti1"
+ "SLAMInstallCopernicus_CCC_2_5_4"
+ "SLAMInstallCopernicus_Home_2_5_4"
+ "SLAMInstallCopernicus_Hydra_2_5_4"
+ "SLAMInstallCopernicus_Lyon_2_5_4"
+ "SLAMInstallCustomDF42Bee"
+ "SLAMLoadAndInstallLogger_1_0_0"
+ "SLAMLoadAndInstallLogger_1_0_0_Internal"
+ "SLAMLoadCopernicus_2_5_4"
+ "Short-lived KeySlot %u not found in applet, set to KSS_Empty(%d)"
+ "Starting the next session (if any)"
+ "Storing current domain %lu"
+ "Successfully migrated and stored metadata for config %s"
+ "T@\"NSArray\",&,V_certificates"
+ "T@\"NSData\",R,V_instanceAID"
+ "T@\"NSData\",R,V_secureElementAttestation"
+ "T@\"NSString\",R,V_identifier"
+ "T@\"NSString\",R,V_subjectIdentifier"
+ "TB,N,D"
+ "TB,R,N,V_shortLived"
+ "The key is not in the SESD and is a short-lived key, which is not loadable."
+ "Timeout error detected for %s, tearing down BLE"
+ "Timer expired but SECPresentmentIntentManager is deallocated or cooldown context not found."
+ "Timer expired but intent manager has been invalidated"
+ "Triggering diagnostics: %s -- Level: need %ld - have %ld"
+ "T{?=*Q},R,V_shortLivedKeyParameter"
+ "Unable to get SecureElementInfo, dequeing all waiters"
+ "Unable to read auth from cache"
+ "Unknown instance MID %s for AID %s -> 0 bytes"
+ "Unknown package PID %s -> 0 bytes"
+ "Unlock with no DI"
+ "Using signature verification PK %@"
+ "Vv136@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"SEEndPointConfigurationAlisha\"48@\"NSData\"56@\"NSData\"64@\"NSString\"72@\"NSData\"80@\"NSData\"88@\"NSData\"96@\"NSArray\"104@\"NSNumber\"112@\"NSNumber\"120@?<v@?@\"SEEndPoint\"@\"NSError\">128"
+ "Vv32@0:8@\"DAKeyPairingConfig\"16@?<v@?@\"NSError\">24"
+ "Vv44@0:8@\"NSString\"16@\"NSData\"24B32@?<v@?@\"SEEndPointCreateAuthorizationIDResponse\"@\"NSError\">36"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">56"
+ "Vv80@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSArray\"56@\"NSData\"64@?<v@?@\"SESShortLivedKeySignResult\"@\"NSError\">72"
+ "Waiting for installation of placeholder default app %s, writing domain to temp"
+ "We have already cached the domain %ld"
+ "_TtC10seserviced17FeedbackFramework"
+ "_certificates"
+ "_createKey:acl:keyType:shortLivedKeyType:shortLivedKeyTimerValue:error:"
+ "_handleEvent:payload:"
+ "_haveInstalledAppletVersion"
+ "_isEndPointCAValid:error:"
+ "_ppid"
+ "_preVehicleTransactionPPID"
+ "_secureElementAttestation"
+ "_shortLived"
+ "_shortLivedKeyParameter"
+ "_subjectIdentifier"
+ "_upgradeToVersion"
+ "addPointer:"
+ "allowLevel"
+ "applicationState"
+ "btIRK"
+ "certificate-%u"
+ "com.apple.identity-document-services.document-provider-ui"
+ "com.apple.seserviced.invalidation"
+ "com.apple.seserviced.sesxpclistener"
+ "createEndPointAuthorizationID:userAuth:forDeviceTransfer:reply:"
+ "createSEKey:extractedACLs:keyType:shortLivedKeyType:shortLivedKeyTimerValue:reply:"
+ "debug.allow.feedback"
+ "debug.have.logging.applet.version"
+ "decodeObjectOfClasses:forKey:"
+ "enumerateObjectsUsingBlock:"
+ "first launch? %s"
+ "framework-car-key"
+ "getApplications(sortedBy:)"
+ "getEncryptedCarOEMProprietaryData:withSecureElement:"
+ "getPrivacyEncryptionPK:error:"
+ "getSignatureCertificateFor:environment:region:keyID:error:"
+ "getUsableKeySlot:secureElement:"
+ "home:didUpdateAccessoryInvitationsForUser:"
+ "iOS (26.4) - SecureElementService-64.20.2"
+ "initWithOpt1:opt2:"
+ "initWithRole:"
+ "initWithSignature:ptAttestation:casdCertificate:"
+ "instanceAID"
+ "isInstalled"
+ "isInternal"
+ "isPidBackgroundedOrSuspended:"
+ "keyEnumerator"
+ "longValue"
+ "modifyAccessForCredential(_:addingOwners:removingOwners:addingUsers:removingUsers:reply:)"
+ "nil parameter to endPointCAWithIdentifier"
+ "outcome"
+ "passbookAppInfo"
+ "password"
+ "pendingEvents"
+ "pendingVersionUpgrades"
+ "ppid"
+ "readAuthCacheWithError:"
+ "reasonForInUseSession"
+ "registeredDelegates"
+ "registeredStreams"
+ "requestAutoBugCapture:subType:subTypeContext:attachments:completion:"
+ "rfuBitsSet"
+ "se,cardauth"
+ "seserviced acquired NFAssertion has expired"
+ "seserviced.sesxpclistener.state"
+ "setAlarm:secondsFromNow:shouldWake:"
+ "setFetchLimit:"
+ "setOptA:"
+ "setPendingVersionUpgrades:"
+ "setSupportsMdocPresentment:"
+ "shortLived"
+ "shortLivedKeyParameter"
+ "signWithSEShortLivedKey:data:algorithm:subjectIdentifier:nonce:OIDs:laExternalizedContext:reply:"
+ "simulateCrossPlatformSharingInitiator"
+ "startKeyPairingWithConfig:callback:"
+ "storeCurrentDomain()"
+ "storeNewCredential(uuid:productConfig:friendlyName:ownerAppId:supportsMdocPresentment:)"
+ "storeNewCredential(uuid:productConfigId:supportsMdocPresentment:friendlyName:)"
+ "supportsMdocPresentment"
+ "temporaryDomainKey"
+ "transport"
+ "triggerDiagnosticsWithForm:level:error:"
+ "unarchivedObjectOfClass:fromData:error:"
+ "updatePPIDWithConfigValue:"
+ "v24@?0@\"SESExpressConfiguration\"8@\"NSError\"16"
+ "v32@?0@\"NSData\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "v40@0:8q16q24q32"
+ "vienna.force.idvExtension"
+ "weakObjectsPointerArray"
+ "{"
+ "}"
+ "\xf0!"
+ "\xf0A"
+ "\xf0\x81"
- " into a CredentialType."
- "%s : %i : PPID: %@"
- "%s : %i : Requesting Pairing to Start"
- "%s : %i : Revert is a no-op for VehicleServer upgrade"
- "%s : %i : SecureChannel: pairingPassword - %@, salt - %@, pakeVersion - %@"
- "%s : %i : Unable to read auth from cache, setting cache as dirty: %@"
- "-[KmlEndpointManager upgradeVersionType:version:upgradeInformation:]_block_invoke"
- "-[KmlOwnerPairingManager startOwnerPairingWithPassword:keyName:transport:bindingAttestation:]_block_invoke"
- "-[KmlOwnerPairingSession startKeyPairingWithPassword:keyName:transport:bindingAttestation:callback:]_block_invoke"
- "-[KmlSeManager createOwnerPairingKeysWithConfig:manufacturer:keyName:secureElementSession:bleIntroKey:bleOOBMasterKey:longTermSharedSecret:uwbSupported:versionInformation:]_block_invoke"
- "-[SESEndpointAndKeyXPCServer(SEEndPointXPC) createEndPointAuthorizationID:userAuth:reply:]"
- "-[SESEndpointAndKeyXPCServer(SEKeyXPC) createSEKey:extractedACLs:reply:]"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "81D292E4-16D8-4630-82ED-BDF62B05E334"
- "?1"
- "?3A"
- "Brand"
- "C4F6386A-780D-40E5-9900-0A26C16273A1"
- "Card Emulation is not available on non-application clients"
- "Could not convert "
- "Default app %s TCC denied/unknown for fallback TCC, overwriting passbook as default due to ineligibility"
- "Default app ineligible for both services, configuring None as default due to TCC revocation"
- "Default app ineligible for both services, configuring Passbook as default due to ineligibility"
- "Deinitializing session-presence related singletons"
- "Deleting unused Logger Applet"
- "Deletion is not available on non-application clients"
- "Edit access is not available on non-application clients"
- "Failed initialize database for fixEndpointSignatureCertificatePK"
- "Failed to acquire read handle for reconciliation %@"
- "Failed to copy random bytes status "
- "Failed to extract PK from signature cert %@"
- "Failed to fix signature certificate PKs %@"
- "Failed to get endpoint %@ %@"
- "Failed to get express pass configurations"
- "Failed to get instance entity %@"
- "Failed to retrieve PK %@"
- "Failed to retrieve signature certificate %@"
- "FixSignaturePK"
- "Fixed signature certificate PK for %@"
- "Fixing endpoint %@"
- "Fixing signature certificate PKs"
- "HUPDataSource"
- "Invalid region %@"
- "Maintenance API is not available on non-application clients"
- "Manufacturer"
- "Missing server privacy public key"
- "Nothing to fix for %@"
- "One of the out of region eligibility conditions not satisfied and but exist candidates, show default app pane"
- "One of the out of region eligibility conditions not satisfied and no candidates, should not show default app pane"
- "PK %@"
- "PerformScriptWithName:seHandle:logSink:"
- "PerformScriptWithName:sefwPath:seHandle:logSink:"
- "Received BLESK with type %s"
- "SLAMInstallCopernicus_CCC_2_4_0"
- "SLAMInstallCopernicus_Home_2_4_0"
- "SLAMInstallCopernicus_Hydra_2_4_0"
- "SLAMInstallCopernicus_Lyon_2_4_0"
- "SLAMLoadAndInstallLogger"
- "SLAMLoadCopernicus_2_4_0"
- "Signature certificate PKs have been fixed"
- "SignatureCertificatePKsHaveBeenFixed"
- "Unable to get SecureElementInfo"
- "Vv136@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"SEEndPointConfiguration\"48@\"NSData\"56@\"NSData\"64@\"NSString\"72@\"NSData\"80@\"NSData\"88@\"NSData\"96@\"NSArray\"104@\"NSNumber\"112@\"NSNumber\"120@?<v@?@\"SEEndPoint\"@\"NSError\">128"
- "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"SEEndPointCreateAuthorizationIDResponse\"@\"NSError\">32"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSData\"40@?<v@?@\"NSError\">48"
- "Vv56@0:8@16@24q32@40@?48"
- "_createKey:acl:error:"
- "accessProfile"
- "accountRole"
- "actionID"
- "activationOption"
- "appleToApple"
- "assetCompatibilityVersion"
- "assetContentVersion"
- "attemptedURSKprefetches"
- "attestationChainLength"
- "avgConnectionDurationPerLock"
- "bluetoothConfiguration"
- "carSupportedFrameworkVersions"
- "certificateChainLength"
- "com.apple.coreidv.mobile-document-provider"
- "com.apple.kml.generalStatisticsEvent"
- "com.apple.kml.generalTransactionStatisticsEvent"
- "com.apple.kml.headUnitPairingEvent"
- "com.apple.kml.keyPairingEvent"
- "com.apple.kml.keyRevocationEvent"
- "com.apple.kml.keySharingEvent"
- "com.apple.kml.keyTrackingEvent"
- "com.apple.kml.keyUpgradeEvent"
- "com.apple.kml.ownerRevokesFriendKeysEvent"
- "com.apple.kml.passiveEntryEvent"
- "com.apple.kml.rkeEvent"
- "com.apple.sesd.aliroSessionEvent"
- "com.apple.sesd.aliroTransactionEvent"
- "com.apple.sesd.dailyAliroTransactionEvent"
- "com.apple.sesd.fidoEvent"
- "com.apple.sesd.keySyncEvent"
- "configurationWithOpt1:opt2:"
- "connectionCount"
- "createEndPointAuthorizationID:userAuth:reply:"
- "createSEKey:extractedACLs:reply:"
- "currentDeviceState"
- "dataCenterCode"
- "dataExchangeStep"
- "destination"
- "deviceInitatedRangingAttemptsCount"
- "deviceInitatedRangingCount"
- "deviceInitatedSuspendRangingCount"
- "deviceIntent"
- "deviceIntentConfidence"
- "deviceIntentCount"
- "deviceStatus"
- "didReceiveImmoToken"
- "didReceiveOnlineBLEKeys"
- "didReceiveProductPlanIdentifier"
- "didReceiveSlotIdentifier"
- "disconnectReason"
- "disconnectionCount"
- "errorCode"
- "eventType"
- "executionStatus"
- "failedURSKprefetches"
- "fixEndpointSignatureCertificatePK:"
- "frameworkVersion"
- "friend3rdPartyRKECount"
- "friendCarKeyCount"
- "friendDrivingSessionCount"
- "friendNoDIPassiveEntryTxCount"
- "friendPassiveEntryTxCount"
- "friendPassthroughCount"
- "friendWalkAwayLockCount"
- "friendWalletRKECount"
- "fromVersion"
- "functionID"
- "getApplicationEntities(sortedBy:)"
- "getEncryptedCarOEMProprietaryData:withEndpointEntity:withSecureElement:"
- "getSignatureCertificateFor:environment:region:error:"
- "getUsableKeySlot:"
- "home:didUpdateAccesoryInvitationsForUser:"
- "homeDefaults"
- "hydraDefaults"
- "iOS (26.3) - SecureElementService-63.2.1"
- "infoFWVersion"
- "infoProductID"
- "infoVendorID"
- "intentFallbackTriggered"
- "inviteCancelReason"
- "isIntraAccountShare"
- "isOwner"
- "keyClassOriginBitmap"
- "keyType"
- "keyVersion"
- "lockCapability"
- "lockSharingCapability"
- "lockStatusAtConnection"
- "lyonHomeDefaults"
- "lyonHydraDefaults"
- "nfcExpressOnlyInLPM"
- "numFriendKeys"
- "numGroupIDs"
- "numSubTrees"
- "numberOfCancelledSheets"
- "numberOfCompleteSheets"
- "numberOfSheetsShown"
- "optimalFlowStatus"
- "owner3rdPartyRKECount"
- "ownerCarKeyCount"
- "ownerDrivingSessionCount"
- "ownerNoDIPassiveEntryTxCount"
- "ownerPassiveEntryTxCount"
- "ownerPassthroughCount"
- "ownerWalkAwayLockCount"
- "ownerWalletRKECount"
- "pairedKeyVersion"
- "pairingResult"
- "pairingTransport"
- "pinAttempts"
- "probingSessionCount"
- "production"
- "readerSupportedTransportTypes"
- "receiverSupportedFrameworkVersions"
- "recoveryFlowStatus"
- "seManagerState"
- "senderSupportedFrameworkVersions"
- "setAlarm:secondsFromNow:"
- "setNfcExpressOnlyInLPM:"
- "setPrivacyEncryptionPK:"
- "setSignatureVerificationPK:"
- "setTerminationNotPersisted:"
- "sharingTransport"
- "startKeyPairingWithPassword:keyName:transport:bindingAttestation:callback:"
- "step"
- "stepUpDuration"
- "storeNewCredential(uuid:productConfig:friendlyName:ownerAppId:)"
- "storeNewCredential(uuid:productConfigId:friendlyName:)"
- "subType"
- "suboptimalFlowStatus"
- "terminationNotPersisted"
- "toVersion"
- "totalOwnerKeysPaired"
- "totalSecureElementCredentialSession"
- "totalSharedKeysForOwnerKey"
- "totalSharedKeysOnFriendDevice"
- "trackingRequestDuration"
- "transportSupported"
- "unifiedAccessHomeKeyCount"
- "unifiedAccessHydraKeyCount"
- "unlockNeededForCarActionCount"
- "unlockSource"
- "vehicleCapabilities"
- "versionType"
- "wasUserAuthRequired"
- "weeksSinceInitialMADownloadAttempt"
- "\xf01"

```
