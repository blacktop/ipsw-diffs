## ReminderKit

> `/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit`

```diff

-3810.0.0.0.0
-  __TEXT.__text: 0x13d8f4
+3854.1.0.0.0
+  __TEXT.__text: 0x13f060
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x15390
+  __TEXT.__objc_methlist: 0x15660
   __TEXT.__const: 0x16b7
   __TEXT.__oslogstring: 0x11960
-  __TEXT.__cstring: 0xde02
+  __TEXT.__cstring: 0xdf2c
   __TEXT.__gcc_except_tab: 0x8350
   __TEXT.__ustring: 0x292
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x67c0
-  __TEXT.__objc_classname: 0x3a4b
-  __TEXT.__objc_methname: 0x27428
-  __TEXT.__objc_methtype: 0x41d5
-  __TEXT.__objc_stubs: 0x165a0
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__const: 0x2a00
-  __DATA_CONST.__objc_classlist: 0xbb8
+  __TEXT.__unwind_info: 0x6840
+  __TEXT.__objc_classname: 0x3aee
+  __TEXT.__objc_methname: 0x27770
+  __TEXT.__objc_methtype: 0x4234
+  __TEXT.__objc_stubs: 0x166e0
+  __DATA_CONST.__got: 0xf38
+  __DATA_CONST.__const: 0x2a08
+  __DATA_CONST.__objc_classlist: 0xbe0
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x79c8
+  __DATA_CONST.__objc_selrefs: 0x7a58
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x9f0
+  __DATA_CONST.__objc_superrefs: 0xa18
   __DATA_CONST.__objc_arraydata: 0x998
   __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0x2ca0
-  __AUTH_CONST.__cfstring: 0xe2c0
-  __AUTH_CONST.__objc_const: 0x238f0
+  __AUTH_CONST.__cfstring: 0xe420
+  __AUTH_CONST.__objc_const: 0x23ea8
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x3020
+  __AUTH.__objc_data: 0x31b0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x1110
+  __DATA.__objc_ivar: 0x1130
   __DATA.__data: 0x1a3c
   __DATA.__bss: 0x314
   __DATA.__common: 0x8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0C992E21-0C5B-3937-A42A-1851AF60977B
-  Functions: 8629
-  Symbols:   27690
-  CStrings:  11348
+  UUID: BD15E54E-FA2F-33A5-AD08-B7EA5E250EE5
+  Functions: 8681
+  Symbols:   27858
+  CStrings:  11407
 
Symbols:
+ +[REMFindMyDeviceInformation supportsSecureCoding]
+ +[REMUrgentPresentationAlarm supportsSecureCoding]
+ +[REMUrgentPresentationAlarmStatePerUser supportsSecureCoding]
+ -[REMAccountCapabilities supportsUrgentAlarm]
+ -[REMDaemonUserDefaults observeShowUrgentRemindersCompleteButtonWithBlock:]
+ -[REMDaemonUserDefaults resetShowSuggestGroceries]
+ -[REMDaemonUserDefaults setResetShowSuggestGroceries:]
+ -[REMDaemonUserDefaults setShowUrgentRemindersCompleteButton:]
+ -[REMDaemonUserDefaults showUrgentRemindersCompleteButton]
+ -[REMFindMyDeviceInformation .cxx_destruct]
+ -[REMFindMyDeviceInformation copyWithZone:]
+ -[REMFindMyDeviceInformation description]
+ -[REMFindMyDeviceInformation deviceName]
+ -[REMFindMyDeviceInformation encodeWithCoder:]
+ -[REMFindMyDeviceInformation initWithCoder:]
+ -[REMFindMyDeviceInformation initWithDeviceName:isMeDevice:]
+ -[REMFindMyDeviceInformation isEqual:]
+ -[REMFindMyDeviceInformation isMeDevice]
+ -[REMReminder urgentAlarmContext]
+ -[REMReminderChangeItem urgentAlarmContext]
+ -[REMReminderStorage isUrgentStateEnabledForCurrentUser]
+ -[REMReminderStorage setIsUrgentStateEnabledForCurrentUser:]
+ -[REMReminderUrgentAlarmContext .cxx_destruct]
+ -[REMReminderUrgentAlarmContext initWithReminder:]
+ -[REMReminderUrgentAlarmContext isUrgentStateEnabledForCurrentUser]
+ -[REMReminderUrgentAlarmContext reminder]
+ -[REMReminderUrgentAlarmContext setReminder:]
+ -[REMReminderUrgentAlarmContextChangeItem .cxx_destruct]
+ -[REMReminderUrgentAlarmContextChangeItem initWithReminderChangeItem:]
+ -[REMReminderUrgentAlarmContextChangeItem isUrgentStateEnabledForCurrentUser]
+ -[REMReminderUrgentAlarmContextChangeItem reminderChangeItem]
+ -[REMReminderUrgentAlarmContextChangeItem setIsUrgentStateEnabledForCurrentUser:]
+ -[REMReminderUrgentAlarmContextChangeItem setReminderChangeItem:]
+ -[REMUrgentPresentationAlarm .cxx_destruct]
+ -[REMUrgentPresentationAlarm copyWithZone:]
+ -[REMUrgentPresentationAlarm description]
+ -[REMUrgentPresentationAlarm encodeWithCoder:]
+ -[REMUrgentPresentationAlarm initWithCoder:]
+ -[REMUrgentPresentationAlarm initWithUrgentAlarmStateByAccountIdentifier:]
+ -[REMUrgentPresentationAlarm initWithUrgentAlarmStates:]
+ -[REMUrgentPresentationAlarm isEqual:]
+ -[REMUrgentPresentationAlarm mergingWith:]
+ -[REMUrgentPresentationAlarm mergingWithState:]
+ -[REMUrgentPresentationAlarm urgentAlarmStateByAccountIdentifier]
+ -[REMUrgentPresentationAlarmStatePerUser .cxx_destruct]
+ -[REMUrgentPresentationAlarmStatePerUser copyWithZone:]
+ -[REMUrgentPresentationAlarmStatePerUser description]
+ -[REMUrgentPresentationAlarmStatePerUser encodeWithCoder:]
+ -[REMUrgentPresentationAlarmStatePerUser initWithCoder:]
+ -[REMUrgentPresentationAlarmStatePerUser initWithPersonIdentifier:isEnabled:modifiedOn:]
+ -[REMUrgentPresentationAlarmStatePerUser isEnabled]
+ -[REMUrgentPresentationAlarmStatePerUser isEqual:]
+ -[REMUrgentPresentationAlarmStatePerUser modifiedOn]
+ -[REMUrgentPresentationAlarmStatePerUser personIdentifier]
+ _OBJC_CLASS_$_REMFindMyDeviceInformation
+ _OBJC_CLASS_$_REMReminderUrgentAlarmContext
+ _OBJC_CLASS_$_REMReminderUrgentAlarmContextChangeItem
+ _OBJC_CLASS_$_REMUrgentPresentationAlarm
+ _OBJC_CLASS_$_REMUrgentPresentationAlarmStatePerUser
+ _OBJC_IVAR_$_REMAccountCapabilities._supportsUrgentAlarm
+ _OBJC_IVAR_$_REMFindMyDeviceInformation._deviceName
+ _OBJC_IVAR_$_REMFindMyDeviceInformation._isMeDevice
+ _OBJC_IVAR_$_REMReminderStorage._isUrgentStateEnabledForCurrentUser
+ _OBJC_IVAR_$_REMReminderUrgentAlarmContext._reminder
+ _OBJC_IVAR_$_REMReminderUrgentAlarmContextChangeItem._reminderChangeItem
+ _OBJC_IVAR_$_REMUrgentPresentationAlarm._urgentAlarmStateByAccountIdentifier
+ _OBJC_IVAR_$_REMUrgentPresentationAlarmStatePerUser._isEnabled
+ _OBJC_IVAR_$_REMUrgentPresentationAlarmStatePerUser._modifiedOn
+ _OBJC_IVAR_$_REMUrgentPresentationAlarmStatePerUser._personIdentifier
+ _OBJC_METACLASS_$_REMFindMyDeviceInformation
+ _OBJC_METACLASS_$_REMReminderUrgentAlarmContext
+ _OBJC_METACLASS_$_REMReminderUrgentAlarmContextChangeItem
+ _OBJC_METACLASS_$_REMUrgentPresentationAlarm
+ _OBJC_METACLASS_$_REMUrgentPresentationAlarmStatePerUser
+ _REMSettingsUrgentRemindersShowStopButtonAsCompleteIdentifier
+ __OBJC_$_CLASS_METHODS_REMFindMyDeviceInformation
+ __OBJC_$_CLASS_METHODS_REMUrgentPresentationAlarm
+ __OBJC_$_CLASS_METHODS_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_$_CLASS_PROP_LIST_REMFindMyDeviceInformation
+ __OBJC_$_CLASS_PROP_LIST_REMUrgentPresentationAlarm
+ __OBJC_$_CLASS_PROP_LIST_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_$_INSTANCE_METHODS_REMFindMyDeviceInformation
+ __OBJC_$_INSTANCE_METHODS_REMReminderUrgentAlarmContext
+ __OBJC_$_INSTANCE_METHODS_REMReminderUrgentAlarmContextChangeItem
+ __OBJC_$_INSTANCE_METHODS_REMUrgentPresentationAlarm
+ __OBJC_$_INSTANCE_METHODS_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_$_INSTANCE_VARIABLES_REMFindMyDeviceInformation
+ __OBJC_$_INSTANCE_VARIABLES_REMReminderUrgentAlarmContext
+ __OBJC_$_INSTANCE_VARIABLES_REMReminderUrgentAlarmContextChangeItem
+ __OBJC_$_INSTANCE_VARIABLES_REMUrgentPresentationAlarm
+ __OBJC_$_INSTANCE_VARIABLES_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_$_PROP_LIST_REMFindMyDeviceInformation
+ __OBJC_$_PROP_LIST_REMReminderUrgentAlarmContext
+ __OBJC_$_PROP_LIST_REMReminderUrgentAlarmContextChangeItem
+ __OBJC_$_PROP_LIST_REMUrgentPresentationAlarm
+ __OBJC_$_PROP_LIST_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_CLASS_PROTOCOLS_$_REMFindMyDeviceInformation
+ __OBJC_CLASS_PROTOCOLS_$_REMUrgentPresentationAlarm
+ __OBJC_CLASS_PROTOCOLS_$_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_CLASS_RO_$_REMFindMyDeviceInformation
+ __OBJC_CLASS_RO_$_REMReminderUrgentAlarmContext
+ __OBJC_CLASS_RO_$_REMReminderUrgentAlarmContextChangeItem
+ __OBJC_CLASS_RO_$_REMUrgentPresentationAlarm
+ __OBJC_CLASS_RO_$_REMUrgentPresentationAlarmStatePerUser
+ __OBJC_METACLASS_RO_$_REMFindMyDeviceInformation
+ __OBJC_METACLASS_RO_$_REMReminderUrgentAlarmContext
+ __OBJC_METACLASS_RO_$_REMReminderUrgentAlarmContextChangeItem
+ __OBJC_METACLASS_RO_$_REMUrgentPresentationAlarm
+ __OBJC_METACLASS_RO_$_REMUrgentPresentationAlarmStatePerUser
+ ___75-[REMDaemonUserDefaults observeShowUrgentRemindersCompleteButtonWithBlock:]_block_invoke
+ _kREMSupportedVersionFor2025C
+ _objc_msgSend$deviceName
+ _objc_msgSend$initWithDeviceName:isMeDevice:
+ _objc_msgSend$initWithPersonIdentifier:isEnabled:modifiedOn:
+ _objc_msgSend$initWithUrgentAlarmStateByAccountIdentifier:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isMeDevice
+ _objc_msgSend$isUrgentStateEnabledForCurrentUser
+ _objc_msgSend$personIdentifier
+ _objc_msgSend$setIsUrgentStateEnabledForCurrentUser:
+ _objc_msgSend$showUrgentRemindersCompleteButton
+ _objc_msgSend$supportsUrgentAlarm
+ _objc_msgSend$urgentAlarmContext
+ _objc_msgSend$urgentAlarmStateByAccountIdentifier
- -[REMAccountCapabilities supportsUrgentAlert]
- -[REMReminderStorage prefersUrgentPresentationStyleForDateAlarms]
- -[REMReminderStorage setPrefersUrgentPresentationStyleForDateAlarms:]
- _OBJC_IVAR_$_REMAccountCapabilities._supportsUrgentAlert
- _OBJC_IVAR_$_REMReminderStorage._prefersUrgentPresentationStyleForDateAlarms
- _objc_msgSend$prefersUrgentPresentationStyleForDateAlarms
- _objc_msgSend$setPrefersUrgentPresentationStyleForDateAlarms:
- _objc_msgSend$supportsUrgentAlert
CStrings:
+ "<%@: %p deviceName: %@, isMeDevice: %i>"
+ "<%@: %p personIdentifier: %@, isEnabled: %@, modifiedOn: %@>"
+ "<%@: %p urgentAlertByAccountIdentifier: %@>"
+ "@36@0:8@16B24@28"
+ "REMFindMyDeviceInformation"
+ "REMReminderUrgentAlarmContext"
+ "REMReminderUrgentAlarmContextChangeItem"
+ "REMUrgentPresentationAlarm"
+ "REMUrgentPresentationAlarmStatePerUser"
+ "T@\"NSDictionary\",R,N,V_urgentAlarmStateByAccountIdentifier"
+ "T@\"NSString\",R,N,V_deviceName"
+ "T@\"NSString\",R,N,V_personIdentifier"
+ "T@\"REMReminderUrgentAlarmContext\",R,N"
+ "T@\"REMReminderUrgentAlarmContextChangeItem\",R,N"
+ "TB,N,V_isUrgentStateEnabledForCurrentUser"
+ "TB,R,N,V_isEnabled"
+ "TB,R,N,V_isMeDevice"
+ "TB,R,N,V_supportsUrgentAlarm"
+ "URGENT_REMINDERS"
+ "_deviceName"
+ "_isEnabled"
+ "_isMeDevice"
+ "_isUrgentStateEnabledForCurrentUser"
+ "_personIdentifier"
+ "_supportsUrgentAlarm"
+ "_urgentAlarmStateByAccountIdentifier"
+ "deviceName"
+ "fetchFindMyDeviceInformationWithCompletion:"
+ "initWithDeviceName:isMeDevice:"
+ "initWithPersonIdentifier:isEnabled:modifiedOn:"
+ "initWithUrgentAlarmStateByAccountIdentifier:"
+ "initWithUrgentAlarmStates:"
+ "isEnabled"
+ "isMeDevice"
+ "isUrgentStateEnabledForCurrentUser"
+ "mergingWithState:"
+ "observeShowUrgentRemindersCompleteButtonWithBlock:"
+ "personIdentifier"
+ "resetShowSuggestGroceries"
+ "setIsUrgentStateEnabledForCurrentUser:"
+ "setResetShowSuggestGroceries:"
+ "setShowUrgentRemindersCompleteButton:"
+ "setSuggestGroceriesDismissed:completion:"
+ "showUrgentRemindersCompleteButton"
+ "supportsUrgentAlarm"
+ "urgentAlarmContext"
+ "urgentAlarmStateByAccountIdentifier"
+ "v24@0:8@?<v@?@\"REMFindMyDeviceInformation\"@\"NSError\">16"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{vector<CRDT::Document_DocObject *, std::allocator<CRDT::Document_DocObject *>>=\"__begin_\"^^{Document_DocObject}\"__end_\"^^{Document_DocObject}\"\"{?=\"__cap_\"^^{Document_DocObject}}}"
+ "{vector<TopoSubstring *, std::allocator<TopoSubstring *>>=\"__begin_\"^^{TopoSubstring}\"__end_\"^^{TopoSubstring}\"\"{?=\"__cap_\"^^{TopoSubstring}}}"
+ "{vector<std::pair<TopoID, TopoID>, std::allocator<std::pair<TopoID, TopoID>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
- "TB,N,V_prefersUrgentPresentationStyleForDateAlarms"
- "TB,R,N,V_supportsUrgentAlert"
- "_prefersUrgentPresentationStyleForDateAlarms"
- "_supportsUrgentAlert"
- "prefersUrgentPresentationStyleForDateAlarms"
- "setPrefersUrgentPresentationStyleForDateAlarms:"
- "supportsUrgentAlert"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
- "{vector<CRDT::Document_DocObject *, std::allocator<CRDT::Document_DocObject *>>=\"__begin_\"^^{Document_DocObject}\"__end_\"^^{Document_DocObject}\"__cap_\"^^{Document_DocObject}}"
- "{vector<TopoSubstring *, std::allocator<TopoSubstring *>>=\"__begin_\"^^{TopoSubstring}\"__end_\"^^{TopoSubstring}\"__cap_\"^^{TopoSubstring}}"
- "{vector<std::pair<TopoID, TopoID>, std::allocator<std::pair<TopoID, TopoID>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"

```
