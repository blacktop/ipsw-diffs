## NanoPeopleBridgeSettings

> `/System/Library/AccessibilityBundles/NanoPeopleBridgeSettings.axbundle/NanoPeopleBridgeSettings`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x18f4
-  __TEXT.__auth_stubs: 0x290
+1001.12.0.0.0
+  __TEXT.__text: 0x19f8
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0x300
   __TEXT.__objc_classname: 0x1a9

   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x198
   __DATA_CONST.__cfstring: 0x660

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5440116F-BFF7-3037-A438-E35812D8D363
+  UUID: 880921EA-17DD-3673-BCF8-864E557B3553
   Functions: 66
-  Symbols:   253
+  Symbols:   248
   CStrings:  214
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ ___63+[AXNanoPeopleBridgeSettingsGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___63+[AXNanoPeopleBridgeSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___63+[AXNanoPeopleBridgeSettingsGlue accessibilityInitializeBundle]_block_invoke_4 : 152 -> 160
~ _accessibilityLocalizedString : 160 -> 168
~ +[NPLPeopleViewControllerAccessibility _accessibilityPerformValidations:] : 468 -> 476
~ -[NPLPeopleViewControllerAccessibility _accessibilitySwapPeopleAtIndex:andIndex:] : 516 -> 552
~ ___81-[NPLPeopleViewControllerAccessibility _accessibilitySwapPeopleAtIndex:andIndex:]_block_invoke : 604 -> 620
~ __81-[NPLPeopleViewControllerAccessibility _accessibilitySwapPeopleAtIndex:andIndex:]_block_invoke.351 : 84 -> 88
~ -[NPLPeopleViewControllerAccessibility _accessibilityUpdateDialViewElements] : 156 -> 168
~ -[NPLPeopleViewControllerAccessibility _accessibilityElementsForDialPersonViews] : 204 -> 216
~ ___80-[NPLPeopleViewControllerAccessibility _accessibilityElementsForDialPersonViews]_block_invoke : 192 -> 208
~ -[NPLPeopleViewControllerAccessibility _accessibilityAssociateUIAXElement:withPersonView:] : 112 -> 116
~ -[NPLPeopleViewControllerAccessibility _accessibilityDialPersonViews] : 160 -> 168
~ +[NPLPersonViewAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[NPLPersonViewAccessibility isAccessibilityElement] : 108 -> 112
~ -[NPLPersonViewAccessibility accessibilityLabel] : 132 -> 144
~ -[NPLPersonViewAccessibility accessibilityValue] : 188 -> 200
~ -[NPLPersonViewAccessibility accessibilityIncrement] : 140 -> 144
~ -[NPLPersonViewAccessibility accessibilityDecrement] : 128 -> 132
~ -[NPLPersonViewAccessibility accessibilityHint] : 144 -> 148
~ -[NPLPersonViewAccessibility _accessibilityIsAddPersonSlot] : 60 -> 64
~ -[NPLPersonViewAccessibility _accessibilityPeopleViewController] : 88 -> 96
~ ___64-[NPLPersonViewAccessibility _accessibilityPeopleViewController]_block_invoke : 80 -> 84
~ +[NPLSettingsPeopleViewControllerAccessibility _accessibilityPerformValidations:] : 356 -> 364
~ -[NPLSettingsPeopleViewControllerAccessibility _accessibilityCenterOfDialView] : 88 -> 92
~ -[NPLSettingsPeopleViewControllerAccessibility peripheryPersonViewTapped:] : 224 -> 236
~ -[NPLSettingsPeopleViewControllerAccessibility _accessibilityUpdateDeleteButtonLabel] : 212 -> 232
~ -[NPLSettingsPeopleViewControllerAccessibility _accessibilityAddPersonSelected] : 60 -> 64
~ -[NPLSettingsPeopleViewControllerAccessibility _accessibilityUpdateCenterPersonViewAXInfo] : 100 -> 104

```
