## AUSettings

> `/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x54d8
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x56c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2553
-  __TEXT.__oslogstring: 0x164
+1338.0.21.0.2
+  __TEXT.__text: 0x4cd4
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_methlist: 0x5f4
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0xc44
+  __TEXT.__oslogstring: 0x18c
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0xfe4
-  __TEXT.__objc_methtype: 0x249
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xef0
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_classname: 0x9d
+  __TEXT.__objc_methname: 0x11e4
+  __TEXT.__objc_methtype: 0x256
+  __TEXT.__objc_stubs: 0x920
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1a8
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x848
+  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0xec0
+  __AUTH_CONST.__objc_const: 0x938
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F08E670-2EE5-3130-974A-898580E34206
-  Functions: 158
-  Symbols:   1013
-  CStrings:  1121
+  UUID: 89DB3BA9-FD83-341D-ACEB-8A77DE965450
+  Functions: 130
+  Symbols:   599
+  CStrings:  538
 
Symbols:
+ -[UARPSettingsAccessory isFusingEqual:]
+ -[UARPSettingsAccessory mobileAssetModelNumber]
+ -[UARPSettingsAccessory pallasAudienceOverride]
+ -[UARPSettingsAccessory pallasAudience]
+ -[UARPSettingsAccessory pallasInternalAssetVariant]
+ -[UARPSettingsAccessory pallasSupportEnabled]
+ -[UARPSettingsAccessory setMobileAssetModelNumber:]
+ -[UARPSettingsAccessory setPallasAudience:]
+ -[UARPSettingsAccessory setPallasAudienceOverride:]
+ -[UARPSettingsAccessory setPallasInternalAssetVariant:]
+ -[UARPSettingsAccessory setPallasSupportEnabled:]
+ _AUSettingsPallasAudienceTypeToString
+ _AUSettingsPallasStringToAudienceType
+ _OBJC_IVAR_$_UARPSettingsAccessory._mobileAssetModelNumber
+ _OBJC_IVAR_$_UARPSettingsAccessory._pallasAudience
+ _OBJC_IVAR_$_UARPSettingsAccessory._pallasAudienceOverride
+ _OBJC_IVAR_$_UARPSettingsAccessory._pallasInternalAssetVariant
+ _OBJC_IVAR_$_UARPSettingsAccessory._pallasSupportEnabled
+ ___kCFBooleanTrue
+ _isPallasEnabledForAccessory
+ _kAUInternalSettingsPallasOptionsPlistName
+ _kAUSettingsAccessoryConfigurePallas
+ _kAUSettingsAccessoryPallasEnabled
+ _kAUSettingsAccessoryPallasInternalVariant
+ _kAUSettingsAssetManagerXpcServiceName
+ _kAUSettingsCustomPallasAudienceGroup
+ _kAUSettingsLocationDeveloperSeed
+ _kAUSettingsLocationInternalStaging
+ _kAUSettingsLocationPallasCustom
+ _kAUSettingsLocationPallasCustomer
+ _kAUSettingsLocationPallasCustomerSeed
+ _kAUSettingsLocationPallasInternalLiveOn
+ _kAUSettingsLocationPallasMAUntested
+ _kAUSettingsPallasAudience
+ _kAUSettingsPallasPlistName
+ _kMobileAssetModelNumberKey
+ _kPallasAudienceKey
+ _kPallasAudienceOverrideKey
+ _kPallasInternalAssetVariant
+ _kPallasSupportEnabledKey
+ _kSettingsFromSeedBuild
+ _objc_msgSend$accessoryList
+ _objc_msgSend$containsObject:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isSeedParticipationEnabled:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _updateSeedEnablementForAccessory
- _InternalStorageDirectoryPath
- _InternalStorageDirectoryPath.cold.1
- _InternalStorageDirectoryPath.onceToken
- _InternalStorageDirectoryPath.path
- _UARPPayloadHashAlgorithmStringToValue
- _UARPStringCmapDatabaseFilePath
- _UARPStringCmapDatabaseFilePath.cold.1
- _UARPStringCmapDatabaseFilePath.onceToken
- _UARPStringCmapDatabaseFilePath.path
- _UARPStringCmapDirectoryPath
- _UARPStringCmapDirectoryPath.cold.1
- _UARPStringCmapDirectoryPath.onceToken
- _UARPStringCmapDirectoryPath.path
- _UARPStringCrashAnalyticsDirectoryFilePath
- _UARPStringCrashAnalyticsDirectoryFilePath.cold.1
- _UARPStringCrashAnalyticsDirectoryFilePath.onceToken
- _UARPStringCrashAnalyticsDirectoryFilePath.path
- _UARPStringDynamicAssetsFilepath
- _UARPStringDynamicAssetsFilepath.cold.1
- _UARPStringDynamicAssetsFilepath.onceToken
- _UARPStringDynamicAssetsFilepath.path
- _UARPStringLogsDirectoryFilePath
- _UARPStringLogsDirectoryFilePath.cold.1
- _UARPStringLogsDirectoryFilePath.onceToken
- _UARPStringLogsDirectoryFilePath.path
- _UARPStringPcapFilesFilepath
- _UARPStringPcapFilesFilepath.cold.1
- _UARPStringPcapFilesFilepath.onceToken
- _UARPStringPcapFilesFilepath.path
- _UARPStringPifMetricsFilePath
- _UARPStringPifMetricsFilePath.cold.1
- _UARPStringPifMetricsFilePath.onceToken
- _UARPStringPifMetricsFilePath.path
- _UARPStringSupplementalAssetsFilepath
- _UARPStringSupplementalAssetsFilepath.cold.1
- _UARPStringSupplementalAssetsFilepath.onceToken
- _UARPStringSupplementalAssetsFilepath.path
- _UARPStringSysdiagnoseDirectoryFilePath
- _UARPStringSysdiagnoseDirectoryFilePath.cold.1
- _UARPStringSysdiagnoseDirectoryFilePath.onceToken
- _UARPStringSysdiagnoseDirectoryFilePath.path
- _UARPStringTapToRadarFilePath
- _UARPStringTapToRadarFilePath.cold.1
- _UARPStringTapToRadarFilePath.onceToken
- _UARPStringTapToRadarFilePath.path
- _UARPStringTempFilesFilepath
- _UARPStringTempFilesFilepath.cold.1
- _UARPStringTempFilesFilepath.onceToken
- _UARPStringTempFilesFilepath.path
- _UARPStringTmapDatabaseFilePath
- _UARPStringTmapDatabaseFilePath.cold.1
- _UARPStringTmapDatabaseFilePath.onceToken
- _UARPStringTmapDatabaseFilePath.path
- _UARPStringTmapDirectoryPath
- _UARPStringTmapDirectoryPath.cold.1
- _UARPStringTmapDirectoryPath.onceToken
- _UARPStringTmapDirectoryPath.path
- ___InternalStorageDirectoryPath_block_invoke
- ___UARPStringCmapDatabaseFilePath_block_invoke
- ___UARPStringCmapDirectoryPath_block_invoke
- ___UARPStringCrashAnalyticsDirectoryFilePath_block_invoke
- ___UARPStringDynamicAssetsFilepath_block_invoke
- ___UARPStringLogsDirectoryFilePath_block_invoke
- ___UARPStringPcapFilesFilepath_block_invoke
- ___UARPStringPifMetricsFilePath_block_invoke
- ___UARPStringSupplementalAssetsFilepath_block_invoke
- ___UARPStringSysdiagnoseDirectoryFilePath_block_invoke
- ___UARPStringTapToRadarFilePath_block_invoke
- ___UARPStringTempFilesFilepath_block_invoke
- ___UARPStringTmapDatabaseFilePath_block_invoke
- ___UARPStringTmapDirectoryPath_block_invoke
- ___block_literal_global.1001
- ___block_literal_global.1009
- ___block_literal_global.1014
- ___block_literal_global.756
- ___block_literal_global.758
- ___block_literal_global.760
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.918
- ___block_literal_global.923
- ___block_literal_global.928
- ___block_literal_global.999
- _kFirmwareDirectoryName
- _kReleaseNotesDirectoryName
- _kUARPAssetLocationTypeMobileAssetServerBasejumperStr
- _kUARPAssetLocationTypeMobileAssetServerLivabilityStr
- _kUARPAssetLocationTypeMobileAssetServerMesuMacOSStr
- _kUARPAssetLocationTypeMobileAssetServerMesuStagingStr
- _kUARPAssetLocationTypeMobileAssetServerMesuStr
- _kUARPDefaultDisplayNameAccessory
- _kUARPDefaultFriendlyNameUnknown
- _kUARPDefaultPersonalizationServer
- _kUARPFirmwareDropboxDirectory
- _kUARPPlistCustomer
- _kUARPPlistFolder
- _kUARPPlistFolderEmbedded
- _kUARPPlistFolderInternal
- _kUARPPlistInternal
- _kUARPPlistInternalFuture
- _kUARPStandaloneFirmwareDirectory
- _kUARPStringBTLEServerUpdaterName
- _kUARPStringBsdNotificationCoreSpeechVoiceTriggerAssetChange
- _kUARPStringBsdNotificationPersonalizationNeededBTLEServer
- _kUARPStringBsdNotificationPersonalizationNeededHID
- _kUARPStringBsdNotificationPersonalizationNeededInternal
- _kUARPStringBsdNotificationPowerAdapter
- _kUARPStringBsdNotificationPowerSource
- _kUARPStringBsdNotificationPowerSourcePercentChange
- _kUARPStringCMAPCrashLogKey
- _kUARPStringCMAPDecodedCrashLogChildKey
- _kUARPStringCMAPDecodedCrashLogKey
- _kUARPStringCMAPDecoderId
- _kUARPStringCMAPEvents
- _kUARPStringCMAPInput
- _kUARPStringCMAPInputDictionary
- _kUARPStringCMAPSectionName
- _kUARPStringCMAPUuid
- _kUARPStringCmapDatabase
- _kUARPStringCmapDatabaseFileName
- _kUARPStringCrashAnalyticsAccessoryPid
- _kUARPStringCrashAnalyticsAccessoryType
- _kUARPStringCrashAnalyticsAppleModelNumber
- _kUARPStringCrashAnalyticsApplicationInfo
- _kUARPStringCrashAnalyticsBugType
- _kUARPStringCrashAnalyticsCore
- _kUARPStringCrashAnalyticsCountryCode
- _kUARPStringCrashAnalyticsCrashLog
- _kUARPStringCrashAnalyticsCrashLogs
- _kUARPStringCrashAnalyticsDirectory
- _kUARPStringCrashAnalyticsLogVersion
- _kUARPStringCrashAnalyticsSections
- _kUARPStringCrashAnalyticsTestMode
- _kUARPStringDynamicAssets
- _kUARPStringHIDUpdaterName
- _kUARPStringLogsDirectory
- _kUARPStringMetadataAppleAnalyticsEventName
- _kUARPStringMetadataAppleAnalyticsPayloadType
- _kUARPStringMetadataAppleHeySiriModelCertificate
- _kUARPStringMetadataAppleHeySiriModelDigest
- _kUARPStringMetadataAppleHeySiriModelEngineType
- _kUARPStringMetadataAppleHeySiriModelEngineVersion
- _kUARPStringMetadataAppleHeySiriModelHash
- _kUARPStringMetadataAppleHeySiriModelLocale
- _kUARPStringMetadataAppleHeySiriModelRole
- _kUARPStringMetadataAppleHeySiriModelSignature
- _kUARPStringMetadataAppleHeySiriModelType
- _kUARPStringMetadataAppleHostPersonalizationRequired
- _kUARPStringMetadataAppleLogAppleModelNumber
- _kUARPStringMetadataAppleLogFriendlyName
- _kUARPStringMetadataAppleLogSerialNumber
- _kUARPStringMetadataAppleMappedAnalyticsEventID
- _kUARPStringMetadataApplePersonalizationBoardID
- _kUARPStringMetadataApplePersonalizationChipEpoch
- _kUARPStringMetadataApplePersonalizationChipID
- _kUARPStringMetadataApplePersonalizationChipRevision
- _kUARPStringMetadataApplePersonalizationECID
- _kUARPStringMetadataApplePersonalizationECIDData
- _kUARPStringMetadataApplePersonalizationEnableMixMatch
- _kUARPStringMetadataApplePersonalizationFTABPayload
- _kUARPStringMetadataApplePersonalizationFTABPayloadDigest
- _kUARPStringMetadataApplePersonalizationFTABPayloadDigestFilename
- _kUARPStringMetadataApplePersonalizationFTABPayloadHashAlgorithm
- _kUARPStringMetadataApplePersonalizationFTABPayloadLongname
- _kUARPStringMetadataApplePersonalizationFTABPayloadProductionMode
- _kUARPStringMetadataApplePersonalizationFTABPayloadProductionModeHostOverride
- _kUARPStringMetadataApplePersonalizationFTABPayloadSecurityMode
- _kUARPStringMetadataApplePersonalizationFTABPayloadSecurityModeHostOverride
- _kUARPStringMetadataApplePersonalizationFTABPayloadTag
- _kUARPStringMetadataApplePersonalizationFTABPayloadTrusted
- _kUARPStringMetadataApplePersonalizationLife
- _kUARPStringMetadataApplePersonalizationLogicalUnitNumber
- _kUARPStringMetadataApplePersonalizationManifestEpoch
- _kUARPStringMetadataApplePersonalizationManifestPrefix
- _kUARPStringMetadataApplePersonalizationManifestSuffix
- _kUARPStringMetadataApplePersonalizationMoreRequestsToFollow
- _kUARPStringMetadataApplePersonalizationNonce
- _kUARPStringMetadataApplePersonalizationNonceHash
- _kUARPStringMetadataApplePersonalizationOptionRequired
- _kUARPStringMetadataApplePersonalizationPayloadBoardID64
- _kUARPStringMetadataApplePersonalizationPayloadDemotionProductionMode
- _kUARPStringMetadataApplePersonalizationPayloadDemotionSecurityMode
- _kUARPStringMetadataApplePersonalizationPayloadDigest
- _kUARPStringMetadataApplePersonalizationPayloadDigestFilename
- _kUARPStringMetadataApplePersonalizationPayloadDigestListSize
- _kUARPStringMetadataApplePersonalizationPayloadHashAlgorithm
- _kUARPStringMetadataApplePersonalizationPayloadLongname
- _kUARPStringMetadataApplePersonalizationPayloadMatchingData
- _kUARPStringMetadataApplePersonalizationPayloadMatchingDataPayloadTags
- _kUARPStringMetadataApplePersonalizationPayloadMatchingDataProductRevisionMax
- _kUARPStringMetadataApplePersonalizationPayloadMatchingDataProductRevisionMin
- _kUARPStringMetadataApplePersonalizationPayloadProductionMode
- _kUARPStringMetadataApplePersonalizationPayloadSecurityMode
- _kUARPStringMetadataApplePersonalizationPayloadTag
- _kUARPStringMetadataApplePersonalizationPayloadTrusted
- _kUARPStringMetadataApplePersonalizationPrefixNeedsLogicalUnitNumber
- _kUARPStringMetadataApplePersonalizationProductionMode
- _kUARPStringMetadataApplePersonalizationProvisioning
- _kUARPStringMetadataApplePersonalizationRequired
- _kUARPStringMetadataApplePersonalizationSecurityDomain
- _kUARPStringMetadataApplePersonalizationSecurityMode
- _kUARPStringMetadataApplePersonalizationSoCLiveNonce
- _kUARPStringMetadataApplePersonalizationSuffixNeedsLogicalUnitNumber
- _kUARPStringMetadataApplePersonalizationSuperBinaryAssetID
- _kUARPStringMetadataApplePersonalizationSuperBinaryPayloadIndex
- _kUARPStringMetadataApplePersonalizationTicketNeedsLogicalUnitNumber
- _kUARPStringMetadataApplePersonalizedManifest
- _kUARPStringMetadataAppleVoiceAssistCertificate
- _kUARPStringMetadataAppleVoiceAssistDigest
- _kUARPStringMetadataAppleVoiceAssistEngineVersion
- _kUARPStringMetadataAppleVoiceAssistHash
- _kUARPStringMetadataAppleVoiceAssistLocale
- _kUARPStringMetadataAppleVoiceAssistRole
- _kUARPStringMetadataAppleVoiceAssistSignature
- _kUARPStringMetadataAppleVoiceAssistType
- _kUARPStringMetadataComposeMetaDataHashAlgorithm
- _kUARPStringMetadataComposePayloadFTABMeasuredPayloads
- _kUARPStringMetadataComposePayloadHashAlgorithm
- _kUARPStringMetadataComposePayloadNonFTABMeasuredPayloads
- _kUARPStringMetadataComposePersonalizationOptionsRequired
- _kUARPStringMetadataComposePropertyListPayload
- _kUARPStringMetadataComposeVersionBVERStringFile
- _kUARPStringMetadataComposeVersionStringFile
- _kUARPStringMetadataDeviceCompressPayloadAlgorithm
- _kUARPStringMetadataDeviceCompressPayloadChunkSize
- _kUARPStringMetadataDeviceCompressedHeaders
- _kUARPStringMetadataDeviceCompressedHeadersPayloadIndex
- _kUARPStringMetadataDeviceCompressionAlgorithmLZ4
- _kUARPStringMetadataDeviceCompressionAlgorithmLZBitmap2
- _kUARPStringMetadataDeviceCompressionAlgorithmLZBitmapFast2
- _kUARPStringMetadataDeviceDeviceSpecificData
- _kUARPStringMetadataDeviceEraseOption
- _kUARPStringMetadataDeviceFlashPartitionBitmap
- _kUARPStringMetadataDeviceFlashPartitionBoot
- _kUARPStringMetadataDeviceIgnoreVersion
- _kUARPStringMetadataDeviceMetaDataHash
- _kUARPStringMetadataDeviceMetaDataHashAlgorithm
- _kUARPStringMetadataDeviceMinimumBatteryLevel
- _kUARPStringMetadataDeviceMinimumVersionRequired
- _kUARPStringMetadataDeviceNoCompressedHeaders
- _kUARPStringMetadataDevicePayloadCertificate
- _kUARPStringMetadataDevicePayloadDescription
- _kUARPStringMetadataDevicePayloadDigest
- _kUARPStringMetadataDevicePayloadExpandFilename
- _kUARPStringMetadataDevicePayloadFileName
- _kUARPStringMetadataDevicePayloadHash
- _kUARPStringMetadataDevicePayloadHashAlgorithm
- _kUARPStringMetadataDevicePayloadHashAlgorithmNone
- _kUARPStringMetadataDevicePayloadHashAlgorithmSHA256
- _kUARPStringMetadataDevicePayloadHashAlgorithmSHA384
- _kUARPStringMetadataDevicePayloadHashAlgorithmSHA512
- _kUARPStringMetadataDevicePayloadLongName
- _kUARPStringMetadataDevicePayloadOrderedIndex
- _kUARPStringMetadataDevicePayloadSignature
- _kUARPStringMetadataDevicePayloadSignatureDevelopment
- _kUARPStringMetadataDeviceTlvFlashSectionLength
- _kUARPStringMetadataDeviceTriggerBatteryLevel
- _kUARPStringMetadataDeviceUncompressedPayloadLength
- _kUARPStringMetadataDeviceUrgentUpdate
- _kUARPStringMetadataDeviceVendorVersionStringFile
- _kUARPStringMetadataHostExcludedHwVersion
- _kUARPStringMetadataHostInactiveToApplyAsset
- _kUARPStringMetadataHostInactiveToStageAsset
- _kUARPStringMetadataHostMinimumBatteryLevel
- _kUARPStringMetadataHostMinimumVersionMacOS
- _kUARPStringMetadataHostMinimumVersioniOS
- _kUARPStringMetadataHostMinimumVersiontvOS
- _kUARPStringMetadataHostMinimumVersionwatchOS
- _kUARPStringMetadataHostNetworkDelay
- _kUARPStringMetadataHostReconnectAfterApply
- _kUARPStringMetadataHostTriggerBatteryLevel
- _kUARPStringMetadataKeyAppleFormat
- _kUARPStringMetadataKeyApplePlist
- _kUARPStringMetadataKeyAppleValues
- _kUARPStringMetadataRootAppleFilepath
- _kUARPStringMetadataRootAppleName
- _kUARPStringMetadataRootAppleValue
- _kUARPStringMetadataSysconfigManufacturingPartNumber
- _kUARPStringMetadataSysconfigRegionCode
- _kUARPStringMetadataSysconfigRegulatoryModelNumber
- _kUARPStringMobileAssetAssetsKey
- _kUARPStringMobileAssetBuildManfestFilename
- _kUARPStringMobileAssetDeploymentCountryListKey
- _kUARPStringMobileAssetDeploymentDeploymentLimitKey
- _kUARPStringMobileAssetDeploymentGoLiveDateKey
- _kUARPStringMobileAssetDeploymentListKey
- _kUARPStringMobileAssetDeploymentRampPeriodKey
- _kUARPStringMobileAssetFirmwareBundleFilenameKey
- _kUARPStringMobileAssetFirmwareImageFilenameKey
- _kUARPStringMobileAssetFirmwareVersionBuildKey
- _kUARPStringMobileAssetFirmwareVersionMajorKey
- _kUARPStringMobileAssetFirmwareVersionMinorKey
- _kUARPStringMobileAssetFirmwareVersionReleaseKey
- _kUARPStringMobileAssetUARPAssetPrefix
- _kUARPStringPcapFiles
- _kUARPStringPersonalizationOptionBoardID
- _kUARPStringPersonalizationOptionChipID
- _kUARPStringPersonalizationOptionDPRO
- _kUARPStringPersonalizationOptionDigest
- _kUARPStringPersonalizationOptionECID
- _kUARPStringPersonalizationOptionEPRO
- _kUARPStringPersonalizationOptionESEC
- _kUARPStringPersonalizationOptionLife
- _kUARPStringPersonalizationOptionManifestEpoch
- _kUARPStringPersonalizationOptionNonce
- _kUARPStringPersonalizationOptionProductionMode
- _kUARPStringPersonalizationOptionProvisioning
- _kUARPStringPersonalizationOptionSecurityDomain
- _kUARPStringPersonalizationOptionSecurityMode
- _kUARPStringPersonalizationOptionSocLiveNonce
- _kUARPStringPersonalizationOptionTicket
- _kUARPStringPersonalizationOptionTrusted
- _kUARPStringPersonalizationOptionUIDMode
- _kUARPStringPifMetrics
- _kUARPStringSuperBinaryKeyDynamicPayload
- _kUARPStringSuperBinaryKeyMetaDataFormatVersion
- _kUARPStringSuperBinaryKeyMetaDataValues
- _kUARPStringSuperBinaryKeyMetadataName
- _kUARPStringSuperBinaryKeyMetadataValue
- _kUARPStringSuperBinaryKeyPayload4CC
- _kUARPStringSuperBinaryKeyPayloadFilepath
- _kUARPStringSuperBinaryKeyPayloadLongName
- _kUARPStringSuperBinaryKeyPayloadMetaData
- _kUARPStringSuperBinaryKeyPayloadMissing
- _kUARPStringSuperBinaryKeyPayloadVersion
- _kUARPStringSuperBinaryKeySuperBinaryFirmwareVersion
- _kUARPStringSuperBinaryKeySuperBinaryFormatVersion
- _kUARPStringSuperBinaryKeySuperBinaryMetaData
- _kUARPStringSuperBinaryKeySuperBinaryPayloads
- _kUARPStringSupplementalAssetVoiceAssist
- _kUARPStringSupplementalAssets
- _kUARPStringSysdiagnose
- _kUARPStringSysdiagnoseApproved
- _kUARPStringTMAPAppleModelNumber
- _kUARPStringTMAPEndian
- _kUARPStringTMAPEventFields
- _kUARPStringTMAPEventID
- _kUARPStringTMAPEventName
- _kUARPStringTMAPEvents
- _kUARPStringTMAPFieldLength
- _kUARPStringTMAPFieldName
- _kUARPStringTMAPFieldType
- _kUARPStringTMAPTypeBigEndian
- _kUARPStringTMAPTypeEncodedString
- _kUARPStringTMAPTypeFloat
- _kUARPStringTMAPTypeInteger
- _kUARPStringTMAPTypeLittleEndian
- _kUARPStringTMAPTypeString
- _kUARPStringTMAPTypeUnsignedInteger
- _kUARPStringTapToRadar
- _kUARPStringTatsuSigningServer
- _kUARPStringTempFiles
- _kUARPStringTmapDatabase
- _kUARPStringTmapDatabaseFileName
- _kUARPStringUSBCLightningDisconnectNotification
- _kUARPStringUSBPDUpdaterName
- _kUARPStringVendorMetadataProductNumber
- _kUARPSupportedAccessoryCaseModelNameIdentifier
- _kUARPSupportedAccessoryKeyAllowDownloadOnCellular
- _kUARPSupportedAccessoryKeyAlternativeAMNs
- _kUARPSupportedAccessoryKeyAppleModelNumber
- _kUARPSupportedAccessoryKeyAutoAppliesStagedFirmware
- _kUARPSupportedAccessoryKeyBSDNotifications
- _kUARPSupportedAccessoryKeyBluetoothProductVersion
- _kUARPSupportedAccessoryKeyBluetoothVendorIDSource
- _kUARPSupportedAccessoryKeyDFUMode
- _kUARPSupportedAccessoryKeyDownstreamAMNs
- _kUARPSupportedAccessoryKeyFusingOverrideUnfused
- _kUARPSupportedAccessoryKeyIsPowerSource
- _kUARPSupportedAccessoryKeyIsSimulator
- _kUARPSupportedAccessoryKeyMobileAssetsModelNumber
- _kUARPSupportedAccessoryKeyModelName
- _kUARPSupportedAccessoryKeyPersonalities
- _kUARPSupportedAccessoryKeyPersonalizationNotification
- _kUARPSupportedAccessoryKeyProductGroup
- _kUARPSupportedAccessoryKeyProductID
- _kUARPSupportedAccessoryKeyProductName
- _kUARPSupportedAccessoryKeyProductNumber
- _kUARPSupportedAccessoryKeyReofferFirmwareOnSync
- _kUARPSupportedAccessoryKeyServiceBSDNotifications
- _kUARPSupportedAccessoryKeySupplementalAssets
- _kUARPSupportedAccessoryKeySupplementalAssetsModelNumber
- _kUARPSupportedAccessoryKeySupportsAccMode7
- _kUARPSupportedAccessoryKeySupportsAnalytics
- _kUARPSupportedAccessoryKeySupportsDeveloperSettings
- _kUARPSupportedAccessoryKeySupportsFriendlyName
- _kUARPSupportedAccessoryKeySupportsHeySiriCompact
- _kUARPSupportedAccessoryKeySupportsInternalSettings
- _kUARPSupportedAccessoryKeySupportsLogs
- _kUARPSupportedAccessoryKeySupportsMappedAnalytics
- _kUARPSupportedAccessoryKeySupportsPowerlog
- _kUARPSupportedAccessoryKeySupportsVersions
- _kUARPSupportedAccessoryKeySupportsVoiceAssist
- _kUARPSupportedAccessoryKeyTransport
- _kUARPSupportedAccessoryKeyTransportB2PHID
- _kUARPSupportedAccessoryKeyTransportBluetooth
- _kUARPSupportedAccessoryKeyTransportHDS
- _kUARPSupportedAccessoryKeyTransportHID
- _kUARPSupportedAccessoryKeyTransportIIC
- _kUARPSupportedAccessoryKeyTransportIP
- _kUARPSupportedAccessoryKeyTransportSerial
- _kUARPSupportedAccessoryKeyTransportUSB
- _kUARPSupportedAccessoryKeyTransportUSBPD
- _kUARPSupportedAccessoryKeyTtrSolicitLogs
- _kUARPSupportedAccessoryKeyUSBPDDeviceClass
- _kUARPSupportedAccessoryKeyUSBPDDeviceClassMagSafeCable
- _kUARPSupportedAccessoryKeyUSBPDDeviceClassPowerAdapter
- _kUARPSupportedAccessoryKeyUSBPDDeviceClassUSBCLightning
- _kUARPSupportedAccessoryKeyUSBPDLocationType
- _kUARPSupportedAccessoryKeyUSBPDLocationTypeSOP
- _kUARPSupportedAccessoryKeyUSBPDLocationTypeSOPDoublePrime
- _kUARPSupportedAccessoryKeyUSBPDLocationTypeSOPPrime
- _kUARPSupportedAccessoryKeyUUID
- _kUARPSupportedAccessoryKeyUpdateRequiresPowerAssertion
- _kUARPSupportedAccessoryKeyUpdaterName
- _kUARPSupportedAccessoryKeyUploaderResponseTimeout
- _kUARPSupportedAccessoryKeyUploaderRetryLimit
- _kUARPSupportedAccessoryKeyVendorID
- _kUARPSupportedAccessoryKeyVendorName
- _kUARPSupportedAccessoryKeyVendorNameApple
- _objc_msgSend$accessoryReachable
- _objc_msgSend$activeVersion
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$assetLocation
- _objc_msgSend$assetURLOverride
- _objc_msgSend$authListingEnabled
- _objc_msgSend$customBuild
- _objc_msgSend$customTrain
- _objc_msgSend$downloadedVersion
- _objc_msgSend$dropboxVersion
- _objc_msgSend$hwFusing
- _objc_msgSend$hwRevision
- _objc_msgSend$name
- _objc_msgSend$numberWithUnsignedShort:
- _objc_msgSend$otaDisabled
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$personalizationRequired
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringByStandardizingPath
- _objc_msgSend$stringWithFormat:
- _objc_msgSend$supplementalAssetLocation
- _objc_msgSend$supplementalCustomBuild
- _objc_msgSend$supplementalCustomTrain
- _objc_msgSend$supportsDeveloperSettings
- _objc_release_x9
CStrings:
+ "AUInternalSettingsPallasOptions"
+ "AUInternalSettingsPallasOptions.plist"
+ "Audience"
+ "CUSTOMER_AUDIENCE"
+ "CUSTOMER_SEED_AUDIENCE"
+ "CUSTOM_AUDIENCE"
+ "Clearing seed enablement for %{public}@"
+ "Configure Pallas"
+ "Custom Audience"
+ "Custom Pallas Audience"
+ "Customer Audience"
+ "Customer Seed Audience"
+ "DEVELOPER_SEED"
+ "Developer Seed"
+ "INTERNAL_LIVEON_AUDIENCE"
+ "INTERNAL_STAGING"
+ "Internal Living On"
+ "Internal Staging"
+ "Internal Variant"
+ "MOBILE_ASSET_UNTESTED"
+ "Mobile Asset Untested"
+ "Pallas Enabled"
+ "Q"
+ "T@\"NSString\",R,V_mobileAssetModelNumber"
+ "T@\"NSString\",R,V_pallasAudienceOverride"
+ "TB,R,V_pallasInternalAssetVariant"
+ "TB,R,V_pallasSupportEnabled"
+ "TQ,R,V_pallasAudience"
+ "_mobileAssetModelNumber"
+ "_pallasAudience"
+ "_pallasAudienceOverride"
+ "_pallasInternalAssetVariant"
+ "_pallasSupportEnabled"
+ "com.apple.uarpassetmanager.settings"
+ "containsObject:"
+ "decodeIntegerForKey:"
+ "encodeInteger:forKey:"
+ "integerValue"
+ "isEqualToDictionary:"
+ "isFusingEqual:"
+ "mobileAssetModelNumber"
+ "numberWithUnsignedInteger:"
+ "pallasAudience"
+ "pallasAudienceOverride"
+ "pallasInternalAsset"
+ "pallasInternalAssetVariant"
+ "pallasSupportEnabled"
+ "setMobileAssetModelNumber:"
+ "setPallasAudience:"
+ "setPallasAudienceOverride:"
+ "setPallasInternalAssetVariant:"
+ "setPallasSupportEnabled:"
+ "settingsFromSeedBuild"
+ "v24@0:8Q16"
- "%@/%@"
- "%@/%@/%@%@"
- "%@/AirPods2022Seed"
- "/AppleInternal/usr/local/misc"
- "/System/Library/PrivateFrameworks/CoreUARP.framework"
- "/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/Current/Resources"
- "/usr/standalone/firmware/accessoryupdater/UARP"
- "/var/db/accessoryupdater/dropbox"
- "/var/db/accessoryupdater/uarp/"
- "0000"
- "Accessory"
- "AirPodsDeveloperSeed"
- "AllowDownloadOnCellular"
- "AlternativeAppleModelNumbers"
- "Analytics Event Name"
- "Analytics Payload Type"
- "Apple Inc."
- "AppleModelNumber"
- "Assets"
- "AutoAppliesStagedFirmware"
- "B2PHID"
- "BSDNotifications"
- "BTLEServer"
- "Base64EncodedString"
- "BigEndian"
- "Bluetooth"
- "BluetoothProductVersion"
- "BluetoothVendorIDSource"
- "BoardID"
- "BuildManifest.plist"
- "Case"
- "ChipID"
- "CmapEvents"
- "Compose Measured Payloads"
- "Compose Measured Payloads (Non-FTAB)"
- "Compose MetaData Hash Algorithm"
- "Compose Payload Hash Algorithm"
- "Compressed Headers"
- "Compressed Headers Payload Index"
- "CrashLogKey"
- "DFUMode"
- "DPRO"
- "DecodedCrashLogChildKey"
- "DecodedCrashLogKey"
- "DeploymentList"
- "Device Specific Data"
- "Digest"
- "DownstreamAppleModelNumbers"
- "Dynamic Payload"
- "ECID"
- "EPRO"
- "ESEC"
- "Endian"
- "Erase Option"
- "EventFields"
- "EventID"
- "EventName"
- "Events"
- "Excluded Hardware Version"
- "FieldLength"
- "FieldName"
- "FieldType"
- "Filepath"
- "FirmwareBundle"
- "FirmwareImageFile"
- "FirmwareVersionBuild"
- "FirmwareVersionMajor"
- "FirmwareVersionMinor"
- "FirmwareVersionRelease"
- "Flash Partition Bitmap"
- "Flash Partition Boot"
- "Flash Section Length"
- "Float"
- "FusingOverrideUnfused"
- "HDS"
- "HID"
- "HeySiri Model Certificate"
- "HeySiri Model Digest"
- "HeySiri Model Engine Type"
- "HeySiri Model Engine Version"
- "HeySiri Model Hash"
- "HeySiri Model Locale"
- "HeySiri Model Role"
- "HeySiri Model Signature"
- "HeySiri Model Type"
- "Host Inactive To Apply Asset"
- "Host Inactive To Stage Asset"
- "Host Minimum Battery Level"
- "Host Network Delay"
- "Host Personalization Required"
- "Host Reconnect After Apply"
- "Host Trigger Battery Level"
- "IIC"
- "IP"
- "Ignore Version"
- "InputDictionary"
- "Integer"
- "IsSimulator"
- "LZ4"
- "LZBitmap2"
- "LZBitmapFast2"
- "Life"
- "LittleEndian"
- "Log Apple Model Number"
- "Log Friendly Name"
- "Log Serial Number"
- "MagSafe Cable"
- "ManifestEpoch"
- "Mapped Analytics Event ID"
- "MetaData Format Version"
- "MetaData Hash"
- "MetaData Hash Algorithm"
- "MetaData Values"
- "MetaData plist"
- "Minimum Battery Level"
- "Minimum Required Version"
- "Minimum iOS Version"
- "Minimum macOS Version"
- "Minimum tvOS Version"
- "Minimum watchOS Version"
- "MobileAssetsModelNumber"
- "ModelName"
- "Name"
- "No Compressed Headers"
- "Nonce"
- "None"
- "Payload 4CC"
- "Payload Certificate"
- "Payload Compression Algorithm"
- "Payload Compression ChunkSize"
- "Payload Description"
- "Payload Digest"
- "Payload Expand Filename"
- "Payload Filepath"
- "Payload Hash"
- "Payload Hash Algorithm"
- "Payload Long Name"
- "Payload MetaData"
- "Payload Missing"
- "Payload Ordered Index"
- "Payload Signature"
- "Payload Signature (Development)"
- "Payload Version"
- "Personalities"
- "Personalization Board ID"
- "Personalization Board ID (64 bits)"
- "Personalization Chip Epoch"
- "Personalization Chip ID"
- "Personalization Chip Revision"
- "Personalization Digest List Size"
- "Personalization ECID"
- "Personalization ECID Data"
- "Personalization Enable Mix Match"
- "Personalization FTAB Payload"
- "Personalization FTAB Payload Digest"
- "Personalization FTAB Payload Digest Filename"
- "Personalization FTAB Payload Hash Algorithm"
- "Personalization FTAB Payload Longname"
- "Personalization FTAB Payload Production Mode"
- "Personalization FTAB Payload Production Mode Host Override"
- "Personalization FTAB Payload Security Mode"
- "Personalization FTAB Payload Security Mode Host Override"
- "Personalization FTAB Payload Tag"
- "Personalization FTAB Payload Trusted"
- "Personalization Life"
- "Personalization Logical Unit Number"
- "Personalization Manifest Epoch"
- "Personalization Manifest Prefix"
- "Personalization Manifest Suffix"
- "Personalization Matching Data"
- "Personalization Matching Data Payload Tags"
- "Personalization Matching Data Product Revision Maximum"
- "Personalization Matching Data Product Revision Minimum"
- "Personalization More Requests to Follow"
- "Personalization Nonce"
- "Personalization Nonce Hash"
- "Personalization Options Required"
- "Personalization Payload Demotion Production Mode"
- "Personalization Payload Demotion Security Mode"
- "Personalization Payload Digest"
- "Personalization Payload Digest Filename"
- "Personalization Payload Effective Production Mode"
- "Personalization Payload Effective Security Mode"
- "Personalization Payload Hash Algorithm"
- "Personalization Payload Longname"
- "Personalization Payload Tag"
- "Personalization Payload Trusted"
- "Personalization Prefix Needs Logical Unit Number"
- "Personalization Production Mode"
- "Personalization Provisioning"
- "Personalization Required"
- "Personalization Security Domain"
- "Personalization Security Mode"
- "Personalization SoC Live Nonce"
- "Personalization Suffix Needs Logical Unit Number"
- "Personalization SuperBinary AssetID"
- "Personalization SuperBinary Payload Index"
- "Personalization Ticket Needs Logical Unit Number"
- "PersonalizationNotification"
- "Personalized Manifest"
- "Power Adapter"
- "ProductGroup"
- "ProductID"
- "ProductName"
- "ProductNumber"
- "ProductionMode"
- "Property List Payload"
- "Provisioning"
- "ReofferFirmwareOnSync"
- "Required Personalization Option"
- "SHA-256"
- "SHA-384"
- "SHA-512"
- "SOP"
- "SOP Double Prime"
- "SOP Prime"
- "SectionName"
- "SecurityDomain"
- "SecurityMode"
- "Serial"
- "ServiceBSDNotifications"
- "SocLiveNonce"
- "SuperBinary Firmware Version"
- "SuperBinary Format Version"
- "SuperBinary MetaData"
- "SuperBinary Payloads"
- "SupplementalAssets"
- "SupplementalAssetsModelNumber"
- "SupportedAccessoriesUARP-Internal.plist"
- "SupportedAccessoriesUARP-InternalFuture.plist"
- "SupportedAccessoriesUARP.plist"
- "SupportsAccMode7"
- "SupportsAnalytics"
- "SupportsFriendlyName"
- "SupportsHeySiriCompact"
- "SupportsInternalSettings"
- "SupportsLogs"
- "SupportsMappedAnalytics"
- "SupportsPowerlog"
- "SupportsVersions"
- "SupportsVoiceAssist"
- "Sysconfig Manufacturing Part Number"
- "Sysconfig Region Code"
- "Sysconfig Regulatory Model Number"
- "Ticket"
- "Transport"
- "Trigger Battery Level"
- "Trusted"
- "TtrSolicitLogs"
- "UID_MODE"
- "UI_country_code"
- "USB"
- "USB-C to Lightning"
- "USB-PD"
- "USB-PD Device Class"
- "USB-PD Location"
- "USBCLightningDisconnect"
- "UUID"
- "Uncompressed Payload Length"
- "Unknown"
- "UnsignedInteger"
- "UpdateRequiresPowerAssertion"
- "UpdaterName"
- "UploaderResponseTimeout"
- "UploaderRetryLimit"
- "Urgent Update"
- "Value"
- "Vendor Version String File"
- "VendorID"
- "VendorName"
- "Version BVER File"
- "Version File"
- "Voice Assist Certificate"
- "Voice Assist Digest"
- "Voice Assist Engine Version"
- "Voice Assist Hash"
- "Voice Assist Locale"
- "Voice Assist Role"
- "Voice Assist Signature"
- "Voice Assist Type"
- "VoiceAssist"
- "accessory_pid"
- "accessory_type"
- "analytics_test_mode"
- "application-info"
- "arrayWithObjects:"
- "bug_type"
- "cmap"
- "cmapdatabase"
- "com.apple.Bluetooth.AccessoryCase.pif_daily"
- "com.apple.MobileAsset.UARP"
- "com.apple.UARPUpdaterServiceHID"
- "com.apple.UARPUpdaterServiceUSBPD"
- "com.apple.corespeech.voicetriggerassetchange"
- "com.apple.system.powermanagement.poweradapter"
- "com.apple.system.powersources.percent"
- "com.apple.system.powersources.source"
- "com.apple.uarp.BTLEServer.personalizationNeeded"
- "com.apple.uarp.UARPUpdaterServiceHID.personalizationNeeded"
- "com.apple.uarp.internal.personalization"
- "core"
- "countryList"
- "crashlog"
- "crashlogs"
- "crsh"
- "decoderId"
- "deploymentLimit"
- "dynamicassets"
- "firmware"
- "goLiveDate"
- "https://gs.apple.com:443"
- "input"
- "isPowerSource"
- "log_version"
- "logs"
- "numberWithUnsignedShort:"
- "pathWithComponents:"
- "pcapfiles"
- "rampPeriod"
- "releasenotes"
- "sections"
- "stringByAppendingPathComponent:"
- "stringByStandardizingPath"
- "stringWithFormat:"
- "supplementalassets"
- "sysdiagnose"
- "sysdiagnose_approved"
- "taptoradar"
- "tatsuSigningServer"
- "tmap"
- "tmapdatabase"
- "tmpfiles"
- "uuid"

```
