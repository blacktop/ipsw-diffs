## ContactsDataclassOwner

> `/System/Library/Accounts/DataclassOwners/ContactsDataclassOwner.bundle/ContactsDataclassOwner`

```diff

-3804.400.41.0.0
-  __TEXT.__text: 0x7540
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2f5
-  __TEXT.__objc_methname: 0x1525
-  __TEXT.__oslogstring: 0x1397
-  __TEXT.__objc_classname: 0x2a1
-  __TEXT.__objc_methtype: 0x40a
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__unwind_info: 0x280
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x488
+3804.500.142.0.0
+  __TEXT.__text: 0x87d4
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_stubs: 0x1360
+  __TEXT.__objc_methlist: 0x854
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x319
+  __TEXT.__objc_methname: 0x1641
+  __TEXT.__oslogstring: 0x177a
+  __TEXT.__objc_classname: 0x2d9
+  __TEXT.__objc_methtype: 0x446
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__cfstring: 0x100
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0xde0
-  __DATA.__objc_selrefs: 0x580
+  __DATA.__objc_const: 0xe98
+  __DATA.__objc_selrefs: 0x5d8
   __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0x460
+  __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x128
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70C86336-17EA-3B38-9AAF-7E4E90ED47DB
-  Functions: 207
-  Symbols:   119
-  CStrings:  356
+  UUID: D5B81FAA-F6E9-36E7-A7DB-BC56DD2894FD
+  Functions: 234
+  Symbols:   117
+  CStrings:  385
 
Symbols:
+ _OBJC_CLASS_$_CNChangeHistoryPendingChangesSummary
+ _OBJC_CLASS_$_CNGenericAccountMergeSyncDataIntoLocalDataActionHandler
+ _OBJC_METACLASS_$_CNGenericAccountMergeSyncDataIntoLocalDataActionHandler
+ ___NSArray0__struct
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ " - %ld added"
+ " - %ld deleted"
+ " - %ld updated"
+ "%p actionsForDeletingAppleAccount - Has pending changes. Offering save option. (%@)"
+ "%p actionsForDeletingGenericAccount - Has pending changes. Offering save option. (%@)"
+ "%p actionsForDisablingDataclassOnAppleAccount - Has pending changes. Offering save option. (%@)"
+ "%p actionsForDisablingDataclassOnGenericAccount - Has pending changes. Offering save option. (%@)"
+ "@\"CNChangeHistoryPendingChangesSummary\"24@0:8@\"ACAccount\"16"
+ "CNGenericAccountMergeSyncDataIntoLocalDataActionHandler"
+ "Could not find Contacts account for account %{public}@"
+ "Could not merge from the Contacts container for account %@ (%@) into the Contacts local container"
+ "DATA WILL BE LOST: %ld pending changes for account %{private}@ (%@)"
+ "Failed to get pending changes summary for account %{public}@: %{public}@"
+ "No pending changes for account %{private}@ (%@)"
+ "Pending changes for account %{public}@ (external identifier %{public}@): %ld added, %ld updated, %ld deleted"
+ "Will merge from the Contacts container for account %@ (%@) to the Contacts local container, so first enable the Contacts local container"
+ "com.apple.contacts"
+ "countOfAddedContacts"
+ "countOfDeletedContacts"
+ "countOfUpdatedContacts"
+ "data-loss-triage"
+ "dataLossTriageLog"
+ "deleteSyncDataWithPendingChanges"
+ "hasPendingChangesForAccount:"
+ "isEmpty"
+ "logPendingChangesForAccount:"
+ "noChanges"
+ "summaryOfPendingChangesForAccount:"
+ "summaryOfPendingChangesForAccountWithIdentifier:error:"

```
