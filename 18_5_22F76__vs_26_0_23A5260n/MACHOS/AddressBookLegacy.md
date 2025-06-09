## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12828.500.41.0.0
-  __TEXT.__text: 0x1734
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__objc_methname: 0x359
-  __TEXT.__cstring: 0x225
-  __TEXT.__oslogstring: 0x2de
+12846.100.1.0.0
+  __TEXT.__text: 0x1b30
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0xe0
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__objc_methname: 0x3de
+  __TEXT.__cstring: 0x298
+  __TEXT.__oslogstring: 0x397
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0x8a
   __TEXT.__dlopen_cstrs: 0xa3
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x200
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0xf8
+  __DATA.__objc_selrefs: 0x120
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4891F3D5-4C33-3B57-9E98-C27EF324B33A
-  Functions: 29
-  Symbols:   79
-  CStrings:  92
+  UUID: 37F30453-8850-3106-8096-EEA201C98101
+  Functions: 34
+  Symbols:   81
+  CStrings:  104
 
Symbols:
+ _objc_alloc
+ _objc_retain_x9
CStrings:
+ "AB Migration - Contact poster data stats: posterCount: %li, migrated: %li, not fetched: %li"
+ "AB Migration - Contact poster data was copied, took %fs"
+ "AB Migration - Poster Data will copy"
+ "CNContactPosterDataPersistentStoreManager"
+ "CNContactPosterMigrator"
+ "Class getCNContactPosterDataPersistentStoreManagerClass(void)_block_invoke"
+ "Class getCNContactPosterMigratorClass(void)_block_invoke"
+ "CopyPosterDataToMetadataStore"
+ "contactsWithPostersCount"
+ "copyPosterDataToMetadataStore"
+ "initWithAddressBook:storeManager:"
+ "postersMigratedCount"
+ "postersNotFetchedCount"
- "CNContactMetadataPersistentStoreManager"
- "Class getCNContactMetadataPersistentStoreManagerClass(void)_block_invoke"

```
