## SiriSuggestionsBaseModel

> `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel`

```diff

-3402.61.1.0.0
-  __TEXT.__text: 0x9ea4
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__const: 0x7c8
-  __TEXT.__cstring: 0xe82
-  __TEXT.__constg_swiftt: 0x338
-  __TEXT.__swift5_typeref: 0x1c2
-  __TEXT.__swift5_fieldmd: 0x17c
-  __TEXT.__oslogstring: 0x5d
-  __TEXT.__swift5_proto: 0x70
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_reflstr: 0x96
-  __TEXT.__swift5_capture: 0x20
+3404.70.4.0.0
+  __TEXT.__text: 0x16840
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__const: 0x984
+  __TEXT.__cstring: 0x1e6a
+  __TEXT.__swift5_typeref: 0x30e
+  __TEXT.__oslogstring: 0xe9
+  __TEXT.__constg_swiftt: 0x3d4
+  __TEXT.__swift5_fieldmd: 0x204
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift5_reflstr: 0xd0
+  __TEXT.__swift5_capture: 0x90
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__eh_frame: 0x478
-  __TEXT.__objc_methname: 0xe
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__eh_frame: 0x568
+  __TEXT.__objc_methname: 0x48
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__auth_ptr: 0xf0
-  __AUTH_CONST.__const: 0x5b8
-  __AUTH_CONST.__objc_const: 0x938
-  __AUTH.__data: 0x820
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0xd80
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_selrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__auth_ptr: 0x180
+  __AUTH_CONST.__const: 0x1490
+  __AUTH_CONST.__objc_const: 0x9f0
+  __AUTH.__data: 0x940
+  __DATA.__data: 0x548
+  __DATA.__common: 0x318
+  __DATA.__bss: 0xf00
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared
   - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
+  - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 224
-  Symbols:   169
-  CStrings:  104
+  Functions: 434
+  Symbols:   278
+  CStrings:  248
 
Symbols:
+ _OBJC_CLASS_$_INPerson
+ _OBJC_CLASS_$_INSendMessageAttachment
+ _OBJC_CLASS_$_INSendMessageIntent
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x25
+ _objc_retain_x20
+ _objc_retain_x8
+ _swift_dynamicCastObjCClass
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getFunctionTypeMetadata0
+ _swift_getObjCClassMetadata
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStructMetadataWithLayoutString
+ _swift_lookUpClassMethod
+ _swift_storeEnumTagSinglePayloadGeneric
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
CStrings:
+ ".ApplyFilterIntent"
+ "/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/"
+ "AudiobookAppEntity"
+ "BaseSuggestions#"
+ "BaseSuggestions#General_SaveArticle"
+ "BaseSuggestions#General_ShareThisWithContact"
+ "BaseSuggestions#General_SummarizeArticle"
+ "BaseSuggestions#Settings_ChangeSettings"
+ "BaseSuggestionsOwnerDefinitionFactory:: AppIntent suggestion '%s' not added due to feature flag 'handCraftedAppIntentSuggestions' is off"
+ "Books_ChangeFontSize"
+ "Books_ChangeTheme"
+ "Books_OpenCollection"
+ "Books_OpenCollectionBookStore"
+ "Books_SleepTimer"
+ "Books_ToggleScrolling"
+ "Clock_AddWorldClock"
+ "Contacts_UpdatePoster"
+ "Files_CompressFolder"
+ "Files_ContentsOf"
+ "Files_GroupBy"
+ "Files_HideGrid"
+ "Files_Search"
+ "Files_SearchFor"
+ "Fitness_ActivityRings"
+ "Fitness_Awards"
+ "Fitness_Breathe"
+ "Fitness_Cardio"
+ "Fitness_LastWorkout"
+ "Fitness_NextWorkout"
+ "Fitness_RecommendWorkout"
+ "Fitness_YesterdayRings"
+ "Freeform_AddStickyNote"
+ "Freeform_ChangeBackground"
+ "Freeform_ChangeTextSize"
+ "Freeform_CreateBoard"
+ "Freeform_CreateNamedBoard"
+ "Freeform_FavoriteBoard"
+ "Freeform_HideGrid"
+ "Freeform_ShareBoardWithPerson"
+ "GEOPOICategoryAirport"
+ "GEOPOICategoryFitnessCenter"
+ "GEOPOICategoryFoodMarket"
+ "GEOPOICategoryNightlife"
+ "GEOPOICategoryPark"
+ "GEOPOICategoryRestaurant"
+ "GEOPOICategoryStore"
+ "Health_ConnectedApps"
+ "Health_GoodSleep"
+ "Health_LogMood"
+ "Health_MentalHealthAssessment"
+ "Health_RingsClosedThisMonth"
+ "Health_SleepSchedule"
+ "Health_StepCount"
+ "Health_StepsThisWeek"
+ "Health_TrackCycle"
+ "Health_Trends"
+ "Journal_CreateEntry"
+ "Journal_RecordEntry"
+ "Mail_FilterInbox"
+ "Mail_FilterInboxAttachments"
+ "Mail_FlagEmails"
+ "Mail_GetSummary"
+ "Mail_SendAnEmail"
+ "Mail_SetReadLater"
+ "Mail_UnreadMail"
+ "Maps_AddToFavorites"
+ "Maps_CreateRoutePlan"
+ "Maps_ShowNearbyGuides"
+ "Messages_TakeSelfie"
+ "Music_GoToMadeForYou"
+ "Music_GoToReleases"
+ "Music_GoToReplay"
+ "Music_GoToStations"
+ "Music_ShareThisWithContact"
+ "Music_ShowLyrics"
+ "News_Feed"
+ "News_Read"
+ "News_SaveArticle"
+ "News_ShareThisWithContact"
+ "News_SummarizeArticle"
+ "News_Trending"
+ "Notes_AddCollaborator"
+ "Notes_AddTagToFolder"
+ "Notes_AppendToNote"
+ "Notes_OpenAttachments"
+ "Notes_ShowNotesWithAttachments"
+ "Notes_StartAudioRecording"
+ "Phone_PlayVoicemail"
+ "Photos_ApplyFilter"
+ "Photos_ApplyStyle"
+ "Photos_Cleanup"
+ "Photos_CreateMemory"
+ "Photos_Crop"
+ "Photos_EnableDepth"
+ "Photos_EnhanceThis"
+ "Photos_PlayFavoriteMemories"
+ "Photos_SetExposure"
+ "Photos_SetSaturation"
+ "Photos_SetWarmth"
+ "Podcasts_FollowShow"
+ "Podcasts_PlayAppleNewsToday"
+ "Podcasts_ShowLatestsEpisodes"
+ "Podcasts_Trending"
+ "Reminders_DueToday"
+ "Reminders_OpenGuide"
+ "Safari_AddTabReadingList"
+ "Safari_MoveTabToGroup"
+ "Safari_NewNamedTabGroup"
+ "Safari_NewPrivateTab"
+ "Safari_NewTab"
+ "Safari_OpenBookmark"
+ "Safari_OpenReadingListItem"
+ "Settings_AddCardToWallet"
+ "Settings_BatteryHealth"
+ "Settings_CameraSettings"
+ "Settings_FocusModeSettings"
+ "Settings_Storage"
+ "Settings_iOSOnlySettings"
+ "Settings_iOSmacOSSettings"
+ "Stocks_AddSymbolToWatchlist"
+ "Stocks_CheckMarketToday"
+ "Stocks_FiveYear"
+ "Stocks_HighestGain"
+ "Stocks_Markets"
+ "Stocks_Mine"
+ "Stocks_NewsAboutSymbol"
+ "Stocks_SaveArticle"
+ "Stocks_ShareThisWithContact"
+ "Stocks_SummarizeArticle"
+ "System_CheckApplePay"
+ "System_CheckPopularItem"
+ "System_CheckSales"
+ "System_CheckVeganOption"
+ "System_GetYelpRating"
+ "System_OpenGroceryList"
+ "System_RestartDevice"
+ "System_Screenshot"
+ "System_SearchCoupons"
+ "System_SearchMenu"
+ "System_SearchRestaurants"
+ "System_ShowActivityRing"
+ "System_ShowPlaceDetails"
+ "TV_ShowGenres"
+ "TV_SportsScores"
+ "Translate_TranslatePhrase"
+ "Weather_Condition"
+ "Weather_FeelsLike"
+ "Weather_SpecificConditionAQI"
+ "Weather_SpecificConditionCity"
+ "Weather_SpecificConditionHumidity"
+ "_TtC24SiriSuggestionsBaseModel20PodcastsShowResolver"
+ "announceNotification"
+ "attachments"
+ "com.apple.graphic-icon.airplane-mode"
+ "com.apple.graphic-icon.battery"
+ "com.apple.graphic-icon.bluetooth"
+ "com.apple.graphic-icon.cellular"
+ "com.apple.graphic-icon.display"
+ "com.apple.graphic-icon.focus"
+ "com.apple.graphic-icon.notifications"
+ "com.apple.graphic-icon.personal-hotspot"
+ "com.apple.graphic-icon.sound"
+ "com.apple.graphic-icon.wifi"
+ "contactIdentifier"
+ "currentLocation"
+ "displayName"
+ "flashlight.on.fill"
+ "freeformBoardName"
+ "newsArticleTitle"
+ "notesTagAndFolder"
+ "proactiveCallContact"
+ "proactiveFacetimeContact"
+ "proactiveMessageContact"
+ "readingListItemTitle"
+ "sirikit.intent.calendar.CreateEventIntent"
+ "sirikit.intent.calendar.FindEventsIntent"
+ "stocksArticleTitle"
+ "weatherCondition"
- "Calendar_CheckConflicts"
- "Calendar_CreateNamedEvent"
- "Clock_DeleteAllAlarms"
- "Clock_SetAlarmRecurring"
- "Clock_SetTimer"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Health_RemindExercise"
- "Insufficient space allocated to copy string contents"
- "Messages_ReadMessages"
- "Music_PlayDiscoveryStation"
- "Music_PlayMoreLikeThis"
- "Music_PlayNewMusicMix"
- "Music_PlayPublicPlaylist"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "System_BookRideshare"
- "System_FlipCoin"
- "System_TellJoke"
- "TV_NewMovies"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
