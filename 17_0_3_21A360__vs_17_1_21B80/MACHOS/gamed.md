## gamed

> `/usr/libexec/gamed`

```diff

-818.0.76.2.2
-  __TEXT.__text: 0x20477c
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_stubs: 0x19380
-  __TEXT.__objc_methlist: 0xb488
-  __TEXT.__objc_classname: 0x1e1c
+818.1.10.2.3
+  __TEXT.__text: 0x201b20
+  __TEXT.__auth_stubs: 0x2420
+  __TEXT.__objc_stubs: 0x19460
+  __TEXT.__objc_methlist: 0xb360
+  __TEXT.__objc_classname: 0x1dd9
   __TEXT.__oslogstring: 0xe
-  __TEXT.__cstring: 0x254c4
+  __TEXT.__cstring: 0x24fb4
   __TEXT.__const: 0xea08
-  __TEXT.__gcc_except_tab: 0x3074
-  __TEXT.__objc_methname: 0x1fe29
-  __TEXT.__objc_methtype: 0x5ff6
-  __TEXT.__constg_swiftt: 0x748
-  __TEXT.__swift5_typeref: 0x85d
-  __TEXT.__swift5_fieldmd: 0x5bc
+  __TEXT.__gcc_except_tab: 0x3010
+  __TEXT.__objc_methname: 0x1fed7
+  __TEXT.__objc_methtype: 0x606c
+  __TEXT.__swift5_typeref: 0x871
+  __TEXT.__constg_swiftt: 0x760
+  __TEXT.__swift5_reflstr: 0x5d0
+  __TEXT.__swift5_fieldmd: 0x5d4
   __TEXT.__swift5_types: 0x68
-  __TEXT.__swift5_reflstr: 0x590
   __TEXT.__swift5_capture: 0x3a4
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x67e8
+  __TEXT.__unwind_info: 0x6754
   __TEXT.__eh_frame: 0x1f00
-  __DATA_CONST.__auth_got: 0x1220
-  __DATA_CONST.__got: 0xee8
+  __DATA_CONST.__auth_got: 0x1228
+  __DATA_CONST.__got: 0xf38
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0xf810
-  __DATA_CONST.__cfstring: 0x17080
-  __DATA_CONST.__objc_classlist: 0x820
+  __DATA_CONST.__const: 0xf5f8
+  __DATA_CONST.__cfstring: 0x16d80
+  __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x8a0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x21668
-  __DATA.__objc_selrefs: 0x75b0
+  __DATA.__objc_const: 0x21060
+  __DATA.__objc_selrefs: 0x75b8
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xe30
-  __DATA.__objc_superrefs: 0x538
-  __DATA.__objc_ivar: 0x7c8
-  __DATA.__objc_data: 0x5578
-  __DATA.__data: 0x3328
-  __DATA.__bss: 0xd80
+  __DATA.__objc_classrefs: 0xe20
+  __DATA.__objc_superrefs: 0x518
+  __DATA.__objc_ivar: 0x7b8
+  __DATA.__objc_data: 0x5458
+  __DATA.__data: 0x3340
+  __DATA.__bss: 0xd40
   __DATA.__common: 0xa8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7669
-  Symbols:   1408
-  CStrings:  9606
+  Functions: 7622
+  Symbols:   1419
+  CStrings:  9574
 
Symbols:
+ _GKDashboardLaunchContextAppStore
+ _GKDashboardLaunchContextContacts
+ _GKDashboardLaunchContextGameController
+ _GKDashboardLaunchContextPushNotification
+ _GKDashboardLaunchContextWidget
+ _GKGameScopedIDPrefix
+ _GKMoltresIdentifier
+ _GKMoltresOverlayIdentifier
+ _GKSupportedTransportVersionsKey
+ _GKTeamScopedIDPrefix
+ _objc_loadWeak
CStrings:
+ "-[GKAuthenticationWrapperService authenticatePlayerWithUsername:password:altDSID:isGame:usingFastPath:handler:]"
+ "2\x18\x12\x11\x12\x1f\x01"
+ "@28@0:8B16@20"
+ "Didn't find a perfect compatible game: bundleID = %@, short version = %@, version = %@"
+ "During getAuthenticatedLocalPlayers, modifying the scopedIDs based on the record for the game:%@ (proxy of the game:%@)"
+ "Found perfect compatible game: bundleID = %@, short version = %@, version = %@"
+ "GKGameplayBulletin - skip checking compatibility for app %@, since compatibility matrix is empty."
+ "GKGameplayBulletin - skipping mismatching platform between current = %ld and game = %@. Supported platforms: %@"
+ "GKGameplayBulletin checkCompatibleGameWithoutCompatibilityMatrix"
+ "GKScopedIDs"
+ "GameDaemonCore.NetworkRequestEligibiltyChecker"
+ "No gameBundleID in server response"
+ "Not setting invalid scoped IDs to game record cache object, player: %@, game: %@, team: %@"
+ "Not setting invalid scoped IDs to player cache object, bundle: %@, game: %@, team: %@"
+ "RemoteAlert: openDashboardAsRemoteAlertForGame:%@\n hostPID:%d\n deeplink:%@\n launchContext:%@"
+ "Returning cached gamePlayerId %@ for bundle: %@ and player: %@"
+ "T@\"NSString\",C,N,V_persistentAnchorIdentifier"
+ "TB,V_isGameCenterEnabledClient"
+ "Unknown bundleId attempting to open the dashboard. Use openDashboardAsRemoteAlertForGame:hostPID:deeplink:launchContext: instead: %@"
+ "Vv44@0:8@\"GKGameInternal\"16i24@\"NSDictionary\"28@\"NSString\"36"
+ "Vv44@0:8@16i24@28@36"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?@\"GKAuthenticateResponse\"@\"NSError\">48"
+ "Vv56@0:8@16@24@32B40B44@?48"
+ "[Internal Only] Found invalid transport version for invitation request."
+ "[Internal Only] Found invalid transport version for matchmaking request."
+ "_gkBundleIdentifierIsRelatedToContactsUI:"
+ "_gkDictionaryWithValue:forKey:"
+ "_isGameCenterEnabledClient"
+ "_issueRequest:bagKey:clientProxy:locale:handler:"
+ "_persistentAnchorIdentifier"
+ "alwaysAllowedBagKeys"
+ "authenticatePlayerWithUsername:password:altDSID:isGame:usingFastPath:handler:"
+ "authenticateWithService:username:password:altDSID:isGame:usingFastPath:displayAuthUI:handler:"
+ "checkCompatibleGameWithoutCompatibilityMatrix"
+ "clientHasAnyPrivateEntitlement"
+ "game-bundle-id"
+ "gamePlayerIDForBundleID:"
+ "gamePlayerIDForPlayerID:"
+ "gk-allowed-pregdpr-requests"
+ "handleNewHostClient:"
+ "initWithHasAcknowledgedLatestGDPR:alwaysAllowedBagKeysObject:"
+ "initWithSanitizeBeforeEncodingBlock:"
+ "isEligibleWithBagKey:"
+ "isGKCompoundError"
+ "isGameCenterDisabled"
+ "isGameCenterEnabledClient"
+ "isRequestKeyAllowed:checkingAllowedRequestKeys:"
+ "isRequestKeyAllowed:replyQueue:completion:"
+ "launchBypassingPreAuthentication:forGame:hostPID:deeplink:launchContext:observer:"
+ "nextObject"
+ "openDashboardAsRemoteAlertForGame:hostPID:deeplink:launchContext:"
+ "persistentAnchorIdentifier"
+ "sanitize"
+ "setGameBundleID:gamePlayerID:teamPlayerID:"
+ "setGamePlayerID:teamPlayerID:"
+ "setIsGameCenterEnabledClient:"
+ "setPersistentAnchorIdentifier:"
+ "stringForPlatform:"
+ "supportedPlatforms"
+ "supportsPlatform:"
+ "teamPlayerIDForBundleID:"
+ "teamPlayerIDForPlayerID:"
+ "v68@0:8@16@24@32@40B48B52B56@?60"
+ "validateRequests:andFileMultiplayerTTRIfNeededWithContext:"
+ "\xf0q"
- "%@ (hostClient != nil)\n[%s (%s:%d)]"
- "%@ didn't implement %@"
- "-[GKAuthenticationWrapperService authenticatePlayerWithUsername:password:altDSID:usingFastPath:handler:]"
- "-[GKExtensionClientProxy setHostPID:reply:]"
- "-[GKUIServiceClientProxy setHostPID:reply:]"
- "2\x18\x11\x11\x12\x1f\x01"
- "@32@0:8@16q24"
- "Associating extension %@ with client %@ : pid(%d)"
- "Avoiding redundant load for %@"
- "B28@0:8@16B24"
- "During app init, this game is not recognized by the server and scoped IDs are being marked as Unavailable"
- "During getAuthenticatedLocalPlayers, modifying the scopedIDs based on the record for the game:%@ (proxy of the game:%@) for player:%@ gamePlayerID:%@"
- "GKCacheReader"
- "GKDataCacheName"
- "GKDatabaseConnectionFactory"
- "GKDelayedRequestCacheName"
- "GKEnvironmentCustom"
- "GKEnvironmentProduction"
- "GKEnvironmentTD1"
- "GKEnvironmentTD2"
- "GKEnvironmentTD3"
- "GKEnvironmentTD4"
- "GKEnvironmentUninitialized"
- "GKGameplayBulletin - skipping mismatching platform between current = %ld and game = %@"
- "GKGameplayBulletin determineGameLocationOnDeviceOnly"
- "GKIDSRequestManager"
- "GKIDSRequestManager responseDictionaryQueue"
- "GKIDSRequestManager sharedManager"
- "GKProcessedResourceKeyTTL"
- "GKRequestDeduper"
- "No gamePlayerID in response"
- "No teamPlayerID in response"
- "RemoteAlert: openDashboardAsRemoteAlertForGame:%@ hostPID:%d deeplink:%@"
- "Request(%@) completed for resources %@"
- "Request(%@) opened for resources %@"
- "Returning cached gamePlayerId %@ for player: %@"
- "ScopedIDs loaded into credential %@ %@ for game: %@"
- "T@\"GKDispatchGroup\",&,N,V_dispatchGroup"
- "T@\"GKThreadsafeDictionary\",&,N,V_processedResources"
- "T@\"NSMutableDictionary\",&,V_idsRequests"
- "T@\"NSString\",C,N,V_databasePath"
- "T@\"NSString\",C,N,V_poolName"
- "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "_dispatchGroup"
- "_idsRequests"
- "_poolName"
- "_processedResources"
- "authenticateWithService:username:password:altDSID:usingFastPath:displayAuthUI:handler:"
- "authenticateWithService:username:password:altDSID:usingFastPath:handler:"
- "com.apple.gamecenter.GKRequestDeduper.%@"
- "com.apple.gamecenter.GKRequestDeduper.%p.processedResults"
- "com.apple.gamecenter.GKRequestDeduper.requestPools"
- "com.apple.gamed.GKIDSRequestManager.dictionary.queue"
- "connectionForReaderWithName:"
- "connectionForWriterWithName:"
- "deduper"
- "deduperForPool:"
- "defaultPool"
- "determineGameLocationOnDeviceOnly"
- "directoryForEnvironment:"
- "enter"
- "factoryWithDatabaseName:environment:"
- "found compatible app: bundleID = %@, short version = %@, version = %@"
- "getTransactionPool:"
- "idsRequests"
- "initWithPath:"
- "initWithPool:"
- "isEligibleWithBagKey:hasAcknowledgedLatestGDPR:"
- "launchBypassingPreAuthentication:forGame:hostPID:deeplink:observer:"
- "leave"
- "namedPool.%@"
- "openRequestForResources:processCallback:"
- "pathForDatabaseName:environment:"
- "platformStringForServerRequest:"
- "poolName"
- "processedResources"
- "readResources:inDatabase:statementStore:handler:"
- "requestGKPlayerIDForiCloudIDs:withHandler:"
- "requestGKPlayerIDforiCloud:handler:"
- "requestGKPlayerIDforiCloudIDs:handler:"
- "responseDictionaryQueue"
- "scoped:not updating gamePlayerID as it is not currently part of the response of get-games-played. Current value in the game record is:%@"
- "scoped:not updating teamPlayerID as it is not currently part of the response of get-games-played. Current value in the game record is:%@"
- "scoped:not updating the scoped IDs for non local players"
- "scoped:updateIDsWithServerRepresentation Updated gamePlayerID in the cached gameRecord for the localPlayer. Current value in the game record is:%@\n and cached localPlayer:%@"
- "scoped:updateIDsWithServerRepresentation Updated teamPlayerID in the cached gameRecord for the localPlayer. Current value in the game record is teamPlayerID:%@\n and cached localPlayer:%@"
- "scoped:updateWithServerRepresentation Updated gamePlayerID in the cached gameRecord for for the localPlayer. Current value in the game record is:%@\n and cached localPlayer:%@"
- "scoped:updateWithServerRepresentation Updated teamPlayerID in the cached gameRecord for the localPlayer. Current value in the game record is teamPlayerID:%@\n and cached localPlayer:%@"
- "setDispatchGroup:"
- "setIdsRequests:"
- "setPoolName:"
- "setProcessedResources:"
- "stripPIIs"
- "v16@?0@\"GKThreadsafeDictionary\"8"
- "v24@?0@\"GKRequestDeduper\"8^B16"
- "v28@?0@\"NSString\"8@\"NSError\"16B24"
- "v48@0:8@16^{sqlite3=}24@32@?40"
- "v60@0:8@16@24@32@40B48@?52"
- "\xf0a"

```
