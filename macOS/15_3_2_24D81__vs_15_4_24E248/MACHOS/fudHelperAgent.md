## fudHelperAgent

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/fudHelperAgent`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x15c0c
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x7c0
-  __TEXT.__cstring: 0x1da1
-  __TEXT.__const: 0x2e0
-  __TEXT.__objc_methname: 0x1e92
-  __TEXT.__objc_classname: 0x120
-  __TEXT.__oslogstring: 0xc67
-  __TEXT.__objc_methtype: 0x361
+1207.100.66.0.0
+  __TEXT.__text: 0xd420
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0xc2c
+  __TEXT.__const: 0x2a0
+  __TEXT.__objc_methname: 0x24d4
+  __TEXT.__cstring: 0x1465
+  __TEXT.__objc_classname: 0x13a
+  __TEXT.__objc_methtype: 0x3b6
+  __TEXT.__oslogstring: 0xa71
   __TEXT.__gcc_except_tab: 0xac
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x520
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x800
-  __DATA_CONST.__cfstring: 0xfe0
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0x2f0
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__cfstring: 0xe00
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1680
-  __DATA.__objc_selrefs: 0x7e8
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x230
-  __DATA.__data: 0x245
-  __DATA.__bss: 0x1198
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x1948
+  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x240
+  __DATA.__bss: 0x48
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UARPiCloud.framework/Versions/A/UARPiCloud
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A891A84C-A0F3-33C6-8A10-FA4216F23CB0
-  Functions: 613
-  Symbols:   3893
-  CStrings:  964
+  UUID: 48D375D3-7BA3-37F9-98D3-A0319DEC480B
+  Functions: 339
+  Symbols:   2520
+  CStrings:  897
 
Symbols:
+ +[AUDeveloperSettingsDatabase sharedDatabase].cold.1
+ +[NSUserDefaults(AUHelperExtend) AUDeveloperSettingsUpdateAccessory:withKey:]
+ +[UARPSettingsAccessory supportsSecureCoding]
+ -[AUDeveloperSettingsDatabase accessoryList]
+ -[AUDeveloperSettingsDatabase copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:]
+ -[AUDeveloperSettingsDatabase copyAccessoryWithSerialNumber:]
+ -[AUDeveloperSettingsDatabase removeAccessory:]
+ -[AUDeveloperSettingsDatabase updateAccessory:]
+ -[AUDeveloperSettingsDatabase updateAccessoryWithSerialNumber:info:]
+ -[UARPSettingsAccessory .cxx_destruct]
+ -[UARPSettingsAccessory accessoryReachable]
+ -[UARPSettingsAccessory activeVersion]
+ -[UARPSettingsAccessory assetLocation]
+ -[UARPSettingsAccessory assetURLOverride]
+ -[UARPSettingsAccessory authListingEnabled]
+ -[UARPSettingsAccessory copyWithZone:]
+ -[UARPSettingsAccessory customBuild]
+ -[UARPSettingsAccessory customTrain]
+ -[UARPSettingsAccessory downloadedVersion]
+ -[UARPSettingsAccessory dropboxVersion]
+ -[UARPSettingsAccessory encodeAsChangedDictionary]
+ -[UARPSettingsAccessory encodeAsDictionary]
+ -[UARPSettingsAccessory encodeWithCoder:]
+ -[UARPSettingsAccessory hwFusing]
+ -[UARPSettingsAccessory hwRevision]
+ -[UARPSettingsAccessory initWithCoder:]
+ -[UARPSettingsAccessory initWithDictionary:]
+ -[UARPSettingsAccessory isEqual:]
+ -[UARPSettingsAccessory modelNumber]
+ -[UARPSettingsAccessory name]
+ -[UARPSettingsAccessory otaDisabled]
+ -[UARPSettingsAccessory partnerSerialNumbers]
+ -[UARPSettingsAccessory personalizationRequired]
+ -[UARPSettingsAccessory serialNumber]
+ -[UARPSettingsAccessory setAccessoryReachable:]
+ -[UARPSettingsAccessory setActiveVersion:]
+ -[UARPSettingsAccessory setAssetLocation:]
+ -[UARPSettingsAccessory setAssetURLOverride:]
+ -[UARPSettingsAccessory setAuthListingEnabled:]
+ -[UARPSettingsAccessory setCustomBuild:]
+ -[UARPSettingsAccessory setCustomTrain:]
+ -[UARPSettingsAccessory setDownloadedVersion:]
+ -[UARPSettingsAccessory setDropboxVersion:]
+ -[UARPSettingsAccessory setHwFusing:]
+ -[UARPSettingsAccessory setHwRevision:]
+ -[UARPSettingsAccessory setModelNumber:]
+ -[UARPSettingsAccessory setName:]
+ -[UARPSettingsAccessory setOtaDisabled:]
+ -[UARPSettingsAccessory setPartnerSerialNumbers:]
+ -[UARPSettingsAccessory setPersonalizationRequired:]
+ -[UARPSettingsAccessory setSerialNumber:]
+ -[UARPSettingsAccessory setSupplementalAssetLocation:]
+ -[UARPSettingsAccessory setSupplementalCustomBuild:]
+ -[UARPSettingsAccessory setSupplementalCustomTrain:]
+ -[UARPSettingsAccessory setSupportsDeveloperSettings:]
+ -[UARPSettingsAccessory supplementalAssetLocation]
+ -[UARPSettingsAccessory supplementalCustomBuild]
+ -[UARPSettingsAccessory supplementalCustomTrain]
+ -[UARPSettingsAccessory supportsDeveloperSettings]
+ -[fudHelper fudHelperContactFud].cold.1
+ -[fudHelper init].cold.1
+ -[fudHelper init].cold.2
+ -[fudHelper processPendingRestartReply:].cold.4
+ -[fudHelper processPendingUpdateReply:].cold.4
+ -[fudHelper retrievePendingMessageInfoFromFud].cold.5
+ -[fudHelper sendRestartUserSelectionToFud:].cold.2
+ -[fudHelper sendUpdateUserSelectionToFud:].cold.2
+ -[fudHelper setupConnectionToFud].cold.2
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUHelperInstance.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUHelperStrings.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUNotification.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUStrings.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAccessoryInternal.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAnalyticsAUDUpdateFirmwareState.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAnalyticsEventUtils.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPSettingsAccessory.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPSettingsDatabaseUtils.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPStrings+Internal.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPUpdateFirmwareAnalyticsEvent.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/fudHelper.o
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/AUDeveloperSettings/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/CommonCode/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/CoreUARP/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/UARP/Analytics/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fudHelper/
+ GCC_except_table2
+ InternalStorageDirectoryPath.cold.1
+ OBJC_IVAR_$_UARPSettingsAccessory._accessoryReachable
+ OBJC_IVAR_$_UARPSettingsAccessory._activeVersion
+ OBJC_IVAR_$_UARPSettingsAccessory._assetLocation
+ OBJC_IVAR_$_UARPSettingsAccessory._assetURLOverride
+ OBJC_IVAR_$_UARPSettingsAccessory._authListingEnabled
+ OBJC_IVAR_$_UARPSettingsAccessory._customBuild
+ OBJC_IVAR_$_UARPSettingsAccessory._customTrain
+ OBJC_IVAR_$_UARPSettingsAccessory._downloadedVersion
+ OBJC_IVAR_$_UARPSettingsAccessory._dropboxVersion
+ OBJC_IVAR_$_UARPSettingsAccessory._hwFusing
+ OBJC_IVAR_$_UARPSettingsAccessory._hwRevision
+ OBJC_IVAR_$_UARPSettingsAccessory._modelNumber
+ OBJC_IVAR_$_UARPSettingsAccessory._name
+ OBJC_IVAR_$_UARPSettingsAccessory._originalSettings
+ OBJC_IVAR_$_UARPSettingsAccessory._otaDisabled
+ OBJC_IVAR_$_UARPSettingsAccessory._partnerSerialNumbers
+ OBJC_IVAR_$_UARPSettingsAccessory._personalizationRequired
+ OBJC_IVAR_$_UARPSettingsAccessory._serialNumber
+ OBJC_IVAR_$_UARPSettingsAccessory._supplementalAssetLocation
+ OBJC_IVAR_$_UARPSettingsAccessory._supplementalCustomBuild
+ OBJC_IVAR_$_UARPSettingsAccessory._supplementalCustomTrain
+ OBJC_IVAR_$_UARPSettingsAccessory._supportsDeveloperSettings
+ UARPSettingsAccessory.m
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_UARPSettingsAccessory
+ _OBJC_METACLASS_$_UARPSettingsAccessory
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __44-[AUDeveloperSettingsDatabase accessoryList]_block_invoke.cold.1
+ __48-[fudHelper fudHelperDarwinNotificationHandler:]_block_invoke.cold.3
+ __50-[UARPSettingsAccessory encodeAsChangedDictionary]_block_invoke.6
+ __OBJC_$_CLASS_METHODS_UARPSettingsAccessory
+ __OBJC_$_CLASS_PROP_LIST_UARPSettingsAccessory
+ __OBJC_$_INSTANCE_METHODS_UARPSettingsAccessory
+ __OBJC_$_INSTANCE_VARIABLES_UARPSettingsAccessory
+ __OBJC_$_PROP_LIST_UARPSettingsAccessory
+ __OBJC_CLASS_PROTOCOLS_$_UARPSettingsAccessory
+ __OBJC_CLASS_RO_$_UARPSettingsAccessory
+ __OBJC_METACLASS_RO_$_UARPSettingsAccessory
+ ___44-[AUDeveloperSettingsDatabase accessoryList]_block_invoke
+ ___50-[UARPSettingsAccessory encodeAsChangedDictionary]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24l
+ _dropboxFileUpdateForAccessory
+ _findPartnerSerialNumberForAccessoryID
+ _generateAssetLocationBasePath
+ _getAccessoryDatabaseKeyForAccessory
+ _isOTAUpdateDisabledForAccessory
+ _kAUAssetLocationTypeMobileAssetServerBasejumperBaseStr
+ _kAccessorySupportsDeveloperSettingsKey
+ _objc_msgSend$AUDeveloperSettingsUpdateAccessory:withKey:
+ _objc_msgSend$accessoryReachable
+ _objc_msgSend$activeVersion
+ _objc_msgSend$assetLocation
+ _objc_msgSend$assetURLOverride
+ _objc_msgSend$authListingEnabled
+ _objc_msgSend$copyAccessoryWithSerialNumber:
+ _objc_msgSend$customBuild
+ _objc_msgSend$customTrain
+ _objc_msgSend$downloadedVersion
+ _objc_msgSend$dropboxVersion
+ _objc_msgSend$encodeAsChangedDictionary
+ _objc_msgSend$encodeAsDictionary
+ _objc_msgSend$hwFusing
+ _objc_msgSend$hwRevision
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$name
+ _objc_msgSend$null
+ _objc_msgSend$otaDisabled
+ _objc_msgSend$personalizationRequired
+ _objc_msgSend$removeAccessoryWithSerialNumber:
+ _objc_msgSend$setSerialNumber:
+ _objc_msgSend$supplementalAssetLocation
+ _objc_msgSend$supplementalCustomBuild
+ _objc_msgSend$supplementalCustomTrain
+ _objc_msgSend$supportsDeveloperSettings
+ _objc_msgSend$updateAccessoryWithSerialNumber:info:
+ _objc_msgSend$userPreferenceUpdateAccessorySettings:withKey:
+ _updateReachabilityForAccessory
- -[AUDeveloperSettingsDatabase accessoriesDictionary].cold.2
- -[AUDeveloperSettingsDatabase migrateExistingDefaults]
- -[AUDeveloperSettingsDatabase seedParticipationDictionary]
- -[AUDeveloperSettingsDatabase seedParticipationDictionary].cold.1
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPCompressionUtils.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformDarwin.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint+Asset.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint+CallbackProtection.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint+Internal.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint+MsgRecv.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint+MsgSend.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformEndpoint.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPPlatformTransmitQueue.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPStreamingRecv.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPSuperBinary.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libUARP.a(CoreUARPUtils.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUHelperInstance.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUHelperStrings.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUNotification.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/AUStrings.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAccessoryInternal.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAnalyticsAUDUpdateFirmwareState.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAnalyticsEventUtils.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPAssetManagerUtils.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPSettingsDatabaseUtils.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPStrings+Internal.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/UARPUpdateFirmwareAnalyticsEvent.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/fudHelperAgent.build/Objects-normal/arm64e/fudHelper.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/AUDeveloperSettings/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/CommonCode/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/CoreUARP/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/UARP/Analytics/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fudHelper/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager_libUARP/libuarp/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager_libUARP/libuarp/Platform/
- CoreUARPCompressionUtils.c
- CoreUARPPlatformDarwin.c
- CoreUARPPlatformEndpoint+Asset.c
- CoreUARPPlatformEndpoint+CallbackProtection.c
- CoreUARPPlatformEndpoint+Internal.c
- CoreUARPPlatformEndpoint+MsgRecv.c
- CoreUARPPlatformEndpoint+MsgSend.c
- CoreUARPPlatformEndpoint.c
- CoreUARPPlatformTransmitQueue.c
- CoreUARPStreamingRecv.c
- CoreUARPSuperBinary.c
- CoreUARPUtils.c
- UARPAssetManagerUtils.m
- _CC_SHA256_Final
- _CC_SHA256_Init
- _CC_SHA256_Update
- _CC_SHA384_Final
- _CC_SHA384_Init
- _CC_SHA384_Update
- _CC_SHA512_Final
- _CC_SHA512_Init
- _CC_SHA512_Update
- _InternalStorageCacheDirectoryPath
- _NSFilePosixPermissions
- _OBJC_CLASS_$_UARPSuperBinaryAsset
- _UARPAccessoryHardwareFusingToString
- _UARPLayer2ActiveFirmwareVersion2
- _UARPLayer2ActiveFirmwareVersionResponse
- _UARPLayer2ApplyStagedAssets
- _UARPLayer2ApplyStagedAssetsResponse
- _UARPLayer2AssetAllHeadersAndMetaDataComplete
- _UARPLayer2AssetCorrupt
- _UARPLayer2AssetGetBytesAtOffset2
- _UARPLayer2AssetMetaDataComplete
- _UARPLayer2AssetMetaDataProcessingError
- _UARPLayer2AssetMetaDataTLV
- _UARPLayer2AssetOrphaned
- _UARPLayer2AssetPreProcessingNotification
- _UARPLayer2AssetPreProcessingNotificationAck
- _UARPLayer2AssetProcessingNotification2
- _UARPLayer2AssetProcessingNotificationAck
- _UARPLayer2AssetReady
- _UARPLayer2AssetReleased2
- _UARPLayer2AssetRescinded
- _UARPLayer2AssetRescindedAck
- _UARPLayer2AssetSetBytesAtOffset2
- _UARPLayer2AssetSolicitation
- _UARPLayer2AssetStore
- _UARPLayer2CompressBuffer
- _UARPLayer2DataTransferPause
- _UARPLayer2DataTransferPauseAck
- _UARPLayer2DataTransferResume
- _UARPLayer2DataTransferResumeAck
- _UARPLayer2DecompressBuffer
- _UARPLayer2DynamicAssetOffered
- _UARPLayer2FriendlyName
- _UARPLayer2FriendlyNameResponse
- _UARPLayer2HardwareVersion
- _UARPLayer2HardwareVersionResponse
- _UARPLayer2HashFinal
- _UARPLayer2HashInfo
- _UARPLayer2HashInit
- _UARPLayer2HashLog
- _UARPLayer2HashUpdate
- _UARPLayer2LastError
- _UARPLayer2LastErrorResponse
- _UARPLayer2LogPacket
- _UARPLayer2ManufacturerName
- _UARPLayer2ManufacturerNameResponse
- _UARPLayer2ModelName
- _UARPLayer2ModelNameResponse
- _UARPLayer2PayloadData
- _UARPLayer2PayloadDataComplete
- _UARPLayer2PayloadDataComplete2
- _UARPLayer2PayloadMetaDataComplete
- _UARPLayer2PayloadMetaDataProcessingError
- _UARPLayer2PayloadMetaDataTLV
- _UARPLayer2PayloadReady
- _UARPLayer2ProtocolVersion
- _UARPLayer2RequestBuffer
- _UARPLayer2RequestTransmitMsgBuffer
- _UARPLayer2RescindAllAssets
- _UARPLayer2RescindAllAssetsAck
- _UARPLayer2ReturnBuffer
- _UARPLayer2ReturnTransmitMsgBuffer
- _UARPLayer2SendMessage
- _UARPLayer2SerialNumber
- _UARPLayer2SerialNumberResponse
- _UARPLayer2StagedFirmwareVersion2
- _UARPLayer2StagedFirmwareVersionResponse
- _UARPLayer2StatisticsResponse
- _UARPLayer2SuperBinaryOffered
- _UARPLayer2VendorSpecificCheckExpectedResponse
- _UARPLayer2VendorSpecificCheckValidToSend
- _UARPLayer2VendorSpecificExceededRetries
- _UARPLayer2VendorSpecificRecvMessage
- _UARPLayer2WatchdogCancel
- _UARPLayer2WatchdogSet
- _UARPPlatformDownstreamEndpointByDelegate
- _UARPPlatformDownstreamEndpointByID
- _UARPSuperBinaryAddMetaData
- _UARPSuperBinaryAddPayload
- _UARPSuperBinaryAddPayload2
- _UARPSuperBinaryAddPayloadData
- _UARPSuperBinaryAddPayloadDataLarge
- _UARPSuperBinaryAddPayloadMetaData
- _UARPSuperBinaryAddSuperBinaryMetaData
- _UARPSuperBinaryAppendPayloadMetaData
- _UARPSuperBinaryAppendPayloadMetaDataBlob
- _UARPSuperBinaryBuildMetaData
- _UARPSuperBinaryFinalizeDynamicAsset
- _UARPSuperBinaryFinalizeHeader
- _UARPSuperBinaryGetInternalPayloadMetaData
- _UARPSuperBinaryGetInternalSuperBinaryMetaData
- _UARPSuperBinaryPrepareDynamicAsset
- _UARPSuperBinaryPreparePayload
- _UARPSuperBinaryQueryAssetLength
- _UARPSuperBinarySetupHeader
- __os_log_fault_impl
- _bzero
- _calloc
- _compression_decode_buffer
- _fUarpLayer3DownstreamEndpointDiscovery
- _fUarpLayer3DownstreamEndpointReachable
- _fUarpLayer3DownstreamEndpointRecvMessage
- _fUarpLayer3DownstreamEndpointReleased
- _fUarpLayer3DownstreamEndpointUnreachable
- _fUarpLayer3NoFirmwareUpdateAvailable
- _getCachedAccessories
- _latestMobileAssetCacheFileURL
- _memcmp
- _memcpy
- _mobileAssetCacheFileURLForRemoteURL
- _mobileAssetStateToString
- _objc_autorelease
- _objc_msgSend$accessoryNameForIdentifier:name:serialNumber:fusingType:
- _objc_msgSend$arrayWithContentsOfFile:
- _objc_msgSend$checkResourceIsReachableAndReturnError:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$containsObject:
- _objc_msgSend$copyItemAtURL:toURL:error:
- _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$enumeratorAtPath:
- _objc_msgSend$fileURLWithPath:isDirectory:
- _objc_msgSend$getBytes:range:
- _objc_msgSend$migrateExistingDefaults
- _objc_msgSend$nextObject
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$pathExtension
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$seedParticipationDictionary
- _objc_msgSend$setAttributes:ofItemAtPath:error:
- _objc_msgSend$supportsInternalSettings
- _objc_msgSend$versionFromString:version:
- _snprintf
- _uarp4ccCompare
- _uarpAllocPrepareTransmitBuffer2
- _uarpAllocateTransmitBuffer2
- _uarpApplyFlagsToString
- _uarpAssetCompare
- _uarpAssetProcessingComplete
- _uarpAssetQueryPayloadInfo
- _uarpAssetQueryPayloadMetaData
- _uarpAssetQuerySuperBinaryMetaData
- _uarpAssetQueueSolicitation
- _uarpAssetRescind
- _uarpAssetSuperBinaryVersionForProtocolVersion
- _uarpAssetTagChdr
- _uarpAssetTagChdr4cc
- _uarpAssetTagCompare
- _uarpAssetTagIsValid
- _uarpAssetTagStructChdr
- _uarpAssetTagStructSuperBinary
- _uarpAvailableTransmitBuffer
- _uarpCallbackUpdateInformationTLV
- _uarpCompressionHeaderEndianSwap
- _uarpCopyDefaultInfoString
- _uarpDownstreamEndpointGetID
- _uarpEndpointRoleToString
- _uarpFilepathForRemotePath
- _uarpFree
- _uarpHtonl
- _uarpHtonll
- _uarpHtons
- _uarpLogDebug
- _uarpLogError
- _uarpLogFault
- _uarpLogInfo
- _uarpLogToken
- _uarpLoggingCategoryToString
- _uarpNtohl
- _uarpNtohll
- _uarpNtohs
- _uarpOfferAssetToRemoteEP
- _uarpOuiCompare
- _uarpPayloadHeader2EndianSwap
- _uarpPayloadHeaderEndianSwap
- _uarpPayloadTagPack
- _uarpPayloadTagStructPack
- _uarpPayloadTagStructUnpack
- _uarpPayloadTagUnpack
- _uarpPlatformAssetAllMetaDataRequestCompleted
- _uarpPlatformAssetAllMetaDataWindowFilled
- _uarpPlatformAssetAllPayloadHeadersRequestCompleted
- _uarpPlatformAssetAllPayloadHeadersRequestWindowFilled
- _uarpPlatformAssetApproveOfferVersion
- _uarpPlatformAssetCleanup
- _uarpPlatformAssetDataRequest
- _uarpPlatformAssetFindByAssetContext
- _uarpPlatformAssetFindByAssetContextAndList
- _uarpPlatformAssetFindByAssetID
- _uarpPlatformAssetFindByTag
- _uarpPlatformAssetIsKnown
- _uarpPlatformAssetOrphan
- _uarpPlatformAssetPayloadDataRequestCompleted
- _uarpPlatformAssetPayloadDataRequestCompressedBlock
- _uarpPlatformAssetPayloadDataRequestCompressionHeader
- _uarpPlatformAssetPayloadDataRequestWindowFilled
- _uarpPlatformAssetPayloadHeaderProcess
- _uarpPlatformAssetPayloadHeaderRequestCompleted
- _uarpPlatformAssetPayloadHeaderRequestWindowFilled
- _uarpPlatformAssetPayloadMetaDataRequestCompleted
- _uarpPlatformAssetPayloadMetaDataRequestWindowFilled
- _uarpPlatformAssetPayloadPullData
- _uarpPlatformAssetPayloadPullMetaData
- _uarpPlatformAssetProcessingCompleteInternal
- _uarpPlatformAssetPullAllMetaData
- _uarpPlatformAssetPullAllPayloadHeaders
- _uarpPlatformAssetQueryAssetID
- _uarpPlatformAssetQueryAssetVersion
- _uarpPlatformAssetRelease
- _uarpPlatformAssetRequestData
- _uarpPlatformAssetRescind
- _uarpPlatformAssetRescinded
- _uarpPlatformAssetResponseData
- _uarpPlatformAssetSelectedPayloadInfo
- _uarpPlatformAssetSuperBinaryMetaDataRequestCompleted
- _uarpPlatformAssetSuperBinaryMetaDataRequestWindowFilled
- _uarpPlatformAssetSuperBinaryPullHeader
- _uarpPlatformAssetSuperBinaryPullMetaData
- _uarpPlatformAssetSuperBinaryPullProposedPayloadHeader
- _uarpPlatformAssetSuperBinaryRequestCompleted
- _uarpPlatformAssetSuperBinaryRequestWindowFilled
- _uarpPlatformAssetUpdateMetaData
- _uarpPlatformCancelPendingTxMessages
- _uarpPlatformCancelRxDynamicAssets
- _uarpPlatformCleanupAssetsForRemoteEndpoint
- _uarpPlatformCompareHash
- _uarpPlatformCreateRxAsset
- _uarpPlatformDarwinCompressBuffer
- _uarpPlatformDarwinDecompressBuffer
- _uarpPlatformDarwinHashFinal
- _uarpPlatformDarwinHashInfo
- _uarpPlatformDarwinHashInit
- _uarpPlatformDarwinHashLog
- _uarpPlatformDarwinHashUpdate
- _uarpPlatformDarwinLogDebug
- _uarpPlatformDarwinLogError
- _uarpPlatformDarwinLogFault
- _uarpPlatformDarwinLogInfo
- _uarpPlatformDataTransferResume
- _uarpPlatformDownstreamEndpointAdd
- _uarpPlatformDownstreamEndpointAddWithID
- _uarpPlatformDownstreamEndpointDiscovery
- _uarpPlatformDownstreamEndpointRemove
- _uarpPlatformDownstreamEndpointSendMessage
- _uarpPlatformDownstreamEndpointSendMessageInternal
- _uarpPlatformEndpointApplyStagedAssets
- _uarpPlatformEndpointAssetAbandon
- _uarpPlatformEndpointAssetAccept
- _uarpPlatformEndpointAssetAcceptWithPayloadAndDecompressionWindows
- _uarpPlatformEndpointAssetAcceptWithPayloadWindow
- _uarpPlatformEndpointAssetCorrupt
- _uarpPlatformEndpointAssetDeny
- _uarpPlatformEndpointAssetFullyStaged
- _uarpPlatformEndpointAssetGetBytesAtOffset
- _uarpPlatformEndpointAssetIsAcceptable
- _uarpPlatformEndpointAssetPayloadTag
- _uarpPlatformEndpointAssetPayloadVersion
- _uarpPlatformEndpointAssetQueryAssetLength
- _uarpPlatformEndpointAssetQueryAssetVersion
- _uarpPlatformEndpointAssetQueryFormatVersion
- _uarpPlatformEndpointAssetQueryNumberOfPayloads
- _uarpPlatformEndpointAssetQueryTag
- _uarpPlatformEndpointAssetRelease
- _uarpPlatformEndpointAssetRelease2
- _uarpPlatformEndpointAssetRequestMetaData
- _uarpPlatformEndpointAssetSetBytesAtOffset
- _uarpPlatformEndpointAssetSetCallbacks
- _uarpPlatformEndpointAssetSetPayloadIndex
- _uarpPlatformEndpointAssetSetPayloadIndex2
- _uarpPlatformEndpointAssetSetPayloadOffset
- _uarpPlatformEndpointAssetStore
- _uarpPlatformEndpointCleanupAssets
- _uarpPlatformEndpointCleanupAssets2
- _uarpPlatformEndpointDynamicAssetSolicitationDeny
- _uarpPlatformEndpointInit
- _uarpPlatformEndpointInit2
- _uarpPlatformEndpointIsMessageTypePending
- _uarpPlatformEndpointOfferAsset
- _uarpPlatformEndpointPauseAssetTransfers
- _uarpPlatformEndpointPayloadRequestAllHeadersAndMetaData
- _uarpPlatformEndpointPayloadRequestData
- _uarpPlatformEndpointPayloadRequestDataPause
- _uarpPlatformEndpointPayloadRequestDataResume
- _uarpPlatformEndpointPayloadRequestMetaData
- _uarpPlatformEndpointPrepareDynamicAsset
- _uarpPlatformEndpointPrepareSolicitedDynamicAsset
- _uarpPlatformEndpointPrepareSuperBinary
- _uarpPlatformEndpointProvideAssetPayloadWindow
- _uarpPlatformEndpointQueryActiveFirmwareVersion
- _uarpPlatformEndpointQueryStagedFirmwareVersion
- _uarpPlatformEndpointRecvMessage
- _uarpPlatformEndpointRemoveAssetPayloadWindow
- _uarpPlatformEndpointRequestInfoProperty
- _uarpPlatformEndpointRescindAllAssets
- _uarpPlatformEndpointRescindAsset
- _uarpPlatformEndpointResumeAssetTransfers
- _uarpPlatformEndpointSendMessageComplete
- _uarpPlatformEndpointSendMessageCompleteInternal
- _uarpPlatformEndpointSendSyncMsg
- _uarpPlatformEndpointSendVendorSpecific
- _uarpPlatformEndpointSolicitDynamicAsset
- _uarpPlatformEndpointStreamingRecvBytes
- _uarpPlatformEndpointStreamingRecvDeinit
- _uarpPlatformEndpointStreamingRecvInit
- _uarpPlatformEndpointSuperBinaryMerge
- _uarpPlatformEndpointWatchDogExpired
- _uarpPlatformFindPreparedAsset
- _uarpPlatformGarbageCollection
- _uarpPlatformGetMaxRxPayloadLength
- _uarpPlatformGetMaxTxPayloadLength
- _uarpPlatformNoFirmwareUpdateAvailable
- _uarpPlatformPayloadCleanup
- _uarpPlatformPrepareAsset
- _uarpPlatformQueryAccessoryInfo
- _uarpPlatformReOfferFirmware
- _uarpPlatformRemoteDelegateForAssetDelegate
- _uarpPlatformRemoteEndpointAdd
- _uarpPlatformRemoteEndpointAddEntry
- _uarpPlatformRemoteEndpointAlloc
- _uarpPlatformRemoteEndpointRemove
- _uarpPlatformResponseAccessoryInfo
- _uarpPlatformSetMaxRxPayloadLength
- _uarpPlatformSetMaxTxPayloadLength
- _uarpPlatformTransmitQueueLogEntry
- _uarpPrintDataResponseDetails
- _uarpProcessPayloadTLVInternal
- _uarpProcessTLV
- _uarpProcessingFlagsReasonToString
- _uarpProcessingFlagsToString
- _uarpProcessingStatusToString
- _uarpRemoteEndpointID
- _uarpRemoteEndpointIDForAsset
- _uarpSendAssetRequestData
- _uarpSendDataTransferNotification
- _uarpSendDataTransferNotificationPause
- _uarpSendDataTransferNotificationResume
- _uarpSendDownstreamEndpointDiscovery
- _uarpSendDownstreamEndpointReachable
- _uarpSendDownstreamEndpointUnreachable
- _uarpSendDynamicAssetPreProcessingStatus
- _uarpSendInformationRequest
- _uarpSendVendorSpecific
- _uarpSendVersionDiscoveryRequest
- _uarpSendVersionDiscoveryResponse
- _uarpSolicitDynamicAsset
- _uarpStageStatusToString
- _uarpStatusCodeToString
- _uarpSuperBinaryHeaderEndianSwap
- _uarpTagStructPack32
- _uarpTagStructUnpack32
- _uarpTransmitBuffer2
- _uarpTransmitBufferUpstream
- _uarpTransmitQueueAssetRescinded
- _uarpTransmitQueuePendingEntryComplete
- _uarpTransmitQueueProcessRecv
- _uarpTransmitQueueService
- _uarpTransmitQueuesCleanup
- _uarpVersionCompare
- _uarpVersionEndianSwap
- _uarpZalloc
- _uarpZero
- _vsnprintf
- getSuperBinaryVersionForAsset.cold.1
- getSuperBinaryVersionForAsset.cold.2
- latestMobileAssetCacheFileURL.cold.1
- mobileAssetCacheFileURLForRemoteURL.cold.1
- mobileAssetCacheFileURLForRemoteURL.cold.2
- uarpAssetTagChdr4cc.assetTag
- uarpAssetTagStructChdr.myTag
- uarpAssetTagStructSuperBinary.myTag
- uarpCopyDefaultInfoString.unknown
- uarpFilepathForRemotePath.cold.1
- uarpFilepathForRemotePath.cold.2
- uarpLogDebug.cold.1
- uarpLogDebug.logBuffer
- uarpLogError.cold.1
- uarpLogError.logBuffer
- uarpLogFault.cold.1
- uarpLogFault.logBuffer
- uarpLogInfo.logBuffer
- uarpLogToken.tokens
- uarpPlatformDarwinLogDebug.cold.1
- uarpPlatformDarwinLogDebug.logBuffer
- uarpPlatformDarwinLogError.cold.1
- uarpPlatformDarwinLogError.logBuffer
- uarpPlatformDarwinLogFault.cold.1
- uarpPlatformDarwinLogFault.logBuffer
- uarpPlatformDarwinLogInfo.logBuffer
- uarpStageStatusToString.stageStatusString
CStrings:
+ "%@/%@/%@%@"
+ "%@/AirPods2022Seed"
+ "%s: Invalid key value / pair = %@ / %@"
+ "%s: setting %@"
+ "%s: unknown key/value pair %@/%@"
+ "-[AUDeveloperSettingsDatabase accessoryList]_block_invoke"
+ "-[AUDeveloperSettingsDatabase updateAccessoryWithSerialNumber:info:]"
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "@48@0:8@16@24@32@40"
+ "AUDeveloperSettingsUpdateAccessory:withKey:"
+ "AirPodsDeveloperSeed"
+ "Removing accessory from database %@"
+ "SupportsDeveloperSettings"
+ "T@\"NSArray\",R,V_partnerSerialNumbers"
+ "T@\"NSString\",R,V_activeVersion"
+ "T@\"NSString\",R,V_assetLocation"
+ "T@\"NSString\",R,V_assetURLOverride"
+ "T@\"NSString\",R,V_customBuild"
+ "T@\"NSString\",R,V_customTrain"
+ "T@\"NSString\",R,V_downloadedVersion"
+ "T@\"NSString\",R,V_dropboxVersion"
+ "T@\"NSString\",R,V_hwFusing"
+ "T@\"NSString\",R,V_hwRevision"
+ "T@\"NSString\",R,V_modelNumber"
+ "T@\"NSString\",R,V_name"
+ "T@\"NSString\",R,V_serialNumber"
+ "T@\"NSString\",R,V_supplementalAssetLocation"
+ "T@\"NSString\",R,V_supplementalCustomBuild"
+ "T@\"NSString\",R,V_supplementalCustomTrain"
+ "TB,R,V_accessoryReachable"
+ "TB,R,V_authListingEnabled"
+ "TB,R,V_otaDisabled"
+ "TB,R,V_personalizationRequired"
+ "TB,R,V_supportsDeveloperSettings"
+ "UARPSettingsAccessory"
+ "Updating database with %@ / %@"
+ "_accessoryReachable"
+ "_activeVersion"
+ "_assetLocation"
+ "_assetURLOverride"
+ "_authListingEnabled"
+ "_customBuild"
+ "_customTrain"
+ "_downloadedVersion"
+ "_dropboxVersion"
+ "_hwFusing"
+ "_hwRevision"
+ "_modelNumber"
+ "_name"
+ "_originalSettings"
+ "_otaDisabled"
+ "_partnerSerialNumbers"
+ "_personalizationRequired"
+ "_serialNumber"
+ "_supplementalAssetLocation"
+ "_supplementalCustomBuild"
+ "_supplementalCustomTrain"
+ "_supportsDeveloperSettings"
+ "accessoryList"
+ "copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:"
+ "copyAccessoryWithSerialNumber:"
+ "customBuild"
+ "customTrain"
+ "encodeAsChangedDictionary"
+ "encodeAsDictionary"
+ "https://basejumper.apple.com"
+ "hwFusing"
+ "initWithDictionary:"
+ "isEqualToArray:"
+ "isEqualToNumber:"
+ "null"
+ "otaDisabled"
+ "removeAccessory:"
+ "setAccessoryReachable:"
+ "setActiveVersion:"
+ "setAssetLocation:"
+ "setAssetURLOverride:"
+ "setAuthListingEnabled:"
+ "setCustomBuild:"
+ "setCustomTrain:"
+ "setDownloadedVersion:"
+ "setDropboxVersion:"
+ "setHwFusing:"
+ "setHwRevision:"
+ "setModelNumber:"
+ "setName:"
+ "setOtaDisabled:"
+ "setPartnerSerialNumbers:"
+ "setPersonalizationRequired:"
+ "setSerialNumber:"
+ "setSupplementalAssetLocation:"
+ "setSupplementalCustomBuild:"
+ "setSupplementalCustomTrain:"
+ "setSupportsDeveloperSettings:"
+ "supplementalCustomBuild"
+ "supplementalCustomTrain"
+ "supportsDeveloperSettings"
+ "updateAccessory:"
+ "updateAccessoryWithSerialNumber:info:"
+ "userPreferenceUpdateAccessorySettings:withKey:"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "v32@?0@8@16^B24"
- "%@/%@/%@/%@"
- "%@/%s"
- "%s\n"
- "%s (%s)"
- "%s: Failed to create UARP Firmware directory error: %@"
- "%s: Failed to set permission for location %@: %@"
- "%s: Failed to write to path %@"
- "%s: Invalid firmware file %@"
- "%s: UARP Firmware directory created %@"
- "%s: Valid firmware file %@"
- "%s: Valid firmware file, firmwareVersion is %@"
- "%s: Valid firmware file, uarpAccessoryPath(1) is %@"
- "%s: Valid firmware file, uarpAccessoryPath(2) is %@"
- "%s: Valid firmware file, uarpFileName is %@"
- "%s: Valid firmware file, uarpFilePath is %@"
- "%s: dictionary = %@"
- "%s: seting %@:%@"
- "%u.%u.%u"
- "+"
- "-%@"
- "-[AUDeveloperSettingsDatabase seedParticipationDictionary]"
- ".%u"
- "/%@"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP status=<%s>, offset=0x%08x, requestedlength=%u, respondedlength=%u"
- "<unknown>"
- "Accessory"
- "Active Firmware Version Equal to Asset"
- "Active Firmware Version Greater than Asset"
- "Asset Corrupt"
- "Asset Data Paused"
- "Asset Decompression Failure"
- "Asset Id Unknown"
- "Asset In Flight"
- "Asset Invalid Compression"
- "Asset No Bytes Remaining"
- "Asset Not Found"
- "Asset Transfer Complete"
- "Better Transport"
- "Cancelled Asset Tag"
- "Checking mobileasset cache file %@"
- "Controller"
- "Corrupt SuperBinary"
- "Data Transfer Paused"
- "Device Error"
- "Duplicate Accessory"
- "Duplicate Controller"
- "Duplicate Message ID"
- "Error decompressing buffer for payload"
- "Exceeded Packet Retry"
- "Failed to open file %{public}@ with error %{public}@"
- "Failure"
- "Higher Version Active"
- "HigherVersion"
- "Host Controller"
- "In Progress"
- "In Use"
- "Incompatible Protocol Version"
- "Invalid Argument"
- "Invalid Asset Tag"
- "Invalid Asset Type"
- "Invalid Data Request Length"
- "Invalid Data Request Offset"
- "Invalid Data Request Type"
- "Invalid Data Response"
- "Invalid Data Response Length"
- "Invalid Data Transfer Notification"
- "Invalid Function Pointer"
- "Invalid Length"
- "Invalid Message"
- "Invalid Message Length"
- "Invalid Object"
- "Invalid Offset"
- "Invalid Payload"
- "Invalid Payload Header"
- "Invalid Super Binary Header"
- "Invalid TLV"
- "Low Battery"
- "MADownloading"
- "MAInstalled"
- "MAInstalledNotInCatalog"
- "MAInstalledWithOs"
- "MAInvalid"
- "MANotPresent"
- "MARequiredByOs"
- "MAUnknown"
- "MetaData Corrupt"
- "MetaData Overflow"
- "MetaData Type Not Found"
- "Mid Upload"
- "Mismatch Data Offset"
- "Mismatch Personalization Option"
- "Mismatch UUID"
- "Needs Restart"
- "No MetaData"
- "No Resources"
- "No Version Agreement"
- "Nothing Staged"
- "Out Of Order Message ID"
- "Personalization Failure"
- "Priority Activity"
- "Processing Error"
- "Processing Incomplete"
- "Same Version Active"
- "Same Version Staged"
- "Staged Firmware Version Equal to Asset"
- "Staged Firmware Version Greater than Asset"
- "Success"
- "SuperBinary file %{public}@ has invalid length %{public}u"
- "UARP.LAYER2 <%s> Cannot find downstream endpoint"
- "Unknown Accessory"
- "Unknown Asset"
- "Unknown Controller"
- "Unknown Data Transfer State"
- "Unknown Downstream Endpoint"
- "Unknown Failure"
- "Unknown Information Option"
- "Unknown Message Type"
- "Unknown Payload"
- "Unknown Personalization Option"
- "Unsupported"
- "Unsupported Asset Tag"
- "Unsupported Hardware Revision"
- "Unsupported Message Type"
- "Upload Abandoned"
- "Upload Complete"
- "Upload Denied"
- "arrayWithContentsOfFile:"
- "assert"
- "checkResourceIsReachableAndReturnError:"
- "com.apple.uarp.embedded"
- "componentsSeparatedByString:"
- "containsObject:"
- "copyItemAtURL:toURL:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dataWithContentsOfFile:options:error:"
- "dictionaryWithObjects:forKeys:count:"
- "downstream"
- "enumeratorAtPath:"
- "fileURLWithPath:isDirectory:"
- "getBytes:range:"
- "memory"
- "migrateExistingDefaults"
- "mobileAssetCache"
- "mobileAssetCacheFileURLForRemoteURL"
- "nextObject"
- "objectAtIndexedSubscript:"
- "pathExtension"
- "pathWithComponents:"
- "platform"
- "prod"
- "product"
- "protocolaccessory"
- "protocolcontroller"
- "seedParticipation"
- "seedParticipationDictionary"
- "setAttributes:ofItemAtPath:error:"
- "streaming"
- "success"
- "supportsInternalSettings"
- "transmitqueue"
- "uarp"
- "uarpAccessories.plist"
- "uarpFilepathForRemotePath"
- "uarpMsgRecvDownstreamEndpointMessage"
- "versionFromString:version:"

```
