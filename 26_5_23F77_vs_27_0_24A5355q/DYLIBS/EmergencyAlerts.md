## EmergencyAlerts

> `/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts`

```diff

-211.0.0.0.0
-  __TEXT.__text: 0x391c
-  __TEXT.__auth_stubs: 0x2f0
+263.0.0.0.0
+  __TEXT.__text: 0x3820
   __TEXT.__objc_methlist: 0x178
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x474
-  __TEXT.__oslogstring: 0x687
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x40e
+  __TEXT.__oslogstring: 0x824
   __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0x4b
-  __TEXT.__objc_methname: 0xb8c
-  __TEXT.__objc_methtype: 0xf8
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x1d0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D422530B-50B9-376E-82BF-27BE927DDEEF
-  Functions: 68
-  Symbols:   400
-  CStrings:  311
+  UUID: 580D1BD5-80FE-33D9-8898-CAD2DA075E10
+  Functions: 70
+  Symbols:   420
+  CStrings:  173
 
Symbols:
+ -[UNMutableNotificationContent(EmergencyAlerts) ea_geofencingIsAvailableForAlertHash:]
+ -[UNMutableNotificationContent(EmergencyAlerts) ea_geofencingIsAvailableForAlertHash:].cold.1
+ -[UNMutableNotificationContent(EmergencyAlerts) ea_geofencingIsAvailableForAlertHash:].cold.2
+ -[UNMutableNotificationContent(EmergencyAlerts) ea_geofencingIsAvailableForAlertHash:].cold.3
+ -[UNMutableNotificationContent(EmergencyAlerts) ea_geofencingIsAvailableForAlertHash:].cold.4
+ _EAAlertHashKey
+ _EACategoryIdentifierGeoAlert
+ _EACategoryIdentifierGeoAlertWatch
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$allKeys
+ _objc_msgSend$applicationIsInstalled:
+ _objc_msgSend$circularGeofences
+ _objc_msgSend$count
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$ea_geofencingIsAvailableForAlertHash:
+ _objc_msgSend$getMetadataForEmergencyAlert:outError:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$polygonalGeofences
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- -[UNMutableNotificationContent(EmergencyAlerts) ea_setAlertCategory:].cold.1
- -[UNMutableNotificationContent(EmergencyAlerts) ea_updateAlertCategory:]
- -[UNMutableNotificationContent(EmergencyAlerts) ea_updateAlertCategory:].cold.1
- _EACategoryIdentifierAlertDetailed
- _EACategoryIdentifierAlertSpinner
- _EACategoryIdentifierConfigurableAlert
- _EACategoryIdentifierConfigurableAlertDetailed
- _EACategoryIdentifierConfigurableAlertSpinner
- _OUTLINED_FUNCTION_3
- _objc_msgSend$ea_updateAlertCategory:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Added alert hash to userInfo: %{public}@"
+ "Alert Category: %{public}@"
+ "Alert hash is nil or empty"
+ "Alert hash key is not present in message dictionary, using default category"
+ "AlertHash"
+ "Error retrieving metadata for alert hash %{public}@: %{public}@"
+ "Failed to create CoreTelephony client"
+ "Invalid CellBroadcast dictionary - received keys: %@, full dictionary: %@"
+ "Maps installed: %{BOOL}d"
+ "Maps not installed, using default alert category"
+ "Metadata is nil for alert hash %{public}@"
+ "No geofences available."
+ "UserInfo dict: %{public}@"
+ "WEA alert hash is available: %{public}@"
+ "WEA can be rendered with map."
+ "cell broadcast wea dictionary: %@"
+ "com.apple.Maps"
+ "geo-alert"
+ "geo-alert-watch"
- ".cxx_destruct"
- "@\"EAEmergencyAlertCenter\""
- "@\"NotificationViewController\""
- "@\"UNUserNotificationCenter\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "Advanced Earthquake Alert"
- "Alert Category updated: %@"
- "Alert Category: %@"
- "Alert category: %@"
- "EACellBroadcastMessageListener"
- "EAEmergencyAlertCenter"
- "EmergencyAlerts"
- "Failed to get switch name."
- "Handling RAW cellbroadcast message"
- "Invalid CellBroadcast dictionary"
- "Overriding user configurable category to NO"
- "Q16@0:8"
- "SwitchName"
- "URLForResource:withExtension:"
- "UTF8String"
- "UserConfigurable"
- "_cellBroadcastMessageReceived:"
- "_emergencyAlertCenter"
- "_notificationViewController"
- "_userNotificationCenter"
- "addNotificationRequest:withCompletionHandler:"
- "alert-configurable"
- "alert-configurable-detailed"
- "alert-configurable-spinner"
- "alert-detailed"
- "alert-spinner"
- "appendFormat:"
- "arrayWithObjects:count:"
- "body"
- "boolValue"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "caseInsensitiveCompare:"
- "categoryIdentifier"
- "cellBroadcastMessageReceived:"
- "characterAtIndex:"
- "characterIsMember:"
- "componentsJoinedByString:"
- "content"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentAudioAndVideoCallCount"
- "currentCalendar"
- "date"
- "dateFormatFromTemplate:options:locale:"
- "dateFromString:"
- "dealloc"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "ea_bundleForBundleIdentifier:"
- "ea_defaultTitle"
- "ea_externalToneFileURLForTone:inBundle:"
- "ea_externalVibrationPatternFileURLForVibration:inBundle:"
- "ea_getUpdatedBodyString:withMessageDictionary:"
- "ea_setAlertCategory:"
- "ea_setPropertiesForCellBroadcastMessage:withActivePhoneCall:"
- "ea_timestampSubtitleForDate:locale:"
- "ea_timestampSubtitleForNow"
- "ea_updateAlertCategory:"
- "ea_updateUserInfo:withMessageDictionary:"
- "errorWithDomain:code:userInfo:"
- "getDeliveredNotificationsWithCompletionHandler:"
- "getUpdatedNotificationForAppleSafetyAlert:withMessageDictionary:"
- "handleAppleSafetyAlertMessage:"
- "handleCellBroadcastMessage:withCompletionHandler:"
- "handleRawCellBroadcastMessage:withCompletionHandler:"
- "identifier"
- "init"
- "initWithBundleIdentifier:"
- "initWithUserNotificationCenter:"
- "integerValue"
- "isDateInToday:"
- "isDateInTomorrow:"
- "isDateInYesterday:"
- "isEqualToString:"
- "lastPathComponent"
- "length"
- "localizedStringForKey:value:table:"
- "localizedUserNotificationStringForKey:arguments:"
- "maximumDuration"
- "mutableCopy"
- "numberWithDouble:"
- "numberWithInt:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "onUserTappedOnWeaWithInfo:"
- "path"
- "pathExtension"
- "rangeOfString:"
- "replaceContentForRequestWithIdentifier:replacementContent:completionHandler:"
- "replaceContentForRequestWithRequestID:replacementContent:completionHandler:"
- "request"
- "requestWithIdentifier:content:trigger:"
- "setAlertTopic:"
- "setBody:"
- "setCategoryIdentifier:"
- "setDateFormat:"
- "setFormatOptions:"
- "setLocalizedDateFormatFromTemplate:"
- "setMaximumDuration:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setScreenCaptureProhibited:"
- "setShouldIgnoreAccessibilityDisabledVibrationSetting:"
- "setShouldIgnoreDoNotDisturb:"
- "setShouldIgnoreRingerSwitch:"
- "setShouldPreemptPresentedNotification:"
- "setShouldRepeat:"
- "setShouldSuppressDefaultAction:"
- "setSound:"
- "setSpeechLanguage:"
- "setSubtitle:"
- "setTitle:"
- "setToneFileURL:"
- "setToneIdentifier:"
- "setUserInfo:"
- "setVibrationIdentifier:"
- "setVibrationPatternFileURL:"
- "sharedInstance"
- "sharedInterface"
- "shouldIgnoreAccessibilityDisabledVibrationSetting"
- "shouldIgnoreRingerSwitch"
- "shouldRepeat"
- "soundWithAlertType:"
- "start"
- "stringByAppendingFormat:"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "substringFromIndex:"
- "substringToIndex:"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^{__CFDictionary=}16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "whitespaceAndNewlineCharacterSet"

```
