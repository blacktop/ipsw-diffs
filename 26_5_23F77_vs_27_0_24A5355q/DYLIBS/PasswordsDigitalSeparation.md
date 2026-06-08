## PasswordsDigitalSeparation

> `/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`

```diff

-7624.2.5.10.4
-  __TEXT.__text: 0x3c28
-  __TEXT.__auth_stubs: 0x2c0
+7625.1.18.10.4
+  __TEXT.__text: 0x3a68
   __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x40d
+  __TEXT.__cstring: 0x414
   __TEXT.__oslogstring: 0x2d8
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methname: 0xc8c
-  __TEXT.__objc_methtype: 0x3cf
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x8e8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 704BD715-88E9-3CF8-8063-03134838A5D9
-  Functions: 98
-  Symbols:   82
-  CStrings:  240
+  UUID: 0B20990F-48EF-3E5D-8992-B1EC52EC9FE9
+  Functions: 96
+  Symbols:   88
+  CStrings:  53
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<DSIdentifiable>\""
- "@\"<DSIdentifiable>\"16@0:8"
- "@\"CNContactStore\""
- "@\"KCSharingGroup\""
- "@\"KCSharingParticipant\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSPersonNameComponents\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DSIdentifiable"
- "DSParticipation"
- "DSSharedResource"
- "DSSource"
- "NSObject"
- "PMSeparationGroup"
- "PMSeparationParticipant"
- "PMSeparationParticipantIdentity"
- "PMSeparationSource"
- "Q16@0:8"
- "T#,R"
- "T@\"<DSIdentifiable>\",R,N"
- "T@\"<DSIdentifiable>\",R,N,V_identity"
- "T@\"KCSharingGroup\",R,N,V_group"
- "T@\"KCSharingParticipant\",R,N,V_participant"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_participants"
- "T@\"NSPersonNameComponents\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_contactIdentifier"
- "T@\"NSString\",R,C,N,V_emailAddress"
- "T@\"NSString\",R,C,N,V_phoneNumber"
- "TQ,?,R,N"
- "TQ,R"
- "Tq,R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_contactIdentifier"
- "_contactStore"
- "_emailAddress"
- "_fetchGroupsExcludingInvitationsWithCompletionHandler:"
- "_group"
- "_groupsAndParticipantsMatchingHandle:completionHandler:"
- "_identity"
- "_leaveGroup:completionHandler:"
- "_moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupID:isForAlreadyExitedGroup:"
- "_participant"
- "_participantIdentityWithHandle:"
- "_participants"
- "_passwordsGroupWithGroup:"
- "_passwordsParticipantWithParticipant:"
- "_phoneNumber"
- "_recordGroupIdentifierForExitCleanup:completionHandler:"
- "_removeAllOtherParticipantsFromGroup:completionHandler:"
- "_removeParticipant:fromGroup:completionHandler:"
- "_stopSharingWithGroup:completionHandler:"
- "_stopSharingWithGroups:completionHandler:"
- "_stopSharingWithParticipant:inGroup:completionHandler:"
- "_stopSharingWithParticipantsMatchingHandle:completionHandler:"
- "addObject:"
- "all"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "currentUserParticipant"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "displayDetail"
- "displayName"
- "emailAddress"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "fetchSharedResourcesWithCompletion:"
- "fetchSharedResourcesWithName:completion:"
- "first"
- "firstObject"
- "getGroupByGroupID:completion:"
- "getGroupsWithRequest:completion:"
- "group"
- "groupID"
- "handle"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "identifier"
- "identity"
- "init"
- "initWithContactIdentifier:"
- "initWithEmailAddress:"
- "initWithFirst:second:"
- "initWithGroup:participants:"
- "initWithGroupID:"
- "initWithParticipant:identity:"
- "initWithPhoneNumber:"
- "initWithUpdatedGroup:"
- "inviteStatus"
- "isCurrentUser"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isStringEmailAddress:"
- "isStringPhoneNumber:"
- "leaveGroupWithRequest:completion:"
- "name"
- "nameComponents"
- "participant"
- "participants"
- "participationAccess"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permission"
- "permissionLevel"
- "phoneNumber"
- "predicateForContactsMatchingHandleStrings:"
- "q16@0:8"
- "release"
- "removeParticipant:"
- "resourceNames"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "role"
- "safari_filterObjectsUsingBlock:"
- "safari_firstObjectPassingTest:"
- "safari_mapObjectsUsingBlock:"
- "safari_privacyPreservingDescription"
- "second"
- "self"
- "sharedInstance"
- "sharedStore"
- "stopAllSharingWithCompletion:"
- "stopSharing:withCompletion:"
- "stopSharingResourcesWithName:completion:"
- "stopSharingWithParticipant:completion:"
- "stopSharingWithParticipant:forResourceName:withCompletion:"
- "stopSharingWithParticipants:completion:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "unifiedContactIdentifier"
- "unifiedContactsMatchingPredicate:keysToFetch:error:"
- "updateGroupWithRequest:completion:"
- "updateParticipantAccessLevelTo:onResource:withCompletion:"
- "updateVisibilityTo:onResource:withCompletion:"
- "v16@0:8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"<DSParticipation>\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"<DSSharedResource>\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"<DSParticipation>\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@\"<DSSharedResource>\"24@?<v@?@\"<DSSharedResource>\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v40@0:8q16@\"<DSSharedResource>\"24@?<v@?@\"<DSSharedResource>\"@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "visibility"
- "zone"

```
