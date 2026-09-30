## ReminderKit

> `/System/Library/PrivateFrameworks/ReminderKit.framework/Versions/A/ReminderKit`

```diff

-1093.0.0.0.0
-  __TEXT.__text: 0x155de4
+1095.0.0.0.0
+  __TEXT.__text: 0x1565f0
   __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x13780
+  __TEXT.__objc_methlist: 0x13818
   __TEXT.__const: 0x16d7
-  __TEXT.__oslogstring: 0x1135b
-  __TEXT.__cstring: 0xda6a
+  __TEXT.__oslogstring: 0x113ac
+  __TEXT.__cstring: 0xdb8a
   __TEXT.__gcc_except_tab: 0x83a8
   __TEXT.__ustring: 0x292
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6620
-  __TEXT.__objc_classname: 0x37b8
-  __TEXT.__objc_methname: 0x25f24
+  __TEXT.__unwind_info: 0x6638
+  __TEXT.__objc_classname: 0x37f2
+  __TEXT.__objc_methname: 0x25f73
   __TEXT.__objc_methtype: 0x4183
-  __TEXT.__objc_stubs: 0x15e40
-  __DATA_CONST.__got: 0xe90
+  __TEXT.__objc_stubs: 0x15ea0
+  __DATA_CONST.__got: 0xe98
   __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__objc_classlist: 0xb58
+  __DATA_CONST.__objc_classlist: 0xb60
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7400
+  __DATA_CONST.__objc_selrefs: 0x7418
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x990
+  __DATA_CONST.__objc_superrefs: 0x998
   __DATA_CONST.__objc_arraydata: 0x960
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x4b90
-  __AUTH_CONST.__cfstring: 0xdc00
-  __AUTH_CONST.__objc_const: 0x248d0
+  __AUTH_CONST.__cfstring: 0xdd80
+  __AUTH_CONST.__objc_const: 0x249d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x24e0
-  __DATA.__objc_ivar: 0x1090
+  __AUTH.__objc_data: 0x2530
+  __DATA.__objc_ivar: 0x1094
   __DATA.__data: 0x1a3c
   __DATA.__bss: 0x4bc
   __DATA.__common: 0x48

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8426
-  Symbols:   18249
-  CStrings:  2072
+  Functions: 8438
+  Symbols:   18275
+  CStrings:  2084
 
Symbols:
+ +[REMListsDataViewInvocation_fetchListsAndSublistsInAccount supportsSecureCoding]
+ -[REMAccount fetchListsAndSublistsWithError:]
+ -[REMDaemonUserDefaults preferredLocalizations]
+ -[REMDaemonUserDefaults setPreferredLocalizations:]
+ -[REMListsDataView fetchListsAndSublistsInAccount:error:]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount .cxx_destruct]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount accountObjectID]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount copyWithZone:]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount encodeWithCoder:]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount hash]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount initWithCoder:]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount initWithParentAccountObjectID:]
+ -[REMListsDataViewInvocation_fetchListsAndSublistsInAccount isEqual:]
+ -[REMStore(FamilyChecklist) postFamilyAnalyticsPayloadWithOperationId:operationDetail:]
+ GCC_except_table265
+ GCC_except_table292
+ GCC_except_table320
+ OBJC_IVAR_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount._accountObjectID
+ _OBJC_CLASS_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ _OBJC_METACLASS_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.702
+ __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.702.cold.1
+ __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.703
+ __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.703.cold.1
+ __113-[REMStore(UnitTest) test_immediatelyCreateOrUpdatePublicLinkOfTemplateWithTemplateObjectID:configuration:error:]_block_invoke.745
+ __145-[REMStore(AccountManagement_Internal) _triggerSyncWithReason:skipDataAccessSync:forcingCloudKitReload:discretionary:bypassThrottler:completion:]_block_invoke.602
+ __145-[REMStore(AccountManagement_Internal) _triggerSyncWithReason:skipDataAccessSync:forcingCloudKitReload:discretionary:bypassThrottler:completion:]_block_invoke.602.cold.1
+ __67-[REMStore(UnitTest) test_revertImageAttachmentsToUnDeduped:error:]_block_invoke.763
+ __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.576
+ __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.584
+ __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.584.cold.1
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.462
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.462.cold.1
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.465
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.465.cold.1
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.469
+ __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.469.cold.1
+ __76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.712
+ __76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.712.cold.1
+ __77-[REMStore(AccountManagement_Internal) removeOrphanedAccountsWithCompletion:]_block_invoke.596
+ __77-[REMStore(AccountManagement_Internal) removeOrphanedAccountsWithCompletion:]_block_invoke.596.cold.1
+ __88-[REMStore(AccountManagement_Internal) updateAccountWithAccountID:restartDA:completion:]_block_invoke.590
+ __88-[REMStore(AccountManagement_Internal) updateAccountWithAccountID:restartDA:completion:]_block_invoke.590.cold.1
+ __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.561
+ __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.567
+ __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.567.cold.1
+ __91-[REMStore(UnitTest) test_immediatelyRevokePublicLinkOfTemplateWithTemplateObjectID:error:]_block_invoke.754
+ __OBJC_$_CLASS_METHODS_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_$_CLASS_PROP_LIST_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_$_INSTANCE_METHODS_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_$_INSTANCE_VARIABLES_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_$_PROP_LIST_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_CLASS_PROTOCOLS_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_CLASS_RO_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __OBJC_METACLASS_RO_$_REMListsDataViewInvocation_fetchListsAndSublistsInAccount
+ __block_literal_global.507
+ __block_literal_global.563
+ __block_literal_global.569
+ __block_literal_global.598
+ __block_literal_global.613
+ __block_literal_global.724
+ __block_literal_global.729
+ __block_literal_global.734
+ __block_literal_global.739
+ __block_literal_global.744
+ __block_literal_global.753
+ __block_literal_global.762
+ _objc_msgSend$analytics
+ _objc_msgSend$fetchListsAndSublistsInAccount:error:
+ _objc_msgSend$postFamilyAnalyticsPayloadWithOperationId:operationDetail:
- -[REMDaemonUserDefaults persistentHistoryRequestFetchLimitDebugOverride]
- -[REMDaemonUserDefaults setPersistentHistoryRequestFetchLimitDebugOverride:]
- GCC_except_table264
- GCC_except_table291
- GCC_except_table294
- GCC_except_table307
- GCC_except_table322
- GCC_except_table325
- __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.661
- __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.661.cold.1
- __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.662
- __105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.662.cold.1
- __113-[REMStore(UnitTest) test_immediatelyCreateOrUpdatePublicLinkOfTemplateWithTemplateObjectID:configuration:error:]_block_invoke.704
- __145-[REMStore(AccountManagement_Internal) _triggerSyncWithReason:skipDataAccessSync:forcingCloudKitReload:discretionary:bypassThrottler:completion:]_block_invoke.561
- __145-[REMStore(AccountManagement_Internal) _triggerSyncWithReason:skipDataAccessSync:forcingCloudKitReload:discretionary:bypassThrottler:completion:]_block_invoke.561.cold.1
- __67-[REMStore(UnitTest) test_revertImageAttachmentsToUnDeduped:error:]_block_invoke.722
- __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.535
- __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.543
- __73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.543.cold.1
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.441
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.441.cold.1
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.444
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.444.cold.1
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.448
- __75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.448.cold.1
- __76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.671
- __76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.671.cold.1
- __77-[REMStore(AccountManagement_Internal) removeOrphanedAccountsWithCompletion:]_block_invoke.555
- __77-[REMStore(AccountManagement_Internal) removeOrphanedAccountsWithCompletion:]_block_invoke.555.cold.1
- __88-[REMStore(AccountManagement_Internal) updateAccountWithAccountID:restartDA:completion:]_block_invoke.549
- __88-[REMStore(AccountManagement_Internal) updateAccountWithAccountID:restartDA:completion:]_block_invoke.549.cold.1
- __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.520
- __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.526
- __90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.526.cold.1
- __91-[REMStore(UnitTest) test_immediatelyRevokePublicLinkOfTemplateWithTemplateObjectID:error:]_block_invoke.713
- __block_literal_global.466
- __block_literal_global.522
- __block_literal_global.528
- __block_literal_global.557
- __block_literal_global.572
- __block_literal_global.683
- __block_literal_global.688
- __block_literal_global.693
- __block_literal_global.698
- __block_literal_global.703
- __block_literal_global.712
- __block_literal_global.721
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/crframework.pb.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/zero_copy_stream.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/stubs/common.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/wire_format_lite.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/replica-manager.pb.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/topotext.pb.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/versioned-document.pb.cc"
+ "addedParticipantsToSharedGroceryList"
+ "cancelledSharedGroceryList"
+ "com.apple.reminderkit.familyChecklist"
+ "createdSharedGroceryList"
+ "eligibleForSharedGroceryList"
+ "existingSharedGroceryList"
+ "existingSharedGroceryLists%!l(MISSING)u"
+ "ineligibleCloudKitAccount"
+ "ineligibleGroceryLocale"
+ "invitedParticipants%!l(MISSING)u"
+ "operationDetail"
+ "operationId"
+ "preferredLocalizations"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/crframework.pb.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/zero_copy_stream.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/stubs/common.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/google/protobuf/wire_format_lite.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/replica-manager.pb.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/topotext.pb.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/ReminderKit/CRProtobuf/protobuf-lite/versioned-document.pb.cc"
- "persistentHistoryRequestFetchLimitDebugOverride"

```
