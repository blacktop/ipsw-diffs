## IntelligentCallScreeningSettingsBundle

> `/System/Library/PreferenceBundles/IntelligentCallScreeningSettingsBundle.bundle/IntelligentCallScreeningSettingsBundle`

```diff

-3018.100.11.2.7
-  __TEXT.__text: 0x9dc
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0x11a
+3021.100.15.1.5
+  __TEXT.__text: 0xef4
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__objc_methname: 0x517
+  __TEXT.__cstring: 0x21f
+  __TEXT.__objc_classname: 0x60
+  __TEXT.__objc_methtype: 0xb8
   __TEXT.__const: 0x8
-  __TEXT.__objc_methname: 0x56b
-  __TEXT.__oslogstring: 0x148
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methtype: 0x123
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__cfstring: 0xc0
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__oslogstring: 0x1dc
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2a0
-  __DATA.__objc_selrefs: 0x1d0
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x30
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x210
+  __DATA.__objc_selrefs: 0x168
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0xa0
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABEC4188-9901-31CB-BA1C-9A921532FCD0
-  Functions: 26
-  Symbols:   62
-  CStrings:  114
+  UUID: 7D0E7A2D-6B2A-350F-90BA-4B7D63AB70D9
+  Functions: 38
+  Symbols:   73
+  CStrings:  99
 
Symbols:
+ _OBJC_CLASS_$_IntelligentCallScreeningSettingsController
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_PSSubtitleButtonCell
+ _OBJC_METACLASS_$_IntelligentCallScreeningSettingsController
+ _PSIsRadioGroupKey
+ _PSRadioGroupCheckedSpecifierKey
+ ___kCFBooleanTrue
+ _kIntelligentCallScreeningSettingsBundleControllerAskExplanation
+ _kIntelligentCallScreeningSettingsBundleControllerAskTitle
+ _kIntelligentCallScreeningSettingsBundleControllerMenuTitle
+ _kIntelligentCallScreeningSettingsBundleControllerNeverExplanation
+ _kIntelligentCallScreeningSettingsBundleControllerNeverTitle
+ _kIntelligentCallScreeningSettingsBundleControllerSilenceExplanation
+ _kIntelligentCallScreeningSettingsBundleControllerSilenceTitle
+ _kIntelligentCallScreeningSettingsUserDidModifySelectionNotification
+ _objc_enumerationMutation
+ _objc_opt_self
+ _objc_release_x24
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retain_x20
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_PSMultilineSubtitleSwitchTableViewCell
- _TUBundleIdentifierTelephonyUtilitiesFramework
- _TUReceptionistDisabledKey
- _kIntelligentCallScreeningSettingsBundleControllerExplanation
- _kIntelligentCallScreeningSettingsBundleControllerSpecifierIdentifier
- _kIntelligentCallScreeningSettingsBundleControllerToggleTitle
- _kIntelligentCallScreeningSettingsChangedNotification
- _objc_alloc
- _objc_retain_x19
- _objc_retain_x3
CStrings:
+ "@\"IntelligentCallScreeningSettingsController\""
+ "@\"NSArray\""
+ "INTELLIGENT CALL SCREENING SETTINGS: User selected option %ld from kIntelligentCallScreeningSettingsUserDidModifySelectionNotification"
+ "INTELLIGENT CALL SCREENING SETTINGS: We are NOT in Phone Settings with receptionist available, so we will NOT show Intelligent Call Screening group, we must show Silence Unknown Callers toggle instead"
+ "INTELLIGENT CALL SCREENING SETTINGS: We are in Phone Settings with receptionist available, so we will show Intelligent Call Screening group"
+ "INTELLIGENT_CALL_SCREENING_MENU_TITLE"
+ "INTELLIGENT_CALL_SCREENING_OPTION_ASK_EXPLANATION"
+ "INTELLIGENT_CALL_SCREENING_OPTION_ASK_TITLE"
+ "INTELLIGENT_CALL_SCREENING_OPTION_NEVER_EXPLANATION"
+ "INTELLIGENT_CALL_SCREENING_OPTION_NEVER_TITLE"
+ "INTELLIGENT_CALL_SCREENING_OPTION_SILENCE_EXPLANATION"
+ "INTELLIGENT_CALL_SCREENING_OPTION_SILENCE_TITLE"
+ "IntelligentCallScreeningSettingsBundle"
+ "IntelligentCallScreeningSettingsController"
+ "IntelligentCallScreeningSettingsUserDidModifySelectionNotification"
+ "T@\"IntelligentCallScreeningSettingsController\",R,N,V_controller"
+ "T@\"NSArray\",&,N,V_specifiers"
+ "T@\"TUFeatureFlags\",R,N,V_featureFlags"
+ "_controller"
+ "_featureFlags"
+ "_specifiers"
+ "arrayWithObjects:count:"
+ "controller"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "featureFlags"
+ "getOptionExplanationKeys"
+ "getOptionTitleKeys"
+ "getSelectedIntelligentCallScreeningMenuOptionForPhone"
+ "getSpecifiers"
+ "groupSpecifierWithName:"
+ "init"
+ "integerValue"
+ "isEqualToString:"
+ "isIntelligentCallScreeningOptionIdentifier:"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "optionExplanationKeys"
+ "optionTitleKeys"
+ "propertyForKey:"
+ "q16@0:8"
+ "setSelectedCallScreeningOption:specifier:"
+ "setSelectedIntelligentCallScreeningMenuOptionForPhone:"
+ "setSpecifiers:"
+ "specifier"
+ "specifiers"
+ "userInfo"
+ "v24@0:8q16"
+ "value"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@\"PSSpecifier\""
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "INTELLIGENT_CALL_SCREENING"
- "INTELLIGENT_CALL_SCREENING_EXPLANATION"
- "INTELLIGENT_CALL_SCREENING_TOGGLE_TITLE"
- "IntelligentCallScreeningSettings"
- "IntelligentCallScreeningSettingsChangedNotification"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"PSSpecifier\",&,N,V_activeSpecifier"
- "T@\"TUFeatureFlags\",R,N,V_tuFeatureFlags"
- "TQ,R"
- "TUConfigurationProviderDelegate"
- "User device does not FF criteria or switch has already been added, so we are not adding Intelligent Call Screening (AKA Receptionist) switch to Settings"
- "User device meets FF criteria, adding Intelligent Call Screening (AKA Receptionist) switch to Settings"
- "User toggled Intelligent Call Screening (AKA Receptionist) switch to %@"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activeSpecifier"
- "_tuFeatureFlags"
- "activeSpecifier"
- "autorelease"
- "boolValue"
- "class"
- "configurationChanged"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "deviceExpertMigrationEnabled"
- "getBooleanFromUserDefaults:default:"
- "getIntelligentCallScreeningEnabled:"
- "hash"
- "i"
- "initWithSuiteName:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "numberWithInt:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "refreshView"
- "release"
- "reloadSpecifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setActiveSpecifier:"
- "setDelegate:"
- "setIntelligentCallScreeningEnabled:specifier:"
- "setReceptionistEnabled:"
- "setValue:forKey:"
- "setValueInUserDefaults:forKey:"
- "superclass"
- "tuFeatureFlags"
- "zone"

```
