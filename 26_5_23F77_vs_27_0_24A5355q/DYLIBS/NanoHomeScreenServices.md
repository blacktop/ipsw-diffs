## NanoHomeScreenServices

> `/System/Library/PrivateFrameworks/NanoHomeScreenServices.framework/NanoHomeScreenServices`

```diff

-171.1.30.0.0
-  __TEXT.__text: 0x51cc
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x544
-  __TEXT.__const: 0x82
-  __TEXT.__cstring: 0x621
-  __TEXT.__oslogstring: 0x3bf
+306.1.0.0.0
+  __TEXT.__text: 0x4e3c
+  __TEXT.__objc_methlist: 0x62c
+  __TEXT.__const: 0x7a
+  __TEXT.__cstring: 0x6ca
+  __TEXT.__oslogstring: 0x408
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__swift5_typeref: 0x8
   __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x1360
-  __TEXT.__objc_methtype: 0x1ef
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x480
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x840
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x158
+  __DATA_CONST.__objc_selrefs: 0x4d8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0x110
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x900
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x130
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/RelevanceKit.framework/RelevanceKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswiftos.dylib
-  UUID: E9A5552D-E927-3D14-B139-9C916CBC0DCA
-  Functions: 156
-  Symbols:   603
-  CStrings:  318
+  UUID: 91FA0CB3-172B-3D27-B8BE-21BBD828184D
+  Functions: 167
+  Symbols:   660
+  CStrings:  114
 
Symbols:
+ +[NHSSSimulationDefaults sharedInstance]
+ +[NHSSSimulationDefaults sharedInstance].cold.1
+ -[NHSSSimulationDefaults .cxx_destruct]
+ -[NHSSSimulationDefaults _mainQueue_notifyObserversDefaultsDidChange]
+ -[NHSSSimulationDefaults _observeChangesToSimulationDefaults]
+ -[NHSSSimulationDefaults addObserver:]
+ -[NHSSSimulationDefaults allowsUserConfiguredItems]
+ -[NHSSSimulationDefaults clearSimulationWithCompletion:]
+ -[NHSSSimulationDefaults clearSimulation]
+ -[NHSSSimulationDefaults elements]
+ -[NHSSSimulationDefaults init]
+ -[NHSSSimulationDefaults isActive]
+ -[NHSSSimulationDefaults removeObserver:]
+ -[NHSSSimulationDefaults setElements:allowsUserConfiguredItems:]
+ -[NHSSSimulationDefaults setElements:allowsUserConfiguredItems:completion:]
+ -[NHSSSimulationDefaults simulationDefaultsDidChange]
+ -[NHSSSmartStackSuggestionDefaults persistSuggestionsAfterInteraction]
+ -[NHSSSmartStackSuggestionDefaults persistSuggestionsAfterInteraction].cold.1
+ -[NHSSSmartStackSuggestionDefaults setPersistSuggestionsAfterInteraction:]
+ -[NHSSSmartStackSuggestionDefaults waitForPendingWrites]
+ GCC_except_table45
+ GCC_except_table57
+ _OBJC_CLASS_$_NHSSSimulationDefaults
+ _OBJC_IVAR_$_NHSSSimulationDefaults._lock
+ _OBJC_IVAR_$_NHSSSimulationDefaults._lock_observers
+ _OBJC_IVAR_$_NHSSSimulationDefaults._queue
+ _OBJC_METACLASS_$_NHSSSimulationDefaults
+ __NHSSSimulationDefaultsChangeHandler
+ __OBJC_$_CLASS_METHODS_NHSSSimulationDefaults
+ __OBJC_$_CLASS_PROP_LIST_NHSSSimulationDefaults
+ __OBJC_$_INSTANCE_METHODS_NHSSSimulationDefaults
+ __OBJC_$_INSTANCE_VARIABLES_NHSSSimulationDefaults
+ __OBJC_$_PROP_LIST_NHSSSimulationDefaults
+ __OBJC_CLASS_RO_$_NHSSSimulationDefaults
+ __OBJC_METACLASS_RO_$_NHSSSimulationDefaults
+ ___40+[NHSSSimulationDefaults sharedInstance]_block_invoke
+ ___53-[NHSSSimulationDefaults simulationDefaultsDidChange]_block_invoke
+ ___56-[NHSSSimulationDefaults clearSimulationWithCompletion:]_block_invoke
+ ___56-[NHSSSimulationDefaults clearSimulationWithCompletion:]_block_invoke.cold.1
+ ___56-[NHSSSmartStackSuggestionDefaults waitForPendingWrites]_block_invoke
+ ___75-[NHSSSimulationDefaults setElements:allowsUserConfiguredItems:completion:]_block_invoke
+ ___75-[NHSSSimulationDefaults setElements:allowsUserConfiguredItems:completion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_literal_global.69
+ __os_log_debug_impl
+ _dispatch_assert_queue_not$V2
+ _dispatch_sync
+ _notify_post
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_observeChangesToSimulationDefaults
+ _objc_msgSend$clearSimulationWithCompletion:
+ _objc_msgSend$setElements:allowsUserConfiguredItems:completion:
+ _objc_msgSend$simulationDefaultsDidChange
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- GCC_except_table41
- GCC_except_table53
- _NSGenericException
- _OBJC_CLASS_$_NSException
- _OUTLINED_FUNCTION_2
- __OBJC_$_PROP_LIST_NHSSSmartStackSuggestionDefaults
- ___chkstk_darwin
- ___swift_allocate_value_buffer
- ___swift_instantiateConcreteTypeFromMangledNameV2
- ___swift_project_value_buffer
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_NanoHomeScreenServices
- __swift_FORCE_LOAD_$_swiftos
- __swift_FORCE_LOAD_$_swiftos_$_NanoHomeScreenServices
- _objc_msgSend$defaultMuteForTodayDuration
- _objc_msgSend$raise:format:
- _objc_msgSend$setSoundDetectionButtonDismissedOnce:
- _objc_msgSend$setWidgetSuggestionsUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:
- _objc_msgSend$soundDetectionButtonDismissedOnce
- _objc_msgSend$widgetSuggestionsUnmuteDateForContainerBundleIdentifier:extensionBundleIdentifier:kind:
- _objc_retainAutoreleasedReturnValue
- _swift_coroFrameAlloc
- _swift_getTypeByMangledNameInContext2
- _swift_once
- _swift_slowAlloc
- _swift_slowDealloc
- _symbolic _____Sg 10Foundation4DateV
CStrings:
+ "NHSSSimulationDefaults: Unable to clear simulation, gizmo must be paired and active"
+ "NHSSSimulationDefaults: Unable to set elements, gizmo must be paired and active"
+ "NO"
+ "YES"
+ "active"
+ "allowsUserConfiguredItems"
+ "com.apple.NanoHomeScreen.SmartStackSuggestionsNPSChanged"
+ "com.apple.NanoSmartStack.SimulationDefaults.syncQueue"
+ "com.apple.NanoSmartStack.SmartStackSimulation"
+ "com.apple.NanoSmartStack.SmartStackSimulationChanged"
+ "elements"
+ "persistSuggestionsAfterInteraction"
+ "persistSuggestionsAfterInteraction: storedValue=%{public}@, returning=%{public}s"
- ".cxx_destruct"
- "@\"NSBundle\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@40@0:8@16@24@32"
- "@56@0:8@16@24@32q40q48"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8@16@24@32"
- "Existing unmute date is after proposed unmute date; keep existing unmute date."
- "NHSSPartialWidgetDescriptor"
- "NHSSPrivacyDefaults"
- "NHSSRelevantWidget"
- "NHSSRelevantWidgetDefaults"
- "NHSSSmartStackSuggestionDefaults"
- "NHSSSmartStackSuggestionDefaults is unsupported on companion"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q16@0:8"
- "T@\"NHSSPrivacyDefaults\",R,N"
- "T@\"NHSSRelevantWidgetDefaults\",R,N"
- "T@\"NHSSSmartStackSuggestionDefaults\",R,N"
- "T@\"NSArray\",C,N"
- "T@\"NSString\",R,C,N,V_containerBundleIdentifier"
- "T@\"NSString\",R,C,N,V_extensionBundleIdentifier"
- "T@\"NSString\",R,C,N,V_kind"
- "T@\"NSString\",R,N,V_appBundleIdentifier"
- "T@\"NSString\",R,N,V_extensionBundleIdentifier"
- "T@\"NSString\",R,N,V_widgetKind"
- "TB,N"
- "TB,R"
- "Td,R,N"
- "Tq,N"
- "Tq,R,N,V_confidenceCategory"
- "Tq,R,N,V_intentIndexingHash"
- "UTF8String"
- "User is muting permission prompt. Has already dismissed once? %{bool,public}d."
- "_appBundleIdentifier"
- "_bundle"
- "_cleanUpExpiredMuteHintPreferences"
- "_cleanUpExpiredMutePreferences"
- "_compositeKeyWithContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "_confidenceCategory"
- "_containerBundleIdentifier"
- "_extensionBundleIdentifier"
- "_intentIndexingHash"
- "_isClockFaceProcess"
- "_isInternalBuild"
- "_kind"
- "_lock"
- "_lock_hintObservers"
- "_lock_observers"
- "_lock_scheduledHintTimers"
- "_lock_scheduledTimers"
- "_lock_userDefaults"
- "_mainQueue_notifyObserversDefaultsDidChange"
- "_mainQueue_notifyObserversDefaultsHintDidChange"
- "_observeChangesToPrivacyDefaults"
- "_observeChangesToRelevantWidgetDefaults"
- "_observeChangesToUserDefaults"
- "_postPrivacyDefaultsDidChangeNotification"
- "_queue"
- "_requestUserDefaultsSyncForKey:"
- "_scheduleTimerToUnmuteHintForKey:onDate:"
- "_scheduleTimerToUnmuteWidgetForKey:onDate:"
- "_scheduleTimersToUnmuteHints"
- "_scheduleTimersToUnmuteWidgets"
- "_widgetKind"
- "addHintObserver:"
- "addObject:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addTimer:forMode:"
- "allKeys"
- "allObjects"
- "appSuggestionsEnabledForContainerBundleIdentifier:"
- "appendInt64:withName:"
- "appendInteger:withName:"
- "appendObject:"
- "appendString:counterpart:"
- "appendString:withName:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "boolValue"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bundleForClass:"
- "bundleIdentifier"
- "com.apple.NanoHomeScreen"
- "compare:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "diagnosticDictionaryRepresentation"
- "domainAccessorForReads"
- "doubleValue"
- "enabledDictionaryValueWithIdentifier:onDomainObjectWithKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "globalSuggestionsEnabled"
- "hash"
- "hintUnmuteDateForContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "init"
- "initForReadingFromData:error:"
- "initWithCoder:"
- "initWithContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "initWithDomain:"
- "initWithExtensionBundleIdentifier:appBundleIdentifier:widgetKind:confidenceCategory:intentIndexingHash:"
- "initWithFireDate:interval:repeats:block:"
- "initWithSuiteName:"
- "integerValue"
- "invalidate"
- "isEqual"
- "isEqual:"
- "isEqualToString:"
- "length"
- "localizedMicrophonePermissionAlertAllowButtonText"
- "localizedMicrophonePermissionAlertDenyButtonText"
- "localizedMicrophonePermissionAlertHeader"
- "localizedMicrophonePermissionAlertMessage"
- "localizedMicrophonePermissionSwitchFootnote"
- "localizedMicrophonePermissionSwitchName"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "mainRunLoop"
- "mutableCopy"
- "now"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKey:"
- "observeValueForKeyPath:ofObject:change:context:"
- "persistentDomainForName:"
- "privacyDefaultsDidChange"
- "q"
- "q16@0:8"
- "raise:format:"
- "relevantWidgetDefaultsDidChange"
- "removeHintObserver:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "setAppSuggestionsEnabled:forContainerBundleIdentifier:"
- "setClearWidgetAlertAcknowledged:"
- "setDecodingFailurePolicy:"
- "setGlobalSuggestionsEnabled:"
- "setHintUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "setMicrophonePermission:"
- "setNPSSyncedBoolEnabledValue:forDomainObjectKey:"
- "setNPSSyncedBoolEnabledValue:forDomainObjectKey:withDictionaryKeyIfDomainIsDictionary:preferenceDeletedIfValueEnabled:"
- "setObject:forKey:"
- "setPresentSmartStackFromHintAlertAcknowledged:"
- "setRelevantWidgets:"
- "setSoundDetectionButtonDismissedOnce:"
- "setSuggestionsShowHintEnabled:"
- "setWidgetSuggestionsEnabled:forContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "setWidgetSuggestionsUnmuteDate:forContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "setWithObject:"
- "setWithObjects:"
- "sharedInstance"
- "smartStackNPSSuggestionsDefaultsDidChange"
- "smartStackSuggestionDefaultsDidChange"
- "smartStackSuggestionDefaultsHintDidChange"
- "soundDetectionButton"
- "stringWithUTF8String:"
- "strongToWeakObjectsMapTable"
- "suggestionsShowHintEnabled"
- "supportsSecureCoding"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "synchronizeUserDefaultsDomain:keys:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8B16@20"
- "v32@0:8@16@24"
- "v40@0:8B16@20@28B36"
- "v44@0:8B16@20@28@36"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32^v40"
- "weakObjectsHashTable"
- "widgetSuggestionsEnabledForContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "widgetSuggestionsUnmuteDateForContainerBundleIdentifier:extensionBundleIdentifier:kind:"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
