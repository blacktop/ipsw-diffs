## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.1.14.0.0
-  __TEXT.__text: 0x16ae0c
+820.2.6.0.0
+  __TEXT.__text: 0x16b764
   __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_methlist: 0x122ac
-  __TEXT.__cstring: 0x198c3
-  __TEXT.__const: 0x63d8
-  __TEXT.__gcc_except_tab: 0x1450
-  __TEXT.__oslogstring: 0xda1b
+  __TEXT.__objc_methlist: 0x1235c
+  __TEXT.__cstring: 0x19ae3
+  __TEXT.__const: 0x6548
+  __TEXT.__gcc_except_tab: 0x149c
+  __TEXT.__oslogstring: 0xd9eb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__swift5_typeref: 0x1f2c
+  __TEXT.__swift5_typeref: 0x1f7e
   __TEXT.__swift5_capture: 0x8c0
-  __TEXT.__swift5_fieldmd: 0x16e8
-  __TEXT.__constg_swiftt: 0x1890
-  __TEXT.__swift5_reflstr: 0x10e3
+  __TEXT.__swift5_fieldmd: 0x171c
+  __TEXT.__constg_swiftt: 0x18b4
+  __TEXT.__swift5_reflstr: 0x1113
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_proto: 0x428
-  __TEXT.__swift5_types: 0x1ac
+  __TEXT.__swift5_proto: 0x43c
+  __TEXT.__swift5_types: 0x1b0
   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x6560
+  __TEXT.__unwind_info: 0x65a8
   __TEXT.__eh_frame: 0x5500
-  __TEXT.__objc_classname: 0x1ed2
-  __TEXT.__objc_methname: 0x2701f
-  __TEXT.__objc_methtype: 0x63fc
-  __TEXT.__objc_stubs: 0x14ee0
+  __TEXT.__objc_classname: 0x1ef7
+  __TEXT.__objc_methname: 0x2733b
+  __TEXT.__objc_methtype: 0x641f
+  __TEXT.__objc_stubs: 0x14f80
   __DATA_CONST.__got: 0x10f8
-  __DATA_CONST.__const: 0x6058
+  __DATA_CONST.__const: 0x60d0
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x228
+  __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8528
+  __DATA_CONST.__objc_selrefs: 0x8588
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1498
-  __AUTH_CONST.__const: 0x5930
-  __AUTH_CONST.__cfstring: 0x11420
-  __AUTH_CONST.__objc_const: 0x24b50
+  __AUTH_CONST.__const: 0x59a0
+  __AUTH_CONST.__cfstring: 0x11460
+  __AUTH_CONST.__objc_const: 0x24cc0
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x2ca8
+  __AUTH.__objc_data: 0x2cf8
   __AUTH.__data: 0x1150
-  __DATA.__objc_ivar: 0x103c
-  __DATA.__data: 0x3a50
-  __DATA.__bss: 0x8210
+  __DATA.__objc_ivar: 0x1054
+  __DATA.__data: 0x3b10
+  __DATA.__bss: 0x8490
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x2b78
+  __DATA_DIRTY.__objc_data: 0x2b28
   __DATA_DIRTY.__data: 0x520
-  __DATA_DIRTY.__bss: 0xb78
+  __DATA_DIRTY.__bss: 0xb68
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F2F1DD89-7FDB-3B8B-8696-8155ED8705F5
-  Functions: 10834
-  Symbols:   24654
-  CStrings:  13623
+  UUID: 3EB2B78D-A058-39E3-8CAF-FAC61BDF20CD
+  Functions: 10872
+  Symbols:   24717
+  CStrings:  13664
 
Symbols:
+ -[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]
+ -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:]
+ -[GKAppMetadata isVerifiedForAppleSiliconMac]
+ -[GKAppMetadata runsOnIntel]
+ -[GKAppMetadata sizeOnDeviceInBytes]
+ -[GKCredentialRenewalInfo .cxx_destruct]
+ -[GKCredentialRenewalInfo attemptDate]
+ -[GKCredentialRenewalInfo error]
+ -[GKCredentialRenewalInfo initWithAttemptDate:error:]
+ -[GKCredentialRenewalInfo isExpiredWithTTL:]
+ -[GKLeaderboardInternal scoreFormat]
+ -[GKLeaderboardInternal scoreSingularSuffix]
+ -[GKLeaderboardInternal scoreSuffix]
+ -[GKLeaderboardInternal setScoreFormat:]
+ -[GKLeaderboardInternal setScoreSingularSuffix:]
+ -[GKLeaderboardInternal setScoreSuffix:]
+ -[GKMultiplayerGroupInternal games]
+ -[GKMultiplayerGroupInternal setGames:]
+ -[GKPlayerCredentialController activeRenewalGroup]
+ -[GKPlayerCredentialController lastRenewalAttemptInfo]
+ -[GKPlayerCredentialController setActiveRenewalGroup:]
+ -[GKPlayerCredentialController setLastRenewalAttemptInfo:]
+ _OBJC_CLASS_$_GKCredentialRenewalInfo
+ _OBJC_IVAR_$_GKAppMetadata._isVerifiedForAppleSiliconMac
+ _OBJC_IVAR_$_GKAppMetadata._runsOnIntel
+ _OBJC_IVAR_$_GKAppMetadata._sizeOnDeviceInBytes
+ _OBJC_IVAR_$_GKCredentialRenewalInfo._attemptDate
+ _OBJC_IVAR_$_GKCredentialRenewalInfo._error
+ _OBJC_IVAR_$_GKLeaderboardInternal._scoreFormat
+ _OBJC_IVAR_$_GKLeaderboardInternal._scoreSingularSuffix
+ _OBJC_IVAR_$_GKLeaderboardInternal._scoreSuffix
+ _OBJC_IVAR_$_GKMultiplayerGroupInternal._games
+ _OBJC_IVAR_$_GKPlayerCredentialController._activeRenewalGroup
+ _OBJC_IVAR_$_GKPlayerCredentialController._lastRenewalAttemptInfo
+ _OBJC_METACLASS_$_GKCredentialRenewalInfo
+ __OBJC_$_INSTANCE_METHODS_GKCredentialRenewalInfo
+ __OBJC_$_INSTANCE_VARIABLES_GKCredentialRenewalInfo
+ __OBJC_$_PROP_LIST_GKCredentialRenewalInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PresentInGameBannerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PresentInGameBannerProtocol
+ __OBJC_$_PROTOCOL_REFS_PresentInGameBannerProtocol
+ __OBJC_CLASS_RO_$_GKCredentialRenewalInfo
+ __OBJC_LABEL_PROTOCOL_$_PresentInGameBannerProtocol
+ __OBJC_METACLASS_RO_$_GKCredentialRenewalInfo
+ __OBJC_PROTOCOL_$_PresentInGameBannerProtocol
+ ___36-[GKServiceProxy forwardInvocation:]_block_invoke.481
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.487.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.488
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.781
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.2
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.3
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.4
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.5
+ ___67-[GKServiceProxy replyToDuplicatesForRequest:withInvocation:queue:]_block_invoke.484
+ ___81-[GKPlayerCredentialController renewCredentialForUsername:ttl:completionHandler:]_block_invoke_3
+ ___81-[GKPlayerCredentialController renewCredentialForUsername:ttl:completionHandler:]_block_invoke_4
+ ___89-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]_block_invoke
+ ___89-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]_block_invoke_2
+ ___89-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]_block_invoke_3
+ ___89-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]_block_invoke_3.cold.1
+ ___89-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]_block_invoke_3.cold.2
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e14_v16?0?<v?>8ls32l8s40l8s48l8w64l8s56l8
+ ___block_literal_global.182
+ ___block_literal_global.193
+ ___block_literal_global.292
+ ___block_literal_global.312
+ _associated conformance 20GameCenterFoundation02InA10BannerDataV0E4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLOSHAASQ
+ _associated conformance 20GameCenterFoundation02InA10BannerDataV0E4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 20GameCenterFoundation02InA10BannerDataV0E4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$_gkRenewCredentialForUsername:replyQueue:completionHandler:
+ _objc_msgSend$activeRenewalGroup
+ _objc_msgSend$attemptDate
+ _objc_msgSend$initWithAttemptDate:error:
+ _objc_msgSend$isExpiredWithTTL:
+ _objc_msgSend$lastRenewalAttemptInfo
+ _objc_msgSend$setActiveRenewalGroup:
+ _objc_msgSend$setLastRenewalAttemptInfo:
+ _secureCodedPropertyKeys.onceToken.191
+ _secureCodedPropertyKeys.onceToken.290
+ _secureCodedPropertyKeys.onceToken.310
+ _secureCodedPropertyKeys.sSecureCodedKeys.190
+ _secureCodedPropertyKeys.sSecureCodedKeys.289
+ _secureCodedPropertyKeys.sSecureCodedKeys.309
+ _symbolic SaySSG12challengeIDs_t
+ _symbolic _____ 20GameCenterFoundation02InA10BannerDataV0E4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 20GameCenterFoundation02InD10BannerDataV0H4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 20GameCenterFoundation02InD10BannerDataV0H4TypeO34ChallengesScoreSubmittedCodingKeys33_D3335929E2949014425306FE59C27973LLO
- +[GKGamePolicyApp secureCodedPropertyKeys]
- +[GKGamePolicyApp secureCodedPropertyKeys].cold.1
- -[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]
- -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:]
- -[GKGamePolicyApp .cxx_destruct]
- -[GKGamePolicyApp adamID]
- -[GKGamePolicyApp bundleID]
- -[GKGamePolicyApp initWithBundleID:adamID:isGame:]
- -[GKGamePolicyApp isGame]
- -[GKPlayerCredentialController lastRenewalAttempt]
- -[GKPlayerCredentialController setLastRenewalAttempt:]
- OBJC_IVAR_$_GKDispatchGroup.result
- _OBJC_CLASS_$_GKGamePolicyApp
- _OBJC_IVAR_$_GKGamePolicyApp._adamID
- _OBJC_IVAR_$_GKGamePolicyApp._bundleID
- _OBJC_IVAR_$_GKGamePolicyApp._isGame
- _OBJC_IVAR_$_GKPlayerCredentialController._lastRenewalAttempt
- _OBJC_METACLASS_$_GKGamePolicyApp
- __OBJC_$_CLASS_METHODS_GKGamePolicyApp
- __OBJC_$_INSTANCE_METHODS_GKGamePolicyApp
- __OBJC_$_INSTANCE_VARIABLES_GKGamePolicyApp
- __OBJC_$_PROP_LIST_GKGamePolicyApp
- __OBJC_CLASS_RO_$_GKGamePolicyApp
- __OBJC_METACLASS_RO_$_GKGamePolicyApp
- ___36-[GKServiceProxy forwardInvocation:]_block_invoke.480
- ___42+[GKGamePolicyApp secureCodedPropertyKeys]_block_invoke
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.486
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.486.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.780
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781.cold.2
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781.cold.3
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781.cold.4
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.781.cold.5
- ___67-[GKServiceProxy replyToDuplicatesForRequest:withInvocation:queue:]_block_invoke.483
- ___78-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]_block_invoke
- ___78-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]_block_invoke_2
- ___78-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]_block_invoke_3
- ___78-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]_block_invoke_3.cold.1
- ___78-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]_block_invoke_3.cold.2
- ___block_literal_global.175
- ___block_literal_global.297
- _objc_msgSend$_gkRenewCredentialForUsername:completionHandler:
- _objc_msgSend$lastRenewalAttempt
- _objc_msgSend$setLastRenewalAttempt:
- _secureCodedPropertyKeys.onceToken.170
- _secureCodedPropertyKeys.onceToken.284
- _secureCodedPropertyKeys.onceToken.295
- _secureCodedPropertyKeys.sSecureCodedKeys.169
- _secureCodedPropertyKeys.sSecureCodedKeys.283
- _secureCodedPropertyKeys.sSecureCodedKeys.294
CStrings:
+ "%@ Challenges • Score Submitted"
+ "-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:replyQueue:completionHandler:]"
+ "-[GKPlayerCredentialController renewCredentialForUsername:ttl:completionHandler:]_block_invoke"
+ "@\"GKCredentialRenewalInfo\""
+ "@200@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160@168@176@184@192"
+ "B24@0:8d16"
+ "Challenge Score Submitted"
+ "GKCredentialRenewalInfo"
+ "MULTIPLE_CHALLENGES_SCORE_SUBMITTED_BANNER_TITLE"
+ "PresentInGameBannerProtocol"
+ "Processing account %s."
+ "SINGLE_CHALLENGE_SCORE_SUBMITTED_BANNER_TITLE"
+ "T@\"GKCredentialRenewalInfo\",&,N,V_lastRenewalAttemptInfo"
+ "T@\"GKDispatchGroup\",&,N,V_activeRenewalGroup"
+ "T@\"NSDate\",R,N,V_attemptDate"
+ "T@\"NSError\",R,N,V_error"
+ "T@\"NSNumber\",R,N,V_isVerifiedForAppleSiliconMac"
+ "T@\"NSNumber\",R,N,V_runsOnIntel"
+ "T@\"NSNumber\",R,N,V_sizeOnDeviceInBytes"
+ "T@\"NSString\",C,N,V_scoreFormat"
+ "T@\"NSString\",C,N,V_scoreSingularSuffix"
+ "T@\"NSString\",C,N,V_scoreSuffix"
+ "Telling authkit account is in use using DSID"
+ "Telling authkit account is in use using altDSID"
+ "Title for multiple challenges score submitted banner"
+ "Title for single challenge score submitted banner"
+ "Updating account properties."
+ "Vv32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "_activeRenewalGroup"
+ "_attemptDate"
+ "_gkRenewCredentialForUsername:replyQueue:completionHandler:"
+ "_isVerifiedForAppleSiliconMac"
+ "_lastRenewalAttemptInfo"
+ "_runsOnIntel"
+ "_scoreFormat"
+ "_scoreSingularSuffix"
+ "_scoreSuffix"
+ "_sizeOnDeviceInBytes"
+ "activeRenewalGroup"
+ "attemptDate"
+ "challengesScoreSubmitted"
+ "groupID: %@, number of automatched: %@ participants: %@ playedAt: %@, number of games: %@"
+ "initWithAttemptDate:error:"
+ "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:"
+ "isExpiredWithTTL:"
+ "isVerifiedForAppleSiliconMac"
+ "lastRenewalAttemptInfo"
+ "readGamesFriendsPlayedMatchingBundleIDs:completionHandler:"
+ "runsOnIntel"
+ "scoreFormat"
+ "scoreSingularSuffix"
+ "scoreSuffix"
+ "setActiveRenewalGroup:"
+ "setLastRenewalAttemptInfo:"
+ "setScoreFormat:"
+ "setScoreSingularSuffix:"
+ "setScoreSuffix:"
+ "sizeOnDeviceInBytes"
- "-[ACAccountStore(GameCenter) _gkRenewCredentialForUsername:completionHandler:]"
- "@176@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160@168"
- "All account properties %@"
- "GKGamePolicyApp"
- "Processing account %@ with parameters %s."
- "T@\"NSDate\",&,N,V_lastRenewalAttempt"
- "TB,R,N,V_isGame"
- "Telling authkit account is in use using DSID: %s"
- "Telling authkit account is in use using altDSID: %s"
- "Vv40@0:8@\"NSString\"16d24@?<v@?@\"NSError\">32"
- "Vv40@0:8@16d24@?32"
- "_gkRenewCredentialForUsername:completionHandler:"
- "_isGame"
- "_lastRenewalAttempt"
- "accountProperties"
- "getGamePoliciesForBundleIDs:withCompletion:"
- "groupID: %@, number of automatched: %@ participants: %@ playedAt: %@"
- "initWithBundleID:adamID:isGame:"
- "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:"
- "isGame"
- "lastRenewalAttempt"
- "renewCredentialsForAccountWithUsername:ttl:withCompletion:"
- "setLastRenewalAttempt:"

```
