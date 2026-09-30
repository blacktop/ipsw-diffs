## CalendarNotification

> `/System/Library/PrivateFrameworks/CalendarNotification.framework/Versions/A/CalendarNotification`

```diff

-1513.3.1.0.0
-  __TEXT.__text: 0x61f60
+1513.5.3.0.0
+  __TEXT.__text: 0x6200c
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x59d4
+  __TEXT.__objc_methlist: 0x69cc
   __TEXT.__const: 0x1f8
   __TEXT.__oslogstring: 0xdd6c
   __TEXT.__cstring: 0x408e
   __TEXT.__gcc_except_tab: 0x5b4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1558
-  __TEXT.__objc_classname: 0x1c56
-  __TEXT.__objc_methname: 0x12584
+  __TEXT.__unwind_info: 0x15c8
+  __TEXT.__objc_classname: 0x1c6f
+  __TEXT.__objc_methname: 0x125e9
   __TEXT.__objc_methtype: 0x30df
-  __TEXT.__objc_stubs: 0xbb20
-  __DATA_CONST.__got: 0x918
+  __TEXT.__objc_stubs: 0xbb40
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3238
+  __DATA_CONST.__objc_selrefs: 0x3368
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x1080
   __AUTH_CONST.__cfstring: 0x2f20
-  __AUTH_CONST.__objc_const: 0xffe8
+  __AUTH_CONST.__objc_const: 0xe560
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0x78c
+  __AUTH.__objc_data: 0x2d50
+  __DATA.__objc_ivar: 0x790
   __DATA.__data: 0x1b00
   __DATA.__bss: 0x288
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 017C55AB-75DD-3FC1-979D-5C014B3C2208
-  Functions: 2265
-  Symbols:   6369
-  CStrings:  4303
+  UUID: AEDD979D-DE5E-3ED1-BD88-56B1F47F6EBE
+  Functions: 2296
+  Symbols:   6410
+  CStrings:  4308
 
Symbols:
+ +[CALNCLCoreLocationProvider sharedInstance].cold.1
+ +[CALNCUIKIconProvider _identifierEncodingAllowedCharacters].cold.1
+ +[CALNDateStringUtils _allDayFormatter].cold.1
+ +[CALNDateStringUtils _dateTimeFormatter].cold.1
+ +[CALNFakeNotificationSource _activeSourcesQueue].cold.1
+ +[CALNFakeNotificationSource _activeSources].cold.1
+ +[CALNLogSubsystem alarmEngine].cold.1
+ +[CALNLogSubsystem calendar].cold.1
+ +[CALNLogSubsystem defaultCategory].cold.1
+ +[CALNNotificationIdentifier _allowedCharacterSetForEncodingNotificationIdentifierComponents].cold.1
+ +[CALNNotificationRecordsDiff emptyDiff].cold.1
+ +[CALNNullCoreLocationProvider sharedInstance].cold.1
+ +[CALNNullRemoteMutator sharedInstance].cold.1
+ +[CALNPersistentNotificationStorage notificationRecordsFromPersistentNotificationStorageWithPath:error:].cold.1
+ +[CALNPersistentTimeToLeaveRefreshStorage timeToLeaveRefreshDataFromPersistentStorageWithPath:error:].cold.1
+ +[CALNPersistentTriggeredEventNotificationDataStorage notificationDataFromPersistentStorageWithPath:error:].cold.1
+ +[CALNSnoozeCategory snoozeCategories].cold.1
+ +[CALNTriggeredEventNotificationSourceClientIdentifierUtilities _characterSetForEncodingIdentifierComponents].cold.1
+ +[CALNUNUserNotificationCenterFactory sharedInstance].cold.1
+ +[_EKAlarmEngine sharedInstance].cold.1
+ -[CALNCalendarResourceChangedNotificationSource categories].cold.1
+ -[CALNDefaultAppURLHandler .cxx_destruct]
+ -[CALNDefaultAppURLHandler fallbackHandler]
+ -[CALNDefaultAppURLHandler initWithFallbackHandler:]
+ -[CALNDefaultAppURLHandler openURL:response:]
+ -[CALNEventInvitationNotificationSource categories].cold.1
+ -[CALNEventInvitationResponseNotificationSource categories].cold.1
+ -[CALNFakeNotificationSource initWithNotificationManager:iconIdentifierProvider:sourceIdentifierSuffix:].cold.1
+ -[CALNNotificationContent initWithCoder:].cold.1
+ -[CALNSharedCalendarInvitationNotificationSource categories].cold.1
+ -[CALNSharedCalendarInvitationResponseNotificationSource categories].cold.1
+ -[CALNTriggeredEventNotificationMailtoURLProvider mailtoURLForEvent:].cold.1
+ -[CALNTriggeredEventNotificationSource categories].cold.1
+ -[_EKAlarmEngine _installTimerWithFireDate:].cold.1
+ OBJC_IVAR_$_CALNDefaultAppURLHandler._fallbackHandler
+ _OBJC_CLASS_$_CALNDefaultAppURLHandler
+ _OBJC_METACLASS_$_CALNDefaultAppURLHandler
+ __64-[CALNNotificationServerModule _registerSettingsCaptureHandlers]_block_invoke.90
+ __OBJC_$_INSTANCE_METHODS_CALNDefaultAppURLHandler
+ __OBJC_$_INSTANCE_VARIABLES_CALNDefaultAppURLHandler
+ __OBJC_$_PROP_LIST_CALNDefaultAppURLHandler
+ __OBJC_CLASS_PROTOCOLS_$_CALNDefaultAppURLHandler
+ __OBJC_CLASS_RO_$_CALNDefaultAppURLHandler
+ __OBJC_METACLASS_RO_$_CALNDefaultAppURLHandler
+ _objc_msgSend$initWithFallbackHandler:
+ snoozeLogHandle.cold.1
- _OUTLINED_FUNCTION_4
- __64-[CALNNotificationServerModule _registerSettingsCaptureHandlers]_block_invoke.89
CStrings:
+ "CALNDefaultAppURLHandler"
+ "T@\"<CALNURLHandler>\",R,N,V_fallbackHandler"
+ "_fallbackHandler"
+ "fallbackHandler"
+ "initWithFallbackHandler:"

```
