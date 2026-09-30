## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-901.0.0.0.0
-  __TEXT.__text: 0x94354
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0xb6a0
+902.0.0.0.0
+  __TEXT.__text: 0x9a270
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_stubs: 0xb8e0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x62fc
-  __TEXT.__cstring: 0x426a
-  __TEXT.__objc_classname: 0xc52
-  __TEXT.__objc_methname: 0xeca3
-  __TEXT.__objc_methtype: 0x2f51
+  __TEXT.__objc_methlist: 0x645c
+  __TEXT.__cstring: 0x43aa
+  __TEXT.__objc_classname: 0xc95
+  __TEXT.__objc_methname: 0xedfa
+  __TEXT.__objc_methtype: 0x2fa5
   __TEXT.__const: 0x5a6
-  __TEXT.__gcc_except_tab: 0x9654
-  __TEXT.__oslogstring: 0xf407
+  __TEXT.__gcc_except_tab: 0xc00c
+  __TEXT.__oslogstring: 0x101e7
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2d78
+  __TEXT.__unwind_info: 0x3300
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0xc48
-  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__auth_got: 0xc40
+  __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x28a0
-  __DATA_CONST.__cfstring: 0x4e00
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__const: 0x29e8
+  __DATA_CONST.__cfstring: 0x4f40
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x248
-  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xe368
-  __DATA.__objc_selrefs: 0x3af8
-  __DATA.__objc_ivar: 0x5dc
-  __DATA.__objc_data: 0x1870
-  __DATA.__data: 0x1040
-  __DATA.__bss: 0x330
+  __DATA.__objc_const: 0xe598
+  __DATA.__objc_selrefs: 0x3b88
+  __DATA.__objc_ivar: 0x5ec
+  __DATA.__objc_data: 0x1960
+  __DATA.__data: 0x10a0
+  __DATA.__bss: 0x380
   __DATA.__common: 0x4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 77C246B9-C20C-3CD8-9AC5-70367F1F6731
-  Functions: 2714
-  Symbols:   701
-  CStrings:  5360
+  UUID: A5C8F502-0C65-364C-8D36-0181E229840F
+  Functions: 2769
+  Symbols:   698
+  CStrings:  5482
 
Symbols:
+ _objc_release_x2
- _CFArrayCreateMutableCopy
- _CFArrayRemoveValueAtIndex
- _OBJC_CLASS_$_VMUtilities
- _OBJC_CLASS_$_VMVoicemailCapabilities
CStrings:
+ " (fractionCompleted %@, totalUnitCount %@)"
+ "#I %s%s%@ %p Created"
+ "#I %s%s%@ %p Deleted"
+ "#I %s%s%@: %@ Trashed flag for detached record %@"
+ "#I %s%s%@: delayed merge required for record %@"
+ "#I %s%s%@: moving %lu tokens started"
+ "#I %s%s%@: moving (matched: %lu, deleted: %lu, delayed: %lu, detached: %lu) completed"
+ "#I %s%s%@: no changes are required for account store database"
+ "#I %s%s%@: no changes are required for delayed merge"
+ "#I %s%s%@: no changes are required for deleted record %@"
+ "#I %s%s%@: no serviceAccount found"
+ "#I %s%s%@: saving account store"
+ "#I %s%s%@: scheduling delayed merge"
+ "#I %s%s--> Get details <range=%@ mailbox=%@> begin"
+ "#I %s%s==> Get details <lowUID=%lu, highUID=%lu, mailbox=%@> begin"
+ "#I %s%sAdding Detached flag to record %@"
+ "#I %s%sCreating App.LanguageConsumption Event for language %@, confidence %@"
+ "#I %s%sDonating App.LanguageConsumption Event: %@"
+ "#I %s%sPosting VMCarrierIMAPParametersChangedNotification"
+ "#I %s%sRecord <identifier=%lu> added to retrieve audio data"
+ "#I %s%sRecord <identifier=%lu> is pending to retrieve audio data"
+ "#I %s%sUpdate selected messages %@ for mailbox %@, destination type is %d"
+ "#I %s%sUpdate selected messages %@ for mailbox %@, mailbox type is %d"
+ "#I %s%s[IVM] %@ _activityEnded: not posting"
+ "#I %s%s[IVM] %@ _activityEnded: task %s info %@ service %@"
+ "#I %s%s[IVM] %@ _activityStarted: bail"
+ "#I %s%s[IVM] %@ _activityStarted: task %s info %@ service %@"
+ "#I %s%s[IVM] %@ _targetsAdded: adding inProcessRecords from activity targets"
+ "#I %s%s[IVM] %@ addScheduledActivity: added to activities"
+ "#I %s%s[IVM] %@ added to activity map for task %s"
+ "#I %s%s[IVM] %@ removeScheduledActivity: removed from activities"
+ "#I %s%s[IVM] %@ removed from activity map"
+ "#I %s%s[IVM] %@ voicemailTaskType: task %s, found taskName '%@' in activity map"
+ "#I %s%s[IVM] %@ voicemailTaskType: task %s, using taskName '%@' from monitor property"
+ "#I %s%s[IVM] Posting %@; userInfo = %@"
+ "#I %s%s[IVM] currentTaskType: %s"
+ "#I %s%s[IVM] taskOfTypeExists: %s -> %@"
+ "#I %s%s[IVQ] queue:%@, schedule: setPasscode, account %@"
+ "#I %s%s_executePostSyncUpdate"
+ "#I %s%s_mailboxUsageUpdateCompletedWithError %@"
+ "#I %s%scopyAccountTokens: added record %@"
+ "#I %s%scopyAccountTokens: no serviceAccount found"
+ "#I %s%scopyAccountTokens: no token for record %@"
+ "#I %s%scopyAccountTokensForDeletedRecords: added record %@, main record %@"
+ "#I %s%scopyAccountTokensForDeletedRecords: no serviceAccount found"
+ "#I %s%scopyAccountTokensForDeletedRecords: no token for record %@"
+ "#I %s%scopyTokensForRecords: no token for record %@"
+ "#I %s%sdo_M2A_merge: completed"
+ "#I %s%sdo_M2A_merge: no serviceAccount found"
+ "#I %s%sdo_M2A_merge: started"
+ "#I %s%sgetMegadomeLanguages: %@"
+ "#I %s%simap_M2A_merge: completed"
+ "#I %s%simap_M2A_merge: found %lu deleted records"
+ "#I %s%simap_M2A_merge: found %lu inbox records"
+ "#I %s%simap_M2A_merge: found %lu read records"
+ "#I %s%simap_M2A_merge: found %lu trash records"
+ "#I %s%simap_M2A_merge: no serviceAccount found"
+ "#I %s%simap_M2A_merge: started"
+ "#I %s%smarkRecordsAsRead: (matched: %lu, deleted: %lu, delayed: %lu, detached: %lu) completed"
+ "#I %s%smarkRecordsAsRead: changing Read flag for detached record %@"
+ "#I %s%smarkRecordsAsRead: changing flag for %lu tokens started"
+ "#I %s%smarkRecordsAsRead: merge required for record %@"
+ "#I %s%smarkRecordsAsRead: no changes are required for account store database"
+ "#I %s%smarkRecordsAsRead: no changes are required for delayed merge"
+ "#I %s%smarkRecordsAsRead: no changes are required for deleted record %@"
+ "#I %s%smarkRecordsAsRead: no serviceAccount found"
+ "#I %s%smarkRecordsAsRead: saving account store"
+ "#I %s%smarkRecordsAsRead: scheduling delayed merge"
+ "#I %s%smoveRecordsToDeleted: delayed merge required for record %@"
+ "#I %s%smoveRecordsToDeleted: moving %lu tokens started"
+ "#I %s%smoveRecordsToDeleted: moving (delayed: %lu) completed"
+ "#I %s%smoveRecordsToDeleted: no changes are required for account store database"
+ "#I %s%smoveRecordsToDeleted: no changes are required for delayed merge"
+ "#I %s%smoveRecordsToDeleted: no serviceAccount found"
+ "#I %s%smoveRecordsToDeleted: scheduling delayed merge"
+ "#I %s%sscheduleDelayedMerge: delayed merge canceled"
+ "#I %s%sscheduleDelayedMerge: delayed merge is scheduled already"
+ "#I %s%sscheduleDelayedMerge: sheduling delayed merge in %d seconds"
+ "#I %s%supdateBodies: found %lu records to retrieve audio data %@"
+ "#I %s%supdateBodies: no records found to retrieve audio data"
+ "#I %s%supdateSelectedMessages: found %lu records, %lu detached records"
+ "#I %s%supdateSelectedMessages: no changes required"
+ "#I %s%supdateSelectedMessages: store changed"
+ "#I [IVM] %@ current monitor"
+ "%@ Adding transcription database sanitization operation"
+ "%@ is executing transcriptionAvailabilityChanged with transcription service available %@"
+ ", client [%s:%d] (conn=%p)"
+ "5"
+ "<%@ %p"
+ "<%@ %p> Adding transcription operation %@, duration %lu"
+ "<%@ %p> Adding transcription operation observers"
+ "<%@ %p> Created"
+ "<%@ %p> observeValueForKeyPath: non-transcription operation %@"
+ "<%@ %p> updating client [%s:%d] (conn=%p) transcribing status changed to %@%@"
+ "<%@ %p> updating client [%s:%d] (conn=%p) transcription availability status changed to %@"
+ "@\"VMBiomeClient\""
+ "@\"VMMegadomeClient\""
+ "B20@0:8B16"
+ "Cannot execute on deleted object"
+ "DisconnectIdleConnections"
+ "Error %@ encountered while encoding file data for file :%@"
+ "Error reading file %@, error: %@"
+ "Error sending transcription availability status back to client with error: %@"
+ "Loading transcription service completed."
+ "T@\"NSProgress\",&,N,V_transcriptionProgress"
+ "T@\"VMBiomeClient\",R,N,V_biomeClient"
+ "T@\"VMMegadomeClient\",R,N,V_megadomeClient"
+ "T@\"_TtC3vmd15MegadomeWrapper\",&,N,V_megadomeWrapper"
+ "UnknownTask"
+ "VMBiomeClient"
+ "VMMegadomeClient"
+ "VMTranscriptionDelegate"
+ "VMTranscriptionService.mm"
+ "VMUtilities"
+ "VMVoicemailTranscriptionController.mm"
+ "_biomeClient"
+ "_executePostSyncUpdate:"
+ "_imap_M2A_merge"
+ "_is_my_activity_sync:"
+ "_megadomeClient"
+ "_updateBodies:"
+ "addBlockInvocation:taskName:withPriority:controlledBy:"
+ "addTranscriptionDelegate:queue:"
+ "addTranscriptionOperation:duration:"
+ "biom.cln"
+ "biomeClient"
+ "copyAccountTokensForDeletedRecords"
+ "copyAccountTokensForDeletedRecords:"
+ "copyAccountTokensForMainRecordsWithFlags:flagsToNotHave:"
+ "copyTokensForDeletedRecords"
+ "copyTokensForRecords:"
+ "copyTokensForRecordsWithFlags:flagsToNotHave:"
+ "countOfRecordsWithFlags:flagsToNotHave:"
+ "do_M2A_merge"
+ "fCacheIsTranscriptionServiceAvailable"
+ "fTranscriptionProgress"
+ "i24@0:8I16I20"
+ "initWithTranscriptionService:"
+ "isInferredLanguage: %@ found in megadome context"
+ "isInferredLanguage: %@ is preferred language"
+ "isInferredLanguage: %@ is system language"
+ "isInferredLanguage: invalid language"
+ "isSyncScheduled"
+ "isTranscriptionServiceAvailable"
+ "kVVChangePasswordTask"
+ "kVVFlagPushTask"
+ "kVVGreetingFetchTask"
+ "kVVHeaderFetchTask"
+ "kVVIdle"
+ "kVVMessageFetchTask"
+ "kVVOtherTask"
+ "kVVSetGreetingTask"
+ "kVVSetGreetingTypeTask"
+ "manageSpeechAssetSubscriptions"
+ "manageSpeechAssetSubscriptions_sync"
+ "markRecordsAsReadTask:"
+ "megadomeClient"
+ "mgdm.cln"
+ "mgmt.cln"
+ "moveRecords%@"
+ "moveRecords:toTrash:"
+ "moveRecordsToDeletedTask:"
+ "moveRecordsToInboxTask:"
+ "moveRecordsToTrashTask:"
+ "removeTranscriptionDelegate:"
+ "reset"
+ "resetTranscriptionProgress"
+ "retrieveDictationResultWithLocaleForFileAtURL:locale:profanityFilterOverride:queuePriority:duration:transcriptionBeginCallback:completion:"
+ "scheduleDelayedMerge"
+ "setByAddingObjectsFromSet:"
+ "setPasscode"
+ "setSyncScheduled:"
+ "setTranscribingChanged:"
+ "setTranscriptionFractionCompleted:"
+ "setTranscriptionProgress:"
+ "setTranscriptionServiceAvailable:"
+ "setTranscriptionTotalUnitCount:"
+ "setWithArray:"
+ "syncRequired"
+ "syncScheduled"
+ "toInbox"
+ "toTrash"
+ "transcriptionAvailabilityChanged:"
+ "tspt.ctr"
+ "tsvc.svc"
+ "updateControllerWithLocale:assetLocale:"
+ "updateMailboxUsage"
+ "updateSelectedMessages:withMailbox:"
+ "updateSystemContext: %@ not found, systemLang: %@, preferredLangs: %@, megadomeLangs: %@"
+ "v24@0:8@\"<VMTranscriptionDelegate>\"16"
+ "v24@0:8@?<v@?BBBBB@\"NSNumber\">16"
+ "v32@0:8@\"<VMTranscriptionDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "v32@0:8{shared_ptr<VMJetsamAssertion>=^{VMJetsamAssertion}^{__shared_weak_count}}16"
+ "v48@0:8@?16@24i32@40"
+ "v68@0:8@16@24B32q36d44@?52@?60"
+ "voicemailTaskType_sync:"
+ "{?=\"greetingTypeRead\"b1\"greetingCached\"b2\"accountState\"b3\"initializing\"b1\"parametersDirty\"b1\"coalesceSyncs\"b1\"smscAvailable\"b1}"
+ "{TranscriptionProgress_t=\"fractionCompleted\"d\"totalUnitCount\"q}"
- "#I %s%s%@ is executing TrashCompaction for service account %@"
- "#I %s%s==> count=%d"
- "#I %s%s==> label=%@"
- "#I %s%sDid not find records that need server sync"
- "#I %s%sFound %lu records for retrieving audio data %@"
- "#I %s%sFound %lu records that need to sync up with the account store"
- "#I %s%sNo records found that require retrieving audio data, removed %lu records, total %lu records"
- "#I %s%sPosting VVServiceFinishedAddingRecordsNotification notification %@"
- "#I %s%sPosting kIMAPServiceLibraryRecordsAddedNotification notification %@"
- "#I %s%sPosting notification VVServiceRecordsAddedNotification %@"
- "#I %s%sRecord %lu is pending to retrieve audio data %@"
- "#I %s%sRetrieving audio data is not scheduled"
- "#I %s%sSet %@ flag for Detached record %@"
- "#I %s%s[IVM] ACTIVITY: %@ %@"
- "#I %s%s[IVM] _activityEnded %@ service %@ monitor %p"
- "#I %s%s[IVM] _activityEnded: not posting"
- "#I %s%s[IVM] _activityStarted: %@ service %@ monitor %p"
- "#I %s%s[IVM] _activityStarted: bail"
- "#I %s%s[IVM] added monitor %p.'%@' for %@ service"
- "#I %s%s[IVM] currentTaskType: %d"
- "#I %s%s[IVM] removed monitor %p.'%@' for %@service"
- "#I %s%s[IVM] taskOfTypeExists: %d -> %d"
- "#I %s%s[IVM] voicemailTaskType '%@': found in map %p"
- "#I %s%s[IVM] voicemailTaskType '%@': using from monitor %p"
- "#I %s%s[IVQ] queue:%@, monitor:%p.'%@', schedule: _synchronouslyPushFlags, account %@ => %@"
- "#I %s%s[IVQ] queue:%@, monitor:???, schedule: setPasscode, account %@"
- "#I %s%sdo_M2A_merge: (deleted) No token for record: %@"
- "#I %s%sdo_M2A_merge: (read) No token for record: %@"
- "#I %s%sdo_M2A_merge: (trashed) No token for record: %@"
- "#I %s%sdo_M2A_merge: (untrashed) No token for record: %@"
- "#I [IVM] for monitor %p.%@"
- "<%@ %p> updating client [%s:%d] (conn=%p) transcribing status changed to %@"
- "???"
- "@\"<VMTranscriptionService>\""
- "@\"BMSource\""
- "@24@0:8Q16"
- "Donating App.LanguageConsumption Event: %@"
- "T@\"<VMTranscriptionService>\",&,N,V_transcriptionService"
- "T@\"BMSource\",R,N,V_langConsumptionBiomeSource"
- "T@\"NSArray\",C,N,V_megadomeContextLanguages"
- "T@\"NSProgress\",R,N,V_transcriptionProgress"
- "T@\"VMVoicemailTranscriptionController\",W,N,V_transcriptionController"
- "T@\"_TtC3vmd15MegadomeWrapper\",C,N,V_megadomeWrapper"
- "TB,R,N,GisTranscriptionAvailable"
- "Unable to send capabilities to client: %@"
- "VMAWDTranscriptionFailureReasonAsString:"
- "VMLanguageIDFailureReasonAsString:"
- "VMTranscriptionService.m"
- "VMVoicemailTranscriptionController.m"
- "VVServiceFinishedAddingRecordsNotification"
- "VVServiceRecordsAddedNotification"
- "__is_my_activity:"
- "_addedRecords"
- "_handleNewServiceNotification:"
- "_langConsumptionBiomeSource"
- "_megadomeContextLanguages"
- "_messagesAddedCompleted"
- "_postMessagesAdded:"
- "_sendCapabilities"
- "addBlockInvocation:withPriority:controlledBy:"
- "addTranscriptionProgressDelegate:queue:"
- "capabilities"
- "getInferredLanguageCodes"
- "getInferredLanguageCodes: inferredLanguageCodes %@"
- "handleIMAPServiceLibraryRecordsAddedNotification:"
- "initWithTranscriptionEnabled:"
- "isInferredLanguage: %@? %d"
- "isMainThread"
- "kIMAPServiceLibraryRecordsAddedNotification"
- "langConsumptionBiomeSource"
- "manageSpeechAssetSubscriptions:limit:"
- "megadomeContextLanguages"
- "removeTranscriptionProgressDelegate:"
- "retrieveDictationResultWithLocaleForFileAtURL:locale:profanityFilterOverride:assetFreqMap:queuePriority:duration:transcriptionBeginCallback:completion:"
- "setCapabilities:"
- "setMegadomeContextLanguages:"
- "storeFlagsWithMask:forRecordsWithIdentifiers:"
- "synchronizeRecordFlags"
- "transcriptionAvailable"
- "updateMegadomeLanguages"
- "updateMegadomeLanguages: %@"
- "v24@0:8@\"<VMTranscriptionProgressDelegate>\"16"
- "v24@0:8@?<v@?@\"VMVoicemailCapabilities\"BBBB@\"NSNumber\">16"
- "v32@0:8@\"<VMTranscriptionProgressDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
- "v40@0:8@?16i24@32"
- "v76@0:8@16@24B32@36q44d52@?60@?68"
- "voicemailTaskType:"
- "{?=\"syncInProgress\"b1\"syncRequired\"b1\"greetingTypeRead\"b1\"greetingCached\"b2\"accountState\"b3\"initializing\"b1\"parametersDirty\"b1\"coalesceSyncs\"b1\"smscAvailable\"b1}"

```
