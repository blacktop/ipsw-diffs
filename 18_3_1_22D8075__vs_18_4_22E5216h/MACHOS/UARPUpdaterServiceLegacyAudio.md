## UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x17a00
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x40e0
-  __TEXT.__objc_methlist: 0x1330
-  __TEXT.__cstring: 0x7d36
+1207.100.63.0.0
+  __TEXT.__text: 0x14fd0
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_stubs: 0x3dc0
+  __TEXT.__objc_methlist: 0x16b4
+  __TEXT.__cstring: 0x6000
   __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__objc_methname: 0x4c42
-  __TEXT.__objc_classname: 0x264
-  __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__oslogstring: 0x59d
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__objc_methname: 0x491f
+  __TEXT.__objc_classname: 0x210
+  __TEXT.__objc_methtype: 0xbfb
+  __TEXT.__oslogstring: 0x4ae
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x220
+  __TEXT.__unwind_info: 0x4b0
+  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1508
-  __DATA_CONST.__cfstring: 0x6f20
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__cfstring: 0x47c0
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x3dc8
-  __DATA.__objc_selrefs: 0x1368
-  __DATA.__objc_ivar: 0x2a0
-  __DATA.__objc_data: 0x460
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x128
+  __DATA.__objc_const: 0x3068
+  __DATA.__objc_selrefs: 0x1370
+  __DATA.__objc_ivar: 0x298
+  __DATA.__objc_data: 0x3c0
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings
+  - /System/Library/PrivateFrameworks/AUSettings.framework/AUSettings
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 548
-  Symbols:   800
-  CStrings:  2178
+  Functions: 511
+  Symbols:   427
+  CStrings:  1793
 
Symbols:
+ _kAUAssetLocationTypeMobileAssetServerBasejumperBaseStr
- _AUDeveloperSettingsAccessoryFusingStringToType
- _InternalStorageDirectoryPath
- _OBJC_CLASS_$_AUHelperInstance
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_UARPSupportedAccessory
- _OBJC_METACLASS_$_AUDeveloperSettingsDatabase
- _OBJC_METACLASS_$_AUHelperInstance
- _UARPPayloadHashAlgorithmStringToValue
- _UARPStringCmapDatabaseFilePath
- _UARPStringCmapDirectoryPath
- _UARPStringCrashAnalyticsDirectoryFilePath
- _UARPStringDynamicAssetsFilepath
- _UARPStringLogsDirectoryFilePath
- _UARPStringPcapFilesFilepath
- _UARPStringPifMetricsFilePath
- _UARPStringSupplementalAssetsFilepath
- _UARPStringSysdiagnoseDirectoryFilePath
- _UARPStringTapToRadarFilePath
- _UARPStringTempFilesFilepath
- _UARPStringTmapDatabaseFilePath
- _UARPStringTmapDirectoryPath
- _cleanupPersonalizedUpdateAvailable
- _configuredToDefaultAssetLocationForAccessory
- _dropboxFileUpdateForAccessoryID
- _findPartnerSerialNumberForAccessory
- _findPartnerSerialNumbersInDatabase
- _getAccessoryDatabaseKeyForAccessoryID
- _getInfoForAccessory
- _getuid
- _isOTAUpdateDisabledForAccessoryID
- _kAUDeveloperSettingsDatabaseDefaultsSuite
- _kAccessoryReachableKey
- _kAssetURLOverrideKey
- _kAuthListingEnabledKey
- _kClientIndentifier
- _kDownloadedVersionKey
- _kDropboxVersionKey
- _kFirmwareDirectoryName
- _kHWRevisionKey
- _kInternalSettingsPaneURL
- _kPartnerSerialNumbersKey
- _kPersonalizationRequiredKey
- _kReleaseNotesDirectoryName
- _kSerialNumberKey
- _kSupplementalAssetLocationKey
- _kSupplementalBasejumperBuildKey
- _kSupplementalBasejumperTrainKey
- _kUARPAssetLocationTypeMobileAssetServerBasejumperStr
- _kUARPAssetLocationTypeMobileAssetServerLivabilityStr
- _kUARPAssetLocationTypeMobileAssetServerMesuMacOSStr
- _kUARPAssetLocationTypeMobileAssetServerMesuStagingStr
- _kUARPAssetLocationTypeMobileAssetServerMesuStr
- _kUARPDefaultDisplayNameAccessory
- _kUARPDefaultFriendlyNameUnknown
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
- _kUARPStringMetadataDevicePayloadSignature
- _kUARPStringMetadataDevicePayloadSignatureDevelopment
- _kUARPStringMetadataDeviceTriggerBatteryLevel
- _kUARPStringMetadataDeviceUncompressedPayloadLength
- _kUARPStringMetadataDeviceUrgentUpdate
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
- _kUARPStringMobileAssetBuildManfestFilename
- _kUARPStringMobileAssetDeploymentListKey
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
- _objc_allocWithZone
- _objc_opt_isKindOfClass
- _objc_retain_x27
- _updateReachabilityForAccessoryID
CStrings:
+ "@32@0:8@16o^@24"
+ "CrystalESeed"
+ "createFileAtPath:contents:attributes:"
+ "fileHandleForWritingToURL:error:"
+ "https://basejumper.apple.com"
+ "removeItemAtPath:error:"
+ "uarpCreateFileHandleForWritingToURL:error:"
- "%@/MarimbaSeed"
- "%s: Failed to get remote object: %@"
- "%s: Failed to get xpc connection"
- "%s: Not adding empty serial number with info = %@"
- "%s: Updating location = %s for accessoryName = %@"
- "%s: dictionary = %@"
- "%s: received unknown object = %@"
- "%s: seting %@:%@"
- "+"
- "+[AUHelperInstance xpcConnectionToHelper]"
- "-[AUDeveloperSettingsDatabase accessoriesDictionary]"
- "-[AUDeveloperSettingsDatabase addAccessoryWithSerialNumber:info:]"
- "-[AUDeveloperSettingsDatabase seedParticipationDictionary]"
- "-[AUDeveloperSettingsDatabase setAccessoriesDictionary:]"
- "-[AUDeveloperSettingsDatabase updateAccessory:locationType:]"
- "-[AUHelperInstance remoteObject]_block_invoke"
- "/AppleInternal/usr/local/misc"
- "/System/Library/PrivateFrameworks/CoreUARP.framework"
- "/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/Current/Resources"
- "/usr/standalone/firmware/accessoryupdater/UARP"
- "/var/db/accessoryupdater/dropbox"
- "0000"
- "@\"NSXPCConnection\""
- "AUDeveloperSettingsDatabase"
- "AUDeveloperSettingsObjectWithKey:"
- "AUDeveloperSettingsSetObject:withKey:"
- "AUHelperExtend"
- "AUHelperInstance"
- "AUHelperServiceProtocol"
- "Accessory"
- "AllowDownloadOnCellular"
- "AlternativeAppleModelNumbers"
- "Analytics Event Name"
- "Analytics Payload Type"
- "Apple Inc."
- "AppleModelNumber"
- "AutoAppliesStagedFirmware"
- "B24@0:8Q16"
- "B2PHID"
- "BSDNotifications"
- "BTLEServer"
- "Base64EncodedString"
- "Basejumper"
- "BigEndian"
- "Bluetooth"
- "BluetoothProductVersion"
- "BluetoothVendorIDSource"
- "Case"
- "CmapEvents"
- "Compose Measured Payloads"
- "Compose Measured Payloads (Non-FTAB)"
- "Compose MetaData Hash Algorithm"
- "Compose Payload Hash Algorithm"
- "Compressed Headers"
- "Compressed Headers Payload Index"
- "CrashLogKey"
- "CrystalDHWiPhone"
- "Custom Basejumper"
- "Customer"
- "DFUMode"
- "DPRO"
- "DecodedCrashLogChildKey"
- "DecodedCrashLogKey"
- "Dev"
- "Device Specific Data"
- "DownstreamAppleModelNumbers"
- "Dynamic Payload"
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
- "FirmwareVersionBuild"
- "Flash Partition Bitmap"
- "Flash Partition Boot"
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
- "Ignore Version"
- "InputDictionary"
- "Integer"
- "Internal Seed"
- "IsSimulator"
- "LZ4"
- "LZBitmap2"
- "LZBitmapFast2"
- "Life"
- "LittleEndian"
- "Livability"
- "Log Apple Model Number"
- "Log Friendly Name"
- "Log Serial Number"
- "MagSafe Cable"
- "Mapped Analytics Event ID"
- "Mesu Staging"
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
- "Payload Signature"
- "Payload Signature (Development)"
- "Payload Version"
- "Pending"
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
- "Prod"
- "ProductGroup"
- "ProductID"
- "ProductName"
- "ProductNumber"
- "Property List Payload"
- "Provisioning"
- "Public Seed"
- "Q24@0:8@16"
- "ReofferFirmwareOnSync"
- "Required Personalization Option"
- "SHA-256"
- "SHA-384"
- "SHA-512"
- "SOP"
- "SOP Double Prime"
- "SOP Prime"
- "SectionName"
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
- "SupportsDeveloperSettings"
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
- "T@\"<AUHelperServiceProtocol>\",R"
- "T@\"AUHelperInstance\",R"
- "T@\"NSDictionary\",R"
- "Transport"
- "Trigger Battery Level"
- "TtrSolicitLogs"
- "UI_country_code"
- "USB"
- "USB-C to Lightning"
- "USB-PD"
- "USB-PD Device Class"
- "USB-PD Location"
- "USBCLightningDisconnect"
- "UTF8String"
- "UUID"
- "Uncompressed Payload Length"
- "Unfused"
- "UnsignedInteger"
- "UpdateRequiresPowerAssertion"
- "UpdaterName"
- "UploaderResponseTimeout"
- "UploaderRetryLimit"
- "Urgent Update"
- "Value"
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
- "_xpcConnection"
- "accessories"
- "accessoryNameForIdentifier:name:serialNumber:fusingType:"
- "accessoryReachable"
- "accessory_pid"
- "accessory_type"
- "activeVersion"
- "analytics_test_mode"
- "application-info"
- "assetURLOverride"
- "authListingEnabled"
- "basejumperBuild"
- "basejumperTrain"
- "bug_type"
- "cmap"
- "cmapdatabase"
- "com.apple.Bluetooth.AccessoryCase.pif_daily"
- "com.apple.MobileAsset.UARP"
- "com.apple.UARPUpdaterServiceHID"
- "com.apple.UARPUpdaterServiceUSBPD"
- "com.apple.accessoryupdater.launchauhelper"
- "com.apple.system.powermanagement.poweradapter"
- "com.apple.system.powersources.percent"
- "com.apple.system.powersources.source"
- "com.apple.uarp.BTLEServer.personalizationNeeded"
- "com.apple.uarp.UARPUpdaterServiceHID.personalizationNeeded"
- "com.apple.uarp.internal.personalization"
- "containsObject:"
- "core"
- "crashlog"
- "crashlogs"
- "crsh"
- "decoderId"
- "default"
- "downloadedVersion"
- "dropboxVersion"
- "dynamicassets"
- "enumerateKeysAndObjectsUsingBlock:"
- "findByAppleModelNumber:"
- "firmware"
- "fusing"
- "hwFusingType"
- "hwRevision"
- "initWithMachServiceName:options:"
- "input"
- "isOTADisabled"
- "isPowerSource"
- "isSeedParticipationEnabled:"
- "isValidLocationType:"
- "log_version"
- "logs"
- "migrateExistingDefaults"
- "numberWithUnsignedShort:"
- "partnerSerialNumbers"
- "pathWithComponents:"
- "pcapfiles"
- "personalizationRequired"
- "prefs:root=INTERNAL_SETTINGS&path=AccessoriesFirmwareUpdate"
- "prod"
- "releasenotes"
- "remoteObject"
- "remoteObjectInterface"
- "removeAccessoryWithSerialNumber:"
- "sections"
- "seedParticipation"
- "seedParticipationDictionary"
- "setAccessoriesDictionary:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "supplementalAssetLocation"
- "supplementalBasejumperBuild"
- "supplementalBasejumperTrain"
- "supplementalassets"
- "supportsInternalSettings"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "sysdiagnose"
- "sysdiagnose_approved"
- "taptoradar"
- "tatsuSigningServer"
- "tmap"
- "tmapdatabase"
- "tmpfiles"
- "unrecognized"
- "updateAccessory:locationType:"
- "urlLocationTypeForAccessory:"
- "userPreferenceObjectForSuite:withKey:withReply:"
- "userPreferenceSetObject:forSuite:withKey:"
- "uuid"
- "v16@?0@8"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "v40@0:8@16Q24@\"NSString\"32"
- "v40@0:8@16Q24@32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@>32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@16^@24^@32^Q40"
- "xpcConnectionToHelper"

```
