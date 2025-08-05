## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.0.70.0.0
-  __TEXT.__text: 0x166c64
+820.0.75.0.0
+  __TEXT.__text: 0x1671cc
   __TEXT.__auth_stubs: 0x27e0
-  __TEXT.__objc_methlist: 0x120ec
-  __TEXT.__cstring: 0x19753
+  __TEXT.__objc_methlist: 0x1215c
+  __TEXT.__cstring: 0x197b3
   __TEXT.__const: 0x5b70
   __TEXT.__gcc_except_tab: 0x1450
   __TEXT.__oslogstring: 0xd9eb

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x64b8
+  __TEXT.__unwind_info: 0x64c0
   __TEXT.__eh_frame: 0x5480
   __TEXT.__objc_classname: 0x1ea9
-  __TEXT.__objc_methname: 0x26b6c
-  __TEXT.__objc_methtype: 0x62d0
-  __TEXT.__objc_stubs: 0x14e20
+  __TEXT.__objc_methname: 0x26d2d
+  __TEXT.__objc_methtype: 0x62dc
+  __TEXT.__objc_stubs: 0x14e40
   __DATA_CONST.__got: 0x10c8
-  __DATA_CONST.__const: 0x6058
+  __DATA_CONST.__const: 0x6048
   __DATA_CONST.__objc_classlist: 0x808
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8470
+  __DATA_CONST.__objc_selrefs: 0x84b8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4f8
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1400
-  __AUTH_CONST.__const: 0x57a8
-  __AUTH_CONST.__cfstring: 0x11260
-  __AUTH_CONST.__objc_const: 0x245c0
+  __AUTH_CONST.__const: 0x5888
+  __AUTH_CONST.__cfstring: 0x11300
+  __AUTH_CONST.__objc_const: 0x24720
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2b48
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0x100c
+  __DATA.__objc_ivar: 0x101c
   __DATA.__data: 0x3970
-  __DATA.__bss: 0x8360
+  __DATA.__bss: 0x82e0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2b78
   __DATA_DIRTY.__data: 0x598
-  __DATA_DIRTY.__bss: 0xa18
+  __DATA_DIRTY.__bss: 0xa98
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91B39D31-9316-33CD-A615-775105EBF15F
-  Functions: 10748
-  Symbols:   24515
-  CStrings:  13539
+  UUID: F35906BC-2E4F-3FF7-93EB-61B2F5A90EA8
+  Functions: 10761
+  Symbols:   24535
+  CStrings:  13565
 
Symbols:
+ -[GKAppMetadata gameDisplayName]
+ -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:]
+ -[GKAppMetadata isGameGenre]
+ -[GKAppMetadata miniGamesDeepLink]
+ -[GKGameActivityEventHandler attemptFallbackForActivity:]
+ -[GKGameActivityEventHandler attemptFallbackForActivity:].cold.1
+ -[GKGameActivityEventHandler attemptFallbackForActivity:].cold.2
+ -[GKLeaderboardChallengeSummaryInternal completedChallenges]
+ -[GKLeaderboardChallengeSummaryInternal setCompletedChallenges:]
+ _GKGameGenreID
+ _GKRemoteAlertDeeplinkActionSystemSettingsValue
+ _OBJC_IVAR_$_GKAppMetadata._gameDisplayName
+ _OBJC_IVAR_$_GKAppMetadata._isGameGenre
+ _OBJC_IVAR_$_GKAppMetadata._miniGamesDeepLink
+ _OBJC_IVAR_$_GKLeaderboardChallengeSummaryInternal._completedChallenges
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.779
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780.cold.2
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780.cold.3
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780.cold.4
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.780.cold.5
+ ___block_literal_global.551
+ ___block_literal_global.583
+ ___block_literal_global.589
+ ___block_literal_global.603
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_GameCenterFoundation
+ _objc_msgSend$attemptFallbackForActivity:
+ _secureCodedPropertyKeys.onceToken.581
+ _secureCodedPropertyKeys.onceToken.601
+ _secureCodedPropertyKeys.sSecureCodedKeys.580
+ _secureCodedPropertyKeys.sSecureCodedKeys.600
- -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:]
- -[GKGameActivityEventHandler receivedGKGameActivityNotification:].cold.3
- -[GKGameActivityEventHandler receivedGKGameActivityNotification:].cold.4
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.778
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779.cold.2
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779.cold.3
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779.cold.4
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.779.cold.5
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_literal_global.539
- ___block_literal_global.571
- ___block_literal_global.577
- ___block_literal_global.591
- _secureCodedPropertyKeys.onceToken.537
- _secureCodedPropertyKeys.onceToken.569
- _secureCodedPropertyKeys.onceToken.589
- _secureCodedPropertyKeys.sSecureCodedKeys.536
- _secureCodedPropertyKeys.sSecureCodedKeys.568
- _secureCodedPropertyKeys.sSecureCodedKeys.588
CStrings:
+ "6014"
+ "@\"RBSAssertion\""
+ "@160@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152"
+ "T@\"NSNumber\",R,C,N,V_isGameGenre"
+ "T@\"NSNumber\",R,N,V_isIOSBinaryMacOSCompatible"
+ "T@\"NSString\",R,C,N,V_gameDisplayName"
+ "T@\"NSString\",R,C,N,V_miniGamesDeepLink"
+ "_gameDisplayName"
+ "_isGameGenre"
+ "_miniGamesDeepLink"
+ "attemptFallbackForActivity:"
+ "deep-link-system-settings"
+ "gameDisplayName"
+ "healthCheck:"
+ "initWithBool:"
+ "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:"
+ "isGameGenre"
+ "launchOverlaySystemSettingsForGameBundleId:"
+ "miniGamesDeepLink"
+ "readGameMetadataForBundleIDs:wihCompletion:"
+ "readGamesPlayedSummaries:limit:wihCompletion:"
- "@132@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120B128"
- "TB,R,N,V_isIOSBinaryMacOSCompatible"
- "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:"

```
