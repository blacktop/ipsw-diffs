## AUDeveloperSettings

> `/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0xab5c
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x97c
-  __TEXT.__const: 0xb0
-  __TEXT.__oslogstring: 0x1df
-  __TEXT.__cstring: 0x746
-  __TEXT.__gcc_except_tab: 0x378
+1338.0.21.0.2
+  __TEXT.__text: 0xeea4
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0xf00
+  __TEXT.__const: 0xc0
+  __TEXT.__oslogstring: 0x331
+  __TEXT.__cstring: 0x1108
+  __TEXT.__gcc_except_tab: 0x518
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0x20a
-  __TEXT.__objc_methname: 0x1fba
-  __TEXT.__objc_methtype: 0x659
-  __TEXT.__objc_stubs: 0x1d60
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__unwind_info: 0x390
+  __TEXT.__objc_classname: 0x2a1
+  __TEXT.__objc_methname: 0x34bf
+  __TEXT.__objc_methtype: 0xb44
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x1c50
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x240
+  __DATA_CONST.__objc_selrefs: 0xcd8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__objc_const: 0x2b50
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x150
+  __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AUSettings.framework/AUSettings

   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5240B239-0B40-3515-944D-901E5C3F95F3
-  Functions: 179
-  Symbols:   1058
-  CStrings:  601
+  UUID: CAA032A7-044D-3F52-8A89-21829BFB88AD
+  Functions: 271
+  Symbols:   1395
+  CStrings:  952
 
Symbols:
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon]
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon].cold.1
+ +[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon].cold.2
+ -[AUDeveloperSettingsAboutListController currentSpecifierMatchesSerialNumber:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAppliedStagedAssets:layer3Flags:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetOffered:assetUUID:assetTag:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateAssetTransferStatus:assetUUID:transferStatus:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateEndpointAvailable:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateEndpointPropertiesUpdated:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateEndpointUnavailable:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegatePersonalizationStatus:assetUUID:status:]
+ -[AUDeveloperSettingsAboutListController endpointControllerDelegateRescindedAssets:]
+ -[AUDeveloperSettingsAboutListController endpointReachable:]
+ -[AUDeveloperSettingsAboutListController endpointUnreachable:]
+ -[AUDeveloperSettingsAboutListController firmwareUpdateProgressForEndpoint:assetVersion:bytesSent:bytesTotal:]
+ -[AUDeveloperSettingsAboutListController firmwareUpdateProgressForEndpoint:assetVersion:bytesSent:bytesTotal:].cold.1
+ -[AUDeveloperSettingsAboutListController getEndpointSerialNumber:]
+ -[AUDeveloperSettingsAboutListController setupConnection]
+ -[AUDeveloperSettingsAboutListController stagingCompleteForEndpoint:assetVersion:stagingStatus:]
+ -[AUDeveloperSettingsController createSeedCustomerSpecifiers]
+ -[AUDeveloperSettingsController setSeedParticipation:]
+ -[AUDeveloperSettingsController setSeedParticipation:].cold.1
+ -[AUDeveloperSettingsController setSeedParticipation:].cold.2
+ -[AUDeveloperSettingsController setSeedParticipationLegacy:specifier:]
+ -[AUDeveloperSettingsLocationListController isInternalVariantEnabled:]
+ -[AUDeveloperSettingsLocationListController isPallasEnabled:]
+ -[AUDeveloperSettingsLocationListController isPallasViewEnabled:]
+ -[AUDeveloperSettingsLocationListController pallasAudience]
+ -[AUDeveloperSettingsLocationListController setInternalVariantEnabled:specifier:]
+ -[AUDeveloperSettingsLocationListController setPallasAudience:]
+ -[AUDeveloperSettingsLocationListController setPallasEnable:specifier:]
+ -[AUDeveloperSettingsLocationListController setPallasViewEnable:specifier:]
+ -[AUInternalSettingsAssetManagerXPC .cxx_destruct]
+ -[AUInternalSettingsAssetManagerXPC dealloc]
+ -[AUInternalSettingsAssetManagerXPC init]
+ -[AUInternalSettingsAssetManagerXPC remoteObject]
+ -[AUInternalSettingsAssetManagerXPC settingsChangedForSerialNumber:]
+ -[AUInternalSettingsController clearStatus]
+ -[AUInternalSettingsController description]
+ -[AUInternalSettingsController endpointControllerDelegateAppliedStagedAssets:layer3Flags:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetOffered:assetUUID:assetTag:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:]
+ -[AUInternalSettingsController endpointControllerDelegateAssetTransferStatus:assetUUID:transferStatus:]
+ -[AUInternalSettingsController endpointControllerDelegateEndpointAvailable:]
+ -[AUInternalSettingsController endpointControllerDelegateEndpointPropertiesUpdated:]
+ -[AUInternalSettingsController endpointControllerDelegateEndpointUnavailable:]
+ -[AUInternalSettingsController endpointControllerDelegatePersonalizationStatus:assetUUID:status:]
+ -[AUInternalSettingsController endpointControllerDelegateRescindedAssets:]
+ -[AUInternalSettingsController endpointReachable:]
+ -[AUInternalSettingsController endpointUnreachable:]
+ -[AUInternalSettingsController firmwareUpdateProgressForEndpoint:assetVersion:bytesSent:bytesTotal:]
+ -[AUInternalSettingsController getEndpointSerialNumber:]
+ -[AUInternalSettingsController modifySpecifiersForSerialNumber:withStatus:]
+ -[AUInternalSettingsController setupConnection]
+ -[AUInternalSettingsController stagingCompleteForEndpoint:assetVersion:stagingStatus:]
+ -[AUInternalSettingsController viewIsAppearing:]
+ -[AUInternalSettingsController viewWillDisappear:]
+ GCC_except_table17
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table4
+ GCC_except_table43
+ _AUSettingsPallasAudienceTypeToString
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_AUInternalSettingsAssetManagerXPC
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._daemonClient
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._lastReportedStatusTime
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._uarpdConnection
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._airPodsDeveloperSeedSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._airPodsInternalSeedSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._airPodsInternalStagingSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._airPodsPublicSeedSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._assetLocationControl
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._customPallasAudienceGroup
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._customPallasSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._defaultLegacySpecifierListLength
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._defaultPallasSpecifierListLength
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._isPallasEnabled
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._isPallasViewShown
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._legacyLocationSpecifiers
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._modelNumber
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._pallasInternalVariant
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._pallasLocationSpecifiers
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._pallasTextField
+ _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._showingCustomPallasAudienceSpecifiers
+ _OBJC_IVAR_$_AUDeveloperSettingsOverrideController._developerSeedSpecifier
+ _OBJC_IVAR_$_AUInternalSettingsAssetManagerXPC._internalQueue
+ _OBJC_IVAR_$_AUInternalSettingsAssetManagerXPC._xpcConnection
+ _OBJC_IVAR_$_AUInternalSettingsController._lastReportedStatusTime
+ _OBJC_IVAR_$_AUInternalSettingsController._uarpdConnection
+ _OBJC_IVAR_$_AUInternalSettingsController.description
+ _OBJC_METACLASS_$_AUInternalSettingsAssetManagerXPC
+ _OUTLINED_FUNCTION_1
+ _UARPAssetProcessingStatusDescription
+ _UARPEndpointControllerDelegateProtocolSetupInterface
+ _UARPEndpointControllerProtocolSetupInterface
+ _UARPLayer3ApplyStagedAssetsStatusDescription
+ _UARPLayer3ArrayOfExpiredFiles
+ _UARPLayer3HashAlgorithmDescription
+ _UARPLayer3HashAlgorithmValue
+ _UARPLayer3IsSupportFileLifespanExpired
+ _UARPLayer3MatchingUUIDs
+ _UARPLayer3PersonalizationStatusDescription
+ _UARPLayer3UARPLayer3AssetTypeDescription
+ _UARPLayer3UtilsCleanFileHandleForWriting
+ _UARPLayer3UtilsCleanFileHandleForWriting.cold.1
+ _UARPLayer3UtilsCleanFileHandleForWriting.cold.2
+ _UARPLayer3UtilsCleanFileHandleForWriting.cold.3
+ _UARPLayer3UtilsCleanFileHandleForWriting.cold.4
+ _UARPLayer3UtilsCleanupExpiredFiles
+ _UARPLayer3UtilsEnsureDirectoryExists
+ __OBJC_$_CLASS_METHODS_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_INSTANCE_METHODS_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_INSTANCE_VARIABLES_AUInternalSettingsAssetManagerXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UARPEndpointControllerDelegateProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UARPEndpointControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UARPEndpointControllerDelegateProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UARPEndpointControllerProtocol
+ __OBJC_$_PROTOCOL_REFS_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_CLASS_RO_$_AUInternalSettingsAssetManagerXPC
+ __OBJC_LABEL_PROTOCOL_$_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_LABEL_PROTOCOL_$_UARPEndpointControllerDelegateProtocol
+ __OBJC_LABEL_PROTOCOL_$_UARPEndpointControllerProtocol
+ __OBJC_METACLASS_RO_$_AUInternalSettingsAssetManagerXPC
+ __OBJC_PROTOCOL_$_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_PROTOCOL_$_UARPEndpointControllerDelegateProtocol
+ __OBJC_PROTOCOL_$_UARPEndpointControllerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_AUInternalSettingsAssetManagerXPCProvider
+ __OBJC_PROTOCOL_REFERENCE_$_UARPEndpointControllerDelegateProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_UARPEndpointControllerProtocol
+ ___49-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke
+ ___49-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke.cold.1
+ ___56-[AUInternalSettingsController getEndpointSerialNumber:]_block_invoke
+ ___56-[AUInternalSettingsController getEndpointSerialNumber:]_block_invoke_2
+ ___62-[AUDeveloperSettingsAboutListController endpointUnreachable:]_block_invoke
+ ___66-[AUDeveloperSettingsAboutListController getEndpointSerialNumber:]_block_invoke
+ ___66-[AUDeveloperSettingsAboutListController getEndpointSerialNumber:]_block_invoke.186
+ ___75-[AUInternalSettingsController modifySpecifiersForSerialNumber:withStatus:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
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
+ _kAccessoryReachableKey
+ _kPallasAudienceKey
+ _kPallasAudienceOverrideKey
+ _kPallasInternalAssetVariant
+ _kPallasSupportEnabledKey
+ _kUARPLayer3StringAnalyticsSubfolder
+ _kUARPLayer3StringAssetsSubfolder
+ _kUARPLayer3StringCrashSubfolder
+ _kUARPLayer3StringLogsSubfolder
+ _kUARPLayer3StringPacketCaptureSubfolder
+ _kUARPPropertyListKeyPayload4CC
+ _kUARPPropertyListKeyPayloadFilepath
+ _kUARPPropertyListKeyPayloadLongName
+ _kUARPPropertyListKeyPayloadMetaData
+ _kUARPPropertyListKeyPayloadVersion
+ _kUARPPropertyListKeyPersonalizationTickets
+ _kUARPPropertyListKeyPropertyListDigestPath
+ _kUARPPropertyListKeyPropertyListPath
+ _kUARPPropertyListKeyPropertyListVersionPath
+ _kUARPPropertyListKeySuperBinaryFirmwareVersion
+ _kUARPPropertyListKeySuperBinaryFormatVersion
+ _kUARPPropertyListKeySuperBinaryMetaData
+ _kUARPPropertyListKeySuperBinaryPayloads
+ _kUARPTatsuPersonalizationServer
+ _kUarpDeviceControlXpcServiceName
+ _objc_msgSend$UUIDString
+ _objc_msgSend$activate
+ _objc_msgSend$btAddressData
+ _objc_msgSend$bytes
+ _objc_msgSend$clearStatus
+ _objc_msgSend$connectedServices
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$createSeedCustomerSpecifiers
+ _objc_msgSend$currentSpecifierMatchesSerialNumber:
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$devicesWithDiscoveryFlags:error:
+ _objc_msgSend$endpointControllerMonitorForDevices
+ _objc_msgSend$endpointControllerQuerySerialNumber:endpointNumber:componentNumber:reply:
+ _objc_msgSend$endpointReachable:
+ _objc_msgSend$endpointUnreachable:
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$firmwareUpdateProgressForEndpoint:assetVersion:bytesSent:bytesTotal:
+ _objc_msgSend$getEndpointSerialNumber:
+ _objc_msgSend$groupSpecifierWithID:name:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isInternalVariantEnabled:
+ _objc_msgSend$modelUser
+ _objc_msgSend$modifySpecifiersForSerialNumber:withStatus:
+ _objc_msgSend$openSensitiveURL:withOptions:error:
+ _objc_msgSend$productID
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$serialNumberLeft
+ _objc_msgSend$serialNumberRight
+ _objc_msgSend$setPallasAudience:
+ _objc_msgSend$setupConnection
+ _objc_msgSend$stagingCompleteForEndpoint:assetVersion:stagingStatus:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$unsignedIntValue
+ _objc_retain_x27
+ _objc_retain_x4
+ _sleep
+ _updateSeedEnablementForAccessory
- -[AUDeveloperSettingsAboutListController currentSpecifierMatchesAccessoryID:]
- -[AUDeveloperSettingsController setSeedParticipation:specifier:]
- -[AUInternalSettingsController modifySpecifiersForAccessoryID:withStatus:]
- -[AUInternalSettingsController viewDidDisappear:]
- -[AUInternalSettingsController viewWillAppear:]
- GCC_except_table15
- GCC_except_table23
- GCC_except_table3
- _OBJC_IVAR_$_AUDeveloperSettingsLocationListController._publicSeedSpecifier
- ___74-[AUInternalSettingsController modifySpecifiersForAccessoryID:withStatus:]_block_invoke
- _kAccessorySupportsDeveloperSettingsKey
- _objc_msgSend$createCustomerSpecifiers
- _objc_msgSend$currentSpecifierMatchesAccessoryID:
- _objc_msgSend$modifySpecifiersForAccessoryID:withStatus:
CStrings:
+ " :\n%@"
+ "%02X:%02X:%02X:%02X:%02X:%02X"
+ "%s: createDirectoryAtPath %@ failed %@ "
+ "%s: createFileAtPath failed %@ "
+ "%s: fileHandleForWritingToURL %@ failed %@ "
+ "%s: removeItemAtPath %@ failed %@ "
+ "+[AUInternalSettingsAssetManagerXPC xpcConnectionToDaemon]"
+ "- Applied Staged Asset"
+ "- Rescinded"
+ "-[AUInternalSettingsAssetManagerXPC remoteObject]"
+ "-[AUInternalSettingsAssetManagerXPC remoteObject]_block_invoke"
+ "-[AUInternalSettingsAssetManagerXPC settingsChangedForSerialNumber:]"
+ "@\"AUInternalSettingsAssetManagerXPC\""
+ "@\"NSDate\""
+ "@\"NSMutableArray\""
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UISegmentedControl\""
+ "@40@0:8@16@24@32"
+ "AUInternalSettingsAssetManagerXPC"
+ "AUInternalSettingsAssetManagerXPCProvider"
+ "Accessory connected: %@"
+ "Applied Staged Asset"
+ "Asset Corrupt"
+ "Asset Not Found"
+ "Asset Staging Still In Progress"
+ "Attempt AppleConnect"
+ "Attempt Auth Listed"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@16@24@32"
+ "Complete"
+ "Could not find paired bluetooth device matching: %{public}@"
+ "Dynamic Asset (RX)"
+ "Dynamic Asset (TX)"
+ "Error navigating to bluetooth settings: %{public}@"
+ "Failure"
+ "Firmware (RX)"
+ "Firmware (TX)"
+ "Idle"
+ "ImprovedSeedingUI"
+ "In Flight"
+ "In Use"
+ "Invalid"
+ "Navigating to Bluetooth settings at URL: %{public}@"
+ "Needs Restart"
+ "None"
+ "Not Auth Listed"
+ "Not Needed"
+ "Nothing Staged"
+ "Pallas"
+ "Pallas Options"
+ "Payload 4CC"
+ "Payload Filepath"
+ "Payload Long Name"
+ "Payload MetaData"
+ "Payload Version"
+ "Personalization Tickets"
+ "Property List Digest Path"
+ "Property List Path"
+ "Property List Version Path"
+ "Request Failure"
+ "Rescinded Asset"
+ "SHA-256"
+ "SHA-384"
+ "SHA-512"
+ "Server Unreachable"
+ "Success"
+ "SuperBinary Firmware Version"
+ "SuperBinary Format Version"
+ "SuperBinary MetaData"
+ "SuperBinary Payloads"
+ "T@\"NSString\",R,C,Vdescription"
+ "Ticket Construction Failure"
+ "UARPEndpointControllerDelegateProtocol"
+ "UARPEndpointControllerProtocol"
+ "UARPLayer3UtilsCleanFileHandleForWriting"
+ "UUIDString"
+ "Upload Abandoned"
+ "Upload Abandoned  - Better Transport"
+ "Upload Abandoned  - Cancelled Asset Tag"
+ "Upload Abandoned  - Device Error"
+ "Upload Abandoned  - Higher Version"
+ "Upload Abandoned  - Higher Version Active"
+ "Upload Abandoned  - Higher Version Staged"
+ "Upload Abandoned  - Low Battery"
+ "Upload Abandoned  - MetaData Overflow"
+ "Upload Abandoned  - Personalization Failure"
+ "Upload Abandoned  - Priority Activity"
+ "Upload Abandoned  - Processing Error"
+ "Upload Abandoned  - Same Asset Tag In Progress"
+ "Upload Abandoned  - Same Version Active"
+ "Upload Abandoned  - Same Version Staged"
+ "Upload Abandoned  - Unsupported Asset Tag"
+ "Upload Abandoned  - Update In Progress"
+ "Upload Complete"
+ "Upload Denied"
+ "Upload Denied  - Better Transport"
+ "Upload Denied  - Cancelled Asset Tag"
+ "Upload Denied  - Device Error"
+ "Upload Denied  - Higher Version"
+ "Upload Denied  - Higher Version Active"
+ "Upload Denied  - Higher Version Staged"
+ "Upload Denied  - Low Battery"
+ "Upload Denied  - MetaData Overflow"
+ "Upload Denied  - Personalization Failure"
+ "Upload Denied  - Priority Activity"
+ "Upload Denied  - Processing Error"
+ "Upload Denied  - Same Asset Tag In Progress"
+ "Upload Denied  - Same Version Active"
+ "Upload Denied  - Same Version Staged"
+ "Upload Denied  - Unsupported Asset Tag"
+ "Upload Denied  - Update In Progress"
+ "_airPodsDeveloperSeedSpecifier"
+ "_airPodsInternalSeedSpecifier"
+ "_airPodsInternalStagingSpecifier"
+ "_airPodsPublicSeedSpecifier"
+ "_assetLocationControl"
+ "_customPallasAudienceGroup"
+ "_customPallasSpecifier"
+ "_daemonClient"
+ "_defaultLegacySpecifierListLength"
+ "_defaultPallasSpecifierListLength"
+ "_developerSeedSpecifier"
+ "_isPallasEnabled"
+ "_isPallasViewShown"
+ "_lastReportedStatusTime"
+ "_legacyLocationSpecifiers"
+ "_modelNumber"
+ "_pallasInternalVariant"
+ "_pallasLocationSpecifiers"
+ "_pallasTextField"
+ "_showingCustomPallasAudienceSpecifiers"
+ "_uarpdConnection"
+ "activate"
+ "assets"
+ "btAddressData"
+ "bytes"
+ "clearStatus"
+ "com.apple.HeadphoneSettings"
+ "connectedServices"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createFileAtPath:contents:attributes:"
+ "createSeedCustomerSpecifiers"
+ "currentSpecifierMatchesSerialNumber:"
+ "date"
+ "defaultManager"
+ "defaultWorkspace"
+ "device/assets/analytics"
+ "device/assets/crash"
+ "device/assets/logs"
+ "devicesWithDiscoveryFlags:error:"
+ "endpointControllerApplyStagedAssets:"
+ "endpointControllerDelegateAppliedStagedAssets:layer3Flags:"
+ "endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:"
+ "endpointControllerDelegateAssetOffered:assetUUID:assetTag:"
+ "endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:"
+ "endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:"
+ "endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:"
+ "endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:"
+ "endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:"
+ "endpointControllerDelegateAssetTransferStatus:assetUUID:transferStatus:"
+ "endpointControllerDelegateEndpointAvailable:"
+ "endpointControllerDelegateEndpointPropertiesUpdated:"
+ "endpointControllerDelegateEndpointUnavailable:"
+ "endpointControllerDelegatePersonalizationStatus:assetUUID:status:"
+ "endpointControllerDelegateRescindedAssets:"
+ "endpointControllerExportDynamicAsset:endpointUUID:dynamicAssetURL:reply:"
+ "endpointControllerExportPersonalizedAsset:endpointUUID:personalizedAssetURL:reply:"
+ "endpointControllerMonitorForDevices"
+ "endpointControllerOfferFirmwareAsset:endpointUUID:assetUUID:"
+ "endpointControllerOfferFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
+ "endpointControllerPersonalizeFirmwareAsset:endpointUUID:assetUUID:tatsuRequest:tssServerURL:"
+ "endpointControllerPersonalizeFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
+ "endpointControllerQueryAppleModelNumber:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryBoardID:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryChipID:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryChipRevision:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryComponentTag:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryECID:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryECIDData:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryFTABGeneration:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryFirmwareVersion:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryFriendlyName:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryHardwareFusingType:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryHardwareVersion:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryManufacturerName:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryModelName:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryNonce:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryNonceSeed:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryNumberOfComponents:endpointNumber:reply:"
+ "endpointControllerQueryNumberOfEndpoints:reply:"
+ "endpointControllerQueryProductionMode:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryRealHdcpKeyPresent:endpointNumber:componentNumber:reply:"
+ "endpointControllerQuerySecurityDomain:endpointNumber:componentNumber:reply:"
+ "endpointControllerQuerySecurityMode:endpointNumber:componentNumber:reply:"
+ "endpointControllerQuerySerialNumber:endpointNumber:componentNumber:reply:"
+ "endpointControllerQueryStagedFirmwareVersion:endpointNumber:componentNumber:reply:"
+ "endpointControllerRescindStagedAssets:"
+ "endpointControllerSolicitAsset:assetTag:assetURL:assetUUID:"
+ "endpointControllerStageAndApplyFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
+ "endpointControllerStageFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
+ "endpointControllerTssRequestForPersonalizedAsset:endpointUUID:reply:"
+ "endpointControllerTssResponseForPersonalizedAsset:endpointUUID:reply:"
+ "endpointReachable:"
+ "endpointUnreachable:"
+ "exportedInterface"
+ "fileExistsAtPath:"
+ "fileHandleForWritingToURL:error:"
+ "firmwareUpdateProgressForEndpoint:assetVersion:bytesSent:bytesTotal:"
+ "getEndpointSerialNumber:"
+ "groupSpecifierWithID:name:"
+ "https://gs.apple.com:443"
+ "insertObject:atIndex:"
+ "integerValue"
+ "isInternalVariantEnabled:"
+ "isPallasEnabled:"
+ "isPallasViewEnabled:"
+ "modelUser"
+ "modifySpecifiersForSerialNumber:withStatus:"
+ "openSensitiveURL:withOptions:error:"
+ "pallasAudience"
+ "pcapfiles"
+ "prefs:root=Bluetooth&path=HeadphoneDetail/SeedingUI&identifier=%@"
+ "productID"
+ "remoteObjectInterface"
+ "remoteObjectProxy"
+ "removeItemAtPath:error:"
+ "removeLastObject"
+ "serialNumberLeft"
+ "serialNumberRight"
+ "setInternalVariantEnabled:specifier:"
+ "setPallasAudience:"
+ "setPallasEnable:specifier:"
+ "setPallasViewEnable:specifier:"
+ "setSeedParticipation:"
+ "setSeedParticipationLegacy:specifier:"
+ "setupConnection"
+ "stagingCompleteForEndpoint:assetVersion:stagingStatus:"
+ "stringByDeletingLastPathComponent"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "timeIntervalSinceDate:"
+ "unsignedIntValue"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8@\"NSUUID\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\">24"
+ "v32@0:8@16@?24"
+ "v40@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32"
+ "v40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?@\"NSNumber\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSNumber\"32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSDictionary\">32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSURL\"40"
+ "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSData\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSNumber\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSString\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSURL\"32@\"NSUUID\"40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSNumber\"32@\"NSNumber\"40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?B>40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16@24@32@?40"
+ "v56@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSDictionary\"40@\"NSURL\"48"
+ "v56@0:8@16@24@32@40@48"
+ "v64@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "viewIsAppearing:"
- "\v"
- "ENABLE_LOG_COLLECTION_FOR_AIRPODS"
- "LOG_COLLECTION"
- "currentSpecifierMatchesAccessoryID:"
- "modifySpecifiersForAccessoryID:withStatus:"
- "setSeedParticipation:specifier:"
- "viewDidDisappear:"

```
