## ContextKitCore

> `/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore`

```diff

-302.0.0.0.0
-  __TEXT.__text: 0x200c
-  __TEXT.__auth_stubs: 0x2b0
+305.0.0.0.0
+  __TEXT.__text: 0x1d78
   __TEXT.__objc_methlist: 0x3ec
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1ff
-  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__cstring: 0x207
+  __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__oslogstring: 0x97
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0xbcc
-  __TEXT.__objc_methtype: 0x156
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x320
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7367B180-AEC5-38CA-9180-AB30B8D534F2
+  UUID: FA8DBE28-137B-3320-9AEC-1C68591D92CF
   Functions: 76
-  Symbols:   377
-  CStrings:  253
+  Symbols:   375
+  CStrings:  70
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x23
CStrings:
- ".cxx_destruct"
- "@\"CKContextUserActivity\""
- "@\"IOSurface\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"NSUserActivity\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "AB"
- "B16@0:8"
- "CKContextDonation"
- "CKContextDonationItem"
- "CKContextDonationServiceProtocol"
- "CKContextUserActivity"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T@\"CKContextUserActivity\",&,N,V_associatedUserActivity"
- "T@\"IOSurface\",&,N,SsetLeadImage:,V_leadImage"
- "T@\"IOSurface\",&,N,SsetSnapshot:,V_snapshot"
- "T@\"NSArray\",&,N,V_extractionItems"
- "T@\"NSArray\",&,N,V_uiElements"
- "T@\"NSArray\",R,N,V_items"
- "T@\"NSDate\",W,N"
- "T@\"NSNumber\",C,N,V_numberOfOccurrences"
- "T@\"NSString\",&,N,V_debugText"
- "T@\"NSString\",&,N,V_debugUrlString"
- "T@\"NSString\",C,N,SsetContentAuthor:,V_contentAuthor"
- "T@\"NSString\",C,N,SsetContentDescription:,V_contentDescription"
- "T@\"NSString\",C,N,SsetContentKeywords:,V_contentKeywords"
- "T@\"NSString\",C,N,SsetRawHTML:,V_rawHTML"
- "T@\"NSString\",C,N,SsetText:,V_text"
- "T@\"NSString\",C,N,SsetTitle:,V_title"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_languageTag"
- "T@\"NSString\",R,N,V_donorBundleIdentifier"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NSUserActivity\",R,N,V_userActivity"
- "TB,R"
- "TQ,N,V_nonce"
- "TQ,V_remoteProcesses"
- "Vv24@0:8@\"CKContextDonation\"16"
- "Vv24@0:8@16"
- "_associatedUserActivity"
- "_bundleIdentifier"
- "_concatenatedRequestTextUsingDebugText:"
- "_contentAuthor"
- "_contentDescription"
- "_contentKeywords"
- "_createUserActivityDataWithOptions:completionHandler:"
- "_debugText"
- "_debugUrlString"
- "_donated"
- "_donorBundleIdentifier"
- "_extractionItems"
- "_initWithUserActivityData:"
- "_items"
- "_languageTag"
- "_leadImage"
- "_nonce"
- "_numberOfOccurrences"
- "_rawHTML"
- "_recordedTimeIntervalSince1970"
- "_remoteProcesses"
- "_snapshot"
- "_text"
- "_title"
- "_uiElements"
- "_userActivity"
- "_userActivityData"
- "_uuid"
- "activityType"
- "addItem:"
- "addObject:"
- "addObjectsFromArray:"
- "allocWithZone:"
- "associatedUserActivity"
- "componentsJoinedByString:"
- "concatenatedRequestsDebugText"
- "concatenatedRequestsText"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "dateWithTimeIntervalSince1970:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "donate"
- "donate:"
- "donorBundleIdentifier"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "entryDate"
- "establishServiceConnection"
- "hash"
- "init"
- "initWithCapacity:"
- "initWithCharactersNoCopy:length:freeWhenDone:"
- "initWithCoder:"
- "initWithDonations:donorBundleIdentifier:"
- "initWithDonorBundleIdentifier:"
- "initWithServiceName:"
- "initWithUserActivity:"
- "initialize"
- "interfaceWithProtocol:"
- "invalidate"
- "items"
- "length"
- "prepareForDonationWithCompletionHandler:"
- "referrerURL"
- "resume"
- "setAssociatedUserActivity:"
- "setBundleIdentifier:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setContentAuthor:"
- "setContentDescription:"
- "setContentKeywords:"
- "setDebugText:"
- "setDebugUrlString:"
- "setEntryDate:"
- "setExtractionItems:"
- "setLanguageTag:"
- "setLeadImage:"
- "setNonce:"
- "setNumberOfOccurrences:"
- "setRawHTML:"
- "setRemoteObjectInterface:"
- "setRemoteProcesses:"
- "setSnapshot:"
- "setText:"
- "setTitle:"
- "setUiElements:"
- "setWithObject:"
- "setWithObjects:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSince1970"
- "trimTextToSize:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "webpageURL"

```
