## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/Versions/A/NotesShared`

```diff

-3195.0.0.0.0
-  __TEXT.__text: 0x358cac
+3195.41.7.101.1
+  __TEXT.__text: 0x36704c
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x6b0
-  __TEXT.__objc_methlist: 0x1829c
-  __TEXT.__const: 0xdb70
-  __TEXT.__cstring: 0x19406
-  __TEXT.__gcc_except_tab: 0xf210
-  __TEXT.__oslogstring: 0x1c919
+  __TEXT.__objc_methlist: 0x1844c
+  __TEXT.__const: 0xde30
+  __TEXT.__cstring: 0x19686
+  __TEXT.__gcc_except_tab: 0xf298
+  __TEXT.__oslogstring: 0x1e4b9
   __TEXT.__ustring: 0x39a
-  __TEXT.__swift5_typeref: 0x4376
-  __TEXT.__constg_swiftt: 0x363c
-  __TEXT.__swift5_reflstr: 0x2099
-  __TEXT.__swift5_fieldmd: 0x2dc8
+  __TEXT.__constg_swiftt: 0x37d8
+  __TEXT.__swift5_typeref: 0x4596
   __TEXT.__swift5_builtin: 0x208
+  __TEXT.__swift5_reflstr: 0x2259
+  __TEXT.__swift5_fieldmd: 0x2f8c
   __TEXT.__swift5_assocty: 0x7e0
-  __TEXT.__swift5_proto: 0x988
-  __TEXT.__swift5_types: 0x380
-  __TEXT.__swift5_capture: 0x1d64
-  __TEXT.__swift5_protos: 0x54
-  __TEXT.__swift_as_entry: 0x184
-  __TEXT.__swift_as_ret: 0x1b4
-  __TEXT.__swift_as_cont: 0x3f0
+  __TEXT.__swift5_proto: 0x994
+  __TEXT.__swift5_types: 0x39c
+  __TEXT.__swift5_capture: 0x1e58
+  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift_as_entry: 0x18c
+  __TEXT.__swift_as_ret: 0x1bc
+  __TEXT.__swift_as_cont: 0x3fc
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x12698
-  __TEXT.__eh_frame: 0x8680
+  __TEXT.__unwind_info: 0x128f8
+  __TEXT.__eh_frame: 0x8804
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e68
-  __DATA_CONST.__objc_classlist: 0xa58
+  __DATA_CONST.__const: 0x1e78
+  __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xcb48
+  __DATA_CONST.__objc_selrefs: 0xcc60
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6d0
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x2178
-  __AUTH_CONST.__const: 0x12828
-  __AUTH_CONST.__cfstring: 0xfae0
-  __AUTH_CONST.__objc_const: 0x22390
+  __DATA_CONST.__got: 0x21a0
+  __AUTH_CONST.__const: 0x12bb0
+  __AUTH_CONST.__cfstring: 0xfc80
+  __AUTH_CONST.__objc_const: 0x22850
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x2848
-  __AUTH.__objc_data: 0x2e50
-  __AUTH.__data: 0x1348
+  __AUTH_CONST.__auth_got: 0x2898
+  __AUTH.__objc_data: 0x2ea0
+  __AUTH.__data: 0x1608
   __DATA.__objc_ivar: 0xd90
-  __DATA.__data: 0x4ac0
+  __DATA.__data: 0x4be8
   __DATA.__objc_stublist: 0x20
-  __DATA.__common: 0x180
+  __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0x4888
   __DATA_DIRTY.__data: 0x1dc0
   __DATA_DIRTY.__bss: 0x2bc0

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
   - /System/Library/PrivateFrameworks/Synapse.framework/Versions/A/Synapse
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18647
-  Symbols:   23361
-  CStrings:  5249
+  Functions: 18801
+  Symbols:   23509
+  CStrings:  5329
 
Symbols:
+ +[ICAttachment(Management) attachmentsMatchingPredicate:context:]
+ +[ICAttachmentPDFModel pageTextFromPDFAtURL:]
+ +[ICAttachmentPDFModel recognizedTextFromPDFAtURL:suggestedTitle:maxPages:isCancelled:]
+ +[ICBackgroundTranscriptionHelper makeDeferredBackgroundTranscriptionTask]
+ +[ICBackgroundTranscriptionHelper scheduleDeferredBackgroundTranscription]
+ +[ICCloudContext ic_currentPersonaDescription]
+ +[ICCloudContext referenceTargetsLoggingDescriptionForRecord:]
+ +[ICCloudContext shouldDeferPushNotificationWhenReadyToSync:isDisabled:isDisabledInternal:configuredContainerCount:]
+ +[ICInlineAttachment(OrphanRepair) discardOrphanedInlineAttachmentsInContext:]
+ +[ICSearchProfiler signpostIDForOperation:]
+ -[ICAccountProxy hasVisibleNotes]
+ -[ICAttachment conversationIdentifier]
+ -[ICAttachment extractedTextContent]
+ -[ICAttachment setConversationIdentifier:]
+ -[ICAttachment(CloudKit) ic_hasAudioMediaOnDiskIncludingSubAttachments]
+ -[ICAttachment(CloudKit) ic_topLevelRecordingAttachment]
+ -[ICAttachmentDrawingModel extractedTextContent]
+ -[ICAttachmentGalleryModel extractedTextContent]
+ -[ICAttachmentImageModel extractedTextContent]
+ -[ICAttachmentInlineDrawingModel extractedTextContent]
+ -[ICAttachmentModel extractedTextContent]
+ -[ICAttachmentPDFModel extractedTextContent]
+ -[ICAttachmentPDFModel supportsOCR]
+ -[ICAttachmentPaperBundleModel extractedTextContent]
+ -[ICCloudContext _prewarmDeferredCommonAssetFetchIfNeededForCloudObject:]
+ -[ICCloudContext deferPushNotificationIfUnableToFetchForSubscriptionID:]
+ -[ICCloudContext needsToFetchForDeferredPushNotification]
+ -[ICCloudContext setNeedsToFetchForDeferredPushNotification:]
+ -[ICCloudContext waitForPendingWorkWithCompletionHandler:]
+ -[ICNote _updateLinksToThisNote]
+ -[ICNote performAfterSave:]
+ -[ICNote setUpdateLinksBackgroundContext:]
+ -[ICNote updateLinksBackgroundContext]
+ -[ICNote updateLinksToThisNoteAfterSave]
+ -[ICNote(AttachmentManagement) titleForParagraphID:]
+ -[ICNoteContainer ic_accessibilityIdentifier]
+ -[ICNoteContext hasVisibleNotes]
+ -[ICNoteContext ic_accessibilityIdentifier]
+ -[NFAttachment(ICLegacyAttachment) setTypeUTI:]
+ -[NSManagedObjectContext(ICInlineAttachmentOrphanRepair) ic_saveRepairingOrphanedInlineAttachmentsWithReason:]
+ GCC_except_table115
+ GCC_except_table173
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table253
+ GCC_except_table271
+ GCC_except_table310
+ GCC_except_table312
+ GCC_except_table317
+ GCC_except_table327
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table376
+ GCC_except_table405
+ GCC_except_table441
+ GCC_except_table446
+ GCC_except_table477
+ GCC_except_table495
+ GCC_except_table522
+ GCC_except_table527
+ GCC_except_table532
+ GCC_except_table92
+ ICSearchProfilingSignpostLog
+ ICSearchProfilingSignpostLog.onceToken
+ ICSearchProfilingSignpostLog.signpostLog
+ OBJC_IVAR_$_ICCloudContext._needsToFetchForDeferredPushNotification
+ OBJC_IVAR_$_ICNote.updateLinksBackgroundContext
+ _CGColorSpaceCreateWithName
+ _CGContextDrawPDFPage
+ _CGContextSetRGBFillColor
+ _CGPDFDocumentGetNumberOfPages
+ _CGPDFDocumentGetPage
+ _CGPDFPageGetDrawingTransform
+ _CGPDFPageGetRotationAngle
+ _ICAttachmentMetadataConversationIdentifierKey
+ _ICAttachmentModelNonBlankString
+ _ICNoteUpdateLinksNotification
+ _ICSearchProfilingSignpostLog
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_UMUserManager
+ __63-[ICCloudContext handleCloudKitNotification:completionHandler:]_block_invoke
+ __DATA__TtC11NotesShared24ProcessActivityAssertion
+ __DATA__TtC11NotesShared31TranscriptionBackgroundActivity
+ __DATA__TtCC11NotesShared13Transcription14RecordingClaim
+ __DATA__TtCC11NotesShared31TranscriptionBackgroundActivity4Hold
+ __IVARS__TtC11NotesShared24ProcessActivityAssertion
+ __IVARS__TtC11NotesShared31TranscriptionBackgroundActivity
+ __IVARS__TtCC11NotesShared13Transcription14RecordingClaim
+ __IVARS__TtCC11NotesShared31TranscriptionBackgroundActivity4Hold
+ __METACLASS_DATA__TtC11NotesShared24ProcessActivityAssertion
+ __METACLASS_DATA__TtC11NotesShared31TranscriptionBackgroundActivity
+ __METACLASS_DATA__TtCC11NotesShared13Transcription14RecordingClaim
+ __METACLASS_DATA__TtCC11NotesShared31TranscriptionBackgroundActivity4Hold
+ __OBJC_$_CATEGORY_NSManagedObjectContext_$_ICInlineAttachmentOrphanRepair
+ __OBJC_$_CLASS_METHODS_ICInlineAttachment(CloudKit|Management|OrphanRepair|ICAttachmentPersistenceAdditions)
+ __OBJC_$_INSTANCE_METHODS_ICInlineAttachment(CloudKit|Management|OrphanRepair|ICAttachmentPersistenceAdditions)
+ __OBJC_$_INSTANCE_METHODS_ICTranscription(NotesShared)
+ __OBJC_$_INSTANCE_METHODS_NSManagedObjectContext(ICInlineAttachmentOrphanRepair|Shared|ICLegacyContext)
+ __OBJC_CLASS_PROTOCOLS_$_ICInlineAttachment(CloudKit|Management|OrphanRepair|ICAttachmentPersistenceAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_NSManagedObjectContext(ICInlineAttachmentOrphanRepair|Shared|ICLegacyContext)
+ ___32-[ICNote _updateLinksToThisNote]_block_invoke
+ ___32-[ICNote _updateLinksToThisNote]_block_invoke_2
+ ___40-[ICNote updateLinksToThisNoteAfterSave]_block_invoke
+ ___40-[ICNote updateLinksToThisNoteAfterSave]_block_invoke_2
+ ___42-[ICAttachment setConversationIdentifier:]_block_invoke
+ ___48-[ICAttachmentGalleryModel extractedTextContent]_block_invoke
+ ___52-[ICNote(AttachmentManagement) titleForParagraphID:]_block_invoke
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke_2
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke_3
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke_4
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke_5
+ ___58-[ICCloudContext waitForPendingWorkWithCompletionHandler:]_block_invoke_6
+ ___78+[ICInlineAttachment(OrphanRepair) discardOrphanedInlineAttachmentsInContext:]_block_invoke
+ ___ICSearchProfilingSignpostLog_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80r88r_e5_v8?0l
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40bs48bs_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_57_e8_32s40bs48bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_65_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_96_e8_32s40s48s56s64bs72r80r_e32_v24?0"CKRecordID"8"NSError"16l
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r88r
+ ___swift_memcpy48_8
+ ___swift_project_boxed_opaque_existential_1Tm
+ _associated conformance 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV4KindOSHADSQ
+ _flat unique So8NSObject_p
+ _kCGColorSpaceSRGB
+ _kICDividerLineHeightBoldText
+ _objc_msgSend$_prewarmDeferredCommonAssetFetchIfNeededForCloudObject:
+ _objc_msgSend$_updateLinksToThisNote
+ _objc_msgSend$audiovisualContentTypes
+ _objc_msgSend$beginActivityWithOptions:reason:
+ _objc_msgSend$biometry
+ _objc_msgSend$clearContainers
+ _objc_msgSend$currentPersona
+ _objc_msgSend$deferPushNotificationIfUnableToFetchForSubscriptionID:
+ _objc_msgSend$discardOrphanedInlineAttachmentsInContext:
+ _objc_msgSend$domainState
+ _objc_msgSend$endActivity:
+ _objc_msgSend$extractedTextContent
+ _objc_msgSend$ic_currentPersonaDescription
+ _objc_msgSend$ic_hasAudioMediaOnDiskIncludingSubAttachments
+ _objc_msgSend$ic_saveRepairingOrphanedInlineAttachmentsWithReason:
+ _objc_msgSend$ic_topLevelRecordingAttachment
+ _objc_msgSend$insertedObjects
+ _objc_msgSend$isEnterprisePersona
+ _objc_msgSend$isPersonalPersona
+ _objc_msgSend$isSystemPersona
+ _objc_msgSend$loadObjectOfClass:completionHandler:
+ _objc_msgSend$lock
+ _objc_msgSend$needsToFetchForDeferredPushNotification
+ _objc_msgSend$objectRegisteredForID:
+ _objc_msgSend$ocrStringFromImage:title:languages:
+ _objc_msgSend$pageTextFromPDFAtURL:
+ _objc_msgSend$performAfterSave:
+ _objc_msgSend$referenceTargetsLoggingDescriptionForRecord:
+ _objc_msgSend$restructureRecordingIntoSubattachmentIfNeeded
+ _objc_msgSend$setNeedsToFetchForDeferredPushNotification:
+ _objc_msgSend$setUpdateLinksBackgroundContext:
+ _objc_msgSend$shouldDeferPushNotificationWhenReadyToSync:isDisabled:isDisabledInternal:configuredContainerCount:
+ _objc_msgSend$signpostIDForOperation:
+ _objc_msgSend$stateHash
+ _objc_msgSend$updateLinksBackgroundContext
+ _objc_msgSend$updateLinksToThisNoteAfterSave
+ _objc_msgSend$userPersonaNickName
+ _objc_msgSend$userPersonaType
+ _objc_msgSend$userPersonaUniqueString
+ _os_signpost_id_make_with_pointer
+ _symbolic $s11NotesShared28BackgroundExecutionAssertionP
+ _symbolic Iegh_
+ _symbolic SayyyYbcG
+ _symbolic So6NSLockC
+ _symbolic So7NSCacheCy_____yxq__G_____yxq__GG 11NotesShared5CacheC10KeyWrapper33_E2980D92141C1715ABC1100DCD468C78LLC AC05ValueE0AELLC
+ _symbolic _____ 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV
+ _symbolic _____ 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV4KindO
+ _symbolic _____ 11NotesShared13TranscriptionC14RecordingClaimC
+ _symbolic _____ 11NotesShared24ProcessActivityAssertionC
+ _symbolic _____ 11NotesShared31TranscriptionBackgroundActivityC
+ _symbolic _____ 11NotesShared31TranscriptionBackgroundActivityC4HoldC
+ _symbolic _____ 11NotesShared31TranscriptionBackgroundActivityC5State33_B3D3F430FDD672DD7B42882042ED77DELLV
+ _symbolic _____ s6UInt64V
+ _symbolic _____Sg 11NotesShared13TranscriptionC14RecordingClaimC
+ _symbolic _____Sg 11NotesShared31TranscriptionBackgroundActivityC4HoldC
+ _symbolic _____SgXw 11NotesShared13TranscriptionC
+ _symbolic _____SgXwz_Xx 11NotesShared13TranscriptionC
+ _symbolic _____XDXMT 11NotesShared13TranscriptionC
+ _symbolic ______pSSYbc 11NotesShared28BackgroundExecutionAssertionP
+ _symbolic ______pSg 11NotesShared28BackgroundExecutionAssertionP
+ _symbolic ______pSg So8NSObjectP
+ _symbolic _____ySDySo17NSManagedObjectIDCSiGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySDySo17NSManagedObjectIDCSiG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____yShySo17NSManagedObjectIDCGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yShySo17NSManagedObjectIDCG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____ySi_____G s18_DictionaryStorageC 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV
+ _symbolic _____ySo17NSManagedObjectIDCSiG s18_DictionaryStorageC
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 11NotesShared31TranscriptionBackgroundActivityC5State33_B3D3F430FDD672DD7B42882042ED77DELLV
+ _symbolic _____y_______G 10Foundation16AttributedStringV4RunsV16AttributesSlice1V 11NotesShared16SpeakerAttributeV
+ _symbolic _____y_______G 10Foundation16AttributedStringV4RunsV16AttributesSlice1V 11NotesShared23TranscriptTextAttributeV
+ _symbolic _____y________G 10Foundation16AttributedStringV4RunsV16AttributesSlice1V8IteratorV 11NotesShared16SpeakerAttributeV
+ _symbolic _____y________G 10Foundation16AttributedStringV4RunsV16AttributesSlice1V8IteratorV 11NotesShared23TranscriptTextAttributeV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 11NotesShared31TranscriptionBackgroundActivityC5State33_B3D3F430FDD672DD7B42882042ED77DELLV So16os_unfair_lock_sV
+ _symbolic _____yyyYbcG s23_ContiguousArrayStorageC
+ _symbolic yyYbc
+ _symbolic yyc
+ _type_layout_string 10Foundation16AttributedStringV11NotesSharedE43TranscriptParagraphAccessibilityInformationV
+ _type_layout_string 11NotesShared31TranscriptionBackgroundActivityC5State33_B3D3F430FDD672DD7B42882042ED77DELLV
- -[ICCloudContext disableAutomaticallyRetryNetworkFailures]
- -[ICCloudContext setDisableAutomaticallyRetryNetworkFailures:]
- -[ICNote _updateLinksOnMainThreadSelectorDelayer]
- -[ICNote setUpdateLinksSelectorDelayer:]
- -[ICNote titleForParagraphID:]
- -[ICNote updateLinksSelectorDelayer]
- -[ICNote updateLinksWhenPossible]
- GCC_except_table122
- GCC_except_table144
- GCC_except_table160
- GCC_except_table197
- GCC_except_table202
- GCC_except_table243
- GCC_except_table263
- GCC_except_table270
- GCC_except_table272
- GCC_except_table291
- GCC_except_table301
- GCC_except_table318
- GCC_except_table322
- GCC_except_table337
- GCC_except_table347
- GCC_except_table360
- GCC_except_table394
- GCC_except_table433
- GCC_except_table464
- GCC_except_table479
- GCC_except_table482
- GCC_except_table509
- GCC_except_table514
- OBJC_IVAR_$_ICCloudContext._disableAutomaticallyRetryNetworkFailures
- OBJC_IVAR_$_ICNote.updateLinksSelectorDelayer
- _ICInternalSettingsIsCollapsibleSectionsEnabled
- __INSTANCE_METHODS_ICTranscription
- __OBJC_$_CATEGORY_NSManagedObjectContext_$_Shared
- __OBJC_$_CLASS_METHODS_ICInlineAttachment(CloudKit|Management|ICAttachmentPersistenceAdditions)
- __OBJC_$_INSTANCE_METHODS_ICInlineAttachment(CloudKit|Management|ICAttachmentPersistenceAdditions)
- __OBJC_$_INSTANCE_METHODS_NSManagedObjectContext(Shared|ICLegacyContext)
- __OBJC_CLASS_PROTOCOLS_$_ICInlineAttachment(CloudKit|Management|ICAttachmentPersistenceAdditions)
- __OBJC_CLASS_PROTOCOLS_$_NSManagedObjectContext(Shared|ICLegacyContext)
- ___30-[ICNote titleForParagraphID:]_block_invoke
- ___49-[ICNote _updateLinksOnMainThreadSelectorDelayer]_block_invoke
- ___block_descriptor_57_e8_32s40bs48bs_e38_v24?0"<NSSecureCoding>"8"NSError"16l
- ___block_descriptor_66_e8_32s40s_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48bs56r_e38_v32?0"NSString"8"CKContainer"16^B24l
- ___block_descriptor_72_e8_32s40s48s56bs_e32_v24?0"CKRecordID"8"NSError"16l
- __swift_closure_destructor.21Tm
- __swift_closure_destructor.40Tm
- _objc_msgSend$audiovisualTypes
- _objc_msgSend$disableAutomaticallyRetryNetworkFailures
- _objc_msgSend$evaluatedPolicyDomainState
- _objc_msgSend$loadItemForTypeIdentifier:options:completionHandler:
- _objc_msgSend$setAutomaticallyRetryNetworkFailures:
- _objc_msgSend$setDisableAutomaticallyRetryNetworkFailures:
- _objc_msgSend$setUpdateLinksSelectorDelayer:
- _objc_msgSend$updateLinksSelectorDelayer
- _objc_msgSend$updateLinksWhenPossible
- _symbolic So7NSCacheCy_____yxq__xG_____yxq__GG 11NotesShared5CacheC10KeyWrapper33_E2980D92141C1715ABC1100DCD468C78LLC AC05ValueE0AELLC
CStrings:
+ "%@ (after orphan repair)"
+ "%@ (unique:%@, type:%lu, personal:%@, enterprise:%@, system:%@)"
+ "%@->%@"
+ "%@->[%@]"
+ "%{public}@"
+ "-[ICNote _updateLinksToThisNote]"
+ "<default>"
+ "<none>"
+ "?"
+ "Acquired background-execution assertion for %{public}s; %{public}ld unit(s) of transcription work outstanding"
+ "Attaching encrypted media asset to CloudKit upload: media=%@ url=%@"
+ "Attaching media archive asset to CloudKit upload: media=%@ archive=%@"
+ "Attaching media asset to CloudKit upload: media=%@ filename=%@"
+ "Attempting to update links on background context note"
+ "Background transcription hold %{public}llu was released by deallocation without a terminal outcome; look for an enqueue path that returns without ending its hold"
+ "Background transcription produced %{public}ld segment(s) for attachment %@; starting summarization while still holding the assertion"
+ "Background transcription starting under assertion for attachment %@: fragments=%{public}ld"
+ "Background transcription unit complete for attachment %@; the assertion is released next"
+ "Background transcription work %llu began under the existing assertion; %ld unit(s) outstanding (%{public}s)"
+ "Background transcription work %llu finished; %ld unit(s) still outstanding, keeping the assertion"
+ "Background transcription work %llu finished; nothing outstanding and no assertion was held"
+ "Cannot remove directory for rolling back asset generation {url: %@, error: %@}"
+ "Cannot restructure recording into sub-attachment: hasTopLevelMediaURL=%{bool,public}d hasNote=%{bool,public}d identifier=%{public}s hasContext=%{bool,public}d"
+ "Copied recording audio onto sub-attachment %{public}s for recording %{public}s"
+ "DeferredPushNotification"
+ "Deferring push notification for subscription %@ until we can fetch: %@ isDisabled=%@ isDisabledInternal=%@ containers=%@"
+ "Discarding orphaned ICInlineAttachment with no note {identifier: %@, typeUTI: %@, altText length: %lu, parentAttachment: %@}. It would fail validation on every save of this context."
+ "Failed to create bitmap context for PDF text recognition {page: %zu, size: %zux%zu}"
+ "Failed to save finished transcript for attachment %{public}s; needsTranscription is NOT durable"
+ "Failed to save restructured recording sub-attachment for attachment %{public}s; background transcription will retry"
+ "Failed to save top-line summary for attachment %{public}s"
+ "Finished transcript fragment"
+ "Fuzzy Query"
+ "Hoisting transcription from recording sub-attachment %{public}s to top-level recording %{public}s"
+ "ICNoteUpdateLinksNotification"
+ "Media push record carries an inaccessible asset: media=%@ filename=%@ mediaURL=%@ mediaFileOnDisk=%d assetURL=%@. CloudKit will reject this save with CKErrorInvalidArguments and, because the modify operation is atomic, fail the whole batch."
+ "Media push record ready: media=%@ filename=%@ mediaURL=%@ mediaFileOnDisk=%d assetAttached=%d assetReachable=%d"
+ "Media record arrived without an asset; marking for fetch: media=%@"
+ "NL Query"
+ "No configured container owns subscription %@, so deferring its fetch until we can sync"
+ "No deferred background-transcription task on this platform"
+ "No encrypted media asset to attach for CloudKit upload (file missing on disk?): media=%@ url=%@"
+ "No sub-attachments to transcribe for audio attachment %{public}s: audioOnDisk=%{bool,public}d topLevelMedia=%{bool,public}d hasNote=%{bool,public}d needsInitialFetchFromCloud=%{bool,public}d"
+ "Not pushing because this object needs to be fetched {object: %@, needsToBeFetchedFromCloud: %d, needsInitialFetchFromCloud: %d, serverRecord: %d, isInCloud: %d}"
+ "Notes: background audio transcription and summarization"
+ "Notes: preparing background audio transcription"
+ "Nothing to remove before beginning asset generation — previous generation directory was never created {url: %@}"
+ "Nothing to remove for rolling back asset generation — directory was never created {url: %@}"
+ "Omitting media reference for attachment %@: media=%@ hasFile=%d. Other devices will see no audio until the media is uploaded."
+ "PersonaDebug: container {identifier: %@, environment: %@, accountID: %@, persona: %@}"
+ "Prefix Query"
+ "Prewarming deferred-asset pre-fetch (inCloud=YES) {object: %@, hasOutOfDateSigs: %d, hasSigs: %d, numAssets: %lu}"
+ "Production"
+ "Record not found on server; clearing fetch/inCloud flags {object: %@, needsToBeFetchedFromCloud: %d, needsInitialFetchFromCloud: %d, serverRecord: %d, isInCloud: %d}"
+ "Refusing to create an inline attachment (%@) on attachment %@ that has no note; it would poison every save of this context"
+ "Refusing to create an inline attachment (%@, typeUTI %@) with no note"
+ "Refusing to resolve attachment ID %@ against a context whose coordinator cannot reach its store; dropping this transcription request"
+ "Refusing to restructure recording %{public}s: derived sub-attachment identifier %{public}s is already taken on this note (markedForDeletion=%{bool,public}d, isSubAttachment=%{bool,public}d). Inserting it would trip the identifier uniqueness constraint."
+ "Refusing to restructure recording sub-attachment %{public}s (parent %{public}s): only the top-level recording is restructured. Hoist with ic_topLevelRecordingAttachment."
+ "Released background-execution assertion for %{public}s immediately: no transcription work left to protect"
+ "Released background-execution assertion: all background transcription work finished"
+ "Restructured recording %{public}s did not survive the save: sub-attachment %{public}s isDeleted=%{bool,public}d detached=%{bool,public}d subAttachments=%{public}ld. Most likely an identifier uniqueness conflict — do not retry, it will only duplicate the media again."
+ "Restructured recording into sub-attachment"
+ "Retrying save after discarding %lu orphaned inline attachment(s) {reason: %@}"
+ "Sandbox"
+ "Saved top-line transcript summary"
+ "Search Step"
+ "Skipping deferred-asset pre-fetch (inCloud=NO; record has never been on server) {object: %@, hasOutOfDateSigs: %d, hasSigs: %d, numAssets: %lu, needsPush: YES}"
+ "Skipping media asset materialization for unsupported object (e.g. audio is unsupported on watchOS unless audio playback is enabled): media=%@"
+ "Sub-attachments present but no media URL yet for audio attachment %{public}s: subAttachments=%{public}ld"
+ "Substring Query"
+ "Syncing for a push notification that arrived while we couldn't fetch"
+ "Top-line call-recording summary failed for attachment %@: %@. Continuing — the transcript is still saved."
+ "Top-line transcript summary failed for attachment %@: %@. Continuing — the transcript is saved and the watch send-back still fires."
+ "Top-line transcript summary unavailable: no safety configuration is registered for use case %{public}s + client application %{public}s. Expected on debug/Sandbox bundle ids, which the GenerativeExperiences safety configuration asset does not list — not a model or transcript problem. Callers should fall back to the on-device summarizer. {domain: %{public}s, code: %{public}ld}"
+ "Will push %@ refs={%@} %@"
+ "Wrote media asset from CloudKit fetch: media=%@ filename=%@"
+ "background transcription already queued for attachment %@; dropping duplicate enqueue"
+ "background transcription not ready yet (%@); retrying in %llus (%ld attempt(s) left)"
+ "background transcription still not ready (%@); timed retries exhausted — re-arming on the next store change (re-arm %{public}ld/%{public}ld). The recording stays queued for this session; no relaunch or tap needed."
+ "call transcription already queued for attachment %@; dropping duplicate enqueue"
+ "conversation_identifier"
+ "self.managedObjectContext.concurrencyType == NSMainQueueConcurrencyType"
+ "unable to queue audio transcription task: %@ — giving up (retriable=%{bool}d stillNeedsTranscription=%{bool}d attemptsRemaining=%ld)."
+ "unable to queue audio transcription task: %@ — re-arm limit reached. The recording stays untranscribed this session."
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
- "Cannot remove directory for rolling back asset generation {url: %@}"
- "Not handling CloudKit push notification: %@"
- "Not pushing because this object needs to be fetched %@"
- "Will push %@ %@"
- "no media URL on imported attachment"
- "unable to queue audio transcription task: %@"
- "v24@?0@\"<NSSecureCoding>\"8@\"NSError\"16"
```
