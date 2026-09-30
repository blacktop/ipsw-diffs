## ReminderKit

> `/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit`

```diff

-3796.11.0.0.0
-  __TEXT.__text: 0x13c64c
+3799.0.0.0.0
+  __TEXT.__text: 0x13d7a8
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x15170
+  __TEXT.__objc_methlist: 0x15370
   __TEXT.__const: 0x16b7
-  __TEXT.__oslogstring: 0x1199e
-  __TEXT.__cstring: 0xdcf8
+  __TEXT.__oslogstring: 0x11960
+  __TEXT.__cstring: 0xdd89
   __TEXT.__gcc_except_tab: 0x8350
   __TEXT.__ustring: 0x292
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6778
-  __TEXT.__objc_classname: 0x39b5
-  __TEXT.__objc_methname: 0x2712c
-  __TEXT.__objc_methtype: 0x41b0
-  __TEXT.__objc_stubs: 0x16420
-  __DATA_CONST.__got: 0xef8
+  __TEXT.__unwind_info: 0x67c0
+  __TEXT.__objc_classname: 0x3a4b
+  __TEXT.__objc_methname: 0x27360
+  __TEXT.__objc_methtype: 0x41d5
+  __TEXT.__objc_stubs: 0x16560
+  __DATA_CONST.__got: 0xf10
   __DATA_CONST.__const: 0x29f8
-  __DATA_CONST.__objc_classlist: 0xba0
+  __DATA_CONST.__objc_classlist: 0xbb8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7958
+  __DATA_CONST.__objc_selrefs: 0x79b0
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x9d8
-  __DATA_CONST.__objc_arraydata: 0x988
+  __DATA_CONST.__objc_superrefs: 0x9f0
+  __DATA_CONST.__objc_arraydata: 0x990
   __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0x2c80
-  __AUTH_CONST.__cfstring: 0xe1c0
-  __AUTH_CONST.__objc_const: 0x23478
+  __AUTH_CONST.__cfstring: 0xe280
+  __AUTH_CONST.__objc_const: 0x23890
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2fd0
+  __AUTH.__objc_data: 0x3070
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x10ec
+  __DATA.__objc_ivar: 0x110c
   __DATA.__data: 0x1a3c
   __DATA.__bss: 0x304
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x4470
+  __DATA_DIRTY.__objc_data: 0x44c0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x450
   __DATA_DIRTY.__common: 0x1a0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B3B0CE7F-9765-3835-929A-A1931978F9BB
-  Functions: 8589
-  Symbols:   27555
-  CStrings:  11303
+  UUID: A7BE3AA1-B950-3D64-835F-B06709B6EA0E
+  Functions: 8624
+  Symbols:   27673
+  CStrings:  11338
 
Symbols:
+ +[REMReminderExtractionOutput supportsSecureCoding]
+ +[REMRemindersDataViewInvocation_fetchByBatchCreationID supportsSecureCoding]
+ +[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID supportsSecureCoding]
+ +[REMUserActivity stringForFlags:]
+ -[REMReminderExtractionOutput .cxx_destruct]
+ -[REMReminderExtractionOutput copyWithZone:]
+ -[REMReminderExtractionOutput description]
+ -[REMReminderExtractionOutput encodeWithCoder:]
+ -[REMReminderExtractionOutput initWithCoder:]
+ -[REMReminderExtractionOutput initWithSuggestedTitles:isClassifiedAsRecipe:]
+ -[REMReminderExtractionOutput isClassifiedAsRecipe]
+ -[REMReminderExtractionOutput isEqual:]
+ -[REMReminderExtractionOutput suggestedTitles]
+ -[REMReminderStorage batchCreationID]
+ -[REMReminderStorage setBatchCreationID:]
+ -[REMRemindersDataView fetchRemindersCountWithBatchCreationID:includingCompleted:error:]
+ -[REMRemindersDataView fetchRemindersWithBatchCreationID:includingCompleted:error:]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID .cxx_destruct]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID batchCreationID]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID copyWithZone:]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID encodeWithCoder:]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID hash]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID includingCompleted]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID initWithBatchCreationID:includingCompleted:]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID initWithCoder:]
+ -[REMRemindersDataViewInvocation_fetchByBatchCreationID isEqual:]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID .cxx_destruct]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID batchCreationID]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID copyWithZone:]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID encodeWithCoder:]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID hash]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID includingCompleted]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID initWithBatchCreationID:includingCompleted:]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID initWithCoder:]
+ -[REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID isEqual:]
+ -[REMUserActivity flags]
+ -[REMUserActivity initWithType:storage:flags:]
+ -[REMUserActivity userActivityWithFlags:]
+ _OBJC_CLASS_$_REMReminderExtractionOutput
+ _OBJC_CLASS_$_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ _OBJC_CLASS_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ _OBJC_IVAR_$_REMReminderExtractionOutput._isClassifiedAsRecipe
+ _OBJC_IVAR_$_REMReminderExtractionOutput._suggestedTitles
+ _OBJC_IVAR_$_REMReminderStorage._batchCreationID
+ _OBJC_IVAR_$_REMRemindersDataViewInvocation_fetchByBatchCreationID._batchCreationID
+ _OBJC_IVAR_$_REMRemindersDataViewInvocation_fetchByBatchCreationID._includingCompleted
+ _OBJC_IVAR_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID._batchCreationID
+ _OBJC_IVAR_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID._includingCompleted
+ _OBJC_IVAR_$_REMUserActivity._flags
+ _OBJC_METACLASS_$_REMReminderExtractionOutput
+ _OBJC_METACLASS_$_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ _OBJC_METACLASS_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_$_CLASS_METHODS_REMReminderExtractionOutput
+ __OBJC_$_CLASS_METHODS_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_$_CLASS_METHODS_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_$_CLASS_PROP_LIST_REMReminderExtractionOutput
+ __OBJC_$_CLASS_PROP_LIST_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_$_CLASS_PROP_LIST_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_$_INSTANCE_METHODS_REMReminderExtractionOutput
+ __OBJC_$_INSTANCE_METHODS_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_$_INSTANCE_METHODS_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_$_INSTANCE_VARIABLES_REMReminderExtractionOutput
+ __OBJC_$_INSTANCE_VARIABLES_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_$_INSTANCE_VARIABLES_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_$_PROP_LIST_REMReminderExtractionOutput
+ __OBJC_$_PROP_LIST_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_$_PROP_LIST_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_CLASS_PROTOCOLS_$_REMReminderExtractionOutput
+ __OBJC_CLASS_PROTOCOLS_$_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_CLASS_PROTOCOLS_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_CLASS_RO_$_REMReminderExtractionOutput
+ __OBJC_CLASS_RO_$_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_CLASS_RO_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ __OBJC_METACLASS_RO_$_REMReminderExtractionOutput
+ __OBJC_METACLASS_RO_$_REMRemindersDataViewInvocation_fetchByBatchCreationID
+ __OBJC_METACLASS_RO_$_REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID
+ ___105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.655
+ ___105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.655.cold.1
+ ___113-[REMStore(UnitTest) test_immediatelyCreateOrUpdatePublicLinkOfTemplateWithTemplateObjectID:configuration:error:]_block_invoke.705
+ ___123-[REMStore(IntelligentFeatures) isIntelligentFeaturesSupportedInCurrentAppVersionWithIntelligentFeature:isInternalInstall:]_block_invoke.471
+ ___67-[REMStore(UnitTest) test_revertImageAttachmentsToUnDeduped:error:]_block_invoke.719
+ ___72-[REMStore(EventKitCompatibility) MCIsManagedAccountWithObjectID:error:]_block_invoke.516
+ ___72-[REMStore(EventKitCompatibility) MCIsManagedAccountWithObjectID:error:]_block_invoke.516.cold.1
+ ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.550
+ ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke_2.552
+ ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke_2.552.cold.1
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.421
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.421.cold.1
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.424
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.424.cold.1
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.432
+ ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.432.cold.1
+ ___76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.664
+ ___76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.664.cold.1
+ ___90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.538
+ ___91-[REMStore(UnitTest) test_immediatelyRevokePublicLinkOfTemplateWithTemplateObjectID:error:]_block_invoke.712
+ ___block_literal_global.480
+ ___block_literal_global.540
+ ___block_literal_global.543
+ ___block_literal_global.560
+ ___block_literal_global.571
+ ___block_literal_global.587
+ ___block_literal_global.590
+ ___block_literal_global.674
+ ___block_literal_global.679
+ ___block_literal_global.684
+ ___block_literal_global.689
+ ___block_literal_global.694
+ ___block_literal_global.699
+ ___block_literal_global.704
+ ___block_literal_global.711
+ ___block_literal_global.718
+ _objc_msgSend$batchCreationID
+ _objc_msgSend$fetchRemindersCountWithBatchCreationID:includingCompleted:error:
+ _objc_msgSend$fetchRemindersWithBatchCreationID:includingCompleted:error:
+ _objc_msgSend$flags
+ _objc_msgSend$initWithBatchCreationID:includingCompleted:
+ _objc_msgSend$initWithSuggestedTitles:isClassifiedAsRecipe:
+ _objc_msgSend$initWithType:storage:flags:
+ _objc_msgSend$isClassifiedAsRecipe
+ _objc_msgSend$setBatchCreationID:
+ _objc_msgSend$stringForFlags:
+ _objc_msgSend$suggestedTitles
- -[REMStore(NewsRecipeCard) fetchIncompleteRemindersCountForNewsRecipeCardWithBatchCreationID:error:].cold.1
- -[REMStore(NewsRecipeCard) fetchIncompleteRemindersForNewsRecipeCardWithBatchCreationID:error:].cold.1
- -[REMUserActivity initWithType:storage:]
- ___105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.657
- ___105-[REMStore(ClientConnections) requestToUpdateClientConnectionsAsynchronously:shouldKeepAlive:completion:]_block_invoke.657.cold.1
- ___113-[REMStore(UnitTest) test_immediatelyCreateOrUpdatePublicLinkOfTemplateWithTemplateObjectID:configuration:error:]_block_invoke.707
- ___123-[REMStore(IntelligentFeatures) isIntelligentFeaturesSupportedInCurrentAppVersionWithIntelligentFeature:isInternalInstall:]_block_invoke.472
- ___67-[REMStore(UnitTest) test_revertImageAttachmentsToUnDeduped:error:]_block_invoke.721
- ___72-[REMStore(EventKitCompatibility) MCIsManagedAccountWithObjectID:error:]_block_invoke.517
- ___72-[REMStore(EventKitCompatibility) MCIsManagedAccountWithObjectID:error:]_block_invoke.517.cold.1
- ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke.551
- ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke_2.553
- ___73-[REMStore(AccountManagement_Internal) updateAccountsAndSync:completion:]_block_invoke_2.553.cold.1
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.422
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.422.cold.1
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.425
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.425.cold.1
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.433
- ___75-[REMStore(FamilyChecklist) addParticipantsToSharedGroceryList:completion:]_block_invoke.433.cold.1
- ___76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.666
- ___76-[REMStore(PhantomObjectRepairing) repairPhantomObjectsWithObjectIDs:error:]_block_invoke.666.cold.1
- ___90-[REMStore(AccountManagement_PrivateSPIs) triggerSyncForDataAccessAccountsWithAccountIDs:]_block_invoke.539
- ___91-[REMStore(UnitTest) test_immediatelyRevokePublicLinkOfTemplateWithTemplateObjectID:error:]_block_invoke.714
- ___block_literal_global.481
- ___block_literal_global.541
- ___block_literal_global.544
- ___block_literal_global.561
- ___block_literal_global.572
- ___block_literal_global.578
- ___block_literal_global.581
- ___block_literal_global.676
- ___block_literal_global.681
- ___block_literal_global.686
- ___block_literal_global.691
- ___block_literal_global.696
- ___block_literal_global.701
- ___block_literal_global.706
- ___block_literal_global.713
- ___block_literal_global.720
- _objc_msgSend$initWithType:storage:
CStrings:
+ "%@ (type=%@, bytes=%@, flags=%@, details=%@)"
+ "<%@: %p suggestedTitles: %@, isClassifiedAsRecipe: %i>"
+ "@40@0:8q16@24q32"
+ "NewsRecipeCardSPI END fetch incomplete reminders count {batchCreationID:%{public}@, remindersCount:%{public}@}"
+ "NewsRecipeCardSPI END fetch incomplete reminders {batchCreationID:%{public}@, remindersCount:%{public}@}"
+ "REMReminderExtractionOutput"
+ "REMRemindersDataViewInvocation_fetchByBatchCreationID"
+ "REMRemindersDataViewInvocation_fetchRemindersCountByBatchCreationID"
+ "T@\"NSArray\",R,N,V_suggestedTitles"
+ "T@\"NSUUID\",&,D,N"
+ "T@\"NSUUID\",&,N,V_batchCreationID"
+ "T@\"NSUUID\",R,N,V_batchCreationID"
+ "TB,R,N,V_isClassifiedAsRecipe"
+ "Tq,R,N,V_flags"
+ "_batchCreationID"
+ "_flags"
+ "_isClassifiedAsRecipe"
+ "_suggestedTitles"
+ "batchCreationID"
+ "fetchRemindersCountWithBatchCreationID:includingCompleted:error:"
+ "fetchRemindersWithBatchCreationID:includingCompleted:error:"
+ "flags"
+ "initWithBatchCreationID:includingCompleted:"
+ "initWithSuggestedTitles:isClassifiedAsRecipe:"
+ "initWithType:storage:flags:"
+ "isClassifiedAsRecipe"
+ "prefersHiddenInRemindersList"
+ "setBatchCreationID:"
+ "stringForFlags:"
+ "suggestedTitles"
+ "unknownFlag(0x%lx)"
+ "userActivityWithFlags:"
+ "v32@0:8@\"REMReminderExtractionInput\"16@?<v@?@\"REMReminderExtractionOutput\"@\"NSError\">24"
- "%@ (type=%@, bytes=%@, details=%@)"
- "NewsRecipeCardSPI END fetch incomplete reminders count {batchCreationID:%{public}@}"
- "NewsRecipeCardSPI END fetch incomplete reminders {batchCreationID:%{public}@}"
- "NewsRecipeCardSPI fetch incomplete reminders count error: %@"
- "NewsRecipeCardSPI fetch incomplete reminders error: %@"
- "SPI not fully implemented."
- "initWithType:storage:"
- "v32@0:8@\"REMReminderExtractionInput\"16@?<v@?@\"NSArray\"@\"NSError\">24"

```
