## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12691.1.0.0.0
-  __TEXT.__text: 0x9d4
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x38
+12695.0.0.0.0
+  __TEXT.__text: 0x135c
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x2b2
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__objc_methname: 0x31c
+  __TEXT.__cstring: 0x209
+  __TEXT.__oslogstring: 0x1fd
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x164
-  __TEXT.__objc_methtype: 0x18
-  __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x94
-  __DATA_CONST.__auth_got: 0x160
+  __TEXT.__objc_methtype: 0x8a
+  __TEXT.__dlopen_cstrs: 0xa3
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x70
+  __DATA.__objc_const: 0x130
+  __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_classrefs: 0x18
+  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBCF39C9-9509-35F4-98E3-BDBC4D8B8F8C
-  Functions: 10
-  Symbols:   58
-  CStrings:  46
+  UUID: C6AF21F1-0ACB-300F-A4A0-7D7BF0BCD34E
+  Functions: 27
+  Symbols:   67
+  CStrings:  84
 
Symbols:
+ _ABOSLogGeneral
+ _CFArrayRemoveAllValues
+ __os_log_error_impl
+ __os_log_impl
+ _objc_autoreleaseReturnValue
+ _objc_msgSendSuper2
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x8
+ _os_log_type_enabled
- _syslog
CStrings:
+ "AB Migration - Contact metadata db was migrated, took %fs"
+ "AB Migration - Contact metadata db was not migrated, %@"
+ "AB Migration - image dbs migration took %fs"
+ "AB Migration - main dbs migration took %fs"
+ "AB Migration - migrating delegate images database"
+ "AB Migration - migrating delegate main database"
+ "AB Migration - user defaults was migrated"
+ "AB Migration estimate - Images DB (v%i) Size: %i - duration: %f (total: %f)"
+ "AB Migration estimate - Regular DB (v%i) Size: %i - estimated duration: %f (%f) (total: %f)"
+ "B32@0:8@16Q24"
+ "CNContactMetadataPersistentStoreManager"
+ "Class getCNContactMetadataPersistentStoreManagerClass(void)_block_invoke"
+ "T^{__CFArray=},N,V_changedImagePersonIdentifiers"
+ "Td,N,V_imageDbTime"
+ "Td,N,V_mainDbTime"
+ "^{__CFArray=}"
+ "^{__CFArray=}16@0:8"
+ "_changedImagePersonIdentifiers"
+ "_imageDbTime"
+ "_mainDbTime"
+ "changedImagePersonIdentifiers"
+ "copy"
+ "d"
+ "d16@0:8"
+ "dealloc"
+ "description"
+ "getDatabasePaths"
+ "imageDbTime"
+ "init"
+ "mainDbTime"
+ "migrateContactMetadataDatabase"
+ "migrateImagesDatabase:index:"
+ "migrateMainDatabase:index:"
+ "performLightweightMigrationIfNeededError:"
+ "setChangedImagePersonIdentifiers:"
+ "setImageDbTime:"
+ "setMainDbTime:"
+ "softlink:r:path:/System/Library/Frameworks/Contacts.framework/Contacts"
+ "v16@0:8"
+ "v24@0:8^{__CFArray=}16"
+ "v24@0:8d16"
+ "v32@0:8@16Q24"
+ "void *ContactsLibrary(void)"
- "\n\nAB Migration - image db migration took %fs\n"
- "\n\nAB Migration - main db migration took %fs\n"
- "\n\nAB Migration - migrating delegate database"
- "\n\nAB Migration estimate - Images DB (v%i) Size: %i - duration: %f (total: %f)\n"
- "\n\nAB Migration estimate - Regular DB (v%i) Size: %i - estimated duration: %f (%f) (total: %f)\n"

```
