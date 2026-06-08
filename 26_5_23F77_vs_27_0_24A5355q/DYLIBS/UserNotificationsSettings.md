## UserNotificationsSettings

> `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings`

```diff

-640.5.32.104.0
-  __TEXT.__text: 0x74c4
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0xaa0
+703.0.0.0.0
+  __TEXT.__text: 0x6d24
+  __TEXT.__objc_methlist: 0xb60
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x758
+  __TEXT.__cstring: 0x766
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0x776
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x22b
-  __TEXT.__objc_methname: 0x1c6b
-  __TEXT.__objc_methtype: 0x6ad
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0x1ab0
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__objc_const: 0x1b58
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x300
-  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA.__data: 0x360
+  __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5B4F77F-37DF-3806-8DBE-5FD2F21CB3CF
+  UUID: 6309D67D-012B-3904-9B00-492ECAD07F09
   Functions: 235
-  Symbols:   937
-  CStrings:  478
+  Symbols:   950
+  CStrings:  148
 
Symbols:
+ -[UNNotificationSourceMuteAssertion expirationDate]
+ -[UNNotificationThreadsMuteAssertion expirationDateByThreadID]
+ __OBJC_$_PROP_LIST_UNNotificationSourceMuteAssertion
+ __OBJC_$_PROP_LIST_UNNotificationThreadsMuteAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UNNotificationSettingsCenterProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNNotificationSettingsCenterProtocol
+ __OBJC_LABEL_PROTOCOL_$_UNNotificationSettingsCenterProtocol
+ __OBJC_PROTOCOL_$_UNNotificationSettingsCenterProtocol
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<UNNotificationSettingsCenterDelegate>\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"UNNotificationIcon\""
- "@\"UNNotificationMuteAssertion\""
- "@\"UNNotificationSettings\""
- "@\"UNNotificationSourceSettings\""
- "@\"UNNotificationTopic\""
- "@104@0:8q16q24q32q40q48@56q64q72q80q88Q96"
- "@112@0:8q16q24q32q40q48@56q64q72q80q88q96Q104"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24@32B40"
- "@60@0:8@16B24@28@36@44@52"
- "@80@0:8q16q24q32q40q48@56q64q72"
- "@96@0:8q16q24q32q40q48@56q64q72q80q88"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16o^@24"
- "B40@0:8@16@?24o^@32"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<UNNotificationSettingsCenterDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",C,D,N"
- "T@\"NSArray\",R,C,N,V_scheduledDeliveryTimes"
- "T@\"NSArray\",R,C,N,V_topicSettings"
- "T@\"NSHashTable\",&,N,V_observers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callOutQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_bundlePath"
- "T@\"NSString\",R,C,N,V_displayName"
- "T@\"NSString\",R,C,N,V_sourceIdentifier"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"UNNotificationIcon\",R,C,N,V_icon"
- "T@\"UNNotificationMuteAssertion\",R,C,N,V_muteAssertion"
- "T@\"UNNotificationSettings\",R,C,N,V_notificationSettings"
- "T@\"UNNotificationSettings\",R,C,N,V_topicSettings"
- "T@\"UNNotificationSourceSettings\",R,C,N,V_sourceSettings"
- "T@\"UNNotificationTopic\",R,C,N,V_topic"
- "TB,R"
- "TB,R,N,V_isHiddenFromSettings"
- "TB,R,N,V_isRestricted"
- "TQ,R"
- "TQ,R,N,V_modifiedSettings"
- "Tq,D,N"
- "Tq,R,N"
- "Tq,R,N,V_announcementCarPlaySetting"
- "Tq,R,N,V_announcementHeadphonesSetting"
- "Tq,R,N,V_announcementSetting"
- "Tq,R,N,V_notificationListDisplayStyleSetting"
- "Tq,R,N,V_prioritizationSetting"
- "Tq,R,N,V_remoteNotificationsSetting"
- "Tq,R,N,V_scheduledDeliverySetting"
- "Tq,R,N,V_scheduledDeliveryShowNextSummarySetting"
- "Tq,R,N,V_showPreviewsSetting"
- "Tq,R,N,V_summarizationSetting"
- "UNMutableNotificationSystemSettings"
- "UNNotificationMuteAssertion"
- "UNNotificationSettingsCenter"
- "UNNotificationSource"
- "UNNotificationSourceMuteAssertion"
- "UNNotificationSourceSettings"
- "UNNotificationSystemSettings"
- "UNNotificationThreadsMuteAssertion"
- "UNNotificationTopicSettings"
- "UNUserNotificationSettingsClientProtocol"
- "UNUserNotificationSettingsServerProtocol"
- "UNUserNotificationSettingsService"
- "UNUserNotificationSettingsServiceConnection"
- "UNUserNotificationSettingsServiceConnectionObserver"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_announcementCarPlaySetting"
- "_announcementHeadphonesSetting"
- "_announcementSetting"
- "_bundlePath"
- "_callOutQueue"
- "_connection"
- "_delegate"
- "_displayName"
- "_expirationDate"
- "_expirationDateByThreadID"
- "_icon"
- "_init"
- "_invalidate"
- "_isHiddenFromSettings"
- "_isRestricted"
- "_modifiedSettings"
- "_muteAssertion"
- "_notificationListDisplayStyleSetting"
- "_notificationSettings"
- "_observers"
- "_prioritizationSetting"
- "_queue"
- "_queue_addObserver:"
- "_queue_ensureConnection"
- "_queue_interruptedConnection"
- "_queue_invalidatedConnection"
- "_queue_removeObserver:"
- "_remoteNotificationsSetting"
- "_scheduledDeliverySetting"
- "_scheduledDeliveryShowNextSummarySetting"
- "_scheduledDeliveryTimes"
- "_showPreviewsSetting"
- "_sourceIdentifier"
- "_sourceSettings"
- "_stringForNotificationListDisplayStyleSetting:"
- "_stringForScheduledDeliveryTimes:"
- "_stringforAnnouncementCarPlaySetting:"
- "_summarizationSetting"
- "_topic"
- "_topicSettings"
- "addObject:"
- "addObserver:"
- "allNotificationSources"
- "allocWithZone:"
- "arrayWithObjects:count:"
- "authorizationWithOptions:forNotificationSourceIdentifier:withCompletionHandler:"
- "autorelease"
- "callOutQueue"
- "class"
- "clientInterface"
- "compare:"
- "conformsToProtocol:"
- "connection"
- "copy"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "currentNotificationSettingsCenter"
- "dateFromComponents:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "getNotificationSettingsForSourceIdentifier:withCompletionHandler:"
- "getNotificationSource:withCompletionHandler:"
- "getNotificationSources:withCompletionHandler:"
- "getNotificationSourcesWithFilter:sort:maxCount:completionHandler:"
- "getNotificationSystemSettingsWithCompletionHandler:"
- "hash"
- "init"
- "initWithCoder:"
- "initWithExpirationDate:"
- "initWithExpirationDateByThreadID:"
- "initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:"
- "initWithMachServiceName:options:"
- "initWithNotificationSettings:topicSettings:muteAssertion:isRestricted:"
- "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:"
- "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:remoteNotificationsSetting:summarizationSetting:prioritizationSetting:modifiedSettings:"
- "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:summarizationSetting:prioritizationSetting:"
- "initWithShowPreviewsSetting:announcementSetting:announcementHeadphonesSetting:announcementCarPlaySetting:scheduledDeliverySetting:scheduledDeliveryTimes:scheduledDeliveryShowNextSummarySetting:notificationListDisplayStyleSetting:summarizationSetting:prioritizationSetting:modifiedSettings:"
- "initWithTopic:settings:"
- "initWithTopic:settings:muteAssertion:"
- "interfaceWithProtocol:"
- "invalidate"
- "isActiveForThreadIdentifier:currentDate:"
- "isEqual:"
- "isHiddenFromSettings"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRestricted"
- "length"
- "mutableCopy"
- "mutableCopyWithZone:"
- "mutateNotificationSettingsForSourceIdentifier:mutatingBlock:error:"
- "notificationSettingsForSourceIdentifier:"
- "notificationSourceWithIdentifier:"
- "notificationSourcesWithFilter:"
- "notificationSourcesWithFilter:sort:maxCount:completionHandler:"
- "notificationSourcesWithIdentifiers:"
- "notificationSystemSettings"
- "now"
- "objectForKey:"
- "observers"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "queue"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObject:"
- "removeObserver:"
- "replaceNotificationSettings:forNotificationSourceIdentifier:"
- "replaceNotificationTopicSettings:forNotificationSourceIdentifier:topicIdentifier:"
- "resetScheduledDeliverySetting"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:"
- "self"
- "serverInterface"
- "setAnnouncementCarPlaySetting:"
- "setAnnouncementHeadphonesSetting:"
- "setAnnouncementSetting:"
- "setCallOutQueue:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setDateFormat:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNotificationListDisplayStyleSetting:"
- "setNotificationSystemSettings:"
- "setObservers:"
- "setPrioritizationSetting:"
- "setQueue:"
- "setRemoteNotificationsSetting:"
- "setRemoteObjectInterface:"
- "setScheduledDeliverySetting:"
- "setScheduledDeliveryShowNextSummarySetting:"
- "setScheduledDeliveryTimes:"
- "setShowPreviewsSetting:"
- "setSourceSettings:"
- "setSourceSettings:completionHandler:"
- "setSourceSettings:error:"
- "setSpokenNotificationSetting:"
- "setSummarizationSetting:"
- "setWithArray:"
- "setWithObjects:"
- "settingsServiceConnection:didUpdateNotificationSourcesWithIdentifiers:"
- "settingsServiceConnection:didUpdateNotificationSystemSettings:"
- "sharedInstance"
- "sourceIdentifier"
- "sourceMuteAssertionUntilDate:"
- "sourceWithIdentifier:"
- "spokenNotificationSetting"
- "stringByAppendingString:"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "threadsMuteAssertionWithExpirationDateByThreadID:"
- "updateNotificationSourcesWithBundleIdentifiers:"
- "updateNotificationSystemSettings:"
- "userNotificationSettingsCenter:didUpdateNotificationSourceIdentifiers:"
- "userNotificationSettingsCenter:didUpdateNotificationSystemSettings:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"UNNotificationSystemSettings\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"UNNotificationSystemSettings\">16"
- "v24@0:8q16"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSSet\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"UNNotificationSettings\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"UNNotificationSource\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"UNNotificationSettings\"16@\"NSString\"24"
- "v32@0:8@\"UNUserNotificationSettingsServiceConnection\"16@\"NSSet\"24"
- "v32@0:8@\"UNUserNotificationSettingsServiceConnection\"16@\"UNNotificationSystemSettings\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"UNNotificationSettings\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8Q16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "weakObjectsHashTable"
- "zone"

```
