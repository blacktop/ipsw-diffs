## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.1.10.0.0
-  __TEXT.__text: 0x168dac
+820.1.13.0.0
+  __TEXT.__text: 0x16935c
   __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_methlist: 0x12214
-  __TEXT.__cstring: 0x19873
+  __TEXT.__objc_methlist: 0x122ac
+  __TEXT.__cstring: 0x198c3
   __TEXT.__const: 0x5bc0
   __TEXT.__gcc_except_tab: 0x1450
   __TEXT.__oslogstring: 0xda1b

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x6520
+  __TEXT.__unwind_info: 0x6540
   __TEXT.__eh_frame: 0x54c8
-  __TEXT.__objc_classname: 0x1ec0
-  __TEXT.__objc_methname: 0x26e1d
-  __TEXT.__objc_methtype: 0x62f1
-  __TEXT.__objc_stubs: 0x14ea0
-  __DATA_CONST.__got: 0x10f0
-  __DATA_CONST.__const: 0x6050
-  __DATA_CONST.__objc_classlist: 0x818
+  __TEXT.__objc_classname: 0x1ed2
+  __TEXT.__objc_methname: 0x2701f
+  __TEXT.__objc_methtype: 0x63fc
+  __TEXT.__objc_stubs: 0x14ee0
+  __DATA_CONST.__got: 0x10f8
+  __DATA_CONST.__const: 0x6058
+  __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84e0
+  __DATA_CONST.__objc_selrefs: 0x8528
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x500
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1498
-  __AUTH_CONST.__const: 0x5910
-  __AUTH_CONST.__cfstring: 0x11380
-  __AUTH_CONST.__objc_const: 0x24978
+  __AUTH_CONST.__const: 0x5930
+  __AUTH_CONST.__cfstring: 0x11420
+  __AUTH_CONST.__objc_const: 0x24b50
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x2c58
+  __AUTH.__objc_data: 0x2ca8
   __AUTH.__data: 0x1150
-  __DATA.__objc_ivar: 0x102c
+  __DATA.__objc_ivar: 0x103c
   __DATA.__data: 0x39c0
-  __DATA.__bss: 0x8200
+  __DATA.__bss: 0x8210
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2b78
   __DATA_DIRTY.__data: 0x5b8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EBD76902-CF45-383A-B521-FFC9BCE8B50D
-  Functions: 10815
-  Symbols:   24606
-  CStrings:  13590
+  UUID: A59E9C54-4BDC-3EF0-BD74-7804E385C399
+  Functions: 10827
+  Symbols:   24646
+  CStrings:  13623
 
Symbols:
+ +[GKGameGenre secureCodedPropertyKeys]
+ +[GKGameGenre secureCodedPropertyKeys].cold.1
+ +[NSError(gamed) gkInternalErrorWithCode:andDetails:]
+ -[GKAppMetadata gkGameGenres]
+ -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:]
+ -[GKGameGenre .cxx_destruct]
+ -[GKGameGenre description]
+ -[GKGameGenre genreID]
+ -[GKGameGenre initWithGenreID:name:parentID:]
+ -[GKGameGenre name]
+ -[GKGameGenre parentID]
+ _GKReporterGamesMappingTopic
+ _OBJC_CLASS_$_GKGameGenre
+ _OBJC_IVAR_$_GKAppMetadata._gkGameGenres
+ _OBJC_IVAR_$_GKGameGenre._genreID
+ _OBJC_IVAR_$_GKGameGenre._name
+ _OBJC_IVAR_$_GKGameGenre._parentID
+ _OBJC_METACLASS_$_GKGameGenre
+ __OBJC_$_CLASS_METHODS_GKGameGenre
+ __OBJC_$_CLASS_METHODS_NSError(GameKitErrors|GameKitInternal|gamed|GKServerError|GKGameSessionError)
+ __OBJC_$_INSTANCE_METHODS_GKGameGenre
+ __OBJC_$_INSTANCE_METHODS_NSError(GameKitErrors|GameKitInternal|gamed|GKServerError|GKGameSessionError)
+ __OBJC_$_INSTANCE_VARIABLES_GKGameGenre
+ __OBJC_$_PROP_LIST_GKGameGenre
+ __OBJC_CLASS_RO_$_GKGameGenre
+ __OBJC_METACLASS_RO_$_GKGameGenre
+ ___38+[GKGameGenre secureCodedPropertyKeys]_block_invoke
+ _objc_msgSend$genreID
+ _objc_msgSend$parentID
+ _secureCodedPropertyKeys.onceToken.170
+ _secureCodedPropertyKeys.sSecureCodedKeys.169
- -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:]
- __OBJC_$_CLASS_METHODS_NSError(GameKitErrors|GameKitInternal|GKServerError|GKGameSessionError)
- __OBJC_$_INSTANCE_METHODS_NSError(GameKitErrors|GameKitInternal|GKServerError|GKGameSessionError)
CStrings:
+ "%@: genreID: %@, name: %@, parentID: %@"
+ "@176@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160@168"
+ "GKGameGenre"
+ "T@\"NSArray\",R,N,V_gkGameGenres"
+ "T@\"NSString\",R,C,N,V_genreID"
+ "T@\"NSString\",R,C,N,V_parentID"
+ "Vv48@0:8q16q24q32@?40"
+ "Vv48@0:8q16q24q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
+ "Vv56@0:8@\"NSString\"16q24q32q40@?<v@?@\"NSArray\"q@\"NSError\">48"
+ "Vv56@0:8@16@24@32@40@48"
+ "Vv56@0:8@16q24q32q40@?48"
+ "Vv60@0:8@\"NSArray\"16@\"NSArray\"24q32q40B48@?<v@?@\"NSDictionary\"@\"NSError\">52"
+ "Vv60@0:8@16@24q32q40B48@?52"
+ "_genreID"
+ "_gkGameGenres"
+ "_parentID"
+ "genreID"
+ "getAppMetadataForBundleIDs:adamIDs:ttlOption:environment:localDataOnly:withCompletion:"
+ "getNicknameSuggestions:minSuggestionLength:maxSuggestionLength:handler:"
+ "gkGameGenres"
+ "gkInternalErrorWithCode:andDetails:"
+ "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:"
+ "initWithDouble:"
+ "initWithGenreID:name:parentID:"
+ "parentID"
+ "postGamesMapEventWithGamesUserID:gameCenterUserID:actionType:hostAppBundleId:additionalFields:"
+ "setPlayerNickname:suggestionsCount:minSuggestionLength:maxSuggestionLength:handler:"
+ "xp_ase_games_mapping"
- "@168@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160"
- "Vv56@0:8@\"NSArray\"16@\"NSArray\"24q32q40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "Vv56@0:8@16@24q32q40@?48"
- "getAppMetadataForBundleIDs:adamIDs:ttlOption:environment:withCompletion:"
- "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:"

```
