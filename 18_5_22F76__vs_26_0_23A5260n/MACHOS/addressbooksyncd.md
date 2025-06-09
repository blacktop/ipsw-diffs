## addressbooksyncd

> `/usr/libexec/addressbooksyncd`

```diff

-283.3.0.0.0
-  __TEXT.__text: 0x36118
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x7180
-  __TEXT.__objc_methlist: 0x4140
+288.0.0.0.0
+  __TEXT.__text: 0x3a610
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x78e0
+  __TEXT.__objc_methlist: 0x4568
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x824
-  __TEXT.__objc_methname: 0x7cef
-  __TEXT.__cstring: 0x2ba8
-  __TEXT.__objc_classname: 0x60e
-  __TEXT.__objc_methtype: 0x1321
-  __TEXT.__oslogstring: 0x229f
-  __TEXT.__unwind_info: 0xc80
-  __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0xda8
-  __DATA_CONST.__cfstring: 0x32c0
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __TEXT.__gcc_except_tab: 0x978
+  __TEXT.__objc_methname: 0x848e
+  __TEXT.__cstring: 0x2c91
+  __TEXT.__objc_classname: 0x647
+  __TEXT.__objc_methtype: 0x13e7
+  __TEXT.__oslogstring: 0x235e
+  __TEXT.__unwind_info: 0xd30
+  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__const: 0xec0
+  __DATA_CONST.__cfstring: 0x3320
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0xb58
-  __DATA.__objc_const: 0x8fe0
-  __DATA.__objc_selrefs: 0x2570
-  __DATA.__objc_ivar: 0x49c
-  __DATA.__objc_data: 0x1270
-  __DATA.__data: 0x6f8
+  __DATA.__objc_const: 0x9520
+  __DATA.__objc_selrefs: 0x27a8
+  __DATA.__objc_ivar: 0x4e0
+  __DATA.__objc_data: 0x1310
+  __DATA.__data: 0x6f0
   __DATA.__bss: 0x158
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/AddressBook.framework/AddressBook
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 30FC8BF1-A893-3DBE-BD51-8BDC267F614D
-  Functions: 1524
-  Symbols:   403
-  CStrings:  3091
+  UUID: D5858F35-51CF-3C44-A8C4-49E83788A33D
+  Functions: 1625
+  Symbols:   409
+  CStrings:  3212
 
Symbols:
+ _OBJC_CLASS_$_CNFavorites
+ _OBJC_CLASS_$_CNFavoritesEntry
+ _OBJC_CLASS_$_LSApplicationRecord
+ _PBDataWriterWriteUint64Field
+ _kABPersonEmailProperty
+ _kABPersonInstantMessageProperty
+ _kABPersonPhoneProperty
+ _kABPersonSocialProfileProperty
+ _objc_retain_x26
+ _objc_retain_x28
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "%lx"
+ "1"
+ "== Started AddressBookSync-288"
+ "@\"ABSPBLimitedAccessSyncData\""
+ "@\"CNFavorites\""
+ "@\"CNLimitedAccessSyncData\""
+ "@48@0:8@16@24@32@40"
+ "ABSPBLimitedAccessObject"
+ "ABSPBLimitedAccessSyncData"
+ "B16@?0@\"ABSContactsSyncObject\"8"
+ "B16@?0@\"CNLimitedAccessSyncData\"8"
+ "B40@0:8@16@24@32"
+ "CNContactStoreLimitedAccessDidChangeNotification"
+ "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
+ "Enqueueing sync data"
+ "Error mapping %@ to counterpart bundle id"
+ "LMA_SEQUENCE_NUMBER_KEY"
+ "LimitedAccessSync"
+ "No sync data? hmm...."
+ "Not updating LMA token, shouldHandleLimitedAccessSyncs said no"
+ "Received CNContactStoreLimitedAccessDidChangeNotification"
+ "Shouldn't save LMA info on iOS, aborting...."
+ "T@\"ABSPBLimitedAccessSyncData\",&,N,V_lmaSyncData"
+ "T@\"CNLimitedAccessSyncData\",&,N,V_lmaData"
+ "T@\"CNLimitedAccessSyncData\",&,N,V_lmaSyncData"
+ "T@\"NSMutableArray\",&,N,V_dictionaryKeys"
+ "T@\"NSMutableArray\",&,N,V_dictionaryValues"
+ "T@\"NSMutableArray\",&,N,V_syncEvents"
+ "T@\"NSString\",&,N,V_bundleID"
+ "T@\"NSString\",&,N,V_contactID"
+ "T@\"NSString\",&,N,V_propertyKey"
+ "T@?,C,N,V_lmaDiffBlock"
+ "TB,N,V_fullSyncRequired"
+ "TB,N,V_isActive"
+ "TQ,N,V_currentSequenceNumber"
+ "TQ,N,V_sequenceNumber"
+ "_bundleID"
+ "_contactID"
+ "_currentSequenceNumber"
+ "_dictionaryKeys"
+ "_dictionaryValues"
+ "_favorites"
+ "_fullSyncRequired"
+ "_isActive"
+ "_lmaData"
+ "_lmaDiffBlock"
+ "_lmaSyncData"
+ "_propertyKey"
+ "_setError"
+ "_shouldReallySendDeltaSessionWithAnchor:lmaData:store:"
+ "_syncEvents"
+ "addDictionaryKeys:"
+ "addDictionaryValues:"
+ "addOrUpdateLMAIn:forSession:"
+ "addSyncEvents:"
+ "allValues"
+ "bundleID"
+ "clearDictionaryKeys"
+ "clearDictionaryValues"
+ "clearSyncEvents"
+ "contactID"
+ "contactProperty"
+ "contactPropertyKeyToProperty:"
+ "counterpartIdentifiers"
+ "currentSequenceNumber"
+ "dictionaryKeys"
+ "dictionaryKeysAtIndex:"
+ "dictionaryKeysCount"
+ "dictionaryKeysType"
+ "dictionaryValues"
+ "dictionaryValuesAtIndex:"
+ "dictionaryValuesCount"
+ "dictionaryValuesType"
+ "entries"
+ "enumerateContactsAdd:remove:lmaAdd:"
+ "fullSyncRequired"
+ "getBytes:range:"
+ "getWatchLimitedAccessSyncDataStartingAtSequenceNumber:"
+ "hasBundleID"
+ "hasContactID"
+ "hasCurrentSequenceNumber"
+ "hasError"
+ "hasFullSyncRequired"
+ "hasIsActive"
+ "hasLmaSyncData"
+ "hasPropertyKey"
+ "iOSLegacyIdentifier"
+ "initWithAnchor:keys:store:lmaData:"
+ "initWithArray:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithContactStore:"
+ "initWithKeys:store:lmaData:"
+ "initWithLMASyncData:"
+ "isActive"
+ "key"
+ "limitedAccessSequenceNumber:"
+ "limitedAccessSyncEnabled"
+ "lmaCounterpartAppBundleIDForBundleID:"
+ "lmaData"
+ "lmaDiffBlock"
+ "lmaSyncData"
+ "mapCNContactPropertyKeyToABProperty:"
+ "numberWithUnsignedLongLong:"
+ "position"
+ "propertyKey"
+ "setBundleID:"
+ "setContactID:"
+ "setCurrentSequenceNumber:"
+ "setDictionaryKeys:"
+ "setDictionaryValues:"
+ "setFullSyncRequired:"
+ "setHasCurrentSequenceNumber:"
+ "setHasFullSyncRequired:"
+ "setHasIsActive:"
+ "setIsActive:"
+ "setLmaData:"
+ "setLmaDiffBlock:"
+ "setLmaSyncData:"
+ "setPosition:"
+ "setPropertyKey:"
+ "setSyncEvents:"
+ "shouldHandleLimitedAccessSyncs"
+ "syncEvents"
+ "syncEventsAtIndex:"
+ "syncEventsCount"
+ "syncEventsType"
+ "updateLMATokenForSession:"
+ "v40@0:8@?16@?24@?32"
+ "{?=\"currentSequenceNumber\"b1\"fullSyncRequired\"b1}"
+ "{?=\"sequenceNumber\"b1\"isActive\"b1}"
- "/var/mobile/Library/Preferences/com.apple.mobilephone.speeddial.plist"
- "13V"
- "== Started AddressBookSync-283.3"
- "ABIdentifier"
- "ABUid"
- "ActionType"
- "BundleIdentifier"
- "EntryType"
- "Label"
- "Name"
- "Property"
- "T@\"NSArray\",R,N,V_favoritesList"
- "Value"
- "_favoritesList"
- "_shouldReallySendDeltaSessionWithAnchor:store:"
- "arrayWithContentsOfFile:"
- "dataWithContentsOfFile:"
- "enumerateContactsAdd:remove:"
- "favoritesList"
- "initWithAnchor:keys:store:"
- "predicateForLegacyIdentifier:"
- "v32@0:8@?16@?24"

```
