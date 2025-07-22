## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-588.0.0.0.0
-  __TEXT.__text: 0xb1c28
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x8570
-  __TEXT.__const: 0x1c50
-  __TEXT.__cstring: 0x9f08
-  __TEXT.__oslogstring: 0x9a2c
-  __TEXT.__gcc_except_tab: 0x1c88
-  __TEXT.__constg_swiftt: 0x824
-  __TEXT.__swift5_typeref: 0x948
-  __TEXT.__swift5_builtin: 0x64
+591.100.0.0.0
+  __TEXT.__text: 0xb5ee0
+  __TEXT.__auth_stubs: 0x1570
+  __TEXT.__objc_methlist: 0x8770
+  __TEXT.__const: 0x1dd0
+  __TEXT.__cstring: 0xa138
+  __TEXT.__oslogstring: 0x9a9c
+  __TEXT.__gcc_except_tab: 0x1ce0
+  __TEXT.__constg_swiftt: 0x844
+  __TEXT.__swift5_typeref: 0xa52
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x50f
-  __TEXT.__swift5_fieldmd: 0x6cc
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x188
-  __TEXT.__swift5_types: 0x90
+  __TEXT.__swift5_fieldmd: 0x6e8
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__swift5_proto: 0x1a0
+  __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_capture: 0x160
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2ae0
-  __TEXT.__eh_frame: 0xc78
+  __TEXT.__unwind_info: 0x2b98
+  __TEXT.__eh_frame: 0xcf8
   __TEXT.__objc_classname: 0x182a
-  __TEXT.__objc_methname: 0x15c3d
-  __TEXT.__objc_methtype: 0x23cc
-  __TEXT.__objc_stubs: 0xd000
-  __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x1998
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __TEXT.__objc_methname: 0x16331
+  __TEXT.__objc_methtype: 0x2407
+  __TEXT.__objc_stubs: 0xd460
+  __DATA_CONST.__got: 0xb48
+  __DATA_CONST.__const: 0x1a00
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47d8
+  __DATA_CONST.__objc_selrefs: 0x4930
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0xab0
-  __AUTH_CONST.__const: 0x16f0
-  __AUTH_CONST.__cfstring: 0x87a0
-  __AUTH_CONST.__objc_const: 0xfcf8
+  __AUTH_CONST.__auth_got: 0xac8
+  __AUTH_CONST.__const: 0x1718
+  __AUTH_CONST.__cfstring: 0x88c0
+  __AUTH_CONST.__objc_const: 0xff68
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2f48
-  __AUTH.__data: 0x240
-  __DATA.__objc_ivar: 0x5dc
-  __DATA.__data: 0x1a08
-  __DATA.__bss: 0x30b0
+  __AUTH.__objc_data: 0x2fb8
+  __AUTH.__data: 0x260
+  __DATA.__objc_ivar: 0x600
+  __DATA.__data: 0x1aa8
+  __DATA.__bss: 0x33b0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1378
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 43419C4D-8A5A-3DFE-B4E4-58EA3AA1459A
-  Functions: 4304
-  Symbols:   11485
-  CStrings:  6738
+  UUID: ED73D615-FF5B-35CA-AD8F-7B3499285A95
+  Functions: 4396
+  Symbols:   11625
+  CStrings:  6819
 
Symbols:
+ +[STRestrictionsFetcher _invertedRestrictionState:]
+ +[STRestrictionsFetcher _restrictionStateForPayloadNumber:]
+ +[STRestrictionsFetcher _webContentFilterStateForWebFilterState:]
+ +[STRestrictionsFetcher _webFilterStateForWebContentDeclaration:]
+ -[STConversation _shouldAllowContactsOnlyCommunicationForHandles:contactsByHandle:]
+ -[STConversation _shouldAllowGroupsWithOneContactCommunicationForHandles:]
+ -[STConversation _shouldAllowWhitelistedContactsCommunicationForHandles:context:]
+ -[STConversation _shouldAllowWhitelistedContactsCommunicationForHandles:context:].cold.1
+ -[STConversation didFetchManagingGuardianState]
+ -[STConversation initSynchronouslyWithBundleIdentifier:].cold.5
+ -[STConversation managingParentAppleIDs]
+ -[STConversation setDidFetchManagingGuardianState:]
+ -[STConversation setManagingParentAppleIDs:]
+ -[STManagementState managingGuardianAppleIDsForLocalUserWithCompletionHandler:]
+ -[STManagementState managingGuardianAppleIDsForLocalUserWithError:]
+ -[STMutableRestrictions initWithIsEnabled:]
+ -[STMutableRestrictions restrictionsImmutableCopy]
+ -[STMutableRestrictions setAllowExplicitLanguageInSiri:]
+ -[STMutableRestrictions setAllowExplicitMediaContent:]
+ -[STMutableRestrictions setAllowExternalIntelligenceIntegrations:]
+ -[STMutableRestrictions setAllowImageCreation:]
+ -[STMutableRestrictions setAllowMusicProfiles:]
+ -[STMutableRestrictions setAllowWritingTools:]
+ -[STMutableRestrictions setMoviesRating:]
+ -[STRestrictions allowExplicitLanguageInSiri]
+ -[STRestrictions allowExplicitMediaContent]
+ -[STRestrictions allowExternalIntelligenceIntegrations]
+ -[STRestrictions allowImageCreation]
+ -[STRestrictions allowMusicProfiles]
+ -[STRestrictions allowWritingTools]
+ -[STRestrictions hash]
+ -[STRestrictions isEqual:]
+ -[STRestrictions moviesRating]
+ -[STRestrictions restrictionsMutableCopy]
+ GCC_except_table134
+ GCC_except_table44
+ GCC_except_table64
+ _OBJC_CLASS_$_STRestrictionsConverter
+ _OBJC_IVAR_$_STConversation._didFetchManagingGuardianState
+ _OBJC_IVAR_$_STConversation._managingParentAppleIDs
+ _OBJC_IVAR_$_STRestrictions._allowExplicitLanguageInSiri
+ _OBJC_IVAR_$_STRestrictions._allowExplicitMediaContent
+ _OBJC_IVAR_$_STRestrictions._allowExternalIntelligenceIntegrations
+ _OBJC_IVAR_$_STRestrictions._allowImageCreation
+ _OBJC_IVAR_$_STRestrictions._allowMusicProfiles
+ _OBJC_IVAR_$_STRestrictions._allowWritingTools
+ _OBJC_IVAR_$_STRestrictions._moviesRating
+ _OBJC_METACLASS_$_STRestrictionsConverter
+ _STAgePresetKeyAllowExternalIntelligenceIntegrations
+ _STAgePresetKeyAllowWritingTools
+ __CLASS_METHODS_STRestrictionsConverter
+ __DATA_STRestrictionsConverter
+ __INSTANCE_METHODS_STRestrictionsConverter
+ __METACLASS_DATA_STRestrictionsConverter
+ ___67-[STManagementState managingGuardianAppleIDsForLocalUserWithError:]_block_invoke
+ ___67-[STManagementState managingGuardianAppleIDsForLocalUserWithError:]_block_invoke_2
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.84
+ ___74-[STConversation initWithBundleIdentifier:contactStore:completionHandler:]_block_invoke.84.cold.1
+ ___79-[STManagementState managingGuardianAppleIDsForLocalUserWithCompletionHandler:]_block_invoke
+ ___79-[STManagementState managingGuardianAppleIDsForLocalUserWithCompletionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ _associated conformance So14STAgePresetKeyaSHSCSQ
+ _associated conformance So14STAgePresetKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So14STAgePresetKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_invertedRestrictionState:
+ _objc_msgSend$_restrictionStateForPayloadNumber:
+ _objc_msgSend$_shouldAllowContactsOnlyCommunicationForHandles:contactsByHandle:
+ _objc_msgSend$_shouldAllowGroupsWithOneContactCommunicationForHandles:
+ _objc_msgSend$_shouldAllowWhitelistedContactsCommunicationForHandles:context:
+ _objc_msgSend$_webContentFilterStateForWebFilterState:
+ _objc_msgSend$_webFilterStateForWebContentDeclaration:
+ _objc_msgSend$allowExplicitLanguageInSiri
+ _objc_msgSend$allowExplicitMediaContent
+ _objc_msgSend$allowExternalIntelligenceIntegrations
+ _objc_msgSend$allowImageCreation
+ _objc_msgSend$allowMusicProfiles
+ _objc_msgSend$allowWritingTools
+ _objc_msgSend$didFetchManagingGuardianState
+ _objc_msgSend$initWithIsEnabled:
+ _objc_msgSend$managingGuardianAppleIDsForLocalUserWithCompletionHandler:
+ _objc_msgSend$managingGuardianAppleIDsForLocalUserWithError:
+ _objc_msgSend$managingParentAppleIDs
+ _objc_msgSend$moviesRating
+ _objc_msgSend$payloadAllowExplicitContent
+ _objc_msgSend$payloadAllowExternalIntelligenceIntegrations
+ _objc_msgSend$payloadAllowMusicArtistActivity
+ _objc_msgSend$payloadAllowWritingTools
+ _objc_msgSend$payloadForceAssistantProfanityFilter
+ _objc_msgSend$payloadRatingMovies
+ _objc_msgSend$restrictionsMutableCopy
+ _objc_msgSend$setAllowExplicitLanguageInSiri:
+ _objc_msgSend$setAllowExplicitMediaContent:
+ _objc_msgSend$setAllowExternalIntelligenceIntegrations:
+ _objc_msgSend$setAllowImageCreation:
+ _objc_msgSend$setAllowMusicProfiles:
+ _objc_msgSend$setAllowWritingTools:
+ _objc_msgSend$setDidFetchManagingGuardianState:
+ _objc_msgSend$setManagingParentAppleIDs:
+ _objc_msgSend$setMoviesRating:
+ _swift_release_n
+ _symbolic SS3key_yp5valuet
+ _symbolic SS_So8NSNumberCt
+ _symbolic _____ So14STAgePresetKeya
+ _symbolic ______So8NSNumberCSgt So14STAgePresetKeya
+ _symbolic ______So8NSNumberCt So14STAgePresetKeya
+ _symbolic _____ySSSo8NSNumberCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSNumberCtG s23_ContiguousArrayStorageC
+ _symbolic _____y_____So8NSNumberCG s18_DictionaryStorageC So14STAgePresetKeya
+ _symbolic _____y_____So8NSNumberCSgG s18_DictionaryStorageC So14STAgePresetKeya
+ _symbolic _____y______So8NSNumberCSgtG s23_ContiguousArrayStorageC So14STAgePresetKeya
+ _symbolic _____y______So8NSNumberCtG s23_ContiguousArrayStorageC So14STAgePresetKeya
- -[STConversation _shouldWhileLimitedAllowHandles:context:].cold.3
- -[STMutableRestrictions _initWithIsEnabled:]
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_ScreenTimeCore
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_ScreenTimeCore
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_ScreenTimeCore
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_ScreenTimeCore
CStrings:
+ "<%@: %p\nIsEnabled: %d\nAllowInstallingApps: %ld\nAllowDeletingApps: %ld,\nAllowInAppPurchases: %ld,\nAllowMusicVideos: %ld,\nAllowMusicProfiles: %ld,\nTVShowsRating: %@,\nMoviesRating: %@,\nAppsRating: %@,\nAllowExplicitBooks: %ld,\nAllowExplicitMediaContent: %ld,\nWebFilterState: %ld,\nAllowAvatarAndNicknameChanges: %ld>,\nAllowPrivateMessaging: %ld,\nAllowProfilePrivacyChanges: %ld,\nAllowWebContentSearchInSiri: %ld,\nAllowExplicitLanguageInSiri: %ld,\nAllowExternalIntelligenceIntegrations: %ld,\nAllowWritingTools: %ld,\nAllowImageCreation: %ld>\n"
+ "@32@0:8@16q24"
+ "AllowExplicitLanguageInSiri"
+ "AllowExplicitMediaContent"
+ "AllowExternalIntelligenceIntegrations"
+ "AllowImageCreation"
+ "AllowMusicProfiles"
+ "AllowWritingTools"
+ "Failed to fetch managing guardian Apple IDs. Error: %{public}@"
+ "Fetched managing guardian Apple IDs: %{private}@"
+ "MoviesRating"
+ "STRestrictionsConverter"
+ "T@\"NSArray\",&,N,V_managingParentAppleIDs"
+ "TB,V_didFetchManagingGuardianState"
+ "_allowExplicitLanguageInSiri"
+ "_allowExplicitMediaContent"
+ "_allowExternalIntelligenceIntegrations"
+ "_allowImageCreation"
+ "_allowMusicProfiles"
+ "_allowWritingTools"
+ "_didFetchManagingGuardianState"
+ "_invertedRestrictionState:"
+ "_managingParentAppleIDs"
+ "_moviesRating"
+ "_restrictionStateForPayloadNumber:"
+ "_shouldAllowContactsOnlyCommunicationForHandles:contactsByHandle:"
+ "_shouldAllowGroupsWithOneContactCommunicationForHandles:"
+ "_shouldAllowWhitelistedContactsCommunicationForHandles:context:"
+ "_webContentFilterStateForWebFilterState:"
+ "_webFilterStateForWebContentDeclaration:"
+ "allowExplicitLanguageInSiri"
+ "allowExplicitMediaContent"
+ "allowExternalIntelligenceIntegrations"
+ "allowImageCreation"
+ "allowMusicProfiles"
+ "allowWritingTools"
+ "didFetchManagingGuardianState"
+ "exceptionConnectionWithUpdateMonitor:"
+ "imageGenerationRestrictionFromRestrictions:"
+ "initWithIsEnabled:"
+ "managingGuardianAppleIDsForLocalUserWithCompletionHandler:"
+ "managingGuardianAppleIDsForLocalUserWithError:"
+ "managingParentAppleIDs"
+ "moviesRating"
+ "numberByAgePresetKeyExcludingImageGenerationForRestrictions:"
+ "numberByAgePresetKeyForRestrictions:"
+ "payloadAllowExplicitContent"
+ "payloadAllowExternalIntelligenceIntegrations"
+ "payloadAllowMusicArtistActivity"
+ "payloadAllowWritingTools"
+ "payloadForceAssistantProfanityFilter"
+ "payloadRatingMovies"
+ "q24@0:8Q16"
+ "q24@0:8q16"
+ "restrictionsImmutableCopy"
+ "restrictionsMutableCopy"
+ "restrictionsWithIsEnabled:valueByAgePresetKey:"
+ "setAllowExplicitLanguageInSiri:"
+ "setAllowExplicitMediaContent:"
+ "setAllowExternalIntelligenceIntegrations:"
+ "setAllowImageCreation:"
+ "setAllowMusicProfiles:"
+ "setAllowWritingTools:"
+ "setDidFetchManagingGuardianState:"
+ "setManagingParentAppleIDs:"
+ "setMoviesRating:"
+ "system.siri.allowExternalIntelligenceIntegrations"
+ "system.siri.allowWritingTools"
+ "updatedRestrictions:withImageGenerationRestriction:"
+ "updatedRestrictions:withValueByAgePresetKey:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "<%@: %p\nIsEnabled: %d\nAllowInstallingApps: %ld\nAllowDeletingApps: %ld,\nAllowInAppPurchases: %ld,\nAllowMusicVideos: %ld,\nTVShowsRating: %@,\nAppsRating: %@,\nAllowExplicitBooks: %ld,\nWebFilterState: %ld,\nAllowAvatarAndNicknameChanges: %ld>,\nAllowPrivateMessaging: %ld,\nAllowProfilePrivacyChanges: %ld,\nAllowWebContentSearchInSiri: %ld>\n"
- "R"

```
