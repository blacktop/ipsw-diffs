## FMF

> `/System/Library/PrivateFrameworks/FMF.framework/Versions/A/FMF`

```diff

-508.23.10.29.2
-  __TEXT.__text: 0x28790
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2334
+508.24.7.11.12
+  __TEXT.__text: 0x242bc
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x2cd4
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__cstring: 0x1eca
-  __TEXT.__oslogstring: 0x1f40
+  __TEXT.__gcc_except_tab: 0x700
+  __TEXT.__cstring: 0x1cd5
+  __TEXT.__oslogstring: 0x1857
   __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0xae0
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x6985
+  __TEXT.__objc_methname: 0x6976
   __TEXT.__objc_methtype: 0x15eb
-  __TEXT.__objc_stubs: 0x5160
+  __TEXT.__objc_stubs: 0x4cc0
   __DATA_CONST.__got: 0x308
   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1950
+  __DATA_CONST.__objc_selrefs: 0x1a20
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0x240
-  __AUTH_CONST.__const: 0xe20
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0xc70
   __AUTH_CONST.__cfstring: 0x1e00
-  __AUTH_CONST.__objc_const: 0x55f0
+  __AUTH_CONST.__objc_const: 0x4368
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x378

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B992D13-0D35-3B1E-8ED2-B4583B2B93A8
-  Functions: 1023
-  Symbols:   2545
-  CStrings:  2147
+  UUID: 0D8AE0D9-78F3-32A1-BD9D-C44D377E4453
+  Functions: 958
+  Symbols:   2435
+  CStrings:  2095
 
Symbols:
+ +[FMFContactUtility sharedInstance].cold.1
+ +[FMFSessionDataManager sharedInstance].cold.1
+ -[FMFHandle cachedPrettyName].cold.1
+ -[FMFHandle prettyNameWithCompletion:].cold.1
+ -[FMFMapCache cacheExpiryInSeconds].cold.1
+ -[FMFMapCache pruneIntervalInSeconds].cold.1
+ -[FMFSchedule _daysOfWeek].cold.1
+ -[FMFSession initWithDelegate:delegateQueue:].cold.1
+ LogCategory_Daemon.cold.1
+ LogCategory_FMFMapXPC.cold.1
+ __51-[FMFSession(Admin) getHandlesFollowingMyLocation:]_block_invoke.25
+ __55-[FMFSession(Notifications) dataForPayload:completion:]_block_invoke.1
+ __86-[FMFSession(Establish) stopSharingMyLocationWithHandles:groupId:callerId:completion:]_block_invoke.14
+ __86-[FMFSession(Establish) stopSharingMyLocationWithHandles:groupId:callerId:completion:]_block_invoke_2.15
+ __block_literal_global.522
+ initACAccountStore.cold.1
- -[FMFSession(Establish) approveFriendshipRequest:completion:].cold.1
- -[FMFSession(Establish) declineFriendshipRequest:completion:].cold.1
- -[FMFSession(Establish) extendFriendshipOfferToHandle:groupId:callerId:endDate:completion:].cold.1
- -[FMFSession(Establish) sendNotNowToHandle:callerId:completion:].cold.1
- _NSStringFromSelector
- __32-[FMFSession(Fences) getFences:]_block_invoke.9
- __42-[FMFSession(Fences) addFence:completion:]_block_invoke.1
- __45-[FMFSession(Fences) deleteFence:completion:]_block_invoke.3
- __48-[FMFSession(Favorites) addFavorite:completion:]_block_invoke.3
- __50-[FMFSession(Fences) fencesForHandles:completion:]_block_invoke.13
- __51-[FMFSession(Admin) getHandlesFollowingMyLocation:]_block_invoke.28
- __51-[FMFSession(Favorites) removeFavorite:completion:]_block_invoke.9
- __52-[FMFSession(Favorites) getFavoritesWithCompletion:]_block_invoke.1
- __55-[FMFSession(Notifications) dataForPayload:completion:]_block_invoke.7
- __55-[FMFSession(Notifications) encryptPayload:completion:]_block_invoke.15
- __57-[FMFSession(TodayWidget) nearbyLocationsWithCompletion:]_block_invoke.5
- __58-[FMFSession(Notifications) contactForPayload:completion:]_block_invoke.1
- __58-[FMFSession(Notifications) contactForPayload:completion:]_block_invoke.cold.1
- __59-[FMFSession(TodayWidget) favoritesForMaxCount:completion:]_block_invoke.1
- __65-[FMFSession(Notifications) decryptPayload:withToken:completion:]_block_invoke.11
- __68-[FMFSession(Notifications) handleAndLocationForPayload:completion:]_block_invoke.3
- __68-[FMFSession(Notifications) handleAndLocationForPayload:completion:]_block_invoke.cold.1
- __73-[FMFSession(Admin) canGetLocationForHandle:groupId:callerId:completion:]_block_invoke.43
- __73-[FMFSession(Admin) getHandlesFollowingMyLocationWithGroupId:completion:]_block_invoke.29
- __76-[FMFSession(Admin) canShareLocationWithHandle:groupId:callerId:completion:]_block_invoke.39
- __76-[FMFSession(Admin) getHandlesSharingLocationsWithMeWithGroupId:completion:]_block_invoke.25
- __86-[FMFSession(Establish) stopSharingMyLocationWithHandles:groupId:callerId:completion:]_block_invoke.16
- __86-[FMFSession(Establish) stopSharingMyLocationWithHandles:groupId:callerId:completion:]_block_invoke_2.17
- __91-[FMFSession(Establish) extendFriendshipOfferToHandle:groupId:callerId:endDate:completion:]_block_invoke.10
- ___32-[FMFSession(Fences) getFences:]_block_invoke
- ___42-[FMFSession(Fences) addFence:completion:]_block_invoke
- ___44-[FMFSession(Admin) getAccountEmailAddress:]_block_invoke
- ___44-[FMFSession(Admin) getAccountEmailAddress:]_block_invoke_2
- ___45-[FMFSession(Fences) deleteFence:completion:]_block_invoke
- ___48-[FMFSession(Favorites) addFavorite:completion:]_block_invoke
- ___49-[FMFSession(Admin) getHandlesWithPendingOffers:]_block_invoke
- ___49-[FMFSession(Admin) getHandlesWithPendingOffers:]_block_invoke_2
- ___50-[FMFSession handleIncomingAirDropURL:completion:]_block_invoke
- ___50-[FMFSession(Admin) isAllowFriendRequestsEnabled:]_block_invoke
- ___50-[FMFSession(Admin) isAllowFriendRequestsEnabled:]_block_invoke_2
- ___50-[FMFSession(Fences) fencesForHandles:completion:]_block_invoke
- ___51-[FMFSession(Favorites) removeFavorite:completion:]_block_invoke
- ___52-[FMFSession(Favorites) getFavoritesWithCompletion:]_block_invoke
- ___55-[FMFSession(Notifications) encryptPayload:completion:]_block_invoke
- ___57-[FMFSession(TodayWidget) nearbyLocationsWithCompletion:]_block_invoke
- ___58-[FMFSession(Notifications) contactForPayload:completion:]_block_invoke
- ___59-[FMFSession(TodayWidget) favoritesForMaxCount:completion:]_block_invoke
- ___61-[FMFSession(Establish) approveFriendshipRequest:completion:]_block_invoke
- ___61-[FMFSession(Establish) approveFriendshipRequest:completion:]_block_invoke_2
- ___61-[FMFSession(Establish) declineFriendshipRequest:completion:]_block_invoke
- ___61-[FMFSession(Establish) declineFriendshipRequest:completion:]_block_invoke_2
- ___61-[FMFSession(Establish) declineFriendshipRequest:completion:]_block_invoke_3
- ___62-[FMFSession(Admin) setAllowFriendRequestsEnabled:completion:]_block_invoke
- ___62-[FMFSession(Admin) setAllowFriendRequestsEnabled:completion:]_block_invoke_2
- ___63-[FMFSession(Fences) muteFencesForHandle:untilDate:completion:]_block_invoke
- ___63-[FMFSession(Fences) muteFencesForHandle:untilDate:completion:]_block_invoke_2
- ___64-[FMFSession(Establish) sendNotNowToHandle:callerId:completion:]_block_invoke
- ___64-[FMFSession(Establish) sendNotNowToHandle:callerId:completion:]_block_invoke_2
- ___65-[FMFSession(Notifications) decryptPayload:withToken:completion:]_block_invoke
- ___68-[FMFSession(Establish) getPendingFriendshipRequestsWithCompletion:]_block_invoke
- ___68-[FMFSession(Establish) getPendingFriendshipRequestsWithCompletion:]_block_invoke_2
- ___68-[FMFSession(Notifications) handleAndLocationForPayload:completion:]_block_invoke
- ___73-[FMFSession(Admin) canGetLocationForHandle:groupId:callerId:completion:]_block_invoke
- ___73-[FMFSession(Admin) getHandlesFollowingMyLocationWithGroupId:completion:]_block_invoke
- ___74-[FMFSession(Admin) getPendingMappingPacketsForHandle:groupId:completion:]_block_invoke
- ___74-[FMFSession(Admin) getPendingMappingPacketsForHandle:groupId:completion:]_block_invoke_2
- ___76-[FMFSession(Admin) canShareLocationWithHandle:groupId:callerId:completion:]_block_invoke
- ___76-[FMFSession(Admin) getHandlesSharingLocationsWithMeWithGroupId:completion:]_block_invoke
- ___76-[FMFSession(Locate) refreshLocationForHandle:callerId:priority:completion:]_block_invoke
- ___76-[FMFSession(Locate) refreshLocationForHandle:callerId:priority:completion:]_block_invoke_2
- ___77-[FMFSession(Admin) getOfferExpirationForHandle:groupId:callerId:completion:]_block_invoke
- ___77-[FMFSession(Admin) getOfferExpirationForHandle:groupId:callerId:completion:]_block_invoke_2
- ___83-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:completion:]_block_invoke
- ___83-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:completion:]_block_invoke_2
- ___91-[FMFSession(Establish) extendFriendshipOfferToHandle:groupId:callerId:endDate:completion:]_block_invoke
- ___91-[FMFSession(Establish) extendFriendshipOfferToHandle:groupId:callerId:endDate:completion:]_block_invoke_2
- ___99-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:triggerLocation:completion:]_block_invoke
- ___99-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:triggerLocation:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSDate"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"FMFFence"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e31_v24?0"CNContact"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e33_v28?0B8"NSString"12"NSError"20l
- ___block_descriptor_48_e8_32s40bs_e37_v32?0"NSSet"8"NSSet"16"NSError"24l
- ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24l
- ___block_descriptor_48_e8_32s40bs_e46_v32?0"FMFHandle"8"CLLocation"16"NSError"24l
- ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSSet"8"NSError"16l
- __block_literal_global.524
- _objc_msgSend$absoluteString
- _objc_msgSend$addFavorite:completion:
- _objc_msgSend$addFence:completion:
- _objc_msgSend$approveFriendshipRequest:completion:
- _objc_msgSend$canGetLocationForHandle:groupId:callerId:completion:
- _objc_msgSend$canOfferToHandles:completion:
- _objc_msgSend$canShareLocationWithHandle:groupId:callerId:completion:
- _objc_msgSend$contactForPayload:completion:
- _objc_msgSend$declineFriendshipRequest:completion:
- _objc_msgSend$decryptPayload:withToken:completion:
- _objc_msgSend$deleteFence:completion:
- _objc_msgSend$encryptPayload:completion:
- _objc_msgSend$extendFriendshipOfferToHandle:groupId:callerId:endDate:completion:
- _objc_msgSend$fencesForHandles:completion:
- _objc_msgSend$fetchLocationForHandle:callerId:priority:completion:
- _objc_msgSend$getAccountEmailAddress:
- _objc_msgSend$getAllLocations:
- _objc_msgSend$getFavoritesWithCompletion:
- _objc_msgSend$getFences:
- _objc_msgSend$getHandlesFollowingMyLocation:
- _objc_msgSend$getHandlesSharingLocationsWithMeWithGroupId:completion:
- _objc_msgSend$getHandlesSharingMyLocationWithGroupId:completion:
- _objc_msgSend$getOfferExpirationForHandle:groupId:callerId:completion:
- _objc_msgSend$getPendingFriendshipRequestsWithCompletion:
- _objc_msgSend$getPendingMappingPacketsForHandle:groupId:completion:
- _objc_msgSend$handleAndLocationForPayload:completion:
- _objc_msgSend$isAllowFriendRequestsEnabled:
- _objc_msgSend$muteFencesForHandle:untilDate:completion:
- _objc_msgSend$nearbyLocationsWithCompletion:
- _objc_msgSend$receivedMappingPacket:completion:
- _objc_msgSend$removeFavorite:completion:
- _objc_msgSend$sendNotNowToHandle:callerId:completion:
- _objc_msgSend$setAllowFriendRequestsEnabled:completion:
- _objc_msgSend$showAirDropImportAlertForId:
- _objc_msgSend$showAirDropImportErrorAlert
- _objc_msgSend$triggerWithUUID:forFenceWithID:withStatus:forDate:completion:
- _objc_msgSend$triggerWithUUID:forFenceWithID:withStatus:forDate:triggerLocation:completion:
CStrings:
- "%@ %@"
- "%s: %@ fenceID: %@ status: %@"
- "%s: %@ fenceID: %@ status: %@ with trigger location"
- "%s: %@ handle: %@ date: %@"
- "-[FMFSession(Fences) muteFencesForHandle:untilDate:completion:]"
- "-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:completion:]"
- "-[FMFSession(Fences) triggerWithUUID:forFenceWithID:withStatus:forDate:triggerLocation:completion:]"
- "Approving friend request for: %@"
- "Can get location %d"
- "Can share location %d"
- "Declining friend request for: %@"
- "Error occured when decryptPayload %@"
- "Error occured when encryptPayload: %@"
- "Error occured when getting contact for payload %@"
- "Error occured when getting handle and location for payload %@"
- "Extending friend offer for: %@ to date: %@"
- "FMFSession: %@ addFavorite: %@"
- "FMFSession: %@ addFence: %@"
- "FMFSession: %@ deleteFence: %@"
- "FMFSession: %@ fenceForHandles: %@"
- "FMFSession: %@ getFavoritesWithCompletion"
- "FMFSession: %@ removeFavorite: %@"
- "FMFSession: addFavorite completed with error: %@"
- "FMFSession: addFences result: error? %@, fences: %@"
- "FMFSession: deleteFence result: error? %@"
- "FMFSession: fenceForHandles result: error? %@, fences: %@"
- "FMFSession: getFavorites: %@"
- "FMFSession: getFavoritesWithCompletion completed with error: %@"
- "FMFSession: getFences result: error? %@, fences: %@"
- "FMFSession: getFences: %@"
- "FMFSession: removeFavorite completed with error: %@"
- "Get pending friendship requests"
- "Handles following my location, through group Id: %@, %@"
- "Handles sharing location with me through group Id: %@, %@"
- "Sending notNow for: %@"
- "Trying to approveFriendshipRequest:completion: when Share My Location is restricted"
- "Trying to declineFriendshipRequest:completion: when Share My Location is restricted"
- "Trying to extendFriendshipOfferToHandle:groupId:callerId:endDate:completion: when Share My Location is restricted"
- "Trying to sendNotNowToHandle:callerId:completion: when Share My Location is restricted"
- "absoluteString"
- "favoritesForMaxCount: %@"
- "getAllLocations"
- "handleIncomingAirDropURL: %@"
- "nearbyLocationsWithCompletion: %@"
- "receivedMappingPacket: completion responseId: %@"
- "v24@?0@\"CNContact\"8@\"NSError\"16"
- "v24@?0@\"FMFFence\"8@\"NSError\"16"
- "v24@?0@\"NSDate\"8@\"NSError\"16"
- "v28@?0B8@\"NSString\"12@\"NSError\"20"
- "v32@?0@\"FMFHandle\"8@\"CLLocation\"16@\"NSError\"24"
- "v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSError\"24"
- "v32@?0@\"NSSet\"8@\"NSSet\"16@\"NSError\"24"

```
