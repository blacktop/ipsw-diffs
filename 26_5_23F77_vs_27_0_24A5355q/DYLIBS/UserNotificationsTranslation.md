## UserNotificationsTranslation

> `/System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation`

```diff

-640.5.32.104.0
-  __TEXT.__text: 0x1668
-  __TEXT.__auth_stubs: 0x140
+703.0.0.0.0
+  __TEXT.__text: 0x159c
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xad
-  __TEXT.__unwind_info: 0x68
-  __TEXT.__objc_classname: 0x9
-  __TEXT.__objc_methname: 0xe73
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__objc_stubs: 0x1880
-  __DATA_CONST.__got: 0x138
+  __TEXT.__cstring: 0xe5
+  __TEXT.__unwind_info: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
-  __AUTH_CONST.__auth_got: 0xa8
+  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x40
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D74E3299-6730-3413-A2DA-923388C021A5
-  Functions: 4
-  Symbols:   268
-  CStrings:  217
+  UUID: A9D18351-AF57-3B2E-AD9C-3AE7D35F95CE
+  Functions: 5
+  Symbols:   285
+  CStrings:  19
 
Symbols:
+ _OBJC_CLASS_$__UNAppEntityIdentifier
+ __NSConcreteGlobalBlock
+ ___52+[UNNotification(Bulletin) notificationForBulletin:]_block_invoke_2
+ ___block_descriptor_32_e55_"_UNAppEntityIdentifier"16?0"BBAppEntityIdentifier"8l
+ ___block_literal_global.33
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$appEntityIdentifiers
+ _objc_msgSend$bs_compactMap:
+ _objc_msgSend$communicationTrustScore
+ _objc_msgSend$initWithBundleIdentifier:typeIdentifier:instanceIdentifier:
+ _objc_msgSend$instanceIdentifier
+ _objc_msgSend$setCommunicationTrustScore:
+ _objc_msgSend$setRawAppEntityIdentifiers:
+ _objc_msgSend$typeIdentifier
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ +[UNNotification(Bulletin) notificationForBulletin:] : 4448 -> 4104
~ ___52+[UNNotification(Bulletin) notificationForBulletin:]_block_invoke : 88 -> 84
~ _UNContactFromBBContact : 380 -> 352
~ _UNCommunicationContextFromBBCommunicationContext : 820 -> 812
CStrings:
+ "@\"_UNAppEntityIdentifier\"16@?0@\"BBAppEntityIdentifier\"8"
- "@24@0:8@16"
- "Bulletin"
- "URL"
- "_bestVariantForFormat:"
- "activationMode"
- "addObject:"
- "addObjectsFromArray:"
- "additionalAttachments"
- "alertConfiguration"
- "appearance"
- "applicationIdentifier"
- "array"
- "arrayByAddingObject:"
- "associatedObjectUri"
- "attachmentWithIdentifier:URL:options:error:"
- "audioCategory"
- "boolValue"
- "bs_secureDecodedFromData:"
- "bundleIdentifier"
- "capabilities"
- "categoryID"
- "cnContactFullname"
- "cnContactIdentifier"
- "communicationContext"
- "contentType"
- "contentURL"
- "context"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "customIdentifier"
- "date"
- "dateComponentDetails"
- "dateIsAllDay"
- "defaultAction"
- "dictionary"
- "dismissalID"
- "displayName"
- "expirationDate"
- "externalToneFileURL"
- "externalToneMediaLibraryItemIdentifier"
- "externalVibrationPatternFileURL"
- "filterCriteria"
- "footer"
- "handle"
- "handleType"
- "hasSubordinateIcon"
- "header"
- "hiddenFromDefaultExpandedView"
- "icon"
- "iconAtPath:shouldSuppressMask:"
- "iconForApplicationIdentifier:"
- "iconForSystemImageNamed:"
- "iconNamed:shouldSuppressMask:"
- "iconWithDateComponents:calendarIdentifier:format:"
- "iconWithUTI:"
- "identifier"
- "ignoresDowntime"
- "imageName"
- "imagePath"
- "initFileURLWithPath:sandboxExtensionClass:"
- "integerValue"
- "intentIDs"
- "interruptionLevel"
- "isAuthenticationRequired"
- "isBusinessCorrespondence"
- "isCNContactIdentifierSuggested"
- "isDisplayNameSuggested"
- "isEqualToString:"
- "isPrecomposed"
- "isReplyToCurrentUser"
- "lastPathComponent"
- "launchBundleID"
- "launchURL"
- "length"
- "maximumDuration"
- "mentionsCurrentUser"
- "message"
- "mutableCopy"
- "notificationForBulletin:"
- "notificationWithRequest:date:sourceIdentifier:intentIdentifiers:"
- "notifyRecipientAnyway"
- "numberWithBool:"
- "objectForKey:"
- "path"
- "primaryAttachment"
- "publisherBulletinID"
- "realertCount"
- "recipientCount"
- "recipients"
- "recordID"
- "relevanceScore"
- "requestWithIdentifier:content:trigger:"
- "screenCaptureProhibited"
- "section"
- "sender"
- "serviceName"
- "setAlertTopic:"
- "setAssociatedObjectUri:"
- "setAttachments:"
- "setAudioCategory:"
- "setAudioVolume:"
- "setBadge:"
- "setBody:"
- "setBundleIdentifier:"
- "setBusinessCorrespondence:"
- "setCapabilities:"
- "setCategoryIdentifier:"
- "setCnContactFullname:"
- "setCnContactIdentifier:"
- "setCnContactIdentifierSuggested:"
- "setCommunicationContext:"
- "setContentType:"
- "setContentURL:"
- "setCritical:"
- "setCustomIdentifier:"
- "setDate:"
- "setDefaultActionBundleIdentifier:"
- "setDefaultActionTitle:"
- "setDefaultActionURL:"
- "setDisplayName:"
- "setDisplayNameSuggested:"
- "setExpirationDate:"
- "setFilterCriteria:"
- "setFooter:"
- "setHandle:"
- "setHandleType:"
- "setHasDefaultAction:"
- "setHeader:"
- "setIcon:"
- "setIdentifier:"
- "setImageName:"
- "setInterruptionLevel:"
- "setLaunchImageName:"
- "setMaximumDuration:"
- "setMentionsCurrentUser:"
- "setNotifyRecipientAnyway:"
- "setObject:forKey:"
- "setRealertCount:"
- "setRecipientCount:"
- "setRecipients:"
- "setRelevanceScore:"
- "setReplyToCurrentUser:"
- "setScreenCaptureProhibited:"
- "setSender:"
- "setServiceName:"
- "setShouldAuthenticateDefaultAction:"
- "setShouldBackgroundDefaultAction:"
- "setShouldHideDate:"
- "setShouldHideTime:"
- "setShouldIgnoreDoNotDisturb:"
- "setShouldIgnoreDowntime:"
- "setShouldIgnoreRingerSwitch:"
- "setShouldPreventNotificationDismissalAfterDefaultAction:"
- "setShouldRepeat:"
- "setShouldShowSubordinateIcon:"
- "setShouldSuppressScreenLightUp:"
- "setShouldSuppressSyncDismissalWhenRemoved:"
- "setShouldUseRequestIdentifierForDismissalSync:"
- "setSound:"
- "setSpeechLanguage:"
- "setSubtitle:"
- "setSummaryArgument:"
- "setSummaryArgumentCount:"
- "setSystemImage:"
- "setTargetContentIdentifier:"
- "setThreadIdentifier:"
- "setTitle:"
- "setToneFileName:"
- "setToneFileURL:"
- "setToneIdentifier:"
- "setToneMediaLibraryItemIdentifier:"
- "setTopicIdentifiers:"
- "setUserInfo:"
- "setVibrationIdentifier:"
- "setVibrationPatternFileURL:"
- "shouldDismissBulletin"
- "shouldIgnoreRingerSwitch"
- "shouldRepeat"
- "sound"
- "soundWithAlertType:"
- "speechLanguage"
- "subsectionIDs"
- "subtitle"
- "summaryArgument"
- "summaryArgumentCount"
- "systemImage"
- "systemImageName"
- "threadID"
- "thumbnailGeneratorUserInfo"
- "thumbnailHidden"
- "title"
- "toneIdentifier"
- "topic"
- "turnsOnDisplay"
- "type"
- "uniformType"
- "usesExternalSync"
- "uti"
- "vibrationIdentifier"

```
