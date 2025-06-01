## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-503.0.30.0.0
-  __TEXT.__text: 0xdbc60
+503.1.5.0.0
+  __TEXT.__text: 0xdc04c
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x942c
+  __TEXT.__objc_methlist: 0x9484
   __TEXT.__const: 0x12f4
-  __TEXT.__cstring: 0xac94
-  __TEXT.__oslogstring: 0x3056
-  __TEXT.__gcc_except_tab: 0x9bc
+  __TEXT.__cstring: 0xad04
+  __TEXT.__oslogstring: 0x30b5
+  __TEXT.__gcc_except_tab: 0x9d8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x18f4
   __TEXT.__swift5_capture: 0x4a8

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x54
-  __TEXT.__unwind_info: 0x2e70
+  __TEXT.__unwind_info: 0x2ea4
   __TEXT.__eh_frame: 0x13d8
-  __TEXT.__objc_classname: 0x19c9
-  __TEXT.__objc_methname: 0x1e5e7
-  __TEXT.__objc_methtype: 0x34c1
-  __TEXT.__objc_stubs: 0x13640
-  __DATA_CONST.__got: 0x850
-  __DATA_CONST.__const: 0x1ed8
-  __DATA_CONST.__objc_classlist: 0x600
+  __TEXT.__objc_classname: 0x1a18
+  __TEXT.__objc_methname: 0x1e67f
+  __TEXT.__objc_methtype: 0x35cf
+  __TEXT.__objc_stubs: 0x13600
+  __DATA_CONST.__got: 0x860
+  __DATA_CONST.__const: 0x1ee8
+  __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ac40
+  __DATA_CONST.__objc_const: 0x1b0a8
   __DATA_CONST.__objc_selrefs: 0x5cf8
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__objc_const: 0x3f18
+  __AUTH_CONST.__objc_const: 0x3f60
   __AUTH_CONST.__cfstring: 0x9c80
   __AUTH_CONST.__objc_intobj: 0x7e0
-  __AUTH_CONST.__const: 0x1d50
+  __AUTH_CONST.__const: 0x1d30
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0xe08
-  __AUTH.__objc_data: 0x35b0
+  __AUTH.__objc_data: 0x3600
   __AUTH.__data: 0x2a0
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0xc10
-  __DATA.__objc_superrefs: 0x538
-  __DATA.__objc_ivar: 0xbac
+  __DATA.__objc_classrefs: 0xc18
+  __DATA.__objc_superrefs: 0x540
+  __DATA.__objc_ivar: 0xbb4
   __DATA.__objc_data: 0x108
-  __DATA.__data: 0x1b50
+  __DATA.__data: 0x1bb0
   __DATA.__bss: 0xac0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x960

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F345DD20-1489-3FC4-ACC9-F8CF2F046EFC
-  Functions: 4553
-  Symbols:   13602
-  CStrings:  8037
+  UUID: CDF2669B-41D0-3FEA-A5B0-BEA99666863D
+  Functions: 4554
+  Symbols:   13622
+  CStrings:  8045
 
Symbols:
+ -[STContentPrivacyAllowedAppsDetailController defaultSwitchSpecifierWithConfiguration:key:fallbackLabel:]
+ -[STCustomizeDailyScheduleListController cancelButtonTapped:]
+ -[STCustomizeDailyScheduleListController delegate]
+ -[STCustomizeDailyScheduleListController doneButtonTapped:]
+ -[STCustomizeDailyScheduleListController setDelegate:]
+ -[STDeviceBedtimeListController _saveDowntimeAndReloadSpecifiers:]
+ -[STDeviceBedtimeListController _showEditSimpleScheduleListController:]
+ -[STDeviceBedtimeListController _simpleScheduleTime:]
+ -[STDeviceBedtimeListController customizeDailyScheduleListController:didSaveDailySchedule:forWeekdayIndex:]
+ -[STDeviceBedtimeListController customizeDailyScheduleListControllerDidCancel:]
+ -[STDeviceBedtimeListController dailyScheduleSpecifier]
+ -[STDeviceBedtimeListController setDailyScheduleSpecifier:]
+ -[STDeviceBedtimeListController simpleScheduleListController:didSaveSimpleSchedule:]
+ -[STDeviceBedtimeListController simpleScheduleListControllerDidCancel:]
+ -[STScreenTimeReportController _didTapShowThisWeekButton:]
+ -[STScreenTimeReportController _didTapShowTodayButton:]
+ -[STSimpleScheduleListController .cxx_destruct]
+ -[STSimpleScheduleListController _endTime:]
+ -[STSimpleScheduleListController _startTime:]
+ -[STSimpleScheduleListController _updateTimeSpecifierDetailTextLabelColors:selectedSpecifier:unselectedSpecifier:]
+ -[STSimpleScheduleListController canBeShownFromSuspendedState]
+ -[STSimpleScheduleListController cancelButtonTapped:]
+ -[STSimpleScheduleListController datePickerChanged:]
+ -[STSimpleScheduleListController datePickerForSpecifier:]
+ -[STSimpleScheduleListController delegate]
+ -[STSimpleScheduleListController doneButtonTapped:]
+ -[STSimpleScheduleListController endTimePickerSpecifier]
+ -[STSimpleScheduleListController endTimeSpecifier]
+ -[STSimpleScheduleListController initWithSimpleSchedule:]
+ -[STSimpleScheduleListController setDelegate:]
+ -[STSimpleScheduleListController setSimpleSchedule:]
+ -[STSimpleScheduleListController simpleScheduleGroupSpecifier]
+ -[STSimpleScheduleListController simpleSchedule]
+ -[STSimpleScheduleListController specifiers]
+ -[STSimpleScheduleListController startTimePickerSpecifier]
+ -[STSimpleScheduleListController startTimeSpecifier]
+ -[STSimpleScheduleListController tableView:didSelectRowAtIndexPath:]
+ -[STSimpleScheduleListController tableView:willDisplayCell:forRowAtIndexPath:]
+ GCC_except_table25
+ GCC_except_table97
+ _OBJC_CLASS_$_STSimpleScheduleListController
+ _OBJC_IVAR_$_STCustomizeDailyScheduleListController._delegate
+ _OBJC_IVAR_$_STDeviceBedtimeListController._dailyScheduleSpecifier
+ _OBJC_IVAR_$_STSimpleScheduleListController._delegate
+ _OBJC_IVAR_$_STSimpleScheduleListController._endTimePickerSpecifier
+ _OBJC_IVAR_$_STSimpleScheduleListController._endTimeSpecifier
+ _OBJC_IVAR_$_STSimpleScheduleListController._simpleSchedule
+ _OBJC_IVAR_$_STSimpleScheduleListController._simpleScheduleGroupSpecifier
+ _OBJC_IVAR_$_STSimpleScheduleListController._startTimePickerSpecifier
+ _OBJC_IVAR_$_STSimpleScheduleListController._startTimeSpecifier
+ _OBJC_METACLASS_$_STSimpleScheduleListController
+ _STScreenTimeReportDidTapShowThisWeekButton
+ _STScreenTimeReportDidTapShowTodayButton
+ __OBJC_$_INSTANCE_METHODS_STSimpleScheduleListController
+ __OBJC_$_INSTANCE_VARIABLES_STSimpleScheduleListController
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.875
+ __OBJC_$_PROP_LIST_STSimpleScheduleListController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STCustomizeDailyScheduleListControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STSimpleScheduleListControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STCustomizeDailyScheduleListControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STSimpleScheduleListControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_STCustomizeDailyScheduleListControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_STSimpleScheduleListControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_STSimpleScheduleListController
+ __OBJC_CLASS_RO_$_STSimpleScheduleListController
+ __OBJC_LABEL_PROTOCOL_$_STCustomizeDailyScheduleListControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_STSimpleScheduleListControllerDelegate
+ __OBJC_METACLASS_RO_$_STSimpleScheduleListController
+ __OBJC_PROTOCOL_$_STCustomizeDailyScheduleListControllerDelegate
+ __OBJC_PROTOCOL_$_STSimpleScheduleListControllerDelegate
+ ___66-[STDeviceBedtimeListController _saveDowntimeAndReloadSpecifiers:]_block_invoke
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.739
+ ___block_descriptor_56_e8_32s40bs48w_e32_v16?0"NSManagedObjectContext"8lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e32_v16?0"NSManagedObjectContext"8ls32l8s48l8s40l8
+ ___block_literal_global.878
+ __swift_FORCE_LOAD_$_swiftCoreML
+ __swift_FORCE_LOAD_$_swiftCoreML_$_ScreenTimeSettingsUI
+ __unnamed_array_storage.181
+ _objc_msgSend$_saveDowntimeAndReloadSpecifiers:
+ _objc_msgSend$customizeDailyScheduleListController:didSaveDailySchedule:forWeekdayIndex:
+ _objc_msgSend$customizeDailyScheduleListControllerDidCancel:
+ _objc_msgSend$dailyScheduleSpecifier
+ _objc_msgSend$defaultSwitchSpecifierWithConfiguration:key:fallbackLabel:
+ _objc_msgSend$dictionary
+ _objc_msgSend$initWithSimpleSchedule:
+ _objc_msgSend$setDailyScheduleSpecifier:
+ _objc_msgSend$setSimpleSchedule:
+ _objc_msgSend$simpleScheduleGroupSpecifier
+ _objc_msgSend$simpleScheduleListController:didSaveSimpleSchedule:
+ _objc_msgSend$simpleScheduleListControllerDidCancel:
- -[STContentPrivacyMediaRestrictionsDetailController initWithCoder:]
- -[STContentPrivacyMediaRestrictionsDetailController initWithNibName:bundle:]
- -[STCustomizeDailyScheduleListController _didEndEditingDailySchedule:]
- -[STCustomizeDailyScheduleListController viewWillDisappear:]
- -[STCustomizeDailyScheduleListController willResignActive]
- -[STDeviceBedtimeListController _didEndEditingDailySchedule:]
- -[STDeviceBedtimeListController _didFinishEditingBedtime]
- -[STDeviceBedtimeListController _renderDeviceBedtimeSpecifierWithBedtime:]
- -[STDeviceBedtimeListController _showOrHidePickerSpecifierForSpecifier:]
- -[STDeviceBedtimeListController _simpleEndTime:]
- -[STDeviceBedtimeListController _simpleStartTime:]
- -[STDeviceBedtimeListController datePickerChanged:]
- -[STDeviceBedtimeListController datePickerForSpecifier:]
- -[STDeviceBedtimeListController datePickerForSpecifier:].cold.1
- -[STDeviceBedtimeListController delegate]
- -[STDeviceBedtimeListController endTimePickerSpecifier]
- -[STDeviceBedtimeListController endTimeSpecifier]
- -[STDeviceBedtimeListController isEditingSimple]
- -[STDeviceBedtimeListController selectedTimeSpecifier]
- -[STDeviceBedtimeListController setDelegate:]
- -[STDeviceBedtimeListController setEndTimePickerSpecifier:]
- -[STDeviceBedtimeListController setEndTimeSpecifier:]
- -[STDeviceBedtimeListController setIsEditingSimple:]
- -[STDeviceBedtimeListController setSelectedTimeSpecifier:]
- -[STDeviceBedtimeListController setStartTimePickerSpecifier:]
- -[STDeviceBedtimeListController setStartTimeSpecifier:]
- -[STDeviceBedtimeListController startTimePickerSpecifier]
- -[STDeviceBedtimeListController startTimeSpecifier]
- -[STDeviceBedtimeListController viewWillDisappear:]
- -[STDeviceBedtimeListController willResignActive]
- -[STLimitUsageGroupSpecifierProvider bedtimeListController:didFinishEditingBedtime:]
- GCC_except_table27
- _OBJC_IVAR_$_STDeviceBedtimeListController._delegate
- _OBJC_IVAR_$_STDeviceBedtimeListController._endTimePickerSpecifier
- _OBJC_IVAR_$_STDeviceBedtimeListController._endTimeSpecifier
- _OBJC_IVAR_$_STDeviceBedtimeListController._isEditingSimple
- _OBJC_IVAR_$_STDeviceBedtimeListController._selectedTimeSpecifier
- _OBJC_IVAR_$_STDeviceBedtimeListController._startTimePickerSpecifier
- _OBJC_IVAR_$_STDeviceBedtimeListController._startTimeSpecifier
- _OUTLINED_FUNCTION_6
- _STDidEndEditingDailyScheduleNotification
- _STNotificationKeyDailySchedule
- _STNotificationKeyResigningActive
- _STNotificationKeyWeekdayIndex
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.872
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_STDeviceBedtimeListControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_STDeviceBedtimeListControllerDelegate
- __OBJC_$_PROTOCOL_REFS_STDeviceBedtimeListControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_STDeviceBedtimeListControllerDelegate
- __OBJC_PROTOCOL_$_STDeviceBedtimeListControllerDelegate
- ___51-[STDeviceBedtimeListController datePickerChanged:]_block_invoke
- ___61-[STDeviceBedtimeListController setAskForMoreTime:specifier:]_block_invoke
- ___67-[STDeviceBedtimeListController setDeviceBedtimeEnabled:specifier:]_block_invoke
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.736
- ___84-[STLimitUsageGroupSpecifierProvider bedtimeListController:didFinishEditingBedtime:]_block_invoke
- ___84-[STLimitUsageGroupSpecifierProvider bedtimeListController:didFinishEditingBedtime:]_block_invoke.cold.1
- ___block_descriptor_72_e8_32s40s48s56bs_e32_v16?0"NSManagedObjectContext"8ls32l8s56l8s40l8s48l8
- ___block_literal_global.139
- ___block_literal_global.875
- __unnamed_array_storage.183
- _objc_msgSend$_didEndEditingDailySchedule:
- _objc_msgSend$_didFinishEditingBedtime
- _objc_msgSend$_renderDeviceBedtimeSpecifierWithBedtime:
- _objc_msgSend$bedtimeListController:didFinishEditingBedtime:
- _objc_msgSend$indexOfSpecifierID:
- _objc_msgSend$initWithObjectsAndKeys:
- _objc_msgSend$insertSpecifier:atIndex:
- _objc_msgSend$isEditingSimple
- _objc_msgSend$removeSpecifier:
- _objc_msgSend$setEndTimePickerSpecifier:
- _objc_msgSend$setEndTimeSpecifier:
- _objc_msgSend$setIsEditingSimple:
- _objc_msgSend$setStartTimePickerSpecifier:
- _objc_msgSend$setStartTimeSpecifier:
CStrings:
+ "\x1f\x04"
+ "!\x16"
+ "@\"<STCustomizeDailyScheduleListControllerDelegate>\""
+ "@\"<STSimpleScheduleListControllerDelegate>\""
+ "DeviceDowntimeDailyScheduleSpecifierName"
+ "DeviceDowntimeEditScheduleTitle"
+ "DeviceDowntimeScheduleDoneBarButtonItemTitle"
+ "Restrictions blueprint configuration payload not found for type %@"
+ "STCustomizeDailyScheduleListControllerDelegate"
+ "STSimpleScheduleListController"
+ "STSimpleScheduleListControllerDelegate"
+ "T@\"<STCustomizeDailyScheduleListControllerDelegate>\",W,N,V_delegate"
+ "T@\"<STSimpleScheduleListControllerDelegate>\",W,N,V_delegate"
+ "T@\"PSSpecifier\",&,N,V_dailyScheduleSpecifier"
+ "T@\"PSSpecifier\",R,V_simpleScheduleGroupSpecifier"
+ "User cancelled editing custom Downtime schedule"
+ "User cancelled editing simple Downtime schedule"
+ "User saved edited custom Downtime schedule"
+ "User saved edited simple Downtime schedule"
+ "_dailyScheduleSpecifier"
+ "_didTapShowThisWeekButton:"
+ "_didTapShowTodayButton:"
+ "_saveDowntimeAndReloadSpecifiers:"
+ "_showEditSimpleScheduleListController:"
+ "_simpleScheduleGroupSpecifier"
+ "_simpleScheduleTime:"
+ "customizeDailyScheduleListController:didSaveDailySchedule:forWeekdayIndex:"
+ "customizeDailyScheduleListControllerDidCancel:"
+ "dailyScheduleSpecifier"
+ "defaultSwitchSpecifierWithConfiguration:key:fallbackLabel:"
+ "dictionary"
+ "doneButtonTapped:"
+ "initWithSimpleSchedule:"
+ "restrictions blueprint configuration payload not found"
+ "setDailyScheduleSpecifier:"
+ "simpleScheduleGroupSpecifier"
+ "simpleScheduleListController:didSaveSimpleSchedule:"
+ "simpleScheduleListControllerDidCancel:"
+ "v24@0:8@\"STCustomizeDailyScheduleListController\"16"
+ "v24@0:8@\"STSimpleScheduleListController\"16"
+ "v32@0:8@\"STSimpleScheduleListController\"16@\"STBlueprintScheduleSimpleItem\"24"
+ "v40@0:8@\"STCustomizeDailyScheduleListController\"16@\"STBlueprintScheduleCustomDayItem\"24Q32"
+ "v40@0:8@16@24Q32"
- "\x11\x16"
- "/\b"
- "@\"<STDeviceBedtimeListControllerDelegate>\""
- "DailySchedule"
- "DidEndEditingDailySchedule"
- "ResigningActive"
- "STDeviceBedtimeListControllerDelegate"
- "STUI:: STCustomizeDailyScheduleListController.viewWillDisappear"
- "STUI:: STDeviceBedtimeListController.viewWillDisappear"
- "T@\"<STDeviceBedtimeListControllerDelegate>\",W,N,V_delegate"
- "T@\"PSSpecifier\",&,N,V_endTimePickerSpecifier"
- "T@\"PSSpecifier\",&,N,V_endTimeSpecifier"
- "T@\"PSSpecifier\",&,N,V_startTimePickerSpecifier"
- "T@\"PSSpecifier\",&,N,V_startTimeSpecifier"
- "TB,N,V_isEditingSimple"
- "WeekdayIndex"
- "_didEndEditingDailySchedule:"
- "_didFinishEditingBedtime"
- "_isEditingSimple"
- "_renderDeviceBedtimeSpecifierWithBedtime:"
- "_simpleEndTime:"
- "_simpleStartTime:"
- "bedtimeListController:didFinishEditingBedtime:"
- "failed to save bedtime: %{public}@"
- "indexOfSpecifierID:"
- "initWithObjectsAndKeys:"
- "insertSpecifier:atIndex:"
- "isEditingSimple"
- "removeSpecifier:"
- "setEndTimePickerSpecifier:"
- "setEndTimeSpecifier:"
- "setIsEditingSimple:"
- "setStartTimePickerSpecifier:"
- "setStartTimeSpecifier:"
- "v32@0:8@\"STDeviceBedtimeListController\"16@\"STDeviceBedtime\"24"

```
