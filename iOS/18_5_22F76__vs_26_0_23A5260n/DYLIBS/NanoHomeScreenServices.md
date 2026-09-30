## NanoHomeScreenServices

> `/System/Library/PrivateFrameworks/NanoHomeScreenServices.framework/NanoHomeScreenServices`

```diff

-15.9.0.0.0
-  __TEXT.__text: 0x32a8
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0x72
-  __TEXT.__cstring: 0x4d1
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__oslogstring: 0x281
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0xf54
-  __TEXT.__objc_methtype: 0x1cb
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x30
+131.0.0.0.0
+  __TEXT.__text: 0x4e74
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x544
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x621
+  __TEXT.__oslogstring: 0x3bf
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__swift5_typeref: 0x8
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_classname: 0xac
+  __TEXT.__objc_methname: 0x1360
+  __TEXT.__objc_methtype: 0x1ef
+  __TEXT.__objc_stubs: 0xae0
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d0
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x8e8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x50
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_selrefs: 0x480
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x840
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x158
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/RelevanceKit.framework/RelevanceKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
-  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8EE567D0-2A07-3A87-9C27-151C4FA8577C
-  Functions: 115
-  Symbols:   550
-  CStrings:  273
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 1D036820-DE52-346C-B24D-553AEA14BD46
+  Functions: 151
+  Symbols:   607
+  CStrings:  318
 
Symbols:
+ -[NHSSPartialWidgetDescriptor initWithContainerBundleIdentifier:extensionBundleIdentifier:kind:]
+ -[NHSSSmartStackSuggestionDefaults _cleanUpExpiredMuteHintPreferences]
+ -[NHSSSmartStackSuggestionDefaults _mainQueue_notifyObserversDefaultsHintDidChange]
+ -[NHSSSmartStackSuggestionDefaults _scheduleTimerToUnmuteHintForKey:onDate:]
+ -[NHSSSmartStackSuggestionDefaults _scheduleTimersToUnmuteHints]
+ -[NHSSSmartStackSuggestionDefaults addHintObserver:]
+ -[NHSSSmartStackSuggestionDefaults defaultMuteHintAfterIgnoredDuration]
+ -[NHSSSmartStackSuggestionDefaults defaultMuteHintForHourDuration]
+ -[NHSSSmartStackSuggestionDefaults defaultMuteHintForTodayDuration]
+ -[NHSSSmartStackSuggestionDefaults diagnosticDictionaryRepresentation]
+ -[NHSSSmartStackSuggestionDefaults domainAccessorForReads]
+ -[NHSSSmartStackSuggestionDefaults domainAccessorForReads].cold.1
+ -[NHSSSmartStackSuggestionDefaults enabledDictionaryValueWithIdentifier:onDomainObjectWithKey:]
+ -[NHSSSmartStackSuggestionDefaults hintUnmuteDateForContainerBundleIdentifier:extensionBundleIdentifier:kind:]
+ -[NHSSSmartStackSuggestionDefaults presentSmartStackFromHintAlertAcknowledged]
+ -[NHSSSmartStackSuggestionDefaults removeHintObserver:]
+ -[NHSSSmartStackSuggestionDefaults setHintUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:]
+ -[NHSSSmartStackSuggestionDefaults setNPSSyncedBoolEnabledValue:forDomainObjectKey:]
+ -[NHSSSmartStackSuggestionDefaults setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:]
+ -[NHSSSmartStackSuggestionDefaults setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:].cold.1
+ -[NHSSSmartStackSuggestionDefaults setPresentSmartStackFromHintAlertAcknowledged:]
+ -[NHSSSmartStackSuggestionDefaults setSuggestionsShowHintEnabled:]
+ -[NHSSSmartStackSuggestionDefaults smartStackNPSSuggestionsDefaultsDidChange]
+ -[NHSSSmartStackSuggestionDefaults suggestionsShowHintEnabled]
+ GCC_except_table41
+ GCC_except_table53
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_IVAR_$_NHSSSmartStackSuggestionDefaults._isClockFaceProcess
+ _OBJC_IVAR_$_NHSSSmartStackSuggestionDefaults._isInternalBuild
+ _OBJC_IVAR_$_NHSSSmartStackSuggestionDefaults._lock_hintObservers
+ _OBJC_IVAR_$_NHSSSmartStackSuggestionDefaults._lock_scheduledHintTimers
+ _OBJC_IVAR_$_NHSSSmartStackSuggestionDefaults._queue
+ _OUTLINED_FUNCTION_0
+ __HintContext
+ __NHSSmartStackSuggestionsDefaultsChangeHandler
+ ___154-[NHSSSmartStackSuggestionDefaults setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:]_block_invoke
+ ___154-[NHSSSmartStackSuggestionDefaults setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:]_block_invoke.cold.1
+ ___64-[NHSSSmartStackSuggestionDefaults _scheduleTimersToUnmuteHints]_block_invoke
+ ___76-[NHSSSmartStackSuggestionDefaults _scheduleTimerToUnmuteHintForKey:onDate:]_block_invoke
+ ___77-[NHSSSmartStackSuggestionDefaults smartStackNPSSuggestionsDefaultsDidChange]_block_invoke
+ ___83-[NHSSSmartStackSuggestionDefaults observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_value_buffer
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_NanoHomeScreenServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_NanoHomeScreenServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_NanoHomeScreenServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_NanoHomeScreenServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_NanoHomeScreenServices
+ _asprintf
+ _free
+ _malloc
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cleanUpExpiredMuteHintPreferences
+ _objc_msgSend$_mainQueue_notifyObserversDefaultsHintDidChange
+ _objc_msgSend$_scheduleTimerToUnmuteHintForKey:onDate:
+ _objc_msgSend$_scheduleTimersToUnmuteHints
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$count
+ _objc_msgSend$domainAccessorForReads
+ _objc_msgSend$enabledDictionaryValueWithIdentifier:onDomainObjectWithKey:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$setNPSSyncedBoolEnabledValue:forDomainObjectKey:
+ _objc_msgSend$setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:
+ _objc_msgSend$smartStackNPSSuggestionsDefaultsDidChange
+ _objc_msgSend$smartStackSuggestionDefaultsHintDidChange
+ _objc_msgSend$stringWithUTF8String:
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _swift_coroFrameAlloc
+ _swift_getTypeByMangledNameInContext2
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _symbolic _____Sg 10Foundation4DateV
- +[NHSSUserPreferences sharedInstance]
- +[NHSSUserPreferences sharedInstance].cold.1
- -[NHSSPartialWidgetDescriptor setContainerBundleIdentifier:]
- -[NHSSPartialWidgetDescriptor setExtensionBundleIdentifier:]
- -[NHSSPartialWidgetDescriptor setKind:]
- -[NHSSUserPreferences .cxx_destruct]
- -[NHSSUserPreferences init]
- -[NHSSUserPreferences rotationEnabled]
- -[NHSSUserPreferences setRotationEnabled:]
- GCC_except_table25
- _NHSSUserPreferencesRotationEnabledKey
- _NHSSUserPreferencesSuggestionsEnabledKey
- _OBJC_CLASS_$_NHSSUserPreferences
- _OBJC_IVAR_$_NHSSUserPreferences._defaults
- _OBJC_METACLASS_$_NHSSUserPreferences
- __OBJC_$_CLASS_METHODS_NHSSUserPreferences
- __OBJC_$_CLASS_PROP_LIST_NHSSUserPreferences
- __OBJC_$_INSTANCE_METHODS_NHSSUserPreferences
- __OBJC_$_INSTANCE_VARIABLES_NHSSUserPreferences
- __OBJC_$_PROP_LIST_NHSSUserPreferences
- __OBJC_CLASS_RO_$_NHSSUserPreferences
- __OBJC_METACLASS_RO_$_NHSSUserPreferences
- ___37+[NHSSUserPreferences sharedInstance]_block_invoke
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_NanoHomeScreenServices
- _objc_msgSend$_requestUserDefaultsSyncForKey:
- _objc_msgSend$boolForKey:
- _objc_msgSend$setBool:forKey:
- _objc_msgSend$stringWithFormat:
- _objc_retain_x5
- _objc_setProperty_nonatomic_copy
- _sharedInstance.instance
CStrings:
+ "%s-%s-%s"
+ "B"
+ "B32@0:8@16@24"
+ "Existing unmute date is after proposed unmute date; keep existing unmute date."
+ "T@\"NSArray\",C,N"
+ "T@\"NSString\",R,C,N,V_containerBundleIdentifier"
+ "T@\"NSString\",R,C,N,V_extensionBundleIdentifier"
+ "T@\"NSString\",R,C,N,V_kind"
+ "UTF8String"
+ "Unable to get Suggestion Defaults domainAccessor"
+ "Unable to get Suggestion Defaults domainAccessor for reads"
+ "User is muting permission prompt. Has already dismissed once? %{bool,public}d."
+ "_cleanUpExpiredMuteHintPreferences"
+ "_isClockFaceProcess"
+ "_isInternalBuild"
+ "_lock_hintObservers"
+ "_lock_scheduledHintTimers"
+ "_mainQueue_notifyObserversDefaultsHintDidChange"
+ "_scheduleTimerToUnmuteHintForKey:onDate:"
+ "_scheduleTimersToUnmuteHints"
+ "addHintObserver:"
+ "apple-internal-install"
+ "bundleIdentifier"
+ "com.apple.NanoHomeScreen.SmartStackSuggestionDefaults.syncQueue"
+ "com.apple.NanoHomeScreen.SmartStackSuggestionsChanged"
+ "com.apple.clockface"
+ "count"
+ "defaultMuteHintAfterIgnoredDuration"
+ "defaultMuteHintForHourDuration"
+ "defaultMuteHintForTodayDuration"
+ "diagnosticDictionaryRepresentation"
+ "domainAccessorForReads"
+ "enabledDictionaryValueWithIdentifier:onDomainObjectWithKey:"
+ "hintUnmuteDateForContainerBundleIdentifier:extensionBundleIdentifier:kind:"
+ "initWithContainerBundleIdentifier:extensionBundleIdentifier:kind:"
+ "isEqualToString:"
+ "mainBundle"
+ "muteHint"
+ "no object key to write so bailing now"
+ "persistentDomainForName:"
+ "presentSmartStackFromHintAlertAcknowledged"
+ "removeHintObserver:"
+ "setHintUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:"
+ "setNPSSyncedBoolEnabledValue:forDomainObjectKey:"
+ "setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:"
+ "setPresentSmartStackFromHintAlertAcknowledged:"
+ "setSuggestionsShowHintEnabled:"
+ "showHint"
+ "smartStackNPSSuggestionsDefaultsDidChange"
+ "smartStackSuggestionDefaultsHintDidChange"
+ "soundDetectionButton"
+ "stringWithUTF8String:"
+ "suggestionsShowHintEnabled"
+ "v40@0:8B16@20@28B36"
- "%@-%@-%@"
- "NHSSUserPreferences"
- "RotationEnabled"
- "SuggestionsEnabled"
- "T@\"NHSSUserPreferences\",R,N"
- "T@\"NSArray\",&,N"
- "T@\"NSString\",C,N,V_containerBundleIdentifier"
- "T@\"NSString\",C,N,V_extensionBundleIdentifier"
- "T@\"NSString\",C,N,V_kind"
- "_defaults"
- "boolForKey:"
- "rotationEnabled"
- "setBool:forKey:"
- "setContainerBundleIdentifier:"
- "setExtensionBundleIdentifier:"
- "setKind:"
- "setRotationEnabled:"
- "stringWithFormat:"

```
