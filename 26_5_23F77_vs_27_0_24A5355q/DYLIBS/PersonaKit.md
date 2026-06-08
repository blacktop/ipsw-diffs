## PersonaKit

> `/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit`

```diff

-1366.500.41.0.0
-  __TEXT.__text: 0x699c
-  __TEXT.__auth_stubs: 0x360
+1372.100.2.0.0
+  __TEXT.__text: 0x5f44
   __TEXT.__objc_methlist: 0x8a0
   __TEXT.__const: 0x59
-  __TEXT.__cstring: 0x1098
+  __TEXT.__cstring: 0x10a3
   __TEXT.__oslogstring: 0xb2f
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x172f
-  __TEXT.__objc_methtype: 0x866
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0xe68
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x180
   __DATA.__bss: 0x30

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CC68ABA-B5A5-3726-AF72-F2F8FFCDC6C6
+  UUID: 209B0381-45AF-378B-A2F2-7548BDB759AF
   Functions: 169
-  Symbols:   644
-  CStrings:  583
+  Symbols:   648
+  CStrings:  219
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
Functions:
~ -[PRLikeness init] : 108 -> 100
~ -[PRLikeness _initWithIdentifier:] : 152 -> 160
~ -[PRLikeness initWithCoder:] : 1140 -> 1028
~ -[PRLikeness encodeWithCoder:] : 520 -> 496
~ +[PRLikeness likenessWithPropagatedData:] : 440 -> 380
~ -[PRLikeness setRecipe:] : 124 -> 120
~ -[PRLikeness setExternalIdentifier:] : 124 -> 120
~ -[PRLikeness staticRepresentation] : 400 -> 348
~ -[PRLikeness staticRepresentationData] : 588 -> 524
~ -[PRLikeness setStaticRepresentationData:] : 56 -> 48
~ +[PRLikeness scopeFromDescription:] : 100 -> 96
~ -[PRLikeness description] : 804 -> 740
~ +[PRLikeness _dateFormatter] : 84 -> 68
~ -[PRLikeness setCreationDate:] : 64 -> 12
~ -[PRLikeness setExpirationDate:] : 64 -> 12
~ -[PRLikeness setSoftExpirationDate:] : 64 -> 12
~ -[PRLikeness setOwnerID:] : 64 -> 12
~ -[PRLikeness setInsertionDate:] : 64 -> 12
~ -[PRLikeness setDirtyProperties:] : 64 -> 12
~ -[NSString(PersonaKit) pr_SHADigest] : 220 -> 224
~ -[NSString(PersonaKit) pr_numericValue] : 208 -> 188
~ +[NSString(PersonaKit) pr_hexStringWithData:] : 196 -> 192
~ +[PRPersonaServiceInterface XPCInterface] : 84 -> 68
~ ___41+[PRPersonaServiceInterface XPCInterface]_block_invoke : 308 -> 296
~ -[NSError(PersonaKit) pr_isNetworkAvailabilityError] : 284 -> 276
~ -[NSError(PersonaKit) pr_isInPersonaDomain] : 68 -> 64
~ -[PRPersonaStore _setHasVendedData:] : 224 -> 176
~ -[PRPersonaStore currentLikenessForPrimaryiCloudAccountWithDesiredFreshness:completion:] : 332 -> 288
~ ___88-[PRPersonaStore currentLikenessForPrimaryiCloudAccountWithDesiredFreshness:completion:]_block_invoke : 472 -> 428
~ -[PRPersonaStore allLikenessesForPrimaryiCloudAccountWithCompletion:] : 332 -> 288
~ ___69-[PRPersonaStore allLikenessesForPrimaryiCloudAccountWithCompletion:]_block_invoke : 472 -> 428
~ -[PRPersonaStore likenessForPhoneNumber:desiredFreshness:completion:] : 372 -> 336
~ ___69-[PRPersonaStore likenessForPhoneNumber:desiredFreshness:completion:]_block_invoke : 496 -> 452
~ -[PRPersonaStore likenessForEmailAddress:desiredFreshness:completion:] : 372 -> 336
~ ___70-[PRPersonaStore likenessForEmailAddress:desiredFreshness:completion:]_block_invoke : 496 -> 452
~ -[PRPersonaStore saveLikeness:forPrimayiCloudAccountWithCompletion:] : 332 -> 288
~ ___68-[PRPersonaStore saveLikeness:forPrimayiCloudAccountWithCompletion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore changeCurrentSelfLikenessToLikenessWithUniqueID:completion:] : 356 -> 316
~ ___77-[PRPersonaStore changeCurrentSelfLikenessToLikenessWithUniqueID:completion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore removeLikeness:forPrimayiCloudAccountWithCompletion:] : 356 -> 316
~ ___70-[PRPersonaStore removeLikeness:forPrimayiCloudAccountWithCompletion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore removeAllLikenessForPrimaryiCloudAccountWithCompletion:] : 332 -> 288
~ ___73-[PRPersonaStore removeAllLikenessForPrimaryiCloudAccountWithCompletion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore handleAppleIDEvent:account:completion:] : 408 -> 364
~ ___56-[PRPersonaStore handleAppleIDEvent:account:completion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore donateLikeness:forEmailAddress:completion:] : 372 -> 336
~ ___60-[PRPersonaStore donateLikeness:forEmailAddress:completion:]_block_invoke : 472 -> 424
~ -[PRPersonaStore donateLikeness:forPhoneNumber:completion:] : 372 -> 336
~ ___59-[PRPersonaStore donateLikeness:forPhoneNumber:completion:]_block_invoke : 472 -> 424
~ -[PRPersonaStore likenessesWithExternalIdentifier:completion:] : 372 -> 336
~ ___62-[PRPersonaStore likenessesWithExternalIdentifier:completion:]_block_invoke : 504 -> 460
~ -[PRPersonaStore screenNameForEmailAddress:completion:] : 408 -> 368
~ ___55-[PRPersonaStore screenNameForEmailAddress:completion:]_block_invoke : 492 -> 448
~ -[PRPersonaStore screenNameForPhoneNumber:completion:] : 408 -> 368
~ ___54-[PRPersonaStore screenNameForPhoneNumber:completion:]_block_invoke : 492 -> 448
~ -[PRPersonaStore screenNameForPrimaryiCloudAccountWithCompletion:] : 368 -> 320
~ ___66-[PRPersonaStore screenNameForPrimaryiCloudAccountWithCompletion:]_block_invoke : 464 -> 420
~ -[PRPersonaStore screenNameForAppleIDWithAltDSID:completion:] : 408 -> 368
~ ___61-[PRPersonaStore screenNameForAppleIDWithAltDSID:completion:]_block_invoke : 492 -> 448
~ -[PRPersonaStore setScreenName:forPrimaryiCloudAccountWithCompletion:] : 368 -> 320
~ ___70-[PRPersonaStore setScreenName:forPrimaryiCloudAccountWithCompletion:]_block_invoke : 444 -> 396
~ -[PRPersonaStore setScreenName:forAppleIDWithAltDSID:completion:] : 408 -> 368
~ ___65-[PRPersonaStore setScreenName:forAppleIDWithAltDSID:completion:]_block_invoke : 472 -> 424
~ -[PRPersonaStore _startListeningForCacheChangeNotifications] : 288 -> 240
~ __PRHandleSelfCacheDidChange : 368 -> 316
~ __PRHandleOtherCacheDidChange : 368 -> 316
~ -[PRPersonaStore _stopListeningForCacheChangeNotifications] : 248 -> 200
~ +[PRLikenessChange changeForLikeness:withType:] : 276 -> 252
~ +[PRLikenessChange changeTypeFromDescription:] : 92 -> 88
~ -[PRLikenessChange description] : 152 -> 144
~ __PRGetLogSystem : 84 -> 68
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSLock\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{CGImage=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^{CGImage=}24"
- "@32@0:8Q16^{CGImage=}24"
- "@40@0:8:16@24@32"
- "@40@0:8Q16@24^{CGImage=}32"
- "@56@0:8^{CGImage=}16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@64@0:8Q16^{CGImage=}24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "PRLikeness"
- "PRLikenessChange"
- "PRManagedLikeness"
- "PRManagedLikenessChange"
- "PRManagedPropagationEvent"
- "PRManagedScreenName"
- "PRPersonaServiceInterface"
- "PRPersonaServiceProtocol"
- "PRPersonaStore"
- "PersonaKit"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"NSArray\",C,N,V_dirtyLikenessProperties"
- "T@\"NSData\",&,N"
- "T@\"NSData\",C,N,V_recipe"
- "T@\"NSDate\",&,D,N"
- "T@\"NSDate\",&,N,V_creationDate"
- "T@\"NSDate\",&,N,V_expirationDate"
- "T@\"NSDate\",&,N,V_insertionDate"
- "T@\"NSDate\",&,N,V_softExpirationDate"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSNumber\",C,N,V_changedLikenessVersion"
- "T@\"NSSet\",&,N,V_dirtyProperties"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",&,N,V_ownerID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_changedLikenessID"
- "T@\"NSString\",C,N,V_externalIdentifier"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_uniqueIdentifier"
- "TB,N,SsetCurrent:,V_isCurrent"
- "TB,R"
- "TB,R,N"
- "TQ,N,V_scope"
- "TQ,N,V_type"
- "TQ,N,V_version"
- "TQ,R"
- "Tq,N,V_source"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cropRectForTopLeftOrigin"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XPCInterface"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_changedLikenessID"
- "_changedLikenessVersion"
- "_connectionLock"
- "_dataVendingFlagLock"
- "_dateFormatter"
- "_dirtyLikenessProperties"
- "_flippedRectForRect:relativeToImage:"
- "_hasVendedData"
- "_identifier"
- "_initWithIdentifier:"
- "_ownerID"
- "_personaServiceConnection"
- "_photoWithScope:image:cropRectForTopLeftOrigin:"
- "_replyHandlingQueue"
- "_serviceListenerEndpoint"
- "_setHasVendedData:"
- "_source"
- "_startListeningForCacheChangeNotifications"
- "_staticRepresentation"
- "_stopListeningForCacheChangeNotifications"
- "addObject:"
- "allLikenessesForPrimaryiCloudAccountWithCompletion:"
- "allObjects"
- "appendBytes:length:"
- "appendFormat:"
- "automaticallyNotifiesObserversOfCropRectForTopLeftOrigin"
- "autorelease"
- "boolValue"
- "bytes"
- "changeCurrentSelfLikenessToLikenessWithUniqueID:completion:"
- "changeForLikeness:withType:"
- "changeTypeFromDescription:"
- "changedID"
- "changedLikenessID"
- "changedLikenessVersion"
- "changedProperties"
- "changedVersion"
- "characterSetWithCharactersInString:"
- "class"
- "clearDirtyProperties"
- "code"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "copy"
- "count"
- "creationDate"
- "cropRectHeight"
- "cropRectWidth"
- "cropRectX"
- "cropRectY"
- "currentLikenessForPrimaryiCloudAccountWithCompletion:"
- "currentLikenessForPrimaryiCloudAccountWithDesiredFreshness:completion:"
- "dataForPropagation"
- "dateAdded"
- "dateCreated"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "description"
- "descriptionForChangeType:"
- "descriptionForScope:"
- "didChangeValueForKey:"
- "diddlySquatLikeness"
- "dirtyLikenessProperties"
- "dirtyProperties"
- "domain"
- "donateLikeness:forEmailAddress:completion:"
- "donateLikeness:forPhoneNumber:completion:"
- "donateLikenessData:forSenderID:isPhoneNumber:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "expiration"
- "expirationDate"
- "externalID"
- "externalIdentifier"
- "handleAppleIDEvent:account:completion:"
- "hasVendedData"
- "hash"
- "identifier"
- "init"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithServiceListenerEndpoint:"
- "insertionDate"
- "interfaceWithProtocol:"
- "invalidate"
- "invertedSet"
- "isCurrent"
- "isDiddlySquat"
- "isDirty"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "likenessDataForPropagationToRecipient:lastContactDate:"
- "likenessForEmailAddress:completion:"
- "likenessForEmailAddress:desiredFreshness:completion:"
- "likenessForPhoneNumber:completion:"
- "likenessForPhoneNumber:desiredFreshness:completion:"
- "likenessForPropagationToRecipient:lastContactDate:completion:"
- "likenessVersionDigestForEmail:"
- "likenessVersionDigestForEmail:completion:"
- "likenessVersionDigestForPhoneNumber:"
- "likenessVersionDigestForPhoneNumber:completion:"
- "likenessWithPropagatedData:"
- "likenessWithUniqueID:"
- "likenessWithUniqueID:completion:"
- "likenessesWithExternalIdentifier:completion:"
- "lock"
- "longLongValue"
- "monogramWithRecipe:staticRepresentation:"
- "monogramWithScope:recipe:staticRepresentation:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "ownerID"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "photoWithImage:"
- "photoWithImage:cropRect:"
- "photoWithImage:cropRectForBottomLeftOrigin:"
- "photoWithImage:cropRectForTopLeftOrigin:"
- "photoWithScope:image:"
- "postNotificationName:object:"
- "pr_SHADigest"
- "pr_errorWithCode:"
- "pr_hexStringWithData:"
- "pr_isInPersonaDomain"
- "pr_isNetworkAvailabilityError"
- "pr_numericValue"
- "q"
- "q16@0:8"
- "recipientID"
- "release"
- "removeAllLikenessForPrimaryiCloudAccountWithCompletion:"
- "removeAllObjects"
- "removeLikeness:forPrimayiCloudAccountWithCompletion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveLikeness:forPrimayiCloudAccountWithCompletion:"
- "scope"
- "scopeDescription"
- "scopeFromDescription:"
- "screenNameForAppleIDWithAltDSID:completion:"
- "screenNameForEmailAddress:completion:"
- "screenNameForPhoneNumber:completion:"
- "screenNameForPrimaryiCloudAccountWithCompletion:"
- "self"
- "sentVersion"
- "setChangedLikenessID:"
- "setChangedLikenessVersion:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCreationDate:"
- "setCropRect:"
- "setCropRectForTopLeftOrigin:"
- "setCurrent:"
- "setDateStyle:"
- "setDirtyLikenessProperties:"
- "setDirtyProperties:"
- "setExpirationDate:"
- "setExternalIdentifier:"
- "setIdentifier:"
- "setInsertionDate:"
- "setLikeness:forPrimayiCloudAccountWithCompletion:"
- "setLikenessVersionDigest:forEmail:"
- "setLikenessVersionDigest:forEmail:completion:"
- "setLikenessVersionDigest:forPhoneNumber:"
- "setLikenessVersionDigest:forPhoneNumber:completion:"
- "setName:"
- "setOwnerID:"
- "setRecipe:"
- "setScope:"
- "setScreenName:forAppleIDWithAltDSID:completion:"
- "setScreenName:forPrimaryiCloudAccountWithCompletion:"
- "setSoftExpirationDate:"
- "setSource:"
- "setStaticRepresentation:"
- "setStaticRepresentationData:"
- "setTimeStyle:"
- "setType:"
- "setVersion:"
- "setWithObjects:"
- "softExpiration"
- "softExpirationDate"
- "source"
- "staticRepresentation"
- "staticRepresentationData"
- "staticRepresentationFileID"
- "stringFromDate:"
- "stringWithFormat:"
- "subdataWithRange:"
- "superclass"
- "supportsSecureCoding"
- "timestamp"
- "type"
- "typeDescription"
- "uniqueID"
- "uniqueIdentifier"
- "unlock"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8^{CGImage=}16"
- "v24@0:8q16"
- "v28@0:8C16@20"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?C@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"PRLikeness\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?C@\"NSError\">24"
- "v32@0:8@\"PRLikeness\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"PRLikeness\"@\"NSError\">24"
- "v36@0:8@16@24B32"
- "v36@0:8C16@\"NSNumber\"20@?<v@?B@\"NSError\">28"
- "v36@0:8C16@\"NSString\"20@?<v@?B@\"NSError\">28"
- "v36@0:8C16@20@?28"
- "v40@0:8@\"NSNumber\"16Q24@?<v@?@\"PRLikeness\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDate\"24@?<v@?@\"PRLikeness\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"PRLikeness\"@\"NSError\">32"
- "v40@0:8@\"PRLikeness\"16@\"NSNumber\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"PRLikeness\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16@\"ACAccount\"24@?<v@?B@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "value"
- "version"
- "willChangeValueForKey:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGImage=}48"

```
