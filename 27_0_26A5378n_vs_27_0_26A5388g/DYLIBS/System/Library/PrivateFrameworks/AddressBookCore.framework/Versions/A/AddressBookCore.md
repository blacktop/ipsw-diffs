## AddressBookCore

> `/System/Library/PrivateFrameworks/AddressBookCore.framework/Versions/A/AddressBookCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2759.100.1.0.0
-  __TEXT.__text: 0xe80fc
-  __TEXT.__objc_methlist: 0x12b84
+2761.100.1.0.0
+  __TEXT.__text: 0xe8544
+  __TEXT.__objc_methlist: 0x12b94
   __TEXT.__const: 0x1e4
   __TEXT.__cstring: 0xcc7e
-  __TEXT.__gcc_except_tab: 0x3f10
+  __TEXT.__gcc_except_tab: 0x3f2c
   __TEXT.__oslogstring: 0x5a03
   __TEXT.__dlopen_cstrs: 0x239
-  __TEXT.__unwind_info: 0x5750
+  __TEXT.__unwind_info: 0x5770
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x148
   __DATA_CONST.__got: 0x1818
-  __AUTH_CONST.__const: 0x5b20
+  __AUTH_CONST.__const: 0x5b50
   __AUTH_CONST.__cfstring: 0xe3a0
   __AUTH_CONST.__objc_const: 0x19fe8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x840
   __AUTH.__objc_data: 0x59b0
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0xb84

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7309
-  Symbols:   16808
+  Functions: 7316
+  Symbols:   16813
   CStrings:  2604
 
Symbols:
+ +[ABVCardFileSerializer vCardDataForContacts:error:]
+ GCC_except_table126
+ GCC_except_table141
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table201
+ GCC_except_table207
+ GCC_except_table216
+ GCC_except_table224
+ GCC_except_table239
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table273
+ GCC_except_table302
+ GCC_except_table320
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table347
+ GCC_except_table352
+ GCC_except_table366
+ GCC_except_table381
+ GCC_except_table404
+ GCC_except_table414
+ GCC_except_table418
+ GCC_except_table441
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table486
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table93
+ GCC_except_table98
+ GCC_except_table99
+ __40-[ABAddressBook isSharedInstanceOrClone]_block_invoke
+ ___107-[ABPersistentStoreCoordinatorUpdater updatePersistentStoresWithBuilder:addedUrls:removedUrls:resultBlock:]_block_invoke_3
+ ___40-[ABAddressBook isSharedInstanceOrClone]_block_invoke
+ ___41-[ABAddressBook affectedStoreForAccount:]_block_invoke
+ ___45-[ABAddressBook persistentStoreAtDefaultPath]_block_invoke
+ ___52-[ABAddressBook persistentStoreForScopedAddressBook]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0l
+ _objc_msgSend$withCoordinator:performBlockAndWait:
- GCC_except_table114
- GCC_except_table120
- GCC_except_table138
- GCC_except_table143
- GCC_except_table149
- GCC_except_table163
- GCC_except_table165
- GCC_except_table169
- GCC_except_table170
- GCC_except_table179
- GCC_except_table181
- GCC_except_table187
- GCC_except_table195
- GCC_except_table202
- GCC_except_table204
- GCC_except_table213
- GCC_except_table221
- GCC_except_table236
- GCC_except_table246
- GCC_except_table247
- GCC_except_table248
- GCC_except_table252
- GCC_except_table270
- GCC_except_table299
- GCC_except_table319
- GCC_except_table322
- GCC_except_table323
- GCC_except_table328
- GCC_except_table332
- GCC_except_table340
- GCC_except_table345
- GCC_except_table359
- GCC_except_table374
- GCC_except_table397
- GCC_except_table407
- GCC_except_table411
- GCC_except_table434
- GCC_except_table458
- GCC_except_table463
- GCC_except_table466
- GCC_except_table468
- GCC_except_table469
- GCC_except_table479
- GCC_except_table487
- GCC_except_table488
- GCC_except_table63
- GCC_except_table66
- GCC_except_table91
- GCC_except_table97
- _CNResultWithLocks
- _objc_msgSend$lockCoordinator:
- _objc_msgSend$unlockCoordinator:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABAddressBook.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABAddressBookC.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABAddressBookHackery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABAddressBook_MailSearch.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABCDRecord.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABDictionaryImporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABImageLoading.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABInfo.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABLog.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABMetadataAddOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABMetadataOperationController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABMultiValueCoreDataWrapper.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABNameCollisionMap.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABNetworkController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABPerson.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABPersonSorting.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABRecord.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABRecordMover.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABRecordVCardAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABSearchElement.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABSearchOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABSmartGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/PHXSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBookUI/ABAllGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBookUI/ABMergePeopleCommand.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/Contacts/ABCNContactDiff.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/Contacts/ABCNLegacyAddressBookDataMapper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABAddressBook.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABAddressBookC.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABAddressBookHackery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABAddressBook_MailSearch.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABCDRecord.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABDictionaryImporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABImageLoading.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABInfo.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABLog.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABMetadataAddOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABMetadataOperationController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABMultiValueCoreDataWrapper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABNameCollisionMap.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABNetworkController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABPerson.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABPersonSorting.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABRecord.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABRecordMover.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABRecordVCardAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABSearchElement.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABSearchOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABSmartGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/PHXSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBookUI/ABAllGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBookUI/ABMergePeopleCommand.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/Contacts/ABCNContactDiff.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/Contacts/ABCNLegacyAddressBookDataMapper.m"
```
