## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.200.11.0.0
-  __TEXT.__text: 0x74d3c
+12851.200.41.0.0
+  __TEXT.__text: 0x74f10
   __TEXT.__auth_stubs: 0x21f0
   __TEXT.__objc_methlist: 0x2fac
-  __TEXT.__const: 0x331
-  __TEXT.__cstring: 0x26602
-  __TEXT.__oslogstring: 0x23f5
+  __TEXT.__const: 0x339
+  __TEXT.__cstring: 0x26648
+  __TEXT.__oslogstring: 0x2478
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1960
+  __TEXT.__unwind_info: 0x1968
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x91d7
+  __TEXT.__objc_methname: 0x91fa
   __TEXT.__objc_methtype: 0x1454
-  __TEXT.__objc_stubs: 0x7b80
-  __DATA_CONST.__got: 0x5b0
+  __TEXT.__objc_stubs: 0x7ba0
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0x27d8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c8
+  __DATA_CONST.__objc_selrefs: 0x24d0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x1108
   __AUTH_CONST.__const: 0xe40
-  __AUTH_CONST.__cfstring: 0xd960
+  __AUTH_CONST.__cfstring: 0xd980
   __AUTH_CONST.__objc_const: 0x4b40
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x128
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 95EBF607-1F42-3CD8-9F0F-1B62D0CDA9A4
-  Functions: 2514
-  Symbols:   7116
-  CStrings:  6032
+  UUID: 450D203D-E9B9-3B70-BB71-051DBB3CC33A
+  Functions: 2515
+  Symbols:   7118
+  CStrings:  6039
 
Symbols:
+ _ABAddressBookSetClientLoggingIdentifier
+ _ABAddressBookSetShouldFaultOnPossibleDataLoss
+ _OBJC_CLASS_$_CNAuditTokenUtilities
+ __MergedGlobals.207
+ ___block_descriptor_40_e629_B48?0^{?={__CFRuntimeBase=QAQ}^{CPRecordStore}^{CPRecordStore}^{__CFString}^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}^{__CFString}^{__CFString}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFDictionary}^{UCollator}^{UCollator}^{__CFString}^{__CFString}^{__CFStringTokenizer}^{__CFString}^{__CFString}C^{__CFArray}CC?{_opaque_pthread_mutex_t=q[56c]}^{__CFString}d^{__CFString}^{__CFString}^{?}{__ABBookflags=b1b1b8b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}8^{CPSqliteConnection=^{CPSqliteDatabase}^{sqlite3}^{__CFDictionary}^{__CFDictionary}^v^?^?^vIB}16^v24^v32^^{__CFError}40l
+ _objc_msgSend$loggingIdentifierForCurrentProcess
- __MergedGlobals.204
- ___block_descriptor_40_e614_B48?0^{?={__CFRuntimeBase=QAQ}^{CPRecordStore}^{CPRecordStore}^{__CFString}^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}^{__CFString}^{__CFString}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFDictionary}^{UCollator}^{UCollator}^{__CFString}^{__CFString}^{__CFStringTokenizer}^{__CFString}^{__CFString}C^{__CFArray}CC?{_opaque_pthread_mutex_t=q[56c]}^{__CFString}d^{__CFString}^{?}{__ABBookflags=b1b1b8b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}8^{CPSqliteConnection=^{CPSqliteDatabase}^{sqlite3}^{__CFDictionary}^{__CFDictionary}^v^?^?^vIB}16^v24^v32^^{__CFError}40l
Functions:
~ _ABCCreateAddressBookWithDatabaseDirectoryAndForceInProcessMigrationInProcessLinkingAndResetSortKeys : 1972 -> 1984
~ _OUTLINED_FUNCTION_7 : 24 -> 12
~ _ABCDestroyAddressBook : 364 -> 376
~ _ABAddressBookRegisterExternalChangeCallback : 520 -> 524
~ _OUTLINED_FUNCTION_8 : 28 -> 24
~ _OUTLINED_FUNCTION_5 : 12 -> 24
~ _OUTLINED_FUNCTION_10 : 24 -> 28
~ _OUTLINED_FUNCTION_11 : 12 -> 24
~ _OUTLINED_FUNCTION_13 : 12 -> 20
- _OUTLINED_FUNCTION_14
~ __migrationMigrateDatabase : 3344 -> 3376
+ _ABAddressBookSetClientLoggingIdentifier
+ _ABAddressBookSetUsedByContacts
~ _ABCAddressBookSaveWithConflictPolicy : 2860 -> 3148
~ __prepareSourceForDeletion : 120 -> 128
CStrings:
+ "B48@?0^{?={__CFRuntimeBase=QAQ}^{CPRecordStore}^{CPRecordStore}^{__CFString}^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}^{__CFString}^{__CFString}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFDictionary}^{UCollator}^{UCollator}^{__CFString}^{__CFString}^{__CFStringTokenizer}^{__CFString}^{__CFString}C^{__CFArray}CC@?{_opaque_pthread_mutex_t=q[56c]}^{__CFString}d^{__CFString}^{__CFString}^{?}{__ABBookflags=b1b1b8b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}8^{CPSqliteConnection=^{CPSqliteDatabase}^{sqlite3}^{__CFDictionary}^{__CFDictionary}^v^?^?^vIB}16^v24^v32^^{__CFError}40"
+ "Deleting %lu people on behalf of client %{public}@"
+ "Possible data loss detected: Deleting %lu people on behalf of client %{public}@"
+ "SetBackgroundColor"
+ "com.apple.contacts"
+ "data-loss-triage"
+ "loggingIdentifierForCurrentProcess"
- "B48@?0^{?={__CFRuntimeBase=QAQ}^{CPRecordStore}^{CPRecordStore}^{__CFString}^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}^{__CFString}^{__CFString}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFArray}^{__CFDictionary}^{UCollator}^{UCollator}^{__CFString}^{__CFString}^{__CFStringTokenizer}^{__CFString}^{__CFString}C^{__CFArray}CC@?{_opaque_pthread_mutex_t=q[56c]}^{__CFString}d^{__CFString}^{?}{__ABBookflags=b1b1b8b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}8^{CPSqliteConnection=^{CPSqliteDatabase}^{sqlite3}^{__CFDictionary}^{__CFDictionary}^v^?^?^vIB}16^v24^v32^^{__CFError}40"

```
