## TextSettingsBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x3fe0
-  __TEXT.__auth_stubs: 0x370
+1001.12.0.0.0
+  __TEXT.__text: 0x45a8
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0x1520
   __TEXT.__objc_methlist: 0x9a0
   __TEXT.__objc_classname: 0x16c

   __TEXT.__oslogstring: 0x2e1
   __TEXT.__objc_methtype: 0xc9c
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x1c8
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x2a0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1417A7AE-F576-370C-98C0-5DE0D42F1353
+  UUID: 4B2272D0-D262-3CED-975C-39744573299E
   Functions: 109
-  Symbols:   510
+  Symbols:   506
   CStrings:  518
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ _textSettingsLocalizedStringForKeyAndTable : 172 -> 176
~ _getActiveDevice : 176 -> 208
~ _boldTextIsEnabledOnDevice : 152 -> 144
~ _boldTextKeyExistsOnDevice : 164 -> 160
~ _contentSizeCategoriesOnDevice : 388 -> 400
~ __mapCompanionTextSizeToGizmoSize : 432 -> 428
~ __defaultTextSize : 92 -> 108
~ _getWatchContentSize : 140 -> 144
~ _contentSizeCategoryOnDevice : 60 -> 64
~ _contentSizeCategoryOnDeviceOrCompanion : 300 -> 320
~ _contentSizeCategoryOnDeviceForValue : 84 -> 92
~ _contentSizeValueOnDevice : 104 -> 116
~ _contentSizeSetValueOnDevice : 240 -> 252
~ _cachedTextPreviewImage : 404 -> 432
~ _cacheTextPreviewImage : 268 -> 284
~ -[TextSettingsViewController initWithDevice:observer:] : 284 -> 288
~ -[TextSettingsViewController viewDidLoad] : 2484 -> 2744
~ -[TextSettingsViewController setSelectedContentSizeValue:] : 112 -> 116
~ -[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:] : 404 -> 428
~ ___74-[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:]_block_invoke : 116 -> 124
~ -[TextSettingsViewController detailString] : 136 -> 152
~ -[TextSettingsViewController suggestedButtonPressed:] : 376 -> 400
~ -[TextSettingsViewController alternateButtonPressed:] : 244 -> 264
~ -[TextSettingsViewController tableView:cellForRowAtIndexPath:] : 608 -> 660
~ -[TextSettingsViewController switchToggled:] : 124 -> 132
~ -[TextSettingsViewController _sliderTextImageWithSystemImageName:] : 212 -> 236
~ -[TextSettingsViewController setTableView:] : 20 -> 80
~ -[TextSettingsViewController setTextPreviewWatchView:] : 20 -> 80
~ -[TextSettingsViewController setTextPreviewIllustratedWatchView:] : 20 -> 80
~ -[TextSettingsViewController setWatchScreenImageView:] : 20 -> 80
~ -[TextSettingsViewController setDefaultTextSizeLabel:] : 20 -> 80
~ -[AXSliderValueTableViewCell initWithStyle:reuseIdentifier:] : 388 -> 424
~ -[AXSliderValueTableViewCell didMoveToSuperview] : 736 -> 836
~ -[AXSliderValueTableViewCell minimumValue] : 64 -> 68
~ -[AXSliderValueTableViewCell setMinimumValue:] : 80 -> 84
~ -[AXSliderValueTableViewCell maximumValue] : 64 -> 68
~ -[AXSliderValueTableViewCell setMaximumValue:] : 80 -> 84
~ -[AXSliderValueTableViewCell value] : 64 -> 68
~ -[AXSliderValueTableViewCell setValue:] : 80 -> 84
~ -[AXSliderValueTableViewCell _sliderChanged:] : 128 -> 136
~ -[AXSliderValueTableViewCell minimumValueImage] : 76 -> 84
~ -[AXSliderValueTableViewCell setMinimumValueImage:] : 96 -> 100
~ -[AXSliderValueTableViewCell maximumValueImage] : 76 -> 84
~ -[AXSliderValueTableViewCell setMaximumValueImage:] : 96 -> 100
~ -[AXSliderValueTableViewCell segmentCount] : 56 -> 60
~ -[AXSliderValueTableViewCell setSegmentCount:] : 80 -> 84
~ -[AXSliderValueTableViewCell setSlider:] : 20 -> 80
~ -[TextSettingsMiniFlowController init] : 224 -> 232
~ -[TextSettingsMiniFlowController dealloc] : 100 -> 104
~ +[TextSettingsMiniFlowController controllerNeedsToRun] : 104 -> 108
~ +[TextSettingsMiniFlowController skipControllerForExpressMode:] : 204 -> 216
~ -[TextSettingsMiniFlowController holdBeforeDisplaying] : 420 -> 436
~ ___54-[TextSettingsMiniFlowController holdBeforeDisplaying]_block_invoke : 172 -> 176
~ ___54-[TextSettingsMiniFlowController holdBeforeDisplaying]_block_invoke_2 : 156 -> 164
~ -[TextSettingsMiniFlowController viewController] : 188 -> 204
~ -[TextSettingsMiniFlowController miniFlowStepComplete:] : 80 -> 84
~ -[TextSettingsMiniFlowController didReceiveIncomingData:] : 272 -> 280
~ ___57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke : 804 -> 832
~ ___57-[TextSettingsMiniFlowController didReceiveIncomingData:]_block_invoke_2 : 200 -> 212
~ ___79-[TextSettingsMiniFlowController didSelectContentSizeCategory:boldTextEnabled:]_block_invoke : 284 -> 300
~ -[TextSettingsMiniFlowController setTextSettingsViewController:] : 20 -> 80
~ -[TextSettingsMiniFlowController setControllerHoldTimeoutTimer:] : 20 -> 80
~ -[TextSettingsMiniFlowController setIdsServicesQueue:] : 20 -> 80
~ -[TextSettingsViewController updateWatchScreenImageViewAndNotifyObserver:].cold.1 : 188 -> 192
CStrings:
+ "B4FBD189-332F-481C-B7DE-7E80973B07BF"
- "B4FBD189-BF37-4C38-A2C3-A0471795086C"

```
