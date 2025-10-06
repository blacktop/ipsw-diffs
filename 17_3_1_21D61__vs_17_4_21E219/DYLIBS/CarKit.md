## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-533.8.0.0.0
-  __TEXT.__text: 0x35a50
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x3724
+553.12.2.0.0
+  __TEXT.__text: 0x42f78
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x4064
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x398d
-  __TEXT.__oslogstring: 0x32a0
-  __TEXT.__ustring: 0x24
-  __TEXT.__gcc_except_tab: 0x580
+  __TEXT.__cstring: 0x4201
+  __TEXT.__gcc_except_tab: 0x72c
+  __TEXT.__oslogstring: 0x45a3
+  __TEXT.__ustring: 0x62
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__unwind_info: 0xfc0
-  __TEXT.__objc_classname: 0x791
-  __TEXT.__objc_methname: 0xb3de
-  __TEXT.__objc_methtype: 0x1774
-  __TEXT.__objc_stubs: 0x6e20
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x16d8
-  __DATA_CONST.__objc_classlist: 0x190
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xf0
+  __TEXT.__unwind_info: 0x12ec
+  __TEXT.__objc_classname: 0x900
+  __TEXT.__objc_methname: 0xd1b8
+  __TEXT.__objc_methtype: 0x1cc7
+  __TEXT.__objc_stubs: 0x7e60
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x1a30
+  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x92b8
-  __DATA_CONST.__objc_selrefs: 0x24e0
-  __AUTH_CONST.__cfstring: 0x3d00
-  __AUTH_CONST.__objc_const: 0x14c0
-  __AUTH_CONST.__const: 0x1020
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x290
-  __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x4e8
-  __DATA.__data: 0xc08
-  __DATA.__bss: 0x2b0
+  __DATA_CONST.__objc_const: 0xb558
+  __DATA_CONST.__objc_selrefs: 0x2a18
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_classrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__cfstring: 0x4700
+  __AUTH_CONST.__objc_const: 0x18a8
+  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x598
+  __DATA.__data: 0xe48
+  __DATA.__bss: 0x2c8
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9009D42A-E3CE-33E4-9060-35ACAAB6AA29
-  Functions: 1743
-  Symbols:   6191
-  CStrings:  3434
+  UUID: 45B2A4E9-FD62-3865-AC01-95AA45C501F3
+  Functions: 2081
+  Symbols:   7264
+  CStrings:  4006
 
Symbols:
+ +[CARPrototypePref force3xCluster]
+ +[CARThemeAsset supportsSecureCoding]
+ +[CARThemeAssetOverrider _assetURLForAssetIdentifier:version:]
+ +[CARThemeAssetOverrider _carplayLibraryDirectoryForAssetIdentifier:]
+ +[CARThemeAssetOverrider _carplayLibraryDirectoryForAssetIdentifier:].cold.1
+ +[CARThemeAssetOverrider _carplayLibraryURL]
+ +[CARThemeAssetOverrider _contentVersionOfAsset:]
+ +[CARThemeAssetOverrider _contentVersionOfAsset:].cold.1
+ +[CARThemeAssetOverrider _generatedAssetForSourceAssetURL:assetIdentifier:version:]
+ +[CARThemeAssetOverrider _generatedAssetForSourceAssetURL:assetIdentifier:version:].cold.1
+ +[CARThemeAssetOverrider _generatedAssetForSourceAssetURL:assetIdentifier:version:].cold.2
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:]
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:].cold.1
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:].cold.2
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:].cold.3
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:].cold.4
+ +[CARThemeAssetOverrider _overrideAssetSourceURLForAssetIdentifier:].cold.5
+ +[CARThemeAssetOverrider _shouldForceUpdateAsset]
+ +[CARThemeAssetOverrider overrideAssetForIdentifer:greaterThanVersion:]
+ +[CARThemeAssetOverrider postAssetErrorNotification:forAsset:]
+ +[CARThemeAssetOverrider postAssetErrorNotification:forAsset:].cold.1
+ +[CRAssetWallpaperData supportsBSXPCSecureCoding]
+ +[CRAssetWallpaperData supportsSecureCoding]
+ +[CRCarPlayAppDeclaration declarationForAppRecord:]
+ +[CRCarPlayAppDeclaration declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:]
+ +[CRCarPlayAppDeclaration declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:bundlePath:]
+ +[CRDisplayThemeData supportsSecureCoding]
+ +[CRSystemWallpaperData supportsBSXPCSecureCoding]
+ +[CRSystemWallpaperData supportsSecureCoding]
+ -[CARConnectionSession initWithEvents:sessionIdentifier:vehicleInformation:]
+ -[CARConnectionSession vehicleInformation]
+ -[CARDisplayInfo supportsAdditionalContent]
+ -[CARDisplayInfo supportsDDPContent]
+ -[CARSession initWithFigEndpoint:sessionStatusOptions:]
+ -[CARSession sessionStatusOptions]
+ -[CARSessionChannel payloadCount]
+ -[CARSessionChannel sendChannelMessage:withDescription:]
+ -[CARSessionChannel setPayloadCount:]
+ -[CARSessionConfiguration hasGaugeClusterScreen]
+ -[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]
+ -[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:].cold.1
+ -[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:].cold.2
+ -[CARSessionConfiguration supportsLogTransfer]
+ -[CARSessionConfiguration supportsVehicleData]
+ -[CARSessionConfiguration vehicleDataPluginCount]
+ -[CARSessionConfiguration vehicleDataProtocolVersion]
+ -[CARSessionStatus sessionStatusOptions]
+ -[CARThemeAsset .cxx_destruct]
+ -[CARThemeAsset assetsArchiveURL]
+ -[CARThemeAsset baseURL]
+ -[CARThemeAsset certificateData]
+ -[CARThemeAsset certificateData].cold.1
+ -[CARThemeAsset description]
+ -[CARThemeAsset encodeWithCoder:]
+ -[CARThemeAsset identifier]
+ -[CARThemeAsset initWithCoder:]
+ -[CARThemeAsset initWithIdentifier:version:baseURL:]
+ -[CARThemeAsset isEqual:]
+ -[CARThemeAsset isEqualToThemeAsset:]
+ -[CARThemeAsset layoutURL]
+ -[CARThemeAsset signatureData]
+ -[CARThemeAsset signatureData].cold.1
+ -[CARThemeAsset version]
+ -[CARThemeAssetLibrary .cxx_destruct]
+ -[CARThemeAssetLibrary _queue_applyOverrideAsset:]
+ -[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]
+ -[CARThemeAssetLibrary _queue_startObserving]
+ -[CARThemeAssetLibrary _queue_stopObserving]
+ -[CARThemeAssetLibrary _setupServiceConnection]
+ -[CARThemeAssetLibrary addObserver:]
+ -[CARThemeAssetLibrary assetIdentifier]
+ -[CARThemeAssetLibrary findCurrentAssetWithCompletion:]
+ -[CARThemeAssetLibrary initWithVehicle:]
+ -[CARThemeAssetLibrary initWithVehicle:].cold.1
+ -[CARThemeAssetLibrary invalidate]
+ -[CARThemeAssetLibrary observerProxy]
+ -[CARThemeAssetLibrary queue]
+ -[CARThemeAssetLibrary removeObserver:]
+ -[CARThemeAssetLibrary serviceConnection]
+ -[CARThemeAssetLibrary vehicleIdentifier]
+ -[CARThemeAssetLibraryAgent .cxx_destruct]
+ -[CARThemeAssetLibraryAgent _addConnection:]
+ -[CARThemeAssetLibraryAgent _performObserverAction:]
+ -[CARThemeAssetLibraryAgent _removeConnection:]
+ -[CARThemeAssetLibraryAgent connections]
+ -[CARThemeAssetLibraryAgent delegate]
+ -[CARThemeAssetLibraryAgent init]
+ -[CARThemeAssetLibraryAgent invalidate]
+ -[CARThemeAssetLibraryAgent listener:shouldAcceptNewConnection:]
+ -[CARThemeAssetLibraryAgent listener:shouldAcceptNewConnection:].cold.1
+ -[CARThemeAssetLibraryAgent notifyAttemptingDownloadForAssetIdentifier:version:]
+ -[CARThemeAssetLibraryAgent notifyCompletedDownloadOfAsset:]
+ -[CARThemeAssetLibraryAgent notifyDidUpdateFromAsset:toAsset:forVehicleIdentifier:]
+ -[CARThemeAssetLibraryAgent notifyFailedDownloadForAssetIdentifier:version:error:]
+ -[CARThemeAssetLibraryAgent service_applyOverrideAsset:forVehicleIdentifier:reply:]
+ -[CARThemeAssetLibraryAgent service_currentAssetForVehicleIdentifier:reply:]
+ -[CARThemeAssetLibraryAgent service_startObservingWithReply:]
+ -[CARThemeAssetLibraryAgent service_stopObservingWithReply:]
+ -[CARThemeAssetLibraryAgent setConnections:]
+ -[CARThemeAssetLibraryAgent setDelegate:]
+ -[CARThemeAssetLibraryObserverProxy .cxx_destruct]
+ -[CARThemeAssetLibraryObserverProxy assetLibrary]
+ -[CARThemeAssetLibraryObserverProxy init]
+ -[CARThemeAssetLibraryObserverProxy observers]
+ -[CARThemeAssetLibraryObserverProxy service_attemptingDownloadForAssetIdentifier:version:reply:]
+ -[CARThemeAssetLibraryObserverProxy service_completedDownloadForAsset:reply:]
+ -[CARThemeAssetLibraryObserverProxy service_didUpdateFromAsset:toAsset:forVehicleIdentifier:reply:]
+ -[CARThemeAssetLibraryObserverProxy service_failedDownloadForAssetIdentifier:version:error:reply:]
+ -[CARThemeAssetLibraryObserverProxy setAssetLibrary:]
+ -[CRAssetWallpaperData .cxx_destruct]
+ -[CRAssetWallpaperData asDictionary]
+ -[CRAssetWallpaperData asDictionary].cold.1
+ -[CRAssetWallpaperData description]
+ -[CRAssetWallpaperData displayID]
+ -[CRAssetWallpaperData encodeWithBSXPCCoder:]
+ -[CRAssetWallpaperData encodeWithCoder:]
+ -[CRAssetWallpaperData identifier]
+ -[CRAssetWallpaperData initWithBSXPCCoder:]
+ -[CRAssetWallpaperData initWithCoder:]
+ -[CRAssetWallpaperData initWithDictionary:]
+ -[CRAssetWallpaperData initWithWallpaperIdentifier:displayID:layoutID:]
+ -[CRAssetWallpaperData isEqual:]
+ -[CRAssetWallpaperData layoutID]
+ -[CRAssetWallpaperData wallpaperID]
+ -[CRCarPlayPreferences isCarPlayThemeSupportEnabled]
+ -[CRCarPlayPreferences profileConnection]
+ -[CRCarPlayPreferences setProfileConnection:]
+ -[CRDisplayThemeData .cxx_destruct]
+ -[CRDisplayThemeData asDictionary]
+ -[CRDisplayThemeData currentLayoutID]
+ -[CRDisplayThemeData currentPaletteID]
+ -[CRDisplayThemeData currentPaletteID].cold.1
+ -[CRDisplayThemeData currentWallpaper]
+ -[CRDisplayThemeData currentWallpaper].cold.1
+ -[CRDisplayThemeData description]
+ -[CRDisplayThemeData encodeWithCoder:]
+ -[CRDisplayThemeData initWithCoder:]
+ -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:]
+ -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:].cold.1
+ -[CRDisplayThemeData initWithDictionary:]
+ -[CRDisplayThemeData initWithDictionary:].cold.1
+ -[CRDisplayThemeData isEqual:]
+ -[CRDisplayThemeData paletteIDForLayout]
+ -[CRDisplayThemeData themeDataWithCurrentLayoutID:]
+ -[CRDisplayThemeData themeDataWithCurrentPaletteID:]
+ -[CRDisplayThemeData themeDataWithCurrentWallpaper:]
+ -[CRDisplayThemeData wallpaperForLayout]
+ -[CRFeatureAvailability .cxx_destruct]
+ -[CRFeatureAvailability deviceSupportedCarPlayFeatures]
+ -[CRFeatureAvailability deviceSupportedCarPlayFeatures].cold.1
+ -[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]
+ -[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:].cold.1
+ -[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]
+ -[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:].cold.1
+ -[CRFeatureAvailability init]
+ -[CRFeatureAvailability isCarPlayAllowed]
+ -[CRFeatureAvailability isCarPlayAllowed].cold.1
+ -[CRFeatureAvailability serviceClient]
+ -[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]
+ -[CRFeatureAvailability setServiceClient:]
+ -[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]
+ -[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:].cold.1
+ -[CRFeatureAvailability supportedCarPlayFeaturesForSession:]
+ -[CRFeatureAvailability supportedCarPlayFeaturesForSession:].cold.1
+ -[CRSystemWallpaperData .cxx_destruct]
+ -[CRSystemWallpaperData asDictionary]
+ -[CRSystemWallpaperData asDictionary].cold.1
+ -[CRSystemWallpaperData description]
+ -[CRSystemWallpaperData encodeWithBSXPCCoder:]
+ -[CRSystemWallpaperData encodeWithCoder:]
+ -[CRSystemWallpaperData identifier]
+ -[CRSystemWallpaperData initWithBSXPCCoder:]
+ -[CRSystemWallpaperData initWithCoder:]
+ -[CRSystemWallpaperData initWithDictionary:]
+ -[CRSystemWallpaperData initWithIdentifier:]
+ -[CRSystemWallpaperData isEqual:]
+ -[CRVehicle SDKVersion]
+ -[CRVehicle assetDescription]
+ -[CRVehicle clusterAssetIdentifier]
+ -[CRVehicle clusterAssetURL]
+ -[CRVehicle clusterAssetVersion]
+ -[CRVehicle colorFilterPreference]
+ -[CRVehicle disabledFeaturesPreference]
+ -[CRVehicle displayThemeData]
+ -[CRVehicle finishedWelcome]
+ -[CRVehicle hasGaugeClusterScreen]
+ -[CRVehicle isSiriBargeInDisabled]
+ -[CRVehicle previousSystemWallpaperData]
+ -[CRVehicle setClusterAssetIdentifier:]
+ -[CRVehicle setClusterAssetURL:]
+ -[CRVehicle setClusterAssetVersion:]
+ -[CRVehicle setColorFilterPreference:]
+ -[CRVehicle setDisabledFeaturesPreference:]
+ -[CRVehicle setDisplayThemeData:]
+ -[CRVehicle setFinishedWelcome:]
+ -[CRVehicle setHasGaugeClusterScreen:]
+ -[CRVehicle setPreviousSystemWallpaperData:]
+ -[CRVehicle setSDKVersion:]
+ -[CRVehicle setSiriBargeInDisabled:]
+ -[CRVehicle setStagedClusterAssetURL:]
+ -[CRVehicle setStagedClusterAssetVersion:]
+ -[CRVehicle setSupportsBluetoothLE:]
+ -[CRVehicle setSupportsMixableAudio:]
+ -[CRVehicle setSupportsThemeAssets:]
+ -[CRVehicle setSystemWallpaperData:]
+ -[CRVehicle setWallpaper:forDisplayWithID:requiresDarkAppearance:]
+ -[CRVehicle setWallpaper:forDisplayWithID:requiresDarkAppearance:].cold.1
+ -[CRVehicle stagedClusterAssetURL]
+ -[CRVehicle stagedClusterAssetVersion]
+ -[CRVehicle supportsBluetoothLE]
+ -[CRVehicle supportsMixableAudio]
+ -[CRVehicle supportsThemeAssets]
+ -[CRVehicle systemWallpaperData]
+ -[CRVehicle wallpaperDescription]
+ -[CRVehicle wallpaperForDisplayWithID:]
+ -[CRVehicle wallpaperForDisplayWithID:].cold.1
+ -[CRVehicleAccessory coreAccessoriesEndpointUUID]
+ -[CRVehicleAccessory digitalCarKeyInformation]
+ -[CRVehicleAccessory sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:]
+ -[CRVehicleAccessory setDigitalCarKeyInformation:]
+ -[CRVehicleAccessory setSupportsBluetoothLE:]
+ -[CRVehicleAccessory setSupportsThemeAssets:]
+ -[CRVehicleAccessory supportsBluetoothLE]
+ -[CRVehicleAccessory supportsThemeAssets]
+ -[LSPropertyList(Helpers) boolForKey:]
+ GCC_except_table115
+ GCC_except_table133
+ GCC_except_table156
+ GCC_except_table162
+ GCC_except_table188
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table61
+ GCC_except_table69
+ GCC_except_table85
+ GCC_except_table93
+ GCC_except_table99
+ _CARCarKitVehicleInformationEvent
+ _CARLimitedUIValueUserInterfaceAutomakerSettings
+ _CARLimitedUIValueUserInterfacePairedDevices
+ _CARLimitedUIValueUserInterfaceThemeCustomization
+ _CARSignpostLogForCategory.logObjects
+ _CARThemeAssetArchiveFilename
+ _CARThemeAssetCertificateFilename
+ _CARThemeAssetInfoFilename
+ _CARThemeAssetLayoutFilename
+ _CARThemeAssetSignatureFilename
+ _CARThemeAssetUnarchivedFolderName
+ _CARTransport
+ _CARkAPEndpointInfoResponseKey_LogTransferDataChannels
+ _CARkAPEndpointInfoResponseKey_VehicleStateProtocolInfo
+ _CARkVehicleStateProtocolInfoKey_PluginCount
+ _CARkVehicleStateProtocolInfoKey_ProtocolVersion
+ _CFAutorelease
+ _CRCarPlayFeaturesAllFerriteFeatures
+ _CRCarPlayFeaturesAsAirPlayFeatures
+ _CRCarPlayFeaturesName
+ _CRConnectBluetoothLE
+ _CRHandleBluetoothClassicPairingCompleted
+ _CRPresentBluetoothClassicPairingConfirmation
+ _CRPresentBluetoothClassicPairingError
+ _CRPresentCarPlayOnlyBluetoothClassicPairingConfirmation
+ _CarThemeAssetsLogging
+ _CarThemeAssetsLogging.facility
+ _CarThemeAssetsLogging.onceToken
+ _OBJC_CLASS_$_CARThemeAsset
+ _OBJC_CLASS_$_CARThemeAssetLibrary
+ _OBJC_CLASS_$_CARThemeAssetLibraryAgent
+ _OBJC_CLASS_$_CARThemeAssetLibraryObserverProxy
+ _OBJC_CLASS_$_CARThemeAssetOverrider
+ _OBJC_CLASS_$_CRAssetWallpaperData
+ _OBJC_CLASS_$_CRDisplayThemeData
+ _OBJC_CLASS_$_CRFeatureAvailability
+ _OBJC_CLASS_$_CRSystemWallpaperData
+ _OBJC_CLASS_$_LSPropertyList
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_IVAR_$_CARConnectionSession._vehicleInformation
+ _OBJC_IVAR_$_CARDisplayInfo._supportsAdditionalContent
+ _OBJC_IVAR_$_CARDisplayInfo._supportsDDPContent
+ _OBJC_IVAR_$_CARSession._sessionStatusOptions
+ _OBJC_IVAR_$_CARSessionChannel._payloadCount
+ _OBJC_IVAR_$_CARSessionConfiguration._hasGaugeClusterScreen
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsLogTransfer
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsVehicleData
+ _OBJC_IVAR_$_CARSessionConfiguration._vehicleDataPluginCount
+ _OBJC_IVAR_$_CARSessionConfiguration._vehicleDataProtocolVersion
+ _OBJC_IVAR_$_CARSessionStatus._sessionStatusOptions
+ _OBJC_IVAR_$_CARThemeAsset._baseURL
+ _OBJC_IVAR_$_CARThemeAsset._identifier
+ _OBJC_IVAR_$_CARThemeAsset._version
+ _OBJC_IVAR_$_CARThemeAssetLibrary._assetIdentifier
+ _OBJC_IVAR_$_CARThemeAssetLibrary._observerProxy
+ _OBJC_IVAR_$_CARThemeAssetLibrary._queue
+ _OBJC_IVAR_$_CARThemeAssetLibrary._serviceConnection
+ _OBJC_IVAR_$_CARThemeAssetLibrary._vehicleIdentifier
+ _OBJC_IVAR_$_CARThemeAssetLibraryAgent._connections
+ _OBJC_IVAR_$_CARThemeAssetLibraryAgent._delegate
+ _OBJC_IVAR_$_CARThemeAssetLibraryObserverProxy._assetLibrary
+ _OBJC_IVAR_$_CARThemeAssetLibraryObserverProxy._observers
+ _OBJC_IVAR_$_CRAssetWallpaperData._displayID
+ _OBJC_IVAR_$_CRAssetWallpaperData._layoutID
+ _OBJC_IVAR_$_CRAssetWallpaperData._wallpaperID
+ _OBJC_IVAR_$_CRCarPlayPreferences._profileConnection
+ _OBJC_IVAR_$_CRDisplayThemeData._currentLayoutID
+ _OBJC_IVAR_$_CRDisplayThemeData._paletteIDForLayout
+ _OBJC_IVAR_$_CRDisplayThemeData._wallpaperForLayout
+ _OBJC_IVAR_$_CRFeatureAvailability._serviceClient
+ _OBJC_IVAR_$_CRSystemWallpaperData._identifier
+ _OBJC_IVAR_$_CRVehicle._SDKVersion
+ _OBJC_IVAR_$_CRVehicle._clusterAssetIdentifier
+ _OBJC_IVAR_$_CRVehicle._clusterAssetURL
+ _OBJC_IVAR_$_CRVehicle._clusterAssetVersion
+ _OBJC_IVAR_$_CRVehicle._colorFilterPreference
+ _OBJC_IVAR_$_CRVehicle._disabledFeaturesPreference
+ _OBJC_IVAR_$_CRVehicle._displayThemeData
+ _OBJC_IVAR_$_CRVehicle._finishedWelcome
+ _OBJC_IVAR_$_CRVehicle._hasGaugeClusterScreen
+ _OBJC_IVAR_$_CRVehicle._siriBargeInDisabled
+ _OBJC_IVAR_$_CRVehicle._stagedClusterAssetURL
+ _OBJC_IVAR_$_CRVehicle._stagedClusterAssetVersion
+ _OBJC_IVAR_$_CRVehicle._supportsBluetoothLE
+ _OBJC_IVAR_$_CRVehicle._supportsMixableAudio
+ _OBJC_IVAR_$_CRVehicle._supportsThemeAssets
+ _OBJC_IVAR_$_CRVehicleAccessory._digitalCarKeyInformation
+ _OBJC_IVAR_$_CRVehicleAccessory._supportsBluetoothLE
+ _OBJC_IVAR_$_CRVehicleAccessory._supportsThemeAssets
+ _OBJC_METACLASS_$_CARThemeAsset
+ _OBJC_METACLASS_$_CARThemeAssetLibrary
+ _OBJC_METACLASS_$_CARThemeAssetLibraryAgent
+ _OBJC_METACLASS_$_CARThemeAssetLibraryObserverProxy
+ _OBJC_METACLASS_$_CARThemeAssetOverrider
+ _OBJC_METACLASS_$_CRAssetWallpaperData
+ _OBJC_METACLASS_$_CRDisplayThemeData
+ _OBJC_METACLASS_$_CRFeatureAvailability
+ _OBJC_METACLASS_$_CRSystemWallpaperData
+ __OBJC_$_CATEGORY_LSPropertyList_$_Helpers
+ __OBJC_$_CLASS_METHODS_CARThemeAsset
+ __OBJC_$_CLASS_METHODS_CARThemeAssetOverrider
+ __OBJC_$_CLASS_METHODS_CRAssetWallpaperData
+ __OBJC_$_CLASS_METHODS_CRDisplayThemeData
+ __OBJC_$_CLASS_METHODS_CRSystemWallpaperData
+ __OBJC_$_CLASS_PROP_LIST_CARThemeAsset
+ __OBJC_$_CLASS_PROP_LIST_CRAssetWallpaperData
+ __OBJC_$_CLASS_PROP_LIST_CRDisplayThemeData
+ __OBJC_$_CLASS_PROP_LIST_CRSystemWallpaperData
+ __OBJC_$_INSTANCE_METHODS_CARThemeAsset
+ __OBJC_$_INSTANCE_METHODS_CARThemeAssetLibrary
+ __OBJC_$_INSTANCE_METHODS_CARThemeAssetLibraryAgent
+ __OBJC_$_INSTANCE_METHODS_CARThemeAssetLibraryObserverProxy
+ __OBJC_$_INSTANCE_METHODS_CRAssetWallpaperData
+ __OBJC_$_INSTANCE_METHODS_CRDisplayThemeData
+ __OBJC_$_INSTANCE_METHODS_CRFeatureAvailability
+ __OBJC_$_INSTANCE_METHODS_CRSystemWallpaperData
+ __OBJC_$_INSTANCE_METHODS_LSPropertyList(Helpers)
+ __OBJC_$_INSTANCE_VARIABLES_CARThemeAsset
+ __OBJC_$_INSTANCE_VARIABLES_CARThemeAssetLibrary
+ __OBJC_$_INSTANCE_VARIABLES_CARThemeAssetLibraryAgent
+ __OBJC_$_INSTANCE_VARIABLES_CARThemeAssetLibraryObserverProxy
+ __OBJC_$_INSTANCE_VARIABLES_CRAssetWallpaperData
+ __OBJC_$_INSTANCE_VARIABLES_CRDisplayThemeData
+ __OBJC_$_INSTANCE_VARIABLES_CRFeatureAvailability
+ __OBJC_$_INSTANCE_VARIABLES_CRSystemWallpaperData
+ __OBJC_$_PROP_LIST_CARThemeAsset
+ __OBJC_$_PROP_LIST_CARThemeAssetLibrary
+ __OBJC_$_PROP_LIST_CARThemeAssetLibraryAgent
+ __OBJC_$_PROP_LIST_CARThemeAssetLibraryObserverProxy
+ __OBJC_$_PROP_LIST_CRAssetWallpaperData
+ __OBJC_$_PROP_LIST_CRDisplayThemeData
+ __OBJC_$_PROP_LIST_CRFeatureAvailability
+ __OBJC_$_PROP_LIST_CRSystemWallpaperData
+ __OBJC_$_PROP_LIST_CRWallpaperData
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CARThemeAssetLibraryService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CARThemeAssetLibraryServiceObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRLayerPropertyService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRWallpaperData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CARThemeAssetLibraryObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CARThemeAssetLibraryObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CARThemeAssetLibraryService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CARThemeAssetLibraryServiceObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRLayerPropertyService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRWallpaperData
+ __OBJC_$_PROTOCOL_REFS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_REFS_CARThemeAssetLibraryObserving
+ __OBJC_$_PROTOCOL_REFS_CARThemeAssetLibraryService
+ __OBJC_$_PROTOCOL_REFS_CARThemeAssetLibraryServiceObserving
+ __OBJC_$_PROTOCOL_REFS_CRLayerPropertyService
+ __OBJC_$_PROTOCOL_REFS_CRWallpaperData
+ __OBJC_CLASS_PROTOCOLS_$_CARThemeAsset
+ __OBJC_CLASS_PROTOCOLS_$_CARThemeAssetLibrary
+ __OBJC_CLASS_PROTOCOLS_$_CARThemeAssetLibraryAgent
+ __OBJC_CLASS_PROTOCOLS_$_CARThemeAssetLibraryObserverProxy
+ __OBJC_CLASS_PROTOCOLS_$_CRAssetWallpaperData
+ __OBJC_CLASS_PROTOCOLS_$_CRDisplayThemeData
+ __OBJC_CLASS_PROTOCOLS_$_CRSystemWallpaperData
+ __OBJC_CLASS_RO_$_CARThemeAsset
+ __OBJC_CLASS_RO_$_CARThemeAssetLibrary
+ __OBJC_CLASS_RO_$_CARThemeAssetLibraryAgent
+ __OBJC_CLASS_RO_$_CARThemeAssetLibraryObserverProxy
+ __OBJC_CLASS_RO_$_CARThemeAssetOverrider
+ __OBJC_CLASS_RO_$_CRAssetWallpaperData
+ __OBJC_CLASS_RO_$_CRDisplayThemeData
+ __OBJC_CLASS_RO_$_CRFeatureAvailability
+ __OBJC_CLASS_RO_$_CRSystemWallpaperData
+ __OBJC_LABEL_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_CARThemeAssetLibraryObserving
+ __OBJC_LABEL_PROTOCOL_$_CARThemeAssetLibraryService
+ __OBJC_LABEL_PROTOCOL_$_CARThemeAssetLibraryServiceObserving
+ __OBJC_LABEL_PROTOCOL_$_CRLayerPropertyService
+ __OBJC_LABEL_PROTOCOL_$_CRWallpaperData
+ __OBJC_METACLASS_RO_$_CARThemeAsset
+ __OBJC_METACLASS_RO_$_CARThemeAssetLibrary
+ __OBJC_METACLASS_RO_$_CARThemeAssetLibraryAgent
+ __OBJC_METACLASS_RO_$_CARThemeAssetLibraryObserverProxy
+ __OBJC_METACLASS_RO_$_CARThemeAssetOverrider
+ __OBJC_METACLASS_RO_$_CRAssetWallpaperData
+ __OBJC_METACLASS_RO_$_CRDisplayThemeData
+ __OBJC_METACLASS_RO_$_CRFeatureAvailability
+ __OBJC_METACLASS_RO_$_CRSystemWallpaperData
+ __OBJC_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_PROTOCOL_$_CARThemeAssetLibraryObserving
+ __OBJC_PROTOCOL_$_CARThemeAssetLibraryService
+ __OBJC_PROTOCOL_$_CARThemeAssetLibraryServiceObserving
+ __OBJC_PROTOCOL_$_CRLayerPropertyService
+ __OBJC_PROTOCOL_$_CRWallpaperData
+ __OBJC_PROTOCOL_REFERENCE_$_CARThemeAssetLibraryObserving
+ __OBJC_PROTOCOL_REFERENCE_$_CARThemeAssetLibraryService
+ __OBJC_PROTOCOL_REFERENCE_$_CARThemeAssetLibraryServiceObserving
+ __OBJC_PROTOCOL_REFERENCE_$_CRLayerPropertyService
+ ___24-[CARSession suggestUI:]_block_invoke.402
+ ___34+[CARPrototypePref force3xCluster]_block_invoke
+ ___34+[CARPrototypePref force3xCluster]_block_invoke_2
+ ___34-[CARThemeAssetLibrary invalidate]_block_invoke
+ ___36-[CARThemeAssetLibrary addObserver:]_block_invoke
+ ___39-[CARThemeAssetLibrary removeObserver:]_block_invoke
+ ___40-[CARThemeAssetLibrary initWithVehicle:]_block_invoke
+ ___41-[CRFeatureAvailability isCarPlayAllowed]_block_invoke
+ ___41-[CRFeatureAvailability isCarPlayAllowed]_block_invoke.15
+ ___41-[CRFeatureAvailability isCarPlayAllowed]_block_invoke.15.cold.1
+ ___41-[CRFeatureAvailability isCarPlayAllowed]_block_invoke_2
+ ___43-[CARLayerPropertyMarshal _setupConnection]_block_invoke
+ ___43-[CARLayerPropertyMarshal _setupConnection]_block_invoke_2
+ ___44-[CARThemeAssetLibrary _queue_stopObserving]_block_invoke
+ ___44-[CARThemeAssetLibrary _queue_stopObserving]_block_invoke.94
+ ___44-[CARThemeAssetLibrary _queue_stopObserving]_block_invoke.cold.1
+ ___45-[CARThemeAssetLibrary _queue_startObserving]_block_invoke
+ ___45-[CARThemeAssetLibrary _queue_startObserving]_block_invoke.89
+ ___45-[CARThemeAssetLibrary _queue_startObserving]_block_invoke.cold.1
+ ___45-[CARWirelessPairingSession _setupConnection]_block_invoke.72.cold.1
+ ___45-[CARWirelessPairingSession _setupConnection]_block_invoke.73
+ ___46-[CARActiveNavigationIdentifiersObserver init]_block_invoke.53
+ ___47-[CARThemeAssetLibrary _setupServiceConnection]_block_invoke
+ ___47-[CARThemeAssetLibrary _setupServiceConnection]_block_invoke.75
+ ___47-[CARThemeAssetLibrary _setupServiceConnection]_block_invoke.cold.1
+ ___47-[CARThemeAssetLibrary _setupServiceConnection]_block_invoke_2
+ ___47-[CARThemeAssetLibrary _setupServiceConnection]_block_invoke_2.cold.1
+ ___50-[CARThemeAssetLibrary _queue_applyOverrideAsset:]_block_invoke
+ ___50-[CARThemeAssetLibrary _queue_applyOverrideAsset:]_block_invoke.84
+ ___50-[CARThemeAssetLibrary _queue_applyOverrideAsset:]_block_invoke.cold.1
+ ___52-[CARThemeAssetLibraryAgent _performObserverAction:]_block_invoke
+ ___52-[CARThemeAssetLibraryAgent _performObserverAction:]_block_invoke.cold.1
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.340
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke_2
+ ___55-[CARThemeAssetLibrary findCurrentAssetWithCompletion:]_block_invoke
+ ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke
+ ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke.18
+ ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke.18.cold.1
+ ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke_2
+ ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke_2.cold.1
+ ___56-[CARSessionChannel sendChannelMessage:withDescription:]_block_invoke
+ ___56-[CARSessionChannel sendChannelMessage:withDescription:]_block_invoke.cold.1
+ ___56-[CARSessionChannel sendChannelMessage:withDescription:]_block_invoke.cold.2
+ ___56-[CARSessionChannel sendChannelMessage:withDescription:]_block_invoke.cold.3
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.229
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.229.cold.1
+ ___60-[CARThemeAssetLibraryAgent notifyCompletedDownloadOfAsset:]_block_invoke
+ ___60-[CARThemeAssetLibraryAgent notifyCompletedDownloadOfAsset:]_block_invoke_2
+ ___60-[CRFeatureAvailability supportedCarPlayFeaturesForSession:]_block_invoke
+ ___60-[CRFeatureAvailability supportedCarPlayFeaturesForSession:]_block_invoke.25
+ ___60-[CRFeatureAvailability supportedCarPlayFeaturesForSession:]_block_invoke.25.cold.1
+ ___60-[CRFeatureAvailability supportedCarPlayFeaturesForSession:]_block_invoke_2
+ ___60-[CRFeatureAvailability supportedCarPlayFeaturesForSession:]_block_invoke_2.cold.1
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.230
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.230.cold.1
+ ___62+[CARThemeAssetOverrider postAssetErrorNotification:forAsset:]_block_invoke
+ ___62-[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]_block_invoke
+ ___62-[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]_block_invoke.77
+ ___62-[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]_block_invoke_2
+ ___62-[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]_block_invoke_2.78
+ ___62-[CARThemeAssetLibrary _queue_findCurrentAssetWithCompletion:]_block_invoke_2.cold.1
+ ___64-[CARThemeAssetLibraryAgent listener:shouldAcceptNewConnection:]_block_invoke
+ ___70-[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]_block_invoke
+ ___70-[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]_block_invoke.21
+ ___70-[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]_block_invoke.21.cold.1
+ ___70-[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]_block_invoke_2
+ ___70-[CRFeatureAvailability disablesCarPlayFeatures:forVehicleIdentifier:]_block_invoke_2.cold.1
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.28
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke.28.cold.1
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke_2
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke_2.cold.1
+ ___70-[CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier:]_block_invoke_2.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.566
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.566.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.566.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.570
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.574
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_3
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_4
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_5
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_6
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_7
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_7.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_7.cold.2
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke.24
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke.24.cold.1
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke_2
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke_2.cold.1
+ ___74-[CRFeatureAvailability setCarPlayFeatures:disabled:forVehicleIdentifier:]_block_invoke_2.cold.2
+ ___77-[CARThemeAssetLibraryObserverProxy service_completedDownloadForAsset:reply:]_block_invoke
+ ___80-[CARThemeAssetLibraryAgent notifyAttemptingDownloadForAssetIdentifier:version:]_block_invoke
+ ___80-[CARThemeAssetLibraryAgent notifyAttemptingDownloadForAssetIdentifier:version:]_block_invoke_2
+ ___82-[CARThemeAssetLibraryAgent notifyFailedDownloadForAssetIdentifier:version:error:]_block_invoke
+ ___82-[CARThemeAssetLibraryAgent notifyFailedDownloadForAssetIdentifier:version:error:]_block_invoke_2
+ ___83-[CARThemeAssetLibraryAgent notifyDidUpdateFromAsset:toAsset:forVehicleIdentifier:]_block_invoke
+ ___83-[CARThemeAssetLibraryAgent notifyDidUpdateFromAsset:toAsset:forVehicleIdentifier:]_block_invoke_2
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.31
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke.31.cold.1
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke_2
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke_2.cold.1
+ ___86-[CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:]_block_invoke_2.cold.2
+ ___96-[CARThemeAssetLibraryObserverProxy service_attemptingDownloadForAssetIdentifier:version:reply:]_block_invoke
+ ___98-[CARThemeAssetLibraryObserverProxy service_failedDownloadForAssetIdentifier:version:error:reply:]_block_invoke
+ ___99-[CARThemeAssetLibraryObserverProxy service_didUpdateFromAsset:toAsset:forVehicleIdentifier:reply:]_block_invoke
+ ___CARHandleSuggestUI_block_invoke.397
+ ___CRCollectCarPlayDiagnostics_block_invoke.122
+ ___CRConnectBluetoothLE_block_invoke
+ ___CRConnectBluetoothLE_block_invoke_2
+ ___CRConnectBluetoothLE_block_invoke_3
+ ___CRConnectBluetoothLE_block_invoke_3.cold.1
+ ___CRHandleBluetoothClassicPairingCompleted_block_invoke
+ ___CRHandleBluetoothClassicPairingCompleted_block_invoke_2
+ ___CRHandleBluetoothClassicPairingCompleted_block_invoke_3
+ ___CRHandleBluetoothClassicPairingCompleted_block_invoke_3.cold.1
+ ___CRHandleCarPlayConnectionRequest_block_invoke.51
+ ___CRHandleCarPlayConnectionRequest_block_invoke.51.cold.1
+ ___CRPostBannerToPhone_block_invoke.114
+ ___CRPresentBluetoothClassicPairingConfirmation_block_invoke
+ ___CRPresentBluetoothClassicPairingConfirmation_block_invoke_2
+ ___CRPresentBluetoothClassicPairingConfirmation_block_invoke_3
+ ___CRPresentBluetoothClassicPairingConfirmation_block_invoke_3.cold.1
+ ___CRPresentBluetoothClassicPairingError_block_invoke
+ ___CRPresentBluetoothClassicPairingError_block_invoke_2
+ ___CRPresentBluetoothClassicPairingError_block_invoke_3
+ ___CRPresentBluetoothClassicPairingError_block_invoke_3.cold.1
+ ___CRPresentCarPlayOnlyBluetoothClassicPairingConfirmation_block_invoke
+ ___CRPresentCarPlayOnlyBluetoothClassicPairingConfirmation_block_invoke_2
+ ___CRPresentCarPlayOnlyBluetoothClassicPairingConfirmation_block_invoke_3
+ ___CRPresentCarPlayOnlyBluetoothClassicPairingConfirmation_block_invoke_3.cold.1
+ ___CarThemeAssetsLogging_block_invoke
+ ___block_descriptor_32_e24_B16?0"CARDisplayInfo"8l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32r_e30_v24?0"NSNumber"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"<CARThemeAssetLibraryServiceObserving>"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32r_e30_v24?0"NSNumber"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v16?0"CARThemeAsset"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e48_v16?0"<CARThemeAssetLibraryServiceObserving>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_56_e8_32s40r_e27_v16?0"<CRCarKitService>"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e48_v16?0"<CARThemeAssetLibraryServiceObserving>"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40r_e27_v16?0"<CRCarKitService>"8ls32l8r40l8
+ ___block_descriptor_57_e8_32s40s48bs_e36_v24?0"<CRCarKitService>"8?<v?>16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e36_v24?0"<CRCarKitService>"8?<v?>16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.121
+ ___block_literal_global.138
+ ___block_literal_global.192
+ ___block_literal_global.20
+ ___block_literal_global.203
+ ___block_literal_global.27
+ ___block_literal_global.270
+ ___block_literal_global.30
+ ___block_literal_global.304
+ ___block_literal_global.307
+ ___block_literal_global.396
+ ___block_literal_global.407
+ ___block_literal_global.53
+ ___block_literal_global.56
+ ___block_literal_global.579
+ ___block_literal_global.588
+ ___block_literal_global.62
+ ___block_literal_global.692
+ ___block_literal_global.76
+ ___block_literal_global.79
+ ___block_literal_global.81
+ ___block_literal_global.86
+ ___block_literal_global.91
+ ___block_literal_global.93
+ __unnamed_array_storage
+ _dispatch_assert_queue$V2
+ _force3xCluster._force3xCluster
+ _force3xCluster.onceToken
+ _kCFBundleVersionKey
+ _kFigEndpointRemoteControlSessionCreationOption_QualityOfService
+ _kFigEndpointRemoteControlSessionCreationOption_SendMessageAsIs
+ _kFigEndpointRemoteControlSessionCreationOption_SendMessageWithoutReply
+ _kFigEndpointRemoteControlSessionCreationOption_StreamPriority
+ _objc_msgSend$SDKVersion
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$URLsForDirectory:inDomains:
+ _objc_msgSend$_addConnection:
+ _objc_msgSend$_assetURLForAssetIdentifier:version:
+ _objc_msgSend$_carplayLibraryDirectoryForAssetIdentifier:
+ _objc_msgSend$_carplayLibraryURL
+ _objc_msgSend$_contentVersionOfAsset:
+ _objc_msgSend$_generatedAssetForSourceAssetURL:assetIdentifier:version:
+ _objc_msgSend$_overrideAssetSourceURLForAssetIdentifier:
+ _objc_msgSend$_performObserverAction:
+ _objc_msgSend$_queue_applyOverrideAsset:
+ _objc_msgSend$_queue_findCurrentAssetWithCompletion:
+ _objc_msgSend$_queue_startObserving
+ _objc_msgSend$_queue_stopObserving
+ _objc_msgSend$_removeConnection:
+ _objc_msgSend$_setupServiceConnection
+ _objc_msgSend$_shouldForceUpdateAsset
+ _objc_msgSend$archiveDirectory:toLocation:
+ _objc_msgSend$asDictionary
+ _objc_msgSend$assetIdentifier
+ _objc_msgSend$assetLibrary
+ _objc_msgSend$baseURL
+ _objc_msgSend$clusterAssetIdentifier
+ _objc_msgSend$clusterAssetURL
+ _objc_msgSend$clusterAssetVersion
+ _objc_msgSend$colorFilterPreference
+ _objc_msgSend$compare:
+ _objc_msgSend$connectWithBluetoothLEIdentifier:name:preApproved:reply:
+ _objc_msgSend$connections
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$coreAccessoriesPrimaryUUID
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentLayoutID
+ _objc_msgSend$currentWallpaper
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:
+ _objc_msgSend$declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:bundlePath:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:
+ _objc_msgSend$deviceSupportedCarPlayFeaturesWithReply:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$disabledFeaturesPreference
+ _objc_msgSend$disablesCarPlayFeatures:forVehicleIdentifier:reply:
+ _objc_msgSend$displayID
+ _objc_msgSend$displayThemeData
+ _objc_msgSend$entitlements
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$finishedWelcome
+ _objc_msgSend$force3xCluster
+ _objc_msgSend$handleBluetoothClassicPairingCompletedForDeviceAddress:name:preApproved:reply:
+ _objc_msgSend$hasGaugeClusterScreen
+ _objc_msgSend$hasObservers
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithFigEndpoint:sessionStatusOptions:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:version:baseURL:
+ _objc_msgSend$initWithSessionStatusOptions:propertySupplier:
+ _objc_msgSend$initWithWallpaperIdentifier:displayID:layoutID:
+ _objc_msgSend$isCarPlayThemeSupportEnabled
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isEqualToThemeAsset:
+ _objc_msgSend$isReadableFileAtPath:
+ _objc_msgSend$isSiriBargeInDisabled
+ _objc_msgSend$layoutID
+ _objc_msgSend$libraryAgent:receivedOverrideAsset:forVehicleIdentifier:
+ _objc_msgSend$libraryAgent:requestsCurrentAssetForVehicleIdentifier:completion:
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$observerProxy
+ _objc_msgSend$overrideAssetForIdentifer:greaterThanVersion:
+ _objc_msgSend$paletteIDForLayout
+ _objc_msgSend$postAssetErrorNotification:forAsset:
+ _objc_msgSend$presentBluetoothClassicPairingConfirmationForDeviceAddress:name:numericComparisonCode:showBluetoothOnlyOption:reply:
+ _objc_msgSend$presentBluetoothClassicPairingErrorForDeviceAddress:name:isTimeout:reply:
+ _objc_msgSend$queue
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$sendChannelMessage:withDescription:
+ _objc_msgSend$sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:
+ _objc_msgSend$serviceName
+ _objc_msgSend$service_applyOverrideAsset:forVehicleIdentifier:reply:
+ _objc_msgSend$service_attemptingDownloadForAssetIdentifier:version:reply:
+ _objc_msgSend$service_completedDownloadForAsset:reply:
+ _objc_msgSend$service_currentAssetForVehicleIdentifier:reply:
+ _objc_msgSend$service_didUpdateFromAsset:toAsset:forVehicleIdentifier:reply:
+ _objc_msgSend$service_failedDownloadForAssetIdentifier:version:error:reply:
+ _objc_msgSend$service_startObservingWithReply:
+ _objc_msgSend$service_stopObservingWithReply:
+ _objc_msgSend$sessionStatusOptions
+ _objc_msgSend$setAssetLibrary:
+ _objc_msgSend$setCarPlayFeatures:disabled:forVehicleIdentifier:reply:
+ _objc_msgSend$setClusterAssetIdentifier:
+ _objc_msgSend$setClusterAssetURL:
+ _objc_msgSend$setClusterAssetVersion:
+ _objc_msgSend$setColorFilterPreference:
+ _objc_msgSend$setConnections:
+ _objc_msgSend$setDisabledFeaturesPreference:
+ _objc_msgSend$setDisplayThemeData:
+ _objc_msgSend$setFinishedWelcome:
+ _objc_msgSend$setHasGaugeClusterScreen:
+ _objc_msgSend$setPreviousSystemWallpaperData:
+ _objc_msgSend$setSDKVersion:
+ _objc_msgSend$setSiriBargeInDisabled:
+ _objc_msgSend$setStagedClusterAssetURL:
+ _objc_msgSend$setStagedClusterAssetVersion:
+ _objc_msgSend$setSupportsBluetoothLE:
+ _objc_msgSend$setSupportsMixableAudio:
+ _objc_msgSend$setSupportsThemeAssets:
+ _objc_msgSend$setSystemWallpaperData:
+ _objc_msgSend$stagedClusterAssetURL
+ _objc_msgSend$stagedClusterAssetVersion
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$supportedCarPlayFeaturesForCertificateSerial:reply:
+ _objc_msgSend$supportedCarPlayFeaturesForVehicleIdentifier:reply:
+ _objc_msgSend$supportsAdditionalContent
+ _objc_msgSend$supportsBluetoothLE
+ _objc_msgSend$supportsDDPContent
+ _objc_msgSend$supportsMixableAudio
+ _objc_msgSend$supportsThemeAssets
+ _objc_msgSend$systemWallpaperData
+ _objc_msgSend$themeAssetLibrary:attemptingDownloadForAssetVersion:
+ _objc_msgSend$themeAssetLibrary:completedDownloadOfAsset:
+ _objc_msgSend$themeAssetLibrary:didUpdateFromAsset:toAsset:
+ _objc_msgSend$themeAssetLibrary:failedDownloadForAssetVersion:error:
+ _objc_msgSend$themeDataWithCurrentWallpaper:
+ _objc_msgSend$unarchive:toLocation:
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$vehicleIdentifier
+ _objc_msgSend$vehicleInformation
+ _objc_msgSend$wallpaperForLayout
+ _objc_msgSend$wallpaperID
+ _objc_retainAutoreleasedReturnValue
+ _os_transaction_create
- +[CARPrototypePref force2xCluster]
- -[CARConnectionEvent transportType]
- -[CARConnectionSession initWithEvents:sessionIdentifier:transportType:]
- -[CARSession clientIsCarPlayShell]
- -[CARSession initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:]
- -[CARSession requiresCarCapabilitiesValues]
- -[CARSession saveInfoResponse]
- -[CARSession setRequiresCarCapabilitiesValues:]
- -[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]
- -[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:].cold.1
- -[CARSessionStatus clientIsCarPlayShell]
- -[CARSessionStatus saveInfoResponse]
- -[CRVehicleAccessory sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:]
- GCC_except_table114
- GCC_except_table136
- GCC_except_table159
- GCC_except_table165
- GCC_except_table192
- GCC_except_table27
- GCC_except_table54
- GCC_except_table62
- GCC_except_table78
- GCC_except_table89
- GCC_except_table95
- _CAREventTransport
- _CARSignpostLogForCategory.logObjects.0
- _CRDeviceSupportsCarPlayVehicleData.onceToken
- _CRDeviceSupportsCarPlayVehicleData.supportsVehicleData
- _OBJC_IVAR_$_CARConnectionEvent._transportType
- _OBJC_IVAR_$_CARSession._clientIsCarPlayShell
- _OBJC_IVAR_$_CARSession._requiresCarCapabilitiesValues
- _OBJC_IVAR_$_CARSession._saveInfoResponse
- _OBJC_IVAR_$_CARSessionStatus._clientIsCarPlayShell
- _OBJC_IVAR_$_CARSessionStatus._saveInfoResponse
- ___24-[CARSession suggestUI:]_block_invoke.410
- ___34+[CARPrototypePref force2xCluster]_block_invoke
- ___34+[CARPrototypePref force2xCluster]_block_invoke_2
- ___40-[CARSessionChannel sendChannelMessage:]_block_invoke
- ___40-[CARSessionChannel sendChannelMessage:]_block_invoke.cold.1
- ___40-[CARSessionChannel sendChannelMessage:]_block_invoke.cold.2
- ___45-[CARWirelessPairingSession _setupConnection]_block_invoke.71
- ___45-[CARWirelessPairingSession _setupConnection]_block_invoke.71.cold.1
- ___46-[CARActiveNavigationIdentifiersObserver init]_block_invoke.52
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.222
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.222.cold.1
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.223
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.223.cold.1
- ___72-[CARSession initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:]_block_invoke
- ___72-[CARSession initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:]_block_invoke.339
- ___72-[CARSession initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:]_block_invoke_2
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.526
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.526.cold.1
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.526.cold.2
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.530
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.534
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.cold.1
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke.cold.2
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_2
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_3
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_4
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_5
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_6
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_6.cold.1
- ___81-[CARSessionConfiguration initForCarPlayShell:saveInfoResponse:propertySupplier:]_block_invoke_6.cold.2
- ___CARHandleSuggestUI_block_invoke.405
- ___CRCollectCarPlayDiagnostics_block_invoke.102
- ___CRDeviceSupportsCarPlayVehicleData_block_invoke
- ___CRHandleCarPlayConnectionRequest_block_invoke.50
- ___CRHandleCarPlayConnectionRequest_block_invoke.50.cold.1
- ___CRPostBannerToPhone_block_invoke.94
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_literal_global.115
- ___block_literal_global.178
- ___block_literal_global.218
- ___block_literal_global.227
- ___block_literal_global.286
- ___block_literal_global.404
- ___block_literal_global.415
- ___block_literal_global.52
- ___block_literal_global.55
- ___block_literal_global.604
- ___block_literal_global.61
- ___block_literal_global.709
- ___block_literal_global.78
- ___block_literal_global.80
- _force2xCluster._force2xCluster
- _force2xCluster.onceToken
- _kCRRequiresFeatureFlagsEntitlement
- _objc_msgSend$arrayForKey:
- _objc_msgSend$clientIsCarPlayShell
- _objc_msgSend$force2xCluster
- _objc_msgSend$initForCarPlayShell:saveInfoResponse:propertySupplier:
- _objc_msgSend$initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:
- _objc_msgSend$numberForKey:
- _objc_msgSend$requiresCarCapabilitiesValues
- _objc_msgSend$saveInfoResponse
- _objc_msgSend$sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:
- _objc_msgSend$setRequiresCarCapabilitiesValues:
CStrings:
+ "\x02\x12"
+ "\nDisplay: %@\n\t%@"
+ "\x13\x1b\x16\x11\x12"
+ "\x14"
+ "\x15\x11\x14"
+ "\"\x14\x13"
+ "%@"
+ "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ version: %@}, enhancedIntegration: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
+ "%@ [id: %@, version: %@, baseURL: %@]"
+ "%@ {currentLayoutID: %@ paletteIDForLayout: %@ wallpaperForLayout: %@}"
+ "%@ {identifier: %@, physicalSize: %@, pixelSize: %@, additionalContent: %@}"
+ "%@ {identifier: %@}"
+ "%@:%@:%@"
+ "-[CRDisplayThemeData currentPaletteID]"
+ "-[CRDisplayThemeData currentWallpaper]"
+ ":\x13\x113#\x13"
+ "=ب\xde=ؙ\xde "
+ "@\"<CARThemeAssetLibraryAgentDelegate>\""
+ "@\"CARThemeAssetLibrary\""
+ "@\"CARThemeAssetLibraryObserverProxy\""
+ "@\"MCProfileConnection\""
+ "@\"NSMutableSet\""
+ "@24@0:8@\"<BSXPCDecoding>\"16"
+ "@24@0:8@\"NSDictionary\"16"
+ "@32@0:8Q16@?24"
+ "@32@0:8^{OpaqueFigEndpoint=}16Q24"
+ "AlternateScreen"
+ "AlwaysUpdateAsset"
+ "Asset Identifier: %@\nAsset Version: %@\nSDK Version: %@\nAsset URL: %@\nStaged Asset Version: %@\nStaged Asset URL: %@\nAlways Update Asset preference: %@"
+ "Asset-%lu"
+ "Automaker Settings"
+ "B32@0:8@\"NSData\"16@\"NSString\"24"
+ "B32@0:8Q16@24"
+ "B36@0:8Q16B24@28"
+ "BSXPCSecureCoding"
+ "CAFAppLaunch"
+ "CAFCore"
+ "CAFData"
+ "CARBluetoothClassicDiscoverer handleBluetoothClassicPairingCompleted failed to call carkitd: %@"
+ "CARBluetoothClassicDiscoverer presentBluetoothClassicPairingConfirmation failed to call carkitd: %@"
+ "CARBluetoothClassicDiscoverer presentBluetoothClassicPairingError failed to call carkitd: %@"
+ "CARBluetoothLEDiscoverer pairBluetoothDevice failed to call carkitd: %@"
+ "CARCarKitVehicleInformationEvent"
+ "CARThemeAsset"
+ "CARThemeAssetLibrary"
+ "CARThemeAssetLibraryAgent"
+ "CARThemeAssetLibraryObserverProxy"
+ "CARThemeAssetLibraryObserving"
+ "CARThemeAssetLibraryService"
+ "CARThemeAssetLibraryServiceObserving"
+ "CARThemeAssetOverrider"
+ "CDS Asset Identifier is MISSING!\nError:\n%@"
+ "CDS Asset Identifier:\n%@ \nError:\n%@ "
+ "CRAssetWallpaperData"
+ "CRDisplayThemeData"
+ "CRDisplayThemeData.m"
+ "CRFeatureAvailability"
+ "CRFeatureAvailability deviceSupportedFeatures"
+ "CRFeatureAvailability disablesCarPlayFeatures: %{public}lu vehicleID: %@"
+ "CRFeatureAvailability fetchSupportedAirPlayFeaturesForVehicleIdentifier: %@"
+ "CRFeatureAvailability isCarPlayAllowed"
+ "CRFeatureAvailability setCarPlayFeaturesDisabled: %{public}lu vehicleID: %@"
+ "CRFeatureAvailability supportedAirPlayFeaturesForVehicleIdentifier: %@"
+ "CRFeatureAvailability supportedFeaturesForSession: %@"
+ "CRLayerPropertyService"
+ "CRSystemWallpaperData"
+ "CRWallpaperData"
+ "CarPlayApp"
+ "Certificate.chain.pem"
+ "Cluster.arc"
+ "Cluster.assets"
+ "Cluster.assets.sha256"
+ "Cluster.assets.zip"
+ "Connecting to CarKit theme asset library service"
+ "Connection %@ was not observing theme library"
+ "DDPManaged"
+ "DPManaged"
+ "DataProtocol"
+ "EnhancedSiri"
+ "Failed to get wallpaper, no display with id: %@"
+ "Failed to initialize wallpaper, %@, from data: %@"
+ "Failed to set wallpaper on display %@: %@"
+ "GaugeCluster"
+ "HEVC"
+ "Helpers"
+ "Incomplete/malformed vehicle data protocol info in INFO response."
+ "Info.plist"
+ "Invalid palette ID, expected string:dictionary, found: %@:%@"
+ "Invalid palette ID, expected strings, found: %@:%@"
+ "No assets found in asset folder %@"
+ "Paired Devices"
+ "PassengerDisplay"
+ "Posting Asset Error Message %@"
+ "RW5hYmxlRmVycml0ZQ=="
+ "Removing theme library connection %@"
+ "SDKVersion"
+ "Selected #wallpaper %{public}@ doesn't support dynamic appearance. Locking Appearance to Always Dark"
+ "Sending data on channel %{public}@: %{public}@, payloadCount: %llu"
+ "T@\"<CARThemeAssetLibraryAgentDelegate>\",W,N,V_delegate"
+ "T@\"<CRWallpaperData>\",R,N"
+ "T@\"CARObserverHashTable\",R,N,V_observers"
+ "T@\"CARThemeAssetLibrary\",W,N,V_assetLibrary"
+ "T@\"CARThemeAssetLibraryObserverProxy\",R,N,V_observerProxy"
+ "T@\"CRSystemWallpaperData\",&,N"
+ "T@\"MCProfileConnection\",&,N,V_profileConnection"
+ "T@\"NSDictionary\",&,N,V_digitalCarKeyInformation"
+ "T@\"NSDictionary\",C,N,V_displayThemeData"
+ "T@\"NSDictionary\",R,C,N,V_paletteIDForLayout"
+ "T@\"NSDictionary\",R,C,N,V_wallpaperForLayout"
+ "T@\"NSDictionary\",R,N,V_vehicleInformation"
+ "T@\"NSMutableSet\",&,N,V_connections"
+ "T@\"NSNumber\",&,N,V_clusterAssetVersion"
+ "T@\"NSNumber\",&,N,V_disabledFeaturesPreference"
+ "T@\"NSNumber\",&,N,V_finishedWelcome"
+ "T@\"NSNumber\",&,N,V_hasGaugeClusterScreen"
+ "T@\"NSNumber\",&,N,V_stagedClusterAssetVersion"
+ "T@\"NSNumber\",&,N,V_supportsThemeAssets"
+ "T@\"NSNumber\",R,N,V_version"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_SDKVersion"
+ "T@\"NSString\",C,N,V_clusterAssetIdentifier"
+ "T@\"NSString\",R,C,N,V_currentLayoutID"
+ "T@\"NSString\",R,C,N,V_displayID"
+ "T@\"NSString\",R,C,N,V_identifier"
+ "T@\"NSString\",R,C,N,V_layoutID"
+ "T@\"NSString\",R,C,N,V_wallpaperID"
+ "T@\"NSString\",R,N,V_assetIdentifier"
+ "T@\"NSString\",R,N,V_vehicleDataProtocolVersion"
+ "T@\"NSURL\",&,N,V_clusterAssetURL"
+ "T@\"NSURL\",&,N,V_stagedClusterAssetURL"
+ "T@\"NSURL\",R,N"
+ "T@\"NSURL\",R,N,V_baseURL"
+ "T@\"NSUUID\",R,N,V_vehicleIdentifier"
+ "T@\"NSXPCConnection\",R,N,V_serviceConnection"
+ "TB,N,GisSiriBargeInDisabled,V_siriBargeInDisabled"
+ "TB,N,V_supportsBluetoothLE"
+ "TB,N,V_supportsMixableAudio"
+ "TB,N,V_supportsThemeAssets"
+ "TB,R,N,V_hasGaugeClusterScreen"
+ "TB,R,N,V_supportsAdditionalContent"
+ "TB,R,N,V_supportsDDPContent"
+ "TB,R,N,V_supportsLogTransfer"
+ "TB,R,N,V_supportsVehicleData"
+ "TQ,N,V_payloadCount"
+ "TQ,R,N,V_sessionStatusOptions"
+ "TQ,R,N,V_vehicleDataPluginCount"
+ "Theme Customization"
+ "ThemeAssets"
+ "Tq,N,V_colorFilterPreference"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByAppendingPathExtension:"
+ "URLByStandardizingPath"
+ "URLsForDirectory:inDomains:"
+ "Unable to serialize wallpaper: %@"
+ "Unknown wallpaper for layout: %@. Wallpapers are available for layouts: %@"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "Wallpaper identifier: %@\nPrevious wallpaper identifier: %@"
+ "_SDKVersion"
+ "_addConnection:"
+ "_assetIdentifier"
+ "_assetLibrary"
+ "_assetURLForAssetIdentifier:version:"
+ "_baseURL"
+ "_carplayLibraryDirectoryForAssetIdentifier:"
+ "_carplayLibraryURL"
+ "_clusterAssetIdentifier"
+ "_clusterAssetURL"
+ "_clusterAssetVersion"
+ "_colorFilterPreference"
+ "_connections"
+ "_contentVersionOfAsset:"
+ "_currentAssetForVehicleIdentifier service asset %@"
+ "_currentAssetForVehicleIdentifier using asset %@"
+ "_currentLayoutID"
+ "_digitalCarKeyInformation"
+ "_disabledFeaturesPreference"
+ "_displayID"
+ "_displayThemeData"
+ "_finishedWelcome"
+ "_generatedAssetForSourceAssetURL:assetIdentifier:version:"
+ "_hasGaugeClusterScreen"
+ "_layoutID"
+ "_observerProxy"
+ "_overrideAssetSourceURLForAssetIdentifier:"
+ "_paletteIDForLayout"
+ "_payloadCount"
+ "_performObserverAction:"
+ "_profileConnection"
+ "_queue_applyOverrideAsset:"
+ "_queue_findCurrentAssetWithCompletion:"
+ "_queue_startObserving"
+ "_queue_stopObserving"
+ "_removeConnection:"
+ "_sessionStatusOptions"
+ "_setupServiceConnection"
+ "_shouldForceUpdateAsset"
+ "_siriBargeInDisabled"
+ "_stagedClusterAssetURL"
+ "_stagedClusterAssetVersion"
+ "_supportsAdditionalContent"
+ "_supportsBluetoothLE"
+ "_supportsDDPContent"
+ "_supportsLogTransfer"
+ "_supportsMixableAudio"
+ "_supportsThemeAssets"
+ "_supportsVehicleData"
+ "_vehicleDataPluginCount"
+ "_vehicleDataProtocolVersion"
+ "_vehicleIdentifier"
+ "_vehicleInformation"
+ "_wallpaperForLayout"
+ "_wallpaperID"
+ "additionalContent"
+ "all"
+ "altScreen"
+ "applied override asset"
+ "applying override asset: %@ for vehicleID: %@"
+ "asDictionary"
+ "asset in asset library: %@"
+ "assetDescription"
+ "assetIdentifier"
+ "assetLibrary"
+ "assetsArchiveURL"
+ "automakerSettings"
+ "baseURL"
+ "certificateData"
+ "checking for override asset"
+ "cluster asset is already the latest version: %{public}@"
+ "clusterAssetIdentifier"
+ "clusterAssetURL"
+ "clusterAssetVersion"
+ "colorFilterPreference"
+ "com.apple.caraccessoryframework"
+ "com.apple.carkit.layer-metadata"
+ "com.apple.carkit.theme-asset-library"
+ "com.apple.carkit.theme_asset_library"
+ "com.apple.carkitd.theme-asset-library-observing"
+ "com.apple.private.carkit.themeAssetLibrary"
+ "compare:"
+ "connectWithBluetoothLEIdentifier:name:preApproved:reply:"
+ "connections"
+ "copyItemAtURL:toURL:error:"
+ "coreAccessoriesEndpointUUID"
+ "coreAccessoriesPrimaryUUID"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "currentConnection"
+ "currentLayoutID"
+ "currentPaletteID"
+ "currentWallpaper"
+ "data"
+ "dataWithContentsOfURL:options:error:"
+ "dd/MM HH:mm:ss"
+ "declarationForAppRecord:"
+ "declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:"
+ "declarationForBundleIdentifier:infoPropertyList:entitlementsPropertyList:bundlePath:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "deviceSupportedCarPlayFeatures"
+ "deviceSupportedCarPlayFeaturesWithReply:"
+ "deviceSupportedFeatures %{public}lu"
+ "deviceSupportedFeatures call failed: %{public}@"
+ "dictionaryWithContentsOfURL:error:"
+ "did notify theme asset observer %@ of attempting download for identifier: %@ version: %@"
+ "did notify theme asset observer %@ of completed download for asset: %@"
+ "did notify theme asset observer %@ of failed download for identifier: %@ version: %@"
+ "did notify theme asset observer %@ of update from asset %@ to asset %@ for vehicleID: %@"
+ "digitalCarKeyInformation"
+ "disabledFeaturesPreference"
+ "disablesCarPlayFeatures %{public}lu: %@"
+ "disablesCarPlayFeatures call failed: %{public}@"
+ "disablesCarPlayFeatures:forVehicleIdentifier:"
+ "disablesCarPlayFeatures:forVehicleIdentifier:reply:"
+ "displayID"
+ "displayIdentifier"
+ "displayThemeData"
+ "encodeWithBSXPCCoder:"
+ "enhancedSiri"
+ "entitlements"
+ "error reading certificate from asset: %@"
+ "error reading signature from asset: %@"
+ "failed to connect to theme asset library service %@"
+ "failed to connect to theme library observer service %@"
+ "failed to copy %@ to %@, error: %@"
+ "failed to copy %@ to %@: %@"
+ "failed to create %@"
+ "failed to create %@: %@"
+ "failed to message CARThemeAssetLibraryService: %@"
+ "failed to prepare override asset"
+ "failed to read %@: %@"
+ "failed to remove override archive %@: %@"
+ "failed to reset asset directory %@: %@"
+ "failed to unarchive override archive %@"
+ "fetchDockAppInCategory:completion:"
+ "fetchSupportedAirPlayFeaturesForVehicleIdentifier:completion:"
+ "fileExistsAtPath:"
+ "fileExistsAtPath:isDirectory:"
+ "fileTransfer"
+ "findCurrentAsset vehicleID: %@ assetID: %@"
+ "findCurrentAssetWithCompletion:"
+ "finishedWelcome"
+ "focusTransfer"
+ "force updating asset version to %{public}@"
+ "force3xCluster"
+ "h.264Level5.1"
+ "handleBluetoothClassicPairingCompletedForDeviceAddress:name:preApproved:reply:"
+ "hasGaugeClusterScreen"
+ "hasPrefix:"
+ "hevc"
+ "holding a theme library observing transaction for %@"
+ "infoDictionary"
+ "initWithBSXPCCoder:"
+ "initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:"
+ "initWithData:encoding:"
+ "initWithEvents:sessionIdentifier:vehicleInformation:"
+ "initWithFigEndpoint:sessionStatusOptions:"
+ "initWithFormat:"
+ "initWithIdentifier:"
+ "initWithIdentifier:version:baseURL:"
+ "initWithSessionStatusOptions:propertySupplier:"
+ "initWithVehicle:"
+ "initWithWallpaperIdentifier:displayID:layoutID:"
+ "interrupted connection to CARThemeAssetService"
+ "invalid asset identifier %@"
+ "invalidated connection to CARThemeAssetService"
+ "isCarPlayAllowed call failed: %{public}@"
+ "isCarPlayAllowed: %{public}@"
+ "isCarPlayThemeSupportEnabled"
+ "isEqualToNumber:"
+ "isEqualToThemeAsset:"
+ "isReadableFileAtPath:"
+ "isSiriBargeInDisabled"
+ "kForce3xCluster"
+ "layoutID"
+ "layoutIdentifier"
+ "layoutURL"
+ "libraryAgent:receivedOverrideAsset:forVehicleIdentifier:"
+ "libraryAgent:requestsCurrentAssetForVehicleIdentifier:completion:"
+ "logTransfer"
+ "logTransferInfo"
+ "mainBuffered"
+ "nil"
+ "no asset source for %@"
+ "no asset version in %@"
+ "no clusterAssetIdentifier for vehicle %@"
+ "none"
+ "notifiying theme asset observers of attempting download for identifier: %@ version: %@"
+ "notifiying theme asset observers of completed download for asset: %@"
+ "notifiying theme asset observers of failed download for identifier: %@ version: %@"
+ "notifiying theme asset observers of update from asset %@ to asset: %@ for vehicleID: %@"
+ "notifyAttemptingDownloadForAssetIdentifier:version:"
+ "notifyCompletedDownloadOfAsset:"
+ "notifyDidUpdateFromAsset:toAsset:forVehicleIdentifier:"
+ "notifyFailedDownloadForAssetIdentifier:version:error:"
+ "objectForKey:ofClass:"
+ "observerProxy"
+ "oemIcon"
+ "oemIconLabel"
+ "oemIcons"
+ "overrideAssetForIdentifer:greaterThanVersion:"
+ "pairedDevices"
+ "paletteID"
+ "paletteIDForLayout"
+ "payloadCount"
+ "pluginCount"
+ "postAssetErrorNotification:forAsset:"
+ "prepared override asset %@"
+ "preparing override asset version %{public}@"
+ "presentBluetoothClassicPairingConfirmationForDeviceAddress:name:numericComparisonCode:showBluetoothOnlyOption:reply:"
+ "presentBluetoothClassicPairingErrorForDeviceAddress:name:isTimeout:reply:"
+ "previousSystemWallpaperData"
+ "profileConnection"
+ "protocolVersion"
+ "queue"
+ "received attempting download for theme asset identifier: %@ version: %@"
+ "received completed download for theme asset %@"
+ "received didUpdateFromAsset: %@ toAsset: %@ forVehicleID: %@"
+ "received failed download for theme asset identifier: %@ version: %@ error: %@"
+ "receiving a service connection %@ to service %@ from %@"
+ "registerObserver:"
+ "releasing a theme library observing transaction for %@"
+ "removeItemAtURL:error:"
+ "removeObjectsForKeys:"
+ "requesting current asset for vehicleID: %@"
+ "sendChannelMessage:withDescription:"
+ "sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:"
+ "sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:"
+ "serviceName"
+ "service_applyOverrideAsset:forVehicleIdentifier:reply:"
+ "service_attemptingDownloadForAssetIdentifier:version:reply:"
+ "service_completedDownloadForAsset:reply:"
+ "service_currentAssetForVehicleIdentifier:reply:"
+ "service_didUpdateFromAsset:toAsset:forVehicleIdentifier:reply:"
+ "service_failedDownloadForAssetIdentifier:version:error:reply:"
+ "service_startObservingWithReply:"
+ "service_stopObservingWithReply:"
+ "sessionStatusOptions"
+ "setAssetLibrary:"
+ "setCarPlayFeatures:disabled:forVehicleIdentifier:"
+ "setCarPlayFeatures:disabled:forVehicleIdentifier:reply:"
+ "setCarPlayFeaturesDisabled call failed: %@"
+ "setCarPlayFeaturesDisabled succeeded"
+ "setClusterAssetIdentifier:"
+ "setClusterAssetURL:"
+ "setClusterAssetVersion:"
+ "setColorFilterPreference:"
+ "setConnections:"
+ "setDigitalCarKeyInformation:"
+ "setDisabledFeaturesPreference:"
+ "setDisplayThemeData:"
+ "setFinishedWelcome:"
+ "setHasGaugeClusterScreen:"
+ "setPayloadCount:"
+ "setPreviousSystemWallpaperData:"
+ "setProfileConnection:"
+ "setSDKVersion:"
+ "setSiriBargeInDisabled:"
+ "setStagedClusterAssetURL:"
+ "setStagedClusterAssetVersion:"
+ "setSupportsBluetoothLE:"
+ "setSupportsMixableAudio:"
+ "setSupportsThemeAssets:"
+ "setSystemWallpaperData:"
+ "setWallpaper:forDisplayWithID:requiresDarkAppearance:"
+ "signatureData"
+ "siriBargeInDisabled"
+ "stagedClusterAssetURL"
+ "stagedClusterAssetVersion"
+ "start observing theme library for connection: %@"
+ "started observing theme asset library"
+ "stop observing theme library for connection: %@"
+ "stopped observing theme asset library"
+ "stringByAppendingFormat:"
+ "supportedAirPlayFeaturesForVehicleIdentifier:"
+ "supportedAirPlayFeaturesForVehicleIdentifier: %{public}@"
+ "supportedCarPlayFeaturesForCertificateSerial:reply:"
+ "supportedCarPlayFeaturesForSession:"
+ "supportedCarPlayFeaturesForVehicleIdentifier call failed: %@"
+ "supportedCarPlayFeaturesForVehicleIdentifier: %{public}lu"
+ "supportedCarPlayFeaturesForVehicleIdentifier: call failed: %{public}@"
+ "supportedCarPlayFeaturesForVehicleIdentifier:reply:"
+ "supportedFeaturesForSession call failed: %@"
+ "supportedFeaturesForSession: %{public}lu"
+ "supportedFeaturesForSession: call failed: %{public}@"
+ "supportsAdditionalContent"
+ "supportsBSXPCSecureCoding"
+ "supportsBluetoothLE"
+ "supportsDDPContent"
+ "supportsLogTransfer"
+ "supportsMixableAudio"
+ "supportsThemeAssets"
+ "supportsVehicleData"
+ "systemWallpaperData"
+ "systemWallpaperIdentifier"
+ "theme asset library connection interrupted or invalidated; removing connection."
+ "themeAssetLibrary:attemptingDownloadForAssetVersion:"
+ "themeAssetLibrary:completedDownloadOfAsset:"
+ "themeAssetLibrary:didUpdateFromAsset:toAsset:"
+ "themeAssetLibrary:failedDownloadForAssetVersion:error:"
+ "themeCustomization"
+ "themeDataWithCurrentLayoutID:"
+ "themeDataWithCurrentPaletteID:"
+ "themeDataWithCurrentWallpaper:"
+ "uiContext"
+ "uiSync"
+ "unregisterObserver:"
+ "using override asset folder %@"
+ "using override zipped asset %@"
+ "v16@?0@\"<CARThemeAssetLibraryServiceObserving>\"8"
+ "v16@?0@\"CARThemeAsset\"8"
+ "v24@0:8@\"<BSXPCEncoding>\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v32@0:8@\"CARThemeAsset\"16@?<v@?>24"
+ "v32@0:8@\"CARThemeAssetLibrary\"16@\"CARThemeAsset\"24"
+ "v32@0:8@\"CARThemeAssetLibrary\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"CARThemeAsset\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v40@0:8@\"CARThemeAsset\"16@\"NSUUID\"24@?<v@?>32"
+ "v40@0:8@\"CARThemeAssetLibrary\"16@\"CARThemeAsset\"24@\"CARThemeAsset\"32"
+ "v40@0:8@\"CARThemeAssetLibrary\"16@\"NSNumber\"24@\"NSError\"32"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?>32"
+ "v40@0:8Q16@\"NSUUID\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?B@\"NSError\">36"
+ "v44@0:8@16@24B32@?36"
+ "v44@0:8Q16B24@\"NSUUID\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8Q16B24@28@?36"
+ "v48@0:8@\"CARThemeAsset\"16@\"CARThemeAsset\"24@\"NSUUID\"32@?<v@?>40"
+ "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSError\"32@?<v@?>40"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSNumber\"@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "v56@0:8@16@24@32@40@48"
+ "vehicle supports theme assets: %{public}@"
+ "vehicleDataPluginCount"
+ "vehicleDataProtocolVersion"
+ "vehicleIdentifier"
+ "vehicleInformation"
+ "vehicleStateProtocol"
+ "vehicleStateProtocolInfo"
+ "wallpaper"
+ "wallpaper identifier: "
+ "wallpaperDescription"
+ "wallpaperForDisplayWithID:"
+ "wallpaperForLayout"
+ "wallpaperID"
+ "zip"
+ "|"
+ "\xf0\xf1"
- "\x13\x11\x16\""
- "\x15\x11\x13"
- "$"
- "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, enhancedIntegration: %@, albumArtUserPreference: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
- "%@ {identifier: %@, physicalSize: %@, pixelSize: %@}"
- "*\x13\x112\x13\x13"
- "2\x17"
- "@32@0:8B16B20@?24"
- "@32@0:8^{OpaqueFigEndpoint=}16B24B28"
- "CARRequiresFeatureFlags"
- "DeviceSupportsCarPlay2"
- "HardwarePlatform"
- "TB,N,V_requiresCarCapabilitiesValues"
- "TB,R,N,V_clientIsCarPlayShell"
- "TB,R,N,V_saveInfoResponse"
- "_clientIsCarPlayShell"
- "_requiresCarCapabilitiesValues"
- "_saveInfoResponse"
- "arrayForKey:"
- "clientIsCarPlayShell"
- "force2xCluster"
- "initForCarPlayShell:saveInfoResponse:propertySupplier:"
- "initWithEvents:sessionIdentifier:transportType:"
- "initWithFigEndpoint:clientIsCarPlayShell:saveInfoResponse:"
- "kForce2xCluster"
- "numberForKey:"
- "requiresCarCapabilitiesValues"
- "s8000"
- "s8001"
- "s8003"
- "saveInfoResponse"
- "sendMessageWithoutReply"
- "sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:"
- "setRequiresCarCapabilitiesValues:"
- "t7000"
- "t8010"
- "t8011"
- "t8012"
- "\xf0\xc1"

```
