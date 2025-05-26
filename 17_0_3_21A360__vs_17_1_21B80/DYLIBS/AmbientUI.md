## AmbientUI

> `/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI`

```diff

-52.2.1.0.0
-  __TEXT.__text: 0x2cb54
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x32f8
+52.7.100.0.0
+  __TEXT.__text: 0x2d9dc
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x341c
   __TEXT.__const: 0x624
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__cstring: 0x1aaf
-  __TEXT.__oslogstring: 0x1847
+  __TEXT.__gcc_except_tab: 0x36c
+  __TEXT.__cstring: 0x1add
+  __TEXT.__oslogstring: 0x198e
   __TEXT.__dlopen_cstrs: 0x110
-  __TEXT.__unwind_info: 0xe34
-  __TEXT.__objc_classname: 0xc06
-  __TEXT.__objc_methname: 0xf7ff
-  __TEXT.__objc_methtype: 0x51e9
-  __TEXT.__objc_stubs: 0x9000
+  __TEXT.__unwind_info: 0xe78
+  __TEXT.__objc_classname: 0xc09
+  __TEXT.__objc_methname: 0xfd05
+  __TEXT.__objc_methtype: 0x5254
+  __TEXT.__objc_stubs: 0x9260
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0xb68
+  __DATA_CONST.__const: 0xb60
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe398
-  __DATA_CONST.__objc_selrefs: 0x2bf0
+  __DATA_CONST.__objc_const: 0xe440
+  __DATA_CONST.__objc_selrefs: 0x2cf8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x1c80
-  __AUTH_CONST.__objc_const: 0x11e8
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x1230
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_classrefs: 0x568
+  __DATA.__objc_classrefs: 0x570
   __DATA.__objc_superrefs: 0x148
-  __DATA.__objc_ivar: 0x4a0
+  __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0x14a0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1318
-  Symbols:   5385
-  CStrings:  3099
+  Functions: 1344
+  Symbols:   5462
+  CStrings:  3143
 
Symbols:
+ +[AMUIInfographViewController(Testing) _bigDateTimeWidgetDescription]
+ +[AMUIInfographViewController(Testing) _bigDateTimeWidget]
+ +[AMUIInfographViewController(Testing) _clockCityWidgetDescription]
+ +[AMUIInfographViewController(Testing) _clockCityWidget]
+ +[AMUIInfographViewController(Testing) _clockLocalWidgetDescription]
+ +[AMUIInfographViewController(Testing) _clockLocalWidget]
+ +[AMUIInfographViewController(Testing) _clockSquareWidgetDescription]
+ +[AMUIInfographViewController(Testing) _clockSquareWidget]
+ +[AMUIInfographViewController(Testing) _defaultWidgetDescriptionForKind:bundleIdentifier:containerBundleIdentifier:]
+ +[AMUIInfographViewController(Testing) _stocksWidgetDescription]
+ +[AMUIInfographViewController(Testing) _stocksWidget]
+ -[AMUIAmbientViewController viewController:isApplicationVisibleWithBundleIdentifier:]
+ -[AMUIDataLayerViewController _updateRedModeFiltersForTraitEnvironment:previousTraitCollection:animated:]
+ -[AMUIDataLayerViewController viewController:isApplicationVisibleWithBundleIdentifier:]
+ -[AMUIInfographViewController _migrateClockCityWidgetForIconListModel:withDefaultIconState:]
+ -[AMUIInfographViewController _shouldMigrateClockCityWidgetForIconDataSources:withWidgetStackElements:]
+ -[AMUIInfographViewController iconManager:backgroundViewForComponentsOfType:forIconView:]
+ -[AMUIInfographViewController iconManager:isIconVisibleForBundleIdentifier:]
+ -[AMUIInfographViewController iconManager:verticalMarginPercentageForConfigurationOfIconView:]
+ -[AMUIInfographViewController setPosterConfiguration:].cold.5
+ -[AMUIInfographViewController(Testing) _setAmbientDefaults:]
+ -[AMUIInfographViewController(Testing) _shouldMigrateClockWidgetForIconDataSources:withWidgetStackElements:]
+ -[AMUIPosterCategoryViewController viewController:isApplicationVisibleWithBundleIdentifier:]
+ -[AMUIPosterEditingSwitcherViewController initWithActiveConfiguration:transitionOverlayView:]
+ -[AMUIPosterEditingSwitcherViewController transitionOverlayView]
+ -[AMUIPosterSwitcherViewController viewController:isApplicationVisibleWithBundleIdentifier:]
+ GCC_except_table125
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table157
+ GCC_except_table52
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table97
+ _CALayerGetRenderId
+ _OBJC_CLASS_$_SBLeafIcon
+ _OBJC_IVAR_$_AMUIPosterEditingSwitcherViewController._transitionOverlayView
+ __OBJC_$_CLASS_METHODS_AMUIInfographViewController(Testing)
+ __OBJC_$_INSTANCE_METHODS_AMUIInfographViewController(Testing)
+ ___68-[AMUIInfographViewController _launchConfirmationTapGestureDidFire:]_block_invoke
+ ___block_descriptor_32_e18_B16?0"BSAction"8l
+ ___block_literal_global.169
+ _getPRUIModalEntryPointAmbientEditingSwitcherWithActiveConfigurationClass
+ _objc_msgSend$_contextId
+ _objc_msgSend$_defaultWidgetDescriptionForKind:bundleIdentifier:containerBundleIdentifier:
+ _objc_msgSend$_migrateClockCityWidgetForIconListModel:withDefaultIconState:
+ _objc_msgSend$_shouldMigrateClockCityWidgetForIconDataSources:withWidgetStackElements:
+ _objc_msgSend$_updateRedModeFiltersForTraitEnvironment:previousTraitCollection:animated:
+ _objc_msgSend$alwaysUpdateIconModelOnAmbientWidgetLayoutChange
+ _objc_msgSend$ambientViewController:isApplicationVisibleWithBundleIdentifier:
+ _objc_msgSend$bs_filter:
+ _objc_msgSend$bs_safeStringForKey:
+ _objc_msgSend$hasMigratedClockCityWidget
+ _objc_msgSend$iconAtIndex:
+ _objc_msgSend$iconDataSources
+ _objc_msgSend$initWithActiveConfiguration:transitionOverlayRenderId:transitionOverlayContextId:
+ _objc_msgSend$initWithActiveConfiguration:transitionOverlayView:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$isValid
+ _objc_msgSend$setMigratedClockCityWidget:
+ _objc_msgSend$transitionOverlayView
+ _objc_msgSend$viewController:isApplicationVisibleWithBundleIdentifier:
- -[AMUIInfographViewController iconManager:backgroundViewForComponentsOfIconView:]
- -[AMUIPosterEditingSwitcherViewController initWithActiveConfiguration:]
- GCC_except_table123
- GCC_except_table145
- GCC_except_table149
- GCC_except_table154
- GCC_except_table51
- GCC_except_table72
- GCC_except_table74
- GCC_except_table95
- __OBJC_$_INSTANCE_METHODS_AMUIInfographViewController
- ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
CStrings:
+ "\x02\x11"
+ "0x%p: Applying red mode filter on the concreteDataLayerViewController of type:%@"
+ "0x%p: Clearing red mode filter on the concreteDataLayerViewController of type:%@"
+ "0x%p: Not changing red mode filters because red mode trait did not change ( isRedModeEnabled=%{BOOL}u )"
+ "@\"UIView\"40@0:8@\"SBHIconManager\"16q24@\"SBIconView\"32"
+ "B16@?0@\"BSAction\"8"
+ "B32@0:8@\"<AMUIAmbientViewControlling>\"16@\"NSString\"24"
+ "Received empty widgetLayoutIconState from posterConfiguration:%@"
+ "Skipping launch confirmation because iconView is no longer in a window"
+ "Skipping launch confirmation because iconView is not in the correct window"
+ "T@\"UIView\",R,N,V_transitionOverlayView"
+ "_bigDateTimeWidget"
+ "_bigDateTimeWidgetDescription"
+ "_clockCityWidget"
+ "_clockCityWidgetDescription"
+ "_clockLocalWidget"
+ "_clockLocalWidgetDescription"
+ "_clockSquareWidget"
+ "_clockSquareWidgetDescription"
+ "_contextId"
+ "_defaultWidgetDescriptionForKind:bundleIdentifier:containerBundleIdentifier:"
+ "_migrateClockCityWidgetForIconListModel:withDefaultIconState:"
+ "_setAmbientDefaults:"
+ "_shouldMigrateClockCityWidgetForIconDataSources:withWidgetStackElements:"
+ "_shouldMigrateClockWidgetForIconDataSources:withWidgetStackElements:"
+ "_stocksWidget"
+ "_stocksWidgetDescription"
+ "_transitionOverlayView"
+ "_updateRedModeFiltersForTraitEnvironment:previousTraitCollection:animated:"
+ "alwaysUpdateIconModelOnAmbientWidgetLayoutChange"
+ "ambientViewController:isApplicationVisibleWithBundleIdentifier:"
+ "bs_filter:"
+ "bs_safeStringForKey:"
+ "com.apple.mobiletimer.City"
+ "hasMigratedClockCityWidget"
+ "iconAtIndex:"
+ "iconDataSources"
+ "iconManager:backgroundViewForComponentsOfType:forIconView:"
+ "iconManager:verticalMarginPercentageForConfigurationOfIconView:"
+ "initWithActiveConfiguration:transitionOverlayRenderId:transitionOverlayContextId:"
+ "initWithActiveConfiguration:transitionOverlayView:"
+ "instancesRespondToSelector:"
+ "isValid"
+ "setMigratedClockCityWidget:"
+ "transitionOverlayView"
+ "viewController:isApplicationVisibleWithBundleIdentifier:"
- "Applying red mode filter on the concreteDataLayerViewController of type:%@"
- "Clearing red mode filter on the concreteDataLayerViewController of type:%@"

```
