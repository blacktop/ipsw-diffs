## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12699.0.0.0.0
-  __TEXT.__text: 0x6e25c
+12701.1.0.0.0
+  __TEXT.__text: 0x6e748
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x2cc8
+  __TEXT.__objc_methlist: 0x2cd8
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x24017
+  __TEXT.__cstring: 0x24527
   __TEXT.__oslogstring: 0x1a74
   __TEXT.__gcc_except_tab: 0x570
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x1794
   __TEXT.__objc_classname: 0x4bc
-  __TEXT.__objc_methname: 0x8d4f
+  __TEXT.__objc_methname: 0x8d83
   __TEXT.__objc_methtype: 0x1418
-  __TEXT.__objc_stubs: 0x7860
+  __TEXT.__objc_stubs: 0x7880
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x25b8
+  __DATA_CONST.__const: 0x2608
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x36f8
-  __DATA_CONST.__objc_selrefs: 0x2340
+  __DATA_CONST.__objc_selrefs: 0x2348
+  __DATA_CONST.__objc_classrefs: 0x3a0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0xcee0
+  __AUTH_CONST.__cfstring: 0xd0e0
   __AUTH_CONST.__const: 0xdd0
   __AUTH_CONST.__objc_const: 0x1338
   __AUTH_CONST.__objc_doubleobj: 0x60

   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_classrefs: 0x3a0
-  __DATA.__objc_superrefs: 0xf8
   __DATA.__objc_ivar: 0x3cc
   __DATA.__data: 0x3a8
   __DATA.__common: 0x10
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x248
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x130
-  __DATA_DIRTY.__bss: 0xd8
-  __DATA_DIRTY.__common: 0x360
+  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__common: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8BECE5B7-9EF3-3A22-A35D-B07A37BAC128
-  Functions: 2315
-  Symbols:   6636
-  CStrings:  5750
+  UUID: 1FA5D460-75C8-36F5-BC76-E5ED94B7577D
+  Functions: 2319
+  Symbols:   6648
+  CStrings:  5786
 
Symbols:
+ -[ABVCardParser parseSensitiveContentConfigurationData]
+ GCC_except_table102
+ GCC_except_table99
+ _ABAddressBookCopySourceWithProviderIdentifier
+ ___ABAddressBookCopySourceWithProviderIdentifier_block_invoke
+ ___block_literal_global.74
+ ___block_literal_global.769
+ ___block_literal_global.82
+ ___block_literal_global.93
+ __renameTable
+ _kABCSourceProviderIdentifierProperty
+ _kABCSourceProviderMetadataProperty
+ _kABSourceProviderIdentifierProperty
+ _kABSourceProviderMetadataProperty
+ _objc_msgSend$hasContactProviderRestrictions
+ _objc_msgSend$parseSensitiveContentConfigurationData
+ _regex.onceToken.80
+ _regex.sRegEx.79
- GCC_except_table100
- GCC_except_table98
- ___block_literal_global.73
- ___block_literal_global.768
- ___block_literal_global.81
- ___block_literal_global.92
- _objc_msgSend$hasContactsProviderRestrictions
- _regex.onceToken.79
- _regex.sRegEx.78
CStrings:
+ "ABPersonChanges_old"
+ "ABPersonLink"
+ "ABPersonLink_old"
+ "ABPersonSearchKey"
+ "ABPersonSearchKey_old"
+ "ABPerson_old"
+ "ABRecordRef ABAddressBookCopySourceWithProviderIdentifier(ABAddressBookRef, CFStringRef)"
+ "CREATE TABLE IF NOT EXISTS ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ExternalIdentifier TEXT, Type INTEGER, ConstraintsPath TEXT, ExternalModificationTag TEXT, ExternalSyncTag TEXT, StoreInternalIdentifier TEXT, AccountID INTEGER DEFAULT -1,Enabled INTEGER DEFAULT 1, SyncData BLOB, MeIdentifier INTEGER DEFAULT -1, Capabilities INTEGER DEFAULT 0, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), LastSyncDate TEXT, ProviderIdentifier TEXT, ProviderMetadata BLOB, UNIQUE(StoreInternalIdentifier), UNIQUE(guid));"
+ "Failed to drop table %@ after failed rename attempt."
+ "Failed to rename table %@ to %@."
+ "Failed to rename tables before recreate!"
+ "INSERT INTO ABPersonChanges (record, type, sequence_number, ExternalIdentifier, StoreID) SELECT record, type, -1, ExternalIdentifier, StoreID FROM ABPersonChanges_old;"
+ "INSERT OR IGNORE INTO ABStore (ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate) SELECT ROWID, Name, ExternalIdentifier, Type, ConstraintsPath, ExternalModificationTag, ExternalSyncTag, StoreInternalIdentifier, AccountID, Enabled, SyncData, MeIdentifier, Capabilities, guid, LastSyncDate FROM ABStore_old;"
+ "ProviderIdentifier"
+ "ProviderMetadata"
+ "T@\"NSString\",?,R,C"
+ "WHERE ProviderIdentifier = ?"
+ "_Bool _renameTable(CPSqliteConnection *, CFStringRef, CFStringRef)"
+ "_recreatePersonTables dropTablesResult=%@"
+ "_recreatePersonTables result=%@"
+ "alter table %@ rename to %@;"
+ "drop table IF EXISTS %@;"
+ "hasContactProviderRestrictions"
+ "parseSensitiveContentConfigurationData"
- "CREATE TABLE IF NOT EXISTS ABStore (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, %s TEXT, %s TEXT, %s INTEGER, %s TEXT, %s TEXT, %s TEXT, %s TEXT, %s INTEGER DEFAULT %i, %s INTEGER DEFAULT 1, %s BLOB, %s INTEGER DEFAULT -1, %s INTEGER DEFAULT 0, %s TEXT NOT NULL DEFAULT (ab_generate_guid()), %s TEXT, UNIQUE(%s), UNIQUE(%s));"
- "alter table ABPersonLink rename to ABPersonLink_old;"
- "alter table ABPersonSearchKey rename to ABPersonSearchKey_old;"
- "hasContactsProviderRestrictions"

```
