## RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0xda90
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x28e0
-  __TEXT.__objc_methlist: 0xfe0
-  __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0xf8a
-  __TEXT.__objc_methname: 0x3db8
+2422.0.15.0.2
+  __TEXT.__text: 0x10454
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x2c80
+  __TEXT.__objc_methlist: 0x1098
+  __TEXT.__gcc_except_tab: 0x424
+  __TEXT.__cstring: 0x125e
+  __TEXT.__objc_methname: 0x419a
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0x15c1
-  __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x1245
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x14c0
+  __TEXT.__objc_methtype: 0x165f
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0x15c7
+  __TEXT.__unwind_info: 0x2b0
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x12d0
-  __DATA.__objc_selrefs: 0x1040
-  __DATA.__objc_ivar: 0x98
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x13a0
+  __DATA.__objc_selrefs: 0x1140
+  __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /System/Library/PrivateFrameworks/SetupKit.framework/SetupKit
+  - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
+  - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BCD6249-4065-3AE6-8890-6A30848700D0
-  Functions: 211
-  Symbols:   1778
-  CStrings:  1227
+  UUID: 593F7268-2DD3-313D-B765-053550F62A7A
+  Functions: 241
+  Symbols:   1986
+  CStrings:  1348
 
Symbols:
+ -[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]
+ -[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]
+ -[RecoverDeviceUIExtensionRemoteViewController scanningCard]
+ -[RecoverDeviceUIExtensionRemoteViewController setScanningCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController setSfClient:]
+ -[RecoverDeviceUIExtensionRemoteViewController setSuCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController setSuSelectionCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController sfClient]
+ -[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]
+ -[RecoverDeviceUIExtensionRemoteViewController showSUSelectionCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController showScanningCard]
+ -[RecoverDeviceUIExtensionRemoteViewController suCard]
+ -[RecoverDeviceUIExtensionRemoteViewController suSelectionCard]
+ GCC_except_table3
+ GCC_except_table80
+ GCC_except_table87
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._scanningCard
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._sfClient
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._suCard
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._suSelectionCard
+ _MAPurgeAllWithPurpose
+ _MAPurgeCatalogsWithPurpose
+ _OBJC_CLASS_$_MAAsset
+ _OBJC_CLASS_$_MAAssetQuery
+ _OBJC_CLASS_$_MADownloadOptions
+ _OBJC_CLASS_$_MAMsuDownloadOptions
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_SFClient
+ _OBJC_CLASS_$_SUCoreDocumentation
+ __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.867
+ __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.674
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.732
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.733
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.734
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.791
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.793
+ __68-[RecoverDeviceUIExtensionRemoteViewController showSUSelectionCard:]_block_invoke.764
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.871
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.872
+ __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.480
+ __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.651
+ __80-[RecoverDeviceUIExtensionRemoteViewController configureWithContext:completion:]_block_invoke.454
+ __82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke.762
+ __82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke_2.763
+ __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.750
+ __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.752
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.772
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.783
+ ___64-[RecoverDeviceUIExtensionRemoteViewController showScanningCard]_block_invoke
+ ___64-[RecoverDeviceUIExtensionRemoteViewController showScanningCard]_block_invoke_2
+ ___66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke
+ ___68-[RecoverDeviceUIExtensionRemoteViewController showSUSelectionCard:]_block_invoke
+ ___81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke_2
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke_2
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke_3
+ ___92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke
+ ___block_descriptor_49_e8_32s40s_e19_v16?0"PRXAction"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0q8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e44_v28?0B8"NSError"12"SUCoreDocumentation"20lr56l8s32l8s40l8s48l8
+ __block_literal_global.869
+ _objc_msgSend$addKeyValuePair:with:
+ _objc_msgSend$cleanDocumentation
+ _objc_msgSend$collectDocumentation:alternative:completion:
+ _objc_msgSend$extendDocumentationProperties
+ _objc_msgSend$initWithDocumentationAsset:
+ _objc_msgSend$initWithType:andPurpose:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$popViewControllerAnimated:
+ _objc_msgSend$queryMetaData:
+ _objc_msgSend$results
+ _objc_msgSend$scanningCard
+ _objc_msgSend$setAdditionalServerParams:
+ _objc_msgSend$setDiscretionary:
+ _objc_msgSend$setLiveAssetAudienceUUID:
+ _objc_msgSend$setPurpose:
+ _objc_msgSend$setScanningCard:
+ _objc_msgSend$setSfClient:
+ _objc_msgSend$setSuCard:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$sfClient
+ _objc_msgSend$showSUCard:build:icon:isAlternate:
+ _objc_msgSend$showSUSelectionCard:
+ _objc_msgSend$showScanningCard
+ _objc_msgSend$softwareUpdateIconImage
+ _objc_msgSend$startCatalogDownload:options:completionWithError:
+ _objc_msgSend$startDownload:completionWithError:
+ _objc_msgSend$startProxCardTransactionWithOptions:completion:
+ _objc_msgSend$suCard
+ _objc_msgSend$suSelectionCard
- GCC_except_table63
- __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.762
- __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.614
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.686
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.688
- __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.766
- __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.767
- __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.432
- __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.591
- __81-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:resultType:]_block_invoke.660
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.667
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.678
- __block_literal_global.764
CStrings:
+ "@\"SFClient\""
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "CaptiveNetworkFailed"
+ "CaptiveNetworkIPAssignFailed"
+ "Cleaning up key for device %{public}@, which was added on: %{public}@"
+ "Device"
+ "Device %{public}@ found in recovered device ids (added on: %{public}@)"
+ "Device %{public}@ is not a recently recovered device. Recently recovered: %{public}@"
+ "DeviceName"
+ "Doc asset query found results:%{public}@"
+ "Failed to activate setupkit client: %{public}@"
+ "Failed to download documentation asset with result:%ld, error:%{public}@"
+ "Failed to download documentation catalog with result:%ld, error:%{public}@"
+ "Failed to find doc asset"
+ "Failed to purge alternate documentation catalog: %{public}@"
+ "Failed to purge alternate documentation: %{public}@"
+ "Failed to purge primary documentation catalog: %{public}@"
+ "Failed to purge primary documentation: %{public}@"
+ "Failed to query documentation catalog with result:%ld"
+ "ForceAuthTag default is set to %{public}@, but server have different auth tag %{public}@, ignoring"
+ "Got OSR message %{public}@"
+ "Got error from SetupKit: %{public}@"
+ "Ignoring user entered code %{public}@ due to flag"
+ "Keeping key for device %{public}@, which was added on: %{public}@"
+ "NeRDOOBCommandSelectSU"
+ "NeRDRecoveryDisabled"
+ "NeRDSUInfoBuild"
+ "NeRDSUInfoDoc"
+ "NeRDSUInfoDocAssetType"
+ "NeRDSUInfoDocAssetUUID"
+ "NeRDSUInfoDocDeviceClass"
+ "NeRDSUInfoDocDocumentationID"
+ "NeRDSUInfoVersion"
+ "NeRDStateUpdateFound"
+ "NeRDSupportsSlowRoll"
+ "NeRDUpdateFound"
+ "OSVersion"
+ "Overall status is %{public}@, type:%d, err:%{public}@"
+ "PROGRESS_CARD_TITLE_VERSION"
+ "Persisting recovered device: %{public}@ with current time: %{public}@"
+ "RecoverDeviceUI successfully initialized. Identifier is %{public}@"
+ "RecoverDeviceUI-alternate"
+ "RecoverDeviceUI-primary"
+ "Remote device sent config: %{public}@"
+ "Remote device setup complete, waiting for scan results"
+ "SCANNING_CARD_DETAILS"
+ "SCANNING_CARD_SCANNING"
+ "SCANNING_CARD_TITLE"
+ "SUDocumentationID"
+ "SU_CARD_DETAILS"
+ "SU_CARD_TITLE"
+ "SetupKitEventHandler invoked for event : %d (%{public}@)"
+ "Sharing client allow us to proceed"
+ "Sharing client does not allow us to proceed"
+ "Starting to show progress"
+ "Subtitle is: %{public}@"
+ "T@\"PRXCardContentViewController\",&,N,V_scanningCard"
+ "T@\"PRXCardContentViewController\",&,N,V_suCard"
+ "T@\"PRXCardContentViewController\",&,N,V_suSelectionCard"
+ "T@\"SFClient\",&,N,V_sfClient"
+ "Unhandled event %d (%{public}@) received by setupKitEventHandler"
+ "Unknown state (%{public}@)!  file a bug"
+ "User entered code %{public}@, attempt # %llu"
+ "_scanningCard"
+ "_sfClient"
+ "_suCard"
+ "_suSelectionCard"
+ "addKeyValuePair:with:"
+ "cleanDocumentation"
+ "collectDocumentation:alternative:completion:"
+ "com.apple.MobileAsset.SoftwareUpdateDocumentation"
+ "com.apple.MobileAsset.WatchSoftwareUpdateDocumentation"
+ "extendDocumentationProperties"
+ "initWithDocumentationAsset:"
+ "initWithType:andPurpose:"
+ "kNeRDSelectedSU"
+ "numberWithInt:"
+ "popViewControllerAnimated:"
+ "preferredWindowingControlStyleForScene:"
+ "queryMetaData:"
+ "recovery button pressed, waiting for scan results"
+ "results"
+ "scanningCard"
+ "setAdditionalServerParams:"
+ "setDiscretionary:"
+ "setLiveAssetAudienceUUID:"
+ "setPurpose:"
+ "setScanningCard:"
+ "setSfClient:"
+ "setSuCard:"
+ "setSuSelectionCard:"
+ "setTimeoutIntervalForResource:"
+ "sfClient"
+ "showSUCard:build:icon:isAlternate:"
+ "showSUSelectionCard:"
+ "showScanningCard"
+ "softwareUpdateIconImage"
+ "startCatalogDownload:options:completionWithError:"
+ "startDownload:completionWithError:"
+ "startProxCardTransactionWithOptions:completion:"
+ "suCard"
+ "suSelectionCard"
+ "v12@?0B8"
+ "v16@?0q8"
+ "v24@?0q8@\"NSError\"16"
+ "v28@?0B8@\"NSError\"12@\"SUCoreDocumentation\"20"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "v36@0:8@16B24@?28"
+ "v44@0:8@16@24@32B40"
+ "windowScene:didUpdateEffectiveGeometry:"
- "Cleaning up key for device %@, which was added on: %@"
- "Device %@ found in recovered device ids (added on: %@)"
- "Device %@ is not a recently recovered device. Recently recovered: %@"
- "Failed to activate setupkit client: %@"
- "ForceAuthTag default is set to %@, but server have different auth tag %@, ignoring"
- "Got OSR message %@"
- "Got error from SetupKit: %@"
- "Ignoring user entered code %@ due to flag"
- "Keeping key for device %@, which was added on: %@"
- "Overall status is %@, type:%d, err:%@"
- "Persisting recovered device: %@ with current time: %@"
- "RecoverDeviceUI successfully initialized. Identifier is %@"
- "Remote device sent config: %@"
- "SetupKitEventHandler invoked for event : %d (%@)"
- "Subtitle is: %@"
- "Unhandled event %d (%@) recieved by setupKitEventHandler"
- "Unknown state (%@)!  file a bug"
- "User entered code %@, attempt # %llu"

```
