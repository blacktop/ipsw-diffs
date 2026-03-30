## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.500.121.2.2
-  __TEXT.__text: 0x75e7c
+12851.600.2.0.0
+  __TEXT.__text: 0x75ec8
   __TEXT.__auth_stubs: 0x2210
   __TEXT.__objc_methlist: 0x3054
   __TEXT.__const: 0x341
-  __TEXT.__cstring: 0x26ada
+  __TEXT.__cstring: 0x26b7a
   __TEXT.__oslogstring: 0x270f
   __TEXT.__gcc_except_tab: 0x638
   __TEXT.__dlopen_cstrs: 0xb8

   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x1118
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xdaa0
+  __AUTH_CONST.__cfstring: 0xdae0
   __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4AEF554F-0C5D-33B2-8474-06C6C1DC2F30
+  UUID: 73C46D2D-F02F-3BC7-AF84-A0FF2CB7801F
   Functions: 2582
   Symbols:   7318
-  CStrings:  6107
+  CStrings:  6111
 
Functions:
~ __migrationMigrateDatabase : 3380 -> 3432
~ _ABCDBContextCreateABPersonTriggersAndIndicesAndDropFirst : 1248 -> 1272
CStrings:
+ "CREATE INDEX ABPersonPersonLinkStoreIndex on ABPerson(PersonLink, StoreID);"
+ "CREATE INDEX IF NOT EXISTS ABPersonPersonLinkStoreIndex on ABPerson(PersonLink, StoreID);"
+ "DROP INDEX IF EXISTS ABPersonPersonLinkStoreIndex;"
+ "SELECT PersonLink FROM ABPerson INDEXED BY ABPersonPersonLinkStoreIndex WHERE PersonLink = 1;"
- "CREATE INDEX ABPersonPersonLinkIndex on ABPerson(PersonLink);"
- "SELECT PersonLink FROM ABPerson INDEXED BY ABPersonPersonLinkIndex WHERE PersonLink = 1;"

```
