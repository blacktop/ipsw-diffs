## HomeMessagingUtils

> `/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils`

```diff

-304.4.1.0.0
-  __TEXT.__text: 0x73e8
-  __TEXT.__auth_stubs: 0x7b0
+314.0.0.0.0
+  __TEXT.__text: 0x761c
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x7d4
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x4b9
+  __TEXT.__cstring: 0x3bd
   __TEXT.__swift5_typeref: 0x1b6
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x164

   __TEXT.__swift5_types: 0x8
   __TEXT.__oslogstring: 0x99
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x150f
-  __TEXT.__objc_methtype: 0x414
-  __TEXT.__objc_stubs: 0xc60
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x378
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__objc_classname: 0x12f
+  __TEXT.__objc_methname: 0x1701
+  __TEXT.__objc_methtype: 0x423
+  __TEXT.__objc_stubs: 0xf40
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0xa40
   __AUTH.__objc_data: 0x1f8
-  __AUTH.__data: 0x120
-  __DATA.__data: 0x3d0
+  __AUTH.__data: 0x118
+  __DATA.__data: 0x3c0
   __DATA.__bss: 0x10
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 445184F6-B1D6-357A-9569-1013D212D42E
+  UUID: 7F15B14B-24C9-317C-A22C-A595F98ABF0D
   Functions: 228
-  Symbols:   730
+  Symbols:   745
   CStrings:  375
 
Symbols:
+ _objc_msgSend$createAccessorySettingsDataSource
+ _objc_msgSend$currentAccessory
+ _objc_msgSend$currentHome
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$descriptorForRequiredKeysForStyle:
+ _objc_msgSend$hmu_isEmail
+ _objc_msgSend$hmu_isPhoneNumber
+ _objc_msgSend$init
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithOptions:cachePolicy:
+ _objc_msgSend$initWithStringValue:
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$predicateForContactsMatchingEmailAddress:
+ _objc_msgSend$predicateForContactsMatchingPhoneNumber:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDelegateQueue:
+ _objc_msgSend$setDiscretionary:
+ _objc_msgSend$setInactiveUpdatingLevel:
+ _objc_msgSend$setStyle:
+ _objc_msgSend$stringFromContact:
+ _objc_msgSend$style
+ _objc_msgSend$unifiedContactsMatchingPredicate:keysToFetch:error:
+ _objc_msgSend$userID
+ _objc_retain_x25
+ _objc_retain_x27
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_HomeMessagingUtils
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x4
Functions:
~ -[IDSService(HMUValidation) hmu_validateFromID:context:currentAccessory:home:options:error:] : 588 -> 624
~ -[IDSService(HMUValidation) hmu_validateDestination:forHome:currentAccessory:options:error:] : 544 -> 560
~ -[NSString(HMUAdditions) hmu_isPhoneNumber] : 212 -> 232
~ ___37-[NSString(HMUAdditions) hmu_isEmail]_block_invoke : 92 -> 96
~ -[HMZone(HMUAdditions) hmu_accessories] : 116 -> 128
~ ___39-[HMZone(HMUAdditions) hmu_accessories]_block_invoke_2 : 8 -> 56
~ -[HMZone(HMUAdditions) hmu_homePods] : 116 -> 128
~ ___36-[HMZone(HMUAdditions) hmu_homePods]_block_invoke_2 : 8 -> 56
~ +[HMZone(HMUAdditions) hmu_accessoriesInZones:] : 96 -> 104
~ ___47+[HMZone(HMUAdditions) hmu_accessoriesInZones:]_block_invoke_2 : 8 -> 56
~ +[HMZone(HMUAdditions) hmu_roomsInZones:] : 96 -> 104
~ ___41+[HMZone(HMUAdditions) hmu_roomsInZones:]_block_invoke_2 : 8 -> 56
~ +[HMZone(HMUAdditions) hmu_roomsInZones:appendingRooms:] : 164 -> 176
~ ___55+[HMZone(HMUAdditions) hmu_zonesWithHomePodsFromZones:]_block_invoke : 64 -> 68
~ ___66+[HMZone(HMUAdditions) hmu_zonesWithAnnounceAccessoriesFromZones:]_block_invoke : 104 -> 112
~ -[HMHomeManager(HMUAdditions) hmu_homeWithUniqueIdentifier:] : 208 -> 212
~ ___60-[HMHomeManager(HMUAdditions) hmu_homeWithUniqueIdentifier:]_block_invoke : 68 -> 72
~ -[HMHomeManager(HMUAdditions) hmu_homeWithName:] : 208 -> 212
~ ___48-[HMHomeManager(HMUAdditions) hmu_homeWithName:]_block_invoke : 68 -> 72
~ -[HMHomeManager(HMUAdditions) hmu_homesContainingRoomsWithNames:] : 224 -> 236
~ ___65-[HMHomeManager(HMUAdditions) hmu_homesContainingRoomsWithNames:]_block_invoke : 168 -> 172
~ ___65-[HMHomeManager(HMUAdditions) hmu_homesContainingRoomsWithNames:]_block_invoke_2 : 72 -> 76
~ -[HMHomeManager(HMUAdditions) hmu_homesContainingZonesWithNames:] : 224 -> 236
~ ___65-[HMHomeManager(HMUAdditions) hmu_homesContainingZonesWithNames:]_block_invoke : 168 -> 172
~ ___65-[HMHomeManager(HMUAdditions) hmu_homesContainingZonesWithNames:]_block_invoke_2 : 72 -> 76
~ -[HMHomeManager(HMUAdditions) hmu_homesWithHomeLocationStatus:] : 164 -> 172
~ -[HMHome(HMUAdditions) hmu_allUsersIncludingCurrentUser] : 116 -> 128
~ -[HMHome(HMUAdditions) hmu_userWithUniqueIdentifier:] : 208 -> 212
~ ___53-[HMHome(HMUAdditions) hmu_userWithUniqueIdentifier:]_block_invoke : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_userWithUniqueIdentifierUUIDString:] : 136 -> 140
~ -[HMHome(HMUAdditions) hmu_isRemoteAccessAllowedForCurrentUser] : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_isCurrentUserAdministrator] : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_isCurrentUserOwner] : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_isRemoteAccessAllowedForUser:] : 56 -> 60
~ -[HMHome(HMUAdditions) hmu_isAdministrator:] : 56 -> 60
~ -[HMHome(HMUAdditions) hmu_isOwner:] : 56 -> 60
~ -[HMHome(HMUAdditions) hmu_userWithSenderCorrelationIdentifier:] : 208 -> 212
~ ___64-[HMHome(HMUAdditions) hmu_userWithSenderCorrelationIdentifier:]_block_invoke : 68 -> 72
~ +[HMHome(HMUAdditions) hmu_homesFromHomes:withRoomNames:] : 544 -> 548
~ +[HMHome(HMUAdditions) hmu_homesFromHomes:withZoneNames:] : 544 -> 548
~ +[HMHome(HMUAdditions) hmu_homesFromHomes:withHomeLocationStatus:] : 132 -> 136
~ -[HMHome(HMUAdditions) hmu_allRoomsIncludingRoomForEntireHome] : 116 -> 128
~ -[HMHome(HMUAdditions) hmu_roomWithUniqueIdentifier:] : 208 -> 212
~ ___53-[HMHome(HMUAdditions) hmu_roomWithUniqueIdentifier:]_block_invoke : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_roomsWithUniqueIdentifiers:] : 232 -> 240
~ ___55-[HMHome(HMUAdditions) hmu_roomsWithUniqueIdentifiers:]_block_invoke : 72 -> 76
~ -[HMHome(HMUAdditions) hmu_roomWithName:] : 208 -> 212
~ ___41-[HMHome(HMUAdditions) hmu_roomWithName:]_block_invoke : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_zoneWithUniqueIdentifier:] : 208 -> 212
~ ___53-[HMHome(HMUAdditions) hmu_zoneWithUniqueIdentifier:]_block_invoke : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_zonesWithUniqueIdentifiers:] : 232 -> 240
~ ___55-[HMHome(HMUAdditions) hmu_zonesWithUniqueIdentifiers:]_block_invoke : 72 -> 76
~ -[HMHome(HMUAdditions) hmu_zoneWithName:] : 208 -> 212
~ ___41-[HMHome(HMUAdditions) hmu_zoneWithName:]_block_invoke : 68 -> 72
~ -[HMHome(HMUAdditions) hmu_accessoryWithUniqueIdentifierUUIDString:] : 136 -> 140
~ -[HMHome(HMUAdditions) hmu_homePodsDictionary] : 344 -> 352
~ -[HMHome(HMUAdditions) hmu_homePodsIncludingCurrentAccessoryDictionary] : 360 -> 376
~ -[HMHome(HMUAdditions) hmu_endpointAccessories] : 84 -> 92
~ -[HMAccessory(HMU_IDS) hmu_destinationForService:] : 108 -> 116
~ -[RPCompanionLinkDevice(HMUAdditions) hmu_isAccessory] : 52 -> 56
~ -[RPCompanionLinkClient(HMU_HomeKit) hmu_devicesInHome:] : 208 -> 212
~ ___56-[RPCompanionLinkClient(HMU_HomeKit) hmu_devicesInHome:]_block_invoke : 244 -> 260
~ ___56-[RPCompanionLinkClient(HMU_HomeKit) hmu_devicesInHome:]_block_invoke_2 : 60 -> 64
~ -[RPCompanionLinkClient(HMU_HomeKit) hmu_devicesForUser:] : 208 -> 212
~ ___57-[RPCompanionLinkClient(HMU_HomeKit) hmu_devicesForUser:]_block_invoke : 100 -> 108
~ -[HMAccessory(HMUAdditions) hmu_isEndpoint] : 52 -> 56
~ -[HMAccessory(HMUAdditions) hmu_isHomePod] : 88 -> 96
~ -[HMAccessory(HMUAdditions) hmu_isAppleTV] : 88 -> 96
~ -[HMAccessory(HMUAdditions) hmu_isPartOfHome:] : 128 -> 140
~ +[HMAccessory(HMUAdditions) hmu_accessoriesFromAccessories:excludingStereoCompanionForAccessory:] : 976 -> 1020
~ -[HMHome(HMU_IDS) hmu_accessoryWithFromID:service:] : 240 -> 236
~ ___51-[HMHome(HMU_IDS) hmu_accessoryWithFromID:service:]_block_invoke : 196 -> 204
~ -[HMHome(HMU_IDS) hmu_userWithFromID:] : 212 -> 216
~ ___38-[HMHome(HMU_IDS) hmu_userWithFromID:]_block_invoke : 192 -> 200
~ -[HMHome(HMU_IDS) hmu_userWithDestination:] : 208 -> 212
~ ___43-[HMHome(HMU_IDS) hmu_userWithDestination:]_block_invoke : 132 -> 144
~ -[HMHome(HMU_IDS) hmu_accessoryWithDestination:service:] : 240 -> 236
~ ___56-[HMHome(HMU_IDS) hmu_accessoryWithDestination:service:]_block_invoke : 120 -> 132
~ -[NSArray(HMUAdditions) hmu_compactMap:] : 224 -> 220
~ ___40-[NSArray(HMUAdditions) hmu_compactMap:]_block_invoke : 104 -> 108
~ +[NSError(HMUAdditions) hmu_errorWithDomain:code:description:] : 240 -> 244
~ -[HMRoom(HMUAdditions) hmu_homePods] : 84 -> 92
~ +[HMRoom(HMUAdditions) hmu_accessoriesInRooms:] : 96 -> 104
~ ___47+[HMRoom(HMUAdditions) hmu_accessoriesInRooms:]_block_invoke_2 : 8 -> 56
~ ___55+[HMRoom(HMUAdditions) hmu_roomsWithHomePodsFromRooms:]_block_invoke : 64 -> 68
~ ___66+[HMRoom(HMUAdditions) hmu_roomsWithAnnounceAccessoriesFromRooms:]_block_invoke : 104 -> 112
~ -[IDSService(HMUAdditions) hmu_homePods] : 84 -> 92
~ -[IDSService(HMUAdditions) hmu_appleTVs] : 84 -> 92
~ -[IDSService(HMUAdditions) hmu_accessories] : 84 -> 92
~ sub_2585b6338 -> sub_25d937634 : 992 -> 932
~ sub_2585b67ec -> sub_25d937aac : 52 -> 44
~ sub_2585b68e0 -> sub_25d937b98 : 780 -> 776
~ sub_2585b6e34 -> sub_25d9380e8 : 224 -> 216
~ sub_2585b6f14 -> sub_25d9381c0 : 64 -> 56
~ sub_2585b6f54 -> sub_25d9381f8 : 64 -> 56
~ sub_2585b7344 -> sub_25d9385e0 : 528 -> 512
~ _block_copy_helper : 16 -> 20
~ sub_2585b77f0 -> sub_25d938a80 : 52 -> 44
~ sub_2585b7824 -> sub_25d938aac : 52 -> 44
~ sub_2585b7858 -> sub_25d938ad8 : 52 -> 44
~ sub_2585b788c -> sub_25d938b04 : 52 -> 44
~ sub_2585b78c0 -> sub_25d938b30 : 52 -> 44
~ sub_2585b7a9c -> sub_25d938d04 : 196 -> 188
~ sub_2585b7b60 -> sub_25d938dc0 : 76 -> 68
~ sub_2585b7c70 -> sub_25d938ec8 : 1096 -> 1092
~ sub_2585b80b8 -> sub_25d93930c : 200 -> 188
~ sub_2585b8240 -> sub_25d939488 : 160 -> 140
~ sub_2585b84a4 -> sub_25d9396d8 : 196 -> 188
~ sub_2585b85e8 -> sub_25d939814 : 880 -> 872
~ sub_2585b8c90 -> sub_25d939eb4 : 672 -> 680
~ sub_2585b8f30 -> sub_25d93a15c : 340 -> 308
~ sub_2585b9084 -> sub_25d93a290 : 112 -> 104
~ sub_2585b91c0 -> sub_25d93a3c4 : 268 -> 276
~ sub_2585b9318 -> sub_25d93a524 : 304 -> 312
~ sub_2585b9448 -> sub_25d93a65c : 236 -> 244
~ ___swift_destroy_boxed_opaque_existential_0 : 76 -> 68
~ sub_2585b991c -> sub_25d93ab30 : 36 -> 28
~ sub_2585b9940 -> sub_25d93ab4c : 36 -> 28
~ sub_2585b9964 -> sub_25d93ab68 : 36 -> 28
~ sub_2585b999c -> sub_25d93ab98 : 92 -> 84
~ sub_2585b9ab8 -> sub_25d93acac : 104 -> 96
CStrings:
+ "HomeMessagingUtils"

```
