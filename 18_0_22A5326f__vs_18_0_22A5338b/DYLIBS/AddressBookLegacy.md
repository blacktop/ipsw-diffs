## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12720.0.0.0.0
-  __TEXT.__text: 0x72720
+12721.0.0.0.0
+  __TEXT.__text: 0x7281c
   __TEXT.__auth_stubs: 0x21b0
   __TEXT.__objc_methlist: 0x2e14
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x25d55
-  __TEXT.__oslogstring: 0x1fb5
-  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__cstring: 0x25f40
+  __TEXT.__oslogstring: 0x1fce
+  __TEXT.__gcc_except_tab: 0x5d4
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
   __TEXT.__unwind_info: 0x1868
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x90d8
-  __TEXT.__objc_methtype: 0x1451
+  __TEXT.__objc_methname: 0x90e9
+  __TEXT.__objc_methtype: 0x1454
   __TEXT.__objc_stubs: 0x7b20
   __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__const: 0x26d0

   __AUTH_CONST.__auth_got: 0x10e8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0xd6e0
+  __AUTH_CONST.__cfstring: 0xd720
   __AUTH_CONST.__objc_const: 0x4db0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2384
-  Symbols:   3634
-  CStrings:  4255
+  Functions: 2385
+  Symbols:   3635
+  CStrings:  4257
 
Symbols:
+ _ABDropAllLimitedAccessRows
- _ABDropAllLimitedAccesRows
CStrings:
+ " INNER JOIN LimitedAccess la ON la.guid IN (abp.guid, abplink.guid) WHERE la.BundleID = ? AND la.IsActive = %!i(MISSING)"
+ "ABDropAllLimitedAccessRows enableFullSyncNotify %!d(MISSING)"
+ "BOOL ABDropAllLimitedAccessRows(ABAddressBookRef, BOOL)"
+ "CREATE TRIGGER IF NOT EXISTS UpdateLinkedContactsInLimited AFTER DELETE ON ABPersonLink \nBEGIN \n    INSERT OR IGNORE INTO LimitedAccess (BundleId, guid, SequenceNumber, IsActive) \n        SELECT la.BundleId, abp.guid, la.SequenceNumber, la.IsActive FROM LimitedAccess la, ABPerson abp \n        WHERE la.guid = OLD.guid AND abp.PersonLink = OLD.ROWID; \n    DELETE FROM LimitedAccess WHERE guid = OLD.guid; \nEND; \n"
+ "DROP TRIGGER IF EXISTS UpdateLinkedContactsInLimited;"
+ "_initSetupPropertySet:includeLinkedContacts:hasLimitedAccess:"
+ "v32@0:8^{__CFSet=}16B24B28"
- " INNER JOIN LimitedAccess la ON la.guid = abp.guid WHERE la.BundleID = ? AND la.IsActive = %!i(MISSING)"
- "ABDropAllLimitedAccesRows"
- "BOOL ABDropAllLimitedAccesRows(ABAddressBookRef)"
- "_initSetupPropertySet:includeLinkedContacts:"
- "v28@0:8^{__CFSet=}16B24"

```
