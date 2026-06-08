## AccessibilityBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/AccessibilityBridgeSetup.bundle/AccessibilityBridgeSetup`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0x2464
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0xd00
+1029.0.0.0.0
+  __TEXT.__text: 0x22dc
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x7e0
-  __TEXT.__cstring: 0x254
-  __TEXT.__objc_methname: 0x1a7d
-  __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methtype: 0xb84
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__cstring: 0x235
+  __TEXT.__objc_methname: 0x1a45
+  __TEXT.__objc_classname: 0x12e
+  __TEXT.__objc_methtype: 0xb85
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0xa8
   __DATA.__objc_const: 0x998
-  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_selrefs: 0x6e8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x240

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
-  UUID: 692A6A5F-D077-3C98-9CE9-763B39F64A05
+  UUID: 7E24A536-81C9-345E-9222-BB5288D1DE52
   Functions: 62
   Symbols:   315
-  CStrings:  403
+  CStrings:  399
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$deviceFromNRDevice:
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDomain:pdrDevice:
+ _objc_msgSend$isAltAccount
+ _objc_release_x9
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsArchived
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSUUID
- _objc_msgSend$activeDeviceSelectorBlock
- _objc_msgSend$firstObject
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithDomain:pairedDevice:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$valueForProperty:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ -[AccessibilitySettingsViewController initWithAccessibilityOptions:device:] : 564 -> 572
~ -[AccessibilitySettingsViewController viewDidLoad] : 1440 -> 1280
~ -[AccessibilitySettingsViewController viewDidAppear:] : 160 -> 148
~ -[AccessibilitySettingsViewController suggestedButtonPressed:] : 152 -> 140
~ -[AccessibilitySettingsViewController numberOfSectionsInTableView:] : 60 -> 56
~ -[AccessibilitySettingsViewController tableView:titleForFooterInSection:] : 112 -> 136
~ -[AccessibilitySettingsViewController tableView:cellForRowAtIndexPath:] : 456 -> 444
~ -[AccessibilitySettingsViewController switchToggled:] : 440 -> 404
~ -[AccessibilitySettingsViewController accessibilityOptions] : 16 -> 20
~ -[AccessibilitySettingsViewController device] : 16 -> 20
~ -[AccessibilitySettingsViewController tableView] : 16 -> 20
~ -[AccessibilitySettingsViewController setTableView:] : 80 -> 20
~ -[AccessibilitySettingsViewController customizedAccessibilityOptions] : 16 -> 20
~ -[AccessibilitySettingsViewController setCustomizedAccessibilityOptions:] : 80 -> 20
~ _accessibilitySetupOptionIsActive : 232 -> 220
~ _accessibilityGetActiveDevice : 208 -> 84
~ _accessibilityDomainKeyForSetupOption : 176 -> 212
~ _accessibilityActiveAccessibilityFeaturesOnCompanion : 156 -> 352
~ _accessibilityLocalizedString : 168 -> 160
~ _accessibilityLocalizedStringForSetupOption : 88 -> 84
~ _accessibilityLocalizedDescriptionForSetupOption : 88 -> 84
~ _accessibilitySetAccessibilityOptionsOnDevice : 516 -> 656
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
~ +[AccessibilitySettingsMiniFlowController controllerNeedsToRun] : 144 -> 124
~ -[AccessibilitySettingsMiniFlowController viewController] : 224 -> 256
~ -[AccessibilitySettingsMiniFlowController miniFlowStepComplete:] : 84 -> 80
~ -[AccessibilitySettingsMiniFlowController accessibilitySettingsViewController] : 16 -> 20
~ -[AccessibilitySettingsMiniFlowController setAccessibilitySettingsViewController:] : 80 -> 20
CStrings:
+ "@\"PDRDevice\""
+ "T@\"PDRDevice\",R,N,V_device"
+ "deviceFromNRDevice:"
+ "getActivePairedDeviceIncludingAltAccount"
+ "initWithDomain:pdrDevice:"
+ "isAltAccount"
- "@\"NRDevice\""
- "T@\"NRDevice\",R,N,V_device"
- "activeDeviceSelectorBlock"
- "d7b1db8f-6f20-44a7-b454-95b8a418d208"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "initWithDomain:pairedDevice:"
- "initWithUUIDString:"
- "valueForProperty:"

```
