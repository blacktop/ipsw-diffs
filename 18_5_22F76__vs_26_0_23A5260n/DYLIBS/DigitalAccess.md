## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-55.4.0.0.0
-  __TEXT.__text: 0x20cd0
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1b84
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x76a8
-  __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0xe54
-  __TEXT.__unwind_info: 0xa30
-  __TEXT.__objc_classname: 0x48e
-  __TEXT.__objc_methname: 0x4c43
-  __TEXT.__objc_methtype: 0x1797
-  __TEXT.__objc_stubs: 0x2500
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xf50
-  __DATA_CONST.__objc_classlist: 0xf8
+60.26.1.0.0
+  __TEXT.__text: 0x32e50
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x252c
+  __TEXT.__const: 0x6a8
+  __TEXT.__cstring: 0x6e71
+  __TEXT.__oslogstring: 0x1f02
+  __TEXT.__gcc_except_tab: 0x1180
+  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__objc_classname: 0x4f4
+  __TEXT.__objc_methname: 0x66c3
+  __TEXT.__objc_methtype: 0x1a1a
+  __TEXT.__objc_stubs: 0x29c0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0xf90
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_selrefs: 0x12e0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x2520
-  __AUTH_CONST.__objc_const: 0x37d8
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x274
-  __DATA.__data: 0x660
-  __DATA.__bss: 0x72
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x1be0
+  __AUTH_CONST.__objc_const: 0x41a8
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x2d8
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSESShared.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E537941-CAEF-38B2-8846-27B8D47ADE77
-  Functions: 717
-  Symbols:   2503
-  CStrings:  1873
+  UUID: 277C4867-249F-3D40-8BAF-9B0B1DA1A150
+  Functions: 918
+  Symbols:   3028
+  CStrings:  2172
 
Symbols:
+ +[DAAdditionalConfigurationData supportsSecureCoding]
+ +[DAKeySharingAnalyticsData supportsSecureCoding]
+ +[DASharingAnalyticsUpdateConfig supportsSecureCoding]
+ +[KmlSettingsManager sharedSettingsManager]
+ +[KmlSettingsManager sharedSettingsManager].cold.1
+ +[KmlTlv TLVWithJustTag:]
+ +[KmlTlv TLVWithTag:unsignedLongValue:]
+ +[KmlVersions doesVersion:support:]
+ -[DAAdditionalConfigurationData .cxx_destruct]
+ -[DAAdditionalConfigurationData copyWithZone:]
+ -[DAAdditionalConfigurationData description]
+ -[DAAdditionalConfigurationData encodeWithCoder:]
+ -[DAAdditionalConfigurationData initWithCoder:]
+ -[DAAdditionalConfigurationData initWithKeyRole:]
+ -[DAAdditionalConfigurationData keyRole]
+ -[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]
+ -[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]
+ -[DAKeyPairingSession preWarmForManufacturer:].cold.1
+ -[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:].cold.1
+ -[DAKeySharing2FAConfiguration initForBringOtherKey]
+ -[DAKeySharingAnalyticsData copyWithZone:]
+ -[DAKeySharingAnalyticsData description]
+ -[DAKeySharingAnalyticsData encodeWithCoder:]
+ -[DAKeySharingAnalyticsData initWithCoder:]
+ -[DAKeySharingAnalyticsData initWithSharingFlow:]
+ -[DAKeySharingAnalyticsData sharingFlow]
+ -[DAKeySharingSession cancelSharingInvitation:completionHandler:]
+ -[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]
+ -[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]
+ -[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:].cold.1
+ -[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]
+ -[DAManager establishXpcConnection].cold.1
+ -[DAManager releaseConnection]
+ -[DAShareRecipientResult initFailureResultWithCredentialIdentifier:error:]
+ -[DAShareRecipientResult initSharingCancelledResultWithResponse:error:]
+ -[DASharingAnalyticsUpdateConfig .cxx_destruct]
+ -[DASharingAnalyticsUpdateConfig analyticsData]
+ -[DASharingAnalyticsUpdateConfig encodeWithCoder:]
+ -[DASharingAnalyticsUpdateConfig initWithCoder:]
+ -[DASharingAnalyticsUpdateConfig initWithInvitationIdentifiers:keyIdentifier:recipientFlow:analyticsData:]
+ -[DASharingAnalyticsUpdateConfig invitationIdentifiers]
+ -[DASharingAnalyticsUpdateConfig keyIdentifier]
+ -[DASharingAnalyticsUpdateConfig recipientFlow]
+ -[KmlCancelMessage cccCode]
+ -[KmlCancelMessage initWithData:]
+ -[KmlCancelMessage initWithKmlErrorCode:]
+ -[KmlCancelMessage kmlCode]
+ -[KmlCancelMessage setCccCode:]
+ -[KmlCancelMessage setKmlCode:]
+ -[KmlDeviceConfigurationData additionalMailboxSettingAsData]
+ -[KmlDeviceConfigurationData asData]
+ -[KmlDeviceConfigurationData carSupportsUpdateAttestation]
+ -[KmlDeviceConfigurationData confMailboxSettingAsData]
+ -[KmlDeviceConfigurationData deviceBtIntroKey]
+ -[KmlDeviceConfigurationData deviceBtOOBKey]
+ -[KmlDeviceConfigurationData didParseDataSuccessfully]
+ -[KmlDeviceConfigurationData immoTokenConfig]
+ -[KmlDeviceConfigurationData initiatorSupportedFrameworkVersionsData]
+ -[KmlDeviceConfigurationData isImmoTokenNeeded]
+ -[KmlDeviceConfigurationData isOwnerImmoTokenOrSlotOnline]
+ -[KmlDeviceConfigurationData isValidForKmlVersion:transport:]
+ -[KmlDeviceConfigurationData keyTrackingReceiptRequired]
+ -[KmlDeviceConfigurationData maxOfflineAttestationCount]
+ -[KmlDeviceConfigurationData mfiPPID]
+ -[KmlDeviceConfigurationData oemSpecificContentAsData]
+ -[KmlDeviceConfigurationData onlineAttestationDeliverySupported]
+ -[KmlDeviceConfigurationData onlineBleOOBMasterKeyOverride]
+ -[KmlDeviceConfigurationData privateMailboxSettingAsData]
+ -[KmlDeviceConfigurationData readerBleConfigWithTag:target:]
+ -[KmlDeviceConfigurationData readerBtIRK]
+ -[KmlDeviceConfigurationData readerBtIdAddress]
+ -[KmlDeviceConfigurationData readerSupportsLELR]
+ -[KmlDeviceConfigurationData readerSupportsNfc]
+ -[KmlDeviceConfigurationData readerSupportsUwb]
+ -[KmlDeviceConfigurationData removeUwbSupportLocally]
+ -[KmlDeviceConfigurationData setAdditionalMailboxSettingAsData:]
+ -[KmlDeviceConfigurationData setCarSupportsUpdateAttestation:]
+ -[KmlDeviceConfigurationData setConfMailboxSettingAsData:]
+ -[KmlDeviceConfigurationData setDeviceBtIntroKey:]
+ -[KmlDeviceConfigurationData setDeviceBtOOBKey:]
+ -[KmlDeviceConfigurationData setDidParseDataSuccessfully:]
+ -[KmlDeviceConfigurationData setImmoTokenConfig:]
+ -[KmlDeviceConfigurationData setInitiatorSupportedFrameworkVersionsData:]
+ -[KmlDeviceConfigurationData setKeyTrackingReceiptRequired:]
+ -[KmlDeviceConfigurationData setMaxOfflineAttestationCount:]
+ -[KmlDeviceConfigurationData setMfiPPID:]
+ -[KmlDeviceConfigurationData setOemSpecificContentAsData:]
+ -[KmlDeviceConfigurationData setOnlineAttestationDeliverySupported:]
+ -[KmlDeviceConfigurationData setOnlineBleOOBMasterKeyOverride:]
+ -[KmlDeviceConfigurationData setPrivateMailboxSettingAsData:]
+ -[KmlDeviceConfigurationData setReaderBtIRK:]
+ -[KmlDeviceConfigurationData setReaderBtIdAddress:]
+ -[KmlDeviceConfigurationData setReaderSupportsLELR:]
+ -[KmlDeviceConfigurationData setReaderSupportsNfc:]
+ -[KmlDeviceConfigurationData setReaderSupportsUwb:]
+ -[KmlDeviceConfigurationData setSharingPasswordLength:]
+ -[KmlDeviceConfigurationData setSharingPasswordLengthAsData:]
+ -[KmlDeviceConfigurationData setSharingPasswordRequired:]
+ -[KmlDeviceConfigurationData setSupportedKeyProfiles:]
+ -[KmlDeviceConfigurationData setUwbDisabledLocally:]
+ -[KmlDeviceConfigurationData setV3ConfMailboxSettingAsData:]
+ -[KmlDeviceConfigurationData setV3PrivateMailboxSettingAsData:]
+ -[KmlDeviceConfigurationData setVehicleSupportedFrameworkVersionsData:]
+ -[KmlDeviceConfigurationData sharingConfigForFriendAsData]
+ -[KmlDeviceConfigurationData sharingConfigToSend:]
+ -[KmlDeviceConfigurationData sharingPasswordLengthAsData]
+ -[KmlDeviceConfigurationData sharingPasswordLength]
+ -[KmlDeviceConfigurationData supportedKeyProfiles]
+ -[KmlDeviceConfigurationData supportedRadiosAsDataForTarget:]
+ -[KmlDeviceConfigurationData updatePPIDWithServerProvidedData:]
+ -[KmlDeviceConfigurationData updateSharingConfigWithData:]
+ -[KmlDeviceConfigurationData updateSupportedRadiosWithData:]
+ -[KmlDeviceConfigurationData uwbDisabledLocally]
+ -[KmlDeviceConfigurationData v3ConfMailboxSettingAsData]
+ -[KmlDeviceConfigurationData v3PrivateMailboxSettingAsData]
+ -[KmlDeviceConfigurationData vehicleSupportedFrameworkVersionsData]
+ -[KmlMailboxMappingData .cxx_destruct]
+ -[KmlMailboxMappingData asData]
+ -[KmlMailboxMappingData attestationPackageLength]
+ -[KmlMailboxMappingData getMaskToIndicateKeyAttestationConsumed]
+ -[KmlMailboxMappingData getMaskToIndicateKeyAttestationSaved]
+ -[KmlMailboxMappingData getMaskToIndicateOemPropDataConsumed]
+ -[KmlMailboxMappingData getMaskToIndicateOemPropDataSaved]
+ -[KmlMailboxMappingData getMaskToIndicateSlotIdListConsumed]
+ -[KmlMailboxMappingData getMaskToIndicateSlotIdListSaved]
+ -[KmlMailboxMappingData immoTokenLength]
+ -[KmlMailboxMappingData initWithData:preferredVersion:]
+ -[KmlMailboxMappingData isKeyAttestationSetByCarInSignalingBitmap:]
+ -[KmlMailboxMappingData isKeyAttestationSetByDeviceInSignalingBitmap:]
+ -[KmlMailboxMappingData isOemPropDataSetByCarInSignalingBitmap:]
+ -[KmlMailboxMappingData isOemPropDataSetByDeviceInSignalingBitmap:]
+ -[KmlMailboxMappingData isSlotIdListSetByCarInSignalingBitmap:]
+ -[KmlMailboxMappingData isSlotIdListSetByDeviceInSignalingBitmap:]
+ -[KmlMailboxMappingData isValid]
+ -[KmlMailboxMappingData keyAttestationStartOffset]
+ -[KmlMailboxMappingData mailboxEndOffset]
+ -[KmlMailboxMappingData mailboxVersion]
+ -[KmlMailboxMappingData signalingBitmapOffset]
+ -[KmlMailboxMappingData signerSlotIdListOffset]
+ -[KmlMailboxMappingData slotIdBitmapOffset]
+ -[KmlMailboxMappingData slotIdListOffset]
+ -[KmlMailboxMappingData slotIdentifierLength]
+ -[KmlMailboxMappingData vehicleProprietaryDataOffset]
+ -[KmlSettingsManager .cxx_destruct]
+ -[KmlSettingsManager BluetoothHceSessionTimeLimit]
+ -[KmlSettingsManager BluetoothLoyaltyAndPaymentSessionTimeLimit]
+ -[KmlSettingsManager NFCHceSessionTimeLimit]
+ -[KmlSettingsManager NFCLoyaltyAndPaymentSessionTimeLimit]
+ -[KmlSettingsManager allowFleetOwnerPairing]
+ -[KmlSettingsManager allowRadioMismatchForTest]
+ -[KmlSettingsManager boolValueForSetting:manufacturer:brand:uuid:error:]
+ -[KmlSettingsManager boolValueForUserDefault:]
+ -[KmlSettingsManager buildNonOSPPreShareTlvOverride]
+ -[KmlSettingsManager bypassAccountInfoHash]
+ -[KmlSettingsManager defaultBoolValueForSetting:]
+ -[KmlSettingsManager disableFleetKeyStrictShareInitCertChainValidation]
+ -[KmlSettingsManager disableOptTwoShareInitCertChainValidation]
+ -[KmlSettingsManager disablePrivateKeyStrictShareInitCertChainValidation]
+ -[KmlSettingsManager emulateNFCOnlyDevice]
+ -[KmlSettingsManager fleetManufacturerAllowListWithError:]
+ -[KmlSettingsManager fleetServiceProviderAllowListWithError:]
+ -[KmlSettingsManager getRootCertificateFor:keyId:]
+ -[KmlSettingsManager ignoreInvalidAttestationPackageSignature]
+ -[KmlSettingsManager init]
+ -[KmlSettingsManager isManufacturerSupported:error:]
+ -[KmlSettingsManager keyRoleToShareOverride]
+ -[KmlSettingsManager kmlVersionOverride]
+ -[KmlSettingsManager mockFleetEndpointCert]
+ -[KmlSettingsManager mockFleetExtCaCert]
+ -[KmlSettingsManager mockFleetIntermediateCert]
+ -[KmlSettingsManager opt2AuthDeletionAlarmDurationSeconds]
+ -[KmlSettingsManager pretendBindingAttestationUsed]
+ -[KmlSettingsManager skipWaitingForBindingAttestation]
+ -[KmlSettingsManager timeIntervalForUserDefault:minTimeInterval:maxTimeInterval:defaultTimeInterval:]
+ -[KmlSettingsManager useAppletVersionsForCertificationTesting]
+ -[KmlSettingsManager useBasicSecurityPolicy]
+ -[KmlSettingsManager useOldKeyConfigTag]
+ -[KmlSettingsManager useOldKeyTrackingTag]
+ -[KmlSettingsManager useOldSignalingBitmap]
+ -[KmlTlv valueAsUnsignedLong]
+ -[KmlVersions doesAgreedVersionSupportOnlineBleKeys]
+ -[KmlVersions downgradePreferredVersion]
+ -[KmlVersions downgradePreferredVersion].cold.1
+ -[KmlVersions generateKmlSupportedVehicleServerVersionsData]
+ -[KmlVersions getAgreedBluetoothVersionsTlv]
+ -[KmlVersions getKmlSupportedVersionsTlvAsShareRecipient]
+ -[KmlVersions getVehicleSupportedVersionsData]
+ -[KmlVersions hasUpgradeForVersionType:versions:isOwnerPairedKey:]
+ -[KmlVersions initWithEndpoint:]
+ -[KmlVersions ourSupportedFrameworkVersionsAsCAString]
+ -[KmlVersions updateSupportedFrameworkVersionsForSharing:]
+ -[KmlVersions updateVehicleSupportedBluetoothVersions:]
+ -[KmlVersions upgradeForVersionType:version:]
+ -[KmlVersions upgradeForVersionType:version:].cold.1
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table44
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table97
+ _KmlLogIsInternalBuild
+ _KmlLogIsInternalBuild.cold.1
+ _KmlLogIsInternalBuild.internalBuild
+ _KmlLogIsInternalBuild.onceToken
+ _OBJC_CLASS_$_DAAdditionalConfigurationData
+ _OBJC_CLASS_$_DAKeySharingAnalyticsData
+ _OBJC_CLASS_$_DASharingAnalyticsUpdateConfig
+ _OBJC_CLASS_$_KmlMailboxMappingData
+ _OBJC_CLASS_$_KmlSettingsManager
+ _OBJC_IVAR_$_DAAdditionalConfigurationData._keyRole
+ _OBJC_IVAR_$_DAKeySharingAnalyticsData._sharingFlow
+ _OBJC_IVAR_$_DASharingAnalyticsUpdateConfig._analyticsData
+ _OBJC_IVAR_$_DASharingAnalyticsUpdateConfig._invitationIdentifiers
+ _OBJC_IVAR_$_DASharingAnalyticsUpdateConfig._keyIdentifier
+ _OBJC_IVAR_$_DASharingAnalyticsUpdateConfig._recipientFlow
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._didParseDataSuccessfully
+ _OBJC_IVAR_$_KmlMailboxMappingData._allMailboxMappingTlvs
+ _OBJC_IVAR_$_KmlMailboxMappingData._attestationPackageLength
+ _OBJC_IVAR_$_KmlMailboxMappingData._immoTokenLength
+ _OBJC_IVAR_$_KmlMailboxMappingData._keyAttestationListStartOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._keyAttestationStartOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._mailboxEndOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._mailboxVersion
+ _OBJC_IVAR_$_KmlMailboxMappingData._preferredVersion
+ _OBJC_IVAR_$_KmlMailboxMappingData._preferredVersionTlvs
+ _OBJC_IVAR_$_KmlMailboxMappingData._signalingBitmapOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._signerSlotIdListOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._slotIdBitmapOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._slotIdListOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._slotIdentifierLength
+ _OBJC_IVAR_$_KmlMailboxMappingData._useOldSignalingBitmap
+ _OBJC_IVAR_$_KmlMailboxMappingData._vehicleProprietaryDataOffset
+ _OBJC_IVAR_$_KmlMailboxMappingData._vehicleProprietaryDataOffset_v3
+ _OBJC_IVAR_$_KmlSettingsManager._dckConfig
+ _OBJC_IVAR_$_KmlSettingsManager._defaultSLGValues
+ _OBJC_IVAR_$_KmlSettingsManager._userDefaults
+ _OBJC_METACLASS_$_DAAdditionalConfigurationData
+ _OBJC_METACLASS_$_DAKeySharingAnalyticsData
+ _OBJC_METACLASS_$_DASharingAnalyticsUpdateConfig
+ _OBJC_METACLASS_$_KmlMailboxMappingData
+ _OBJC_METACLASS_$_KmlSettingsManager
+ _SESEndPointPreWarmForAlisha
+ __OBJC_$_CLASS_METHODS_DAAdditionalConfigurationData
+ __OBJC_$_CLASS_METHODS_DAKeySharingAnalyticsData
+ __OBJC_$_CLASS_METHODS_DASharingAnalyticsUpdateConfig
+ __OBJC_$_CLASS_METHODS_KmlSettingsManager
+ __OBJC_$_CLASS_METHODS_KmlTlv
+ __OBJC_$_CLASS_METHODS_KmlVersions
+ __OBJC_$_CLASS_PROP_LIST_DAAdditionalConfigurationData
+ __OBJC_$_CLASS_PROP_LIST_DAKeySharingAnalyticsData
+ __OBJC_$_CLASS_PROP_LIST_DASharingAnalyticsUpdateConfig
+ __OBJC_$_INSTANCE_METHODS_DAAdditionalConfigurationData
+ __OBJC_$_INSTANCE_METHODS_DAKeySharingAnalyticsData
+ __OBJC_$_INSTANCE_METHODS_DASharingAnalyticsUpdateConfig
+ __OBJC_$_INSTANCE_METHODS_KmlCancelMessage
+ __OBJC_$_INSTANCE_METHODS_KmlMailboxMappingData
+ __OBJC_$_INSTANCE_METHODS_KmlSettingsManager
+ __OBJC_$_INSTANCE_VARIABLES_DAAdditionalConfigurationData
+ __OBJC_$_INSTANCE_VARIABLES_DAKeySharingAnalyticsData
+ __OBJC_$_INSTANCE_VARIABLES_DASharingAnalyticsUpdateConfig
+ __OBJC_$_INSTANCE_VARIABLES_KmlMailboxMappingData
+ __OBJC_$_INSTANCE_VARIABLES_KmlSettingsManager
+ __OBJC_$_PROP_LIST_DAAdditionalConfigurationData
+ __OBJC_$_PROP_LIST_DAKeySharingAnalyticsData
+ __OBJC_$_PROP_LIST_DASharingAnalyticsUpdateConfig
+ __OBJC_$_PROP_LIST_KmlCancelMessage
+ __OBJC_$_PROP_LIST_KmlDeviceConfigurationData
+ __OBJC_$_PROP_LIST_KmlMailboxMappingData
+ __OBJC_$_PROP_LIST_KmlTlv
+ __OBJC_CLASS_PROTOCOLS_$_DAAdditionalConfigurationData
+ __OBJC_CLASS_PROTOCOLS_$_DAKeySharingAnalyticsData
+ __OBJC_CLASS_PROTOCOLS_$_DASharingAnalyticsUpdateConfig
+ __OBJC_CLASS_RO_$_DAAdditionalConfigurationData
+ __OBJC_CLASS_RO_$_DAKeySharingAnalyticsData
+ __OBJC_CLASS_RO_$_DASharingAnalyticsUpdateConfig
+ __OBJC_CLASS_RO_$_KmlMailboxMappingData
+ __OBJC_CLASS_RO_$_KmlSettingsManager
+ __OBJC_METACLASS_RO_$_DAAdditionalConfigurationData
+ __OBJC_METACLASS_RO_$_DAKeySharingAnalyticsData
+ __OBJC_METACLASS_RO_$_DASharingAnalyticsUpdateConfig
+ __OBJC_METACLASS_RO_$_KmlMailboxMappingData
+ __OBJC_METACLASS_RO_$_KmlSettingsManager
+ ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.42
+ ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke.24
+ ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke.28
+ ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.45
+ ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke.7
+ ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke.30
+ ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.43
+ ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke.22
+ ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke.9
+ ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.16
+ ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke.46
+ ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke
+ ___113-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke.33
+ ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke.27
+ ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke.27
+ ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke.19
+ ___23-[DASession endSession]_block_invoke.8
+ ___35-[DAKeyPairingSession startProbing]_block_invoke.10
+ ___35-[DAManager establishXpcConnection]_block_invoke.67
+ ___35-[DAManager establishXpcConnection]_block_invoke.67.cold.1
+ ___35-[DAManager establishXpcConnection]_block_invoke.cold.1
+ ___43+[KmlSettingsManager sharedSettingsManager]_block_invoke
+ ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.7
+ ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke.70
+ ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke.73
+ ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke.12
+ ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke.76
+ ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke.9
+ ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke.16
+ ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke
+ ___65-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke.15
+ ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke.18
+ ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke.15
+ ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.41
+ ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke.34
+ ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke.22
+ ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke.17
+ ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke.44
+ ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke.13
+ ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke.18
+ ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.48
+ ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke
+ ___74-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke.35
+ ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.38
+ ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke.51
+ ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke.19
+ ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke.42
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.15
+ ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke.33
+ ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.45
+ ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke
+ ___80-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke.23
+ ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke.78
+ ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.37
+ ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke
+ ___81-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke.28
+ ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.36
+ ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.48
+ ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke.11
+ ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.46
+ ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke.40
+ ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke.39
+ ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke.49
+ ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke
+ ___86-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.47
+ ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.39
+ ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke.31
+ ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke.29
+ ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke
+ ___89-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke.50
+ ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke.43
+ ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke.24
+ ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke.20
+ ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke.25
+ ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke.8
+ ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke.25
+ ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke.21
+ ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.31
+ ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke.32
+ ___KmlLogIsInternalBuild_block_invoke
+ ___block_literal_global.22
+ ___block_literal_global.357
+ ___block_literal_global.4
+ ___block_literal_global.425
+ ___block_literal_global.7
+ ___block_literal_global.80
+ ___block_literal_global.82
+ ___block_literal_global.84
+ ___block_literal_global.86
+ ___block_literal_global.88
+ ___block_literal_global.90
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___block_literal_global.96
+ ___block_literal_global.98
+ ___kCFBooleanFalse
+ _decodeWithData:error:.allowedClasses.355
+ _decodeWithData:error:.allowedClasses.423
+ _decodeWithData:error:.pred.354
+ _decodeWithData:error:.pred.422
+ _objc_msgSend$TLVWithJustTag:
+ _objc_msgSend$TLVWithTag:unsignedChar:
+ _objc_msgSend$TLVWithTag:unsignedShort:
+ _objc_msgSend$TLVWithTag:value:
+ _objc_msgSend$TLVsWithData:
+ _objc_msgSend$acceptInvitationWithIdentifier:passcode:completionHandler:
+ _objc_msgSend$acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:productPlanIdentifier:completionHandler:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$analyticsData
+ _objc_msgSend$asData
+ _objc_msgSend$boolValueForUserDefault:
+ _objc_msgSend$defaultBoolValueForSetting:
+ _objc_msgSend$doesVersion:support:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$getRootCertificateFor:keyID:error:
+ _objc_msgSend$getSettingForKey:error:
+ _objc_msgSend$initFailureResultWithCredentialIdentifier:error:
+ _objc_msgSend$initWithCCCErrorCode:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithData:outerTag:
+ _objc_msgSend$initWithEndpoint:downgradeFrameworkSetting:
+ _objc_msgSend$invitationIdentifiers
+ _objc_msgSend$isDCKConfigurationAvailableFor:error:
+ _objc_msgSend$isFriendImmoTokenOrSlotOnline
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$keyRoleToShareOverride
+ _objc_msgSend$kmlVersionOverride
+ _objc_msgSend$longValue
+ _objc_msgSend$readerSupportedTransports
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedSettingsManager
+ _objc_msgSend$sharingPasswordRequired
+ _objc_msgSend$startShareAcceptanceFlowWithInvitation:completionHandler:
+ _objc_msgSend$supportedRadiosAsDataForTarget:
+ _objc_msgSend$tag
+ _objc_msgSend$timeIntervalForUserDefault:minTimeInterval:maxTimeInterval:defaultTimeInterval:
+ _objc_msgSend$updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:
+ _objc_msgSend$updateSharingAnalyticsWithConfig:completionHandler:
+ _objc_msgSend$updateVehicleServerSupportedVersions:
+ _objc_msgSend$updateVehicleSupportedAppletVersions:
+ _objc_msgSend$updateVehicleSupportedFrameworkVersions:
+ _objc_msgSend$useAppletVersionsForCertificationTesting
+ _objc_msgSend$useOldSignalingBitmap
+ _objc_msgSend$value
+ _objc_msgSend$valueAsUnsignedChar
+ _objc_msgSend$valueAsUnsignedShort
+ _objc_retain_x28
+ _sharedSettingsManager._sharedInstance
+ _sharedSettingsManager.onceToken
- -[DACarKeySharingMessage initWithGenericCrossPlatformSharingData:additionalDataDictionary:]
- -[DAKeyManagementSession requestImmobilizerTokenRefillForKeyWithIdentifier:callback:]
- -[DAKeyManagementSession setImmobilizerTokens:publicKey:forKeyWithIdentifier:callback:]
- -[DAKeyPairingSession requestBindingAttestationDataForManufacturer:callback:]
- -[DAKeyPairingSession requestImmobilizerTokenRefillForKeyWithIdentifier:callback:]
- -[DAKeyPairingSession setImmobilizerTokens:publicKey:forKeyWithIdentifier:callback:]
- -[DAKeySharingInvitationData passwordPiece]
- -[DAShareRecipientResult initFailureResultWithCrdentialIdentifier:error:]
- GCC_except_table25
- GCC_except_table38
- GCC_except_table41
- GCC_except_table45
- GCC_except_table48
- GCC_except_table70
- GCC_except_table8
- _KmlLogFunc2
- _KmlLogFunc_InternalOnly
- _KmlLogFunc_InternalOnly.cold.1
- _KmlSharingLogFunc
- _OBJC_IVAR_$_DAKeySharingInvitationData._passwordPiece
- _OBJC_IVAR_$_KmlDeviceConfigurationData._sharingInAChainTestFromFriend
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _SESEndPointPreWarm
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_DAKeyImmobilizerTokenUpdate
- __OBJC_$_PROTOCOL_METHOD_TYPES_DAKeyImmobilizerTokenUpdate
- __OBJC_$_PROTOCOL_REFS_DAKeyImmobilizerTokenUpdate
- __OBJC_LABEL_PROTOCOL_$_DAKeyImmobilizerTokenUpdate
- __OBJC_PROTOCOL_$_DAKeyImmobilizerTokenUpdate
- ___102-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke_2
- ___102-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:fromMailboxIdentifier:completionHandler:]_block_invoke_2
- ___105-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke_2
- ___105-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke_2
- ___107-[DAKeySharingSession sendSharingInvitationForKeyIdentifier:toIdsIdentifier:auth:config:completionHandler:]_block_invoke_2
- ___108-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke_2
- ___108-[DAKeySharingSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke_2
- ___108-[DAKeySharingSession setMailboxIdentifier:forOwnerKeyIdentifier:forInvitationIdentifier:completionHandler:]_block_invoke_2
- ___109-[DAKeySharingSession sendSilentSharingInvitationWithKeyIdentifier:config:groupIdentifier:completionHandler:]_block_invoke_2
- ___110-[DAKeySharingSession acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke_2
- ___111-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:fromMailboxIdentifier:completionHandler:]_block_invoke_2
- ___116-[DAKeySharingSession acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler:]_block_invoke_2
- ___122-[DAKeyManagementSession revokeNodesWithGroupIdentifiers:treesWithGroupIdentifier:authorizedByKeyWithIdentifier:callback:]_block_invoke_2
- ___133-[DAKeySharingSession createSharingInvitationsForKeyIdentifier:friendIdentifier:auth:ourBindingAttestation:config:completionHandler:]_block_invoke_2
- ___23-[DASession endSession]_block_invoke_2
- ___35-[DAKeyPairingSession startProbing]_block_invoke_2
- ___35-[DAManager establishXpcConnection]_block_invoke_2
- ___35-[DAManager establishXpcConnection]_block_invoke_2.cold.1
- ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke_2
- ___46-[DAManager createPairingSessionWithDelegate:]_block_invoke_2
- ___46-[DAManager createSharingSessionWithDelegate:]_block_invoke_2
- ___47-[DAKeySharingSession cancelSharingInvitation:]_block_invoke_2
- ___49-[DAManager createManagementSessionWithDelegate:]_block_invoke_2
- ___54-[DAKeyManagementSession deleteKey:completionHandler:]_block_invoke_2
- ___59-[DAKeyManagementSession localDeleteKey:completionHandler:]_block_invoke_2
- ___65-[DAKeySharingSession requestInviteWithConfig:completionHandler:]_block_invoke_2
- ___69-[DAKeyManagementSession listReceivedSharingInvitationsWithCallback:]_block_invoke_2
- ___71-[DAKeySharingSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke_2
- ___72-[DAKeySharingSession retryPasscode:forKeyIdentifier:completionHandler:]_block_invoke_2
- ___73-[DAKeyManagementSession cancelInvitationWithIdentifier:reason:callback:]_block_invoke_2
- ___74-[DAKeyManagementSession cancelAllFriendInvitationsWithCompletionHandler:]_block_invoke_2
- ___74-[DAKeyManagementSession getPreTrackRequestForKeyWithIdentifier:callback:]_block_invoke_2
- ___74-[DAKeyManagementSession listSharingInvitationsForKeyIdentifier:callback:]_block_invoke_2
- ___74-[DAKeyManagementSession removeSharingInvitationWithId:completionHandler:]_block_invoke_2
- ___74-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke_2
- ___75-[DAKeySharingSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke_2
- ___77-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke_2
- ___78-[DAKeyManagementSession countImmobilizerTokensForKeyWithIdentifier:callback:]_block_invoke_2
- ___78-[DAKeyManagementSession setBindingAttestation:forKeyWithIdentifier:callback:]_block_invoke_2
- ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2
- ___79-[DAKeySharingSession retryPasscode:forInvitationIdentifier:completionHandler:]_block_invoke_2
- ___80-[DAKeySharingSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke_2
- ___80-[DAManager handleSharingMessage:forInvitationIdentifier:fromMailboxIdentifier:]_block_invoke_2
- ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2
- ___82-[DAKeySharingSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke_2
- ___83-[DAKeyManagementSession ppidRequestForInvitationWithIdentifier:completionHandler:]_block_invoke_2
- ___83-[DAKeySharingSession authorizeSharingInvitationIdentifier:auth:completionHandler:]_block_invoke_2
- ___83-[DAKeySharingSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke_2
- ___85-[DAKeyManagementSession requestBindingAttestationDataForKeyWithIdentifier:callback:]_block_invoke_2
- ___85-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke_2
- ___86-[DAKeyManagementSession setProductPlanIdentifier:forInvitationIdentifier:completion:]_block_invoke_2
- ___87-[DAKeySharingSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke_2
- ___88-[DAKeySharingSession handleInitiatorMessage:forInvitationIdentifier:completionHandler:]_block_invoke_2
- ___88-[DAKeySharingSession handleRecipientMessage:forInvitationIdentifier:completionHandler:]_block_invoke_2
- ___90-[DAKeyManagementSession getPreTrackRequestForInvitationWithIdentifier:completionHandler:]_block_invoke_2
- ___90-[DAKeyManagementSession removeSharedKeysWithIdentifiers:ownerKeyWithIdentifier:callback:]_block_invoke_2
- ___90-[DAKeySharingSession createSilentSharingInvitationWithGroupIdentifier:completionHandler:]_block_invoke_2
- ___92-[DAKeyManagementSession revokeKeysWithIdentifiers:sharedByOwnerKeyWithIdentifier:callback:]_block_invoke_2
- ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke_2
- ___93-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]_block_invoke
- ___93-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]_block_invoke_2
- ___96-[DAKeySharingSession acceptSharingInvitation:fromMailboxIdentifier:passcode:completionHandler:]_block_invoke_2
- ___97-[DAKeyManagementSession cancelInvitationsWithIdentifiers:sentByOwnerKeyWithIdentifier:callback:]_block_invoke_2
- ___98-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke_2
- ___98-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke_2
- ___block_literal_global.11
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.129
- ___block_literal_global.370
- ___block_literal_global.438
- ___block_literal_global.49
- ___block_literal_global.8
- ___isInternalBuild_block_invoke
- _decodeWithData:error:.allowedClasses.368
- _decodeWithData:error:.allowedClasses.436
- _decodeWithData:error:.pred.367
- _decodeWithData:error:.pred.435
- _isInternalBuild.onceToken
- _objc_msgSend$acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:
- _objc_msgSend$acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:sharingFlow:productPlanIdentifier:completionHandler:
- _objc_msgSend$initFailureResultWithCrdentialIdentifier:error:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithFormat:arguments:
- _objc_msgSend$integerForKey:
- _objc_msgSend$sharingFlow
- _objc_msgSend$updateConfiguration:forKeyWithIdentifier:completionHandler:
CStrings:
+ "\tKey Role          : 0x%04X\n"
+ "\tSharing Flow         : 0x%02X\n"
+ "%04X,"
+ "%s : %i : "
+ "%s : %i : %@"
+ "%s : %i : --- end %@ ---"
+ "%s : %i : --- start %@ ---"
+ "%s : %i : : %d"
+ "%s : %i : :%@"
+ "%s : %i : API Deprecated, please stop use"
+ "%s : %i : Agreed KML framework version is unknown"
+ "%s : %i : Can't cancel invite missing invitationIdentifier"
+ "%s : %i : Cancel TLV not found"
+ "%s : %i : Cancel code TLV not found"
+ "%s : %i : Cancel invite with id : %@"
+ "%s : %i : Car sent SharingInAChain version mailboxMapping Data"
+ "%s : %i : Checking availability: Framework upgrade from : 0x%04hx, to : 0x%04lx"
+ "%s : %i : Checking availability: VehicleServer upgrade from : 0x%04hx, to : 0x%04lx"
+ "%s : %i : Config: %@"
+ "%s : %i : DAKeyManager: XPC connection already established"
+ "%s : %i : DCK Identifier : %@"
+ "%s : %i : Deprecated"
+ "%s : %i : Deprecated API, use setTrackingReceipt:decryptedDeviceData:forKeyWithIdentifier: instead"
+ "%s : %i : Deprecated function"
+ "%s : %i : DeviceConfig Data : %@"
+ "%s : %i : Did not find version appropriate data to initialize Mailbox mapping, using defaults"
+ "%s : %i : Endpoint not set"
+ "%s : %i : Expected to find outer tag, but did not"
+ "%s : %i : Failed to get remote proxy"
+ "%s : %i : Found Mailbox mapping data to parse"
+ "%s : %i : Found default product plan data for %@ : (%@)"
+ "%s : %i : Found device config data to parse in outer tag"
+ "%s : %i : Found oem specific data for %@ : (%@)"
+ "%s : %i : Found sharing config data"
+ "%s : %i : IDS based sharing is now deprecated, please use cross platform APIs instead"
+ "%s : %i : Internal released"
+ "%s : %i : Invalid EP type %d"
+ "%s : %i : Invalid MailboxMapping Data"
+ "%s : %i : Invalid callback queue"
+ "%s : %i : Invalid node group identifier (%@) provided, must be 2 bytes (4 chars)"
+ "%s : %i : Invalid slotId %@:"
+ "%s : %i : Invalid tree group identifier (%@) provided, must be 2 bytes (4 chars)"
+ "%s : %i : Invitation Id %@"
+ "%s : %i : Invitation Identifier : %@"
+ "%s : %i : InvitationId : %@"
+ "%s : %i : InvitationIdentifier - %@"
+ "%s : %i : Key id = %@"
+ "%s : %i : Key identifier required for share initiator"
+ "%s : %i : KeyIdentifier : %@, friendIdentifier: %@"
+ "%s : %i : KeyIdentifier : %@, remoteIdsId: %@"
+ "%s : %i : KeyIdentifier : %@, uuid: %@"
+ "%s : %i : KeyIdentifier: %@"
+ "%s : %i : KmlVersionOverride = %@"
+ "%s : %i : Let's downgrade to v1"
+ "%s : %i : Looking for %@, or back up %@"
+ "%s : %i : Looking for available upgrade of Framework version"
+ "%s : %i : Looking for available upgrade of VehicleServer version"
+ "%s : %i : MailboxIdentifier - %@"
+ "%s : %i : MailboxMapping Data : %@"
+ "%s : %i : Manufacturer: %@"
+ "%s : %i : Max attestation count must be at least 2 for sharing in a chain"
+ "%s : %i : Mismatch in expected mailbox version (0x%02X) and received version (0x%02X)"
+ "%s : %i : Missing Update config"
+ "%s : %i : Missing analytics data in update config"
+ "%s : %i : Missing default value for key: %@, assuming default is NO"
+ "%s : %i : Missing masterKey or identifier"
+ "%s : %i : Missing target dictionary with keyName : %@"
+ "%s : %i : No Data to initalize Mailbox mapping, using defaults"
+ "%s : %i : No invitation identifiers supplied to update config"
+ "%s : %i : No override found"
+ "%s : %i : No vehicle supported versions data"
+ "%s : %i : Null argument provided"
+ "%s : %i : Null argument provided."
+ "%s : %i : Null arguments provided"
+ "%s : %i : Null arguments provided. Session : %@, seid : %@"
+ "%s : %i : Only found default product plan data, so using it"
+ "%s : %i : Original key name: %@ ,  truncated key name: %@"
+ "%s : %i : OwnerKeyIdentifier - %@, InvitationIdentifier - %@"
+ "%s : %i : OwnerKeyIdentifier: %@"
+ "%s : %i : Proxy end session"
+ "%s : %i : Ran out of randomizer counter. Abort!"
+ "%s : %i : Received duplicated tag: 0x%02X"
+ "%s : %i : Requested Versions = { %@ }"
+ "%s : %i : Result : %@"
+ "%s : %i : Result of decrypting vehicleMobilizationData: %@"
+ "%s : %i : Result: %@"
+ "%s : %i : Result: %d"
+ "%s : %i : Server provided PPID data: %@"
+ "%s : %i : Sharing In a chain does not support offline immo tokens"
+ "%s : %i : SharingInAChain override %@"
+ "%s : %i : Skip %@, since it has non string value in json"
+ "%s : %i : Skip %@, since it is expected to have value of unsupported class"
+ "%s : %i : Skip %@, since value is nil"
+ "%s : %i : Sync agreed vehicle version to v1"
+ "%s : %i : TLV: %02x : %@"
+ "%s : %i : TLV: Underflow"
+ "%s : %i : TLV: Underflow: tag=0x%x"
+ "%s : %i : TLV: Underflow: tag=0x%x len=%u"
+ "%s : %i : TLV: Value too large: %@"
+ "%s : %i : TLV: adding tag:0x%x, len:%u"
+ "%s : %i : TLV: found %lu tlvs"
+ "%s : %i : TLV: tag and length is 0"
+ "%s : %i : This API is deprecated, please stop use"
+ "%s : %i : This API is deprecated, please use DAManager version instead"
+ "%s : %i : This API is deprecated, please use updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler instead"
+ "%s : %i : This API is deprecated, use cancelSharingInvitation:completionHandler instead"
+ "%s : %i : This API is deprecated, use getPreTrackRequestForInvitationWithIdentifier: instead"
+ "%s : %i : This API is deprecated, use retryPasscode:forInvitationIdentifier:completionHandler: instead"
+ "%s : %i : This API is deprecated, use startKeyPairingWithPassword:displayName:transport:bindingAttestation: instead"
+ "%s : %i : This function is deprecated, please use acceptInvitationWithIdentifier:passcode:completionHandler instead"
+ "%s : %i : This function is deprecated, please use either [DAKeySharingSession handleRecipientMessage] or [DAKeySharingSession handleInititiatorMessage] instead"
+ "%s : %i : This function is deprecated, please use startShareAcceptanceFlowWithInvitation:completionHandler instead"
+ "%s : %i : This method is deprecated, please use ppidRequestForInvitationWithIdentifier:completionHandler: instead"
+ "%s : %i : This method is deprecated, please use readerInformationForInvitationWithIdentifier:completionHandler: instead"
+ "%s : %i : This method will be deprecated soon. Start using acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler"
+ "%s : %i : This method will be deprecated soon. Start using acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler"
+ "%s : %i : This reader doesn't support UWB. Nothing to disable locally."
+ "%s : %i : Transport = %@, displayName: %@"
+ "%s : %i : Treating unknown sharing version as v1 for sharing"
+ "%s : %i : Treating unknown vehicle applet version as v1"
+ "%s : %i : Treating unknown vehicle version as v1"
+ "%s : %i : UTF8 encoded friendly name is less than %ld chars : %@"
+ "%s : %i : UWB disabled locally, config saved for sharing"
+ "%s : %i : UWB is disabled for local use, but available for sharing."
+ "%s : %i : Upgrade disabled for friend key by settings"
+ "%s : %i : Upgrade disabled for owner paired key by settings"
+ "%s : %i : Upgrade eligible"
+ "%s : %i : Vehicle never provided a supported versiosn list"
+ "%s : %i : We already have car provided ppid. Ignore the server provided value"
+ "%s : %i : We are already at v1, nothing to downgrade"
+ "%s : %i : We prefer SharingInAChain version"
+ "%s : %i : We will use spec_v1 mailboxMapping data"
+ "%s : %i : XPC Connection created"
+ "%s : %i : XPC Proxy error %@"
+ "%s : %i : XPC proxy not available"
+ "%s : %i : anonymizedDsid.length = %lu, readerIdentifier.length = %lu"
+ "%s : %i : cchkdf failed with %d"
+ "%s : %i : counter : %u ; digits scored : %u"
+ "%s : %i : date five minutes from %@"
+ "%s : %i : date now %@"
+ "%s : %i : displayName is empty"
+ "%s : %i : endPointPrivacyDecryption: got decrypted data: %@"
+ "%s : %i : endPointPrivacyDecryption: return error: %@"
+ "%s : %i : groupIdentifier: %@"
+ "%s : %i : infinite date %@"
+ "%s : %i : invitationIdentifier: %@"
+ "%s : %i : json data is nil"
+ "%s : %i : json serialization error : %@"
+ "%s : %i : jsonObject : %@"
+ "%s : %i : key count = %lu"
+ "%s : %i : keyGroupIdentifier List: %@"
+ "%s : %i : keyIdentifier List: %@"
+ "%s : %i : keyIdentifier is empty"
+ "%s : %i : keyIdentifier: %@"
+ "%s : %i : keyRoleToShareOverride: %@"
+ "%s : %i : length of : longTermSecret:%u; seed:%u; desiredPasscode:%u"
+ "%s : %i : listKeysWithSession: key count = %lu"
+ "%s : %i : mailboxIdentifier - %@"
+ "%s : %i : manufacturer is empty"
+ "%s : %i : nothing to parse"
+ "%s : %i : password is empty"
+ "%s : %i : proxyError: %@"
+ "%s : %i : treeGroupIdentifier List: %@"
+ "%s : %i : versionData: %@"
+ "-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]"
+ "-[DAKeyManagementSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke"
+ "-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]"
+ "-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:]_block_invoke"
+ "-[DAKeyPairingSession startKeyPairingWithPassword:displayName:]"
+ "-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:]"
+ "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession cancelSharingInvitation:completionHandler:]"
+ "-[DAKeySharingSession cancelSharingInvitation:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]"
+ "-[DAKeySharingSession readerInformationForInvitationWithIdentifier:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]"
+ "-[DAKeySharingSession startShareAcceptanceFlowWithInvitation:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]"
+ "-[DAKeySharingSession updateSharingAnalyticsWithConfig:completionHandler:]_block_invoke"
+ "-[KmlCancelMessage initWithData:]"
+ "-[KmlDeviceConfigurationData asData]"
+ "-[KmlDeviceConfigurationData isValidForKmlVersion:transport:]"
+ "-[KmlDeviceConfigurationData removeUwbSupportLocally]"
+ "-[KmlDeviceConfigurationData updatePPIDWithServerProvidedData:]"
+ "-[KmlDeviceConfigurationData updateSharingConfigWithData:]"
+ "-[KmlMailboxMappingData asData]"
+ "-[KmlMailboxMappingData initWithData:preferredVersion:]"
+ "-[KmlMailboxMappingData isValid]"
+ "-[KmlSettingsManager defaultBoolValueForSetting:]"
+ "-[KmlTlv valueAsUnsignedLong]"
+ "-[KmlVersions downgradePreferredVersion]"
+ "-[KmlVersions getAgreedBluetoothVersionsTlv]"
+ "-[KmlVersions hasUpgradeForVersionType:versions:isOwnerPairedKey:]"
+ "-[KmlVersions updateSupportedFrameworkVersionsForSharing:]"
+ "0x%04lx, "
+ "@\"DAKeySharingAnalyticsData\""
+ "@\"NSDictionary\""
+ "@\"NSNumber\""
+ "@\"NSUserDefaults\""
+ "@\"SESConfigDCK\""
+ "@20@0:8C16"
+ "@20@0:8I16"
+ "@20@0:8S16"
+ "@24@0:8S16C20"
+ "@24@0:8S16I20"
+ "@24@0:8S16S20"
+ "@24@0:8q16"
+ "@28@0:8@16B24"
+ "@28@0:8@16S24"
+ "@28@0:8S16@20"
+ "AdditionalConfigurationData:\n"
+ "AllowFleetOP"
+ "AllowRadioMismatchInUpgrade"
+ "AllowedFleetManufacturers"
+ "AllowedFleetServiceProviders"
+ "B20@0:8C16"
+ "B24@0:8Q16"
+ "B24@0:8S16S20"
+ "B28@0:8S16q20"
+ "B32@0:8@16^@24"
+ "B56@0:8Q16@24@32@40^@48"
+ "BindingAttestationSkip"
+ "BluetoothHceSessionTimeLimit"
+ "BluetoothLoyaltyAndPaymentSessionTimeLimit"
+ "BypassAccountInfoHash"
+ "C16@0:8"
+ "Cert chain not signed by a trusted root"
+ "DAAdditionalConfigurationData"
+ "DAKeySharingAnalyticsData"
+ "DAKeySharingAnalyticsData:\n"
+ "DASharingAnalyticsUpdateConfig"
+ "DisableFleetKeyStrictShareInitCertChainValidation"
+ "DisablePrivateKeyStrictShareInitCertChainValidation"
+ "Failed to connect to network"
+ "HceSessionTimeout"
+ "I16@0:8"
+ "IgnoreInvalidAttestationPackageSignature"
+ "KmlMailboxMappingData"
+ "KmlSettingsManager"
+ "MockFleetEndpointCert"
+ "MockFleetExtCaCert"
+ "MockFleetIntermediateCert"
+ "NFCHceSessionTimeLimit"
+ "NFCLoyaltyAndPaymentSessionTimeLimit"
+ "OPTransactionTimeout"
+ "Opt2AuthDeletionAlarmDurationSeconds"
+ "PretendBindingAttestationUsed"
+ "Provided cert chain not trusted"
+ "SecurityPolicy"
+ "T@\"DAKeySharingAnalyticsData\",R,N,V_analyticsData"
+ "T@\"NSArray\",R,N,V_invitationIdentifiers"
+ "T@\"NSData\",&,N,V_additionalMailboxSettingAsData"
+ "T@\"NSData\",&,N,V_confMailboxSettingAsData"
+ "T@\"NSData\",&,N,V_deviceBtIntroKey"
+ "T@\"NSData\",&,N,V_deviceBtOOBKey"
+ "T@\"NSData\",&,N,V_initiatorSupportedFrameworkVersionsData"
+ "T@\"NSData\",&,N,V_mfiPPID"
+ "T@\"NSData\",&,N,V_oemSpecificContentAsData"
+ "T@\"NSData\",&,N,V_onlineBleOOBMasterKeyOverride"
+ "T@\"NSData\",&,N,V_privateMailboxSettingAsData"
+ "T@\"NSData\",&,N,V_readerBtIRK"
+ "T@\"NSData\",&,N,V_readerBtIdAddress"
+ "T@\"NSData\",&,N,V_sharingPasswordLengthAsData"
+ "T@\"NSData\",&,N,V_supportedKeyProfiles"
+ "T@\"NSData\",&,N,V_v3ConfMailboxSettingAsData"
+ "T@\"NSData\",&,N,V_v3PrivateMailboxSettingAsData"
+ "T@\"NSData\",&,N,V_vehicleSupportedFrameworkVersionsData"
+ "T@\"NSNumber\",R,N,V_keyRole"
+ "TB,N,V_carSupportsUpdateAttestation"
+ "TB,N,V_didParseDataSuccessfully"
+ "TB,N,V_keyTrackingReceiptRequired"
+ "TB,N,V_onlineAttestationDeliverySupported"
+ "TB,N,V_readerSupportsLELR"
+ "TB,N,V_readerSupportsNfc"
+ "TB,N,V_readerSupportsUwb"
+ "TB,N,V_sharingPasswordRequired"
+ "TB,N,V_uwbDisabledLocally"
+ "TC,N,V_cccCode"
+ "TC,N,V_immoTokenConfig"
+ "TC,N,V_maxOfflineAttestationCount"
+ "TC,N,V_sharingPasswordLength"
+ "TC,R,N,V_immoTokenLength"
+ "TC,R,N,V_mailboxVersion"
+ "TC,R,N,V_slotIdentifierLength"
+ "TI,N,V_kmlCode"
+ "TLVWithJustTag:"
+ "TLVWithTag:unsignedChar:"
+ "TLVWithTag:unsignedLongValue:"
+ "TLVWithTag:unsignedShort:"
+ "TLVWithTag:value:"
+ "TLVsWithData:"
+ "TS,R,N,V_attestationPackageLength"
+ "TS,R,N,V_keyAttestationStartOffset"
+ "TS,R,N,V_mailboxEndOffset"
+ "TS,R,N,V_signalingBitmapOffset"
+ "TS,R,N,V_signerSlotIdListOffset"
+ "TS,R,N,V_slotIdBitmapOffset"
+ "TS,R,N,V_slotIdListOffset"
+ "TS,R,N,V_vehicleProprietaryDataOffset"
+ "Tq,R,N,V_sharingFlow"
+ "UseAppletVersionsForCertificationTesting"
+ "UseOldKeyConfigTag"
+ "UseOldKeyTrackingTag"
+ "UseOldSignalingBitmap"
+ "Vv32@0:8@\"DACarKeySharingMessage\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"DASharingAnalyticsUpdateConfig\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"DAShareRecipientResult\">24"
+ "Vv48@0:8@\"NSData\"16@\"NSString\"24@\"DAAdditionalConfigurationData\"32@?<v@?@\"NSError\">40"
+ "Vv64@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"DAAlishaKeyEncryptedRequest\"48@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">56"
+ "_allMailboxMappingTlvs"
+ "_analyticsData"
+ "_attestationPackageLength"
+ "_dckConfig"
+ "_defaultSLGValues"
+ "_didParseDataSuccessfully"
+ "_immoTokenLength"
+ "_invitationIdentifiers"
+ "_keyAttestationListStartOffset"
+ "_keyAttestationStartOffset"
+ "_mailboxEndOffset"
+ "_mailboxVersion"
+ "_preferredVersion"
+ "_preferredVersionTlvs"
+ "_signalingBitmapOffset"
+ "_signerSlotIdListOffset"
+ "_slotIdBitmapOffset"
+ "_slotIdListOffset"
+ "_slotIdentifierLength"
+ "_useOldSignalingBitmap"
+ "_userDefaults"
+ "_vehicleProprietaryDataOffset"
+ "_vehicleProprietaryDataOffset_v3"
+ "acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:productPlanIdentifier:completionHandler:"
+ "addObjectsFromArray:"
+ "additionalMailboxSettingAsData"
+ "allowFleetOwnerPairing"
+ "allowRadioMismatchForTest"
+ "analyticsData"
+ "asData"
+ "attestationPackageLength"
+ "boolValueForUserDefault:"
+ "buildNonOSPPreShareTlvOverride"
+ "bypassAccountInfoHash"
+ "carSupportsUpdateAttestation"
+ "cccCode"
+ "confMailboxSettingAsData"
+ "d16@0:8"
+ "d48@0:8@16d24d32d40"
+ "debug.BuildNonOSPPreShareTlvOverride"
+ "debug.EmulateNFCOnlyDevice"
+ "defaultBoolValueForSetting:"
+ "deviceBtIntroKey"
+ "deviceBtOOBKey"
+ "didParseDataSuccessfully"
+ "disableFleetKeyStrictShareInitCertChainValidation"
+ "disableOptTwoShareInitCertChainValidation"
+ "disablePrivateKeyStrictShareInitCertChainValidation"
+ "doesAgreedVersionSupportOnlineBleKeys"
+ "doesVersion:support:"
+ "doubleForKey:"
+ "downgradePreferredVersion"
+ "emulateNFCOnlyDevice"
+ "fleetManufacturerAllowListWithError:"
+ "fleetServiceProviderAllowListWithError:"
+ "getAgreedBluetoothVersionsTlv"
+ "getKmlSupportedVersionsTlvAsShareRecipient"
+ "getMaskToIndicateKeyAttestationConsumed"
+ "getMaskToIndicateKeyAttestationSaved"
+ "getMaskToIndicateOemPropDataConsumed"
+ "getMaskToIndicateOemPropDataSaved"
+ "getMaskToIndicateSlotIdListConsumed"
+ "getMaskToIndicateSlotIdListSaved"
+ "getRootCertificateFor:keyID:error:"
+ "getRootCertificateFor:keyId:"
+ "getSettingForKey:error:"
+ "getVehicleSupportedVersionsData"
+ "hasUpgradeForVersionType:versions:isOwnerPairedKey:"
+ "ignoreInvalidAttestationPackageSignature"
+ "immoTokenConfig"
+ "immoTokenLength"
+ "initFailureResultWithCredentialIdentifier:error:"
+ "initForBringOtherKey"
+ "initSharingCancelledResultWithResponse:error:"
+ "initWithCCCErrorCode:"
+ "initWithData:"
+ "initWithData:outerTag:"
+ "initWithData:preferredVersion:"
+ "initWithEndpoint:downgradeFrameworkSetting:"
+ "initWithInvitationIdentifiers:keyIdentifier:recipientFlow:analyticsData:"
+ "initWithKeyRole:"
+ "initWithKmlErrorCode:"
+ "initWithSharingFlow:"
+ "initiatorSupportedFrameworkVersionsData"
+ "invitationIdentifiers"
+ "isDCKConfigurationAvailableFor:error:"
+ "isFriendImmoTokenOrSlotOnline"
+ "isImmoTokenNeeded"
+ "isKeyAttestationSetByCarInSignalingBitmap:"
+ "isKeyAttestationSetByDeviceInSignalingBitmap:"
+ "isManufacturerSupported:error:"
+ "isOemPropDataSetByCarInSignalingBitmap:"
+ "isOemPropDataSetByDeviceInSignalingBitmap:"
+ "isOwnerImmoTokenOrSlotOnline"
+ "isSlotIdListSetByCarInSignalingBitmap:"
+ "isSlotIdListSetByDeviceInSignalingBitmap:"
+ "isSubsetOfSet:"
+ "isValid"
+ "isValidForKmlVersion:transport:"
+ "keyAttestationStartOffset"
+ "keyRoleToShareOverride"
+ "keyTrackingReceiptRequired"
+ "kmlCode"
+ "kmlVersionOverride"
+ "longValue"
+ "mailboxEndOffset"
+ "mailboxVersion"
+ "maxOfflineAttestationCount"
+ "mfiPPID"
+ "mockFleetEndpointCert"
+ "mockFleetExtCaCert"
+ "mockFleetIntermediateCert"
+ "oemSpecificContentAsData"
+ "onlineAttestationDeliverySupported"
+ "onlineBleOOBMasterKeyOverride"
+ "opt2AuthDeletionAlarmDurationSeconds"
+ "ourSupportedFrameworkVersionsAsCAString"
+ "pretendBindingAttestationUsed"
+ "privateMailboxSettingAsData"
+ "readerBtIRK"
+ "readerBtIdAddress"
+ "readerInformationForInvitationWithIdentifier:completionHandler:"
+ "readerSupportedTransports"
+ "readerSupportsLELR"
+ "readerSupportsNfc"
+ "readerSupportsUwb"
+ "removeUwbSupportLocally"
+ "setAdditionalMailboxSettingAsData:"
+ "setCarSupportsUpdateAttestation:"
+ "setCccCode:"
+ "setConfMailboxSettingAsData:"
+ "setDeviceBtIntroKey:"
+ "setDeviceBtOOBKey:"
+ "setDidParseDataSuccessfully:"
+ "setImmoTokenConfig:"
+ "setInitiatorSupportedFrameworkVersionsData:"
+ "setKeyTrackingReceiptRequired:"
+ "setKmlCode:"
+ "setMaxOfflineAttestationCount:"
+ "setMfiPPID:"
+ "setOemSpecificContentAsData:"
+ "setOnlineAttestationDeliverySupported:"
+ "setOnlineBleOOBMasterKeyOverride:"
+ "setPrivateMailboxSettingAsData:"
+ "setReaderBtIRK:"
+ "setReaderBtIdAddress:"
+ "setReaderSupportsLELR:"
+ "setReaderSupportsNfc:"
+ "setReaderSupportsUwb:"
+ "setSharingPasswordLength:"
+ "setSharingPasswordLengthAsData:"
+ "setSharingPasswordRequired:"
+ "setSupportedKeyProfiles:"
+ "setUwbDisabledLocally:"
+ "setV3ConfMailboxSettingAsData:"
+ "setV3PrivateMailboxSettingAsData:"
+ "setVehicleSupportedFrameworkVersionsData:"
+ "setWithArray:"
+ "sharedSettingsManager"
+ "sharingConfigForFriendAsData"
+ "sharingPasswordLength"
+ "sharingPasswordLengthAsData"
+ "sharingPasswordRequired"
+ "signalingBitmapOffset"
+ "signerSlotIdListOffset"
+ "skipWaitingForBindingAttestation"
+ "slotIdBitmapOffset"
+ "slotIdListOffset"
+ "slotIdentifierLength"
+ "startShareAcceptanceFlowWithInvitation:completionHandler:"
+ "supportedKeyProfiles"
+ "supportedRadiosAsDataForTarget:"
+ "tag"
+ "timeIntervalForUserDefault:minTimeInterval:maxTimeInterval:defaultTimeInterval:"
+ "updateConfiguration:forKeyWithIdentifier:additionalConfigurationData:completionHandler:"
+ "updatePPIDWithServerProvidedData:"
+ "updateSharingAnalyticsWithConfig:completionHandler:"
+ "updateSharingConfigWithData:"
+ "updateSupportedFrameworkVersionsForSharing:"
+ "updateSupportedRadiosWithData:"
+ "updateVehicleServerSupportedVersions:"
+ "updateVehicleSupportedAppletVersions:"
+ "updateVehicleSupportedBluetoothVersions:"
+ "updateVehicleSupportedFrameworkVersions:"
+ "upgradeForVersionType:version:"
+ "useAppletVersionsForCertificationTesting"
+ "useBasicSecurityPolicy"
+ "useOldKeyConfigTag"
+ "useOldKeyTrackingTag"
+ "useOldSignalingBitmap"
+ "uwbDisabledLocally"
+ "v20@0:8C16"
+ "v20@0:8I16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8Q16Q24"
+ "v3ConfMailboxSettingAsData"
+ "v3PrivateMailboxSettingAsData"
+ "value"
+ "valueAsUnsignedChar"
+ "valueAsUnsignedLong"
+ "valueAsUnsignedShort"
+ "vehicleProprietaryDataOffset"
+ "vehicleSupportedFrameworkVersionsData"
+ "{_DAVersionUpgrade=QBQQ}36@0:8Q16@24B32"
- "%s : %d : %@"
- "%s : %d : %s : %@"
- "%{public}@"
- "--- end %@ ---"
- "--- start %@ ---"
- "-[DAKeyManagementSession commitUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke_2"
- "-[DAKeyManagementSession hasUpgradeAvailableForKeyWithIdentifier:versionType:versions:completionHandler:]_block_invoke_2"
- "-[DAKeyManagementSession requestImmobilizerTokenRefillForKeyWithIdentifier:callback:]"
- "-[DAKeyManagementSession revertUpgradeForKeyWithIdentifier:versionType:version:completionHandler:]_block_invoke_2"
- "-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2"
- "-[DAKeyManagementSession setImmobilizerTokens:publicKey:forKeyWithIdentifier:callback:]"
- "-[DAKeyManagementSession updateConfiguration:forKeyWithIdentifier:completionHandler:]_block_invoke_2"
- "-[DAKeyManagementSession upgradeKeyWithIdentifier:versionType:version:upgradeInformation:completionHandler:]_block_invoke_2"
- "-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke_2"
- "-[DAKeyPairingSession requestBindingAttestationDataForManufacturer:callback:]"
- "-[DAKeyPairingSession requestImmobilizerTokenRefillForKeyWithIdentifier:callback:]"
- "-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2"
- "-[DAKeyPairingSession setImmobilizerTokens:publicKey:forKeyWithIdentifier:callback:]"
- "-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke_2"
- "-[DAKeyPairingSession startProbing]_block_invoke_2"
- "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]_block_invoke"
- "-[DAKeySharingSession cancelSharingInvitation:]_block_invoke_2"
- "-[DAManager createManagementSessionWithDelegate:]_block_invoke_2"
- "-[DAManager createPairingSessionWithDelegate:]_block_invoke_2"
- "-[DAManager createSharingSessionWithDelegate:]_block_invoke_2"
- "-[DAManager establishXpcConnection]_block_invoke_2"
- "-[DASession endSession]_block_invoke_2"
- ": %d"
- ":%@"
- "Can't cancel invite missing invitationIdentifier"
- "Cancel invite with id : %@"
- "DAKeyImmobilizerTokenUpdate"
- "DAKeyManager: XPC connection already established"
- "DCK Identifier : %@"
- "Deprecated"
- "Deprecated API"
- "Deprecated function"
- "Failed to get remote proxy"
- "Found default product plan data for %@ : (%@)"
- "Found device config data to parse in outer tag"
- "Found oem specific data for %@ : (%@)"
- "Internal released"
- "Invalid EP type %d"
- "Invalid callback queue"
- "Invalid slotId %@:"
- "Invitation Id %@"
- "Invitation Identifier : %@"
- "InvitationId : %@"
- "InvitationIdentifier - %@"
- "Key id = %@"
- "KeyIdentifier : %@, friendIdentifier: %@"
- "KeyIdentifier : %@, remoteIdsId: %@"
- "KeyIdentifier : %@, uuid: %@"
- "KeyIdentifier: %@"
- "Looking for %@, or back up %@"
- "MailboxIdentifier - %@"
- "Manufacturer: %@"
- "Missing masterKey or identifier"
- "Missing target dictionary with keyName : %@"
- "No override found"
- "No vehicle supported versions data"
- "Null argument provided"
- "Null argument provided."
- "Null arguments provided"
- "Null arguments provided. Session : %@, seid : %@"
- "Only found default product plan data, so using it"
- "Original key name: %@ ,  truncated key name: %@"
- "OwnerKeyIdentifier - %@, InvitationIdentifier - %@"
- "OwnerKeyIdentifier: %@"
- "Proxy end session"
- "Ran out of randomizer counter. Abort!"
- "Received duplicated tag: 0x%02X"
- "Result : %@"
- "Result of decrypting vehicleMobilizationData: %@"
- "Result: %@"
- "Result: %d"
- "Sharing Flow          : %ld\n"
- "SharingInAChain override %@"
- "Skip %@, since it has non string value in json"
- "Skip %@, since it is expected to have value of unsupported class"
- "Skip %@, since value is nil"
- "T@\"NSString\",R,N,V_passwordPiece"
- "TLV: %02x : %@"
- "TLV: Underflow"
- "TLV: Underflow: tag=0x%x"
- "TLV: Underflow: tag=0x%x len=%u"
- "TLV: Value too large: %@"
- "TLV: adding tag:0x%x, len:%u"
- "TLV: found %lu tlvs"
- "TLV: tag and length is 0"
- "This function is deprecated, please use acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler instead"
- "This method is deprecated. Please stop use."
- "This method will be deprecated soon. Start using acceptCrossPlatformInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler"
- "This method will be deprecated soon. Start using acceptSharingInvitationWithIdentifier:passcode:productPlanIdentifier:completionHandler"
- "Transport = %@, displayName: %@"
- "Treating unknown vehicle applet version as v1"
- "Treating unknown vehicle version as v1"
- "UTF8 encoded friendly name is less than %ld chars : %@"
- "UWB is disabled for local use, but available for sharing."
- "UserDefault: %@"
- "Valid endpoint not set"
- "Vv72@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@\"DAAlishaKeyEncryptedRequest\"56@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">64"
- "Vv72@0:8@16@24@32@40q48@56@?64"
- "XPC Connection created"
- "XPC Proxy error %@"
- "XPC proxy not available"
- "_passwordPiece"
- "_sharingInAChainTestFromFriend"
- "acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:sharingFlow:productPlanIdentifier:completionHandler:"
- "anonymizedDsid.length = %lu, readerIdentifier.length = %lu"
- "cchkdf failed with %d"
- "counter : %u ; digits scored : %u"
- "date five minutes from %@"
- "date now %@"
- "displayName is empty"
- "endPointPrivacyDecryption: got decrypted data: %@"
- "endPointPrivacyDecryption: return error: %@"
- "groupIdentifier: %@"
- "infinite date %@"
- "initFailureResultWithCrdentialIdentifier:error:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithGenericCrossPlatformSharingData:additionalDataDictionary:"
- "integerForKey:"
- "invitationIdentifier: %@"
- "json data is nil"
- "json serialization error : %@"
- "jsonObject : %@"
- "key count = %lu"
- "keyGrouoIdentifier List: %@"
- "keyIdentifier List: %@"
- "keyIdentifier is empty"
- "keyIdentifier: %@"
- "length of : longTermSecret:%u; seed:%u; desiredPasscode:%u"
- "listKeysWithSession: key count = %lu"
- "mailboxIdentifier - %@"
- "manufacturer is empty"
- "nothing to parse"
- "password is empty"
- "passwordPiece"
- "proxyError: %@"
- "requestImmobilizerTokenRefillForKeyWithIdentifier:callback:"
- "setImmobilizerTokens:publicKey:forKeyWithIdentifier:callback:"
- "treeGrouoIdentifier List: %@"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"

```
