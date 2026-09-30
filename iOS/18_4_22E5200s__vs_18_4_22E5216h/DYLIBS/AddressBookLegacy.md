## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12828.500.34.0.0
-  __TEXT.__text: 0x73340
-  __TEXT.__auth_stubs: 0x21d0
+12828.500.41.0.0
+  __TEXT.__text: 0x736cc
+  __TEXT.__auth_stubs: 0x21e0
   __TEXT.__objc_methlist: 0x2f9c
-  __TEXT.__const: 0x361
-  __TEXT.__cstring: 0x25f9a
-  __TEXT.__oslogstring: 0x2167
+  __TEXT.__const: 0x369
+  __TEXT.__cstring: 0x26160
+  __TEXT.__oslogstring: 0x2259
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x18f8
+  __TEXT.__unwind_info: 0x1900
   __TEXT.__objc_classname: 0x501
   __TEXT.__objc_methname: 0x915f
   __TEXT.__objc_methtype: 0x1454

   __DATA_CONST.__objc_selrefs: 0x24c0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x10f8
+  __AUTH_CONST.__auth_got: 0x1100
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xe10
-  __AUTH_CONST.__cfstring: 0xd7c0
+  __AUTH_CONST.__cfstring: 0xd7e0
   __AUTH_CONST.__objc_const: 0x4b10
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2478
-  Symbols:   3751
-  CStrings:  4268
+  Functions: 2482
+  Symbols:   3756
+  CStrings:  4271
 
Symbols:
+ _ABCDBContextCreateGroupMembersTable
+ _CPSqlitePreparedStatement
+ __logUpdatesZeroingPhoneAndEmailForChangedPeople
- _ABCDBContextCreateGroupTables
CStrings:
+ "CREATE TABLE ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ExternalIdentifier TEXT, Type INTEGER, ConstraintsPath TEXT, ExternalModificationTag TEXT, ExternalSyncTag TEXT, StoreInternalIdentifier TEXT, AccountID INTEGER DEFAULT -1,Enabled INTEGER DEFAULT 1, SyncData BLOB, MeIdentifier INTEGER DEFAULT -1, Capabilities INTEGER DEFAULT 0, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), LastSyncDate TEXT, ProviderIdentifier TEXT, ProviderMetadata BLOB, UNIQUE(StoreInternalIdentifier), UNIQUE(guid));"
+ "Failed to execute sqlite. Result: %{public}d, sql: %{public}@."
+ "Failed to prepare sqlite. sql: %{public}@."
+ "INSERT OR IGNORE INTO ABStore (ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate, ProviderIdentifier, ProviderMetadata) SELECT ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate, ProviderIdentifier, ProviderMetadata FROM ABStore_old;"
+ "SELECT ProviderIdentifier, ProviderMetadata FROM ABStore_old;"
+ "[Unusual Clearing of Contact] Saving an ABPerson to have no phone numbers or emails. Previous number of phone numbers: %ld, emails: %ld"
- "CREATE TABLE IF NOT EXISTS ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ExternalIdentifier TEXT, Type INTEGER, ConstraintsPath TEXT, ExternalModificationTag TEXT, ExternalSyncTag TEXT, StoreInternalIdentifier TEXT, AccountID INTEGER DEFAULT -1,Enabled INTEGER DEFAULT 1, SyncData BLOB, MeIdentifier INTEGER DEFAULT -1, Capabilities INTEGER DEFAULT 0, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), LastSyncDate TEXT, ProviderIdentifier TEXT, ProviderMetadata BLOB, UNIQUE(StoreInternalIdentifier), UNIQUE(guid));"
- "Failed to execute sqlite. Result: %d, statement: %@."
- "_Bool ABCDBContextPerformSQLResultDone(CPSqliteConnection *, CFStringRef)"

```
