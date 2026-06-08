## CorrectionsProfilesSync

> `/System/Library/Assistant/Plugins/CorrectionsProfilesSync.assistantBundle/CorrectionsProfilesSync`

```diff

-3525.5.12.11.2
-  __TEXT.__text: 0x189c
-  __TEXT.__auth_stubs: 0x290
+3600.62.21.1.5
+  __TEXT.__text: 0x172c
   __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x1f3
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__cstring: 0x1f9
   __TEXT.__oslogstring: 0x22d
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x818
-  __TEXT.__objc_methtype: 0x36a
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x528
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5C0D4C5-D603-35C5-845C-F50678A43AF2
+  UUID: C9AD1441-E2DD-3737-AB3A-BEDF653B6CA6
   Functions: 27
-  Symbols:   72
-  CStrings:  193
+  Symbols:   75
+  CStrings:  39
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x8
- _objc_release_x28
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AFSyncSnapshot\"16@0:8"
- "@\"AFSyncSnapshot\"24@0:8@\"NSString\"16"
- "@\"CorrectionsProfilesLastState\""
- "@\"CorrectionsProfilesPersistedState\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AFSyncHandler"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CorrectionsProfilesLastState"
- "CorrectionsProfilesPersistedState"
- "CorrectionsProfilesSyncHandler"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSDictionary\",&,N,V_correctionsProfiles"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_digest"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "TQ,R,N,V_count"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_correctionProfileKeysToDelete"
- "_correctionProfileKeysToSync"
- "_correctionProfiles"
- "_correctionsProfiles"
- "_count"
- "_digest"
- "_lastState"
- "_loadCorrectionProfiles"
- "_path"
- "_persistedState"
- "absoluteString"
- "addObject:"
- "allKeys"
- "appendFormat:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autorelease"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:configuration:"
- "beginSyncWithAnchor:validity:forKey:beginInfo:"
- "beginSyncWithInfo:configuration:"
- "bytes"
- "class"
- "compare:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "correctionKeys"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentSyncSnapshot"
- "dataWithContentsOfFile:options:error:"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "defaultSynchedKnowledgeStore"
- "description"
- "dictionaryRepresentationAndReturnError:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "fileExistsAtPath:"
- "firstObject"
- "getChangeAfterAnchor:changeInfo:"
- "hash"
- "init"
- "initWithArray:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithFormat:"
- "initWithString:"
- "integerValue"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "length"
- "loadLastState"
- "mutableCopy"
- "name"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "profileDataForKey:"
- "release"
- "removeItemAtPath:error:"
- "removeLastObject"
- "resetWithValidity:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveNewState:"
- "scheme"
- "self"
- "setCorrectionEntryData:"
- "setCorrectionsProfiles:"
- "setDigest:"
- "setIdentifier:"
- "setIsDelete:"
- "setObject:"
- "setObject:forKey:"
- "setPostAnchor:"
- "setWithObject:"
- "setWithObjects:"
- "sortUsingComparator:"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "syncDidEnd"
- "syncSnapshotForKey:"
- "syncVerificationKeyForKey:"
- "unarchivedObjectOfClasses:fromData:error:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@\"<AFSyncBeginInfo>\"16@\"<AFSyncConfiguration>\"24"
- "v32@0:8@\"NSString\"16@\"<AFSyncChangeInfo>\"24"
- "v32@0:8@16@24"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"<AFSyncBeginInfo>\"40"
- "v48@0:8@16@24@32@40"
- "v56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48"
- "v56@0:8@16@24q32@40@48"
- "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48@\"<AFSyncConfiguration>\"56"
- "v64@0:8@16@24q32@40@48@56"
- "writeToFile:options:error:"
- "zone"

```
