## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-966.0.0.0.0
-  __TEXT.__text: 0x73378
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0x40cc
+967.0.0.0.0
+  __TEXT.__text: 0x73f24
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_methlist: 0x4164
   __TEXT.__const: 0x11a8
-  __TEXT.__cstring: 0xb79c
-  __TEXT.__swift5_typeref: 0x528
-  __TEXT.__swift5_capture: 0x204
-  __TEXT.__oslogstring: 0x43c4
+  __TEXT.__cstring: 0xb974
+  __TEXT.__swift5_typeref: 0x50e
+  __TEXT.__oslogstring: 0x4482
   __TEXT.__constg_swiftt: 0x45c
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x3f8
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_capture: 0x200
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xac8
   __TEXT.__gcc_except_tab: 0xef8
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x1798
+  __TEXT.__unwind_info: 0x17c0
   __TEXT.__eh_frame: 0x8e0
   __TEXT.__objc_classname: 0x99d
-  __TEXT.__objc_methname: 0xbaea
-  __TEXT.__objc_methtype: 0x20f3
-  __TEXT.__objc_stubs: 0x5420
+  __TEXT.__objc_methname: 0xbcd2
+  __TEXT.__objc_methtype: 0x211e
+  __TEXT.__objc_stubs: 0x5560
   __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__const: 0x1470
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e88
+  __DATA_CONST.__objc_selrefs: 0x1ef0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x988
   __AUTH_CONST.__auth_ptr: 0x300
-  __AUTH_CONST.__const: 0xb48
-  __AUTH_CONST.__cfstring: 0x4ac0
-  __AUTH_CONST.__objc_const: 0x8fd8
+  __AUTH_CONST.__const: 0xb68
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0x9038
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1220
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x380
-  __DATA.__data: 0x1118
+  __DATA.__data: 0x1128
   __DATA.__bss: 0x1600
   __DATA.__common: 0x2e8
   __DATA_DIRTY.__objc_ivar: 0x1d8
   __DATA_DIRTY.__objc_data: 0x928
-  __DATA_DIRTY.__data: 0xe0
+  __DATA_DIRTY.__data: 0xe8
   __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2186
-  Symbols:   2147
-  CStrings:  3249
+  Functions: 2205
+  Symbols:   2186
+  CStrings:  3286
 
Symbols:
+ _CFAutorelease
+ _CFEqual
+ _CFPreferencesGetAppBooleanValue
+ _MGCopyAnswer
+ _SMInitiatorInitializationNumRecepients
+ _SMRemoteUserActionsCommand
+ _SMRemoteUserActionsCommandType
+ _SMRemoteUserActionsErrorCode
+ _SMRemoteUserActionsErrorDomain
+ _SMRemoteUserActionsIsCellularActivated
+ _SMRemoteUserActionsIsStandalone
+ _SMRemoteUserActionsSuccess
+ _SMSessionGroupBimonthlyCount
+ _SMSessionGroupDailyCount
+ _SMSessionGroupMonthlyCount
+ _SMSessionGroupWeeklyCount
+ _SMSessionUserDetailsAnalyticsEvent
+ _SMSiriSettingsLockScreenPrefsChangedNotificationName
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
CStrings:
+ "%!@(MISSING), %!@(MISSING), lockscreenSuggestionsDisabledBundles, %!@(MISSING), globalSiriSuggestionsEnabled, %!@(MISSING), globalSiriSuggestionsEnabledQuerySuccess, %!@(MISSING)"
+ "-[SMSafetyMonitorManager fetchNumEmergencyRecipientsWithReceiverHandles:handler:]"
+ "-[SMSafetyMonitorManager fetchNumFavoriteRecipientsWithReceiverHandles:handler:]"
+ "-[SMSafetyMonitorManager fetchNumiCloudFamilyRecipientsWithReceiverHandles:handler:]"
+ "-[SMSafetyMonitorManager submitInitializationAnalyticsEventWithError:conversation:duration:]"
+ "DeviceClass"
+ "Invalid parameter not satisfying: receiverHandles (in %!s(MISSING):%!d(MISSING))"
+ "LockScreenSuggestionsDisabled"
+ "LockscreenSuggestionsDisabledBundles"
+ "SMTriggerCategoryWorkoutManualPauseTimeout"
+ "SafetyMonitorLockscreenSuggestionsEnabledWatch"
+ "_copyDuetExpertPreferencesValueForKey:"
+ "_syncSiriLockScreenSuggestionsPrefIfNeeded"
+ "_syncSiriLockScreenSuggestionsPrefWithValue:"
+ "bimonthlyGroupCount"
+ "com.apple.SafetyMonitor.perSessionUserDetails"
+ "com.apple.duetexpertd"
+ "com.apple.duetexpertd.prefschanged"
+ "com.apple.lockscreen.shared"
+ "command"
+ "commandType"
+ "dailyGroupCount"
+ "duetExpertStore"
+ "errorCode"
+ "errorDomain"
+ "fetchNumEmergencyRecipientsWithReceiverHandles:handler:"
+ "fetchNumFavoriteRecipientsWithReceiverHandles:handler:"
+ "fetchNumiCloudFamilyRecipientsWithReceiverHandles:handler:"
+ "iPhone"
+ "isAnomalyState"
+ "isCellularActivated"
+ "isLockScreenSuggestionsAllowed"
+ "isMobileSMSPreferencesLockScreenSuggestionsAllowed"
+ "isMonitoringState"
+ "isStandalone"
+ "monthlyGroupCount"
+ "numRecepients"
+ "submitInitializationAnalyticsEventWithError:conversation:duration:"
+ "syncSiriLockScreenSuggestionsPrefs"
+ "synchronize"
+ "v32@0:8@\"NSArray\"16@?<v@?Q@\"NSError\">24"
+ "v40@0:8@16@24d32"
+ "weeklyGroupCount"
- "-[SMSafetyMonitorManager submitInitializationAnalyticsEventWithError:duration:]"
- "No Internet Connection"
- "Warning text to be used in Live Activity when the user turns off cellular or turns on Airplane mode."
- "Warning title to be used in Live Activity when the user turns off cellular or turns on Airplane mode."
- "submitInitializationAnalyticsEventWithError:duration:"
- "v32@0:8@16d24"

```
