## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-576.0.4.0.0
-  __TEXT.__text: 0x447c9c
+579.0.0.0.0
+  __TEXT.__text: 0x448e40
   __TEXT.__auth_stubs: 0x31f0
-  __TEXT.__objc_methlist: 0x35d9c
+  __TEXT.__objc_methlist: 0x35e84
   __TEXT.__const: 0x2a12
-  __TEXT.__cstring: 0x56f62
-  __TEXT.__oslogstring: 0x39e86
-  __TEXT.__gcc_except_tab: 0xeffc
+  __TEXT.__cstring: 0x57482
+  __TEXT.__oslogstring: 0x39fc6
+  __TEXT.__gcc_except_tab: 0xf030
   __TEXT.__dlopen_cstrs: 0x23c
   __TEXT.__swift5_typeref: 0xdc6
   __TEXT.__constg_swiftt: 0x1624

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xd4e8
+  __TEXT.__unwind_info: 0xd528
   __TEXT.__eh_frame: 0x1b44
-  __TEXT.__objc_classname: 0x8b5c
-  __TEXT.__objc_methname: 0xabdcf
-  __TEXT.__objc_methtype: 0x19467
-  __TEXT.__objc_stubs: 0x4c060
-  __DATA_CONST.__got: 0x3650
-  __DATA_CONST.__const: 0xb8d8
-  __DATA_CONST.__objc_classlist: 0x1ef8
+  __TEXT.__objc_classname: 0x8b84
+  __TEXT.__objc_methname: 0xac2bc
+  __TEXT.__objc_methtype: 0x19494
+  __TEXT.__objc_stubs: 0x4c340
+  __DATA_CONST.__got: 0x3658
+  __DATA_CONST.__const: 0xb928
+  __DATA_CONST.__objc_classlist: 0x1f00
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b520
+  __DATA_CONST.__objc_selrefs: 0x1b5e8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x1500
-  __DATA_CONST.__objc_arraydata: 0x1258
+  __DATA_CONST.__objc_superrefs: 0x1508
+  __DATA_CONST.__objc_arraydata: 0x1280
   __AUTH_CONST.__auth_got: 0x1910
   __AUTH_CONST.__auth_ptr: 0x4b8
   __AUTH_CONST.__const: 0x7528
-  __AUTH_CONST.__cfstring: 0x39660
-  __AUTH_CONST.__objc_const: 0x852e0
+  __AUTH_CONST.__cfstring: 0x39800
+  __AUTH_CONST.__objc_const: 0x85368
   __AUTH_CONST.__objc_intobj: 0x33a8
-  __AUTH_CONST.__objc_arrayobj: 0x1038
+  __AUTH_CONST.__objc_arrayobj: 0x1050
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x4c00
+  __AUTH.__objc_data: 0x4c50
   __AUTH.__data: 0x1c08
-  __DATA.__objc_ivar: 0x4a48
+  __DATA.__objc_ivar: 0x4a60
   __DATA.__data: 0x3b30
   __DATA.__bss: 0x1c10
   __DATA.__common: 0x68

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24252
-  Symbols:   28870
-  CStrings:  34834
+  Functions: 24278
+  Symbols:   28905
+  CStrings:  34893
 
Symbols:
+ _kATXIsNotificationSummaryEnabled
+ _kATXNotificationSummaryStatus
+ _OBJC_CLASS_$_ATXRecentAndSuggestedAppsLayoutSelector
+ _OBJC_METACLASS_$_ATXLayoutSelector
+ _kATXNotificationPriorityStatus
+ _kATXNumberOfNotificationsInStack
+ _OBJC_METACLASS_$_ATXRecentAndSuggestedAppsLayoutSelector
+ _OBJC_CLASS_$_ATXLayoutGenerator
+ _kATXIsPriorityNotificationEnabled
CStrings:
+ "-[ATXFaceGalleryLayoutGenerator _generateSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:assetDescriptors:otherParameters:semanticType:]"
+ "_recencyLookBackSeconds"
+ ":numberOfNotificationsInStack"
+ "setIsNotificationSummaryEnabled:"
+ "setNotificationSummaryStatus:"
+ "_notificationSummaryStatus"
+ "initWithNotificationAndSuggestionDatabase:bookmark:notificationEventPublisher:suggestionPublisher:suggestionInteractionEventPublisher:notificationGroupEventPublisher:notificationDeliveryEventPublisher:"
+ "shouldRemoveDescriptorFromFeatured:withDescriptorsToRemove:"
+ "priorityStatus"
+ "ALTER TABLE notifications ADD COLUMN notificationSummaryStatus INTEGER NOT NULL DEFAULT 0"
+ "recentAppsHeuristicMaxRecents"
+ "initWithRankedSuggestions:layoutsToConsider:hyperParameters:suggestionDeduplicator:"
+ "initWithSuggestionDeduplicator:hyperParameters:maxRecents:recencyLookBackSeconds:"
+ "@48@0:8@16@24Q32d40"
+ "initWithSuggestionDeduplicator:hyperParameters:maxRecents:recencyLookBackSeconds:appLaunchPublisher:"
+ ":notificationPriorityStatus"
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
+ "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :receivedMode, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isDeliveredInPrioritySection, :isSummarized, :isPartOfStack, :isStackSummary, 0, :numberOfNotificationsInStack, :notificationPriorityStatus, :notificationSummaryStatus, :isPriorityNotificationEnabled, :isNotificationSummaryEnabled)"
+ "Recency Blending: recentlyLaunchedApps count: %!l(MISSING)u"
+ "isPriorityNotificationEnabled"
+ "setNotificationPriorityStatus:"
+ "layoutsToConsiderForConsumerSubType:"
+ "ALTER TABLE notifications ADD COLUMN isNotificationSummaryEnabled INTEGER NOT NULL DEFAULT 0"
+ "notificationSummaryStatus"
+ "TQ,N,V_numberOfNotificationsInStack"
+ "generateValidLayouts"
+ "TQ,N,V_notificationPriorityStatus"
+ "isNotificationSummaryEnabled"
+ "_numberOfNotificationsInStack"
+ "ALTER TABLE notifications ADD COLUMN numberOfNotificationsInStack INTEGER NOT NULL DEFAULT 0"
+ "TB,N,V_isNotificationSummaryEnabled"
+ "descriptorsToRemoveFromSectionWithSemanticType:parameters:"
+ "recent_app_heuristic"
+ "_notificationPriorityStatus"
+ "orderedSetWithCapacity:"
+ "RecentAppsHeuristicMaxRecents"
+ ":isPriorityNotificationEnabled"
+ "setDictionary:"
+ "notificationPriorityStatus"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "recentAppsHeuristicLookBackSeconds"
+ "lockScreenBundleIdsWithReply:"
+ "setNumberOfNotificationsInStack:"
+ "deduplicator"
+ "_isPriorityNotificationEnabled"
+ "_getATXProactiveSuggestionForRecentAppLaunch:"
+ "-[ATXRecentAndSuggestedAppsLayoutSelector _accumulateRecentAppLaunchBundleIds]"
+ "_generatedHeroSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:heroSectionOrder:"
+ "RecentAppsHeuristicLookBackSeconds"
+ "+[ATXFaceSuggestionAssetParameters loadAssetParametersDictionaryFromPath:]"
+ "descriptorsToRemoveFromFeatured"
+ "_accumulateRecentAppLaunchBundleIds"
+ ":isNotificationSummaryEnabled"
+ "mergeWithOthers:"
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
+ ":receivedMode"
+ "Recency Blending: Unable to generate any valid layouts for consumerSubType: %!@(MISSING)."
+ "ALTER TABLE notifications ADD COLUMN isPriorityNotificationEnabled INTEGER NOT NULL DEFAULT 0"
+ "setIsPriorityNotificationEnabled:"
+ "@64@0:8@16@24@32@40@48q56"
+ ":notificationSummaryStatus"
+ "summaryStatus"
+ "TB,N,V_isPriorityNotificationEnabled"
+ "-[ATXFaceGalleryLayoutGenerator _generatedHeroSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:heroSectionOrder:]"
+ "ALTER TABLE notifications ADD COLUMN notificationPriorityStatus INTEGER NOT NULL DEFAULT 0"
+ "loadAssetParametersDictionaryFromPath:"
+ "Recency Blending: Generating layouts for non-homescreen consumerSubType %!{(MISSING)public}@ with %!l(MISSING)u ranked and filtered suggestions"
+ "_generateSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:assetDescriptors:otherParameters:semanticType:"
+ "TQ,N,V_notificationSummaryStatus"
+ "numberOfNotificationsInStack"
+ "@56@0:8@16@24Q32d40@48"
+ "Recency Blending: Layout Selector asked to provide validLayouts."
+ "_isNotificationSummaryEnabled"
+ "ATXRecentAndSuggestedAppsLayoutSelector"
+ "_maxRecents"
- "shouldRemoveDescriptorFromFeatured:"
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isSummarized,     isPartOfStack,     isStackSummary,     isDeliveredInPrioritySection,     isDeterminedUrgentByModel FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
- "_generatedHeroSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:"
- "descriptorsToRemoveFromSectionWithSemanticType:"
- "_generateSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:assetDescriptors:semanticType:"
- ":isDeterminedUrgentByModel"
- "_isDeterminedUrgentByModel"
- "-[ATXFaceGalleryLayoutGenerator _generatedHeroSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:]"
- "@56@0:8@16@24@32@40q48"
- "TB,N,V_isDeterminedUrgentByModel"
- "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :modeIdentifier, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isSummarized, :isPartOfStack, :isStackSummary, :isDeliveredInPrioritySection, :isDeterminedUrgentByModel)"
- "_loadAssetParametersDictionaryFromPath:"
- "_assetParameters"
- "setIsDeterminedUrgentByModel:"
- "@\"ATXFaceSuggestionAssetParameters\""
- "+[ATXFaceSuggestionAssetParameters _loadAssetParametersDictionaryFromPath:]"
- "-[ATXFaceGalleryLayoutGenerator _generateSectionWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:assetDescriptors:semanticType:]"
- "initWithNotificationAndSuggestionDatabase:bookmark:notificationEventPublisher:suggestionPublisher:suggestionInteractionEventPublisher:notificationGroupEventPublisher:"
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     deliveryReason,     firstUI,     mostRecentUI,     receivedMode,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isSummarized,     isPartOfStack,     isStackSummary,     isDeliveredInPrioritySection,     isDeterminedUrgentByModel FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
- ":modeIdentifier"

```
