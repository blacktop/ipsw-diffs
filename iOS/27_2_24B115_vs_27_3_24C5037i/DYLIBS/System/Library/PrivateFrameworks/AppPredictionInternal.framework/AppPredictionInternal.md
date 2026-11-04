## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-678.0.1.0.0
-  __TEXT.__text: 0x47d2a0
-  __TEXT.__objc_methlist: 0x38f3c
-  __TEXT.__const: 0x450a
-  __TEXT.__cstring: 0x59872
-  __TEXT.__oslogstring: 0x3bd49
-  __TEXT.__gcc_except_tab: 0xf4a0
+678.2.1.0.3
+  __TEXT.__text: 0x47ecec
+  __TEXT.__objc_methlist: 0x3902c
+  __TEXT.__const: 0x44fa
+  __TEXT.__cstring: 0x5ad12
+  __TEXT.__oslogstring: 0x3bea9
+  __TEXT.__gcc_except_tab: 0xf4d4
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
-  __TEXT.__swift5_typeref: 0x14f2
+  __TEXT.__swift5_typeref: 0x14c6
   __TEXT.__constg_swiftt: 0x1dc0
   __TEXT.__swift5_reflstr: 0xc04
   __TEXT.__swift5_fieldmd: 0x1024

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x150
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_capture: 0x6f8
+  __TEXT.__swift5_capture: 0x6e0
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12878
+  __TEXT.__unwind_info: 0x12948
   __TEXT.__eh_frame: 0x262c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc0f8
+  __DATA_CONST.__const: 0xc230
   __DATA_CONST.__objc_classlist: 0x1f58
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1c020
+  __DATA_CONST.__objc_selrefs: 0x1c0c0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x14f8
   __DATA_CONST.__objc_arraydata: 0x12f0
   __DATA_CONST.__got: 0x39c8
-  __AUTH_CONST.__const: 0x8d38
-  __AUTH_CONST.__cfstring: 0x3b300
-  __AUTH_CONST.__objc_const: 0x83bf0
+  __AUTH_CONST.__const: 0x8e70
+  __AUTH_CONST.__cfstring: 0x3bc80
+  __AUTH_CONST.__objc_const: 0x83d78
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3468
   __AUTH_CONST.__objc_arrayobj: 0x1098
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x21e8
+  __AUTH_CONST.__auth_got: 0x21f0
   __AUTH.__objc_data: 0x4008
   __AUTH.__data: 0x2178
-  __DATA.__objc_ivar: 0x4aac
+  __DATA.__objc_ivar: 0x4abc
   __DATA.__data: 0x3d18
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0x10088
-  __DATA_DIRTY.__data: 0xd28
+  __DATA_DIRTY.__data: 0xd18
   __DATA_DIRTY.__bss: 0xbb8
   __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25718
-  Symbols:   36769
-  CStrings:  12414
+  Functions: 25767
+  Symbols:   36813
+  CStrings:  12517
 
Symbols:
+ +[ATXMediaActionPrediction hasMediaToPlayForINPlayMediaIntent:]
+ -[ATXFaceSuggestionParametersAmbient classicAnalogSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient classicCalendarSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient classicDigitalSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient descriptorsToExcludeFromSections]
+ -[ATXFaceSuggestionParametersAmbient homeCameraSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient homeModularSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient memoriesSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient modularSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient photoFrameSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient reflectionsDigitalSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient responsiveArtSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient sharedPhotoFrameSectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient snoopySectionDescriptors]
+ -[ATXFaceSuggestionParametersAmbient weatherSectionDescriptors]
+ -[ATXNotificationAndSuggestionDatabase _latestOutcomeForNotification:]
+ -[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:timestamp:]
+ -[ATXNotificationTelemetryQueryResult priorityFeedback]
+ -[ATXNotificationTelemetryQueryResult resolutionEventType]
+ -[ATXNotificationTelemetryQueryResult setPriorityFeedback:]
+ -[ATXNotificationTelemetryQueryResult setResolutionEventType:]
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table93
+ _ATXStringToFaceGallerySectionAmbientSemanticType
+ _OBJC_IVAR_$_ATXFaceSuggestionParametersAmbient._descriptorsToExcludeFromSections
+ _OBJC_IVAR_$_ATXNotificationHandleSummaryMetrics._unresolvedNotificationCount
+ _OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._priorityFeedback
+ _OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._resolutionEventType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ATXWidgetDescriptorCacheObserver
+ ___62-[ATXFaceSuggestionParametersAmbient snoopySectionDescriptors]_block_invoke
+ ___63-[ATXFaceSuggestionParametersAmbient modularSectionDescriptors]_block_invoke
+ ___63-[ATXFaceSuggestionParametersAmbient weatherSectionDescriptors]_block_invoke
+ ___64-[ATXFaceSuggestionParametersAmbient memoriesSectionDescriptors]_block_invoke
+ ___66-[ATXFaceSuggestionParametersAmbient homeCameraSectionDescriptors]_block_invoke
+ ___66-[ATXFaceSuggestionParametersAmbient photoFrameSectionDescriptors]_block_invoke
+ ___67-[ATXFaceSuggestionParametersAmbient homeModularSectionDescriptors]_block_invoke
+ ___69-[ATXFaceSuggestionParametersAmbient classicAnalogSectionDescriptors]_block_invoke
+ ___69-[ATXFaceSuggestionParametersAmbient responsiveArtSectionDescriptors]_block_invoke
+ ___70-[ATXFaceSuggestionParametersAmbient classicDigitalSectionDescriptors]_block_invoke
+ ___70-[ATXNotificationAndSuggestionDatabase _latestOutcomeForNotification:]_block_invoke
+ ___70-[ATXNotificationAndSuggestionDatabase _latestOutcomeForNotification:]_block_invoke_2
+ ___70-[ATXNotificationAndSuggestionDatabase _latestOutcomeForNotification:]_block_invoke_3
+ ___70-[ATXNotificationAndSuggestionDatabase _latestOutcomeForNotification:]_block_invoke_4
+ ___71-[ATXFaceSuggestionParametersAmbient classicCalendarSectionDescriptors]_block_invoke
+ ___72-[ATXFaceSuggestionParametersAmbient sharedPhotoFrameSectionDescriptors]_block_invoke
+ ___74-[ATXFaceSuggestionParametersAmbient reflectionsDigitalSectionDescriptors]_block_invoke
+ ___94-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:timestamp:]_block_invoke
+ ___94-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:timestamp:]_block_invoke_2
+ ___94-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:timestamp:]_block_invoke_3
+ ___94-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:timestamp:]_block_invoke_4
+ ___block_descriptor_56_e8_32s_e29_v16?0"_PASSqliteStatement"8ls32l8
+ _kATXAddNotificationUUIDToNotifications
+ _kATXAddPriorityFeedbackToNotifications
+ _kATXAddResolutionUIToNotifications
+ _kATXEarlierDeliveryIndex
+ _kATXLatestOutcomeForNotificationQuery
+ _kATXRetireNotificationWithEndedDeliveryQuery
+ _kATXUpdateEarlierDeliveryUIQuery
+ _kATXUpdateNotificationPriorityFeedbackQuery
- -[ATXNotificationAndSuggestionDatabase setAllNotificationsToClearedExceptProminent]
- -[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]
- GCC_except_table173
- GCC_except_table178
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATXWidgetDescriptorCacheObserver
- ___83-[ATXNotificationAndSuggestionDatabase setAllNotificationsToClearedExceptProminent]_block_invoke
- ___83-[ATXNotificationAndSuggestionDatabase setAllNotificationsToClearedExceptProminent]_block_invoke_2
- ___83-[ATXNotificationAndSuggestionDatabase setAllNotificationsToClearedExceptProminent]_block_invoke_3
- ___84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke
- ___84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke_2
- ___84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke_3
- ___84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke_4
- _kATXChangeActiveStatusGivenProminenceQuery
- _symbolic SDySS_____G 10Foundation4DateV
- _symbolic SDySS_____Gz_Xx 10Foundation4DateV
- _symbolic _____ySS_____G s18_DictionaryStorageC 10Foundation4DateV
CStrings:
+ " UPDATE notifications SET   firstUI = COALESCE(firstUI, :nextUI),   mostRecentUI = :nextUI,   isDeliveredInPrioritySection = (COALESCE(isDeliveredInPrioritySection, 0) | (:nextUI = :priorityNotificationUI)) WHERE   notificationUUID IN _pas_nsarray(:notificationUUIDs) AND   receiveTimestamp <= :timestamp AND   NOT EXISTS (     SELECT 1 FROM notifications AS laterDelivery     WHERE (laterDelivery.uuid = notifications.notificationUUID OR laterDelivery.notificationUUID = notifications.notificationUUID) AND       laterDelivery.receiveTimestamp > notifications.receiveTimestamp AND laterDelivery.receiveTimestamp <= :timestamp) "
+ " UPDATE notifications SET   firstUI = COALESCE(firstUI, :nextUI),   mostRecentUI = :nextUI,   isDeliveredInPrioritySection = (COALESCE(isDeliveredInPrioritySection, 0) | (:nextUI = :priorityNotificationUI)) WHERE   uuid IN _pas_nsarray(:notificationUUIDs) AND   NOT (receiveTimestamp > :timestamp AND EXISTS (     SELECT 1 FROM notifications AS earlierDelivery     WHERE earlierDelivery.notificationUUID = notifications.uuid AND earlierDelivery.receiveTimestamp <= :timestamp)) "
+ "%s: no section order provided in ambient asset parameters, or asset parameters missing!"
+ "-[ATXFaceGalleryLayoutGenerator _ambientFaceGallerySectionsWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:ambientParameters:]"
+ "-[ATXFaceSuggestionParametersAmbient classicAnalogSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient classicCalendarSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient classicDigitalSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient homeCameraSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient homeModularSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient memoriesSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient modularSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient photoFrameSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient reflectionsDigitalSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient responsiveArtSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient sharedPhotoFrameSectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient snoopySectionDescriptors]_block_invoke"
+ "-[ATXFaceSuggestionParametersAmbient weatherSectionDescriptors]_block_invoke"
+ ":clear"
+ ":clearAll"
+ ":expired"
+ ":priorityFeedback"
+ ":priorityNotificationUI"
+ ":removed"
+ ":resolutionUI"
+ ":retiredUUID"
+ "ALTER TABLE notifications ADD COLUMN notificationUUID TEXT"
+ "ALTER TABLE notifications ADD COLUMN priorityFeedback INTEGER"
+ "ALTER TABLE notifications ADD COLUMN resolutionUI INTEGER"
+ "CREATE INDEX earlierDeliveryIndex ON notifications (notificationUUID) WHERE notificationUUID IS NOT NULL"
+ "ClassicAnalogSectionDescriptors"
+ "ClassicCalendarSectionDescriptors"
+ "ClassicDigitalSectionDescriptors"
+ "Cleared"
+ "ClearedAll"
+ "Deduplicated"
+ "DismissedBanner"
+ "Encountered an unknown tvOS poster extension identifier: %@"
+ "Error fetching latest outcome for notification %@: %@"
+ "Error recording priority feedback for notification event %@: %@"
+ "Error retiring ended delivery for notification event %@: %@"
+ "ExpandedNotification"
+ "Expired"
+ "FACE_GALLERY_SECTION_SUBTITLE_CLASSIC_ANALOG"
+ "FACE_GALLERY_SECTION_SUBTITLE_CLASSIC_CALENDAR"
+ "FACE_GALLERY_SECTION_SUBTITLE_CLASSIC_DIGITAL"
+ "FACE_GALLERY_SECTION_SUBTITLE_HOME_CAMERA"
+ "FACE_GALLERY_SECTION_SUBTITLE_HOME_MODULAR"
+ "FACE_GALLERY_SECTION_SUBTITLE_MEMORIES_IOS"
+ "FACE_GALLERY_SECTION_SUBTITLE_MODULAR_IOS"
+ "FACE_GALLERY_SECTION_SUBTITLE_PHOTO_FRAME"
+ "FACE_GALLERY_SECTION_SUBTITLE_RESPONSIVE_ART"
+ "FACE_GALLERY_SECTION_SUBTITLE_SHARED_PHOTO_FRAME"
+ "FACE_GALLERY_SECTION_SUBTITLE_SNOOPY"
+ "FACE_GALLERY_SECTION_TITLE_CLASSIC_ANALOG"
+ "FACE_GALLERY_SECTION_TITLE_CLASSIC_CALENDAR"
+ "FACE_GALLERY_SECTION_TITLE_CLASSIC_DIGITAL"
+ "FACE_GALLERY_SECTION_TITLE_HOME_CAMERA"
+ "FACE_GALLERY_SECTION_TITLE_HOME_MODULAR"
+ "FACE_GALLERY_SECTION_TITLE_MEMORIES"
+ "FACE_GALLERY_SECTION_TITLE_MODULAR"
+ "FACE_GALLERY_SECTION_TITLE_PHOTO_FRAME"
+ "FACE_GALLERY_SECTION_TITLE_RESPONSIVE_ART"
+ "FACE_GALLERY_SECTION_TITLE_SHARED_PHOTO_FRAME"
+ "FACE_GALLERY_SECTION_TITLE_SNOOPY"
+ "HomeCameraSectionDescriptors"
+ "HomeModularSectionDescriptors"
+ "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :receivedMode, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isDeliveredInPrioritySection, :isSummarized, :isPartOfStack, :isStackSummary, 0, :numberOfNotificationsInStack, :notificationPriorityStatus, :notificationSummaryStatus, :isPriorityNotificationEnabled, :isNotificationSummaryEnabled, NULL, NULL, NULL, NULL)"
+ "LegacyInteractionDetail"
+ "Localizable-GalleryAmbient"
+ "Media prediction for %@ has no media items, container, or buckets. Resolving as a nil prediction."
+ "MemoriesSectionDescriptors"
+ "ModularSectionDescriptors"
+ "MovedOffLockScreen"
+ "Negative"
+ "OpenedApp"
+ "PhotoFrameSectionDescriptors"
+ "Positive"
+ "PulledDownBanner"
+ "ReflectionsDigitalSectionDescriptors"
+ "RemovedWithoutUserAction"
+ "ReportedConcern"
+ "ResponsiveArtSectionDescriptors"
+ "SELECT     COALESCE(notificationUUID, uuid) AS uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp,     priorityFeedback,     resolutionUI FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
+ "SELECT     COALESCE(notificationUUID, uuid) AS uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp,     priorityFeedback,     resolutionUI FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
+ "SELECT latestOutcome FROM notifications WHERE uuid = :uuid"
+ "SharedPhotoFrameSectionDescriptors"
+ "SnoopySectionDescriptors"
+ "SpringBoardRestarted"
+ "TappedActionButton"
+ "TappedNotification"
+ "UPDATE notifications SET latestOutcome = :latestOutcome, latestOutcomeTimestamp = :latestOutcomeTimestamp, resolutionUI = :resolutionUI, isProminent = (isProminent & :isProminent), isActive = (isActive & :isActive) WHERE uuid = :uuid"
+ "UPDATE notifications SET nextAppLaunchTimestamp = :nextAppLaunchTimestamp WHERE bundleId = :bundleId AND nextAppLaunchTimestamp IS NULL AND receiveTimestamp >= :receivedDateAfter AND receiveTimestamp < :nextAppLaunchTimestamp"
+ "UPDATE notifications SET notificationUUID = uuid, uuid = :retiredUUID WHERE uuid = :uuid AND latestOutcome IN (:defaultAction, :supplementaryAction, :clear, :clearAll, :removed, :appLaunch, :expired) AND recordTimestamp IS NOT :recordTimestamp"
+ "UPDATE notifications SET priorityFeedback = :priorityFeedback WHERE uuid = :uuid"
+ "com.apple.ClockFacePosters.ResponsiveArtPosterExtension"
+ "com.apple.ClockFacePosters.SimpleClockPosterExtension"
+ "com.apple.ClockFacePosters.SimpleDigitalPosterExtension"
+ "com.apple.Home.CameraFace"
+ "com.apple.Home.HomeFace"
+ "com.apple.PhotosUIPrivate.PhotosClockPoster"
+ "com.apple.PhotosUIPrivate.PhotosMemoriesPoster"
+ "com.apple.PhotosUIPrivate.PhotosSharedAlbumPoster"
+ "com.apple.WatchFacesWallpaperSupport.SnoopyPoster"
+ "com.apple.WidgetFace.WidgetFaceExtension"
+ "com.apple.mobilecal.CalendarPosterExtension"
+ "com.apple.weather.face"
+ "earlierDeliveryIndex"
+ "notificationUUID"
+ "priorityFeedback"
+ "resolutionAction"
+ "resolutionUI"
- " UPDATE notifications SET   firstUI = COALESCE(firstUI, :nextUI),   mostRecentUI = :nextUI WHERE   uuid IN _pas_nsarray(:notificationUUIDs) "
- "Error updating notification while clearing all except prominent. Error: %@"
- "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :receivedMode, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isDeliveredInPrioritySection, :isSummarized, :isPartOfStack, :isStackSummary, 0, :numberOfNotificationsInStack, :notificationPriorityStatus, :notificationSummaryStatus, :isPriorityNotificationEnabled, :isNotificationSummaryEnabled, NULL)"
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
- "UPDATE notifications SET latestOutcome = :latestOutcome, isActive = :isActive WHERE isProminent = :isProminent"
- "UPDATE notifications SET latestOutcome = :latestOutcome, latestOutcomeTimestamp = :latestOutcomeTimestamp, isProminent = (isProminent & :isProminent), isActive = (isActive & :isActive) WHERE uuid = :uuid"
- "UPDATE notifications SET nextAppLaunchTimestamp = :nextAppLaunchTimestamp WHERE bundleId = :bundleId AND receiveTimestamp >= :receivedDateAfter AND receiveTimestamp < :nextAppLaunchTimestamp"
```
