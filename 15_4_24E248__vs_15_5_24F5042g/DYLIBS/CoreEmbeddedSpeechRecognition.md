## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x1b7c08
+3405.20.3.0.0
+  __TEXT.__text: 0x1b0d58
   __TEXT.__auth_stubs: 0x2e90
-  __TEXT.__objc_methlist: 0x4448
+  __TEXT.__objc_methlist: 0x3d98
   __TEXT.__const: 0x1638
-  __TEXT.__cstring: 0xaafb
-  __TEXT.__swift5_typeref: 0x1f54
-  __TEXT.__oslogstring: 0x71f7
-  __TEXT.__swift5_capture: 0x3dd0
+  __TEXT.__cstring: 0x9a93
+  __TEXT.__swift5_typeref: 0x1f76
+  __TEXT.__oslogstring: 0x72be
+  __TEXT.__swift5_capture: 0x3e84
   __TEXT.__swift5_reflstr: 0xb83
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__constg_swiftt: 0x1024

   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0xe0
-  __TEXT.__swift_as_entry: 0x1a0
-  __TEXT.__swift_as_ret: 0x20c
+  __TEXT.__swift_as_entry: 0x1a4
+  __TEXT.__swift_as_ret: 0x210
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0xb28
-  __TEXT.__ustring: 0x112
-  __TEXT.__unwind_info: 0x2578
-  __TEXT.__eh_frame: 0x2bf8
-  __TEXT.__objc_classname: 0x9d3
-  __TEXT.__objc_methname: 0xe35b
-  __TEXT.__objc_methtype: 0x2b55
-  __TEXT.__objc_stubs: 0x7a40
-  __DATA_CONST.__got: 0x12a0
-  __DATA_CONST.__const: 0x608
+  __TEXT.__unwind_info: 0x2508
+  __TEXT.__eh_frame: 0x2c48
+  __TEXT.__objc_classname: 0x9d1
+  __TEXT.__objc_methname: 0xc5d2
+  __TEXT.__objc_methtype: 0x2b10
+  __TEXT.__objc_stubs: 0x6ea0
+  __DATA_CONST.__got: 0xed0
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f70
+  __DATA_CONST.__objc_selrefs: 0x2968
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x1c8
-  __DATA_CONST.__objc_arraydata: 0x228
+  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x1760
   __AUTH_CONST.__auth_ptr: 0x558
-  __AUTH_CONST.__const: 0xbbf0
-  __AUTH_CONST.__cfstring: 0x6880
-  __AUTH_CONST.__objc_const: 0x78e0
-  __AUTH_CONST.__objc_intobj: 0x5a0
-  __AUTH_CONST.__objc_arrayobj: 0x300
+  __AUTH_CONST.__const: 0xbda8
+  __AUTH_CONST.__cfstring: 0x3ee0
+  __AUTH_CONST.__objc_const: 0x7ad0
+  __AUTH_CONST.__objc_intobj: 0x570
+  __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x17d8
-  __AUTH.__data: 0xcb0
-  __DATA.__objc_ivar: 0x4a8
-  __DATA.__data: 0x2928
+  __AUTH.__data: 0xcc8
+  __DATA.__objc_ivar: 0x4d0
+  __DATA.__data: 0x28f8
   __DATA.__bss: 0x1450
-  __DATA.__common: 0x38
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4747
-  Symbols:   4722
-  CStrings:  4211
+  Functions: 4626
+  Symbols:   4378
+  CStrings:  3728
 
Symbols:
+ +[CESRUtilities isSiriUODWithASROnServerSupported]
+ -[CESREntityCleanupConfig .cxx_destruct]
+ -[CESREntityCleanupConfig _parseJsonObject:]
+ -[CESREntityCleanupConfig applyRegex]
+ -[CESREntityCleanupConfig description]
+ -[CESREntityCleanupConfig enableDatatypeCleanupFromNonAppEntities]
+ -[CESREntityCleanupConfig enableEmojiCleanupFromAppEntities]
+ -[CESREntityCleanupConfig enableEmojiCleanupFromNonAppEntities]
+ -[CESREntityCleanupConfig enableSpecialCharacterCleanupFromAppEntities]
+ -[CESREntityCleanupConfig enableSpecialCharacterCleanupFromNonAppEntities]
+ -[CESREntityCleanupConfig initWithJsonObject:]
+ -[CESREntityCleanupConfig keepEmojis]
+ -[CESREntityCleanupConfig keepSpecialCharacters]
+ -[CESREntityCleanupConfig specialCharactersToRemove]
+ -[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]
+ -[CESRSpeechProfileBuilder initWithDirectory:locale:userId:personaId:dataProtectionClass:isInUserVault:]
+ -[CESRSpeechProfileConfig entityCleanupConfig]
+ -[CESRSpeechProfileSettings _isAssistantRequired]
+ -[CESRSpeechProfileSettings _isDictationRequired]
+ -[CESRSpeechProfileSettings refreshRequiredLocales:]
+ GCC_except_table1000
+ GCC_except_table1001
+ GCC_except_table1005
+ GCC_except_table1006
+ GCC_except_table1009
+ GCC_except_table1109
+ GCC_except_table1201
+ GCC_except_table1208
+ GCC_except_table1212
+ GCC_except_table1258
+ GCC_except_table1266
+ GCC_except_table1271
+ GCC_except_table1275
+ GCC_except_table150
+ GCC_except_table180
+ GCC_except_table204
+ GCC_except_table272
+ GCC_except_table291
+ GCC_except_table295
+ GCC_except_table338
+ GCC_except_table359
+ GCC_except_table383
+ GCC_except_table497
+ GCC_except_table502
+ GCC_except_table505
+ GCC_except_table509
+ GCC_except_table512
+ GCC_except_table515
+ GCC_except_table518
+ GCC_except_table521
+ GCC_except_table524
+ GCC_except_table527
+ GCC_except_table651
+ GCC_except_table689
+ GCC_except_table882
+ GCC_except_table889
+ GCC_except_table996
+ GCC_except_table997
+ GCC_except_table998
+ GCC_except_table999
+ OBJC_IVAR_$_CESREntityCleanupConfig._applyRegex
+ OBJC_IVAR_$_CESREntityCleanupConfig._enableDatatypeCleanupFromNonAppEntities
+ OBJC_IVAR_$_CESREntityCleanupConfig._enableEmojiCleanupFromAppEntities
+ OBJC_IVAR_$_CESREntityCleanupConfig._enableEmojiCleanupFromNonAppEntities
+ OBJC_IVAR_$_CESREntityCleanupConfig._enableSpecialCharacterCleanupFromAppEntities
+ OBJC_IVAR_$_CESREntityCleanupConfig._enableSpecialCharacterCleanupFromNonAppEntities
+ OBJC_IVAR_$_CESREntityCleanupConfig._keepEmojis
+ OBJC_IVAR_$_CESREntityCleanupConfig._keepSpecialCharacters
+ OBJC_IVAR_$_CESREntityCleanupConfig._specialCharactersToRemove
+ OBJC_IVAR_$_CESRSpeechProfileConfig._entityCleanupConfig
+ _OBJC_CLASS_$_CESREntityCleanupConfig
+ _OBJC_METACLASS_$_CESREntityCleanupConfig
+ _PROTOCOLS_CoreEmbeddedSpeechAnalyzer.851
+ __120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.380
+ __Block_byref_object_copy_.1071
+ __Block_byref_object_copy_.1482
+ __Block_byref_object_copy_.2883
+ __Block_byref_object_copy_.4210
+ __Block_byref_object_copy_.956
+ __Block_byref_object_dispose_.1072
+ __Block_byref_object_dispose_.1483
+ __Block_byref_object_dispose_.2884
+ __Block_byref_object_dispose_.4211
+ __Block_byref_object_dispose_.957
+ __OBJC_$_INSTANCE_METHODS_CESREntityCleanupConfig
+ __OBJC_$_INSTANCE_VARIABLES_CESREntityCleanupConfig
+ __OBJC_$_PROP_LIST_CESREntityCleanupConfig
+ __OBJC_CLASS_RO_$_CESREntityCleanupConfig
+ __OBJC_METACLASS_RO_$_CESREntityCleanupConfig
+ ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke
+ __block_literal_global.1954
+ __block_literal_global.2958
+ __block_literal_global.3607
+ __block_literal_global.3962
+ __block_literal_global.4247
+ __block_literal_global.428
+ __block_literal_global.763
+ __block_literal_global.775
+ _objc_msgSend$_isAssistantRequired
+ _objc_msgSend$_isDictationRequired
+ _objc_msgSend$_setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:
+ _objc_msgSend$initWithDirectory:locale:userId:personaId:dataProtectionClass:isInUserVault:
+ _objc_msgSend$isSiriUODWithASROnServerSupported
+ _objc_msgSend$refreshRequiredLocales:
+ _objc_msgSend$setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:completion:
+ _symbolic ScTyyt______pGSg s5ErrorP
+ _symbolic ______pIegHzo_ s5ErrorP
+ sharedManager.onceToken.2957
+ sharedManager.onceToken.762
+ sharedManager.sharedMyManager.2959
+ sharedManager.sharedMyManager.764
- +[CESRSpeechProfileTestData AppCustomCarName_1]
- +[CESRSpeechProfileTestData AppCustomCarProfileName_1]
- +[CESRSpeechProfileTestData AppCustomContactGroupName_1]
- +[CESRSpeechProfileTestData AppCustomContactGroupName_vocabularyString:vocabularyIdentifier:sourceItemIdentifier:]
- +[CESRSpeechProfileTestData AppCustomContactName_1]
- +[CESRSpeechProfileTestData AppCustomContactName_vocabularyString:vocabularyIdentifier:sourceItemIdentifier:]
- +[CESRSpeechProfileTestData AppCustomMediaAudiobookAuthorName_1]
- +[CESRSpeechProfileTestData AppCustomMediaAudiobookTitle_1]
- +[CESRSpeechProfileTestData AppCustomMediaMusicArtistName_1]
- +[CESRSpeechProfileTestData AppCustomMediaPlaylistTitle_1]
- +[CESRSpeechProfileTestData AppCustomMediaShowTitle_1]
- +[CESRSpeechProfileTestData AppCustomNotebookItemGroupName_1]
- +[CESRSpeechProfileTestData AppCustomNotebookItemTitle_1]
- +[CESRSpeechProfileTestData AppCustomPaymentsAccountNickname_1]
- +[CESRSpeechProfileTestData AppCustomPaymentsOrganizationName_1]
- +[CESRSpeechProfileTestData AppCustomPhotoAlbumName_1]
- +[CESRSpeechProfileTestData AppCustomPhotoTag_1]
- +[CESRSpeechProfileTestData AppCustomVoiceCommandName_1]
- +[CESRSpeechProfileTestData AppCustomWorkoutActivityName_1]
- +[CESRSpeechProfileTestData AppGlobalMediaAudiobookAuthor_1]
- +[CESRSpeechProfileTestData AppGlobalMediaAudiobookTitle_1]
- +[CESRSpeechProfileTestData AppGlobalMediaMusicArtistName_1]
- +[CESRSpeechProfileTestData AppGlobalMediaPlaylistTitle_1]
- +[CESRSpeechProfileTestData AppGlobalMediaShowTitle_1]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_1]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_2]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_3]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_4]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_5]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_6]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_7]
- +[CESRSpeechProfileTestData AppIntentsIndexedEntity_emptyDisplayRepresentation]
- +[CESRSpeechProfileTestData AppIntentsIndexedEnum_1]
- +[CESRSpeechProfileTestData AppShortcutEntity_1]
- +[CESRSpeechProfileTestData AppShortcutPhrase_1]
- +[CESRSpeechProfileTestData AppShortcutPhrase_2]
- +[CESRSpeechProfileTestData AppShortcutPhrase_3]
- +[CESRSpeechProfileTestData CalendarEvent_1]
- +[CESRSpeechProfileTestData CascadeSerializedSets_1]
- +[CESRSpeechProfileTestData Contact_10]
- +[CESRSpeechProfileTestData Contact_11]
- +[CESRSpeechProfileTestData Contact_12]
- +[CESRSpeechProfileTestData Contact_13]
- +[CESRSpeechProfileTestData Contact_14]
- +[CESRSpeechProfileTestData Contact_15]
- +[CESRSpeechProfileTestData Contact_16]
- +[CESRSpeechProfileTestData Contact_17]
- +[CESRSpeechProfileTestData Contact_18]
- +[CESRSpeechProfileTestData Contact_19]
- +[CESRSpeechProfileTestData Contact_1]
- +[CESRSpeechProfileTestData Contact_20]
- +[CESRSpeechProfileTestData Contact_21]
- +[CESRSpeechProfileTestData Contact_22]
- +[CESRSpeechProfileTestData Contact_23]
- +[CESRSpeechProfileTestData Contact_24]
- +[CESRSpeechProfileTestData Contact_25]
- +[CESRSpeechProfileTestData Contact_26]
- +[CESRSpeechProfileTestData Contact_27]
- +[CESRSpeechProfileTestData Contact_28]
- +[CESRSpeechProfileTestData Contact_29]
- +[CESRSpeechProfileTestData Contact_2]
- +[CESRSpeechProfileTestData Contact_30]
- +[CESRSpeechProfileTestData Contact_31]
- +[CESRSpeechProfileTestData Contact_32]
- +[CESRSpeechProfileTestData Contact_33]
- +[CESRSpeechProfileTestData Contact_34]
- +[CESRSpeechProfileTestData Contact_35]
- +[CESRSpeechProfileTestData Contact_36]
- +[CESRSpeechProfileTestData Contact_3]
- +[CESRSpeechProfileTestData Contact_4]
- +[CESRSpeechProfileTestData Contact_5]
- +[CESRSpeechProfileTestData Contact_6]
- +[CESRSpeechProfileTestData Contact_7]
- +[CESRSpeechProfileTestData Contact_8]
- +[CESRSpeechProfileTestData Contact_9]
- +[CESRSpeechProfileTestData Contact_givenName:familyName:sourceItemIdentifier:]
- +[CESRSpeechProfileTestData FindMyDevice_1]
- +[CESRSpeechProfileTestData FindMyDevice_2]
- +[CESRSpeechProfileTestData FitnessGuest_1]
- +[CESRSpeechProfileTestData HealthMedication_1]
- +[CESRSpeechProfileTestData Home_1]
- +[CESRSpeechProfileTestData Home_2]
- +[CESRSpeechProfileTestData Home_3]
- +[CESRSpeechProfileTestData Home_withType:name:sourceItemIdentifier:]
- +[CESRSpeechProfileTestData InstalledApp_1]
- +[CESRSpeechProfileTestData InstalledApp_2]
- +[CESRSpeechProfileTestData InstalledApp_3]
- +[CESRSpeechProfileTestData InstalledApp_4]
- +[CESRSpeechProfileTestData InstalledApp_displayAppName:]
- +[CESRSpeechProfileTestData Media_1]
- +[CESRSpeechProfileTestData Media_2]
- +[CESRSpeechProfileTestData Media_3]
- +[CESRSpeechProfileTestData Media_4]
- +[CESRSpeechProfileTestData Media_5]
- +[CESRSpeechProfileTestData Media_6]
- +[CESRSpeechProfileTestData Media_7]
- +[CESRSpeechProfileTestData Media_8]
- +[CESRSpeechProfileTestData Media_withType:name:sourceItemIdentifier:]
- +[CESRSpeechProfileTestData Podcast_1]
- +[CESRSpeechProfileTestData Podcast_2]
- +[CESRSpeechProfileTestData RadioStation_1]
- +[CESRSpeechProfileTestData RadioStation_2]
- +[CESRSpeechProfileTestData RadioStation_3]
- +[CESRSpeechProfileTestData SignificantLocation_1]
- +[CESRSpeechProfileTestData SiriLearnedContact_1]
- +[CESRSpeechProfileTestData SiriLearnedMedia_1]
- +[CESRSpeechProfileTestData SiriLearnedMedia_2]
- +[CESRSpeechProfileTestData SiriLearnedMedia_3]
- +[CESRSpeechProfileTestData SiriLearnedMedia_4]
- +[CESRSpeechProfileTestData SiriLearnedMedia_5]
- +[CESRSpeechProfileTestData SiriLearnedMedia_6]
- +[CESRSpeechProfileTestData SiriLearnedMedia_7]
- +[CESRSpeechProfileTestData SiriLearnedMedia_8]
- +[CESRSpeechProfileTestData UserAccountIdentity_1]
- +[CESRSpeechProfileTestData itemInstanceForItemType:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomCarNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomContactGroupNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomContactNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomMediaAudiobookAuthorNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomMediaAudiobookTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomMediaMusicArtistNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomMediaPlaylistTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomMediaShowTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomNotebookItemGroupNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomNotebookItemTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomPaymentsAccountNicknameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomPaymentsOrganizationNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomPhotoAlbumNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomPhotoTagWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomVoiceCommandNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppCustomWorkoutActivityNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:]
- +[CESRSpeechProfileTestData sampleItem_AppIntentsIndexedEntityWithSourceItemIdentifier:typeIdentifier:title:subtitle:synonyms:typeDisplayName:typeDisplaySynonyms:]
- +[CESRSpeechProfileTestData sampleItem_AppShortcutPhraseWithSourceItemIdentifier:phrase:baseTemplate:templateParameterValue:]
- +[CESRSpeechProfileTestData sampleItem_ContactWithSourceItemIdentifier:givenName:middleName:familyName:nickname:organizationName:phoneticGivenName:phoneticMiddleName:phoneticFamilyName:phoneticOrganizationName:]
- +[CESRSpeechProfileTestData sampleItem_HealthMedicationWithSourceItemIdentifier:name:nickname:]
- +[CESRSpeechProfileTestData sampleItem_HomeAccessoryWithSourceItemIdentifier:assistantHomeKitIdentifier:deviceType:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeRoomWithSourceItemIdentifier:assistantHomeKitIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeSceneWithSourceItemIdentifier:assistantHomeKitIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeServiceAreaMapWithSourceItemIdentifier:serviceAreaMapName:]
- +[CESRSpeechProfileTestData sampleItem_HomeServiceAreaWithSourceItemIdentifier:serviceAreaName:]
- +[CESRSpeechProfileTestData sampleItem_HomeServiceGroupWithSourceItemIdentifier:assistantHomeKitIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeServiceWithSourceItemIdentifier:assistantHomeKitIdentifier:deviceType:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeWithSourceItemIdentifier:assistantHomeKitIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_HomeZoneWithSourceItemIdentifier:assistantHomeKitIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_InstalledAppWithSourceItemIdentifier:bundleVersion:bundleIdentifier:bundleName:displayAppName:spokenName:alternativeAppNames:carPlayAlternativeDisplayName:spotlightName:providerName:]
- +[CESRSpeechProfileTestData sampleItem_MediaAlbumArtistWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaAlbumWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaAudiobookArtistWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaAudiobookWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaPlaylistWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaSongArtistWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_MediaSongWithSourceItemIdentifier:linkedIdentifiers:name:]
- +[CESRSpeechProfileTestData sampleItem_PodcastPlaylistWithSourceItemIdentifier:name:]
- +[CESRSpeechProfileTestData sampleItem_PodcastShowWithSourceItemIdentifier:name:author:]
- +[CESRSpeechProfileTestData sampleItem_RadioStationWithSourceItemIdentifier:name:callSign:frequency:channel:signalType:]
- +[CESRSpeechProfileTestData sampleItem_UserAccountIdentityWithSourceItemIdentifier:userName:givenName:]
- +[CESRUtilities isSiriUODwithASROnServerSupported]
- -[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:]
- -[CESRSpeechProfileBuilder initWithDirectory:locale:userId:dataProtectionClass:]
- -[CESRSpeechProfileSettings _assistantLocale]
- -[CESRSpeechProfileSettings _dictationLocales]
- -[CESRSpeechProfileSettings refreshLocalesIfNeeded]
- -[CESRSpeechProfileSettings refreshLocales]
- GCC_except_table1039
- GCC_except_table1046
- GCC_except_table1153
- GCC_except_table1154
- GCC_except_table1155
- GCC_except_table1156
- GCC_except_table1157
- GCC_except_table1158
- GCC_except_table1162
- GCC_except_table1163
- GCC_except_table1166
- GCC_except_table1252
- GCC_except_table1344
- GCC_except_table1351
- GCC_except_table1355
- GCC_except_table1401
- GCC_except_table1409
- GCC_except_table1414
- GCC_except_table1418
- GCC_except_table151
- GCC_except_table181
- GCC_except_table205
- GCC_except_table273
- GCC_except_table292
- GCC_except_table296
- GCC_except_table339
- GCC_except_table360
- GCC_except_table384
- GCC_except_table498
- GCC_except_table503
- GCC_except_table506
- GCC_except_table510
- GCC_except_table513
- GCC_except_table516
- GCC_except_table519
- GCC_except_table522
- GCC_except_table525
- GCC_except_table528
- GCC_except_table652
- GCC_except_table690
- _OBJC_CLASS_$_CCAppCustomCarNameContent
- _OBJC_CLASS_$_CCAppCustomCarNameMetaContent
- _OBJC_CLASS_$_CCAppCustomCarProfileNameContent
- _OBJC_CLASS_$_CCAppCustomCarProfileNameMetaContent
- _OBJC_CLASS_$_CCAppCustomContactGroupNameContent
- _OBJC_CLASS_$_CCAppCustomContactGroupNameMetaContent
- _OBJC_CLASS_$_CCAppCustomContactNameContent
- _OBJC_CLASS_$_CCAppCustomContactNameMetaContent
- _OBJC_CLASS_$_CCAppCustomMediaAudiobookAuthorNameContent
- _OBJC_CLASS_$_CCAppCustomMediaAudiobookAuthorNameMetaContent
- _OBJC_CLASS_$_CCAppCustomMediaAudiobookTitleContent
- _OBJC_CLASS_$_CCAppCustomMediaAudiobookTitleMetaContent
- _OBJC_CLASS_$_CCAppCustomMediaMusicArtistNameContent
- _OBJC_CLASS_$_CCAppCustomMediaMusicArtistNameMetaContent
- _OBJC_CLASS_$_CCAppCustomMediaPlaylistTitleContent
- _OBJC_CLASS_$_CCAppCustomMediaPlaylistTitleMetaContent
- _OBJC_CLASS_$_CCAppCustomMediaShowTitleContent
- _OBJC_CLASS_$_CCAppCustomMediaShowTitleMetaContent
- _OBJC_CLASS_$_CCAppCustomNotebookItemGroupNameContent
- _OBJC_CLASS_$_CCAppCustomNotebookItemGroupNameMetaContent
- _OBJC_CLASS_$_CCAppCustomNotebookItemTitleContent
- _OBJC_CLASS_$_CCAppCustomNotebookItemTitleMetaContent
- _OBJC_CLASS_$_CCAppCustomPaymentsAccountNicknameContent
- _OBJC_CLASS_$_CCAppCustomPaymentsAccountNicknameMetaContent
- _OBJC_CLASS_$_CCAppCustomPaymentsOrganizationNameContent
- _OBJC_CLASS_$_CCAppCustomPaymentsOrganizationNameMetaContent
- _OBJC_CLASS_$_CCAppCustomPhotoAlbumNameContent
- _OBJC_CLASS_$_CCAppCustomPhotoAlbumNameMetaContent
- _OBJC_CLASS_$_CCAppCustomPhotoTagContent
- _OBJC_CLASS_$_CCAppCustomPhotoTagMetaContent
- _OBJC_CLASS_$_CCAppCustomVoiceCommandNameContent
- _OBJC_CLASS_$_CCAppCustomVoiceCommandNameMetaContent
- _OBJC_CLASS_$_CCAppCustomWorkoutActivityNameContent
- _OBJC_CLASS_$_CCAppCustomWorkoutActivityNameMetaContent
- _OBJC_CLASS_$_CCAppEntityDisplayRepresentation
- _OBJC_CLASS_$_CCAppEntityTypeDisplayRepresentation
- _OBJC_CLASS_$_CCAppEnumCase
- _OBJC_CLASS_$_CCAppEnumCaseDisplayRepresentation
- _OBJC_CLASS_$_CCAppEnumTypeDisplayRepresentation
- _OBJC_CLASS_$_CCAppGlobalMediaAudiobookAuthorContent
- _OBJC_CLASS_$_CCAppGlobalMediaAudiobookAuthorMetaContent
- _OBJC_CLASS_$_CCAppGlobalMediaAudiobookTitleContent
- _OBJC_CLASS_$_CCAppGlobalMediaAudiobookTitleMetaContent
- _OBJC_CLASS_$_CCAppGlobalMediaMusicArtistNameContent
- _OBJC_CLASS_$_CCAppGlobalMediaMusicArtistNameMetaContent
- _OBJC_CLASS_$_CCAppGlobalMediaPlaylistTitleContent
- _OBJC_CLASS_$_CCAppGlobalMediaPlaylistTitleMetaContent
- _OBJC_CLASS_$_CCAppGlobalMediaShowTitleContent
- _OBJC_CLASS_$_CCAppGlobalMediaShowTitleMetaContent
- _OBJC_CLASS_$_CCAppIntentsIndexedEntityMetaContent
- _OBJC_CLASS_$_CCAppIntentsIndexedEnumContent
- _OBJC_CLASS_$_CCAppIntentsIndexedEnumMetaContent
- _OBJC_CLASS_$_CCAppShortcutEntityContent
- _OBJC_CLASS_$_CCAppShortcutEntityMetaContent
- _OBJC_CLASS_$_CCAppShortcutPhraseContent
- _OBJC_CLASS_$_CCAppShortcutPhraseMetaContent
- _OBJC_CLASS_$_CCAssistantSchema
- _OBJC_CLASS_$_CCAssistantSchemaVersion
- _OBJC_CLASS_$_CCCalendarEventContent
- _OBJC_CLASS_$_CCCalendarEventMetaContent
- _OBJC_CLASS_$_CCContactContent
- _OBJC_CLASS_$_CCContactEmailAddress
- _OBJC_CLASS_$_CCContactInstantMessageAddress
- _OBJC_CLASS_$_CCContactMetaContent
- _OBJC_CLASS_$_CCContactPhoneNumber
- _OBJC_CLASS_$_CCContactPostalAddress
- _OBJC_CLASS_$_CCContactRelation
- _OBJC_CLASS_$_CCContactSocialProfile
- _OBJC_CLASS_$_CCContactURLAddress
- _OBJC_CLASS_$_CCFindMyDeviceContent
- _OBJC_CLASS_$_CCFindMyDeviceMetaContent
- _OBJC_CLASS_$_CCFindMyDeviceOwner
- _OBJC_CLASS_$_CCFitnessGuestContent
- _OBJC_CLASS_$_CCFitnessGuestMetaContent
- _OBJC_CLASS_$_CCHealthMedicationContent
- _OBJC_CLASS_$_CCHealthMedicationMetaContent
- _OBJC_CLASS_$_CCHome
- _OBJC_CLASS_$_CCHomeAccessory
- _OBJC_CLASS_$_CCHomeContent
- _OBJC_CLASS_$_CCHomeMetaContent
- _OBJC_CLASS_$_CCHomeRoom
- _OBJC_CLASS_$_CCHomeScene
- _OBJC_CLASS_$_CCHomeService
- _OBJC_CLASS_$_CCHomeServiceArea
- _OBJC_CLASS_$_CCHomeServiceAreaContent
- _OBJC_CLASS_$_CCHomeServiceAreaMap
- _OBJC_CLASS_$_CCHomeServiceAreaMetaContent
- _OBJC_CLASS_$_CCHomeServiceGroup
- _OBJC_CLASS_$_CCHomeTrigger
- _OBJC_CLASS_$_CCHomeZone
- _OBJC_CLASS_$_CCInstalledAppContent
- _OBJC_CLASS_$_CCInstalledAppMetaContent
- _OBJC_CLASS_$_CCMediaAlbum
- _OBJC_CLASS_$_CCMediaAlbumArtist
- _OBJC_CLASS_$_CCMediaAudiobook
- _OBJC_CLASS_$_CCMediaAudiobookArtist
- _OBJC_CLASS_$_CCMediaGenre
- _OBJC_CLASS_$_CCMediaLinkedIdentifier
- _OBJC_CLASS_$_CCMediaMetaContent
- _OBJC_CLASS_$_CCMediaMovie
- _OBJC_CLASS_$_CCMediaMusicVideo
- _OBJC_CLASS_$_CCMediaPlaylist
- _OBJC_CLASS_$_CCMediaSong
- _OBJC_CLASS_$_CCMediaSongArtist
- _OBJC_CLASS_$_CCMediaTVEpisode
- _OBJC_CLASS_$_CCMediaTVShow
- _OBJC_CLASS_$_CCPodcastContent
- _OBJC_CLASS_$_CCPodcastMetaContent
- _OBJC_CLASS_$_CCPodcastPlaylist
- _OBJC_CLASS_$_CCPodcastShow
- _OBJC_CLASS_$_CCRadioStationContent
- _OBJC_CLASS_$_CCRadioStationMetaContent
- _OBJC_CLASS_$_CCSerializedSet
- _OBJC_CLASS_$_CCSignificantLocationAddress
- _OBJC_CLASS_$_CCSignificantLocationContent
- _OBJC_CLASS_$_CCSignificantLocationMetaContent
- _OBJC_CLASS_$_CCSiriLearnedContactContent
- _OBJC_CLASS_$_CCSiriLearnedContactMetaContent
- _OBJC_CLASS_$_CCSiriLearnedMediaContent
- _OBJC_CLASS_$_CCSiriLearnedMediaMetaContent
- _OBJC_CLASS_$_CCUserAccountIdentityContent
- _OBJC_CLASS_$_CCUserAccountIdentityMetaContent
- _OBJC_CLASS_$_CESRSpeechProfileTestData
- _OBJC_METACLASS_$_CESRSpeechProfileTestData
- _PROTOCOLS_CoreEmbeddedSpeechAnalyzer.831
- __96-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:]_block_invoke.380
- __Block_byref_object_copy_.1070
- __Block_byref_object_copy_.1481
- __Block_byref_object_copy_.3105
- __Block_byref_object_copy_.4431
- __Block_byref_object_copy_.957
- __Block_byref_object_dispose_.1071
- __Block_byref_object_dispose_.1482
- __Block_byref_object_dispose_.3106
- __Block_byref_object_dispose_.4432
- __Block_byref_object_dispose_.958
- __OBJC_$_CLASS_METHODS_CESRSpeechProfileTestData
- __OBJC_CLASS_RO_$_CESRSpeechProfileTestData
- __OBJC_METACLASS_RO_$_CESRSpeechProfileTestData
- ___96-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:]_block_invoke
- __block_literal_global.1952
- __block_literal_global.3181
- __block_literal_global.3831
- __block_literal_global.4171
- __block_literal_global.429
- __block_literal_global.4468
- __block_literal_global.764
- __block_literal_global.776
- _objc_msgSend$AppCustomCarName_1
- _objc_msgSend$AppCustomCarProfileName_1
- _objc_msgSend$AppCustomContactGroupName_1
- _objc_msgSend$AppCustomContactName_1
- _objc_msgSend$AppCustomMediaAudiobookAuthorName_1
- _objc_msgSend$AppCustomMediaAudiobookTitle_1
- _objc_msgSend$AppCustomMediaMusicArtistName_1
- _objc_msgSend$AppCustomMediaPlaylistTitle_1
- _objc_msgSend$AppCustomMediaShowTitle_1
- _objc_msgSend$AppCustomNotebookItemGroupName_1
- _objc_msgSend$AppCustomNotebookItemTitle_1
- _objc_msgSend$AppCustomPaymentsAccountNickname_1
- _objc_msgSend$AppCustomPaymentsOrganizationName_1
- _objc_msgSend$AppCustomPhotoAlbumName_1
- _objc_msgSend$AppCustomPhotoTag_1
- _objc_msgSend$AppCustomVoiceCommandName_1
- _objc_msgSend$AppCustomWorkoutActivityName_1
- _objc_msgSend$AppGlobalMediaAudiobookAuthor_1
- _objc_msgSend$AppGlobalMediaAudiobookTitle_1
- _objc_msgSend$AppGlobalMediaMusicArtistName_1
- _objc_msgSend$AppGlobalMediaPlaylistTitle_1
- _objc_msgSend$AppGlobalMediaShowTitle_1
- _objc_msgSend$AppIntentsIndexedEntity_1
- _objc_msgSend$AppIntentsIndexedEnum_1
- _objc_msgSend$AppShortcutEntity_1
- _objc_msgSend$AppShortcutPhrase_1
- _objc_msgSend$CalendarEvent_1
- _objc_msgSend$Contact_1
- _objc_msgSend$Contact_2
- _objc_msgSend$Contact_3
- _objc_msgSend$Contact_givenName:familyName:sourceItemIdentifier:
- _objc_msgSend$FindMyDevice_1
- _objc_msgSend$FitnessGuest_1
- _objc_msgSend$HealthMedication_1
- _objc_msgSend$Home_1
- _objc_msgSend$Home_2
- _objc_msgSend$InstalledApp_1
- _objc_msgSend$InstalledApp_2
- _objc_msgSend$InstalledApp_3
- _objc_msgSend$Media_1
- _objc_msgSend$Podcast_1
- _objc_msgSend$RadioStation_1
- _objc_msgSend$SignificantLocation_1
- _objc_msgSend$SiriLearnedContact_1
- _objc_msgSend$SiriLearnedMedia_1
- _objc_msgSend$UserAccountIdentity_1
- _objc_msgSend$_assistantLocale
- _objc_msgSend$_dictationLocales
- _objc_msgSend$_setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:
- _objc_msgSend$initWithBundleIdentifier:bundleName:displayAppName:spokenName:alternativeAppNames:carPlayAlternativeDisplayName:spotlightName:providerName:error:
- _objc_msgSend$initWithCaseIdentifier:displayRepresentation:error:
- _objc_msgSend$initWithContent:metaContent:error:
- _objc_msgSend$initWithDirectory:locale:userId:dataProtectionClass:
- _objc_msgSend$initWithEntity:entityType:error:
- _objc_msgSend$initWithEntityTitle:entityInstanceIdentifier:entityTypeIdentifier:providerClass:entitySynonyms:error:
- _objc_msgSend$initWithFirstName:lastName:error:
- _objc_msgSend$initWithGivenName:middleName:familyName:previousFamilyName:nickname:namePrefix:nameSuffix:phoneNumbers:emailAddresses:postalAddresses:urlAddresses:socialProfiles:instantMessageAddresses:relations:organizationName:departmentName:jobTitle:phoneticGivenName:phoneticMiddleName:phoneticFamilyName:phoneticOrganizationName:note:birthday:nonGregorianBirthday:dates:error:
- _objc_msgSend$initWithItemType:descriptors:localInstances:error:
- _objc_msgSend$initWithLabel:email:error:
- _objc_msgSend$initWithLabel:name:error:
- _objc_msgSend$initWithLabel:street:subLocality:city:subAdministrativeArea:state:postalCode:country:ISOCountryCode:error:
- _objc_msgSend$initWithLabel:stringValue:error:
- _objc_msgSend$initWithLabel:url:error:
- _objc_msgSend$initWithLabel:urlString:username:userIdentifier:serviceName:error:
- _objc_msgSend$initWithLabel:username:serviceName:error:
- _objc_msgSend$initWithMajor:minor:patch:error:
- _objc_msgSend$initWithMatterDeviceIdentifier:serviceArea:serviceAreaType:error:
- _objc_msgSend$initWithName:areaIdentifier:associatedMapIdentifier:error:
- _objc_msgSend$initWithName:author:error:
- _objc_msgSend$initWithName:callSign:frequency:channel:signalType:error:
- _objc_msgSend$initWithName:deviceType:error:
- _objc_msgSend$initWithName:error:
- _objc_msgSend$initWithName:mapIdentifier:error:
- _objc_msgSend$initWithName:nickname:error:
- _objc_msgSend$initWithName:owner:error:
- _objc_msgSend$initWithName:synonyms:error:
- _objc_msgSend$initWithPhrase:baseTemplate:templateParameterValue:error:
- _objc_msgSend$initWithPreferredName:mapItemName:address:error:
- _objc_msgSend$initWithSourceItemIdentifier:assistantHomeKitIdentifier:error:
- _objc_msgSend$initWithSourceItemIdentifier:bundleVersion:error:
- _objc_msgSend$initWithSourceItemIdentifier:error:
- _objc_msgSend$initWithSourceItemIdentifier:linkedIdentifiers:error:
- _objc_msgSend$initWithSourceItemIdentifier:saliency:error:
- _objc_msgSend$initWithSourceItemIdentifier:type:error:
- _objc_msgSend$initWithThoroughfare:subLocality:locality:country:error:
- _objc_msgSend$initWithTitle:locationName:error:
- _objc_msgSend$initWithTitle:subtitle:synonyms:error:
- _objc_msgSend$initWithType:version:error:
- _objc_msgSend$initWithTypeIdentifier:displayRepresentation:typeDisplayRepresentation:assistantDefinedSchemas:error:
- _objc_msgSend$initWithTypeIdentifier:displayRepresentation:typeDisplayRepresentation:error:
- _objc_msgSend$initWithTypeIdentifier:typeDisplayRepresentation:cases:error:
- _objc_msgSend$initWithUserName:givenName:error:
- _objc_msgSend$initWithUserPhrasedName:suggestedContactId:error:
- _objc_msgSend$initWithUserPhrasedSongName:userPhrasedArtistName:userPhrasedAlbumName:userPhrasedEntityName:userPhrasedVersion:suggestedAdamId:error:
- _objc_msgSend$initWithVocabularyString:vocabularyIdentifier:error:
- _objc_msgSend$initWithVocabularyStrings:error:
- _objc_msgSend$isSiriUODwithASROnServerSupported
- _objc_msgSend$refreshLocales
- _objc_msgSend$refreshLocalesIfNeeded
- _objc_msgSend$setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:completion:
- sharedManager.onceToken.3180
- sharedManager.onceToken.763
- sharedManager.sharedMyManager.3182
- sharedManager.sharedMyManager.765
CStrings:
+ "\x14"
+ "%s Dictation is disabled in Settings."
+ "%s Failed to parse Entity Cleanup config."
+ "%s Failed to parse Entity Cleanup section of json."
+ "%s Offline Dictation is not supported."
+ "%s Refreshing required locales as needed..."
+ "%s Siri UOD is not supported."
+ "%s Siri UOD with ASR on server is supported."
+ "%s Siri is disabled in Settings."
+ "-[CESREntityCleanupConfig initWithJsonObject:]"
+ "-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke"
+ "-[CESRSpeechProfileSettings _isAssistantRequired]"
+ "-[CESRSpeechProfileSettings _isDictationRequired]"
+ "-[CESRSpeechProfileSettings refreshRequiredLocales:]"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CESRPhoneticEmbedder.h"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CoreEmbeddedSpeechAnalyzer.h"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CoreEmbeddedSpeechAnalyzer.swift"
+ "@\"CESREntityCleanupConfig\""
+ "@60@0:8@16@24@32@40q48B56"
+ "Already processing visual context, skipping"
+ "B20@0:8B16"
+ "B60@0:8@16@24@32@40q48B56"
+ "CESREntityCleanupConfig"
+ "CESREntityCleanupConfig: _enableDatatypeCleanupFromNonAppEntities=%@ enableEmojiCleanupFromAppEntities=%@ enableEmojiCleanupFromNonAppEntities=%@ enableSpecialCharacterCleanupFromAppEntities=%@ enableSpecialCharacterCleanupFromNonAppEntities=%@ keepEmojis=%@ keepSpecialCharacters=%@ applyRegex=%@ specialCharactersToRemove=%@"
+ "Cached evaluation record with interactionId: %s"
+ "T@\"CESREntityCleanupConfig\",R,N,V_entityCleanupConfig"
+ "T@\"NSDictionary\",R,N,V_applyRegex"
+ "T@\"NSDictionary\",R,N,V_keepEmojis"
+ "T@\"NSDictionary\",R,N,V_keepSpecialCharacters"
+ "T@\"NSSet\",R,N,V_specialCharactersToRemove"
+ "TB,R,N,V_enableDatatypeCleanupFromNonAppEntities"
+ "TB,R,N,V_enableEmojiCleanupFromAppEntities"
+ "TB,R,N,V_enableEmojiCleanupFromNonAppEntities"
+ "TB,R,N,V_enableSpecialCharacterCleanupFromAppEntities"
+ "TB,R,N,V_enableSpecialCharacterCleanupFromNonAppEntities"
+ "Vv68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48B56@?<v@?B@\"NSError\">60"
+ "Vv68@0:8@16@24@32@40q48B56@?60"
+ "Writing record with interactionId: %s"
+ "_applyRegex"
+ "_enableDatatypeCleanupFromNonAppEntities"
+ "_enableEmojiCleanupFromAppEntities"
+ "_enableEmojiCleanupFromNonAppEntities"
+ "_enableSpecialCharacterCleanupFromAppEntities"
+ "_enableSpecialCharacterCleanupFromNonAppEntities"
+ "_entityCleanupConfig"
+ "_isAssistantRequired"
+ "_isDictationRequired"
+ "_keepEmojis"
+ "_keepSpecialCharacters"
+ "_setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:"
+ "_specialCharactersToRemove"
+ "applyRegex"
+ "enableDatatypeCleanupFromNonAppEntities"
+ "enableEmojiCleanupFromAppEntities"
+ "enableEmojiCleanupFromNonAppEntities"
+ "enableSpecialCharacterCleanupFromAppEntities"
+ "enableSpecialCharacterCleanupFromNonAppEntities"
+ "entityCleanup"
+ "entityCleanupConfig"
+ "initWithDirectory:locale:userId:personaId:dataProtectionClass:isInUserVault:"
+ "isSiriUODWithASROnServerSupported"
+ "keepEmojis"
+ "keepSpecialCharacters"
+ "refreshRequiredLocales:"
+ "setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:completion:"
+ "specialCharactersToRemove"
- "\x13"
- "%s Dictation disabled in settings"
- "%s No case defined for itemType: %@"
- "%s Offline dictation not supported"
- "%s Refreshing locales if needed."
- "%s Refreshing locales."
- "%s Siri Assistant disabled in settings"
- "%s Siri UOD Not supported"
- "%s Siri UOD with ASR on Server supported"
- "(HN)"
- "+[CESRSpeechProfileTestData itemInstanceForItemType:]"
- "-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:]_block_invoke"
- "-[CESRSpeechProfileSettings _assistantLocale]"
- "-[CESRSpeechProfileSettings _dictationLocales]"
- "-[CESRSpeechProfileSettings refreshLocalesIfNeeded]"
- "-[CESRSpeechProfileSettings refreshLocales]"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CESRPhoneticEmbedder.h"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CoreEmbeddedSpeechAnalyzer.h"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreSpeech/CoreEmbeddedSpeechRecognition/CoreEmbeddedSpeechAnalyzer.swift"
- "0000accb-09cc-264b-991a-5545c5ab5fe5"
- "0324accb-09cc-264b-991a-5545c5ab5fe5"
- "03838475y30"
- "0384r7334948"
- "0f69c466-1ce8-4ad0-aff2-e8f572994a3a"
- "1"
- "1.0.1"
- "1.23.23"
- "10"
- "100"
- "1000"
- "10022c4-00c2-e5f6-991a-80a72382226"
- "101#sampleIntentSlot"
- "1054"
- "1055"
- "1056"
- "1057"
- "1058"
- "1059"
- "1060"
- "1061"
- "11"
- "12.3.4.5"
- "123"
- "123#sampleIntentSlot"
- "1234"
- "12345"
- "1324accb-09cc-264b-991a-5545c5ab5fe5"
- "1500"
- "1600 Pennsylvania Ave."
- "17BA6D2D-AD53-4130-A5F0-3FBC5F79AB37"
- "2"
- "2.4.2"
- "202#sampleIntentSlot"
- "2068f727-c4a6-468b-991a-80a209b32226"
- "2068f727-c4a6-468b-991a-80a209b32227"
- "23412323#98234"
- "3"
- "34.2.1"
- "4"
- "4000accb-09cc-264b-991a-5545c5ab5fe5"
- "4000accb-09cc-264b-991a-5545c5ab5fe6"
- "4000accb-09cc-264b-991a-5545c5ab5fe7"
- "420.69"
- "456#sampleIntentSlot"
- "4815162342"
- "4ed"
- "5"
- "5551234567"
- "5556479283"
- "5556479443"
- "6"
- "60022c4-00c2-e5f6-991a-80a72382226"
- "678"
- "6a65b2c4-00c2-e5f6-991a-80a209b32226"
- "6a65b2c4-00c2-e5f6-ff45-179ad53c6def"
- "7"
- "7000accb-09cc-264b-991a-5545c5ab5fe5"
- "789#sampleIntentSlot"
- "7a6d500a-7bbf-4d89-80ac-799f4927d000"
- "8"
- "8068f727-c4a6-468b-991a-80a209b32226"
- "9"
- "9000accb-09cc-264b-991a-5545c5ab5fe5"
- "90s Rock"
- "92973"
- "96.5"
- "@20@0:8S16"
- "@36@0:8I16@20@28"
- "@44@0:8@16@24I32@36"
- "@48@0:8@16@24@32q40"
- "@60@0:8@16@24@32@40@48I56"
- "@72@0:8@16@24@32@40@48@56@64"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "@jfk"
- "Album"
- "AlbumEntity"
- "Alejandro"
- "Alice"
- "Alone"
- "An Wen"
- "Anna"
- "Apartment"
- "AppCustomCarName_1"
- "AppCustomCarProfileName_1"
- "AppCustomContactGroupName_1"
- "AppCustomContactGroupName_vocabularyString:vocabularyIdentifier:sourceItemIdentifier:"
- "AppCustomContactName_1"
- "AppCustomContactName_vocabularyString:vocabularyIdentifier:sourceItemIdentifier:"
- "AppCustomMediaAudiobookAuthorName_1"
- "AppCustomMediaAudiobookTitle_1"
- "AppCustomMediaMusicArtistName_1"
- "AppCustomMediaPlaylistTitle_1"
- "AppCustomMediaShowTitle_1"
- "AppCustomNotebookItemGroupName_1"
- "AppCustomNotebookItemTitle_1"
- "AppCustomPaymentsAccountNickname_1"
- "AppCustomPaymentsOrganizationName_1"
- "AppCustomPhotoAlbumName_1"
- "AppCustomPhotoTag_1"
- "AppCustomVoiceCommandName_1"
- "AppCustomWorkoutActivityName_1"
- "AppGlobalMediaAudiobookAuthor_1"
- "AppGlobalMediaAudiobookTitle_1"
- "AppGlobalMediaMusicArtistName_1"
- "AppGlobalMediaPlaylistTitle_1"
- "AppGlobalMediaShowTitle_1"
- "AppIntentsIndexedEntity_1"
- "AppIntentsIndexedEntity_2"
- "AppIntentsIndexedEntity_3"
- "AppIntentsIndexedEntity_4"
- "AppIntentsIndexedEntity_5"
- "AppIntentsIndexedEntity_6"
- "AppIntentsIndexedEntity_7"
- "AppIntentsIndexedEntity_emptyDisplayRepresentation"
- "AppIntentsIndexedEnum_1"
- "AppShortcutEntity_1"
- "AppShortcutPhrase_1"
- "AppShortcutPhrase_2"
- "AppShortcutPhrase_3"
- "Apple King"
- "Around the house"
- "Art Thompson"
- "Auto"
- "B48@0:8@16@24@32q40"
- "BMW iX xDrive50"
- "Backyard Lights"
- "Bakery"
- "Bank"
- "BaseTemplate"
- "Best Electronic Alternative"
- "Best Vacation Ever"
- "Bob"
- "Bobby"
- "Boston Red Sox"
- "Breakfast"
- "Bring the action"
- "Brother"
- "Browser Tab Header"
- "BrowserEntity"
- "By 10/20/26"
- "CESRSpeechProfileTestData"
- "CalendarEvent_1"
- "Car"
- "Carter"
- "CascadeSerializedSets_1"
- "Castle"
- "Cat"
- "Catherine"
- "Cheesesteak Shop"
- "Chevrolet"
- "Chevy Pickup"
- "Chevy Truck"
- "Chillax"
- "Church"
- "Classic 80's"
- "Coffee Shop"
- "Coffee Stop"
- "Contact_1"
- "Contact_10"
- "Contact_11"
- "Contact_12"
- "Contact_13"
- "Contact_14"
- "Contact_15"
- "Contact_16"
- "Contact_17"
- "Contact_18"
- "Contact_19"
- "Contact_2"
- "Contact_20"
- "Contact_21"
- "Contact_22"
- "Contact_23"
- "Contact_24"
- "Contact_25"
- "Contact_26"
- "Contact_27"
- "Contact_28"
- "Contact_29"
- "Contact_3"
- "Contact_30"
- "Contact_31"
- "Contact_32"
- "Contact_33"
- "Contact_34"
- "Contact_35"
- "Contact_36"
- "Contact_4"
- "Contact_5"
- "Contact_6"
- "Contact_7"
- "Contact_8"
- "Contact_9"
- "Contact_givenName:familyName:sourceItemIdentifier:"
- "Costanza"
- "Cox"
- "Cupertino"
- "Dan Harris"
- "Dan Peter"
- "Davis Bowie"
- "Deli"
- "Discrete Envelope"
- "Dodge Ram"
- "Downstairs"
- "Drew Tangerine"
- "Dwayne"
- "Empty"
- "EmptyEntity"
- "Eric Tyson, MBA"
- "Estelle"
- "F"
- "Faouzia"
- "Ferrari Profile"
- "Fidelity"
- "FindMyDevice_1"
- "FindMyDevice_2"
- "FitnessGuest_1"
- "For everything, all the time, just not for website URLs"
- "Friend"
- "GenericMediaEntity"
- "GeoPOIRestaurant"
- "George"
- "Gym"
- "HIT"
- "Hacker News"
- "Haley"
- "Harris"
- "Hayleigh"
- "HealthMedication_1"
- "Heroes"
- "Home"
- "Home_1"
- "Home_2"
- "Home_3"
- "Home_withType:name:sourceItemIdentifier:"
- "IV"
- "InstalledApp_1"
- "InstalledApp_2"
- "InstalledApp_3"
- "InstalledApp_4"
- "InstalledApp_displayAppName:"
- "Investing for Dummies"
- "Investments"
- "Italian Deli"
- "Italian Foods"
- "J.R.R. Tolkien"
- "Jack FM"
- "Jack XM"
- "James"
- "James Blunt"
- "Jennifer Strong"
- "John"
- "John F Kennedy"
- "John's Mom"
- "Johnny"
- "Johnson"
- "KJAQ"
- "Kaskade"
- "Kennedy"
- "Kiro Radio"
- "Kitchen"
- "Knight"
- "Kox"
- "Lake Tahoe"
- "Leduc"
- "Live version of Hero"
- "Lost"
- "Lynyrd Skynyrd"
- "Main"
- "Maps"
- "Media Title"
- "Media_1"
- "Media_2"
- "Media_3"
- "Media_4"
- "Media_5"
- "Media_6"
- "Media_7"
- "Media_8"
- "Media_withType:name:sourceItemIdentifier:"
- "Mehmet"
- "Mobile"
- "Molly Fox"
- "Mom"
- "Mother"
- "Mr."
- "My AirPods"
- "My iPhone"
- "MyProvider"
- "New York Yankees"
- "Note Title"
- "NoteEntity"
- "Operations"
- "Patrick Tyrone"
- "Paul Glenn Matthew George II"
- "Podcast_1"
- "Podcast_2"
- "Portfolio"
- "President"
- "Private Chat"
- "Pronounced'Leh-'Nerd'Skin-'Nerd,"
- "RadioStation_1"
- "RadioStation_2"
- "RadioStation_3"
- "Ram"
- "Ram Pickup"
- "Reminder Title"
- "ReminderEntity"
- "Restaurant"
- "Richard Lewis"
- "Road Trip"
- "Rose"
- "Round Table"
- "S N U G"
- "S&S"
- "SCV"
- "School"
- "Season 8"
- "SignificantLocation_1"
- "Silverado"
- "Simple Man"
- "Sir"
- "SiriLearnedContact_1"
- "SiriLearnedMedia_1"
- "SiriLearnedMedia_2"
- "SiriLearnedMedia_3"
- "SiriLearnedMedia_4"
- "SiriLearnedMedia_5"
- "SiriLearnedMedia_6"
- "SiriLearnedMedia_7"
- "SiriLearnedMedia_8"
- "Ski Buddies"
- "Slack"
- "Starbs"
- "Starbucks"
- "Starbucks Coffee"
- "Stevens Creek Blvd"
- "Summit House"
- "T"
- "Tacoliccio's"
- "Tame Impala"
- "Tang"
- "Tears of Gold"
- "Ten Percent Happier"
- "The Brave"
- "The Hobbit"
- "The Rock"
- "Tip"
- "TipEntity"
- "Trip"
- "Two Union Square, 601 Union St #4400, Seattle, WA 98101"
- "U2tpIFdlYXRoZXIQzUtODBFOS02MTM1OTgzMUY5MEE"
- "USA"
- "United States"
- "Use Dictation!!!!"
- "UserAccountIdentity_1"
- "UserCar"
- "Vegas Delights"
- "Vehicle"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@?<v@?B@\"NSError\">48"
- "Vv56@0:8@16@24@32q40@?48"
- "Weekend List"
- "Where's my bus"
- "White House"
- "Williams Jr"
- "Winchester"
- "X-HM://id=2bcf29c7-6118-4ec2-98fb-2f49e1894d88"
- "X-HM://id=774DB160-4F9C-4D17-8F5A-222A279E4E0D"
- "X-HM://id=8EADA8FB-93EF-481B-A0CE-8FA7EFD64A4D"
- "Zen Podcasts"
- "_setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:"
- "a5ea540d-8fa1-4ede-8471-a3e566da83b8"
- "a923nfashfiqu36"
- "bob"
- "bobby"
- "car-manager-1"
- "cash app"
- "ce16238a-007d-4394-b622-f61d640d88b4"
- "coffee time"
- "com.apple.Maps"
- "com.example.app"
- "content-1"
- "e7b2480e-9b7c-4b16-b578-34bc8bc16706"
- "entity-1"
- "enum-1"
- "fb"
- "fb0b9750-1f57-46a4-b46b-b0646fba49a3"
- "ff78262a-c4a6-0000-991a-80a209b32999"
- "ffffeeee-00c2-e5f6-ff45-179ad53c6def"
- "happy gummies"
- "initWithBundleIdentifier:bundleName:displayAppName:spokenName:alternativeAppNames:carPlayAlternativeDisplayName:spotlightName:providerName:error:"
- "initWithCaseIdentifier:displayRepresentation:error:"
- "initWithContent:metaContent:error:"
- "initWithDirectory:locale:userId:dataProtectionClass:"
- "initWithEntity:entityType:error:"
- "initWithEntityTitle:entityInstanceIdentifier:entityTypeIdentifier:providerClass:entitySynonyms:error:"
- "initWithFirstName:lastName:error:"
- "initWithGivenName:middleName:familyName:previousFamilyName:nickname:namePrefix:nameSuffix:phoneNumbers:emailAddresses:postalAddresses:urlAddresses:socialProfiles:instantMessageAddresses:relations:organizationName:departmentName:jobTitle:phoneticGivenName:phoneticMiddleName:phoneticFamilyName:phoneticOrganizationName:note:birthday:nonGregorianBirthday:dates:error:"
- "initWithItemType:descriptors:localInstances:error:"
- "initWithLabel:email:error:"
- "initWithLabel:name:error:"
- "initWithLabel:street:subLocality:city:subAdministrativeArea:state:postalCode:country:ISOCountryCode:error:"
- "initWithLabel:stringValue:error:"
- "initWithLabel:url:error:"
- "initWithLabel:urlString:username:userIdentifier:serviceName:error:"
- "initWithLabel:username:serviceName:error:"
- "initWithMajor:minor:patch:error:"
- "initWithMatterDeviceIdentifier:serviceArea:serviceAreaType:error:"
- "initWithName:areaIdentifier:associatedMapIdentifier:error:"
- "initWithName:author:error:"
- "initWithName:callSign:frequency:channel:signalType:error:"
- "initWithName:deviceType:error:"
- "initWithName:error:"
- "initWithName:mapIdentifier:error:"
- "initWithName:nickname:error:"
- "initWithName:owner:error:"
- "initWithName:synonyms:error:"
- "initWithPhrase:baseTemplate:templateParameterValue:error:"
- "initWithPreferredName:mapItemName:address:error:"
- "initWithSourceItemIdentifier:assistantHomeKitIdentifier:error:"
- "initWithSourceItemIdentifier:bundleVersion:error:"
- "initWithSourceItemIdentifier:error:"
- "initWithSourceItemIdentifier:linkedIdentifiers:error:"
- "initWithSourceItemIdentifier:saliency:error:"
- "initWithSourceItemIdentifier:type:error:"
- "initWithThoroughfare:subLocality:locality:country:error:"
- "initWithTitle:locationName:error:"
- "initWithTitle:subtitle:synonyms:error:"
- "initWithType:version:error:"
- "initWithTypeIdentifier:displayRepresentation:typeDisplayRepresentation:assistantDefinedSchemas:error:"
- "initWithTypeIdentifier:displayRepresentation:typeDisplayRepresentation:error:"
- "initWithTypeIdentifier:typeDisplayRepresentation:cases:error:"
- "initWithUserName:givenName:error:"
- "initWithUserPhrasedName:suggestedContactId:error:"
- "initWithUserPhrasedSongName:userPhrasedArtistName:userPhrasedAlbumName:userPhrasedEntityName:userPhrasedVersion:suggestedAdamId:error:"
- "initWithVocabularyString:vocabularyIdentifier:error:"
- "initWithVocabularyStrings:error:"
- "isSiriUODwithASROnServerSupported"
- "itemInstanceForItemType:"
- "lexapro"
- "library"
- "live"
- "mail@mail.com"
- "my home"
- "myLinkedIdentifier"
- "notes123"
- "org-123"
- "param"
- "phoneme1"
- "phoneme2"
- "phoneme3"
- "phoneme4"
- "photo manager"
- "photos-123"
- "reddit"
- "refreshLocales"
- "refreshLocalesIfNeeded"
- "sample.app"
- "sample.app.1"
- "sample.app.2"
- "sample.net"
- "sampleItem_AppCustomCarNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomContactGroupNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomContactNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomMediaAudiobookAuthorNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomMediaAudiobookTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomMediaMusicArtistNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomMediaPlaylistTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomMediaShowTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomNotebookItemGroupNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomNotebookItemTitleWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomPaymentsAccountNicknameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomPaymentsOrganizationNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomPhotoAlbumNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomPhotoTagWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomVoiceCommandNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppCustomWorkoutActivityNameWithSourceItemIdentifier:vocabularyString:vocabularyIdentifier:"
- "sampleItem_AppIntentsIndexedEntityWithSourceItemIdentifier:typeIdentifier:title:subtitle:synonyms:typeDisplayName:typeDisplaySynonyms:"
- "sampleItem_AppShortcutPhraseWithSourceItemIdentifier:phrase:baseTemplate:templateParameterValue:"
- "sampleItem_ContactWithSourceItemIdentifier:givenName:middleName:familyName:nickname:organizationName:phoneticGivenName:phoneticMiddleName:phoneticFamilyName:phoneticOrganizationName:"
- "sampleItem_HealthMedicationWithSourceItemIdentifier:name:nickname:"
- "sampleItem_HomeAccessoryWithSourceItemIdentifier:assistantHomeKitIdentifier:deviceType:name:"
- "sampleItem_HomeRoomWithSourceItemIdentifier:assistantHomeKitIdentifier:name:"
- "sampleItem_HomeSceneWithSourceItemIdentifier:assistantHomeKitIdentifier:name:"
- "sampleItem_HomeServiceAreaMapWithSourceItemIdentifier:serviceAreaMapName:"
- "sampleItem_HomeServiceAreaWithSourceItemIdentifier:serviceAreaName:"
- "sampleItem_HomeServiceGroupWithSourceItemIdentifier:assistantHomeKitIdentifier:name:"
- "sampleItem_HomeServiceWithSourceItemIdentifier:assistantHomeKitIdentifier:deviceType:name:"
- "sampleItem_HomeWithSourceItemIdentifier:assistantHomeKitIdentifier:name:"
- "sampleItem_HomeZoneWithSourceItemIdentifier:assistantHomeKitIdentifier:name:"
- "sampleItem_InstalledAppWithSourceItemIdentifier:bundleVersion:bundleIdentifier:bundleName:displayAppName:spokenName:alternativeAppNames:carPlayAlternativeDisplayName:spotlightName:providerName:"
- "sampleItem_MediaAlbumArtistWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaAlbumWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaAudiobookArtistWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaAudiobookWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaPlaylistWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaSongArtistWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_MediaSongWithSourceItemIdentifier:linkedIdentifiers:name:"
- "sampleItem_PodcastPlaylistWithSourceItemIdentifier:name:"
- "sampleItem_PodcastShowWithSourceItemIdentifier:name:author:"
- "sampleItem_RadioStationWithSourceItemIdentifier:name:callSign:frequency:channel:signalType:"
- "sampleItem_UserAccountIdentityWithSourceItemIdentifier:userName:givenName:"
- "setProfileConfigWithLanguage:profileDir:userId:dataProtectionClass:completion:"
- "sirikit-item-1"
- "sirikit-item-10"
- "sirikit-item-11"
- "sirikit-item-12"
- "sirikit-item-13"
- "sirikit-item-14"
- "sirikit-item-15"
- "sirikit-item-16"
- "sirikit-item-17"
- "sirikit-item-2"
- "sirikit-item-3"
- "sirikit-item-4"
- "sirikit-item-5"
- "sirikit-item-6"
- "sirikit-item-7"
- "sirikit-item-8"
- "sirikit-item-9"
- "square cash"
- "test://id=12345678-9012-3456-7890-123456789012"
- "test://id=abcdefab-cdef-abcd-efab-cdefabcdefab"
- "test://id=qwertyui-opas-dfgh-jklz-xcvbnmqwerty"
- "twitter"
- "work"
- "x-fitness-guest://Molly+Fox"
- "x-health-medicationName://lexapro"
- "x-media-library://08F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-media-library://18F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-media-library://28F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-media-library://38F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-media-library://48F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-media-library://58F895E8-DE36-439C-ACA1-B7F734B25344/1/2289062476331755325"
- "x-sampcollection-podcast://device/00D5118F-FFDD-0000-AF25-6BE847222C79"
- "x-sampcollection-podcast://device/98D5808C-0BDD-47A1-AF25-CBE847221B68"
- "xyz-123"

```
