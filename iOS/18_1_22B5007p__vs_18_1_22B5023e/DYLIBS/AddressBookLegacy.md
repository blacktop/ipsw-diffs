## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12718.0.0.0.0
-  __TEXT.__text: 0x719bc
-  __TEXT.__auth_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x2d34
+12721.0.0.0.0
+  __TEXT.__text: 0x7281c
+  __TEXT.__auth_stubs: 0x21b0
+  __TEXT.__objc_methlist: 0x2e14
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x25a85
-  __TEXT.__oslogstring: 0x1da8
-  __TEXT.__gcc_except_tab: 0x5c4
+  __TEXT.__cstring: 0x25f40
+  __TEXT.__oslogstring: 0x1fce
+  __TEXT.__gcc_except_tab: 0x5d4
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1850
-  __TEXT.__objc_classname: 0x4cc
-  __TEXT.__objc_methname: 0x8eeb
-  __TEXT.__objc_methtype: 0x1451
-  __TEXT.__objc_stubs: 0x79a0
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x26b0
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__unwind_info: 0x1868
+  __TEXT.__objc_classname: 0x501
+  __TEXT.__objc_methname: 0x90e9
+  __TEXT.__objc_methtype: 0x1454
+  __TEXT.__objc_stubs: 0x7b20
+  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__const: 0x26d0
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23a0
+  __DATA_CONST.__objc_selrefs: 0x2410
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__auth_got: 0x10e8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0xd5e0
-  __AUTH_CONST.__objc_const: 0x4b10
+  __AUTH_CONST.__cfstring: 0xd720
+  __AUTH_CONST.__objc_const: 0x4db0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x3d4
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x3f0
   __DATA.__data: 0x2c0
   __DATA.__common: 0x4
   __DATA.__bss: 0x338
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x128
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x390
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2360
-  Symbols:   3601
-  CStrings:  4197
+  Functions: 2385
+  Symbols:   3635
+  CStrings:  4257
 
Symbols:
+ _ABApplyLimitedAccessSyncEvents
+ _ABDropAllLimitedAccessRows
+ _ABGetWatchLimitedAccessSyncDataStartingAtSequenceNumber
+ _ABPurgeLimitedAccessRecordsForBundle
+ _ABSetLimitedAccessTableCurrentSequenceNumber
+ _OBJC_CLASS_$_ABLimitedAccessSyncData
+ _OBJC_CLASS_$_ABLimitedAccessSyncEvent
+ _OBJC_METACLASS_$_ABLimitedAccessSyncData
+ _OBJC_METACLASS_$_ABLimitedAccessSyncEvent
+ _kABLimitedAccessSyncNotification
+ _kABlimitedAccessLastFullSyncSequenceNumber
+ _kABlimitedAccessTableCurrentSequenceNumber
+ _kABlimitedAccessTableLastSequenceNumber
+ _sqlite3_bind_parameter_index
- _updateActiveState
CStrings:
+ "\x12"
+ " INNER JOIN LimitedAccess la ON la.guid IN (abp.guid, abplink.guid) WHERE la.BundleID = ? AND la.IsActive = %!i(MISSING)"
+ "!"
+ ":bundleId"
+ ":seqNumber"
+ "ABApplyLimitedAccessSyncEvents"
+ "ABApplyLimitedAccessSyncEvents sequenceNumber %!d(MISSING)"
+ "ABBufferQuery limited access for bundleIdentifier: %!{(MISSING)public}@"
+ "ABDropAllLimitedAccessRows enableFullSyncNotify %!d(MISSING)"
+ "ABGetWatchLimitedAccessSyncDataStartingAtSequenceNumber requesterSeqNum:%!d(MISSING)"
+ "ABLimitedAccess requesterSeqNum %!d(MISSING) fullSyncVersion %!d(MISSING) currentversion %!d(MISSING)"
+ "ABLimitedAccessSyncData"
+ "ABLimitedAccessSyncEvent"
+ "ABPurgeLimitedAccessRecordsForBundle bundleId:%!@(MISSING)"
+ "ABlimitedAccessLastFullSyncSequencenumber"
+ "ABlimitedAccessLastSequenceNumber"
+ "ABlimitedAccessTableCurrentSequenceNumber"
+ "BOOL ABApplyLimitedAccessSyncEvents(ABAddressBookRef, NSArray<ABLimitedAccessSyncEvent *> *)"
+ "BOOL ABDropAllLimitedAccessRows(ABAddressBookRef, BOOL)"
+ "BOOL ABPurgeLimitedAccessRecordsForBundle(ABAddressBookRef, NSString *)"
+ "CNContactStoreLimitedAccessDidChangeNotification"
+ "CREATE TRIGGER IF NOT EXISTS RemoveDeletedContactsFromLimited AFTER DELETE ON ABPerson \nBEGIN \n    DELETE FROM LimitedAccess \n    WHERE Old.guid = guid    ; \nEND; \n"
+ "CREATE TRIGGER IF NOT EXISTS UpdateLinkedContactsInLimited AFTER DELETE ON ABPersonLink \nBEGIN \n    INSERT OR IGNORE INTO LimitedAccess (BundleId, guid, SequenceNumber, IsActive) \n        SELECT la.BundleId, abp.guid, la.SequenceNumber, la.IsActive FROM LimitedAccess la, ABPerson abp \n        WHERE la.guid = OLD.guid AND abp.PersonLink = OLD.ROWID; \n    DELETE FROM LimitedAccess WHERE guid = OLD.guid; \nEND; \n"
+ "DELETE FROM LimitedAccess WHERE BundleID = :bundleId;"
+ "DELETE FROM LimitedAccess;"
+ "DROP TRIGGER IF EXISTS RemoveDeletedContactsFromLimited;"
+ "DROP TRIGGER IF EXISTS UpdateLinkedContactsInLimited;"
+ "T@\"NSArray\",&,N,V_syncEventsArray"
+ "T@\"NSEnumerator\",R,N"
+ "T@\"NSString\",&,N,V_bundleID"
+ "T@\"NSString\",&,N,V_contactID"
+ "TB,N,V_fullSyncRequired"
+ "TB,N,V_isActive"
+ "Tq,N,V_currentSequenceNumber"
+ "Tq,N,V_sequenceNumber"
+ "_bundleID"
+ "_contactID"
+ "_currentSequenceNumber"
+ "_fullSyncRequired"
+ "_initSetupPropertySet:includeLinkedContacts:hasLimitedAccess:"
+ "_isActive"
+ "_syncEventsArray"
+ "appendLimitedAccessLeftJoinToQueryString:"
+ "bundleID"
+ "contactID"
+ "currentSequenceNumber"
+ "fullSyncRequired"
+ "getCurrentSequenceNumber %!d(MISSING)"
+ "getCurrentSequenceNumber key not found, save %!d(MISSING)"
+ "getFreshSequenceNumber"
+ "getFullSyncSequenceNumber %!d(MISSING)"
+ "getFullSyncSequenceNumber key not found, save %!d(MISSING)"
+ "getLastUsedSequenceNumber %!d(MISSING)"
+ "getLastUsedSequenceNumber key not found, save %!d(MISSING)"
+ "isActive"
+ "limitedAccessBundleIdentifierForAuthorizationContext:"
+ "markFullSyncRequired"
+ "select * from LimitedAccess WHERE SequenceNumber > :seqNumber;"
+ "setBundleID:"
+ "setContactID:"
+ "setCurrentSequenceNumber:"
+ "setFullSyncRequired:"
+ "setIsActive:"
+ "setSequenceNumber:"
+ "setSyncEventsArray:"
+ "syncEvents"
+ "syncEventsArray"
+ "v32@0:8^{__CFSet=}16B24B28"
- " INNER JOIN LimitedAccess la ON la.guid = abp.guid WHERE la.BundleID = '%!@(MISSING)' AND la.IsActive = %!i(MISSING)"
- "ABBufferQuery limited access granted for bundleIdentifier: %!{(MISSING)public}@"
- "Empty bundleid passed to LimitedAccess query"
- "__ABLimitedAccessSyncTableUpdateNotification"
- "_initSetupPropertySet:includeLinkedContacts:"
- "appendLimitedAccessLeftJoinQueryString:forBundleIdentifier:"
- "appendLimitedAccessToQueryString:authorizationContext:"
- "v28@0:8^{__CFSet=}16B24"

```
