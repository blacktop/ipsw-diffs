# 17.5 (21F79) .vs 17.5.1 (21F90)

## IPSWs

- `iPhone16,1_17.5_21F79_Restore.ipsw`
- `iPhone16,1_17.5.1_21F90_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.5 *(21F79)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |
| 17.5.1 *(21F90)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |

### Kexts

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleDCP`

```diff

-590.120.28.0.2
+590.122.1.0.0
   __TEXT.__cstring: 0x12a3
   __TEXT.__const: 0x18
   __TEXT_EXEC.__text: 0x504c

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1400
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 264CB017-15A5-3820-8FC7-11726D42DE71
+  UUID: 8C088795-6151-3676-832B-C03020110DEE
   Functions: 103
   Symbols:   0
   CStrings:  89

```

</details>

## MachO

### ⬆️ Updated (72)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker](MACHOS/PhotoPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation](MACHOS/PhotosDestructiveChangeConfirmation.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider](MACHOS/PhotosFileProvider.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMemoriesNotificationUpdates.appex/PhotosMemoriesNotificationUpdates](MACHOS/PhotosMemoriesNotificationUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp](MACHOS/PhotosMessagesApp.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker](MACHOS/PhotosPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidgetIntents.appex/PhotosReliveWidgetIntents](MACHOS/PhotosReliveWidgetIntents.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosTCCNotificationExtension.appex/PhotosTCCNotificationExtension](MACHOS/PhotosTCCNotificationExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService](MACHOS/com.apple.social.StreamShareService.md)
- [/Applications/PhotosUIService.app/PhotosUIService](MACHOS/PhotosUIService.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/IDSAuthenticationDelegatePlugin.bundle/IDSAuthenticationDelegatePlugin](MACHOS/IDSAuthenticationDelegatePlugin.md)
- [/System/Library/Accounts/ServiceOwners/IDSServiceOwner.bundle/IDSServiceOwner](MACHOS/IDSServiceOwner.md)
- [/System/Library/CloudRecommendations/ClientSources/PhotosCloudRecommendations.bundle/PhotosCloudRecommendations](MACHOS/PhotosCloudRecommendations.md)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI.md)
- [/System/Library/DataClassMigrators/AirTrafficMigrator.migrator/AirTrafficMigrator](MACHOS/AirTrafficMigrator.md)
- [/System/Library/DataClassMigrators/MobileSlideShow.migrator/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/DigitalSeparation/SharingSources/PhotosSeparation.bundle/PhotosSeparation](MACHOS/PhotosSeparation.md)
- [/System/Library/DistributedEvaluation/Plugins/PhotosDESPlugin.desPlugin/PhotosDESPlugin](MACHOS/PhotosDESPlugin.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.FontPicker.appex/com.apple.UIKit.FontPicker](MACHOS/com.apple.UIKit.FontPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.TextFormatting.appex/com.apple.UIKit.TextFormatting](MACHOS/com.apple.UIKit.TextFormatting.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/MediaStreamPlugins/PhotoSharingPlugin.mediastream/PhotoSharingPlugin](MACHOS/PhotoSharingPlugin.md)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings.md)
- [/System/Library/PreferenceBundles/PhotosCustomNotifications.bundle/PhotosCustomNotifications](MACHOS/PhotosCustomNotifications.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PhotosStorageManagementSettings.bundle/PhotosStorageManagementSettings](MACHOS/PhotosStorageManagementSettings.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSCredentialsAgent.app/IDSCredentialsAgent](MACHOS/IDSCredentialsAgent.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSRemoteURLConnectionAgent.app/IDSRemoteURLConnectionAgent](MACHOS/IDSRemoteURLConnectionAgent.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PlugIns/PhotoAnalysisLighthousePlugin.appex/PhotoAnalysisLighthousePlugin](MACHOS/PhotoAnalysisLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/PhotosDiagnostics](MACHOS/PhotosDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI](MACHOS/AirDropAlertUI.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropNotice.appex/AirDropNotice](MACHOS/AirDropNotice.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/ContinuityRemote.appex/ContinuityRemote](MACHOS/ContinuityRemote.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/XPCServices/SharingXPCHelper.xpc/SharingXPCHelper](MACHOS/SharingXPCHelper.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/Artwork.bundle/Artwork](MACHOS/Artwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/BoundingPathData.bundle/BoundingPathData](MACHOS/BoundingPathData.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/SetupAssistantBundles/SBSyncServiceSetupAssistantBundle.bundle/SBSyncServiceSetupAssistantBundle](MACHOS/SBSyncServiceSetupAssistantBundle.md)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2.md)
- [/System/Library/SyncBundles/LogsPlugin.syncBundle/LogsPlugin](MACHOS/LogsPlugin.md)
- [/System/Library/SyncBundles/MobileSlideShow.syncBundle/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/SyncBundles/UserDataPlugin.syncBundle/UserDataPlugin](MACHOS/UserDataPlugin.md)
- [/System/Library/UserNotifications/Bundles/com.apple.identityservicesd.firewall.bundle/com.apple.identityservicesd.firewall](MACHOS/com.apple.identityservicesd.firewall.md)
- [/usr/libexec/atc](MACHOS/atc.md)
- [/usr/libexec/corebrightnessdiag](MACHOS/corebrightnessdiag.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)

</details>

## Firmware

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

   __OS_LOG.__string: 0x26799
   __MISC.__apf_list: 0xb0
   __CMA.__cma_log_string: 0x40da
-  UUID: 02059E09-6278-3AD4-AA56-A74D99AB3CF4
+  UUID: 4ED68705-3040-3F6E-A2E4-03EA52E4D370
   Functions: 4232
   Symbols:   0
   CStrings:  3622

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2b3074
+  __TEXT.__text: 0x2b3084
   __TEXT.__const: 0x7b21c
   __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160

   __DATA._rtk_mtab: 0x5b0
   __DATA.__zerofill: 0x9c868
   __OS_LOG.__string: 0x1ed47
-  UUID: 778822D5-3DB9-3B48-9185-154E7FB344AE
+  UUID: A6B13FFD-1613-3C8D-A3C9-222A5E57854A
   Functions: 6434
   Symbols:   0
   CStrings:  5771

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b3074
+  __TEXT.__text: 0x2b3084
   __TEXT.__const: 0x7b21c
   __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160

   __DATA._rtk_mtab: 0x5b0
   __DATA.__zerofill: 0x9c868
   __OS_LOG.__string: 0x1ed47
-  UUID: 40C4FA09-7F9A-3129-88C3-7CF35F87EB32
+  UUID: 9BB1907C-38D4-30CF-991A-80F4FC44EC21
   Functions: 6434
   Symbols:   0
   CStrings:  5771

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.5 *(21F79)* | 618.2.12.10.9 |
| 17.5.1 *(21F90)* | 618.2.12.10.9 |

### Dylibs

#### ⬆️ Updated (67)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/IDSAccountNotificationPlugin.bundle/IDSAccountNotificationPlugin](DYLIBS/IDSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin](DYLIBS/PhotosAccountNotificationPlugin.md)
- [/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator](DYLIBS/FaceTimeMigrator.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic](DYLIBS/AirTraffic.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/PrivateFrameworks/BagKit.framework/BagKit](DYLIBS/BagKit.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices](DYLIBS/CloudPhotoServices.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore.md)
- [/System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices](DYLIBS/FTClientServices.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence](DYLIBS/IDSHashPersistence.md)
- [/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore](DYLIBS/IDSKVStore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/PDS.framework/PDS](DYLIBS/PDS.md)
- [/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent](DYLIBS/PDSAgent.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlacesKit.framework/PlacesKit](DYLIBS/PlacesKit.md)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/usr/lib/swift/libswiftAssetsLibrary.dylib](DYLIBS/libswiftAssetsLibrary.dylib.md)
- [/usr/lib/swift/libswiftPhotos.dylib](DYLIBS/libswiftPhotos.dylib.md)
- [/usr/lib/swift/libswiftPhotosUI.dylib](DYLIBS/libswiftPhotosUI.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)

</details>

## EOF
