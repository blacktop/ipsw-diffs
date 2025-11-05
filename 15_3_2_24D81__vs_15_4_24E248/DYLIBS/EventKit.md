## EventKit

> `/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit`

```diff

-1902.3.1.100.0
-  __TEXT.__text: 0x14eddc
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0x138f0
-  __TEXT.__const: 0x5e2
-  __TEXT.__cstring: 0xb2b4
-  __TEXT.__oslogstring: 0xd03e
-  __TEXT.__gcc_except_tab: 0x3734
+1902.5.6.0.0
+  __TEXT.__text: 0x150d1c
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x1480c
+  __TEXT.__const: 0x5f2
+  __TEXT.__cstring: 0xb052
+  __TEXT.__oslogstring: 0xd12e
+  __TEXT.__gcc_except_tab: 0x3768
   __TEXT.__dlopen_cstrs: 0x3f2
   __TEXT.__ustring: 0x162
   __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_typeref: 0x267
+  __TEXT.__swift5_typeref: 0x253
   __TEXT.__swift5_reflstr: 0x1b2
   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4ed0
+  __TEXT.__unwind_info: 0x5010
   __TEXT.__objc_classname: 0x18ea
-  __TEXT.__objc_methname: 0x2bf03
-  __TEXT.__objc_methtype: 0x40e0
-  __TEXT.__objc_stubs: 0x1f4e0
-  __DATA_CONST.__got: 0x15c8
-  __DATA_CONST.__const: 0x11a8
+  __TEXT.__objc_methname: 0x2c252
+  __TEXT.__objc_methtype: 0x40f1
+  __TEXT.__objc_stubs: 0x1f700
+  __DATA_CONST.__got: 0x15d8
+  __DATA_CONST.__const: 0x1200
   __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa268
+  __DATA_CONST.__objc_selrefs: 0xa3c0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__auth_got: 0x958
-  __AUTH_CONST.__const: 0x54b0
+  __AUTH_CONST.__auth_got: 0x920
+  __AUTH_CONST.__const: 0x54d0
   __AUTH_CONST.__cfstring: 0x94a0
-  __AUTH_CONST.__objc_const: 0x17508
+  __AUTH_CONST.__objc_const: 0x15b98
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH.__objc_data: 0x2888
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0xbe4
-  __DATA.__data: 0x16b0
+  __DATA.__objc_ivar: 0xbec
+  __DATA.__data: 0x16a0
   __DATA.__bss: 0xb68
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1ea0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7A79A7E8-C49C-3774-8FC8-C603022F39D4
-  Functions: 8383
-  Symbols:   17311
-  CStrings:  10859
+  UUID: 865BF02C-D35F-31FB-8DD6-15468ADD28BB
+  Functions: 8565
+  Symbols:   17533
+  CStrings:  10872
 
Symbols:
+ +[EKAlarm _processIsAllowedToCreateProcedureAlarms]
+ +[EKAlarm knownIdentityKeysForComparison].cold.1
+ +[EKAlarm knownRelationshipMultiValueKeys].cold.1
+ +[EKAlarm knownRelationshipSingleValueKeys].cold.1
+ +[EKAlarm knownRelationshipWeakKeys].cold.1
+ +[EKAlarm knownSingleValueKeysForComparison].cold.1
+ +[EKAttachment _compressItemAtURLToTemporaryDirectory:]
+ +[EKAttachment _compressItemAtURLToTemporaryDirectory:].cold.1
+ +[EKAttachment _compressItemAtURLToTemporaryDirectory:].cold.2
+ +[EKAttachment _prepareFileAtURLInTemporaryDirectory:]
+ +[EKAttachment _prepareFileAtURLInTemporaryDirectory:].cold.1
+ +[EKAttachment _prepareFileAtURLInTemporaryDirectory:].cold.2
+ +[EKAttachment _prepareFileAtURLInTemporaryDirectory:].cold.3
+ +[EKAttachment knownIdentityKeysForComparison].cold.1
+ +[EKAttachment knownRelationshipWeakKeys].cold.1
+ +[EKAttachment knownSingleValueKeysForComparison].cold.1
+ +[EKAutocompletePendingSearch _eventKitQueue].cold.1
+ +[EKAutocompletePendingSearch _queue].cold.1
+ +[EKBirthdayListener sharedListener].cold.1
+ +[EKCalendar knownIdentityKeysForComparison].cold.1
+ +[EKCalendar knownRelationshipMultiValueKeys].cold.1
+ +[EKCalendar knownRelationshipSingleValueKeys].cold.1
+ +[EKCalendar knownRelationshipWeakKeys].cold.1
+ +[EKCalendar knownSingleValueKeysForComparison].cold.1
+ +[EKCalendar orderSortDescriptors].cold.1
+ +[EKCalendar(EKObjectChangeSummarizer) EKObjectChangeSummarizer_multiValueDiffKeys].cold.1
+ +[EKCalendar(EKObjectChangeSummarizer) EKObjectChangeSummarizer_singleValueDiffKeys].cold.1
+ +[EKCalendarItem knownDerivedRelationshipKeys].cold.1
+ +[EKCalendarItem knownIdentityKeysForComparison].cold.1
+ +[EKCalendarItem knownRelationshipMultiValueKeysForValidation].cold.1
+ +[EKCalendarItem knownRelationshipMultiValueKeys].cold.1
+ +[EKCalendarItem knownRelationshipSingleValueKeysForValidation].cold.1
+ +[EKCalendarItem knownRelationshipSingleValueKeys].cold.1
+ +[EKCalendarItem knownRelationshipWeakKeys].cold.1
+ +[EKCalendarItem knownSingleValueKeysForComparison].cold.1
+ +[EKCalendarItem(EKObjectChangeSummarizer) EKObjectChangeSummarizer_multiValueDiffKeys].cold.1
+ +[EKCalendarItem(EKObjectChangeSummarizer) EKObjectChangeSummarizer_singleValueDiffKeys].cold.1
+ +[EKCalendarPreferences calendarPreferences].cold.1
+ +[EKCalendarSuggestionNotification _queue].cold.1
+ +[EKCalendarVisibilityManager _defaultQueue].cold.1
+ +[EKColor knownIdentityKeysForComparison].cold.1
+ +[EKConferenceUtils _workQueue].cold.1
+ +[EKConferenceUtils appRecordCache].cold.1
+ +[EKDebugPreferences shared].cold.1
+ +[EKDiff _keysToIgnoreForComputingDiff].cold.1
+ +[EKDiff _populateIdentityKeysForDiff:keysToIgnore:]
+ +[EKDiff _populateIdentityKeysForDiff:keysToIgnore:].cold.1
+ +[EKDiff _populateIdentityKeysForDiff:keysToIgnore:].cold.2
+ +[EKDiff _populateImmutableKeysForDiff:keysToIgnore:]
+ +[EKDiff _populateImmutableKeysForDiff:keysToIgnore:].cold.1
+ +[EKDiff _populateImmutableKeysForDiff:keysToIgnore:].cold.2
+ +[EKDiff _populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:]
+ +[EKDiff _populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.1
+ +[EKDiff _populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.2
+ +[EKDiff _populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.3
+ +[EKDiff _populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:]
+ +[EKDiff _populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.1
+ +[EKDiff _populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.2
+ +[EKDiff _populateSingleValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:]
+ +[EKDiff _populateSingleValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:].cold.1
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:]
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:].cold.1
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:].cold.2
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:].cold.3
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:].cold.4
+ +[EKDiff diffBetweenObject:andObject:fetchKeysToIgnoreBlock:].cold.5
+ +[EKDiff keysToIgnoreForComparingUIVisiblePropertiesOfObject:andObject:]
+ +[EKEvent _basicChangesRequiringSpanAll].cold.1
+ +[EKEvent _relatedCachedTimeKeys].cold.1
+ +[EKEvent knownKeysToSkipForFutureChanges].cold.1
+ +[EKEvent knownKeysToUseForFutureChanges].cold.1
+ +[EKEvent knownPerUserPropertyKeys].cold.1
+ +[EKEvent knownRequireRSVPKeys].cold.1
+ +[EKEvent uniqueIDForDetachedOccurrenceOfEvent:withOriginalStartDate:timeZone:allDay:]
+ +[EKEventAction knownIdentityKeysForComparison].cold.1
+ +[EKEventActionHandler _displayStringForDate:].cold.1
+ +[EKEventActionHandler _logHandle].cold.1
+ +[EKEventActionHandler sharedInstance].cold.1
+ +[EKEventStore _contextForNotificationWithChangeType:changedObjectIDs:].cold.1
+ +[EKEventStore classForEntityName:].cold.1
+ +[EKEventTimeDetector dateResultsFromString:referenceDate:].cold.1
+ +[EKExceptionDate knownIdentityKeysForComparison].cold.1
+ +[EKImage knownIdentityKeysForComparison].cold.1
+ +[EKLogSubsystem autocomplete].cold.1
+ +[EKLogSubsystem availabilitySearch].cold.1
+ +[EKLogSubsystem defaultCategory].cold.1
+ +[EKLogSubsystem exchangeSync].cold.1
+ +[EKLogSubsystem junk].cold.1
+ +[EKLogSubsystem savingSignposts].cold.1
+ +[EKMapsUtilities geocodeEventIfNeeded:].cold.1
+ +[EKNotification knownRelationshipSingleValueKeys].cold.1
+ +[EKNotification knownRelationshipWeakKeys].cold.1
+ +[EKNotificationCollection knownRelationshipMultiValueKeys].cold.1
+ +[EKNullFetchRequestToken sharedToken].cold.1
+ +[EKObject(Shared) knownRelationshipWeakKeys].cold.1
+ +[EKObjectID objectIDWithURL:].cold.7
+ +[EKParticipant knownIdentityKeysForComparison].cold.1
+ +[EKParticipant knownRelationshipWeakKeys].cold.1
+ +[EKParticipant knownSingleValueKeysForComparison].cold.1
+ +[EKParticipantForSorting _cache].cold.1
+ +[EKPersistentAlarm defaultPropertiesToLoad].cold.1
+ +[EKPersistentAlarm relations].cold.1
+ +[EKPersistentAttachment relations].cold.1
+ +[EKPersistentAttendee relations].cold.1
+ +[EKPersistentCalendar defaultPropertiesToLoad].cold.1
+ +[EKPersistentCalendar relations].cold.1
+ +[EKPersistentCalendarItem relations].cold.1
+ +[EKPersistentColor defaultPropertiesToLoad].cold.1
+ +[EKPersistentColor relations].cold.1
+ +[EKPersistentEvent defaultPropertiesToLoad].cold.1
+ +[EKPersistentEventAction relations].cold.1
+ +[EKPersistentExceptionDate relations].cold.1
+ +[EKPersistentImage defaultPropertiesToLoad].cold.1
+ +[EKPersistentImage relations].cold.1
+ +[EKPersistentInviteReplyNotification defaultPropertiesToLoad].cold.1
+ +[EKPersistentLocation defaultPropertiesToLoad].cold.1
+ +[EKPersistentLocation relations].cold.1
+ +[EKPersistentNotification relations].cold.1
+ +[EKPersistentObject propertiesToUnloadOnCommit].cold.1
+ +[EKPersistentOrganizer relations].cold.1
+ +[EKPersistentParticipant defaultPropertiesToLoad].cold.1
+ +[EKPersistentRecurrenceRule defaultPropertiesToLoad].cold.1
+ +[EKPersistentRecurrenceRule relations].cold.1
+ +[EKPersistentResourceChange defaultPropertiesToLoad].cold.1
+ +[EKPersistentResourceChange relations].cold.1
+ +[EKPersistentSharee defaultPropertiesToLoad].cold.1
+ +[EKPersistentSharee relations].cold.1
+ +[EKPersistentSource defaultPropertiesToLoad].cold.1
+ +[EKPersistentSource relations].cold.1
+ +[EKPersistentSuggestedEventInfo relations].cold.1
+ +[EKPersistentSyncError relations].cold.1
+ +[EKPredicateSearch signpostHandle].cold.1
+ +[EKPreferences shared].cold.1
+ +[EKRecents crAddressKindEmailString].cold.1
+ +[EKRecents crAddressKindPhoneNumberString].cold.1
+ +[EKRecents crRecentContactsLibraryClass].cold.1
+ +[EKRecents crRecentsDomainCalendarString].cold.1
+ +[EKRecurrenceRule knownIdentityKeysForComparison].cold.1
+ +[EKRecurrenceRule knownRelationshipWeakKeys].cold.1
+ +[EKRecurrenceRule knownSingleValueKeysForComparison].cold.1
+ +[EKReminderStore frozenClassForReminderClass:].cold.2
+ +[EKReminderStore log].cold.1
+ +[EKRemoteXPCConnectionFactory sharedInstance].cold.1
+ +[EKResourceChange knownRelationshipSingleValueKeys].cold.1
+ +[EKResourceChange knownRelationshipWeakKeys].cold.1
+ +[EKSharee knownIdentityKeysForComparison].cold.1
+ +[EKSharee knownSingleValueKeysForComparison].cold.1
+ +[EKSource knownIdentityKeysForComparison].cold.1
+ +[EKSource knownRelationshipSingleValueKeys].cold.1
+ +[EKSource knownSingleValueKeysForComparison].cold.1
+ +[EKStructuredLocation _stringByStrippingControlCharactersFromString:].cold.1
+ +[EKStructuredLocation knownIdentityKeysForComparison].cold.1
+ +[EKStructuredLocation knownRelationshipWeakKeys].cold.1
+ +[EKStructuredLocation knownSingleValueKeysForComparison].cold.1
+ +[EKStructuredLocation knownSingleValueKeysToSkipForUIComparison].cold.1
+ +[EKStructuredLocationPrediction _mockLocationForEvent:].cold.1
+ +[EKStructuredLocationPrediction userInteractionWithPredictedLocationOfInterest:interaction:].cold.1
+ +[EKSuggestedEventInfo knownIdentityKeysForComparison].cold.1
+ +[EKSuggestedEventInfo knownSingleValueKeysForComparison].cold.1
+ +[EKSyncError knownIdentityKeysForComparison].cold.1
+ +[EKSyncStatusUtils _permittedClassesForArchivingLastSyncErrorUserInfo].cold.1
+ +[_EKNotificationMonitor blacklistedNotificationQueue].cold.1
+ -[EKAlarm _setUrlWrapper:].cold.1
+ -[EKAlarm initWithAbsoluteDate:].cold.1
+ -[EKAlarm setUrlWrapper:].cold.1
+ -[EKAttachment URLWrapperForPendingFileCopy]
+ -[EKAttachment setURLWrapperForPendingFileCopy:]
+ -[EKAutocompletePendingSearch searchWithString:completionHandler:].cold.2
+ -[EKAvailabilitySpan initWithStartDate:endDate:type:].cold.1
+ -[EKAvailabilitySpan initWithStartDate:endDate:type:].cold.2
+ -[EKAvailabilitySpan initWithStartDate:endDate:type:].cold.3
+ -[EKCalendar externalURI].cold.1
+ -[EKCalendar snoozeAlarm:withLocation:proximity:].cold.1
+ -[EKCalendar validate:].cold.1
+ -[EKCalendarInviteReplyNotification initWithType:].cold.1
+ -[EKCalendarItem _moveToCalendar:forSavingItem:].cold.1
+ -[EKCalendarItem setOriginalItem:].cold.1
+ -[EKCalendarItem snoozeAlarm:withLocation:proximity:].cold.1
+ -[EKCalendarItem validate:].cold.1
+ -[EKCalendarSharedCalendarNotification initWithType:].cold.1
+ -[EKConferenceInvalidationRecord generateNewValidURLForOriginalURL:].cold.1
+ -[EKDaemonConnection _finishAllRepliesOnServerDeath].cold.1
+ -[EKEvent _multiValueRelatedObject:isAlsoASingleValueRelatedObjectForKey:]
+ -[EKEvent appEntityIdentifierOverride]
+ -[EKEvent appEntityIdentifier]
+ -[EKEvent externalURL].cold.1
+ -[EKEvent setAppEntityIdentifierOverride:]
+ -[EKEventStore _calendar:supportsEntityType:].cold.1
+ -[EKEventStore _handleExternalDatabaseChangeNotification:synchronously:].cold.2
+ -[EKEventStore _registerObjectImmediate:].cold.1
+ -[EKEventStore calendarWithExternalURI:].cold.2
+ -[EKEventStore calendarsForEntityType:].cold.1
+ -[EKEventStore calendarsForEntityType:inSource:].cold.1
+ -[EKEventStore databaseRestoreGenerationChangedExternally:].cold.1
+ -[EKEventStore eventWithAppEntityIdentifier:]
+ -[EKEventStore eventWithRecurrenceIdentifier:isAppEntityID:]
+ -[EKEventStore preferences]
+ -[EKEventStore publicObjectWithPersistentObject:].cold.1
+ -[EKEventStore reminderWithExternalURI:].cold.3
+ -[EKFrozenReminderAlarm initWithAlternateUniverseObject:inEventStore:withUpdatedChildObjects:].cold.1
+ -[EKFrozenReminderObject initWithREMObject:inStore:withChanges:].cold.1
+ -[EKICSImporter _createImportHandle].cold.1
+ -[EKObject _multiValueRelatedObject:isAlsoASingleValueRelatedObjectForKey:]
+ -[EKObject meltedObjectInStore:].cold.1
+ -[EKObject(Shared) _lock].cold.1
+ -[EKPersistentAttachment URLWrapperForPendingFileCopy]
+ -[EKPersistentAttachment setURLWrapperForPendingFileCopy:]
+ -[EKPersistentObject _setObjectID:inDatabaseRestoreGeneration:].cold.1
+ -[EKPersistentObject frozenObjectInStore:].cold.1
+ -[EKPersistentObject primitiveSetRelationValue:forKey:].cold.1
+ -[EKPersistentObject primitiveSetRelationValue:forKey:].cold.2
+ -[EKPersistentObject primitiveSetURLWrapperValue:forKey:]
+ -[EKPersistentObject primitiveURLWrapperValueForKey:]
+ -[EKPreferences initWithPreferences:]
+ -[EKRecurrenceRule setFirstDayOfTheWeek:].cold.1
+ -[EKRecurrenceRule setInterval:].cold.1
+ -[EKReminder externalURI].cold.1
+ -[EKVirtualConferenceExtensionContext completeRequestWithAvailableRoomTypes:completionHandler:].cold.1
+ -[EKVirtualConferenceExtensionContext completeRequestWithInvalidationSuccess:error:completionHandler:].cold.1
+ -[EKVirtualConferenceExtensionContext completeRequestWithRenewalSuccess:error:completionHandler:].cold.1
+ -[EKVirtualConferenceExtensionContext completeRequestWithVirtualConference:completionHandler:].cold.1
+ EKBundle.cold.1
+ EKLogInitIfNeeded.cold.1
+ EKTravelEngineLogInitialize.cold.1
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table184
+ GCC_except_table189
+ GCC_except_table228
+ GCC_except_table252
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table271
+ GCC_except_table275
+ GCC_except_table279
+ GCC_except_table292
+ GCC_except_table297
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table346
+ GCC_except_table349
+ GCC_except_table377
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table402
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table420
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table440
+ GCC_except_table442
+ GCC_except_table462
+ GCC_except_table467
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table483
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table528
+ GCC_except_table550
+ GCC_except_table556
+ GCC_except_table570
+ GCC_except_table579
+ GCC_except_table592
+ GCC_except_table608
+ GCC_except_table612
+ GCC_except_table631
+ GCC_except_table666
+ GCC_except_table709
+ GCC_except_table715
+ GCC_except_table733
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table748
+ GCC_except_table755
+ GCC_except_table769
+ GCC_except_table779
+ GCC_except_table794
+ GCC_except_table798
+ GCC_except_table854
+ GCC_except_table883
+ GCC_except_table94
+ OBJC_IVAR_$_EKEvent._appEntityIdentifierOverride
+ OBJC_IVAR_$_EKEventStore._preferences
+ _EKAttachmentProperty_URLWrapperForPendingFileCopy
+ _OBJC_CLASS_$_CalMockPreferenceStore
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ __102-[EKObject(Shared) _addChangesFromObject:ignoringDifferencesFrom:changesToSkip:copyingBackingObjects:]_block_invoke.58
+ __112-[EKEvent _adjustPrivacyAfterMovingOrCopyingFromCalendar:toCalendar:cachedConstraintsForOldCalendar:savingItem:]_block_invoke.297
+ __137-[EKObject(Shared) _convertBackingObjectsWithPath:updateBackingObjects:allChangedBackingObjects:eventStore:updatedBackingObjectProvider:]_block_invoke.125
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.261
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.262
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.263
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.267
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.271
+ __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.272
+ __181-[EKEventStore initWithEKOptions:path:containerProvider:tccPermissionChecker:changeTrackingClientId:enablePropertyModificationLogging:allowDelegateSources:allowedSourceIdentifiers:]_block_invoke.184
+ __181-[EKEventStore initWithEKOptions:path:containerProvider:tccPermissionChecker:changeTrackingClientId:enablePropertyModificationLogging:allowDelegateSources:allowedSourceIdentifiers:]_block_invoke.188
+ __36-[EKEventStore _loadSourcesIfNeeded]_block_invoke.292
+ __37-[EKEventStore _trackModifiedObject:]_block_invoke.cold.1
+ __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke.105
+ __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke.110
+ __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke_2.111
+ __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke_2.111.cold.1
+ __38-[EKEventStore _loadCalendarsIfNeeded]_block_invoke.376
+ __48-[EKCalendarItem _moveToCalendar:forSavingItem:]_block_invoke.123
+ __48-[EKCalendarItem _moveToCalendar:forSavingItem:]_block_invoke.126
+ __48-[EKEvent _attemptToUpdateComplexRecurrenceRule]_block_invoke.267
+ __60+[EKPersistentObject allObjectsWithChangesRelatedToObjects:]_block_invoke.122
+ __61-[EKEventStore localBirthdayCalendarCreateIfNeededWithError:]_block_invoke.310
+ __76-[EKObject(Shared) _addChanges:copyingBackingObjects:objectIdentifierBlock:]_block_invoke.66
+ __99-[EKObject(Shared) updateMultiValueCacheForChangeSet:preservingExistingAdds:objectIdentifierBlock:]_block_invoke.89
+ ___52+[EKDiff _populateIdentityKeysForDiff:keysToIgnore:]_block_invoke
+ ___53+[EKDiff _populateImmutableKeysForDiff:keysToIgnore:]_block_invoke
+ ___53-[EKPersistentObject primitiveURLWrapperValueForKey:]_block_invoke
+ ___69+[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:]_block_invoke
+ ___78+[EKDiff _populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:]_block_invoke
+ ___89+[EKDiff _populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:]_block_invoke
+ ___block_descriptor_32_e18_16?0"NSString"8l
+ ___block_descriptor_40_e40_"NSArray"24?0"EKObject"8"EKObject"16l
+ ___block_descriptor_48_e8_32s40s_e40_"NSArray"24?0"EKObject"8"EKObject"16l
+ ___block_descriptor_56_e8_32s40s_e15_B32?08Q16^B24l
+ ___block_descriptor_64_e8_32s40s48bs_e15_B32?08Q16^B24l
+ __block_literal_global.103
+ __block_literal_global.121
+ __block_literal_global.135
+ __block_literal_global.1707
+ __block_literal_global.210
+ __block_literal_global.216
+ __block_literal_global.242
+ __block_literal_global.244
+ __block_literal_global.246
+ __block_literal_global.248
+ __block_literal_global.250
+ __block_literal_global.252
+ __block_literal_global.259
+ __block_literal_global.270
+ __block_literal_global.279
+ __block_literal_global.300
+ __block_literal_global.312
+ __block_literal_global.321
+ __block_literal_global.335
+ __block_literal_global.399
+ __block_literal_global.444
+ __block_literal_global.55
+ __block_literal_global.86
+ _objc_msgSend$URLWrapperForPendingFileCopy
+ _objc_msgSend$_compressItemAtURLToTemporaryDirectory:
+ _objc_msgSend$_multiValueRelatedObject:isAlsoASingleValueRelatedObjectForKey:
+ _objc_msgSend$_populateIdentityKeysForDiff:keysToIgnore:
+ _objc_msgSend$_populateImmutableKeysForDiff:keysToIgnore:
+ _objc_msgSend$_populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:
+ _objc_msgSend$_populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:
+ _objc_msgSend$_populateSingleValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:
+ _objc_msgSend$_prepareFileAtURLInTemporaryDirectory:
+ _objc_msgSend$_processIsAllowedToCreateProcedureAlarms
+ _objc_msgSend$alertInviteeDeclines
+ _objc_msgSend$appEntityIdentifier
+ _objc_msgSend$archiveURLToFile:toFile:createPKZipArchive:error:
+ _objc_msgSend$currentProcessIsFirstPartyApp
+ _objc_msgSend$diffBetweenObject:andObject:fetchKeysToIgnoreBlock:
+ _objc_msgSend$eventWithRecurrenceIdentifier:isAppEntityID:
+ _objc_msgSend$initWithDomain:store:
+ _objc_msgSend$initWithPreferences:
+ _objc_msgSend$keysToIgnoreForComparingUIVisiblePropertiesOfObject:andObject:
+ _objc_msgSend$preferences
+ _objc_msgSend$preferencesStoreForPath:
+ _objc_msgSend$primitiveSetURLWrapperValue:forKey:
+ _objc_msgSend$primitiveURLWrapperValueForKey:
+ _objc_msgSend$setAppEntityIdentifierOverride:
+ _objc_msgSend$setURLWrapperForPendingFileCopy:
+ _objc_msgSend$uniqueIDForDetachedOccurrenceOfEvent:withOriginalStartDate:timeZone:allDay:
+ _shouldUseLegacyAccessBehavior.cold.1
+ logHandle.cold.1
- +[EKAttachment _copyFileAtURLToTemporaryDirectory:]
- +[EKAttachment _copyFileAtURLToTemporaryDirectory:].cold.1
- +[EKAttachment _copyFileAtURLToTemporaryDirectory:].cold.2
- +[EKDiff _populateIdentityKeysForDiff:]
- +[EKDiff _populateIdentityKeysForDiff:].cold.1
- +[EKDiff _populateIdentityKeysForDiff:].cold.2
- +[EKDiff _populateImmutableKeysForDiff:]
- +[EKDiff _populateImmutableKeysForDiff:].cold.1
- +[EKDiff _populateImmutableKeysForDiff:].cold.2
- +[EKDiff _populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:]
- +[EKDiff _populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:].cold.1
- +[EKDiff _populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:].cold.2
- +[EKDiff _populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:]
- +[EKDiff _populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:].cold.1
- +[EKDiff _populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:].cold.2
- +[EKDiff _populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:]
- +[EKDiff _populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:].cold.1
- +[EKDiff _populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:].cold.2
- +[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:].cold.1
- +[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:].cold.2
- +[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:].cold.3
- +[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:].cold.4
- +[EKDiff diffBetweenObject:andObject:compareUIVisiblePropertiesOnly:].cold.5
- -[EKAttachment securityScopedURLWrapperForPendingFileCopy]
- -[EKAttachment setSecurityScopedURLWrapperForPendingFileCopy:]
- -[EKEvent allowsAlarmModifications]
- -[EKPersistentAttachment securityScopedURLWrapperForPendingFileCopy]
- -[EKPersistentAttachment setSecurityScopedURLWrapperForPendingFileCopy:]
- GCC_except_table130
- GCC_except_table135
- GCC_except_table136
- GCC_except_table148
- GCC_except_table160
- GCC_except_table183
- GCC_except_table188
- GCC_except_table216
- GCC_except_table227
- GCC_except_table250
- GCC_except_table254
- GCC_except_table259
- GCC_except_table262
- GCC_except_table265
- GCC_except_table273
- GCC_except_table277
- GCC_except_table286
- GCC_except_table295
- GCC_except_table298
- GCC_except_table304
- GCC_except_table307
- GCC_except_table342
- GCC_except_table347
- GCC_except_table375
- GCC_except_table379
- GCC_except_table386
- GCC_except_table394
- GCC_except_table398
- GCC_except_table399
- GCC_except_table407
- GCC_except_table410
- GCC_except_table413
- GCC_except_table418
- GCC_except_table430
- GCC_except_table434
- GCC_except_table438
- GCC_except_table439
- GCC_except_table460
- GCC_except_table465
- GCC_except_table469
- GCC_except_table476
- GCC_except_table481
- GCC_except_table485
- GCC_except_table488
- GCC_except_table491
- GCC_except_table495
- GCC_except_table498
- GCC_except_table524
- GCC_except_table548
- GCC_except_table554
- GCC_except_table568
- GCC_except_table577
- GCC_except_table590
- GCC_except_table604
- GCC_except_table610
- GCC_except_table629
- GCC_except_table660
- GCC_except_table707
- GCC_except_table711
- GCC_except_table729
- GCC_except_table736
- GCC_except_table739
- GCC_except_table746
- GCC_except_table753
- GCC_except_table761
- GCC_except_table773
- GCC_except_table792
- GCC_except_table796
- GCC_except_table850
- GCC_except_table876
- GCC_except_table93
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- __112-[EKEvent _adjustPrivacyAfterMovingOrCopyingFromCalendar:toCalendar:cachedConstraintsForOldCalendar:savingItem:]_block_invoke.299
- __137-[EKObject(Shared) _convertBackingObjectsWithPath:updateBackingObjects:allChangedBackingObjects:eventStore:updatedBackingObjectProvider:]_block_invoke.121
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.258
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.259
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.260
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.264
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.268
- __156-[EKEventStore _processExternalChangesWithLatestTimestamp:changedObjectIDsData:deletedObjectIDOffsets:changesWereSyncStatusOnly:forceImmediateNotification:]_block_invoke.269
- __181-[EKEventStore initWithEKOptions:path:containerProvider:tccPermissionChecker:changeTrackingClientId:enablePropertyModificationLogging:allowDelegateSources:allowedSourceIdentifiers:]_block_invoke.181
- __181-[EKEventStore initWithEKOptions:path:containerProvider:tccPermissionChecker:changeTrackingClientId:enablePropertyModificationLogging:allowDelegateSources:allowedSourceIdentifiers:]_block_invoke.185
- __36-[EKEventStore _loadSourcesIfNeeded]_block_invoke.289
- __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke.101
- __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke.106
- __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke_2.107
- __38+[EKObject(Shared) _changeSetForDiff:]_block_invoke_2.107.cold.1
- __38-[EKEventStore _loadCalendarsIfNeeded]_block_invoke.373
- __48-[EKCalendarItem _moveToCalendar:forSavingItem:]_block_invoke.122
- __48-[EKCalendarItem _moveToCalendar:forSavingItem:]_block_invoke.125
- __48-[EKEvent _attemptToUpdateComplexRecurrenceRule]_block_invoke.269
- __60+[EKPersistentObject allObjectsWithChangesRelatedToObjects:]_block_invoke.120
- __61-[EKEventStore localBirthdayCalendarCreateIfNeededWithError:]_block_invoke.307
- __76-[EKObject(Shared) _addChanges:copyingBackingObjects:objectIdentifierBlock:]_block_invoke.60
- __99-[EKObject(Shared) updateMultiValueCacheForChangeSet:preservingExistingAdds:objectIdentifierBlock:]_block_invoke.84
- ___39+[EKDiff _populateIdentityKeysForDiff:]_block_invoke
- ___40+[EKDiff _populateImmutableKeysForDiff:]_block_invoke
- ___73+[EKDiff _populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:]_block_invoke
- ___84+[EKDiff _populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:]_block_invoke
- ___85+[EKDiff _populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:]_block_invoke
- ___block_descriptor_48_e8_32s_e15_B32?08Q16^B24l
- ___block_descriptor_49_e8_32s40s_e15_B32?08Q16^B24l
- ___block_descriptor_57_e8_32s40s_e15_B32?08Q16^B24l
- __block_literal_global.134
- __block_literal_global.1700
- __block_literal_global.207
- __block_literal_global.213
- __block_literal_global.236
- __block_literal_global.241
- __block_literal_global.243
- __block_literal_global.245
- __block_literal_global.247
- __block_literal_global.249
- __block_literal_global.261
- __block_literal_global.272
- __block_literal_global.277
- __block_literal_global.297
- __block_literal_global.308
- __block_literal_global.309
- __block_literal_global.318
- __block_literal_global.332
- __block_literal_global.403
- __block_literal_global.448
- __block_literal_global.49
- __block_literal_global.62
- __block_literal_global.81
- _objc_msgSend$_copyFileAtURLToTemporaryDirectory:
- _objc_msgSend$_populateIdentityKeysForDiff:
- _objc_msgSend$_populateImmutableKeysForDiff:
- _objc_msgSend$_populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:
- _objc_msgSend$_populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:
- _objc_msgSend$_populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:
- _objc_msgSend$securityScopedURLWrapperForPendingFileCopy
- _objc_msgSend$setLocalRelativePath:
- _objc_msgSend$setSecurityScopedURLWrapperForPendingFileCopy:
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _symbolic SS3key_yp5valuetSg
CStrings:
+ "@\"EKPreferences\""
+ "@\"NSArray\"24@?0@\"EKObject\"8@\"EKObject\"16"
+ "Attempted to set URL on an alarm in a process that is not allowed. Ignoring."
+ "Error creating archive of %@: %@"
+ "Found event that should have had the identifier %@ using the identifier %@ instead. Pretending that these are the same thing."
+ "T@\"EKPreferences\",R,N,V_preferences"
+ "T@\"NSString\",&,N,V_appEntityIdentifierOverride"
+ "URLWrapperForPendingFileCopy"
+ "Unable to determine if %@ is a file or directory: %@"
+ "_appEntityIdentifierOverride"
+ "_compressItemAtURLToTemporaryDirectory:"
+ "_multiValueRelatedObject:isAlsoASingleValueRelatedObjectForKey:"
+ "_populateIdentityKeysForDiff:keysToIgnore:"
+ "_populateImmutableKeysForDiff:keysToIgnore:"
+ "_populateMultiValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_populateSingleValueKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_populateSingleValueRelationshipKeysForDiff:keysToIgnore:fetchKeysToIgnoreBlock:"
+ "_prepareFileAtURLInTemporaryDirectory:"
+ "_processIsAllowedToCreateProcedureAlarms"
+ "appEntityIdentifier"
+ "appEntityIdentifierOverride"
+ "archiveURLToFile:toFile:createPKZipArchive:error:"
+ "currentProcessIsFirstPartyApp"
+ "diffBetweenObject:andObject:fetchKeysToIgnoreBlock:"
+ "eventWithAppEntityIdentifier:"
+ "eventWithRecurrenceIdentifier:isAppEntityID:"
+ "initWithDomain:store:"
+ "initWithPreferences:"
+ "keysToIgnoreForComparingUIVisiblePropertiesOfObject:andObject:"
+ "preferences"
+ "preferencesStoreForPath:"
+ "primitiveSetURLWrapperValue:forKey:"
+ "primitiveURLWrapperValueForKey:"
+ "setAppEntityIdentifierOverride:"
+ "setURLWrapperForPendingFileCopy:"
+ "uniqueIDForDetachedOccurrenceOfEvent:withOriginalStartDate:timeZone:allDay:"
+ "zip"
- "%@/RID=%lu"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Single value relationship differences? [%d] - %@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_copyFileAtURLToTemporaryDirectory:"
- "_populateIdentityKeysForDiff:"
- "_populateImmutableKeysForDiff:"
- "_populateMultiValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:"
- "_populateSingleValueKeysForDiff:compareUIVisiblePropertiesOnly:"
- "_populateSingleValueRelationshipKeysForDiff:compareUIVisiblePropertiesOnly:"
- "invalid Collection: less than 'count' elements in collection"
- "securityScopedURLWrapperForPendingFileCopy"
- "setSecurityScopedURLWrapperForPendingFileCopy:"

```
