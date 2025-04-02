## ScreenTimeSettings

> `/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings`

```diff

-537.4.20.1.0
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x48
+537.5.2.0.0
+  __TEXT.__text: 0x90c
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0xbc
+  __TEXT.__const: 0x58
+  __TEXT.__objc_methname: 0x395
+  __TEXT.__cstring: 0xca
+  __TEXT.__oslogstring: 0x69
+  __TEXT.__objc_classname: 0x29
+  __TEXT.__objc_methtype: 0x85
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x148
+  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x50
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI
   - /usr/lib/libSystem.B.dylib
-  Functions: 0
-  Symbols:   0
-  CStrings:  0
+  - /usr/lib/libobjc.A.dylib
+  Functions: 18
+  Symbols:   53
+  CStrings:  67
 
Symbols:
+ OBJC_IVAR_$_PSListController._specifiers
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PSListController
+ _OBJC_CLASS_$_PSSpecifier
+ _OBJC_CLASS_$_STAdminPersistenceController
+ _OBJC_CLASS_$_STCoreUser
+ _OBJC_CLASS_$_STCustomNotificationSettingsController
+ _OBJC_CLASS_$_STLog
+ _OBJC_CLASS_$_STScreenTimeSettingsUIBundle
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_PSListController
+ _OBJC_METACLASS_$_STCustomNotificationSettingsController
+ _STUserDefaultsKeyIsPasscodeUseNotificationDisabled
+ _STUserDefaultsKeyIsWeeklyReportNotificationDisabled
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ ___CFConstantStringClassReference
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __objc_empty_cache
+ __os_feature_enabled_impl
+ __os_log_error_impl
+ __os_log_impl
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_getProperty
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_storeStrong
+ _os_log_type_enabled
+ radr://5614542
CStrings:
+ "\x12"
+ ".cxx_destruct"
+ "@\"NSUserDefaults\""
+ "@\"STPersistenceController\""
+ "@16@0:8"
+ "@24@0:8@16"
+ "@32@0:8@16@24"
+ "AllowNotificationsGroupSpecifierName"
+ "B"
+ "B16@0:8"
+ "Failed to load custom notification settings: %{public}@"
+ "STCustomNotificationSettingsController"
+ "ScreenTime"
+ "ScreenTimePasscodeUseNotificationSpecifierName"
+ "Successfully loaded custom notification settings"
+ "T@\"NSUserDefaults\",R"
+ "T@\"NSUserDefaults\",R,V_userDefaults"
+ "T@\"STPersistenceController\",R,V_persistenceController"
+ "TB,V_isParent"
+ "WeeklyReportNotificationSpecifierName"
+ "_createSpecifierWithNameKey:userDefaultsKey:"
+ "_isNotificationEnabled:"
+ "_isParent"
+ "_persistenceController"
+ "_setIsNotificationEnabled:specifier:"
+ "_userDefaults"
+ "addObject:"
+ "addOperationWithBlock:"
+ "boolForKey:"
+ "boolValue"
+ "bundle"
+ "com.apple.ScreenTimeAgent"
+ "copy"
+ "fetchLocalUserInContext:error:"
+ "groupSpecifierWithName:"
+ "identifier"
+ "init"
+ "initWithCapacity:"
+ "initWithNibName:bundle:"
+ "initWithPersistenceController:userDefaults:"
+ "initWithSuiteName:"
+ "isParent"
+ "loadCustomSettingsWithCompletionHandler:"
+ "localizedStringForKey:value:table:"
+ "mainQueue"
+ "newBackgroundContext"
+ "numberWithInt:"
+ "passcode_activity"
+ "performBlock:"
+ "persistenceController"
+ "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
+ "reloadSpecifiers"
+ "screenTimeAgentDefaults"
+ "setBool:forKey:"
+ "setIdentifier:"
+ "setIsParent:"
+ "sharedController"
+ "specifiers"
+ "userDefaults"
+ "userNotifications"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8B16"
+ "v24@0:8@?16"
+ "v32@0:8@16@24"
+ "v8@?0"
+ "viewDidLoad"

```
