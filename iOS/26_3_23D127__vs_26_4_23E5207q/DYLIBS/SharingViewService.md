## SharingViewService

> `/System/Library/AccessibilityBundles/SharingViewService.axbundle/SharingViewService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x46b8
-  __TEXT.__auth_stubs: 0x3a0
+3005.16.0.0.0
+  __TEXT.__text: 0x4a5c
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x760
   __TEXT.__cstring: 0xc7d
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0x60a
   __TEXT.__objc_methname: 0xb5b
   __TEXT.__objc_methtype: 0xdc

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0xf20
   __AUTH_CONST.__objc_const: 0x14c8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87EA1498-9645-3259-BB4C-7E03A31A74C2
+  UUID: 0147513B-3EBC-3A7B-803B-CC80D01BD920
   Functions: 147
-  Symbols:   687
+  Symbols:   682
   CStrings:  430
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x8
Functions:
~ ___57+[AXSharingViewServiceGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___57+[AXSharingViewServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___57+[AXSharingViewServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 392 -> 400
~ _localizedString : 172 -> 176
~ +[HeadphoneImageBatteryViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[HeadphoneImageBatteryViewAccessibility updateWithBattery:] : 336 -> 348
~ +[HeadphoneBatteryContainerAccessibility _accessibilityPerformValidations:] : 100 -> 108
~ -[HeadphoneBatteryContainerAccessibility accessibilityFrame] : 268 -> 276
~ +[HeadphoneMovieBatteryViewAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[HeadphoneMovieBatteryViewAccessibility accessibilityFrame] : 268 -> 276
~ -[HeadphoneMovieBatteryViewAccessibility updateWithBatteries:] : 220 -> 224
~ ___62-[HeadphoneMovieBatteryViewAccessibility updateWithBatteries:]_block_invoke : 224 -> 236
~ +[LabelledBatteryViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[LabelledBatteryViewAccessibility accessibilityLabel] : 180 -> 200
~ -[LabelledBatteryViewAccessibility accessibilityValue] : 84 -> 92
~ -[LabelledBatteryViewAccessibility accessibilityHint] : 84 -> 92
~ +[AppleTVSetupStartViewControllerAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[AppleTVSetupStartViewControllerAccessibility viewWillAppear:] : 176 -> 188
~ +[BroadwayActivationDoneViewControllerAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ ___68-[BroadwayActivationDoneViewControllerAccessibility viewWillAppear:]_block_invoke : 104 -> 108
~ -[BroadwayActivationDoneViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 148 -> 156
~ +[BroadwayActivationStartViewControllerAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ ___69-[BroadwayActivationStartViewControllerAccessibility viewWillAppear:]_block_invoke : 104 -> 108
~ -[BroadwayActivationStartViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 220 -> 236
~ +[PINEntryViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[PINEntryViewAccessibility _accessibilitySelectedTextRange] : 136 -> 144
~ -[PINEntryViewAccessibility accessibilityLabel] : 360 -> 392
~ -[PINEntryViewAccessibility accessibilityValue] : 168 -> 180
~ -[PINEntryViewAccessibility _updateLabels] : 220 -> 232
~ +[ProximityPairingViewControllerAccessibility _accessibilityPerformValidations:] : 396 -> 404
~ -[ProximityPairingViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 940 -> 1000
~ ___89-[ProximityPairingViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 108 -> 116
~ ___89-[ProximityPairingViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 108 -> 116
~ ___89-[ProximityPairingViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 108 -> 116
~ -[ProximityPairingViewControllerAccessibility accessibilityPerformEscape] : 64 -> 68
~ -[AXAggregatedDeviceBatteryStatusView initWithAccessibilityContainer:representedElements:primaryTitle:batteryLevelLabel:chargingImage:warningImage:] : 304 -> 288
~ -[AXAggregatedDeviceBatteryStatusView accessibilityLabel] : 76 -> 88
~ -[AXAggregatedDeviceBatteryStatusView accessibilityValue] : 288 -> 308
~ +[ProximityStatusViewControllerAccessibility _accessibilityPerformValidations:] : 824 -> 832
~ -[ProximityStatusViewControllerAccessibility _accessibilityUpdateAccessibilityElements] : 2420 -> 2716
~ -[ProximityStatusViewControllerAccessibility _axCreateAggregateStatusView:primaryTitle:batteryLevelLabel:chargingImage:warningImage:] : 408 -> 404
~ +[RepairStartViewControllerAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[RepairStartViewControllerAccessibility _axLabelDismissButton] : 160 -> 172
~ +[SVSBaseViewControllerAccessibility _accessibilityPerformValidations:] : 288 -> 296
~ -[SVSBaseViewControllerAccessibility viewDidAppear:] : 784 -> 828
~ ___52-[SVSBaseViewControllerAccessibility viewDidAppear:]_block_invoke_2 : 136 -> 144
~ ___52-[SVSBaseViewControllerAccessibility viewDidAppear:]_block_invoke_4 : 136 -> 140
~ ___52-[SVSBaseViewControllerAccessibility viewDidAppear:]_block_invoke.354 : 480 -> 524
~ ___52-[SVSBaseViewControllerAccessibility viewDidAppear:]_block_invoke_3.362 : 16 -> 64
~ +[UIButtonAccessibility__Sharing__UIKit _accessibilityPerformValidations:] : 148 -> 156
~ -[UIButtonAccessibility__Sharing__UIKit _axIsDismissButton] : 688 -> 696
~ -[UIButtonAccessibility__Sharing__UIKit accessibilityLabel] : 204 -> 216
~ +[WHASetupStartViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[WHASetupStartViewControllerAccessibility _axLabelDismissButton] : 160 -> 172
~ +[iOSSetupStartViewControllerAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[iOSSetupStartViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 220 -> 236

```
