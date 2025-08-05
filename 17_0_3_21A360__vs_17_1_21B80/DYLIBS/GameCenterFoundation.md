## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-818.0.76.2.2
-  __TEXT.__text: 0x155684
+818.1.10.2.3
+  __TEXT.__text: 0x157fc0
   __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_methlist: 0xe1d8
-  __TEXT.__cstring: 0x2270f
-  __TEXT.__const: 0x34c4
-  __TEXT.__gcc_except_tab: 0xf24
+  __TEXT.__objc_methlist: 0xe240
+  __TEXT.__cstring: 0x229af
+  __TEXT.__const: 0x34b4
+  __TEXT.__gcc_except_tab: 0xf6c
   __TEXT.__oslogstring: 0xe
   __TEXT.__ustring: 0x24c
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__swift5_typeref: 0x16d7
+  __TEXT.__swift5_typeref: 0x1715
   __TEXT.__swift5_capture: 0x654
-  __TEXT.__swift5_fieldmd: 0xe30
+  __TEXT.__swift5_fieldmd: 0xe54
   __TEXT.__constg_swiftt: 0x1018
-  __TEXT.__swift5_reflstr: 0x9e2
+  __TEXT.__swift5_reflstr: 0xa12
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x11c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x6348
-  __TEXT.__eh_frame: 0x4a78
-  __TEXT.__objc_classname: 0x18b4
-  __TEXT.__objc_methname: 0x20e7b
-  __TEXT.__objc_methtype: 0x5500
-  __TEXT.__objc_stubs: 0x13800
+  __TEXT.__unwind_info: 0x6584
+  __TEXT.__eh_frame: 0x4bd0
+  __TEXT.__objc_classname: 0x1842
+  __TEXT.__objc_methname: 0x21005
+  __TEXT.__objc_methtype: 0x5564
+  __TEXT.__objc_stubs: 0x13980
   __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x5a78
-  __DATA_CONST.__objc_classlist: 0x678
+  __DATA_CONST.__const: 0x5b58
+  __DATA_CONST.__objc_classlist: 0x668
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b770
-  __DATA_CONST.__objc_selrefs: 0x70b8
+  __DATA_CONST.__objc_const: 0x1b400
+  __DATA_CONST.__objc_selrefs: 0x7118
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __AUTH_CONST.__cfstring: 0x150c0
-  __AUTH_CONST.__objc_const: 0x6068
-  __AUTH_CONST.__const: 0x4508
+  __AUTH_CONST.__cfstring: 0x152a0
+  __AUTH_CONST.__objc_const: 0x5fd8
+  __AUTH_CONST.__const: 0x4590
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x1138
-  __AUTH.__objc_data: 0x2568
+  __AUTH.__objc_data: 0x24c8
   __AUTH.__data: 0xd60
-  __DATA.__objc_protorefs: 0x120
+  __DATA.__objc_protorefs: 0x110
   __DATA.__objc_classrefs: 0x868
-  __DATA.__objc_superrefs: 0x410
-  __DATA.__objc_ivar: 0xcbc
+  __DATA.__objc_superrefs: 0x418
+  __DATA.__objc_ivar: 0xcc4
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x3ab0
-  __DATA.__bss: 0x6490
+  __DATA.__data: 0x3a00
+  __DATA.__bss: 0x64c0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1f58
   __DATA_DIRTY.__data: 0x188
   __DATA_DIRTY.__common: 0xa0
-  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__bss: 0x3f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B7171C7-538D-300C-BAED-382745910EC0
-  Functions: 9396
-  Symbols:   21007
-  CStrings:  12675
+  UUID: D3498549-9DD7-38E3-B09C-9F8C35B16692
+  Functions: 9451
+  Symbols:   21102
+  CStrings:  12715
 
Symbols:
+ +[GKGameDescriptor stringForPlatform:]
+ +[GKGameDescriptor supportsPlatform:]
+ +[GKLocalPlayerInternal minimalInternalFromSourcePlayer:]
+ -[ACAccount(GameCenter) _gkPlayerInternal].cold.2
+ -[ACAccount(GameCenter) _gkPlayerInternal].cold.3
+ -[GKAnonymousPlayerInternal gamePlayerIDForBundleID:]
+ -[GKAnonymousPlayerInternal teamPlayerIDForBundleID:]
+ -[GKAutomatchPlayerInternal gamePlayerIDForBundleID:]
+ -[GKAutomatchPlayerInternal teamPlayerIDForBundleID:]
+ -[GKGame isGameCenterHostingContainer]
+ -[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:]
+ -[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:].cold.1
+ -[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:].cold.2
+ -[GKPlayer initWithInternalRepresentation:].cold.1
+ -[GKPlayer isArcadeGame]
+ -[GKPlayer nonPersistentScopedID]
+ -[GKPlayerInternal encodeWithCoder:]
+ -[GKPlayerInternal gameBundleID]
+ -[GKPlayerInternal gamePlayerIDForBundleID:]
+ -[GKPlayerInternal initWithSanitizeBeforeEncodingBlock:]
+ -[GKPlayerInternal sanitizeBeforeEncoding]
+ -[GKPlayerInternal sanitize]
+ -[GKPlayerInternal setGameBundleID:gamePlayerID:teamPlayerID:]
+ -[GKPlayerInternal setSanitizeBeforeEncoding:]
+ -[GKPlayerInternal teamPlayerIDForBundleID:]
+ -[GKPreferences easySignInSheetEnabled]
+ -[GKPreferences(Restrictions) isGameCenterDisabled]
+ -[GKRemoteAlertLauncher launchBypassingPreAuthentication:forGame:hostPID:deeplink:launchContext:observer:]
+ -[GKRemoteAlertLauncher launchBypassingPreAuthentication:forGame:hostPID:deeplink:launchContext:observer:].cold.1
+ -[GKSpecialPlayerInternal gamePlayerIDForBundleID:]
+ -[GKSpecialPlayerInternal teamPlayerIDForBundleID:]
+ -[GKTransportContext selectTransportWith:].cold.2
+ -[GKUnauthenticatedPlayerInternal gamePlayerIDForBundleID:]
+ -[GKUnauthenticatedPlayerInternal gamePlayerIDForBundleID:].cold.1
+ -[GKUnauthenticatedPlayerInternal teamPlayerIDForBundleID:]
+ -[GKUnauthenticatedPlayerInternal teamPlayerIDForBundleID:].cold.1
+ -[GKUnknownPlayerInternal gamePlayerIDForBundleID:]
+ -[GKUnknownPlayerInternal teamPlayerIDForBundleID:]
+ -[NSDictionary(GKCollectionUtils) _gkDictionaryWithValue:forKey:]
+ -[NSError(GKServerError) isGKClientError]
+ -[NSError(GKServerError) isGKCompoundError]
+ -[NSError(GKServerError) isGKServerError]
+ GCC_except_table104
+ GCC_except_table167
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table184
+ GCC_except_table201
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table66
+ GCC_except_table82
+ GCC_except_table95
+ GCC_except_table97
+ _GKDashboardLaunchContextAppStore
+ _GKDashboardLaunchContextContacts
+ _GKDashboardLaunchContextGameController
+ _GKDashboardLaunchContextPushNotification
+ _GKDashboardLaunchContextWidget
+ _GKMoltresIdentifier
+ _GKMoltresOverlayIdentifier
+ _GKRemoteAlertUserInfoDashboardLaunchContextKey
+ _OBJC_IVAR_$_GKPlayerInternal._gameBundleID
+ _OBJC_IVAR_$_GKPlayerInternal._sanitizeBeforeEncoding
+ __OBJC_$_CLASS_METHODS_NSError(GameKitErrors|GKServerError|GKGameSessionError)
+ __OBJC_$_INSTANCE_METHODS_NSError(GameKitErrors|GKServerError|GKGameSessionError)
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke.380
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke.382
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke.390
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke_2.381
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke_2.381.cold.1
+ ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke_2.391
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.548
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.556
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.556.cold.1
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.556.cold.2
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.572
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.584
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.592
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.573
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.573.cold.1
+ ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.585
+ ___20-[GKPlayer playerID]_block_invoke.cold.1
+ ___24-[GKPlayer isArcadeGame]_block_invoke
+ ___24-[GKPlayer isArcadeGame]_block_invoke_2
+ ___24-[GKPlayer teamPlayerID]_block_invoke
+ ___24-[GKPlayer teamPlayerID]_block_invoke.cold.1
+ ___36-[GKServiceProxy buildServiceLookup]_block_invoke.882
+ ___36-[GKServiceProxy buildServiceLookup]_block_invoke.882.cold.1
+ ___36-[GKServiceProxy buildServiceLookup]_block_invoke.884
+ ___36-[GKServiceProxy buildServiceLookup]_block_invoke.884.cold.1
+ ___36-[GKServiceProxy buildServiceLookup]_block_invoke.884.cold.2
+ ___41-[GKMatch reinviteeAcceptedNotification:]_block_invoke
+ ___42-[GKMatchmaker inviteeUpdateNotification:]_block_invoke.788
+ ___42-[GKMatchmaker inviteeUpdateNotification:]_block_invoke.788.cold.1
+ ___44-[GKMatchmaker inviteeDeclinedWithUserInfo:]_block_invoke.776
+ ___49-[GKMatchmaker shareInviteeAcceptedWithUserInfo:]_block_invoke.725
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.104
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.113
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.118
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.123
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.123.cold.1
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.127
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.128
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.128.cold.1
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.752
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.752.cold.1
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.758
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.759
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke_2
+ ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke_2.cold.1
+ ___55-[GKMatchmaker matchForRemoteInvite:completionHandler:]_block_invoke.328
+ ___55-[GKMatchmaker matchForRemoteInvite:completionHandler:]_block_invoke.347
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.138
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.138.cold.1
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.152
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_2.140
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_3.141
+ ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_3.141.cold.1
+ ___61-[GKLocalPlayer _startAuthenticationForExistingPrimaryPlayer]_block_invoke.264
+ ___63-[GKMatchmaker loadURLForMatch:matchRequest:completionHandler:]_block_invoke.596
+ ___63-[GKMatchmaker loadURLForMatch:matchRequest:completionHandler:]_block_invoke.600
+ ___66-[ACAccountStore(GameCenter) _gkSaveCredential:completionHandler:]_block_invoke.184
+ ___67-[GKLocalPlayer handleChallengableFriendsResults:error:completion:]_block_invoke.140
+ ___67-[GKLocalPlayer handleChallengableFriendsResults:error:completion:]_block_invoke_2.144
+ ___68-[ACAccountStore(GameCenter) _gkDeleteCredential:completionHandler:]_block_invoke.194
+ ___75-[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:]_block_invoke
+ ___75-[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:]_block_invoke.449
+ ___75-[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:]_block_invoke.449.cold.1
+ ___75-[GKMatch connectToPlayers:version:invitedByLocalPlayer:completionHandler:]_block_invoke.cold.1
+ ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.156
+ ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.156.cold.1
+ ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.160
+ ___83-[GKPlayerCredentialController replaceCredential:withCredential:completionHandler:]_block_invoke.98
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.436
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.448
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.456
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.460
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.460.cold.1
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.481
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.481.cold.1
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.485
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.485.cold.1
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.485.cold.2
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.498
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.498.cold.1
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.498.cold.2
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.517
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.525
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.529
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.533
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.537
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.518
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.518.cold.1
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.518.cold.2
+ ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.518.cold.3
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke.399
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke.404
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.400
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.400.cold.1
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.405
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_5
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_6
+ ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_6.cold.1
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e14_v16?0?<v?>8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s64l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s64l8s72l8s40l8s48l8s56l8
+ ___block_literal_global.130
+ ___block_literal_global.134
+ ___block_literal_global.143
+ ___block_literal_global.148
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.221
+ ___block_literal_global.247
+ ___block_literal_global.25
+ ___block_literal_global.257
+ ___block_literal_global.389
+ ___block_literal_global.397
+ ___block_literal_global.405
+ ___block_literal_global.414
+ ___block_literal_global.417
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.462
+ ___block_literal_global.563
+ ___block_literal_global.587
+ ___block_literal_global.610
+ ___block_literal_global.626
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.663
+ ___block_literal_global.671
+ ___block_literal_global.700
+ ___block_literal_global.754
+ ___block_literal_global.770
+ ___block_literal_global.772
+ ___block_literal_global.790
+ ___block_literal_global.834
+ ___block_literal_global.85
+ __unnamed_array_storage.51
+ _isArcadeGame.isArcadeGame
+ _isArcadeGame.onceToken
+ _objc_msgSend$_gkSHA256Hash
+ _objc_msgSend$connectToPlayers:version:invitedByLocalPlayer:completionHandler:
+ _objc_msgSend$gameBundleID
+ _objc_msgSend$gamePlayerIDForBundleID:
+ _objc_msgSend$isGKClientError
+ _objc_msgSend$isGKCompoundError
+ _objc_msgSend$isGKServerError
+ _objc_msgSend$lockedDown
+ _objc_msgSend$minimalInternalFromSourcePlayer:
+ _objc_msgSend$nonPersistentScopedID
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processInfo
+ _objc_msgSend$sanitize
+ _objc_msgSend$sanitizeBeforeEncoding
+ _objc_msgSend$setGameBundleID:gamePlayerID:teamPlayerID:
+ _objc_msgSend$stringForPlatform:
+ _objc_msgSend$supportedPlatforms
+ _objc_msgSend$teamPlayerIDForBundleID:
+ _objectdestroy.23Tm
+ _objectdestroy.29Tm
+ _objectdestroy.58Tm
+ _objectdestroy.72Tm
+ _secureCodedPropertyKeys.onceToken.245
+ _secureCodedPropertyKeys.onceToken.502
+ _secureCodedPropertyKeys.onceToken.523
+ _secureCodedPropertyKeys.onceToken.544
+ _secureCodedPropertyKeys.onceToken.585
+ _secureCodedPropertyKeys.onceToken.621
+ _secureCodedPropertyKeys.onceToken.645
+ _secureCodedPropertyKeys.onceToken.737
+ _secureCodedPropertyKeys.onceToken.760
+ _secureCodedPropertyKeys.sSecureCodedKeys.244
+ _secureCodedPropertyKeys.sSecureCodedKeys.501
+ _secureCodedPropertyKeys.sSecureCodedKeys.522
+ _secureCodedPropertyKeys.sSecureCodedKeys.543
+ _secureCodedPropertyKeys.sSecureCodedKeys.584
+ _secureCodedPropertyKeys.sSecureCodedKeys.620
+ _secureCodedPropertyKeys.sSecureCodedKeys.644
+ _secureCodedPropertyKeys.sSecureCodedKeys.736
+ _secureCodedPropertyKeys.sSecureCodedKeys.759
+ _symbolic _____Sg10errorState_______pSg13internalErrort 20GameCenterFoundation21FastSyncLeaderElectorC10ErrorStateO s0H0P
+ _symbolic ______p5error_t s5ErrorP
+ _teamPlayerID.onceToken
- +[GKGameDescriptor platformStringForServerRequest:]
- +[GKLinkedAccountsServiceInterface interfaceProtocol]
- +[GKLinkedAccountsServicePrivateInterface interfaceProtocol]
- +[NSError(GameKitErrors) userErrorForInternalErrorCode:reason:]
- -[GKAnonymousPlayerInternal gamePlayerID]
- -[GKAnonymousPlayerInternal teamPlayerID]
- -[GKAutomatchPlayerInternal gamePlayerID]
- -[GKAutomatchPlayerInternal teamPlayerID]
- -[GKLocalPlayer recordScopedIdState:]
- -[GKLocalPlayer scopedIDsArePersistent]
- -[GKMatch connectToPlayers:version:invitedByLocalPlayer:]
- -[GKMatch connectToPlayers:version:invitedByLocalPlayer:].cold.1
- -[GKMatch connectToPlayers:version:invitedByLocalPlayer:].cold.2
- -[GKPlayer playerID].cold.1
- -[GKPlayerInternal setGamePlayerID:]
- -[GKPlayerInternal setTeamPlayerID:]
- -[GKPlayerInternal stripPIIs]
- -[GKRemoteAlertLauncher launchBypassingPreAuthentication:forGame:hostPID:deeplink:observer:]
- -[GKRemoteAlertLauncher launchBypassingPreAuthentication:forGame:hostPID:deeplink:observer:].cold.1
- -[GKSpecialPlayerInternal gamePlayerID]
- -[GKSpecialPlayerInternal setGamePlayerID:]
- -[GKSpecialPlayerInternal setTeamPlayerID:]
- -[GKSpecialPlayerInternal teamPlayerID]
- -[GKUnauthenticatedPlayerInternal gamePlayerID]
- -[GKUnauthenticatedPlayerInternal gamePlayerID].cold.1
- -[GKUnauthenticatedPlayerInternal teamPlayerID]
- -[GKUnauthenticatedPlayerInternal teamPlayerID].cold.1
- -[GKUnknownPlayerInternal gamePlayerID]
- -[GKUnknownPlayerInternal teamPlayerID]
- GCC_except_table166
- GCC_except_table169
- GCC_except_table174
- GCC_except_table176
- GCC_except_table183
- GCC_except_table194
- GCC_except_table41
- GCC_except_table49
- GCC_except_table63
- GCC_except_table71
- GCC_except_table89
- GCC_except_table93
- _OBJC_CLASS_$_GKLinkedAccountsServiceInterface
- _OBJC_CLASS_$_GKLinkedAccountsServicePrivateInterface
- _OBJC_METACLASS_$_GKLinkedAccountsServiceInterface
- _OBJC_METACLASS_$_GKLinkedAccountsServicePrivateInterface
- _OUTLINED_FUNCTION_170
- __OBJC_$_CLASS_METHODS_GKLinkedAccountsServiceInterface
- __OBJC_$_CLASS_METHODS_GKLinkedAccountsServicePrivateInterface
- __OBJC_$_CLASS_METHODS_NSError(GameKitErrors|GKGameSessionError)
- __OBJC_$_INSTANCE_METHODS_NSError(GameKitErrors|GKGameSessionError)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_GKLinkedAccountsServicePrivate
- __OBJC_$_PROTOCOL_METHOD_TYPES_GKLinkedAccountsServicePrivate
- __OBJC_$_PROTOCOL_REFS_GKLinkedAccountsService
- __OBJC_$_PROTOCOL_REFS_GKLinkedAccountsServicePrivate
- __OBJC_CLASS_RO_$_GKLinkedAccountsServiceInterface
- __OBJC_CLASS_RO_$_GKLinkedAccountsServicePrivateInterface
- __OBJC_LABEL_PROTOCOL_$_GKLinkedAccountsService
- __OBJC_LABEL_PROTOCOL_$_GKLinkedAccountsServicePrivate
- __OBJC_METACLASS_RO_$_GKLinkedAccountsServiceInterface
- __OBJC_METACLASS_RO_$_GKLinkedAccountsServicePrivateInterface
- __OBJC_PROTOCOL_$_GKLinkedAccountsService
- __OBJC_PROTOCOL_$_GKLinkedAccountsServicePrivate
- __OBJC_PROTOCOL_REFERENCE_$_GKLinkedAccountsService
- __OBJC_PROTOCOL_REFERENCE_$_GKLinkedAccountsServicePrivate
- ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke.386
- ___127-[GKMatchmaker invitePlayersWithRequest:serverHosted:onlineConnectionData:devicePushTokenMap:isNearbyInvite:completionHandler:]_block_invoke_2.387
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.542
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.550
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.550.cold.1
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.550.cold.2
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.566
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.578
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke.586
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.567
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.567.cold.1
- ___128-[GKMatchmaker matchWithRequest:currentMatch:hostedCurrentPlayerCount:serverHosted:rematchID:devicePushToken:completionHandler:]_block_invoke_2.579
- ___20-[GKPlayer playerID]_block_invoke_2
- ___36-[GKServiceProxy buildServiceLookup]_block_invoke.879
- ___36-[GKServiceProxy buildServiceLookup]_block_invoke.879.cold.1
- ___36-[GKServiceProxy buildServiceLookup]_block_invoke.881
- ___36-[GKServiceProxy buildServiceLookup]_block_invoke.881.cold.1
- ___36-[GKServiceProxy buildServiceLookup]_block_invoke.881.cold.2
- ___39-[GKLocalPlayer scopedIDsArePersistent]_block_invoke
- ___39-[GKLocalPlayer scopedIDsArePersistent]_block_invoke_2
- ___44-[GKMatchmaker inviteeDeclinedWithUserInfo:]_block_invoke.768
- ___49-[GKMatchmaker shareInviteeAcceptedWithUserInfo:]_block_invoke.719
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.107
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.112
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.117
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.117.cold.1
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.121
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.122
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.122.cold.1
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.98
- ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.746
- ___54-[GKMatchmaker inviteeAccepted:userInfo:allResponded:]_block_invoke.746.cold.1
- ___55-[GKMatchmaker matchForRemoteInvite:completionHandler:]_block_invoke.346
- ___57-[GKLocalPlayer _loadFriendPlayersWithCompletionHandler:]_block_invoke_3
- ___57-[GKMatch connectToPlayers:version:invitedByLocalPlayer:]_block_invoke
- ___57-[GKMatch connectToPlayers:version:invitedByLocalPlayer:]_block_invoke.449
- ___57-[GKMatch connectToPlayers:version:invitedByLocalPlayer:]_block_invoke.449.cold.1
- ___57-[GKMatch connectToPlayers:version:invitedByLocalPlayer:]_block_invoke.cold.1
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.134
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.134.cold.1
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke.148
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_2.136
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_3.137
- ___61+[GKPlayer _loadPlayersForIdentifiers:withCompletionHandler:]_block_invoke_3.137.cold.1
- ___61-[GKLocalPlayer _startAuthenticationForExistingPrimaryPlayer]_block_invoke.294
- ___63-[GKMatchmaker loadURLForMatch:matchRequest:completionHandler:]_block_invoke.590
- ___63-[GKMatchmaker loadURLForMatch:matchRequest:completionHandler:]_block_invoke.594
- ___66-[ACAccountStore(GameCenter) _gkSaveCredential:completionHandler:]_block_invoke.178
- ___67-[GKLocalPlayer handleChallengableFriendsResults:error:completion:]_block_invoke.171
- ___67-[GKLocalPlayer handleChallengableFriendsResults:error:completion:]_block_invoke_2.175
- ___68-[ACAccountStore(GameCenter) _gkDeleteCredential:completionHandler:]_block_invoke.188
- ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.150
- ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.150.cold.1
- ___81-[ACAccountStore(GameCenter) _getAltDSIDFromIDMSForCredential:completionHandler:]_block_invoke.154
- ___83-[GKPlayerCredentialController replaceCredential:withCredential:completionHandler:]_block_invoke.99
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.434
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.446
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.454
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.458
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.458.cold.1
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.479
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.479.cold.1
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.483
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.483.cold.1
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.483.cold.2
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.483.cold.3
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.511
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.519
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.523
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.527
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke.531
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.512
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.512.cold.1
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.512.cold.2
- ___84-[GKMatchmaker _request:match:rematchID:serverHosted:playerCount:completionHandler:]_block_invoke_2.512.cold.3
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke.392
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke.397
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke.402
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.393
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.393.cold.1
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.398
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.398.cold.1
- ___91-[GKMatchmaker invitePlayersWithRequest:serverHosted:devicePushTokenMap:completionHandler:]_block_invoke_2.403
- ___block_descriptor_40_e8_32s_e39_"GKPlayer"24?0"GKPlayerInternal"8Q16ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s48l8s40l8
- ___block_literal_global.114
- ___block_literal_global.142
- ___block_literal_global.160
- ___block_literal_global.162
- ___block_literal_global.165
- ___block_literal_global.218
- ___block_literal_global.244
- ___block_literal_global.258
- ___block_literal_global.33
- ___block_literal_global.373
- ___block_literal_global.382
- ___block_literal_global.390
- ___block_literal_global.398
- ___block_literal_global.407
- ___block_literal_global.410
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.460
- ___block_literal_global.532
- ___block_literal_global.555
- ___block_literal_global.620
- ___block_literal_global.641
- ___block_literal_global.650
- ___block_literal_global.655
- ___block_literal_global.657
- ___block_literal_global.665
- ___block_literal_global.694
- ___block_literal_global.730
- ___block_literal_global.748
- ___block_literal_global.764
- ___block_literal_global.81
- ___block_literal_global.820
- __unnamed_array_storage.53
- _objc_msgSend$connectToPlayers:version:invitedByLocalPlayer:
- _objc_msgSend$currentPlatformServerString
- _objc_msgSend$longValue
- _objc_msgSend$platformStringForServerRequest:
- _objc_msgSend$setGamePlayerID:
- _objc_msgSend$setTeamPlayerID:
- _objectdestroy.22Tm
- _objectdestroy.28Tm
- _objectdestroy.57Tm
- _objectdestroy.71Tm
- _playerID.isArcadeGame
- _secureCodedPropertyKeys.onceToken.242
- _secureCodedPropertyKeys.onceToken.471
- _secureCodedPropertyKeys.onceToken.492
- _secureCodedPropertyKeys.onceToken.513
- _secureCodedPropertyKeys.onceToken.553
- _secureCodedPropertyKeys.onceToken.589
- _secureCodedPropertyKeys.onceToken.613
- _secureCodedPropertyKeys.onceToken.705
- _secureCodedPropertyKeys.onceToken.728
- _secureCodedPropertyKeys.sSecureCodedKeys.241
- _secureCodedPropertyKeys.sSecureCodedKeys.470
- _secureCodedPropertyKeys.sSecureCodedKeys.491
- _secureCodedPropertyKeys.sSecureCodedKeys.512
- _secureCodedPropertyKeys.sSecureCodedKeys.552
- _secureCodedPropertyKeys.sSecureCodedKeys.588
- _secureCodedPropertyKeys.sSecureCodedKeys.612
- _secureCodedPropertyKeys.sSecureCodedKeys.704
- _secureCodedPropertyKeys.sSecureCodedKeys.727
CStrings:
+ "\x05\x1d$b"
+ "%@(%p)(playerID:%@, alias:%@, accountName: %@, gameBundleID:%@, gamePlayerID:%@, teamPlayerID:%@, _achievementsVisibility:%@)"
+ "%@:%@:%d"
+ "(%@alias:%@ gameBundleID:%@ gamePlayerID:%@ teamPlayerID:%@ name:%@ status:%@ friendBiDirectional:%@ friendPlayedWith:%@ friendPlayedNearby:%@ acceptedGameInviteFromThisFriend:%@ initiatedGameInviteToThisFriend:%@ automatchedTogether:%@)"
+ "-> Failed to choose host. No transport participant found for handle: "
+ "13BkaEjxAE14gjlkESTaloU7hVo3CJfEpwAtY/48TdE="
+ "@\"GKLocalPlayerInternal\""
+ "Arcade game is attempting to fetch teamPlayerID"
+ "Cannot send state call back for player: %@, state: %@, due to missing delegates set for GKMatch: %p"
+ "Converting a GKPlayerInternal to a GKLocalPlayerInternal"
+ "Failed to connect invitees due to error: %@"
+ "FailedToElectLeader: "
+ "GKServerError"
+ "Initialized player with internal representation: %@"
+ "Invitee failed to perform invite update due to error: %@"
+ "Nil channel for default scope"
+ "Nil local player handle"
+ "Not setting invalid scoped IDs to internal player, bundle: %@, game: %@, team: %@"
+ "RemoteAlert: launchBypassingPreAuthentication:%d\n forGame:%@\n hostPID:%@\n deeplink:%@\n launchContext:%@\n observer:%@"
+ "ScopedIDs for Player: %@ gamePlayerID: %@ teamPlayerID: %@"
+ "Skip transport selection for undefined version."
+ "T@\"GKLocalPlayerInternal\",&,V_playerInternal"
+ "T@\"NSString\",R,V_gameBundleID"
+ "T@\"NSString\",R,V_gamePlayerID"
+ "T@\"NSString\",R,V_teamPlayerID"
+ "T@?,C,N,V_sanitizeBeforeEncoding"
+ "TB,R,N,GisGameCenterDisabled"
+ "Unable to decode player internal due to unrecognized type"
+ "Unknown best host handle"
+ "Vv44@0:8@\"GKGameInternal\"16i24@\"NSDictionary\"28@\"NSString\"36"
+ "Vv44@0:8@16i24@28@36"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?@\"GKAuthenticateResponse\"@\"NSError\">48"
+ "Vv56@0:8@16@24@32B40B44@?48"
+ "_gkDictionaryWithValue:forKey:"
+ "_sanitizeBeforeEncoding"
+ "appStore"
+ "asking for GKLocalPlayer gamePlayerID when player is not authenticated. Might be in the process of being authenticated or this is a race condition.Call stack:%@"
+ "asking for GKLocalPlayer teamPlayerID when player is not authenticated. Might be in the process of being authenticated or this is a race condition.Call stack:%@"
+ "authenticatePlayerWithUsername:password:altDSID:isGame:usingFastPath:handler:"
+ "connectToPlayers:version:invitedByLocalPlayer:completionHandler:"
+ "contacts"
+ "dashboard-launch-context"
+ "determineBestHostPlayerHandle(channel:)"
+ "easySignInSheetEnabled"
+ "easy_sign_in_sheet"
+ "gameCenterDisabled"
+ "gameController"
+ "gamePlayerIDForBundleID:"
+ "initWithSanitizeBeforeEncodingBlock:"
+ "isGKClientError"
+ "isGKCompoundError"
+ "isGKServerError"
+ "isGameCenterDisabled"
+ "isGameCenterHostingContainer"
+ "launchBypassingPreAuthentication:forGame:hostPID:deeplink:launchContext:observer:"
+ "minimalInternalFromSourcePlayer:"
+ "nonPersistentScopedID"
+ "openDashboardAsRemoteAlertForGame:hostPID:deeplink:launchContext:"
+ "pushNotification"
+ "sanitize"
+ "sanitizeBeforeEncoding"
+ "sendLeaderQueryMessage(_:localParticipantHandle:)"
+ "sendLocalScoreToRemoteParticipants(_:localParticipantHandle:channel:)"
+ "setGameBundleID:gamePlayerID:teamPlayerID:"
+ "setSanitizeBeforeEncoding:"
+ "stringForPlatform:"
+ "supportsPlatform:"
+ "t/IRG+OATWH+smiJ2A4GRp6fHjSftOF5bYwT7kv+1Mk="
+ "teamPlayerIDForBundleID:"
+ "timeout"
+ "v40@0:8@16C24B28@?32"
+ "v56@0:8B16@20i28@32@40@48"
+ "waitScoresFromAllActiveParticipantsOrTimeout(channel:)"
+ "widget"
- "\x04\x1d$a"
- "%@(%p)(playerID:%@, alias:%@, accountName: %@, gamePlayerID:%@, teamPlayerID:%@, _achievementsVisibility:%@)"
- "%lu"
- "(%@alias:%@ gamePlayerID:%@ teamPlayerID:%@ name:%@ status:%@ friendBiDirectional:%@ friendPlayedWith:%@ friendPlayedNearby:%@ acceptedGameInviteFromThisFriend:%@ initiatedGameInviteToThisFriend:%@ automatchedTogether:%@)"
- "-> Cannot query remote player scores because the local participant handle is nil."
- "-> Failed to choose host. State: "
- "Cannot determine best host player handle because the transport is nil."
- "Cannot determine if all scores are received because the transport is nil."
- "Cannot query remote player scores because the transport is nil."
- "Cannot send state call back for player: %@, state: %@, as there is no delegate or inviteDelegate set for GKMatch: %p"
- "Cannot update score because the transport is nil."
- "GKLinkedAccountsService"
- "GKLinkedAccountsServiceInterface"
- "GKLinkedAccountsServicePrivate"
- "GKLinkedAccountsServicePrivateInterface"
- "RemoteAlert: launchBypassingPreAuthentication:%d\nforGame:%@\nhostPID:%@\ndeeplink:%@\nobserver:%@"
- "ScopedIDs for Player: %@ gameID: %@ teamID: %@"
- "T@\"GKPlayerInternal\",&,V_playerInternal"
- "T@\"NSString\",&,V_gamePlayerID"
- "T@\"NSString\",&,V_teamPlayerID"
- "Vv28@0:8c16@?20"
- "Vv28@0:8c16@?<v@?@\"NSError\">20"
- "Vv28@0:8c16@?<v@?@\"NSString\"@\"NSError\">20"
- "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "allScoreReceived"
- "availableExternalServicesWithHandler:"
- "connectExternalService:handler:"
- "connectToPlayers:version:invitedByLocalPlayer:"
- "determineBestHostPlayerHandle()"
- "disconnectExternalService:handler:"
- "getAuthTokenForExternalService:handler:"
- "launchBypassingPreAuthentication:forGame:hostPID:deeplink:observer:"
- "longValue"
- "notifyAvailableExternalServicesWithHandler:"
- "platformStringForServerRequest:"
- "requestGKPlayerIDforiCloudIDs:handler:"
- "scoped:initialized a local player:%@ with gamePlayerID:%@ teamPlayerID:%@"
- "scoped:initialized a non local player:%@ with gamePlayerID:%@"
- "sendLeaderQueryMessage(_:)"
- "sendLocalScoreToRemoteParticipants(_:)"
- "setGamePlayerID:"
- "setTeamPlayerID:"
- "stripPIIs"
- "updateScore(_:forParticipantHandle:)"
- "userErrorForInternalErrorCode:reason:"
- "v32@0:8@16C24B28"
- "v48@0:8B16@20i28@32@40"
- "waitScoresFromAllActiveParticipantsOrTimeout()"

```
