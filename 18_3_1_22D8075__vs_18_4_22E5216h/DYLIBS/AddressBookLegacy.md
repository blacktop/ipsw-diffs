## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12828.400.1.0.0
-  __TEXT.__text: 0x734d4
-  __TEXT.__auth_stubs: 0x21c0
-  __TEXT.__objc_methlist: 0x2e24
-  __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x25f90
-  __TEXT.__oslogstring: 0x2167
+12828.500.41.0.0
+  __TEXT.__text: 0x736cc
+  __TEXT.__auth_stubs: 0x21e0
+  __TEXT.__objc_methlist: 0x2f9c
+  __TEXT.__const: 0x369
+  __TEXT.__cstring: 0x26160
+  __TEXT.__oslogstring: 0x2259
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1888
+  __TEXT.__unwind_info: 0x1900
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x9139
+  __TEXT.__objc_methname: 0x915f
   __TEXT.__objc_methtype: 0x1454
-  __TEXT.__objc_stubs: 0x7b40
+  __TEXT.__objc_stubs: 0x7b80
   __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0x26d0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2418
+  __DATA_CONST.__objc_selrefs: 0x24c0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x10f0
+  __AUTH_CONST.__auth_got: 0x1100
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xe10
-  __AUTH_CONST.__cfstring: 0xd7a0
-  __AUTH_CONST.__objc_const: 0x4db0
+  __AUTH_CONST.__cfstring: 0xd7e0
+  __AUTH_CONST.__objc_const: 0x4b10
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xaa0
+  __AUTH.__objc_data: 0xa50
   __DATA.__objc_ivar: 0x3f0
   __DATA.__data: 0x2c0
   __DATA.__common: 0x4
-  __DATA.__bss: 0x348
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA.__bss: 0x338
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x128
-  __DATA_DIRTY.__bss: 0xe8
-  __DATA_DIRTY.__common: 0x390
+  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__common: 0x38c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2399
-  Symbols:   3651
-  CStrings:  4266
+  Functions: 2482
+  Symbols:   3756
+  CStrings:  4271
 
Symbols:
+ _ABCDBContextCreateGroupMembersTable
+ _CPSqlitePreparedStatement
+ __logUpdatesZeroingPhoneAndEmailForChangedPeople
+ _bzero
+ _objc_retain_x26
- _ABCDBContextCreateGroupTables
- _objc_retain_x28
CStrings:
+ "CREATE TABLE ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ExternalIdentifier TEXT, Type INTEGER, ConstraintsPath TEXT, ExternalModificationTag TEXT, ExternalSyncTag TEXT, StoreInternalIdentifier TEXT, AccountID INTEGER DEFAULT -1,Enabled INTEGER DEFAULT 1, SyncData BLOB, MeIdentifier INTEGER DEFAULT -1, Capabilities INTEGER DEFAULT 0, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), LastSyncDate TEXT, ProviderIdentifier TEXT, ProviderMetadata BLOB, UNIQUE(StoreInternalIdentifier), UNIQUE(guid));"
+ "Failed to execute sqlite. Result: %{public}d, sql: %{public}@."
+ "Failed to prepare sqlite. sql: %{public}@."
+ "INSERT OR IGNORE INTO ABStore (ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate, ProviderIdentifier, ProviderMetadata) SELECT ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate, ProviderIdentifier, ProviderMetadata FROM ABStore_old;"
+ "SELECT ProviderIdentifier, ProviderMetadata FROM ABStore_old;"
+ "[Unusual Clearing of Contact] Saving an ABPerson to have no phone numbers or emails. Previous number of phone numbers: %ld, emails: %ld"
+ "_cn_containsOnlyDigits"
+ "_cn_hasPrefix:"
+ "kLostModeChangedRestrictedNotification"
- "CREATE TABLE IF NOT EXISTS ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ExternalIdentifier TEXT, Type INTEGER, ConstraintsPath TEXT, ExternalModificationTag TEXT, ExternalSyncTag TEXT, StoreInternalIdentifier TEXT, AccountID INTEGER DEFAULT -1,Enabled INTEGER DEFAULT 1, SyncData BLOB, MeIdentifier INTEGER DEFAULT -1, Capabilities INTEGER DEFAULT 0, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), LastSyncDate TEXT, ProviderIdentifier TEXT, ProviderMetadata BLOB, UNIQUE(StoreInternalIdentifier), UNIQUE(guid));"
- "Failed to execute sqlite. Result: %d, statement: %@."
- "_Bool ABCDBContextPerformSQLResultDone(CPSqliteConnection *, CFStringRef)"
- "kLostModeChangedNotification"

```
