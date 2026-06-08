## SynapseSyncPlugin

> `/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/SynapseSyncPlugin`

```diff

-3525.5.12.11.2
-  __TEXT.__text: 0x15fc
-  __TEXT.__auth_stubs: 0x210
+3600.62.21.1.5
+  __TEXT.__text: 0x14a8
   __TEXT.__objc_methlist: 0x224
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x16f
+  __TEXT.__cstring: 0x171
   __TEXT.__oslogstring: 0x41b
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x77c
-  __TEXT.__objc_methtype: 0x30d
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BAF2F13-078C-370E-ABD2-F31DE094E4C8
+  UUID: 563D365E-EC72-3793-B8D1-B68010494D82
   Functions: 12
   Symbols:   57
-  CStrings:  168
+  CStrings:  31
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AFSyncSnapshot\"16@0:8"
- "@\"AFSyncSnapshot\"24@0:8@\"NSString\"16"
- "@\"NSEnumerator\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "AFSyncHandler"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B48@0:8@16@24q32@40"
- "NSObject"
- "Q16@0:8"
- "SynapseSyncIdentifiers"
- "SynapseSyncPlugin"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URL"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_af_preferredBundleID"
- "_anchorEnumerator"
- "_checkIfResetIsNeededForSyncTransaction:validity:serverCountOfItems:startAnchorFromServer:"
- "_clearChangeInfo"
- "_currentSyncSlotAllowedToSync"
- "_deletedIDs"
- "_newItems"
- "_prepareToVendChangeInfoForSyncTransaction:startAnchorFromServer:"
- "_siriID"
- "_siri_UUIDWithDomainObjectIdentifier:"
- "_siri_domainObjectIdentifier"
- "addObject:"
- "anchor"
- "appMetadata"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:configuration:"
- "beginSyncWithAnchor:validity:forKey:beginInfo:"
- "beginSyncWithInfo:configuration:"
- "beginTransactionForBundleID:bundlePath:syncSlot:"
- "calculateDiff"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentSyncSnapshot"
- "debugDescription"
- "deletedSiriIDs"
- "description"
- "dictionaryWithCapacity:"
- "endTransactionWithFinalAnchor:"
- "firstObject"
- "fullResetRequired"
- "getChangeAfterAnchor:changeInfo:"
- "getDisallowedSyncSlotNames"
- "hash"
- "host"
- "init"
- "initWithUUIDString:"
- "isEqual:"
- "isFullReset"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSyncSlotNameAllowedToSync:"
- "lastObject"
- "latestVocabularyDocument"
- "length"
- "longLongValue"
- "nextObject"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectEnumerator"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "resetWithValidity:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheme"
- "self"
- "sentVocabularyDocument"
- "setFullResetRequired:"
- "setHost:"
- "setIdentifier:"
- "setIntentSlotValue:"
- "setIsDelete:"
- "setObject:"
- "setObject:forKeyedSubscript:"
- "setPath:"
- "setPostAnchor:"
- "setScheme:"
- "setVocabularyIdentifier:"
- "string"
- "stringValue"
- "superclass"
- "syncDidEnd"
- "syncSlots"
- "syncSnapshotForKey:"
- "syncVerificationKeyForKey:"
- "thisGeneration"
- "updatedVocabularyItems"
- "v16@0:8"
- "v32@0:8@\"<AFSyncBeginInfo>\"16@\"<AFSyncConfiguration>\"24"
- "v32@0:8@\"NSString\"16@\"<AFSyncChangeInfo>\"24"
- "v32@0:8@16@24"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"<AFSyncBeginInfo>\"40"
- "v48@0:8@16@24@32@40"
- "v56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48"
- "v56@0:8@16@24q32@40@48"
- "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48@\"<AFSyncConfiguration>\"56"
- "v64@0:8@16@24q32@40@48@56"
- "validity"
- "vocabularyIdentifier"
- "vocabularyItems"
- "zone"

```
