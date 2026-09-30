## MediaGroups

> `/System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0x9fdc
-  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__text: 0xa548
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0xb44
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x86c
-  __TEXT.__gcc_except_tab: 0x2f8
+  __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__oslogstring: 0x493
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0x250
   __TEXT.__objc_methname: 0x14ae
   __TEXT.__objc_methtype: 0x695

   __DATA_CONST.__objc_selrefs: 0x630
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x14f8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAFE97CD-63A6-318E-AC81-D4DCADF6DE2E
+  UUID: 3CAB51FE-C990-328C-B833-FF36E389E4FA
   Functions: 242
-  Symbols:   988
+  Symbols:   981
   CStrings:  509
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x8
Functions:
~ -[MGHomeTheater audioEntityRouteID] : 84 -> 92
~ +[MGHomeTheater predicateForType] : 108 -> 116
~ +[MGHomeTheater predicateForCurrentDevice] : 296 -> 320
~ -[MGHome initWithClientService:home:] : 212 -> 224
~ -[MGHome HomeKitHomeIdentifier] : 76 -> 84
~ -[MGHome HomeKitHomeWithHomeManager:] : 112 -> 120
~ +[MGHome predicateForType] : 108 -> 116
~ _MGLogForCategory : 100 -> 108
~ +[MGSoloDevice predicateForType] : 108 -> 116
~ +[MGSoloDevice predicateForCurrentDevice] : 244 -> 260
~ -[MGZone initWithClientService:zone:home:] : 232 -> 240
~ -[MGZone initWithConnectionProvider:zone:home:] : 148 -> 144
~ -[MGZone HomeKitZoneIdentifier] : 76 -> 84
~ -[MGZone HomeKitZoneWithHomeManager:] : 112 -> 120
~ +[MGZone predicateForType] : 108 -> 116
~ -[MGGroup initWithClientService:type:identifier:name:properties:memberIdentifiers:] : 472 -> 468
~ -[MGGroup initWithConnectionProvider:type:identifier:name:properties:memberIdentifiers:] : 216 -> 200
~ -[MGGroup initWithCoder:] : 1016 -> 1060
~ -[MGGroup description] : 228 -> 252
~ -[MGGroup encodeWithCoder:] : 276 -> 296
~ +[MGGroup groupWithClientService:name:members:completion:] : 176 -> 168
~ +[MGGroup groupWithConnectionProvider:name:members:completion:] : 184 -> 176
~ +[MGGroup groupWithName:members:completion:] : 404 -> 408
~ +[MGGroup validateGroupSpecificationWithType:identifier:name:properties:members:] : 672 -> 704
~ -[MGGroup forceSetClientService:] : 12 -> 64
~ -[MGGroup predicateForMembers] : 376 -> 388
~ -[MGGroup membersWithCompletion:] : 436 -> 444
~ ___33-[MGGroup membersWithCompletion:]_block_invoke : 156 -> 152
~ -[MGGroup isSameGroup:] : 112 -> 120
~ +[MGGroup predicateForGroup:] : 92 -> 100
~ +[MGGroup predicateForGroupIdentifier:] : 280 -> 300
~ +[MGGroup predicateForGroupsContainingGroup:] : 360 -> 392
~ -[MGGroup _conformingProtocols] : 248 -> 260
~ +[MGGroup predicateForGroupsConformingToProtocol:] : 108 -> 116
~ -[MGAudioReceiverAccessory deviceIdentifier] : 84 -> 92
~ -[MGAudioReceiverAccessory HomeKitAccesoryIdentifier] : 76 -> 84
~ -[MGAudioReceiverAccessory HomeKitAccessoryWithHomeManager:] : 112 -> 120
~ -[MGClientConnectionProvider init] : 712 -> 740
~ ___34-[MGClientConnectionProvider init]_block_invoke : 240 -> 248
~ -[MGClientConnectionProvider dealloc] : 296 -> 300
~ -[MGClientConnectionProvider _unsafe_setServiceConnection:] : 764 -> 772
~ -[MGClientConnectionProvider delegate] : 256 -> 252
~ -[MGClientConnectionProvider _createServiceConnection] : 108 -> 112
~ -[MGClientConnectionProvider serviceConnection] : 256 -> 252
~ ___47-[MGClientConnectionProvider serviceConnection]_block_invoke : 140 -> 164
~ ___59-[MGClientConnectionProvider _unsafe_setServiceConnection:]_block_invoke : 292 -> 300
~ ___59-[MGClientConnectionProvider _unsafe_setServiceConnection:]_block_invoke.16 : 292 -> 300
~ -[MGClientServiceQueryData initWithPredicate:updateHandler:] : 152 -> 148
~ -[MGClientService initWithConnectionProvider:] : 312 -> 320
~ -[MGClientService connection] : 256 -> 252
~ ___29-[MGClientService connection]_block_invoke : 388 -> 424
~ -[MGClientService reconnect] : 624 -> 632
~ ___28-[MGClientService reconnect]_block_invoke : 520 -> 540
~ -[MGClientService startQueryWithQueryData:] : 576 -> 588
~ ___41-[MGClientService updateHandlerForQuery:]_block_invoke : 108 -> 116
~ ___41-[MGClientService setQueryData:forQuery:]_block_invoke : 112 -> 116
~ ___43-[MGClientService removeQueryDataForQuery:]_block_invoke : 112 -> 116
~ +[MGClientService clientServiceWithConnectionProvider:] : 132 -> 144
~ -[MGClientService createGroupWithType:name:members:completion:] : 496 -> 488
~ ___63-[MGClientService createGroupWithType:name:members:completion:]_block_invoke_2 : 128 -> 132
~ -[MGClientService deleteGroup:completion:] : 348 -> 352
~ -[MGClientService HomeKitAccessoryOfType:accessoryIdentifier:homeIdentifier:categoryType:name:properties:completion:] : 572 -> 552
~ ___117-[MGClientService HomeKitAccessoryOfType:accessoryIdentifier:homeIdentifier:categoryType:name:properties:completion:]_block_invoke_2 : 128 -> 132
~ -[MGClientService setName:group:completion:] : 468 -> 464
~ ___44-[MGClientService setName:group:completion:]_block_invoke_2 : 128 -> 132
~ -[MGClientService addMember:group:completion:] : 488 -> 484
~ ___46-[MGClientService addMember:group:completion:]_block_invoke_2 : 128 -> 132
~ -[MGClientService removeMember:group:completion:] : 488 -> 484
~ ___49-[MGClientService removeMember:group:completion:]_block_invoke_2 : 128 -> 132
~ ___43-[MGClientService startQueryWithQueryData:]_block_invoke_2 : 336 -> 320
~ -[MGClientService stopQuery:completion:] : 396 -> 392
~ ___40-[MGClientService stopQuery:completion:]_block_invoke_2 : 196 -> 192
~ -[MGClientService query:didUpdate:completion:] : 556 -> 548
~ -[MGClientService connectionProvider:serviceLost:] : 516 -> 500
~ ___54-[MGClientService connectionProviderServiceAvailable:]_block_invoke : 216 -> 220
~ -[MGClientService setConnection:] : 12 -> 64
~ _MGSetServiceXPCInterfacesOnConnection : 1476 -> 1492
~ -[MGSpeakerAccessory deviceIdentifier] : 84 -> 92
~ -[MGSpeakerAccessory HomeKitAccesoryIdentifier] : 76 -> 84
~ -[MGSpeakerAccessory HomeKitAccessoryWithHomeManager:] : 112 -> 120
~ -[MGGroupIdentifier initWithCoder:] : 164 -> 168
~ -[MGGroupIdentifier normalized] : 100 -> 112
~ +[MGGroupIdentifier groupIdentifierWithUUID:] : 300 -> 308
~ -[MGGroupIdentifier description] : 148 -> 160
~ -[MGGroupIdentifier data] : 80 -> 88
~ -[MGGroupIdentifier compare:] : 112 -> 120
~ -[MGGroupIdentifier hash] : 56 -> 60
~ -[MGGroupIdentifier isEqual:] : 432 -> 464
~ -[MGGroupIdentifier copyWithZone:] : 4 -> 40
~ -[MGGroupIdentifier encodeWithCoder:] : 108 -> 112
~ _MGGroupIdentifierCopyApplyingHashing : 684 -> 712
~ __MGRelevantComponentsForGroupIdentifierComponents : 568 -> 584
~ _MGHomeUniqueIdentifierForAccessory : 76 -> 84
~ _MGAccessoryCategoryTypeForAccessory : 76 -> 84
~ _MGGroupIdentifierForAccessory : 256 -> 272
~ __MGGroupIdentifierHomeKitComponents : 480 -> 468
~ __MGHomeKitIdentifierForGroupIdentifier : 152 -> 176
~ _MGAccessoryFromHomeManagerForGroupIdentifier : 780 -> 824
~ _MGMemberIdentifiersForMediaSystem : 648 -> 644
~ ___MGMemberIdentifiersForMediaSystem_block_invoke : 136 -> 144
~ _MGMediaSystemFromHomeManagerForGroupIdentifier : 644 -> 684
~ _MGMemberIdentifiersForRoomInHome : 348 -> 340
~ ___MGMemberIdentifiersForRoomInHome_block_invoke : 192 -> 208
~ _MGRoomFromHomeManagerForGroupIdentifier : 644 -> 684
~ _MGMemberIdentifiersForZoneInHome : 352 -> 344
~ ___MGMemberIdentifiersForZoneInHome_block_invoke : 128 -> 136
~ _MGGroupIdentifierForRoomInHome : 132 -> 144
~ _MGZoneFromHomeManagerForGroupIdentifier : 644 -> 684
~ _MGGroupIdentifierForHomeInHome : 132 -> 144
~ _MGMemberIdentifiersForHome : 336 -> 332
~ ___MGMemberIdentifiersForHome_block_invoke : 128 -> 136
~ _MGHomeFromHomeManagerForGroupIdentifier : 416 -> 444
~ _MGGroupIdentifierForHomeIdentifierInHome : 136 -> 144
~ _MGGroupIdentifierForZoneInHome : 132 -> 144
~ _MGGroupIdentifierForZoneIdentifierInHome : 136 -> 144
~ _MGGroupIdentifierForRoomIdentifierInHome : 136 -> 144
~ _MGGroupIdentifierForMediaSystemInHome : 132 -> 144
~ _MGGroupIdentifierForMediaSystemIdentifierInHome : 136 -> 144
~ -[MGAppleTVAccessory deviceIdentifier] : 84 -> 92
~ -[MGAppleTVAccessory HomeKitAccesoryIdentifier] : 76 -> 84
~ -[MGAppleTVAccessory HomeKitAccessoryWithHomeManager:] : 112 -> 120
~ -[MGHomePodAccessory HomePodVariant] : 84 -> 92
~ -[MGHomePodAccessory productColor] : 84 -> 92
~ -[MGHomePodAccessory deviceIdentifier] : 84 -> 92
~ -[MGHomePodAccessory HomeKitAccesoryIdentifier] : 76 -> 84
~ -[MGHomePodAccessory HomeKitAccessoryWithHomeManager:] : 112 -> 120
~ +[MGHomePodAccessory HomePodWithClientService:HomeKitAccessory:completion:] : 504 -> 536
~ +[MGHomePodAccessory HomePodAccessoryWithConnectionProvider:HomeKitAccessory:completion:] : 156 -> 152
~ +[MGHomePodAccessory HomePodAccessoryWithHomeKitAccessory:completion:] : 136 -> 132
~ -[MGGroupQuery initWithConnectionProvider:predicate:updateHandler:] : 536 -> 544
~ ___67-[MGGroupQuery initWithConnectionProvider:predicate:updateHandler:]_block_invoke : 772 -> 800
~ -[MGGroupQuery dealloc] : 360 -> 372
~ ___23-[MGGroupQuery dealloc]_block_invoke : 296 -> 300
~ +[MGGroupQuery queryWithPredicate:updateHandler:] : 112 -> 108
~ -[MGGroupQuery setQuery:] : 12 -> 64
~ -[MGRoom initWithClientService:room:home:] : 232 -> 240
~ -[MGRoom initWithConnectionProvider:room:home:] : 148 -> 144
~ -[MGRoom HomeKitRoomIdentifier] : 76 -> 84
~ -[MGRoom HomeKitRoomWithHomeManager:] : 112 -> 120
~ +[MGRoom predicateForType] : 108 -> 116
~ -[MGMediaSystem initWithClientService:mediaSystem:home:] : 232 -> 240
~ -[MGMediaSystem initWithConnectionProvider:mediaSystem:home:] : 148 -> 144
~ -[MGMediaSystem syncUUID] : 76 -> 84
~ -[MGMediaSystem audioEntityRouteID] : 76 -> 84
~ -[MGMediaSystem HomeKitMediaSystemIdentifier] : 76 -> 84
~ -[MGMediaSystem HomeKitMediaSystemWithHomeManager:] : 112 -> 120
~ +[MGMediaSystem predicateForType] : 108 -> 116

```
