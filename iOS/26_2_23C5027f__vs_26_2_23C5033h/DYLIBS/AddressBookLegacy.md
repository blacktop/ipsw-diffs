## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

 12851.300.13.2.1
-  __TEXT.__text: 0x758dc
+  __TEXT.__text: 0x758e0
   __TEXT.__auth_stubs: 0x2210
   __TEXT.__objc_methlist: 0x2fc4
   __TEXT.__const: 0x339

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 09D9BB47-7C2C-30B5-8F5A-C7A7C162D269
+  UUID: 79BA3FF0-FA92-3E54-B2DE-C0B70E7D9303
   Functions: 2528
   Symbols:   7159
   CStrings:  6068
Functions:
~ _ABCAddressBookFlushPhoneCache : 92 -> 88
~ -[ABVCardCardDAVValueSetter copyParsedRecordWithSource:outRecordType:] : 364 -> 404
~ -[ABBufferQuery _initSetupPropertySet:includeLinkedContacts:hasLimitedAccess:] : 600 -> 620
~ _ABCProcessAddedImages : 88 -> 96
~ _ABCAddressBookBeginExclusiveRead : 60 -> 64
~ _ABCAddressBookEndExclusiveRead : 60 -> 64
~ _ABCGroupCopyArrayOfAllMembersWithSortOrdering : 156 -> 168
~ _ABCGroupCopyArrayFromProperty : 56 -> 60
~ _loadMembersAndSubgroups : 340 -> 336
~ _ABCMultiValueCreate : 120 -> 116
~ _ABCMultiValueCopyLabelAtIndex : 140 -> 136
~ _ABCMultiValueGetLabelAtIndex : 104 -> 100
~ _ABCMultiValueCopyUUIDAtIndex : 140 -> 136
~ _ABCMultiValueCreateMutable : 56 -> 52
~ _ABCMultiValueCreateMutableCopy : 48 -> 44
~ _ABCMultiValueRemove : 152 -> 148
~ _ABCMultiValueSetPrimaryIdentifier : 120 -> 116
~ _ABCMultiValueShow : 268 -> 264
~ _ABCMultiValueDestroy : 104 -> 100
~ _ABCCopyPeopleAndIdentifiersMatchingName : 64 -> 60
~ _ABCCopyPeopleAndMultiValuePropertiesMatchingName : 60 -> 56
~ _ABCCopyPeopleAndIdentifiersMatchingNameWithCancellationCallback : 68 -> 64
~ _saveImage : 276 -> 272
~ _saveAvatarRecipeData : 232 -> 228
~ __ABCSaveSingleStringValue : 432 -> 428
~ _ABCDBContextMultiValueWillChange : 552 -> 548
~ _ABCDBContextSaveCallback : 988 -> 984
~ _ABCDBContextPreCommitSaveCallback : 332 -> 328
~ _ABCDBContextDeleteMultiValueDeletesInSourceToSequenceNumber : 168 -> 164

```
