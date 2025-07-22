## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.0.64.0.0
-  __TEXT.__text: 0x166a20
+820.0.70.0.0
+  __TEXT.__text: 0x166c64
   __TEXT.__auth_stubs: 0x27e0
-  __TEXT.__objc_methlist: 0x1205c
-  __TEXT.__cstring: 0x196b3
+  __TEXT.__objc_methlist: 0x120ec
+  __TEXT.__cstring: 0x19753
   __TEXT.__const: 0x5b70
   __TEXT.__gcc_except_tab: 0x1450
   __TEXT.__oslogstring: 0xd9eb

   __TEXT.__unwind_info: 0x64b8
   __TEXT.__eh_frame: 0x5480
   __TEXT.__objc_classname: 0x1ea9
-  __TEXT.__objc_methname: 0x269e8
-  __TEXT.__objc_methtype: 0x62ea
-  __TEXT.__objc_stubs: 0x14d60
+  __TEXT.__objc_methname: 0x26b6c
+  __TEXT.__objc_methtype: 0x62d0
+  __TEXT.__objc_stubs: 0x14e20
   __DATA_CONST.__got: 0x10c8
-  __DATA_CONST.__const: 0x6048
+  __DATA_CONST.__const: 0x6058
   __DATA_CONST.__objc_classlist: 0x808
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8430
+  __DATA_CONST.__objc_selrefs: 0x8470
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4f8
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1400
   __AUTH_CONST.__const: 0x57a8
-  __AUTH_CONST.__cfstring: 0x11180
-  __AUTH_CONST.__objc_const: 0x244a8
+  __AUTH_CONST.__cfstring: 0x11260
+  __AUTH_CONST.__objc_const: 0x245c0
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2b48
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0xff8
+  __DATA.__objc_ivar: 0x100c
   __DATA.__data: 0x3970
-  __DATA.__bss: 0x8320
+  __DATA.__bss: 0x8360
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2b78
   __DATA_DIRTY.__data: 0x598
-  __DATA_DIRTY.__bss: 0xa58
+  __DATA_DIRTY.__bss: 0xa18
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6D912747-C16E-3C97-A6D1-1A3F8B82C8E2
-  Functions: 10737
-  Symbols:   24480
-  CStrings:  13511
+  UUID: 91B39D31-9316-33CD-A615-775105EBF15F
+  Functions: 10748
+  Symbols:   24515
+  CStrings:  13539
 
Symbols:
+ -[GKBaseLeaderboardChallengeInternal challengeVendorID]
+ -[GKBaseLeaderboardChallengeInternal scheduledEndDate]
+ -[GKBaseLeaderboardChallengeInternal setChallengeVendorID:]
+ -[GKBaseLeaderboardChallengeInternal setScheduledEndDate:]
+ -[GKClientPreferencesSupport localPlayerID]
+ -[GKClientPreferencesSupport localPlayerIsUnderage]
+ -[GKLeaderboardChallengeInviteInternal challengeVendorID]
+ -[GKLeaderboardChallengeInviteInternal setChallengeVendorID:]
+ -[GKPlayerInternal isChallengeable]
+ -[GKPlayerInternal setIsChallengeable:]
+ -[GKPlayerInternal setSupportsMultiplayerActivities:]
+ -[GKPlayerInternal supportsMultiplayerActivities]
+ -[GKTTRLogRequestInfo initWithPlayersAndPushTokens:radarID:requesterPlayerID:]
+ -[GKTTRLogRequestInfo requesterPlayerID]
+ -[GKTTRLogRequestInfo setRequesterPlayerID:]
+ _GKIsChallengeable
+ _GKSupportsMultiplayerActivities
+ _OBJC_IVAR_$_GKBaseLeaderboardChallengeInternal._challengeVendorID
+ _OBJC_IVAR_$_GKBaseLeaderboardChallengeInternal._scheduledEndDate
+ _OBJC_IVAR_$_GKLeaderboardChallengeInviteInternal._challengeVendorID
+ _OBJC_IVAR_$_GKPlayerInternal._isChallengeable
+ _OBJC_IVAR_$_GKPlayerInternal._supportsMultiplayerActivities
+ _OBJC_IVAR_$_GKTTRLogRequestInfo._requesterPlayerID
+ ___block_literal_global.251
+ ___block_literal_global.308
+ ___block_literal_global.344
+ ___block_literal_global.356
+ ___block_literal_global.378
+ ___block_literal_global.400
+ ___block_literal_global.427
+ ___block_literal_global.433
+ ___block_literal_global.466
+ ___block_literal_global.472
+ ___block_literal_global.486
+ ___block_literal_global.539
+ ___block_literal_global.571
+ ___block_literal_global.577
+ ___block_literal_global.591
+ ___block_literal_global.596
+ ___block_literal_global.644
+ ___block_literal_global.662
+ ___block_literal_global.672
+ ___block_literal_global.702
+ ___block_literal_global.707
+ ___block_literal_global.765
+ _objc_msgSend$isChallengeable
+ _objc_msgSend$localPlayerIsUnderage
+ _objc_msgSend$setChallengeVendorID:
+ _objc_msgSend$setIsChallengeable:
+ _objc_msgSend$setRequesterPlayerID:
+ _objc_msgSend$setScheduledEndDate:
+ _objc_msgSend$setSupportsMultiplayerActivities:
+ _objc_msgSend$supportsMultiplayerActivities
+ _secureCodedPropertyKeys.onceToken.194
+ _secureCodedPropertyKeys.onceToken.306
+ _secureCodedPropertyKeys.onceToken.316
+ _secureCodedPropertyKeys.onceToken.332
+ _secureCodedPropertyKeys.onceToken.342
+ _secureCodedPropertyKeys.onceToken.376
+ _secureCodedPropertyKeys.onceToken.386
+ _secureCodedPropertyKeys.onceToken.425
+ _secureCodedPropertyKeys.onceToken.464
+ _secureCodedPropertyKeys.onceToken.484
+ _secureCodedPropertyKeys.onceToken.491
+ _secureCodedPropertyKeys.onceToken.516
+ _secureCodedPropertyKeys.onceToken.537
+ _secureCodedPropertyKeys.onceToken.549
+ _secureCodedPropertyKeys.onceToken.569
+ _secureCodedPropertyKeys.onceToken.589
+ _secureCodedPropertyKeys.onceToken.594
+ _secureCodedPropertyKeys.onceToken.630
+ _secureCodedPropertyKeys.onceToken.642
+ _secureCodedPropertyKeys.onceToken.654
+ _secureCodedPropertyKeys.onceToken.660
+ _secureCodedPropertyKeys.onceToken.670
+ _secureCodedPropertyKeys.onceToken.740
+ _secureCodedPropertyKeys.onceToken.763
+ _secureCodedPropertyKeys.sSecureCodedKeys.193
+ _secureCodedPropertyKeys.sSecureCodedKeys.305
+ _secureCodedPropertyKeys.sSecureCodedKeys.315
+ _secureCodedPropertyKeys.sSecureCodedKeys.331
+ _secureCodedPropertyKeys.sSecureCodedKeys.341
+ _secureCodedPropertyKeys.sSecureCodedKeys.375
+ _secureCodedPropertyKeys.sSecureCodedKeys.385
+ _secureCodedPropertyKeys.sSecureCodedKeys.424
+ _secureCodedPropertyKeys.sSecureCodedKeys.463
+ _secureCodedPropertyKeys.sSecureCodedKeys.483
+ _secureCodedPropertyKeys.sSecureCodedKeys.490
+ _secureCodedPropertyKeys.sSecureCodedKeys.515
+ _secureCodedPropertyKeys.sSecureCodedKeys.536
+ _secureCodedPropertyKeys.sSecureCodedKeys.548
+ _secureCodedPropertyKeys.sSecureCodedKeys.568
+ _secureCodedPropertyKeys.sSecureCodedKeys.588
+ _secureCodedPropertyKeys.sSecureCodedKeys.593
+ _secureCodedPropertyKeys.sSecureCodedKeys.629
+ _secureCodedPropertyKeys.sSecureCodedKeys.641
+ _secureCodedPropertyKeys.sSecureCodedKeys.653
+ _secureCodedPropertyKeys.sSecureCodedKeys.659
+ _secureCodedPropertyKeys.sSecureCodedKeys.669
+ _secureCodedPropertyKeys.sSecureCodedKeys.739
+ _secureCodedPropertyKeys.sSecureCodedKeys.762
- -[GKClientPreferencesSupport localPlayerInternal]
- -[GKTTRLogRequestInfo initWithPlayersAndPushTokens:radarID:requesterAlias:]
- -[GKTTRLogRequestInfo requesterAlias]
- -[GKTTRLogRequestInfo setRequesterAlias:]
- _OBJC_IVAR_$_GKTTRLogRequestInfo._requesterAlias
- ___block_literal_global.227
- ___block_literal_global.232
- ___block_literal_global.289
- ___block_literal_global.299
- ___block_literal_global.306
- ___block_literal_global.337
- ___block_literal_global.359
- ___block_literal_global.381
- ___block_literal_global.408
- ___block_literal_global.414
- ___block_literal_global.447
- ___block_literal_global.453
- ___block_literal_global.467
- ___block_literal_global.520
- ___block_literal_global.552
- ___block_literal_global.558
- ___block_literal_global.572
- ___block_literal_global.580
- ___block_literal_global.625
- ___block_literal_global.643
- ___block_literal_global.653
- ___block_literal_global.683
- ___block_literal_global.688
- ___block_literal_global.749
- _objc_msgSend$localPlayerInternal
- _objc_msgSend$setRequesterAlias:
- _secureCodedPropertyKeys.onceToken.172
- _secureCodedPropertyKeys.onceToken.287
- _secureCodedPropertyKeys.onceToken.297
- _secureCodedPropertyKeys.onceToken.323
- _secureCodedPropertyKeys.onceToken.357
- _secureCodedPropertyKeys.onceToken.367
- _secureCodedPropertyKeys.onceToken.406
- _secureCodedPropertyKeys.onceToken.465
- _secureCodedPropertyKeys.onceToken.475
- _secureCodedPropertyKeys.onceToken.500
- _secureCodedPropertyKeys.onceToken.518
- _secureCodedPropertyKeys.onceToken.533
- _secureCodedPropertyKeys.onceToken.550
- _secureCodedPropertyKeys.onceToken.570
- _secureCodedPropertyKeys.onceToken.578
- _secureCodedPropertyKeys.onceToken.614
- _secureCodedPropertyKeys.onceToken.623
- _secureCodedPropertyKeys.onceToken.638
- _secureCodedPropertyKeys.onceToken.641
- _secureCodedPropertyKeys.onceToken.651
- _secureCodedPropertyKeys.onceToken.724
- _secureCodedPropertyKeys.onceToken.747
- _secureCodedPropertyKeys.sSecureCodedKeys.171
- _secureCodedPropertyKeys.sSecureCodedKeys.286
- _secureCodedPropertyKeys.sSecureCodedKeys.296
- _secureCodedPropertyKeys.sSecureCodedKeys.322
- _secureCodedPropertyKeys.sSecureCodedKeys.356
- _secureCodedPropertyKeys.sSecureCodedKeys.366
- _secureCodedPropertyKeys.sSecureCodedKeys.405
- _secureCodedPropertyKeys.sSecureCodedKeys.464
- _secureCodedPropertyKeys.sSecureCodedKeys.474
- _secureCodedPropertyKeys.sSecureCodedKeys.499
- _secureCodedPropertyKeys.sSecureCodedKeys.517
- _secureCodedPropertyKeys.sSecureCodedKeys.532
- _secureCodedPropertyKeys.sSecureCodedKeys.549
- _secureCodedPropertyKeys.sSecureCodedKeys.569
- _secureCodedPropertyKeys.sSecureCodedKeys.577
- _secureCodedPropertyKeys.sSecureCodedKeys.613
- _secureCodedPropertyKeys.sSecureCodedKeys.622
- _secureCodedPropertyKeys.sSecureCodedKeys.637
- _secureCodedPropertyKeys.sSecureCodedKeys.640
- _secureCodedPropertyKeys.sSecureCodedKeys.650
- _secureCodedPropertyKeys.sSecureCodedKeys.723
- _secureCodedPropertyKeys.sSecureCodedKeys.746
CStrings:
+ "T@\"NSDate\",&,N,V_scheduledEndDate"
+ "T@\"NSString\",&,N,V_challengeVendorID"
+ "T@\"NSString\",&,N,V_requesterPlayerID"
+ "TB,N,V_isChallengeable"
+ "TB,N,V_supportsMultiplayerActivities"
+ "_challengeVendorID"
+ "_isChallengeable"
+ "_requesterPlayerID"
+ "_scheduledEndDate"
+ "_supportsMultiplayerActivities"
+ "challengeVendorID"
+ "initWithPlayersAndPushTokens:radarID:requesterPlayerID:"
+ "is-challengeable"
+ "isChallengeable"
+ "localPlayerIsUnderage"
+ "requesterPlayerID"
+ "scheduled-end-timestamp"
+ "scheduledEndDate"
+ "setChallengeVendorID:"
+ "setIsChallengeable:"
+ "setRequesterPlayerID:"
+ "setScheduledEndDate:"
+ "setSupportsMultiplayerActivities:"
+ "supports-multiplayer-activities"
+ "supportsMultiplayerActivities"
- "@\"GKPlayerInternal\"16@0:8"
- "T@\"GKPlayerInternal\",R"
- "T@\"NSString\",&,N,V_requesterAlias"
- "_requesterAlias"
- "initWithPlayersAndPushTokens:radarID:requesterAlias:"
- "localPlayerInternal"
- "setRequesterAlias:"

```
