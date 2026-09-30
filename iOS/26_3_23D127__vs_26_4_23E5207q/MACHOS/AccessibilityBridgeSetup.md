## AccessibilityBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/AccessibilityBridgeSetup.bundle/AccessibilityBridgeSetup`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x2150
-  __TEXT.__auth_stubs: 0x2b0
+1001.12.0.0.0
+  __TEXT.__text: 0x2464
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0xd00
   __TEXT.__objc_methlist: 0x7e0
   __TEXT.__cstring: 0x254
   __TEXT.__objc_methname: 0x1a7d
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methtype: 0xb84
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x160
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x320

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 623F800D-021C-38F6-9826-3516126A53AA
+  UUID: 22DAB78F-D24C-3274-8A47-0E0F03B455A2
   Functions: 62
-  Symbols:   320
+  Symbols:   315
   CStrings:  403
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[AccessibilitySettingsViewController initWithAccessibilityOptions:device:] : 552 -> 564
~ -[AccessibilitySettingsViewController viewDidLoad] : 1280 -> 1440
~ -[AccessibilitySettingsViewController viewDidAppear:] : 148 -> 160
~ -[AccessibilitySettingsViewController suggestedButtonPressed:] : 140 -> 152
~ -[AccessibilitySettingsViewController alternateButtonPressed:] : 352 -> 368
~ -[AccessibilitySettingsViewController numberOfSectionsInTableView:] : 56 -> 60
~ -[AccessibilitySettingsViewController tableView:titleForFooterInSection:] : 104 -> 112
~ -[AccessibilitySettingsViewController tableView:cellForRowAtIndexPath:] : 424 -> 456
~ -[AccessibilitySettingsViewController switchToggled:] : 404 -> 440
~ -[AccessibilitySettingsViewController setTableView:] : 20 -> 80
~ -[AccessibilitySettingsViewController setCustomizedAccessibilityOptions:] : 20 -> 80
~ _accessibilitySetupOptionIsActive : 228 -> 232
~ _accessibilityGetActiveDevice : 176 -> 208
~ _accessibilityDomainKeyForSetupOption : 212 -> 176
~ _accessibilityActiveAccessibilityFeaturesOnCompanion : 148 -> 156
~ _accessibilityLocalizedString : 160 -> 168
~ _accessibilityLocalizedStringForSetupOption : 84 -> 88
~ _accessibilityLocalizedDescriptionForSetupOption : 84 -> 88
~ _accessibilitySetAccessibilityOptionsOnDevice : 520 -> 516
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
~ +[AccessibilitySettingsMiniFlowController controllerNeedsToRun] : 132 -> 144
~ -[AccessibilitySettingsMiniFlowController viewController] : 204 -> 224
~ -[AccessibilitySettingsMiniFlowController miniFlowStepComplete:] : 80 -> 84
~ -[AccessibilitySettingsMiniFlowController setAccessibilitySettingsViewController:] : 20 -> 80
CStrings:
+ "D7B1DB8F-332F-481C-B7DE-7E80973B07BF"
- "D7B1DB8F-6F20-44A7-B454-95B8A418D208"

```
