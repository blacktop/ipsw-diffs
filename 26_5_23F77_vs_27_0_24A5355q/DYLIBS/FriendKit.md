## FriendKit

> `/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit`

```diff

 31.0.0.0.0
-  __TEXT.__text: 0xde58
-  __TEXT.__auth_stubs: 0x790
+  __TEXT.__text: 0xd378
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xbf2
-  __TEXT.__gcc_except_tab: 0x3a8
+  __TEXT.__cstring: 0xc06
+  __TEXT.__gcc_except_tab: 0x354
   __TEXT.__oslogstring: 0xca9
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x468
-  __TEXT.__objc_classname: 0xeb
-  __TEXT.__objc_methname: 0x21bb
-  __TEXT.__objc_methtype: 0x554
-  __TEXT.__objc_stubs: 0x1da0
-  __DATA_CONST.__got: 0x178
+  __TEXT.__unwind_info: 0x458
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa00
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0xe38
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AF78272-448A-313A-9687-703A1B58B11C
+  UUID: A2E4224D-E226-3C96-A440-4C9D1E064DD9
   Functions: 280
-  Symbols:   1203
-  CStrings:  726
+  Symbols:   1205
+  CStrings:  231
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x27
- _objc_retain_x28
Functions:
~ +[FKUtility shouldAllowAddingFriendWithRecordID:withFriendListManager:addressBook:personValueCache:] : 336 -> 324
~ +[FKUtility _nameFormatter] : 84 -> 68
~ +[FKUtility initialsForPerson:] : 376 -> 364
~ +[FKUtility initialForString:] : 216 -> 200
~ +[FKUtility hashFromData:] : 224 -> 212
~ -[FKDelayedOperation initWithQueue:delay:block:] : 312 -> 316
~ -[NSSet(FriendKit) fkSanitizedDestinationSet] : 376 -> 372
~ +[FKFriendsManager managerForDomain:] : 164 -> 160
~ ___37+[FKFriendsManager managerForDomain:]_block_invoke : 68 -> 64
~ -[FKFriendsManager initWithDomain:] : 1044 -> 1004
~ _getCNContactStoreDidChangeNotification : 232 -> 224
~ -[FKFriendsManager dealloc] : 200 -> 196
~ -[FKFriendsManager friendGroups] : 56 -> 8
~ -[FKFriendsManager _addEmptyGroup] : 220 -> 216
~ -[FKFriendsManager _createEmptyFriendList] : 112 -> 104
~ -[FKFriendsManager reloadFriendList] : 200 -> 152
~ -[FKFriendsManager _loadFriendList] : 720 -> 664
~ -[FKFriendsManager _curatedFriendList] : 520 -> 464
~ ___38-[FKFriendsManager _curatedFriendList]_block_invoke : 1160 -> 1128
~ -[FKFriendsManager _addCuratedFriends:] : 436 -> 424
~ ___39-[FKFriendsManager _addCuratedFriends:]_block_invoke_2 : 228 -> 224
~ -[FKFriendsManager _shouldAddEmptyGroup] : 108 -> 104
~ -[FKFriendsManager _updateFriendGroups] : 380 -> 372
~ -[FKFriendsManager canAddFriend] : 272 -> 276
~ -[FKFriendsManager syncFriendGroup:] : 520 -> 460
~ -[FKFriendsManager purgeEmptyFriendGroups] : 196 -> 192
~ ___53-[FKFriendsManager _postGroupListChangedNotification]_block_invoke : 88 -> 84
~ +[FKFriendsManager setMaxGroupCount:domain:] : 120 -> 116
~ +[FKFriendsManager setGroupSize:domain:] : 120 -> 116
~ +[FKFriendsManager setEnableEmptyTrailingGroup:domain:] : 120 -> 116
~ +[FKFriendsManager setFriendsChangedExternallyNotificationName:domain:] : 100 -> 96
~ +[FKFriendsManager setFriendGroupTitleChangedExternallyNotificationName:domain:] : 100 -> 96
~ +[FKFriendsManager setRefreshAgainstContactsOnInitEnabled:domain:] : 120 -> 116
~ -[FKFriendsManager shouldAllowAddingContact:withContactStore:personValueCache:] : 308 -> 292
~ -[FKFriendsManager friendGroup:didSetFriend:atPosition:] : 220 -> 216
~ -[FKFriendsManager friendGroup:didRemoveFriend:atPosition:] : 300 -> 296
~ -[FKFriendsManager friendGroup:didMoveFriends:] : 368 -> 372
~ -[FKFriendsManager allPeople] : 88 -> 80
~ -[FKFriendsManager addFriend:] : 308 -> 312
~ -[FKFriendsManager containsFriendWithABRecordGUID:] : 132 -> 124
~ -[FKFriendsManager personLikePerson:] : 164 -> 160
~ -[FKFriendsManager _friendAtPosition:] : 160 -> 152
~ ___24-[FKFriendsManager save]_block_invoke : 320 -> 312
~ -[FKFriendsManager _save] : 956 -> 928
~ -[FKFriendsManager personWithDestinations:] : 512 -> 476
~ -[FKFriendsManager personWithABRecordGUID:] : 356 -> 360
~ -[FKFriendsManager _storeSourcedPerson:] : 100 -> 96
~ -[FKFriendsManager _addPersonToIdentifiersToPersonMap:] : 380 -> 364
~ -[FKFriendsManager _removePersonFromIdentifiersToPersonMap:] : 372 -> 356
~ -[FKFriendsManager setServiceName:] : 268 -> 220
~ -[FKFriendsManager _destinations] : 432 -> 416
~ -[FKFriendsManager refreshDestinationStatuses] : 492 -> 420
~ -[FKFriendsManager idStatusUpdatedForDestinations:] : 1548 -> 1552
~ ___51-[FKFriendsManager idStatusUpdatedForDestinations:]_block_invoke : 216 -> 208
~ -[FKFriendsManager statusForPerson:requery:] : 588 -> 580
~ -[FKFriendsManager reachableDestinationsForPerson:] : 276 -> 264
~ -[FKFriendsManager _queryDestinations:] : 568 -> 552
~ -[FKFriendsManager _startIDSQueryTimeoutTimer] : 112 -> 108
~ -[FKFriendsManager _idsQueryTimeoutTimerFired] : 420 -> 364
~ ___55-[FKFriendsManager _shouldBypassDestinationStatusCheck]_block_invoke : 152 -> 140
~ -[FKFriendsManager _firstEmptyPosition] : 156 -> 148
~ -[FKFriendsManager _numberOfFriendsInList:] : 252 -> 248
~ ___54-[FKFriendsManager _postChangeNotificationIfNecessary]_block_invoke : 404 -> 352
~ -[FKFriendsManager _personValuesChanged:] : 132 -> 128
~ -[FKFriendsManager _friendsChangedExternally] : 220 -> 172
~ -[FKFriendsManager _loadGroupTitles] : 216 -> 208
~ -[FKFriendsManager _groupTitleChangedExternally] : 200 -> 152
~ -[FKFriendsManager _addressBookChanged:] : 336 -> 284
~ ___40-[FKFriendsManager _addressBookChanged:]_block_invoke : 148 -> 144
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke : 936 -> 924
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke_2 : 1340 -> 1320
~ ___35-[FKFriendsManager _updateFriends:]_block_invoke_3 : 120 -> 116
~ ___53-[FKFriendsManager _deduplicateFriendListIfNecessary]_block_invoke : 416 -> 368
~ -[FKFriendsManager _removeDestinationlessFriendsIfNecessary] : 204 -> 200
~ ___60-[FKFriendsManager _removeDestinationlessFriendsIfNecessary]_block_invoke : 344 -> 296
~ -[FKFriendsManager _removeFriendsAtIndices:] : 156 -> 152
~ ___44-[FKFriendsManager _removeFriendsAtIndices:]_block_invoke : 216 -> 204
~ ___35-[FKFriendsManager _changeLogCount]_block_invoke : 108 -> 104
~ -[FKFriendsManager _copyAndResetChangeLog] : 272 -> 276
~ ___42-[FKFriendsManager _copyAndResetChangeLog]_block_invoke : 288 -> 276
~ -[FKFriendsManager _addEntryToChangeLogForPerson:changeType:] : 232 -> 236
~ ___61-[FKFriendsManager _addEntryToChangeLogForPerson:changeType:]_block_invoke : 304 -> 280
~ ___62-[FKFriendsManager _changeLogContainsFriendAdditionsOrUpdates]_block_invoke : 168 -> 164
~ ___62-[FKFriendsManager _changeLogContainsFriendAdditionsOrUpdates]_block_invoke_2 : 136 -> 128
~ ___52+[FKFriendsManager collapseChangeLogsIntoChangeLog:]_block_invoke : 260 -> 248
~ -[FKFriendsManager refreshAgainstAddressBook] : 348 -> 300
~ ___45-[FKFriendsManager refreshAgainstAddressBook]_block_invoke_2 : 112 -> 108
~ ___41-[FKFriendsManager saveFriendGroupTitles]_block_invoke : 176 -> 172
~ ___46-[FKFriendsManager markFriendListAsNormalized]_block_invoke : 188 -> 184
~ -[FKFriendsManager setSaveOperation:] : 64 -> 12
~ -[FKFriendsManager setChangeLog:] : 64 -> 12
~ +[FKAddressBook sharedInstance] : 84 -> 68
~ -[FKAddressBook init] : 276 -> 272
~ ___21-[FKAddressBook init]_block_invoke : 152 -> 148
~ +[FKAddressBook performBlock:] : 220 -> 216
~ -[FKAddressBook setOperationQueue:] : 64 -> 12
~ -[NSString(IDSDestinationParsing) fkMessageDestinationType] : 164 -> 160
~ -[NSString(IDSDestinationParsing) fkMessageCanonicalRawAddress] : 160 -> 156
~ _FriendKitBundle : 84 -> 68
~ ___FriendKitBundle_block_invoke : 76 -> 72
~ +[FKPerson sharedMetadataQueue] : 84 -> 68
~ -[FKPerson init] : 116 -> 112
~ -[FKPerson initWithDestinations:addressBook:] : 132 -> 128
~ -[FKPerson initWithFavorite:addressBook:] : 288 -> 272
~ -[FKPerson copyWithZone:] : 40 -> 4
~ -[FKPerson encodeWithCoder:] : 276 -> 268
~ -[FKPerson initWithCoder:] : 864 -> 808
~ -[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:] : 2084 -> 1948
~ ___65-[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:]_block_invoke : 484 -> 424
~ ___65-[FKPerson _updateFromDictionaryRepresentation:shouldLogUpdates:]_block_invoke.72 : 148 -> 140
~ -[FKPerson dictionaryRepresentation] : 460 -> 436
~ ___36-[FKPerson dictionaryRepresentation]_block_invoke : 144 -> 140
~ -[FKPerson displayName] : 148 -> 140
~ -[FKPerson primaryDestination] : 224 -> 200
~ -[FKPerson setPreferredReplyAs:] : 316 -> 280
~ -[FKPerson _metadataDictionary] : 56 -> 8
~ -[FKPerson metadataValueForKey:] : 324 -> 328
~ ___32-[FKPerson metadataValueForKey:]_block_invoke : 84 -> 80
~ -[FKPerson setMetadataValue:forKey:] : 268 -> 276
~ ___36-[FKPerson setMetadataValue:forKey:]_block_invoke : 152 -> 148
~ -[FKPerson addMetadataEntriesFromDictionary:] : 276 -> 272
~ ___45-[FKPerson addMetadataEntriesFromDictionary:]_block_invoke : 152 -> 148
~ -[FKPerson removeAllMetadataValues] : 204 -> 200
~ ___35-[FKPerson removeAllMetadataValues]_block_invoke : 148 -> 144
~ ___20-[FKPerson metadata]_block_invoke : 92 -> 88
~ -[FKPerson description] : 192 -> 176
~ -[FKPerson abRecordGUID] : 56 -> 8
~ ___29-[FKPerson _setABRecordGUID:]_block_invoke : 124 -> 120
~ -[FKPerson abDatabaseUID] : 56 -> 8
~ -[FKPerson isLikePerson:] : 188 -> 180
~ ___35-[FKPerson _postChangeNotification]_block_invoke : 120 -> 116
~ -[FKPerson _reconcile:canPostChangeNotification:shouldLogUpdates:] : 1956 -> 1860
~ +[FKPerson preferredNameForPerson:] : 224 -> 228
~ +[FKPerson allValuesForPerson:] : 520 -> 500
~ -[FKPerson _recordMatchDictionaryFromCFArray:followLinks:addressBook:] : 352 -> 336
~ -[FKPerson _bestRecordMatchFromDictionary:addressBook:] : 296 -> 292
~ +[FKPerson _allPhoneValuesForRecord:] : 224 -> 208
~ +[FKPerson _allPhoneValuesInSet:] : 324 -> 328
~ +[FKPerson _allEmailValuesForRecord:] : 224 -> 208
~ +[FKPerson _allEmailValuesInSet:] : 324 -> 328
~ __FKGetLogSystem : 84 -> 68
~ ____FKGetLogSystem_block_invoke : 128 -> 120
~ -[FKFriendGroup initWithGroupSize:] : 208 -> 200
~ -[FKFriendGroup friendAtPosition:] : 156 -> 148
~ -[FKFriendGroup count] : 248 -> 244
~ -[FKFriendGroup addFriend:error:] : 272 -> 224
~ -[FKFriendGroup setTitle:] : 216 -> 228
~ ___26-[FKFriendGroup setTitle:]_block_invoke : 128 -> 124
~ -[FKFriendGroup setFriend:atPosition:error:] : 664 -> 596
~ -[FKFriendGroup removeFriendAtPosition:] : 492 -> 424
~ -[FKFriendGroup setFriends:] : 96 -> 92
~ -[FKFriendGroup friends] : 56 -> 8
~ -[FKFriendGroup _firstEmptyPosition] : 148 -> 140
~ -[FKFriendGroup displayNameForGroupWithSeparator:] : 804 -> 776
~ -[FKFriendsManager initWithDomain:].cold.1 : 148 -> 104
~ ___21-[FKAddressBook init]_block_invoke.cold.1 : 160 -> 116
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<FKFriendGroupDelegate>\""
- "@\"FKDelayedOperation\""
- "@\"IDSBatchIDQueryController\""
- "@\"NPSManager\""
- "@\"NSArray\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^v16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^v24"
- "@36@0:8^{__CFArray=}16B24^v28"
- "@40@0:8:16@24@32"
- "@40@0:8@16d24@?32"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^v16"
- "B28@0:8@16B24"
- "B40@0:8@16@24@32"
- "B44@0:8i16@20^v28@36"
- "FKAddressBook"
- "FKDelayedOperation"
- "FKFriendGroup"
- "FKFriendGroupDelegate"
- "FKFriendsManager"
- "FKPerson"
- "FKUtility"
- "FriendKit"
- "IDSBatchIDQueryControllerDelegate"
- "IDSDestinationParsing"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8Q16@24"
- "T#,R"
- "T@\"<FKFriendGroupDelegate>\",W,N,V_delegate"
- "T@\"FKDelayedOperation\",&,N,V_saveOperation"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSMutableDictionary\",&,N,V_changeLog"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_operationQueue"
- "T@\"NSString\",&,N,V_preferredReplyAs"
- "T@\"NSString\",&,N,V_serviceName"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,GdidLastLoadHaveChanges,V_lastLoadHadChanges"
- "TB,N,GisRefreshAgainstContactsEnabled,V_refreshAgainstContactsEnabled"
- "TB,N,V_needsSave"
- "TB,R"
- "TB,R,N,V_hasUnreadMessages"
- "TQ,N,V_selectedPosition"
- "TQ,R"
- "T^v,N,V_addressBook"
- "UTF8String"
- "Vv16@0:8"
- "^v"
- "^v16@0:8"
- "^v24@0:8^v16"
- "^v32@0:8@16^v24"
- "^{_NSZone=}16@0:8"
- "^{__CFString=}"
- "^{__CFString=}16@0:8"
- "_abDatabaseUID"
- "_abRecordGUID"
- "_abRecordID"
- "_abUid"
- "_addCuratedFriends:"
- "_addEmptyGroup"
- "_addEntryToChangeLogForPerson:changeType:"
- "_addPersonToIdentifiersToPersonMap:"
- "_addressBook"
- "_addressBookChanged:"
- "_addressBookRefreshTimer"
- "_addressBookSequenceNumberDidChange"
- "_aggdLogFriendCount"
- "_aggdLogFriendGroupCount"
- "_aggdSetValue:forScalarKey:"
- "_allEmailValuesForRecord:"
- "_allEmailValuesInSet:"
- "_allPhoneValuesForRecord:"
- "_allPhoneValuesInSet:"
- "_allValues"
- "_allValuesMatchScore:"
- "_bestRecordMatchFromDictionary:addressBook:"
- "_block"
- "_blockEnqueued"
- "_cachedStatuses"
- "_canAddFriendGroup"
- "_changeLog"
- "_changeLogContainsFriendAdditionsOrUpdates"
- "_changeLogCount"
- "_changeLogQueue"
- "_cleanUpFriendListIfNecessary"
- "_compareStatus:toStatus:"
- "_copyAndResetChangeLog"
- "_createAddressToPersonDictionary"
- "_createEmptyFriendList"
- "_curatedFriendList"
- "_deduplicateFriendListIfNecessary"
- "_delay"
- "_delegate"
- "_destinations"
- "_didCompleteInitialLoading"
- "_domain"
- "_emailAddressCount"
- "_firstEmptyPosition"
- "_friendAtPosition:"
- "_friendGroupTitleChangedExternallyNotificationName"
- "_friendGroups"
- "_friendList"
- "_friendsChangedExternally"
- "_friendsChangedExternallyNotificationName"
- "_friendsManager"
- "_groupSize"
- "_groupTitleChangedExternally"
- "_hasUnreadMessages"
- "_highPriorityDestinations"
- "_identifiersToPersonMap"
- "_idsQueryTimeoutTimer"
- "_idsQueryTimeoutTimerFired"
- "_incrementExternalChangePostCount"
- "_indexForPosition:inGroup:"
- "_initials"
- "_initiateIDSDestinationStatusQuery:"
- "_lastExecution"
- "_lastKnownAddressBookSequenceNumber"
- "_lastLoadHadChanges"
- "_loadFriendList"
- "_loadGroupTitles"
- "_maxFriendGroups"
- "_maxFriendsPerGroup"
- "_metadata"
- "_metadataDictionary"
- "_name"
- "_nameFormatter"
- "_needsAddressBookRefresh"
- "_needsFriendListSync"
- "_needsSave"
- "_notificationForExternalListChange"
- "_npsManager"
- "_numberOfFriendsInList:"
- "_operationQueue"
- "_pendingDestinations"
- "_personValuesChanged:"
- "_phoneNumberCount"
- "_postChangeNotification"
- "_postChangeNotificationIfNecessary"
- "_postCount"
- "_postGroupListChangedNotification"
- "_preferredReplyAs"
- "_primaryDestination"
- "_queryController"
- "_queryDestinations:"
- "_queue"
- "_queue_executeBlock"
- "_queue_updateLastExecution"
- "_reconcile:canPostChangeNotification:shouldLogUpdates:"
- "_recordMatchDictionaryFromCFArray:followLinks:addressBook:"
- "_refreshAgainstContactsEnabled"
- "_removeDestinationlessFriendsIfNecessary"
- "_removeFriendsAtIndices:"
- "_removeGroupAtIndex:"
- "_removePersonFromIdentifiersToPersonMap:"
- "_save"
- "_saveOperation"
- "_saveQueue"
- "_selectedPosition"
- "_serviceName"
- "_setABRecordGUID:"
- "_setupQueryController"
- "_shouldAddEmptyGroup"
- "_shouldAddEmptyTrailingGroup"
- "_shouldBypassDestinationStatusCheck"
- "_shouldDeduplicateFriendList"
- "_shouldRemoveDestinationlessFriends"
- "_sourcedPersons"
- "_startIDSQueryTimeoutTimer"
- "_stopIDSQueryTimeoutTimer"
- "_storeSourcedPerson:"
- "_timerSource"
- "_title"
- "_updateFriendGroups"
- "_updateFriends:"
- "_updateFromDictionaryRepresentation:shouldLogUpdates:"
- "_updateLastKnownAddressBookSequenceNumber:"
- "abDatabaseUID"
- "abRecordGUID"
- "addEntriesFromDictionary:"
- "addFriend:"
- "addFriend:error:"
- "addIndex:"
- "addMetadataEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addValue:withLabel:toPerson:property:"
- "addressBook"
- "allKeys"
- "allObjects"
- "allPeople"
- "allValues"
- "allValuesCount"
- "allValuesForPerson:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "batchQueryController:updatedDestinationsStatus:onService:error:"
- "boolValue"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "canAddFriend"
- "changeLog"
- "class"
- "collapseChangeLogsIntoChangeLog:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "compressPhoneNumberString:"
- "conformsToProtocol:"
- "containsFriend:"
- "containsFriendWithABRecordGUID:"
- "containsObject:"
- "containsString:"
- "copy"
- "copyABPersonWithAddressBook:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decimalDigitCharacterSet"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "delegate"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didLastLoadHaveChanges"
- "displayName"
- "displayNameForGroupWithSeparator:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateIndexesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsAtIndexes:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "execute"
- "f24@0:8@16"
- "firstObjectCommonWithArray:"
- "fkMessageCanonicalRawAddress"
- "fkMessageDestinationType"
- "fkMessageIDSIdentifier"
- "fkMessageIsIDSIdentifier"
- "fkMessageIsRawAddress"
- "fkMessageRawAddress"
- "fkSanitizedDestinationSet"
- "friendAtPosition:"
- "friendGroup:didMoveFriends:"
- "friendGroup:didRemoveFriend:atPosition:"
- "friendGroup:didSetFriend:atPosition:"
- "friendGroups"
- "friends"
- "groupIndexContainingFriend:"
- "hasName"
- "hasUnreadMessages"
- "hash"
- "hashFromData:"
- "hashTableWithOptions:"
- "i16@0:8"
- "i44@0:8^v16^{__CFString=}24^v32i40"
- "idStatusUpdatedForDestinations:"
- "idStatusUpdatedForDestinations:service:"
- "indexOfObject:"
- "indexSet"
- "indexSetWithIndexesInRange:"
- "init"
- "initWithABRecordGUID:addressBook:"
- "initWithCoder:"
- "initWithDelegate:groupSize:"
- "initWithDestinations:addressBook:"
- "initWithDictionaryRepresentation:addressBook:"
- "initWithDomain:"
- "initWithFavorite:addressBook:"
- "initWithGroupSize:"
- "initWithQueue:delay:block:"
- "initWithService:delegate:queue:"
- "initialForString:"
- "initials"
- "initialsForPerson:"
- "intValue"
- "integerValue"
- "intersectSet:"
- "intersectsSet:"
- "invalidate"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToDictionaryRepresentation:"
- "isEqualToSet:"
- "isEqualToString:"
- "isFull"
- "isKindOfClass:"
- "isLikePerson:"
- "isMemberOfClass:"
- "isPersonFriend:"
- "isProxy"
- "isRefreshAgainstContactsEnabled"
- "isRomanString:"
- "isValid"
- "keyEnumerator"
- "lastLoadHadChanges"
- "lastObject"
- "length"
- "letterCharacterSet"
- "localizedStringForKey:value:table:"
- "localizedUppercaseString"
- "managerForDomain:"
- "markFriendListAsNormalized"
- "metadata"
- "metadataValueForKey:"
- "mutableCopy"
- "name"
- "needsSave"
- "null"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "operationQueue"
- "performBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentDomainForName:"
- "personFromContact:"
- "personHasLinkages:"
- "personLikePerson:"
- "personWithABRecordGUID:"
- "personWithDestinations:"
- "positionOfFriend:"
- "positionOfFriendInGroup:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "preferredNameForPerson:"
- "preferredReplyAs"
- "primaryDestination"
- "purgeEmptyFriendGroups"
- "q16@0:8"
- "q28@0:8@16B24"
- "q32@0:8q16q24"
- "rangeOfCharacterFromSet:"
- "reachableDestinationsForPerson:"
- "refreshAgainstAddressBook"
- "refreshAgainstContactsEnabled"
- "refreshDestinationStatuses"
- "refreshWithAddressBook:"
- "release"
- "reloadFriendList"
- "removeAllMetadataValues"
- "removeAllObjects"
- "removeFriendAtPosition:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObjectsInRange:"
- "removeObserver:"
- "replaceObjectsInRange:withObjectsFromArray:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "save"
- "saveFriendGroupTitles"
- "saveOperation"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "selectedPosition"
- "self"
- "serviceName"
- "set"
- "setAddressBook:"
- "setByAddingObjectsFromSet:"
- "setChangeLog:"
- "setDelegate:"
- "setDestinations:"
- "setEnableEmptyTrailingGroup:domain:"
- "setFamilyName:"
- "setFriend:atPosition:error:"
- "setFriendGroupTitleChangedExternallyNotificationName:domain:"
- "setFriends:"
- "setFriendsChangedExternallyNotificationName:domain:"
- "setGivenName:"
- "setGroupSize:domain:"
- "setLastLoadHadChanges:"
- "setMaxGroupCount:domain:"
- "setMetadataValue:forKey:"
- "setNeedsSave:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setOperationQueue:"
- "setPreferredReplyAs:"
- "setRefreshAgainstContactsEnabled:"
- "setRefreshAgainstContactsOnInitEnabled:domain:"
- "setSaveOperation:"
- "setSelectedPosition:"
- "setServiceName:"
- "setStyle:"
- "setTitle:"
- "setWithArray:"
- "setWithObject:"
- "setWithSet:"
- "set_ignoresFallbacks:"
- "sharedInstance"
- "sharedMetadataQueue"
- "shouldAllowAddingContact:withContactStore:personValueCache:"
- "shouldAllowAddingFriendWithRecordID:withFriendListManager:addressBook:personValueCache:"
- "standardUserDefaults"
- "statusForPerson:requery:"
- "stringFromPersonNameComponents:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "subarrayWithRange:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "syncFriendGroup:"
- "synchronizeUserDefaultsDomain:keys:"
- "title"
- "unsignedIntegerValue"
- "updateFromDictionaryRepresentation:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^v16"
- "v28@0:8B16@20"
- "v32@0:8@\"FKFriendGroup\"16@\"NSArray\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16^I24"
- "v32@0:8Q16@24"
- "v32@0:8^v16B24B28"
- "v32@0:8q16^{__CFString=}24"
- "v40@0:8@\"FKFriendGroup\"16@\"FKPerson\"24Q32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16Q24^I32"
- "v48@0:8@\"IDSBatchIDQueryController\"16@\"NSDictionary\"24@\"NSString\"32@\"NSError\"40"
- "v48@0:8@16@24@32@40"
- "value"
- "zone"

```
