## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-417.0.0.0.0
-  __TEXT.__text: 0x73758
-  __TEXT.__objc_methlist: 0x682c
-  __TEXT.__cstring: 0xe38f
-  __TEXT.__const: 0xfe8
-  __TEXT.__oslogstring: 0x55ce
+502.0.5.0.0
+  __TEXT.__text: 0x76944
+  __TEXT.__objc_methlist: 0x6d24
+  __TEXT.__cstring: 0xe5ee
+  __TEXT.__const: 0x1008
+  __TEXT.__oslogstring: 0x5683
   __TEXT.__gcc_except_tab: 0x430
-  __TEXT.__swift5_typeref: 0x2ca
-  __TEXT.__constg_swiftt: 0x390
-  __TEXT.__swift5_reflstr: 0x47c
-  __TEXT.__swift5_fieldmd: 0x568
+  __TEXT.__swift5_typeref: 0x2f1
+  __TEXT.__constg_swiftt: 0x3cc
+  __TEXT.__swift5_reflstr: 0x4a6
+  __TEXT.__swift5_fieldmd: 0x5a8
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x21a8
-  __TEXT.__eh_frame: 0x9c8
+  __TEXT.__unwind_info: 0x22b8
+  __TEXT.__eh_frame: 0xb10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3438
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x3470
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3258
+  __DATA_CONST.__objc_selrefs: 0x34c0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0x840
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x10920
-  __AUTH_CONST.__objc_const: 0xaec0
+  __DATA_CONST.__got: 0x858
+  __AUTH_CONST.__const: 0x810
+  __AUTH_CONST.__cfstring: 0x10c20
+  __AUTH_CONST.__objc_const: 0xb828
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x960
-  __AUTH.__objc_data: 0x1eb8
-  __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x7c4
-  __DATA.__data: 0xeb8
+  __AUTH.__objc_data: 0x2080
+  __AUTH.__data: 0x2b0
+  __DATA.__objc_ivar: 0x844
+  __DATA.__data: 0xef0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2924
-  Symbols:   7583
-  CStrings:  2645
+  Functions: 3045
+  Symbols:   7804
+  CStrings:  2678
 
Symbols:
+ +[MOEventCalendarContext supportsSecureCoding]
+ +[MOEventMessageContext supportsSecureCoding]
+ +[MOEventPhotoContext supportsSecureCoding]
+ -[MOEvent calendarContextEvent]
+ -[MOEvent messageContextEvent]
+ -[MOEvent photoContextEvent]
+ -[MOEvent setCalendarContextEvent:]
+ -[MOEvent setMessageContextEvent:]
+ -[MOEvent setPhotoContextEvent:]
+ -[MOEventBundle enrichedNLString]
+ -[MOEventBundle enrichmentRationale]
+ -[MOEventBundle eventForWorkoutPlaceID:]
+ -[MOEventBundle originalNLString]
+ -[MOEventBundle setEnrichedNLString:]
+ -[MOEventBundle setEnrichmentRationale:]
+ -[MOEventBundle setOriginalNLString:]
+ -[MOEventBundle setSourceSuggestionID:]
+ -[MOEventBundle setWorkoutPlaceAssociationKind:]
+ -[MOEventBundle setWorkoutPlaceDestinationID:]
+ -[MOEventBundle setWorkoutPlaceEncompassingID:]
+ -[MOEventBundle setWorkoutPlaceOriginID:]
+ -[MOEventBundle sourceSuggestionID]
+ -[MOEventBundle workoutPlaceAssociationKind]
+ -[MOEventBundle workoutPlaceDestinationID]
+ -[MOEventBundle workoutPlaceDestination]
+ -[MOEventBundle workoutPlaceEncompassingID]
+ -[MOEventBundle workoutPlaceEncompassing]
+ -[MOEventBundle workoutPlaceOriginID]
+ -[MOEventBundle workoutPlaceOrigin]
+ -[MOEventBundleFetchOptions allowedInterfaceTypes]
+ -[MOEventBundleFetchOptions excludeEnrichmentDedupIneligible]
+ -[MOEventBundleFetchOptions excludedInterfaceTypes]
+ -[MOEventBundleFetchOptions initWithDateInterval:ascending:limit:includeDeletedBundles:skipRanking:allowedInterfaceTypes:excludedInterfaceTypes:]
+ -[MOEventBundleFetchOptions rehydrated]
+ -[MOEventBundleFetchOptions setExcludeEnrichmentDedupIneligible:]
+ -[MOEventBundleFetchOptions setRehydrated:]
+ -[MOEventBundleFetchOptions setSuggestionIDs:]
+ -[MOEventBundleFetchOptions suggestionIDs]
+ -[MOEventCalendarContext .cxx_destruct]
+ -[MOEventCalendarContext calendarEndDate]
+ -[MOEventCalendarContext calendarEventIdentifier]
+ -[MOEventCalendarContext calendarIsAllDay]
+ -[MOEventCalendarContext calendarLocation]
+ -[MOEventCalendarContext calendarParticipationStatus]
+ -[MOEventCalendarContext calendarStartDate]
+ -[MOEventCalendarContext calendarTitle]
+ -[MOEventCalendarContext calendarType]
+ -[MOEventCalendarContext copyWithZone:]
+ -[MOEventCalendarContext description]
+ -[MOEventCalendarContext encodeWithCoder:]
+ -[MOEventCalendarContext initWithCoder:]
+ -[MOEventCalendarContext init]
+ -[MOEventCalendarContext setCalendarEndDate:]
+ -[MOEventCalendarContext setCalendarEventIdentifier:]
+ -[MOEventCalendarContext setCalendarIsAllDay:]
+ -[MOEventCalendarContext setCalendarLocation:]
+ -[MOEventCalendarContext setCalendarParticipationStatus:]
+ -[MOEventCalendarContext setCalendarStartDate:]
+ -[MOEventCalendarContext setCalendarTitle:]
+ -[MOEventCalendarContext setCalendarType:]
+ -[MOEventMessageContext .cxx_destruct]
+ -[MOEventMessageContext copyWithZone:]
+ -[MOEventMessageContext description]
+ -[MOEventMessageContext encodeWithCoder:]
+ -[MOEventMessageContext initWithCoder:]
+ -[MOEventMessageContext messageBody]
+ -[MOEventMessageContext messageDate]
+ -[MOEventMessageContext messageIdentifier]
+ -[MOEventMessageContext messageSenderName]
+ -[MOEventMessageContext setMessageBody:]
+ -[MOEventMessageContext setMessageDate:]
+ -[MOEventMessageContext setMessageIdentifier:]
+ -[MOEventMessageContext setMessageSenderName:]
+ -[MOEventPhotoContext .cxx_destruct]
+ -[MOEventPhotoContext copyWithZone:]
+ -[MOEventPhotoContext description]
+ -[MOEventPhotoContext encodeWithCoder:]
+ -[MOEventPhotoContext initWithCoder:]
+ -[MOEventPhotoContext init]
+ -[MOEventPhotoContext photoIdentifier]
+ -[MOEventPhotoContext photoIsScreenshot]
+ -[MOEventPhotoContext photoTextRepresentation]
+ -[MOEventPhotoContext setPhotoIdentifier:]
+ -[MOEventPhotoContext setPhotoIsScreenshot:]
+ -[MOEventPhotoContext setPhotoTextRepresentation:]
+ -[MOEventWorkout setWorkoutSwimmingLocationType:]
+ -[MOEventWorkout workoutSwimmingLocationType]
+ -[MOPromptManager fetchEffectiveDoubleValueForKey:withHandler:]
+ -[MOPromptManager runEnrichmentWithLimit:handler:]
+ GCC_except_table113
+ _$s7Moments11MOTLVWriterC11transferred33_9DB782766A4C3AE6AE3E210C72ADFBB8LLSbvpWvd
+ _$s7Moments11MOTLVWriterC20createUnlinkedWriter15protectionClassACSo20NSFileProtectionTypea_tKFZTf4nd_n
+ _$s7Moments18MOTLVRecordBuilderC14appendOptional_2aty10Foundation4DateVSg_xtAA15MOTLVFieldIndexRzlFAA015MODonationFieldJ0O_TB5
+ _$s7Moments18MOTLVRecordBuilderC14appendOptional_2aty10Foundation4UUIDVSg_xtAA15MOTLVFieldIndexRzlFAA015MODonationFieldJ0O_TB5
+ _$s7Moments22MODonationWriteSessionC10assertOpen33_851E244E6A6886B58B01382E3B42F443LLyyKF
+ _$s7Moments22MODonationWriteSessionC11appendEventyySo7MOEventCKF
+ _$s7Moments22MODonationWriteSessionC11appendEventyySo7MOEventCKFTo
+ _$s7Moments22MODonationWriteSessionC11appendEventyySo7MOEventCKFToTm
+ _$s7Moments22MODonationWriteSessionC12appendBundleyySo07MOEventF0CKF
+ _$s7Moments22MODonationWriteSessionC12appendBundleyySo07MOEventF0CKFTo
+ _$s7Moments22MODonationWriteSessionC16appendPredictionyySo022MOAvailabilityDowntimeF0CKF
+ _$s7Moments22MODonationWriteSessionC16appendPredictionyySo022MOAvailabilityDowntimeF0CKFTo
+ _$s7Moments22MODonationWriteSessionC6createACyKFZ
+ _$s7Moments22MODonationWriteSessionC6createACyKFZTf4d_n
+ _$s7Moments22MODonationWriteSessionC6createACyKFZTo
+ _$s7Moments22MODonationWriteSessionC6finishSo12NSFileHandleCyKF
+ _$s7Moments22MODonationWriteSessionC6finishSo12NSFileHandleCyKFTo
+ _$s7Moments22MODonationWriteSessionC6writer33_851E244E6A6886B58B01382E3B42F443LLAA0B6WriterCvpWvd
+ _$s7Moments22MODonationWriteSessionC7abandonyyF
+ _$s7Moments22MODonationWriteSessionC7abandonyyFTo
+ _$s7Moments22MODonationWriteSessionC8finished33_851E244E6A6886B58B01382E3B42F443LLSbvpWvd
+ _$s7Moments22MODonationWriteSessionC9abandoned33_851E244E6A6886B58B01382E3B42F443LLSbvpWvd
+ _$s7Moments22MODonationWriteSessionCACycfC
+ _$s7Moments22MODonationWriteSessionCACycfc
+ _$s7Moments22MODonationWriteSessionCACycfcTo
+ _$s7Moments22MODonationWriteSessionCMF
+ _$s7Moments22MODonationWriteSessionCMa
+ _$s7Moments22MODonationWriteSessionCMf
+ _$s7Moments22MODonationWriteSessionCMn
+ _$s7Moments22MODonationWriteSessionCMo
+ _$s7Moments22MODonationWriteSessionCMu
+ _$s7Moments22MODonationWriteSessionCN
+ _$s7Moments22MODonationWriteSessionCfD
+ _$s7Moments22MODonationWriteSessionCfETo
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_ypTt0g5Tf4g_n
+ _$sSS_yptMR
+ _$sSS_yptMd
+ _$ss18_DictionaryStorageCySSypGMR
+ _$ss18_DictionaryStorageCySSypGMd
+ _$ss23_ContiguousArrayStorageCySS_yptGMR
+ _$ss23_ContiguousArrayStorageCySS_yptGMd
+ _MOEventBundleTypeEnrichment
+ _MOEventBundleTypeWorkoutPlace
+ _OBJC_CLASS_$_MOEventCalendarContext
+ _OBJC_CLASS_$_MOEventMessageContext
+ _OBJC_CLASS_$_MOEventPhotoContext
+ _OBJC_CLASS_$__TtC7Moments22MODonationWriteSession
+ _OBJC_IVAR_$_MOEvent._calendarContextEvent
+ _OBJC_IVAR_$_MOEvent._messageContextEvent
+ _OBJC_IVAR_$_MOEvent._photoContextEvent
+ _OBJC_IVAR_$_MOEventBundle._enrichedNLString
+ _OBJC_IVAR_$_MOEventBundle._enrichmentRationale
+ _OBJC_IVAR_$_MOEventBundle._originalNLString
+ _OBJC_IVAR_$_MOEventBundle._sourceSuggestionID
+ _OBJC_IVAR_$_MOEventBundle._workoutPlaceAssociationKind
+ _OBJC_IVAR_$_MOEventBundle._workoutPlaceDestinationID
+ _OBJC_IVAR_$_MOEventBundle._workoutPlaceEncompassingID
+ _OBJC_IVAR_$_MOEventBundle._workoutPlaceOriginID
+ _OBJC_IVAR_$_MOEventBundleFetchOptions._allowedInterfaceTypes
+ _OBJC_IVAR_$_MOEventBundleFetchOptions._excludeEnrichmentDedupIneligible
+ _OBJC_IVAR_$_MOEventBundleFetchOptions._excludedInterfaceTypes
+ _OBJC_IVAR_$_MOEventBundleFetchOptions._rehydrated
+ _OBJC_IVAR_$_MOEventBundleFetchOptions._suggestionIDs
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarEndDate
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarEventIdentifier
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarIsAllDay
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarLocation
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarParticipationStatus
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarStartDate
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarTitle
+ _OBJC_IVAR_$_MOEventCalendarContext._calendarType
+ _OBJC_IVAR_$_MOEventMessageContext._messageBody
+ _OBJC_IVAR_$_MOEventMessageContext._messageDate
+ _OBJC_IVAR_$_MOEventMessageContext._messageIdentifier
+ _OBJC_IVAR_$_MOEventMessageContext._messageSenderName
+ _OBJC_IVAR_$_MOEventPhotoContext._photoIdentifier
+ _OBJC_IVAR_$_MOEventPhotoContext._photoIsScreenshot
+ _OBJC_IVAR_$_MOEventPhotoContext._photoTextRepresentation
+ _OBJC_IVAR_$_MOEventWorkout._workoutSwimmingLocationType
+ _OBJC_METACLASS_$_MOEventCalendarContext
+ _OBJC_METACLASS_$_MOEventMessageContext
+ _OBJC_METACLASS_$_MOEventPhotoContext
+ _OBJC_METACLASS_$__TtC7Moments22MODonationWriteSession
+ __CLASS_METHODS__TtC7Moments22MODonationWriteSession
+ __DATA__TtC7Moments22MODonationWriteSession
+ __INSTANCE_METHODS__TtC7Moments22MODonationWriteSession
+ __IVARS__TtC7Moments22MODonationWriteSession
+ __METACLASS_DATA__TtC7Moments22MODonationWriteSession
+ __OBJC_$_CLASS_METHODS_MOEventCalendarContext
+ __OBJC_$_CLASS_METHODS_MOEventMessageContext
+ __OBJC_$_CLASS_METHODS_MOEventPhotoContext
+ __OBJC_$_CLASS_PROP_LIST_MOEventCalendarContext
+ __OBJC_$_CLASS_PROP_LIST_MOEventMessageContext
+ __OBJC_$_CLASS_PROP_LIST_MOEventPhotoContext
+ __OBJC_$_INSTANCE_METHODS_MOEventCalendarContext
+ __OBJC_$_INSTANCE_METHODS_MOEventMessageContext
+ __OBJC_$_INSTANCE_METHODS_MOEventPhotoContext
+ __OBJC_$_INSTANCE_VARIABLES_MOEventCalendarContext
+ __OBJC_$_INSTANCE_VARIABLES_MOEventMessageContext
+ __OBJC_$_INSTANCE_VARIABLES_MOEventPhotoContext
+ __OBJC_$_PROP_LIST_MOEventCalendarContext
+ __OBJC_$_PROP_LIST_MOEventMessageContext
+ __OBJC_$_PROP_LIST_MOEventPhotoContext
+ __OBJC_CLASS_PROTOCOLS_$_MOEventCalendarContext
+ __OBJC_CLASS_PROTOCOLS_$_MOEventMessageContext
+ __OBJC_CLASS_PROTOCOLS_$_MOEventPhotoContext
+ __OBJC_CLASS_RO_$_MOEventCalendarContext
+ __OBJC_CLASS_RO_$_MOEventMessageContext
+ __OBJC_CLASS_RO_$_MOEventPhotoContext
+ __OBJC_METACLASS_RO_$_MOEventCalendarContext
+ __OBJC_METACLASS_RO_$_MOEventMessageContext
+ __OBJC_METACLASS_RO_$_MOEventPhotoContext
+ ___50-[MOPromptManager runEnrichmentWithLimit:handler:]_block_invoke
+ ___50-[MOPromptManager runEnrichmentWithLimit:handler:]_block_invoke_2
+ ___63-[MOPromptManager fetchEffectiveDoubleValueForKey:withHandler:]_block_invoke
+ ___63-[MOPromptManager fetchEffectiveDoubleValueForKey:withHandler:]_block_invoke_2
+ _kMOEnrichedInfoKeyEnrichedNL
+ _kMOEnrichedInfoKeyOriginalNL
+ _kMOEnrichedInfoKeyRationale
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$eventForWorkoutPlaceID:
+ _objc_msgSend$fetchEffectiveDoubleValueForKey:withHandler:
+ _objc_msgSend$runEnrichmentWithContext:limit:andHandler:
+ _objc_msgSend$workoutPlaceAssociationKind
+ _objc_msgSend$workoutPlaceDestinationID
+ _objc_msgSend$workoutPlaceEncompassingID
+ _objc_msgSend$workoutPlaceOriginID
+ _swift_deletedMethodError
+ _symbolic SS_ypt
+ _symbolic _____ 7Moments22MODonationWriteSessionC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
- GCC_except_table109
CStrings:
+ "Enriched"
+ "Enriched Evidence"
+ "MOEventCalendarContext"
+ "MOEventMessageContext"
+ "MOEventPhotoContext"
+ "Moments.MODonationWriteSession"
+ "allowedInterfaceTypes"
+ "calendar event title, %@"
+ "calendarContextEvent"
+ "calendarEndDate"
+ "calendarEventIdentifier"
+ "calendarIsAllDay"
+ "calendarLocation"
+ "calendarParticipationStatus"
+ "calendarStartDate"
+ "calendarTitle"
+ "calendarType"
+ "calling fetchEffectiveDoubleValueForKey completed"
+ "calling fetchEffectiveDoubleValueForKey: %@"
+ "calling runEnrichmentWithContext completed"
+ "calling runEnrichmentWithContext, limit %lu"
+ "enrichedNL"
+ "enrichedNLString"
+ "enrichment"
+ "excludeEnrichmentDedupIneligible"
+ "excludedInterfaceTypes"
+ "message from, %@"
+ "messageBody"
+ "messageContextEvent"
+ "messageDate"
+ "messageIdentifier"
+ "messageSenderName"
+ "originalNL"
+ "originalNLString"
+ "photo context, %@"
+ "photoContextEvent"
+ "photoIdentifier"
+ "photoIsScreenshot"
+ "photoTextRepresentation"
+ "rationale"
+ "rehydrated"
+ "session abandoned"
+ "session already finished"
+ "sourceSuggestionID"
+ "suggestionIDs"
+ "workoutPlaceAssociationKind"
+ "workoutPlaceDestinationID"
+ "workoutPlaceEncompassingID"
+ "workoutPlaceOriginID"
+ "workoutSwimmingLocationType"
+ "workout_place"
- "MOAction.m"
- "MOAppEngagementReporter.m"
- "MOConnectionManager.m"
- "MODefaultsManager.m"
- "MODictionaryEncoder.m"
- "MOEvent.m"
- "MOEventBundle.m"
- "MOEventBundleLabelCondition.m"
- "MOEventBundleLabelFormat.m"
- "MOEventBundleLabelLocalizer.m"
- "MOEventBundleLabelTemplate.m"
- "MOEventExtendedAtrributes.m"
- "MOInteraction.m"
- "MOMediaPlaySession.m"
- "MOPlace.m"
- "MOResource.m"
- "MOTime.m"
- "MOXPCContext.m"
```
