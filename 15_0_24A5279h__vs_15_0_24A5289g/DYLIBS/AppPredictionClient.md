## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient`

```diff

-569.0.1.0.0
-  __TEXT.__text: 0x18baec
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x15bf8
+571.0.3.0.0
+  __TEXT.__text: 0x18d970
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x15f30
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x199e0
+  __TEXT.__cstring: 0x19b98
   __TEXT.__oslogstring: 0x157ec
-  __TEXT.__gcc_except_tab: 0x1efc
+  __TEXT.__gcc_except_tab: 0x1eec
   __TEXT.__dlopen_cstrs: 0x26f
   __TEXT.__ustring: 0x18a
   __TEXT.__unwind_info: 0x5f08
-  __TEXT.__objc_classname: 0x376e
-  __TEXT.__objc_methname: 0x2ffed
-  __TEXT.__objc_methtype: 0x6314
-  __TEXT.__objc_stubs: 0x1a540
+  __TEXT.__objc_classname: 0x3770
+  __TEXT.__objc_methname: 0x305d5
+  __TEXT.__objc_methtype: 0x63f1
+  __TEXT.__objc_stubs: 0x1a880
   __DATA_CONST.__got: 0x15f0
-  __DATA_CONST.__const: 0x2c20
+  __DATA_CONST.__const: 0x2dd0
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9070
+  __DATA_CONST.__objc_selrefs: 0x91f8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xb78
   __DATA_CONST.__objc_arraydata: 0xac8
-  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x5c00
-  __AUTH_CONST.__cfstring: 0x13ac0
-  __AUTH_CONST.__objc_const: 0x440a8
+  __AUTH_CONST.__const: 0x5c20
+  __AUTH_CONST.__cfstring: 0x13d80
+  __AUTH_CONST.__objc_const: 0x44578
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x8340
-  __DATA.__objc_ivar: 0x1a9c
+  __DATA.__objc_ivar: 0x1af4
   __DATA.__data: 0x1b08
-  __DATA.__bss: 0x540
+  __DATA.__bss: 0x538
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9878
-  Symbols:   22561
-  CStrings:  3073
+  Functions: 9944
+  Symbols:   22675
+  CStrings:  3094
 
Symbols:
+ -[ATXPBUserNotification hasIsDeterminedUrgentByModel]
+ -[ATXPBUserNotification hasIsPartOfStack]
+ -[ATXPBUserNotification hasIsStackSummary]
+ -[ATXPBUserNotification hasIsSummarized]
+ -[ATXPBUserNotification hasNumberOfNotificationsInStack]
+ -[ATXPBUserNotification hasPositionInStack]
+ -[ATXPBUserNotification hasSubtitleLength]
+ -[ATXPBUserNotification hasSummaryLength]
+ -[ATXPBUserNotification hasSummary]
+ -[ATXPBUserNotification hasTitleLength]
+ -[ATXPBUserNotification isDeterminedUrgentByModel]
+ -[ATXPBUserNotification isPartOfStack]
+ -[ATXPBUserNotification isStackSummary]
+ -[ATXPBUserNotification isSummarized]
+ -[ATXPBUserNotification numberOfNotificationsInStack]
+ -[ATXPBUserNotification positionInStack]
+ -[ATXPBUserNotification setHasIsDeterminedUrgentByModel:]
+ -[ATXPBUserNotification setHasIsPartOfStack:]
+ -[ATXPBUserNotification setHasIsStackSummary:]
+ -[ATXPBUserNotification setHasIsSummarized:]
+ -[ATXPBUserNotification setHasNumberOfNotificationsInStack:]
+ -[ATXPBUserNotification setHasPositionInStack:]
+ -[ATXPBUserNotification setHasSubtitleLength:]
+ -[ATXPBUserNotification setHasSummaryLength:]
+ -[ATXPBUserNotification setHasTitleLength:]
+ -[ATXPBUserNotification setIsDeterminedUrgentByModel:]
+ -[ATXPBUserNotification setIsPartOfStack:]
+ -[ATXPBUserNotification setIsStackSummary:]
+ -[ATXPBUserNotification setIsSummarized:]
+ -[ATXPBUserNotification setNumberOfNotificationsInStack:]
+ -[ATXPBUserNotification setPositionInStack:]
+ -[ATXPBUserNotification setSubtitleLength:]
+ -[ATXPBUserNotification setSummary:]
+ -[ATXPBUserNotification setSummaryLength:]
+ -[ATXPBUserNotification setTitleLength:]
+ -[ATXPBUserNotification subtitleLength]
+ -[ATXPBUserNotification summaryLength]
+ -[ATXPBUserNotification summary]
+ -[ATXPBUserNotification titleLength]
+ -[ATXPBUserNotificationLoggingEvent StringAsDeliveryUI:]
+ -[ATXPBUserNotificationLoggingEvent deliveryUIAsString:]
+ -[ATXPBUserNotificationLoggingEvent deliveryUI]
+ -[ATXPBUserNotificationLoggingEvent hasDeliveryUI]
+ -[ATXPBUserNotificationLoggingEvent setDeliveryUI:]
+ -[ATXPBUserNotificationLoggingEvent setHasDeliveryUI:]
+ -[ATXUserNotification isDeterminedUrgentByModel]
+ -[ATXUserNotification isPartOfStack]
+ -[ATXUserNotification isStackSummary]
+ -[ATXUserNotification isSummarized]
+ -[ATXUserNotification numberOfNotificationsInStack]
+ -[ATXUserNotification positionInStack]
+ -[ATXUserNotification setIsDeterminedUrgentByModel:]
+ -[ATXUserNotification setIsPartOfStack:]
+ -[ATXUserNotification setIsStackSummary:]
+ -[ATXUserNotification setIsSummarized:]
+ -[ATXUserNotification setNumberOfNotificationsInStack:]
+ -[ATXUserNotification setPositionInStack:]
+ -[ATXUserNotification setSubtitleLength:]
+ -[ATXUserNotification setSummary:]
+ -[ATXUserNotification setSummaryLength:]
+ -[ATXUserNotification setTitleLength:]
+ -[ATXUserNotification subtitleLength]
+ -[ATXUserNotification summaryLength]
+ -[ATXUserNotification summary]
+ -[ATXUserNotification titleLength]
+ -[ATXUserNotificationLoggingEvent deliveryUI]
+ -[ATXUserNotificationLoggingEvent initFromUserNotification:eventType:timestamp:deliveryReason:deliveryUI:]
+ -[ATXUserNotificationLoggingEvent initFromUserNotification:eventType:timestamp:deliveryReason:deliveryUI:modeUUID:]
+ -[ATXUserNotificationLoggingEvent isDeliveredInPrioritySection]
+ OBJC_IVAR_$_ATXPBUserNotification._isDeterminedUrgentByModel
+ OBJC_IVAR_$_ATXPBUserNotification._isPartOfStack
+ OBJC_IVAR_$_ATXPBUserNotification._isStackSummary
+ OBJC_IVAR_$_ATXPBUserNotification._isSummarized
+ OBJC_IVAR_$_ATXPBUserNotification._numberOfNotificationsInStack
+ OBJC_IVAR_$_ATXPBUserNotification._positionInStack
+ OBJC_IVAR_$_ATXPBUserNotification._subtitleLength
+ OBJC_IVAR_$_ATXPBUserNotification._summary
+ OBJC_IVAR_$_ATXPBUserNotification._summaryLength
+ OBJC_IVAR_$_ATXPBUserNotification._titleLength
+ OBJC_IVAR_$_ATXPBUserNotificationLoggingEvent._deliveryUI
+ OBJC_IVAR_$_ATXUserNotification._isDeterminedUrgentByModel
+ OBJC_IVAR_$_ATXUserNotification._isPartOfStack
+ OBJC_IVAR_$_ATXUserNotification._isStackSummary
+ OBJC_IVAR_$_ATXUserNotification._isSummarized
+ OBJC_IVAR_$_ATXUserNotification._numberOfNotificationsInStack
+ OBJC_IVAR_$_ATXUserNotification._positionInStack
+ OBJC_IVAR_$_ATXUserNotification._subtitleLength
+ OBJC_IVAR_$_ATXUserNotification._summary
+ OBJC_IVAR_$_ATXUserNotification._summaryLength
+ OBJC_IVAR_$_ATXUserNotification._titleLength
+ OBJC_IVAR_$_ATXUserNotificationLoggingEvent._deliveryUI
+ __42+[ATXAppDisplayIdentifiers allIdentifiers]_block_invoke.9
+ __71-[ATXWidgetDescriptorCache initWithProvider:cachePath:legacyCachePath:]_block_invoke.17
+ __block_literal_global.42
+ __getAVOutputDeviceClass_block_invoke.cold.2
+ __os_feature_enabled_impl
+ _objc_msgSend$deliveryUI
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initFromUserNotification:eventType:timestamp:deliveryReason:deliveryUI:
+ _objc_msgSend$initFromUserNotification:eventType:timestamp:deliveryReason:deliveryUI:modeUUID:
+ _objc_msgSend$isDeterminedUrgentByModel
+ _objc_msgSend$isPartOfStack
+ _objc_msgSend$isStackSummary
+ _objc_msgSend$isSummarized
+ _objc_msgSend$numberOfNotificationsInStack
+ _objc_msgSend$pathComponents
+ _objc_msgSend$positionInStack
+ _objc_msgSend$setBiomeStreamIdentifier:
+ _objc_msgSend$setDeliveryUI:
+ _objc_msgSend$setIsDeterminedUrgentByModel:
+ _objc_msgSend$setIsPartOfStack:
+ _objc_msgSend$setIsStackSummary:
+ _objc_msgSend$setIsSummarized:
+ _objc_msgSend$setNumberOfNotificationsInStack:
+ _objc_msgSend$setPositionInStack:
+ _objc_msgSend$setSubtitleLength:
+ _objc_msgSend$setSummary:
+ _objc_msgSend$setSummaryLength:
+ _objc_msgSend$setTitleLength:
+ _objc_msgSend$settingBiomeStreamIdentifier
+ _objc_msgSend$subtitleLength
+ _objc_msgSend$summary
+ _objc_msgSend$summaryLength
+ _objc_msgSend$titleLength
- -[ATXUserNotificationLoggingEvent initFromUserNotification:eventType:timestamp:deliveryReason:modeUUID:]
- AVFoundationLibrary.cold.1
- _AVFoundationLibrary
- __71-[ATXWidgetDescriptorCache initWithProvider:cachePath:legacyCachePath:]_block_invoke.19
- ___getAVRoutingSessionManagerClass_block_invoke
- __getAVRoutingSessionManagerClass_block_invoke.cold.1
- _objc_msgSend$initFromUserNotification:eventType:timestamp:deliveryReason:modeUUID:
- _objc_msgSend$instancesRespondToSelector:
- getAVRoutingSessionManagerClass.softClass
CStrings:
+ ".app"
+ "Banner"
+ "Digest"
+ "MissedNotificationBundle"
+ "Notification event: user notification: %!@(MISSING), event: %!@(MISSING), timestamp: %!f(MISSING), deliveryReason: %!@(MISSING), deliveryUI: %!@(MISSING), mode: %!@(MISSING)"
+ "NotificationCenter"
+ "Priority"
+ "PriorityNotification"
+ "PriorityNotificationsSectionAppeared"
+ "PriorityNotificationsSectionClearAll"
+ "PriorityNotificationsSectionCollapsed"
+ "PriorityNotificationsSectionDisappeared"
+ "PriorityNotificationsSectionExpanded"
+ "deliveryUI"
+ "isDeterminedUrgentByModel"
+ "isPartOfStack"
+ "isStackSummary"
+ "isSummarized"
+ "load_widget_descriptors_mac"
+ "numberOfNotificationsInStack"
+ "positionInStack"
+ "subtitleLength"
+ "summaryLength"
+ "titleLength"
- "AVRoutingSessionManager"
- "Class getAVRoutingSessionManagerClass(void)_block_invoke"
- "Notification event: user notification: %!@(MISSING), event: %!@(MISSING), timestamp: %!f(MISSING)"

```
