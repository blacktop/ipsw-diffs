## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-491.2.1.0.0
-  __TEXT.__text: 0x2c5a8
+491.8.0.0.0
+  __TEXT.__text: 0x2c7e4
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x2d4c
-  __TEXT.__cstring: 0x2e06
+  __TEXT.__objc_methlist: 0x2d7c
+  __TEXT.__cstring: 0x2e2e
   __TEXT.__const: 0x90
   __TEXT.__oslogstring: 0x1f4c
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0xbd4
+  __TEXT.__unwind_info: 0xbdc
   __TEXT.__objc_classname: 0x863
-  __TEXT.__objc_methname: 0x8895
-  __TEXT.__objc_methtype: 0x10c7
+  __TEXT.__objc_methname: 0x88ff
+  __TEXT.__objc_methtype: 0x10cb
   __TEXT.__objc_stubs: 0x4a20
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__const: 0xa90
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7e60
-  __DATA_CONST.__objc_selrefs: 0x1958
-  __AUTH_CONST.__cfstring: 0x2fc0
+  __DATA_CONST.__objc_const: 0x7ea0
+  __DATA_CONST.__objc_selrefs: 0x1970
+  __AUTH_CONST.__cfstring: 0x3000
   __AUTH_CONST.__objc_const: 0x18b0
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_intobj: 0x18

   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x298
   __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x708
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xc58

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1193
-  Symbols:   4181
-  CStrings:  2028
+  Functions: 1197
+  Symbols:   4190
+  CStrings:  2035
 
Symbols:
+ +[UNNotificationIcon iconWithData:]
+ -[UNMutableNotificationContent setSpeechLanguage:]
+ -[UNNotificationContent _initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:speechLanguage:userInfo:]
+ -[UNNotificationContent speechLanguage]
+ -[UNNotificationIcon data]
+ OBJC_IVAR_$_UNNotificationContent._speechLanguage
+ _objc_msgSend$_initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:speechLanguage:userInfo:
+ _objc_msgSend$speechLanguage
- -[UNNotificationContent _initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:userInfo:]
- _objc_msgSend$_initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:userInfo:
- _objc_msgSend$markedMutableCopyMessage
CStrings:
+ "\x0f&\x11\x13!\x12"
+ "<%@: %p; title: %@, subtitle: %@, body: %@, summaryArgument: %@, summaryArgumentCount: %u, categoryIdentifier: %@, launchImageName: %@, threadIdentifier: %@, attachments: %@, badge: %@, sound: %@, realert: %u, interruptionLevel: %lu, relevanceScore: %.2f, filterCriteria: %@, screenCaptureProhibited: %d, speechLanguage: %@"
+ "@324@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144B152B156B160B164B168B172B176B180B184B188B192B196B200B204@208@216@224@232@240Q248@256Q264@272Q280d288@296B304@308@316"
+ "Data"
+ "T@\"NSString\",R,C,N,V_speechLanguage"
+ "_initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:speechLanguage:userInfo:"
+ "_speechLanguage"
+ "iconWithData:"
+ "setSpeechLanguage:"
+ "speechLanguage"
- "\x0f&\x11\x13!\x11"
- "<%@: %p; title: %@, subtitle: %@, body: %@, summaryArgument: %@, summaryArgumentCount: %u, categoryIdentifier: %@, launchImageName: %@, threadIdentifier: %@, attachments: %@, badge: %@, sound: %@, realert: %u, interruptionLevel: %lu, relevanceScore: %.2f, filterCriteria: %@, screenCaptureProhibited: %d"
- "@316@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144B152B156B160B164B168B172B176B180B184B188B192B196B200B204@208@216@224@232@240Q248@256Q264@272Q280d288@296B304@308"
- "_initWithContentType:communicationContext:accessoryImageName:attachments:badge:body:categoryIdentifier:date:icon:defaultActionTitle:defaultActionURL:defaultActionBundleIdentifier:expirationDate:header:footer:launchImageName:peopleIdentifiers:shouldHideDate:shouldHideTime:shouldIgnoreDoNotDisturb:shouldIgnoreDowntime:shouldSuppressScreenLightUp:shouldAuthenticateDefaultAction:shouldBackgroundDefaultAction:shouldPreventNotificationDismissalAfterDefaultAction:shouldShowSubordinateIcon:shouldSuppressDefaultAction:shouldSuppressSyncDismissalWhenRemoved:shouldUseRequestIdentifierForDismissalSync:shouldPreemptPresentedNotification:shouldDisplayActionsInline:sound:subtitle:threadIdentifier:title:topicIdentifiers:realertCount:summaryArgument:summaryArgumentCount:targetContentIdentifier:interruptionLevel:relevanceScore:filterCriteria:screenCaptureProhibited:userInfo:"

```
