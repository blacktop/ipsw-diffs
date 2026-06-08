## RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0x122cc
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x2d00
-  __TEXT.__objc_methlist: 0x1098
-  __TEXT.__gcc_except_tab: 0x420
-  __TEXT.__cstring: 0x12bf
-  __TEXT.__objc_methname: 0x420f
-  __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0x165f
-  __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x15c7
-  __TEXT.__unwind_info: 0x3a0
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x1900
+2717.0.0.0.0
+  __TEXT.__text: 0x13700
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_stubs: 0x3200
+  __TEXT.__objc_methlist: 0x11b0
+  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__cstring: 0x153e
+  __TEXT.__objc_methname: 0x465a
+  __TEXT.__objc_classname: 0x14c
+  __TEXT.__objc_methtype: 0x16ad
+  __TEXT.__const: 0x80
+  __TEXT.__oslogstring: 0x19e7
+  __TEXT.__unwind_info: 0x320
+  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__cfstring: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x13a0
-  __DATA.__objc_selrefs: 0x1160
-  __DATA.__objc_ivar: 0xa8
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x240
+  __DATA.__objc_const: 0x14a8
+  __DATA.__objc_selrefs: 0x12a8
+  __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /System/Library/PrivateFrameworks/SetupKit.framework/SetupKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 819C1F9A-1761-3300-87ED-859C640D5862
-  Functions: 241
-  Symbols:   1984
-  CStrings:  1362
+  UUID: 026AF2D7-0DBD-372C-B8D4-6CD8B0FB7AF9
+  Functions: 273
+  Symbols:   2211
+  CStrings:  1485
 
Symbols:
+ -[RecoverDeviceUIExtensionRemoteViewController apcListener]
+ -[RecoverDeviceUIExtensionRemoteViewController configureSUCardForErase:isAlternate:]
+ -[RecoverDeviceUIExtensionRemoteViewController configureSUCardForRecovery:isAlternate:]
+ -[RecoverDeviceUIExtensionRemoteViewController convertDataToPasscode:]
+ -[RecoverDeviceUIExtensionRemoteViewController createDefaultAPCPlayerConfigurationData]
+ -[RecoverDeviceUIExtensionRemoteViewController eraseApprovalCard]
+ -[RecoverDeviceUIExtensionRemoteViewController eraseCard]
+ -[RecoverDeviceUIExtensionRemoteViewController handleAudioPasscodeError:]
+ -[RecoverDeviceUIExtensionRemoteViewController handleDetectedPasscode:]
+ -[RecoverDeviceUIExtensionRemoteViewController inErase]
+ -[RecoverDeviceUIExtensionRemoteViewController setApcListener:]
+ -[RecoverDeviceUIExtensionRemoteViewController setDefaultPasscodeCardText]
+ -[RecoverDeviceUIExtensionRemoteViewController setEraseApprovalCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController setEraseCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController setInErase:]
+ -[RecoverDeviceUIExtensionRemoteViewController setPasscodeCardText:entryViewText:]
+ -[RecoverDeviceUIExtensionRemoteViewController setupCorrectPasscodeCard]
+ -[RecoverDeviceUIExtensionRemoteViewController setupHomePodListeningCard]
+ -[RecoverDeviceUIExtensionRemoteViewController setupManualPasscodeEntryCard]
+ -[RecoverDeviceUIExtensionRemoteViewController showEraseApprovalCard:isAlternate:]
+ -[RecoverDeviceUIExtensionRemoteViewController showEraseCard]
+ -[UIImageView(AlignmentInsets) maxAlignmentRectInsets]
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/CircularProgressView.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceMenuViewController.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUIAppDelegate.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUISceneDelegate.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUIViewController.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/RecoverDeviceUI/
+ GCC_except_table100
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table5
+ GCC_except_table93
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._apcListener
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._eraseApprovalCard
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._eraseCard
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._inErase
+ _NSLocalizedDescriptionKey
+ _NeRDExtraDataFromNSData
+ _OBJC_CLASS_$_APCCodecInfo
+ _OBJC_CLASS_$_APCListener
+ _OBJC_CLASS_$_NSMutableString
+ __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.996
+ __61-[RecoverDeviceUIExtensionRemoteViewController showEraseCard]_block_invoke.793
+ __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.783
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.854
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.855
+ __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.856
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.914
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.916
+ __68-[RecoverDeviceUIExtensionRemoteViewController showSUSelectionCard:]_block_invoke.890
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.1000
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.1001
+ __73-[RecoverDeviceUIExtensionRemoteViewController setupHomePodListeningCard]_block_invoke.1022
+ __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.580
+ __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.757
+ __80-[RecoverDeviceUIExtensionRemoteViewController configureWithContext:completion:]_block_invoke.554
+ __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.872
+ __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.874
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.907
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIImageView_$_AlignmentInsets
+ __OBJC_$_CATEGORY_UIImageView_$_AlignmentInsets
+ ___61-[RecoverDeviceUIExtensionRemoteViewController showEraseCard]_block_invoke
+ ___61-[RecoverDeviceUIExtensionRemoteViewController showEraseCard]_block_invoke_2
+ ___61-[RecoverDeviceUIExtensionRemoteViewController showEraseCard]_block_invoke_3
+ ___73-[RecoverDeviceUIExtensionRemoteViewController setupHomePodListeningCard]_block_invoke
+ ___76-[RecoverDeviceUIExtensionRemoteViewController setupManualPasscodeEntryCard]_block_invoke
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showEraseApprovalCard:isAlternate:]_block_invoke
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showEraseApprovalCard:isAlternate:]_block_invoke_2
+ ___82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke_4
+ ___84-[RecoverDeviceUIExtensionRemoteViewController configureSUCardForErase:isAlternate:]_block_invoke
+ ___87-[RecoverDeviceUIExtensionRemoteViewController configureSUCardForRecovery:isAlternate:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32w_e18_v16?0"NSString"8lw32l8
+ ___block_descriptor_40_e8_32w_e28_v24?0"NSError"8"NSData"16lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e18_v16?0"UIAction"8ls32l8s40l8s48l8
+ __block_literal_global.998
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$apcListener
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bytes
+ _objc_msgSend$configurationClassForName:
+ _objc_msgSend$configureSUCardForErase:isAlternate:
+ _objc_msgSend$configureSUCardForRecovery:isAlternate:
+ _objc_msgSend$convertDataToPasscode:
+ _objc_msgSend$copy
+ _objc_msgSend$createDefaultAPCPlayerConfigurationData
+ _objc_msgSend$eraseApprovalCard
+ _objc_msgSend$eraseCard
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$handleAudioPasscodeError:
+ _objc_msgSend$handleDetectedPasscode:
+ _objc_msgSend$inErase
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCodecConfiguration:
+ _objc_msgSend$initWithCommandLineArgs:
+ _objc_msgSend$length
+ _objc_msgSend$maxAlignmentRectInsets
+ _objc_msgSend$nearbyActionExtraData
+ _objc_msgSend$setApcListener:
+ _objc_msgSend$setDefaultPasscodeCardText
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setEraseApprovalCard:
+ _objc_msgSend$setEraseCard:
+ _objc_msgSend$setInErase:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setPasscodeCardText:entryViewText:
+ _objc_msgSend$setPayloadLengthBytes:
+ _objc_msgSend$setPersistentPairing:
+ _objc_msgSend$setRetrievedDataHandler:
+ _objc_msgSend$setupCorrectPasscodeCard
+ _objc_msgSend$setupHomePodListeningCard
+ _objc_msgSend$setupManualPasscodeEntryCard
+ _objc_msgSend$showEraseApprovalCard:isAlternate:
+ _objc_msgSend$showEraseCard
+ _objc_msgSend$startListeningWithError:
+ _objc_msgSend$stopListening
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/CircularProgressView.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceMenuViewController.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUIAppDelegate.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUISceneDelegate.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/RecoverDeviceUI.build/Objects-normal/arm64e/RecoverDeviceUIViewController.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/RecoverDeviceUI/
- GCC_except_table2
- GCC_except_table80
- GCC_except_table87
- __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.933
- __64-[RecoverDeviceUIExtensionRemoteViewController showRecoveryCard]_block_invoke.728
- __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.786
- __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.787
- __66-[RecoverDeviceUIExtensionRemoteViewController cleanDocumentation]_block_invoke.788
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.845
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.847
- __68-[RecoverDeviceUIExtensionRemoteViewController showSUSelectionCard:]_block_invoke.818
- __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.937
- __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.938
- __75-[RecoverDeviceUIExtensionRemoteViewController overallResultSUButtonAction]_block_invoke.531
- __78-[RecoverDeviceUIExtensionRemoteViewController sendMessage:completionHandler:]_block_invoke.702
- __80-[RecoverDeviceUIExtensionRemoteViewController configureWithContext:completion:]_block_invoke.505
- __82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke.816
- __82-[RecoverDeviceUIExtensionRemoteViewController showSUCard:build:icon:isAlternate:]_block_invoke_2.817
- __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.804
- __92-[RecoverDeviceUIExtensionRemoteViewController collectDocumentation:alternative:completion:]_block_invoke.806
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.826
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.837
- ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
- __block_literal_global.935
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%d%d"
+ "%s: called with subtitle: %{public}@, entryViewText: %{public}@"
+ "-[RecoverDeviceUIExtensionRemoteViewController setPasscodeCardText:entryViewText:]"
+ "@\"APCListener\""
+ "APCListener detected invalid BCD passcode format"
+ "APCListener detected passcode: %{public}@"
+ "APCListener error: %{public}@"
+ "APCListener invalidated"
+ "APCListener started successfully for HomePod authentication"
+ "AlignmentInsets"
+ "Converted BCD data to passcode: %{public}@"
+ "Creating audio listening UI for HomePod authentication"
+ "Creating manual passcode entry UI for device type: %d"
+ "Device needing recovery is an HomePod"
+ "Doc asset query found results: %{public}@"
+ "DontPersistPairing"
+ "DontPersistPairing flag set - using transient pairing (kPairingFlag_Transient)"
+ "ERASE_APPROVAL_SUBTITLE"
+ "ERASE_DETAILS"
+ "Failed to create APCPlayer configuration data"
+ "Failed to get 'echo' configuration class"
+ "Failed to start APCListener: %{public}@"
+ "HomePod does not have valid audio TTR extra data, ignoring"
+ "HomePod extra data: %{public}@"
+ "Invalid BCD data length: expected 3 bytes, got %lu"
+ "Invalid BCD digit in byte %lu: 0x%02X"
+ "Invalid BCD passcode format detected"
+ "LISTENING_CARD_DESCRIPTION"
+ "LISTENING_CARD_TITLE"
+ "LISTENING_STATUS"
+ "MENU_ERASE_BUTTON_SUBTITLE"
+ "MENU_ERASE_BUTTON_TITLE"
+ "MENU_ERASE_IN_PROGRESS_TEXT"
+ "NeRDEraseEnabled"
+ "NeRDExtraData{valid_bits=%u, version=%u, is_audio_ttr=%u}"
+ "NeRDIntentEraseOnly"
+ "NeRDOOBCommandErase"
+ "NeRDOOBCommandSelectSUForErase"
+ "NeRDStateErasing"
+ "PROGRESS_STATE_ERASING"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "Received passcode BCD data: %{public}@"
+ "Remote device wants to show erase only"
+ "START_ERASE_BUTTON_TEXT"
+ "SU_CARD_ERASE_DETAILS"
+ "SU_CARD_ERASE_TITLE"
+ "Setting passcode entry view text to %{public}@"
+ "T@\"APCListener\",&,N,V_apcListener"
+ "T@\"PRXCardContentViewController\",&,N,V_eraseApprovalCard"
+ "T@\"PRXCardContentViewController\",&,N,V_eraseCard"
+ "TB,V_inErase"
+ "_apcListener"
+ "_eraseApprovalCard"
+ "_eraseCard"
+ "_inErase"
+ "apcListener"
+ "appendFormat:"
+ "boolForKey:"
+ "bytes"
+ "configurationClassForName:"
+ "configureSUCardForErase:isAlternate:"
+ "configureSUCardForRecovery:isAlternate:"
+ "convertDataToPasscode:"
+ "copy"
+ "createDefaultAPCPlayerConfigurationData"
+ "echo"
+ "erase button pressed, showing progress"
+ "erase button pressed, waiting for scan results"
+ "eraseApprovalCard"
+ "eraseCard"
+ "getBytes:length:"
+ "handleAudioPasscodeError:"
+ "handleDetectedPasscode:"
+ "homepod.and.homepod.mini.badge.exclamationmark"
+ "inErase"
+ "initWithCapacity:"
+ "initWithCodecConfiguration:"
+ "initWithCommandLineArgs:"
+ "length"
+ "maxAlignmentRectInsets"
+ "nearbyActionExtraData"
+ "setApcListener:"
+ "setDefaultPasscodeCardText"
+ "setDispatchQueue:"
+ "setEraseApprovalCard:"
+ "setEraseCard:"
+ "setInErase:"
+ "setInvalidationHandler:"
+ "setPasscodeCardText:entryViewText:"
+ "setPayloadLengthBytes:"
+ "setPersistentPairing:"
+ "setRetrievedDataHandler:"
+ "setupCorrectPasscodeCard"
+ "setupHomePodListeningCard"
+ "setupManualPasscodeEntryCard"
+ "showEraseApprovalCard:isAlternate:"
+ "showEraseCard"
+ "startListeningWithError:"
+ "stopListening"
+ "supportedInterfaceOrientationsForWindowScene:"
+ "v24@?0@\"NSError\"8@\"NSData\"16"
+ "waveform"
+ "{UIEdgeInsets=dddd}16@0:8"
- "Continue"
- "Doc asset query found results:%{public}@"
- "homepod.badge.exclamationmark"

```
