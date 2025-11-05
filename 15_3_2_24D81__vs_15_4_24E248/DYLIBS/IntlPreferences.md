## IntlPreferences

> `/System/iOSSupport/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

```diff

-454.201.0.0.0
-  __TEXT.__text: 0x16524
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0xe10
+454.302.0.0.0
+  __TEXT.__text: 0x1711c
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x1004
   __TEXT.__const: 0x162
-  __TEXT.__cstring: 0x10c5
-  __TEXT.__oslogstring: 0xb3e
-  __TEXT.__gcc_except_tab: 0x124
+  __TEXT.__cstring: 0x1115
+  __TEXT.__oslogstring: 0xb96
+  __TEXT.__gcc_except_tab: 0x120
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x62
-  __TEXT.__unwind_info: 0x488
-  __TEXT.__objc_classname: 0x2a6
-  __TEXT.__objc_methname: 0x352b
+  __TEXT.__swift5_typeref: 0x5a
+  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__objc_classname: 0x2c2
+  __TEXT.__objc_methname: 0x362a
   __TEXT.__objc_methtype: 0x3f8
-  __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__objc_stubs: 0x2e80
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x518
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe18
+  __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_arraydata: 0x328
-  __AUTH_CONST.__auth_got: 0x560
+  __DATA_CONST.__objc_arraydata: 0x360
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x1728
+  __AUTH_CONST.__cfstring: 0x1a00
+  __AUTH_CONST.__objc_const: 0x14e8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x280
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x140
+  __DATA.__data: 0x178
+  __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F212BA41-0A55-39A6-8826-4F53BF190E58
-  Functions: 355
-  Symbols:   1243
-  CStrings:  1106
+  UUID: B055B684-083E-310A-88AF-D5E8DC174AD5
+  Functions: 379
+  Symbols:   1292
+  CStrings:  1125
 
Symbols:
+ +[IPFoundationNamePreferenceInfoProvider canonicalKeyToValueIdentifierToNumericValueMap].cold.1
+ +[IPFoundationNamePreferenceInfoProvider nativeKeyNameToCanonicalKeyName].cold.1
+ +[IPOSXABNamePreferenceInfoProvider canonicalKeyToValueIdentifierToNumericValueMap].cold.1
+ +[IPOSXABNamePreferenceInfoProvider nativeKeyNameToCanonicalKeyName].cold.1
+ +[IPiOSABNamePreferenceInfoProvider canonicalKeyToValueIdentifierToNumericValueMap].cold.1
+ +[IPiOSABNamePreferenceInfoProvider nativeKeyNameToCanonicalKeyName].cold.1
+ +[IntlUtility _getXPCConnectionForLocalizationSwitcher].cold.1
+ +[IntlUtility _lunarCalendarData]
+ +[IntlUtility _lunarCalendars]
+ +[IntlUtility alternateContinentOfRegion:].cold.1
+ +[IntlUtility localeForCalendarID:andLocale:preferredLanguages:]
+ +[IntlUtility sharedIntlUtility].cold.1
+ +[IntlUtility stdLanguageIDs].cold.1
+ +[NSLocale(IntlPreferencesAdditions) renderableLocaleLanguages].cold.1
+ +[NSLocale(IntlPreferencesAdditions) renderableUILanguages].cold.1
+ -[IP_scriptSelection_migrator performMigrationForPreferences:]
+ -[NSLocale(IntlPreferencesAdditions) preferenceKeysForSelectableScripts]
+ -[NSLocale(IntlPreferencesAdditions) selectableScriptCodes].cold.1
+ -[NSLocale(IntlPreferencesAdditions) selectedScript]
+ -[NSLocale(IntlPreferencesAdditions) setSelectedScript:]
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table79
+ IPLoadUIKitFramework.cold.1
+ IPUIKeyboardCanonicalInputModeName.cold.1
+ IPUIKeyboardInputModeController.cold.1
+ IPUIKeyboardInputModeGetBaseLanguage.cold.1
+ IPUIKeyboardInputModeGetIdentifierWithKeyboardLayouts.cold.1
+ IPUIKeyboardInputModeGetLanguageWithRegion.cold.1
+ IPUIKeyboardInputModeGetNormalizedIdentifier.cold.1
+ IPUIKeyboardInputMode_Intl.cold.1
+ IPUIKeyboardPreferencesController.cold.1
+ MigrationLogger.cold.1
+ _IPAppleLanguagesSchemaVersionCrystalglowE
+ _OBJC_CLASS_$_IP_scriptSelection_migrator
+ _OBJC_METACLASS_$_IP_scriptSelection_migrator
+ __33+[IntlUtility _lunarCalendarData]_block_invoke.cold.1
+ __46+[IntlUtility preferredLanguagesForBundleIDs:]_block_invoke.246
+ __OBJC_$_INSTANCE_METHODS_IP_scriptSelection_migrator
+ __OBJC_CLASS_RO_$_IP_scriptSelection_migrator
+ __OBJC_METACLASS_RO_$_IP_scriptSelection_migrator
+ ___30+[IntlUtility _lunarCalendars]_block_invoke
+ ___33+[IntlUtility _lunarCalendarData]_block_invoke
+ ___62-[IP_scriptSelection_migrator performMigrationForPreferences:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8
+ __block_literal_global.269
+ __os_feature_enabled_impl
+ _lunarCalendarData.__lunarCalendarData
+ _lunarCalendarData.__onceToken
+ _lunarCalendars.__lunarCalendars
+ _lunarCalendars.__onceToken
+ _objc_msgSend$_lunarCalendarData
+ _objc_msgSend$_lunarCalendars
+ _objc_msgSend$localeForCalendarID:andLocale:preferredLanguages:
+ _objc_msgSend$mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:
+ _objc_msgSend$preferenceKeysForSelectableScripts
+ _objc_msgSend$selectableScriptCodes
+ _objc_msgSend$selectedScript
- GCC_except_table15
- GCC_except_table20
- GCC_except_table75
- __41+[IntlUtility lunarCalendarsForLocaleID:]_block_invoke.61
- __46+[IntlUtility preferredLanguagesForBundleIDs:]_block_invoke.245
- __block_literal_global.268
- _symbolic _____Sg 10Foundation6LocaleV
- lunarCalendarsForLocaleID:.onceToken
- lunarCalendarsForLocaleID:.sLunarCalendarList
CStrings:
+ "%@_%@"
+ "%s: %{public}@ set to %{public}@. Writing to disk."
+ "AppleScriptPreference_"
+ "HinduCalendar"
+ "IP_scriptSelection_migrator"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSString\",C"
+ "Unable to load Lunar Calendars plist"
+ "_lunarCalendarData"
+ "_lunarCalendars"
+ "localeForCalendarID:andLocale:preferredLanguages:"
+ "mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:"
+ "preferenceKeysForSelectableScripts"
+ "restrictToPreferredLanguages"
+ "selectedScript"
+ "setSelectedScript:"
- "zh-HK"

```
