## FriendKit

> `/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit`

```diff

 31.0.0.0.0
-  __TEXT.__text: 0xd720
-  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__text: 0xde58
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xbf2
-  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__gcc_except_tab: 0x3a8
   __TEXT.__oslogstring: 0xca9
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x468
   __TEXT.__objc_classname: 0xeb
   __TEXT.__objc_methname: 0x21bb
   __TEXT.__objc_methtype: 0x554

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa00
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0xe38

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 002A0A68-F7B5-396B-8925-25E3043CCBAC
+  UUID: 624E6E90-6CC1-3F57-B11A-83874DDDECA4
   Functions: 280
-  Symbols:   1205
+  Symbols:   1203
   CStrings:  726
 
Symbols:
+ _objc_release_x2
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
Functions:
~ +[FKUtility shouldAllowAddingFriendWithRecordID:withFriendListManager:addressBook:personValueCache:] : 324 -> 336
~ +[FKUtility _nameFormatter] : 68 -> 84
~ +[FKUtility initialsForPerson:] : 364 -> 376
~ +[FKUtility initialForString:] : 200 -> 216
~ +[FKUtility hashFromData:] : 212 -> 224
~ -[FKDelayedOperation initWithQueue:delay:block:] : 316 -> 312
~ -[FKDelayedOperation execute] : 284 -> 280
~ -[NSSet(FriendKit) fkSanitizedDestinationSet] : 368 -> 376
~ +[FKFriendsManager managerForDomain:] : 160 -> 164
~ ___37+[FKFriendsManager managerForDomain:]_block_invoke : 64 -> 68
~ -[FKFriendsManager initWithDomain:] : 1004 -> 1044
~ _getCNContactStoreDidChangeNotification : 224 -> 232
~ -[FKFriendsManager dealloc] : 196 -> 200
~ -[FKFriendsManager friendGroups] : 8 -> 56
~ -[FKFriendsManager _addEmptyGroup] : 216 -> 220
~ -[FKFriendsManager _createEmptyFriendList] : 104 -> 112
~ -[FKFriendsManager reloadFriendList] : 196 -> 200
~ -[FKFriendsManager _loadFriendList] : 708 -> 720
~ -[FKFriendsManager _curatedFriendList] : 516 -> 520
~ ___38-[FKFriendsManager _curatedFriendList]_block_invoke : 1124 -> 1160
~ -[FKFriendsManager _addCuratedFriends:] : 424 -> 436
~ ___39-[FKFriendsManager _addCuratedFriends:]_block_invoke_2 : 224 -> 228
~ -[FKFriendsManager _shouldAddEmptyGroup] : 104 -> 108
~ -[FKFriendsManager _updateFriendGroups] : 368 -> 380
~ -[FKFriendsManager syncFriendGroup:] : 504 -> 520
~ ___53-[FKFriendsManager _postGroupListChangedNotification]_block_invoke : 84 -> 88
~ +[FKFriendsManager setMaxGroupCount:domain:] : 116 -> 120
~ +[FKFriendsManager setGroupSize:domain:] : 116 -> 120
~ +[FKFriendsManager setEnableEmptyTrailingGroup:domain:] : 116 -> 120
~ +[FKFriendsManager setFriendsChangedExternallyNotificationName:domain:] : 96 -> 100
~ +[FKFriendsManager setFriendGroupTitleChangedExternallyNotificationName:domain:] : 96 -> 100
~ +[FKFriendsManager setRefreshAgainstContactsOnInitEnabled:domain:] : 116 -> 120
~ -[FKFriendsManager shouldAllowAddingContact:withContactStore:personValueCache:] : 292 -> 308
~ -[FKFriendsManager friendGroup:didSetFriend:atPosition:] : 216 -> 220
~ -[FKFriendsManager friendGroup:didRemoveFriend:atPosition:] : 296 -> 300
~ -[FKFriendsManager allPeople] : 80 -> 88
~ -[FKFriendsManager containsFriendWithABRecordGUID:] : 124 -> 132
~ -[FKFriendsManager personLikePerson:] : 160 -> 164
~ -[FKFriendsManager _friendAtPosition:] : 152 -> 160
~ ___24-[FKFriendsManager save]_block_invoke : 312 -> 320
~ -[FKFriendsManager _save] : 928 -> 956
~ -[FKFriendsManager personWithDestinations:] : 476 -> 512
~ -[FKFriendsManager personWithABRecordGUID:] : 360 -> 356
~ -[FKFriendsManager _storeSourcedPerson:] : 96 -> 100
~ -[FKFriendsManager _addPersonToIdentifiersToPersonMap:] : 360 -> 380
~ -[FKFriendsManager _removePersonFromIdentifiersToPersonMap:] : 352 -> 372
~ -[FKFriendsManager _createAddressToPersonDictionary] : 380 -> 384
~ -[FKFriendsManager setServiceName:] : 264 -> 268
~ -[FKFriendsManager _destinations] : 412 -> 432
~ -[FKFriendsManager refreshDestinationStatuses] : 464 -> 492
~ -[FKFriendsManager idStatusUpdatedForDestinations:] : 1540 -> 1548
~ ___51-[FKFriendsManager idStatusUpdatedForDestinations:]_block_invoke : 208 -> 216
~ -[FKFriendsManager statusForPerson:requery:] : 576 -> 588
~ -[FKFriendsManager reachableDestinationsForPerson:] : 264 -> 276
~ -[FKFriendsManager _queryDestinations:] : 544 -> 568
~ -[FKFriendsManager _startIDSQueryTimeoutTimer] : 108 -> 112
~ -[FKFriendsManager _idsQueryTimeoutTimerFired] : 408 -> 420
~ ___55-[FKFriendsManager _shouldBypassDestinationStatusCheck]_block_invoke : 140 -> 152
~ -[FKFriendsManager _firstEmptyPosition] : 148 -> 156
~ -[FKFriendsManager _numberOfFriendsInList:] : 248 -> 252
~ ___54-[FKFriendsManager _postChangeNotificationIfNecessary]_block_invoke : 396 -> 404
~ -[FKFriendsManager _personValuesChanged:] : 128 -> 132
~ -[FKFriendsManager _friendsChangedExternally] : 216 -> 220
~ -[FKFriendsManager _loadGroupTitles] : 208 -> 216
~ -[FKFriendsManager _groupTitleChangedExternally] : 196 -> 200
~ -[FKFriendsManager _addressBookChanged:] : 328 -> 336
~ ___40-[FKFriendsManager _addressBookChanged:]_block_invoke : 144 -> 148
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke : 924 -> 936
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke_2 : 1312 -> 1340
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke_3 : 116 -> 120
~ ___53-[FKFriendsManager _deduplicateFriendListIfNecessary]_block_invoke : 412 -> 416
~ -[FKFriendsManager _removeDestinationlessFriendsIfNecessary] : 200 -> 204
~ ___60-[FKFriendsManager _removeDestinationlessFriendsIfNecessary]_block_invoke : 340 -> 344
~ -[FKFriendsManager _removeFriendsAtIndices:] : 152 -> 156
~ ___44-[FKFriendsManager _removeFriendsAtIndices:]_block_invoke : 204 -> 216
~ ___35-[FKFriendsManager _changeLogCount]_block_invoke : 104 -> 108
~ -[FKFriendsManager _copyAndResetChangeLog] : 276 -> 272
~ ___42-[FKFriendsManager _copyAndResetChangeLog]_block_invoke : 276 -> 288
~ -[FKFriendsManager _addEntryToChangeLogForPerson:changeType:] : 236 -> 232
~ ___61-[FKFriendsManager _addEntryToChangeLogForPerson:changeType:]_block_invoke : 280 -> 304
~ ___62-[FKFriendsManager _changeLogContainsFriendAdditionsOrUpdates]_block_invoke : 164 -> 168
~ ___62-[FKFriendsManager _changeLogContainsFriendAdditionsOrUpdates]_block_invoke_2 : 128 -> 136
~ +[FKFriendsManager collapseChangeLogsIntoChangeLog:] : 400 -> 404
~ ___52+[FKFriendsManager collapseChangeLogsIntoChangeLog:]_block_invoke : 248 -> 260
~ -[FKFriendsManager refreshAgainstAddressBook] : 344 -> 348
~ ___45-[FKFriendsManager refreshAgainstAddressBook]_block_invoke_2 : 108 -> 112
~ -[FKFriendsManager saveFriendGroupTitles] : 420 -> 424
~ ___41-[FKFriendsManager saveFriendGroupTitles]_block_invoke : 172 -> 176
~ ___46-[FKFriendsManager markFriendListAsNormalized]_block_invoke : 184 -> 188
~ -[FKFriendsManager setSaveOperation:] : 12 -> 64
~ -[FKFriendsManager setChangeLog:] : 12 -> 64
~ +[FKAddressBook sharedInstance] : 68 -> 84
~ -[FKAddressBook init] : 272 -> 276
~ ___21-[FKAddressBook init]_block_invoke : 148 -> 152
~ +[FKAddressBook performBlock:] : 216 -> 220
~ -[FKAddressBook setOperationQueue:] : 12 -> 64
~ -[NSString(IDSDestinationParsing) fkMessageDestinationType] : 160 -> 164
~ -[NSString(IDSDestinationParsing) fkMessageCanonicalRawAddress] : 156 -> 160
~ _FriendKitBundle : 68 -> 84
~ ___FriendKitBundle_block_invoke : 72 -> 76
~ +[FKPerson sharedMetadataQueue] : 68 -> 84
~ -[FKPerson init] : 112 -> 116
~ -[FKPerson initWithDestinations:addressBook:] : 128 -> 132
~ -[FKPerson initWithFavorite:addressBook:] : 272 -> 288
~ -[FKPerson copyWithZone:] : 4 -> 40
~ -[FKPerson encodeWithCoder:] : 268 -> 276
~ -[FKPerson initWithCoder:] : 808 -> 864
~ -[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:] : 2000 -> 2084
~ ___65-[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:]_block_invoke : 476 -> 484
~ ___65-[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:]_block_invoke.72 : 140 -> 148
~ -[FKPerson dictionaryRepresentation] : 436 -> 460
~ ___36-[FKPerson dictionaryRepresentation]_block_invoke : 140 -> 144
~ -[FKPerson displayName] : 140 -> 148
~ -[FKPerson primaryDestination] : 200 -> 224
~ -[FKPerson setPreferredReplyAs:] : 324 -> 316
~ -[FKPerson _metadataDictionary] : 8 -> 56
~ -[FKPerson metadataValueForKey:] : 328 -> 324
~ ___32-[FKPerson metadataValueForKey:]_block_invoke : 80 -> 84
~ -[FKPerson setMetadataValue:forKey:] : 276 -> 268
~ ___36-[FKPerson setMetadataValue:forKey:]_block_invoke : 148 -> 152
~ -[FKPerson addMetadataEntriesFromDictionary:] : 272 -> 276
~ ___45-[FKPerson addMetadataEntriesFromDictionary:]_block_invoke : 148 -> 152
~ -[FKPerson removeAllMetadataValues] : 200 -> 204
~ ___35-[FKPerson removeAllMetadataValues]_block_invoke : 144 -> 148
~ ___20-[FKPerson metadata]_block_invoke : 88 -> 92
~ -[FKPerson description] : 176 -> 192
~ -[FKPerson abRecordGUID] : 8 -> 56
~ ___29-[FKPerson _setABRecordGUID:]_block_invoke : 120 -> 124
~ -[FKPerson abDatabaseUID] : 8 -> 56
~ -[FKPerson isEqualToDictionaryRepresentation:] : 412 -> 416
~ -[FKPerson isLikePerson:] : 180 -> 188
~ ___35-[FKPerson _postChangeNotification]_block_invoke : 116 -> 120
~ -[FKPerson _reconcile:canPostChangeNotification:shouldLogUpdates:] : 1900 -> 1956
~ +[FKPerson preferredNameForPerson:] : 228 -> 224
~ +[FKPerson allValuesForPerson:] : 496 -> 520
~ -[FKPerson _recordMatchDictionaryFromCFArray:followLinks:addressBook:] : 336 -> 352
~ -[FKPerson _bestRecordMatchFromDictionary:addressBook:] : 292 -> 296
~ +[FKPerson _allPhoneValuesForRecord:] : 208 -> 224
~ +[FKPerson _allEmailValuesForRecord:] : 208 -> 224
~ __FKGetLogSystem : 68 -> 84
~ ____FKGetLogSystem_block_invoke : 120 -> 128
~ -[FKFriendGroup initWithGroupSize:] : 200 -> 208
~ -[FKFriendGroup friendAtPosition:] : 148 -> 156
~ -[FKFriendGroup count] : 244 -> 248
~ -[FKFriendGroup addFriend:error:] : 268 -> 272
~ -[FKFriendGroup setTitle:] : 228 -> 216
~ ___26-[FKFriendGroup setTitle:]_block_invoke : 124 -> 128
~ -[FKFriendGroup setFriend:atPosition:error:] : 640 -> 664
~ -[FKFriendGroup removeFriendAtPosition:] : 468 -> 492
~ -[FKFriendGroup setFriends:] : 92 -> 96
~ -[FKFriendGroup friends] : 8 -> 56
~ -[FKFriendGroup _firstEmptyPosition] : 140 -> 148
~ -[FKFriendGroup displayNameForGroupWithSeparator:] : 768 -> 804

```
