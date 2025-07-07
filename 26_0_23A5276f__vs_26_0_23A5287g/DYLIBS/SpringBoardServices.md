## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4556.102.0.0.0
-  __TEXT.__text: 0x73bf4
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x7d58
-  __TEXT.__cstring: 0xcbca
+4557.0.3.103.0
+  __TEXT.__text: 0x749b4
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x7e88
+  __TEXT.__cstring: 0xce0d
   __TEXT.__const: 0x5d8
-  __TEXT.__oslogstring: 0x4286
-  __TEXT.__gcc_except_tab: 0xd04
-  __TEXT.__dlopen_cstrs: 0x116
+  __TEXT.__oslogstring: 0x4454
+  __TEXT.__gcc_except_tab: 0xd14
+  __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2618
-  __TEXT.__objc_classname: 0x296a
-  __TEXT.__objc_methname: 0xfa51
-  __TEXT.__objc_methtype: 0x2b7e
-  __TEXT.__objc_stubs: 0x85a0
-  __DATA_CONST.__got: 0x838
-  __DATA_CONST.__const: 0x3320
-  __DATA_CONST.__objc_classlist: 0x660
+  __TEXT.__unwind_info: 0x2710
+  __TEXT.__objc_classname: 0x2a3c
+  __TEXT.__objc_methname: 0xfea5
+  __TEXT.__objc_methtype: 0x2bc3
+  __TEXT.__objc_stubs: 0x8780
+  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__const: 0x3338
+  __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f98
+  __DATA_CONST.__objc_selrefs: 0x3030
   __DATA_CONST.__objc_protorefs: 0x1a8
-  __DATA_CONST.__objc_superrefs: 0x420
-  __AUTH_CONST.__auth_got: 0x7f0
-  __AUTH_CONST.__const: 0x27d0
-  __AUTH_CONST.__cfstring: 0x9c20
-  __AUTH_CONST.__objc_const: 0x22a38
+  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__const: 0x27f0
+  __AUTH_CONST.__cfstring: 0x9dc0
+  __AUTH_CONST.__objc_const: 0x22dc8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x2e90
-  __DATA.__objc_ivar: 0x7b0
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x2fd0
+  __DATA.__objc_ivar: 0x7cc
   __DATA.__data: 0x1fc0
-  __DATA.__bss: 0x840
+  __DATA.__bss: 0x868
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x250

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 268717E5-6F17-3C04-806C-BC23B05B533B
-  Functions: 3907
-  Symbols:   13339
-  CStrings:  6069
+  UUID: 8A520B24-2FB6-3FF2-9710-1B29306F1CC9
+  Functions: 3938
+  Symbols:   13458
+  CStrings:  6144
 
Symbols:
+ +[SBSBuddyMultitaskingFlow sharedInstance]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics _initWithPreviousMultitaskingMode:currentMultitaskingMode:source:multitaskingBuddyPanePresentation:]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics currentMultitaskingMode]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics emit]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics emit].cold.1
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics multitaskingBuddyPanePresentation]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics previousMultitaskingMode]
+ -[SBSAbstractWindowingTelemetryPersonalizationMetrics source]
+ -[SBSBuddyMultitaskingFlow .cxx_destruct]
+ -[SBSBuddyMultitaskingFlow _currentDeviceMemorySizeInGigabytes]
+ -[SBSBuddyMultitaskingFlow _emitBuddyWindowingPersonalizationTelemetry]
+ -[SBSBuddyMultitaskingFlow _initialMultitaskingOptionSelectedInViewController]
+ -[SBSBuddyMultitaskingFlow _telemetryMultitaskingModeForOption:]
+ -[SBSBuddyMultitaskingFlow dealloc]
+ -[SBSBuddyMultitaskingFlow init]
+ -[SBSBuddyMultitaskingFlow setUserPreviouslySelectedMultitaskingOptionInViewController:]
+ -[SBSBuddyMultitaskingFlow userPreviouslySelectedMultitaskingOptionInViewController]
+ -[SBSBuddyWindowingTelemetryPersonalizationMetrics initWithPreviousMultitaskingMode:currentMultitaskingMode:hasShownMultitaskingBuddyPane:]
+ -[SBSControlCenterWindowingTelemetryPersonalizationMetrics initWithPreviousMultitaskingMode:currentMultitaskingMode:]
+ -[SBSHomeScreenService osMigrationDefaultHomeScreenLayout]
+ -[SBSHomeScreenService osMigrationDefaultHomeScreenLayout].cold.1
+ -[SBSSettingsWindowingTelemetryPersonalizationMetrics initWithPreviousMultitaskingMode:currentMultitaskingMode:]
+ _AnalyticsSendEventLazy
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ _OBJC_CLASS_$_SBSBuddyWindowingTelemetryPersonalizationMetrics
+ _OBJC_CLASS_$_SBSControlCenterWindowingTelemetryPersonalizationMetrics
+ _OBJC_CLASS_$_SBSSettingsWindowingTelemetryPersonalizationMetrics
+ _OBJC_IVAR_$_SBSAbstractWindowingTelemetryPersonalizationMetrics._currentMultitaskingMode
+ _OBJC_IVAR_$_SBSAbstractWindowingTelemetryPersonalizationMetrics._multitaskingBuddyPanePresentation
+ _OBJC_IVAR_$_SBSAbstractWindowingTelemetryPersonalizationMetrics._previousMultitaskingMode
+ _OBJC_IVAR_$_SBSAbstractWindowingTelemetryPersonalizationMetrics._source
+ _OBJC_IVAR_$_SBSBuddyMultitaskingFlow._hasShownMultitaskingBuddyPane
+ _OBJC_IVAR_$_SBSBuddyMultitaskingFlow._sbDefaults
+ _OBJC_IVAR_$_SBSBuddyMultitaskingFlow._userPreviouslySelectedMultitaskingOptionInViewController
+ _OBJC_METACLASS_$_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ _OBJC_METACLASS_$_SBSBuddyWindowingTelemetryPersonalizationMetrics
+ _OBJC_METACLASS_$_SBSControlCenterWindowingTelemetryPersonalizationMetrics
+ _OBJC_METACLASS_$_SBSSettingsWindowingTelemetryPersonalizationMetrics
+ _SBLogBuddy
+ _SBLogBuddy.__logObj
+ _SBLogBuddy.cold.1
+ _SBLogBuddy.onceToken
+ _SetupAssistantLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_SBSBuddyMultitaskingFlow
+ __OBJC_$_INSTANCE_METHODS_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ __OBJC_$_INSTANCE_METHODS_SBSBuddyWindowingTelemetryPersonalizationMetrics
+ __OBJC_$_INSTANCE_METHODS_SBSControlCenterWindowingTelemetryPersonalizationMetrics
+ __OBJC_$_INSTANCE_METHODS_SBSSettingsWindowingTelemetryPersonalizationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_SBSBuddyMultitaskingFlow
+ __OBJC_$_PROP_LIST_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ __OBJC_CLASS_RO_$_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ __OBJC_CLASS_RO_$_SBSBuddyWindowingTelemetryPersonalizationMetrics
+ __OBJC_CLASS_RO_$_SBSControlCenterWindowingTelemetryPersonalizationMetrics
+ __OBJC_CLASS_RO_$_SBSSettingsWindowingTelemetryPersonalizationMetrics
+ __OBJC_METACLASS_RO_$_SBSAbstractWindowingTelemetryPersonalizationMetrics
+ __OBJC_METACLASS_RO_$_SBSBuddyWindowingTelemetryPersonalizationMetrics
+ __OBJC_METACLASS_RO_$_SBSControlCenterWindowingTelemetryPersonalizationMetrics
+ __OBJC_METACLASS_RO_$_SBSSettingsWindowingTelemetryPersonalizationMetrics
+ __SBSetupAssistantFinished
+ ___59-[SBSAbstractWindowingTelemetryPersonalizationMetrics emit]_block_invoke
+ ___SBLogBuddy_block_invoke
+ ___SetupAssistantLibraryCore_block_invoke
+ ___block_literal_global.222
+ ___block_literal_global.263
+ ___getBYSetupAssistantFinishedDarwinNotificationSymbolLoc_block_invoke
+ ___getBYSetupAssistantFinishedDarwinNotificationSymbolLoc_block_invoke.cold.1
+ ___sharedInstance
+ _audit_stringSetupAssistant
+ _getBYSetupAssistantFinishedDarwinNotification
+ _getBYSetupAssistantFinishedDarwinNotification.cold.1
+ _getBYSetupAssistantFinishedDarwinNotificationSymbolLoc.ptr
+ _objc_msgSend$_currentDeviceMemorySizeInGigabytes
+ _objc_msgSend$_emitBuddyWindowingPersonalizationTelemetry
+ _objc_msgSend$_initialMultitaskingOptionSelectedInViewController
+ _objc_msgSend$_telemetryMultitaskingModeForOption:
+ _objc_msgSend$bundleID
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentMultitaskingMode
+ _objc_msgSend$date
+ _objc_msgSend$day
+ _objc_msgSend$emit
+ _objc_msgSend$initWithPreviousMultitaskingMode:currentMultitaskingMode:hasShownMultitaskingBuddyPane:
+ _objc_msgSend$multitaskingBuddyPanePresentation
+ _objc_msgSend$osMigrationDefaultHomeScreenLayout
+ _objc_msgSend$previousMultitaskingMode
+ _objc_msgSend$source
- -[SBSBuddyMultitaskingFlow _isLowCapacityDevice]
- ___block_literal_global.221
- _objc_msgSend$_isLowCapacityDevice
CStrings:
+ "@\"NSUserDefaults\""
+ "@32@0:8q16q24"
+ "@36@0:8q16q24B32"
+ "@48@0:8q16q24q32q40"
+ "Abstract class; do not use directly"
+ "BYSetupAssistantFinishedDarwinNotification"
+ "Buddy"
+ "NSString *getBYSetupAssistantFinishedDarwinNotification(void)"
+ "SBHasEverUsedMultiAppConfiguration"
+ "SBLastMultitaskingModeSwitchDate"
+ "SBSAbstractWindowingTelemetryPersonalizationMetrics"
+ "SBSAbstractWindowingTelemetryPersonalizationMetrics.m"
+ "SBSBuddyMultitaskingFlow.m"
+ "SBSBuddyWindowingTelemetryPersonalizationMetrics"
+ "SBSControlCenterWindowingTelemetryPersonalizationMetrics"
+ "SBSHomeScreenService: failed osMigrationDefaultHomeScreenLayout request (no target)."
+ "SBSSettingsWindowingTelemetryPersonalizationMetrics"
+ "Should not show multitasking buddy pane due to current device has memory size <= 3GB and user has never used multiple app configuration before."
+ "Should not show multitasking buddy pane due to flexible windowing feature is disabled or current device is not an iPad."
+ "Should not show multitasking buddy pane due to upgrading from Stage Manager."
+ "Should show multitasking buddy pane"
+ "T@\"NSNumber\",&,N,V_userPreviouslySelectedMultitaskingOptionInViewController"
+ "Tq,R,N,V_currentMultitaskingMode"
+ "Tq,R,N,V_multitaskingBuddyPanePresentation"
+ "Tq,R,N,V_previousMultitaskingMode"
+ "Tq,R,N,V_source"
+ "_currentDeviceMemorySizeInGigabytes"
+ "_currentMultitaskingMode"
+ "_emitBuddyWindowingPersonalizationTelemetry"
+ "_hasShownMultitaskingBuddyPane"
+ "_initWithPreviousMultitaskingMode:currentMultitaskingMode:source:multitaskingBuddyPanePresentation:"
+ "_initialMultitaskingOptionSelectedInViewController"
+ "_multitaskingBuddyPanePresentation"
+ "_previousMultitaskingMode"
+ "_sbDefaults"
+ "_source"
+ "_telemetryMultitaskingModeForOption:"
+ "_userPreviouslySelectedMultitaskingOptionInViewController"
+ "com.apple.Preferences"
+ "com.apple.SpringBoard.Windowing.Personalization"
+ "com.apple.springboard.windowing-telemetry-personalization"
+ "components:fromDate:toDate:options:"
+ "currentCalendar"
+ "currentMultitaskingMode"
+ "date"
+ "day"
+ "daysInPreviousMultitaskingMode"
+ "emit"
+ "initWithPreviousMultitaskingMode:currentMultitaskingMode:"
+ "initWithPreviousMultitaskingMode:currentMultitaskingMode:hasShownMultitaskingBuddyPane:"
+ "multitaskingBuddyPanePresentation"
+ "osMigrationDefaultHomeScreenLayout"
+ "previousMultitaskingMode"
+ "setUserPreviouslySelectedMultitaskingOptionInViewController:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "source"
+ "userPreviouslySelectedMultitaskingOptionInViewController"
+ "void *SetupAssistantLibrary(void)"
- "_isLowCapacityDevice"

```
