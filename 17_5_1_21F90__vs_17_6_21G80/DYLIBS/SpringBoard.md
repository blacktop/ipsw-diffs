## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4416.306.103.0.0
-  __TEXT.__text: 0x89d94c
-  __TEXT.__auth_stubs: 0x4fc0
+4416.405.0.0.0
+  __TEXT.__text: 0x89f380
+  __TEXT.__auth_stubs: 0x4fd0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x85374
+  __TEXT.__objc_methlist: 0x853ec
   __TEXT.__const: 0x12700
-  __TEXT.__oslogstring: 0x4962f
-  __TEXT.__cstring: 0x6ac2c
-  __TEXT.__gcc_except_tab: 0xe54c
+  __TEXT.__oslogstring: 0x4977f
+  __TEXT.__cstring: 0x6ad7b
+  __TEXT.__gcc_except_tab: 0xe5bc
   __TEXT.__ustring: 0x15b4
   __TEXT.__dlopen_cstrs: 0x2e6
-  __TEXT.__unwind_info: 0x24c68
+  __TEXT.__unwind_info: 0x24cb4
   __TEXT.__eh_frame: 0xd48
   __TEXT.__objc_classname: 0x1bce9
-  __TEXT.__objc_methname: 0x1874f8
-  __TEXT.__objc_methtype: 0x3f2fb
-  __TEXT.__objc_stubs: 0xd0420
-  __DATA_CONST.__got: 0x27d8
-  __DATA_CONST.__const: 0x19090
+  __TEXT.__objc_methname: 0x1876ac
+  __TEXT.__objc_methtype: 0x3f329
+  __TEXT.__objc_stubs: 0xd05c0
+  __DATA_CONST.__got: 0x2820
+  __DATA_CONST.__const: 0x190e0
   __DATA_CONST.__objc_classlist: 0x44e8
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1de398
-  __DATA_CONST.__objc_selrefs: 0x3ea38
+  __DATA_CONST.__objc_const: 0x1de460
+  __DATA_CONST.__objc_selrefs: 0x3eaa0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_classrefs: 0x6478
   __DATA_CONST.__objc_superrefs: 0x35a0
   __DATA_CONST.__objc_arraydata: 0x14e0
   __AUTH_CONST.__objc_const: 0x2eaa0
-  __AUTH_CONST.__cfstring: 0x61040
-  __AUTH_CONST.__const: 0xea98
+  __AUTH_CONST.__cfstring: 0x611c0
+  __AUTH_CONST.__const: 0xeab8
   __AUTH_CONST.__objc_arrayobj: 0x1590
-  __AUTH_CONST.__objc_intobj: 0x24f0
+  __AUTH_CONST.__objc_intobj: 0x2580
   __AUTH_CONST.__objc_doubleobj: 0x530
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__auth_got: 0x27f8
+  __AUTH_CONST.__auth_got: 0x2800
   __AUTH.__objc_data: 0xc490
-  __DATA.__objc_ivar: 0xc920
+  __DATA.__objc_ivar: 0xc928
   __DATA.__data: 0x1aba8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xa68

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 56649
-  Symbols:   192951
-  CStrings:  76944
+  Functions: 56670
+  Symbols:   193027
+  CStrings:  76977
 
Symbols:
+ +[UISApplicationSupportDisplayEdgeInfo(SpringBoard) sb_displayEdgeInfoForScreenTypeConsideringCurrentDevice:]
+ -[SBActivitySystemApertureElementObserver _addPendingAlert:]
+ -[SBActivitySystemApertureElementObserver _removePendingItem:withPendingAlerts:]
+ -[SBAssistantController _isLocationTCCAlert:]
+ -[SBAssistantController alertItemsController:didActivateAlertItem:]
+ -[SBAssistantController alertItemsController:didDeactivateAlertItem:forReason:]
+ -[SBAssistantController alertItemsController:willActivateAlertItem:]
+ -[SBHomeScreenConfigurationManager currentConfiguration]
+ -[SBHomeScreenConfigurationManager currentFocusMode]
+ -[SBHomeScreenConfigurationManager iconModelDidLayout:]
+ -[SBHomeScreenConfigurationManager setCurrentConfiguration:]
+ -[SBHomeScreenConfigurationManager setCurrentFocusMode:]
+ -[SBHomeScreenConfigurationManager teardownFocusMode:rootFolder:]
+ -[SBHomeScreenConfigurationManager updateHomeScreenWithConfiguration:completion:]
+ -[SBHomeScreenConfigurationManager updateHomeScreenWithConfiguration:completion:].cold.1
+ -[SBIconController _analyticsLoggingForIconVisibility]
+ -[SBIconController _extractFieldsForIconVisibilityAnalytics:]
+ -[SBIconController _lookupVersionForIconVisibilityAnalytics:]
+ -[SBIconController _selectIconForIconVisibilityAnalytics:]
+ GCC_except_table541
+ GCC_except_table542
+ GCC_except_table569
+ GCC_except_table580
+ GCC_except_table582
+ GCC_except_table584
+ _OBJC_IVAR_$_SBHomeScreenConfigurationManager._currentConfiguration
+ _OBJC_IVAR_$_SBHomeScreenConfigurationManager._currentFocusMode
+ _SBHAnalyticsIconVisibility
+ _SBHAnalyticsIconVisibilityCustomIcon
+ _SBHAnalyticsIconVisibilityDimensions
+ _SBHAnalyticsIconVisibilityFirstPageOrDock
+ _SBHAnalyticsIconVisibilityIconClass
+ _SBHAnalyticsIconVisibilityIdentifier
+ _SBHAnalyticsIconVisibilityInFolderOrStack
+ _SBHAnalyticsIconVisibilityTotalIcons
+ _SBHAnalyticsIconVisibilityVersion
+ _SBHScreenTypeIsPhone
+ ___40-[SBHomeScreenConfigurationManager init]_block_invoke
+ ___54-[SBIconController _analyticsLoggingForIconVisibility]_block_invoke
+ ___55-[SBHomeScreenConfigurationManager iconModelDidLayout:]_block_invoke
+ ___55-[SBHomeScreenConfigurationManager iconModelDidLayout:]_block_invoke.cold.1
+ ___58-[SBIconController _selectIconForIconVisibilityAnalytics:]_block_invoke
+ ___58-[SBIconController _selectIconForIconVisibilityAnalytics:]_block_invoke_2
+ ___58-[SBIconController _selectIconForIconVisibilityAnalytics:]_block_invoke_3
+ ___64-[SBAssistantController alwaysOnLiveRenderingAssertionRequested]_block_invoke.179
+ ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.197
+ ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.202
+ ___80-[SBActivitySystemApertureElementObserver _removePendingItem:withPendingAlerts:]_block_invoke
+ ___83-[SBAssistantController siriPresentation:requestsDismissalWithOptions:withHandler:]_block_invoke.191
+ ___86-[SBAssistantController siriPresentation:requestsPresentationWithOptions:withHandler:]_block_invoke.186
+ ___block_descriptor_64_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r_e36_v32?0"SBIcon"8"NSIndexPath"16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.932
+ _objc_msgSend$_addPendingAlert:
+ _objc_msgSend$_analyticsLoggingForIconVisibility
+ _objc_msgSend$_extractFieldsForIconVisibilityAnalytics:
+ _objc_msgSend$_isLocationTCCAlert:
+ _objc_msgSend$_lookupVersionForIconVisibilityAnalytics:
+ _objc_msgSend$_removePendingItem:withPendingAlerts:
+ _objc_msgSend$_selectIconForIconVisibilityAnalytics:
+ _objc_msgSend$alternateIconName
+ _objc_msgSend$didDismissLocationTCC:
+ _objc_msgSend$didPresentLocationTCC:
+ _objc_msgSend$iconIsPrecomposed
+ _objc_msgSend$requiresDismissedPresentationmode
+ _objc_msgSend$sb_displayEdgeInfoForScreenTypeConsideringCurrentDevice:
+ _objc_msgSend$setIcons:gridCellInfoOptions:
- -[SBActivitySystemApertureElementObserver _removePendingItem:]
- -[SBApplication _isNewEnoughToKnowAboutJ7xx]
- -[SBHomeScreenConfigurationManager focusModeFromConfiguration:]
- -[SBHomeScreenConfigurationManager focusModeFromConfiguration:].cold.1
- -[SBHomeScreenConfigurationManager teardownFocusMode]
- GCC_except_table561
- GCC_except_table572
- GCC_except_table574
- GCC_except_table576
- ___62-[SBActivitySystemApertureElementObserver _removePendingItem:]_block_invoke
- ___64-[SBAssistantController alwaysOnLiveRenderingAssertionRequested]_block_invoke.178
- ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.196
- ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.201
- ___83-[SBAssistantController siriPresentation:requestsDismissalWithOptions:withHandler:]_block_invoke.190
- ___86-[SBAssistantController siriPresentation:requestsPresentationWithOptions:withHandler:]_block_invoke.185
- ___block_literal_global.878
- _objc_msgSend$_removePendingItem:
CStrings:
+ "%{public}@ - observed did activate alert item: %{public}@, notifying siri location tcc presented."
+ "%{public}@ - observed did deactivate alert item: %{public}@, notifying siri location tcc dismissed."
+ "://"
+ "@\"SBHFocusMode\""
+ "@\"SBSHomeScreenConfiguration\""
+ "An error occurred updating the installed focus mode: %{public}@"
+ "Installed focus mode with ID: %@"
+ "T@\"NSString\",C,N,V_extensionIdentifier"
+ "Tearing down focus mode with ID: %@"
+ "Updating installed focus mode because icon model laid out"
+ "_addPendingAlert:"
+ "_analyticsLoggingForIconVisibility"
+ "_currentFocusMode"
+ "_extractFieldsForIconVisibilityAnalytics:"
+ "_isLocationTCCAlert:"
+ "_lookupVersionForIconVisibilityAnalytics:"
+ "_removePendingItem:withPendingAlerts:"
+ "_selectIconForIconVisibilityAnalytics:"
+ "alternateIconName"
+ "com.apple.SpringBoard.HomeScreenConfigurationService.configuration.%@"
+ "com.apple.corelocation.CoreLocationRepromptAlwaysAuthPromptPlugin"
+ "com.apple.corelocation.CoreLocationTemporaryPreciseAuthPromptPlugin"
+ "com.apple.corelocation.CoreLocationVanillaWhenInUseAuthPromptPlugin"
+ "customIcon"
+ "didDismissLocationTCC:"
+ "didPresentLocationTCC:"
+ "iconDimensions"
+ "iconIsPrecomposed"
+ "iconType"
+ "iconVersion"
+ "inFolderOrStack"
+ "onFirstPageOrDock"
+ "requiresDismissedPresentationmode"
+ "sb_displayEdgeInfoForScreenTypeConsideringCurrentDevice:"
+ "setIcons:gridCellInfoOptions:"
+ "totalIcons"
- "17.5"
- "T@\"NSString\",&,V_extensionIdentifier"
- "Tearing down focus mode and restoring original state"
- "_removePendingItem:"
- "com.apple.springboard.homeScreenConfigurationService.configuration"

```
