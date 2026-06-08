## TextSettingsBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0x45a8
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x1520
+1029.0.0.0.0
+  __TEXT.__text: 0x42e4
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0x14c0
   __TEXT.__objc_methlist: 0x9a0
-  __TEXT.__objc_classname: 0x16c
-  __TEXT.__cstring: 0x1f0
-  __TEXT.__const: 0xb8
-  __TEXT.__objc_methname: 0x230f
-  __TEXT.__oslogstring: 0x2e1
-  __TEXT.__objc_methtype: 0xc9c
+  __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x1c8
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__objc_classname: 0x15f
+  __TEXT.__cstring: 0x1d8
+  __TEXT.__objc_methname: 0x22d3
+  __TEXT.__oslogstring: 0x2e1
+  __TEXT.__objc_methtype: 0xc9d
+  __TEXT.__unwind_info: 0x188
   __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x198
   __DATA.__objc_const: 0xc00
-  __DATA.__objc_selrefs: 0x928
+  __DATA.__objc_selrefs: 0x910
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83C2F118-CAE1-3FD0-90EF-DC218AECE714
-  Functions: 109
-  Symbols:   506
-  CStrings:  518
+  UUID: B9CA0DC4-B908-3B04-BA05-E126C6649580
+  Functions: 107
+  Symbols:   502
+  CStrings:  513
 
Symbols:
+ GCC_except_table100
+ _OBJC_CLASS_$_PDRRegistry
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$deviceFromNRDevice:
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDomain:pdrDevice:
+ _objc_msgSend$isAltAccount
+ _objc_msgSend$materialFromPdrDevice:
+ _objc_msgSend$sizeFromPdrDevice:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- -[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:].cold.1
- GCC_except_table4
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsArchived
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSUUID
- __57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke.cold.1
- _objc_msgSend$activeDeviceSelectorBlock
- _objc_msgSend$boolValue
- _objc_msgSend$firstObject
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithDomain:pairedDevice:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$materialFromDevice:
- _objc_msgSend$sizeFromDevice:
- _objc_msgSend$valueForProperty:
- _objc_retainAutoreleasedReturnValue
Functions:
~ _textSettingsLocalizedStringForKeyAndTable : 176 -> 172
~ _getActiveDevice : 208 -> 84
~ _boldTextIsEnabledOnDevice : 144 -> 152
~ _boldTextKeyExistsOnDevice : 160 -> 164
~ _contentSizeCategoriesOnDevice : 400 -> 388
~ __mapCompanionTextSizeToGizmoSize : 428 -> 432
~ __defaultTextSize : 108 -> 92
~ _getWatchContentSize : 144 -> 140
~ _contentSizeCategoryOnDevice : 64 -> 60
~ _contentSizeCategoryOnDeviceOrCompanion : 320 -> 424
~ _contentSizeCategoryOnDeviceForValue : 92 -> 84
~ _contentSizeValueOnDevice : 116 -> 120
~ _contentSizeSetValueOnDevice : 252 -> 256
~ _cachedTextPreviewImage : 432 -> 404
~ _cacheTextPreviewImage : 284 -> 268
~ -[TextSettingsViewController initWithDevice:observer:] : 288 -> 468
~ -[TextSettingsViewController viewDidLoad] : 2744 -> 2492
~ -[TextSettingsViewController watchScreenInsetForDeviceSize:screenScale:] : 204 -> 244
~ -[TextSettingsViewController watchScreenSizeForDeviceSize:screenScale:] : 216 -> 236
~ -[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:] : 428 -> 508
~ ___74-[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:]_block_invoke : 124 -> 116
~ -[TextSettingsViewController titleString] : 12 -> 20
~ -[TextSettingsViewController detailString] : 152 -> 108
~ -[TextSettingsViewController suggestedButtonTitle] : 12 -> 20
~ -[TextSettingsViewController alternateButtonTitle] : 12 -> 20
~ -[TextSettingsViewController suggestedButtonPressed:] : 400 -> 332
~ -[TextSettingsViewController alternateButtonPressed:] : 264 -> 428
~ -[TextSettingsViewController tableView:cellForRowAtIndexPath:] : 660 -> 800
~ -[TextSettingsViewController switchToggled:] : 132 -> 124
~ -[TextSettingsViewController _sliderTextImageWithSystemImageName:] : 236 -> 212
~ -[TextSettingsViewController device] : 16 -> 20
~ -[TextSettingsViewController tableView] : 16 -> 20
~ -[TextSettingsViewController setTableView:] : 80 -> 20
~ -[TextSettingsViewController textPreviewWatchView] : 16 -> 20
~ -[TextSettingsViewController setTextPreviewWatchView:] : 80 -> 20
~ -[TextSettingsViewController textPreviewIllustratedWatchView] : 16 -> 20
~ -[TextSettingsViewController setTextPreviewIllustratedWatchView:] : 80 -> 20
~ -[TextSettingsViewController watchScreenImageView] : 16 -> 20
~ -[TextSettingsViewController setWatchScreenImageView:] : 80 -> 20
~ -[TextSettingsViewController selectedContentSizeValue] : 16 -> 20
~ -[TextSettingsViewController selectedBoldTextEnabled] : 16 -> 20
~ -[TextSettingsViewController setSelectedBoldTextEnabled:] : 16 -> 20
~ -[TextSettingsViewController defaultTextSizeLabel] : 16 -> 20
~ -[TextSettingsViewController setDefaultTextSizeLabel:] : 80 -> 20
~ -[TextSettingsViewController defaultContentSizeValue] : 16 -> 20
~ -[TextSettingsViewController setDefaultContentSizeValue:] : 16 -> 20
~ -[AXSliderValueTableViewCell initWithStyle:reuseIdentifier:] : 424 -> 388
~ -[AXSliderValueTableViewCell didMoveToSuperview] : 836 -> 736
~ -[AXSliderValueTableViewCell minimumValue] : 68 -> 64
~ -[AXSliderValueTableViewCell setMinimumValue:] : 84 -> 80
~ -[AXSliderValueTableViewCell maximumValue] : 68 -> 64
~ -[AXSliderValueTableViewCell setMaximumValue:] : 84 -> 80
~ -[AXSliderValueTableViewCell value] : 68 -> 64
~ -[AXSliderValueTableViewCell setValue:] : 84 -> 80
~ -[AXSliderValueTableViewCell _sliderChanged:] : 136 -> 128
~ -[AXSliderValueTableViewCell minimumValueImage] : 84 -> 76
~ -[AXSliderValueTableViewCell setMinimumValueImage:] : 100 -> 96
~ -[AXSliderValueTableViewCell maximumValueImage] : 84 -> 76
~ -[AXSliderValueTableViewCell setMaximumValueImage:] : 100 -> 96
~ -[AXSliderValueTableViewCell segmentCount] : 60 -> 56
~ -[AXSliderValueTableViewCell setSegmentCount:] : 84 -> 80
~ -[AXSliderValueTableViewCell slider] : 16 -> 20
~ -[AXSliderValueTableViewCell setSlider:] : 80 -> 20
~ -[TextSettingsMiniFlowController init] : 232 -> 224
~ -[TextSettingsMiniFlowController dealloc] : 104 -> 100
~ +[TextSettingsMiniFlowController controllerNeedsToRun] : 108 -> 92
~ +[TextSettingsMiniFlowController skipControllerForExpressMode:] : 216 -> 328
~ -[TextSettingsMiniFlowController holdBeforeDisplaying] : 436 -> 420
~ ___54-[TextSettingsMiniFlowController holdBeforeDisplaying]_block_invoke : 176 -> 172
~ ___54-[TextSettingsMiniFlowController holdBeforeDisplaying]_block_invoke_2 : 164 -> 156
~ -[TextSettingsMiniFlowController viewController] : 204 -> 232
~ -[TextSettingsMiniFlowController miniFlowStepComplete:] : 84 -> 80
~ -[TextSettingsMiniFlowController didReceiveIncomingData:] : 280 -> 272
~ ___57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke : 832 -> 848
~ ___57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke_2 : 212 -> 200
~ ___79-[TextSettingsMiniFlowController didSelectContentSizeCategory:boldTextEnabled:]_block_invoke : 300 -> 284
~ -[TextSettingsMiniFlowController textSettingsViewController] : 16 -> 20
~ -[TextSettingsMiniFlowController setTextSettingsViewController:] : 80 -> 20
~ -[TextSettingsMiniFlowController controllerHoldTimeoutTimer] : 16 -> 20
~ -[TextSettingsMiniFlowController setControllerHoldTimeoutTimer:] : 80 -> 20
~ -[TextSettingsMiniFlowController idsServicesQueue] : 16 -> 20
~ -[TextSettingsMiniFlowController setIdsServicesQueue:] : 80 -> 20
~ -[TextSettingsMiniFlowController controllerIsOnHold] : 16 -> 20
~ -[TextSettingsMiniFlowController setControllerIsOnHold:] : 16 -> 20
~ -[TextSettingsMiniFlowController receivedCachedScreenshots] : 16 -> 20
~ -[TextSettingsMiniFlowController setReceivedCachedScreenshots:] : 16 -> 20
CStrings:
+ "@\"PDRDevice\""
+ "T@\"PDRDevice\",R,N,V_device"
+ "deviceFromNRDevice:"
+ "getActivePairedDeviceIncludingAltAccount"
+ "initWithDomain:pdrDevice:"
+ "isAltAccount"
+ "materialFromPdrDevice:"
+ "sizeFromPdrDevice:"
- "@\"NRDevice\""
- "T@\"NRDevice\",R,N,V_device"
- "activeDeviceSelectorBlock"
- "b4fbd189-bf37-4c38-a2c3-a0471795086c"
- "boolValue"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "initWithDomain:pairedDevice:"
- "initWithUUIDString:"
- "materialFromDevice:"
- "sizeFromDevice:"
- "valueForProperty:"

```
