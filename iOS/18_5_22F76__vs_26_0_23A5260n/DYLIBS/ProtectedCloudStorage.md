## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1037.120.2.0.0
-  __TEXT.__text: 0x63730
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0x1df0
+1188.0.1.0.0
+  __TEXT.__text: 0x65040
+  __TEXT.__auth_stubs: 0x1960
+  __TEXT.__objc_methlist: 0x1e3c
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xd6f3
-  __TEXT.__oslogstring: 0x39e0
-  __TEXT.__gcc_except_tab: 0x2c80
-  __TEXT.__dlopen_cstrs: 0x37e
-  __TEXT.__unwind_info: 0x1648
-  __TEXT.__objc_classname: 0x305
-  __TEXT.__objc_methname: 0x4ec6
-  __TEXT.__objc_methtype: 0x1504
-  __TEXT.__objc_stubs: 0x3fa0
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x27c0
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__cstring: 0xd7cf
+  __TEXT.__oslogstring: 0x3a49
+  __TEXT.__gcc_except_tab: 0x2d94
+  __TEXT.__dlopen_cstrs: 0x311
+  __TEXT.__unwind_info: 0x1698
+  __TEXT.__objc_classname: 0x322
+  __TEXT.__objc_methname: 0x500f
+  __TEXT.__objc_methtype: 0x15a0
+  __TEXT.__objc_stubs: 0x40e0
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x28e0
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f0
+  __DATA_CONST.__objc_selrefs: 0x1548
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x40e0
-  __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0x17f80
-  __AUTH_CONST.__objc_const: 0x3528
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0x4130
+  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__const: 0x940
+  __AUTH_CONST.__cfstring: 0x180e0
+  __AUTH_CONST.__objc_const: 0x35a0
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x268
-  __DATA.__data: 0x8d0
-  __DATA.__bss: 0x378
+  __DATA.__objc_ivar: 0x264
+  __DATA.__data: 0x8e0
+  __DATA.__bss: 0x360
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x10b8
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A59DFE4A-CABD-3A1C-B007-3084BA18B05D
-  Functions: 1909
-  Symbols:   5909
-  CStrings:  7927
+  UUID: FBD35BAD-F552-3B13-B82B-1E67D3BCD1DE
+  Functions: 1915
+  Symbols:   5929
+  CStrings:  7961
 
Symbols:
+ -[PCSCKKS addOperations:completionOp:allOps:context:]
+ -[PCSCKKS addOperations:completionOp:allOps:context:].cold.1
+ -[PCSCKKS addOperations:completionOp:allOps:context:].cold.2
+ -[PCSCKKS blockAfterCreate]
+ -[PCSCKKS createNewIdentities:roll:sync:forceSync:complete:]
+ -[PCSCKKS setBlockAfterCreate:]
+ -[PCSCKKSCreateIdentityOperation addAndNotifyOnSync:identity:attributes:returnAttributes:complete:]
+ -[PCSCKKSCreateIdentityOperation createPCSIdentity:complete:]
+ -[PCSCKKSCreateIdentityOperation itemStored:complete:]
+ -[PCSCKKSCreateIdentityOperation setIdentityToCurrent:complete:]
+ -[PCSCKKSCreateIdentityOperation storePCSIdentity:identity:complete:]
+ -[PCSCKKSFetchCurrentOperation fetchComplete:currentItemData:point:error:]
+ -[PCSCKKSFetchCurrentOperation fetchPersistentRef:persistentRef:]
+ -[PCSCKKSItemModifyContext serviceContexts]
+ -[PCSCKKSItemModifyContext setCurrentIdentityForService:identity:persistentReference:]
+ -[PCSCKKSItemModifyContext setServiceContexts:]
+ -[PCSCKKSPerServiceContext .cxx_destruct]
+ -[PCSCKKSPerServiceContext currentIdentity]
+ -[PCSCKKSPerServiceContext currentItemReference]
+ -[PCSCKKSPerServiceContext dealloc]
+ -[PCSCKKSPerServiceContext existingItemReference]
+ -[PCSCKKSPerServiceContext existingItemSHA1]
+ -[PCSCKKSPerServiceContext init]
+ -[PCSCKKSPerServiceContext resetIdentity]
+ -[PCSCKKSPerServiceContext retryLeftCount]
+ -[PCSCKKSPerServiceContext returnedExistingIdentity]
+ -[PCSCKKSPerServiceContext rollIdentity]
+ -[PCSCKKSPerServiceContext rollItemReference]
+ -[PCSCKKSPerServiceContext rollItemSHA1]
+ -[PCSCKKSPerServiceContext roll]
+ -[PCSCKKSPerServiceContext service]
+ -[PCSCKKSPerServiceContext setCurrentIdentity:]
+ -[PCSCKKSPerServiceContext setCurrentIdentity:persistentReference:]
+ -[PCSCKKSPerServiceContext setCurrentItemReference:]
+ -[PCSCKKSPerServiceContext setExistingItemReference:]
+ -[PCSCKKSPerServiceContext setExistingItemSHA1:]
+ -[PCSCKKSPerServiceContext setRetryLeftCount:]
+ -[PCSCKKSPerServiceContext setReturnedExistingIdentity:]
+ -[PCSCKKSPerServiceContext setRoll:]
+ -[PCSCKKSPerServiceContext setRollIdentity:]
+ -[PCSCKKSPerServiceContext setRollItemReference:]
+ -[PCSCKKSPerServiceContext setRollItemSHA1:]
+ -[PCSCKKSPerServiceContext setService:]
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table96
+ OBJC_IVAR_$_PCSCKKSPerServiceContext._rollAttributes
+ _CloudKitLibraryCore.frameworkLibrary
+ _CreateSignature.cold.2
+ _MobileBackupLibraryCore
+ _MobileBackupLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_AAFAnalyticsReporter
+ _OBJC_CLASS_$_AAFAnalyticsTransportRTC
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_PCSCKKSPerServiceContext
+ _OBJC_IVAR_$_PCSCKKS._blockAfterCreate
+ _OBJC_IVAR_$_PCSCKKSItemModifyContext._serviceContexts
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._currentIdentity
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._currentItemReference
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._existingItemReference
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._existingItemSHA1
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._retryLeftCount
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._returnedExistingIdentity
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._roll
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._rollIdentity
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._rollItemReference
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._rollItemSHA1
+ _OBJC_IVAR_$_PCSCKKSPerServiceContext._service
+ _OBJC_METACLASS_$_PCSCKKSPerServiceContext
+ _PCSCKKSBulkIdentityCreationService
+ _PCSIdentitySetCreateAllManateeIdentities
+ _PCSTestsEnabled
+ _PCSTestsSetDisabled
+ _PCSTestsSetEnabled
+ _ValidateSignature.cold.3
+ __OBJC_$_INSTANCE_METHODS_PCSCKKSPerServiceContext
+ __OBJC_$_INSTANCE_VARIABLES_PCSCKKSPerServiceContext
+ __OBJC_$_PROP_LIST_PCSCKKSPerServiceContext
+ __OBJC_CLASS_RO_$_PCSCKKSPerServiceContext
+ __OBJC_METACLASS_RO_$_PCSCKKSPerServiceContext
+ __PCSMostRecentlyCreatedItem
+ __PCSServiceItemsGetAllManateeServices
+ __PCSServiceItemsGetAllManateeServices.cold.1
+ ___34-[PCSCKKSOperation startOperation]_block_invoke
+ ___39-[PCSCKKSCreateIdentityOperation start]_block_invoke
+ ___39-[PCSCKKSCreateIdentityOperation start]_block_invoke_2
+ ___53-[PCSCKKS addOperations:completionOp:allOps:context:]_block_invoke
+ ___53-[PCSCKKS addOperations:completionOp:allOps:context:]_block_invoke_2
+ ___53-[PCSCKKS addOperations:completionOp:allOps:context:]_block_invoke_3
+ ___60-[PCSCKKS createNewIdentities:roll:sync:forceSync:complete:]_block_invoke
+ ___64-[PCSCKKSCreateIdentityOperation setIdentityToCurrent:complete:]_block_invoke
+ ___69-[PCSCKKSCreateIdentityOperation storePCSIdentity:identity:complete:]_block_invoke
+ ___69-[PCSCKKSCreateIdentityOperation storePCSIdentity:identity:complete:]_block_invoke.49
+ ___69-[PCSCKKSCreateIdentityOperation storePCSIdentity:identity:complete:]_block_invoke_2
+ ___CloudKitLibraryCore_block_invoke
+ ___MobileBackupLibraryCore_block_invoke
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.876
+ ___PCSEngineExtractKeys_block_invoke.598
+ ___PCSEngineExtractKeys_block_invoke.603
+ ___PCSEngineExtractKeys_block_invoke.614
+ ___PCSEngineStoreHSM_block_invoke.750
+ ___PCSEngineStoreHSM_block_invoke.750.cold.1
+ ___PCSEngineStoreHSM_block_invoke.757
+ ___PCSEngineStoreHSM_block_invoke.765
+ ___PCSEngineStoreHSM_block_invoke.801
+ ___PCSEngineStoreHSM_block_invoke.801.cold.1
+ ___PCSEngineStoreRTHSM_block_invoke.828
+ ___PCSGuitarfishCreateSetupParameters_block_invoke.245
+ ___PCSGuitarfishRepairIdentities_block_invoke.205
+ ___PCSGuitarfishRepairIdentities_block_invoke.207
+ ___PCSGuitarfishRepairIdentities_block_invoke.209
+ ___PCSGuitarfishRepairIdentities_block_invoke.223
+ ___PCSGuitarfishSetupIdentities_block_invoke.261
+ ___PCSGuitarfishValidateIdentities_block_invoke.269
+ ___PCSGuitarfishValidateIdentities_block_invoke.276
+ ___PCSGuitarfishValidateIdentities_block_invoke.281
+ ___PCSGuitarfishValidateIdentities_block_invoke.289
+ ___PCSIdentitySetCreateAllManateeIdentities_block_invoke
+ ___PCSIdentitySetCreateAllManateeIdentities_block_invoke_2
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.557
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.557.cold.1
+ ____PCSServiceItemsGetAllManateeServices_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80r88w_e23_v20?0B8^{__CFError=}12lw88l8s32l8s40l8s48l8s56l8s72l8s64l8r80l8
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e40_v32?0"NSArray"8"PCSMTT"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e10_v16?0r^v8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e39_v24?0^{_PCSIdentityData=}8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48s56s_e44_v24?0"SecItemCurrentItemData"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e20_v16?0^{__CFError=}8lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_tmp.169
+ ___block_literal_global.1073
+ ___block_literal_global.171
+ ___block_literal_global.225
+ ___block_literal_global.263
+ ___block_literal_global.309
+ ___block_literal_global.357
+ ___block_literal_global.360
+ ___block_literal_global.404
+ ___block_literal_global.809
+ ___block_literal_global.96
+ ___connectionPCSKeySyncing_block_invoke.355
+ ___connectionPCSKeySyncing_block_invoke.358
+ ___getCKAcceptableValueClassesSymbolLoc_block_invoke
+ ___getMBManagerClass_block_invoke
+ ___getMBManagerClass_block_invoke.cold.1
+ _addOperations:completionOp:allOps:context:.once
+ _addOperations:completionOp:allOps:context:.queue
+ _addOperations:completionOp:allOps:context:.serviceOperationMap
+ _audit_stringCloudKit
+ _audit_stringMobileBackup
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _getCKAcceptableValueClassesSymbolLoc.ptr
+ _getMBManagerClass.softClass
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
+ _kPCSRTCClientName
+ _kPCSRTCEventNameCreateManateeIdentities
+ _kPCSRTCFieldEventName
+ _kPCSSafariSharedBookmarks
+ _kPCSiCloudAccountsAttestationFramework
+ _objc_msgSend$_setError
+ _objc_msgSend$addAndNotifyOnSync:identity:attributes:returnAttributes:complete:
+ _objc_msgSend$addOperations:completionOp:allOps:context:
+ _objc_msgSend$allValues
+ _objc_msgSend$blockAfterCreate
+ _objc_msgSend$createIdentities:dsid:roll:sync:forceSync:complete:
+ _objc_msgSend$createPCSIdentity:complete:
+ _objc_msgSend$dependencies
+ _objc_msgSend$fetchComplete:currentItemData:point:error:
+ _objc_msgSend$fetchPersistentRef:persistentRef:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
+ _objc_msgSend$itemStored:complete:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$position
+ _objc_msgSend$removeDependency:
+ _objc_msgSend$resetIdentity
+ _objc_msgSend$serviceContexts
+ _objc_msgSend$setCompletionBlock:
+ _objc_msgSend$setIdentityToCurrent:complete:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$storePCSIdentity:identity:complete:
+ _objc_retain_x6
+ _testPCS
- +[AAFAnalyticsEventPCS isAAAFoundationAvailable].cold.1
- -[AAFAnalyticsEventPCS initWithPCSMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:].cold.1
- -[AAFAnalyticsEventPCS isAAAFoundationAvailable]
- -[AAFAnalyticsEventPCS setIsAAAFoundationAvailable:]
- -[PCSCKKS createNewIdentity:roll:sync:forceSync:complete:]
- -[PCSCKKS submitRequest:complete:].cold.1
- -[PCSCKKSCreateIdentityOperation addAndNotifyOnSync:attributes:returnAttributes:complete:]
- -[PCSCKKSCreateIdentityOperation createPCSIdentity]
- -[PCSCKKSCreateIdentityOperation itemStored:]
- -[PCSCKKSCreateIdentityOperation setIdentityToCurrent]
- -[PCSCKKSCreateIdentityOperation storePCSIdentity:]
- -[PCSCKKSFetchCurrentOperation fetchComplete:point:error:]
- -[PCSCKKSFetchCurrentOperation fetchPersistentRef:]
- -[PCSCKKSItemModifyContext currentIdentity]
- -[PCSCKKSItemModifyContext currentItemReference]
- -[PCSCKKSItemModifyContext existingItemReference]
- -[PCSCKKSItemModifyContext existingItemSHA1]
- -[PCSCKKSItemModifyContext retryLeftCount]
- -[PCSCKKSItemModifyContext returnedExistingIdentity]
- -[PCSCKKSItemModifyContext rollIdentity]
- -[PCSCKKSItemModifyContext rollItemReference]
- -[PCSCKKSItemModifyContext rollItemSHA1]
- -[PCSCKKSItemModifyContext roll]
- -[PCSCKKSItemModifyContext server_NextRollDate]
- -[PCSCKKSItemModifyContext service]
- -[PCSCKKSItemModifyContext setCurrentIdentity:]
- -[PCSCKKSItemModifyContext setCurrentIdentity:persistentReference:]
- -[PCSCKKSItemModifyContext setCurrentItemReference:]
- -[PCSCKKSItemModifyContext setExistingItemReference:]
- -[PCSCKKSItemModifyContext setExistingItemSHA1:]
- -[PCSCKKSItemModifyContext setRetryLeftCount:]
- -[PCSCKKSItemModifyContext setReturnedExistingIdentity:]
- -[PCSCKKSItemModifyContext setRoll:]
- -[PCSCKKSItemModifyContext setRollIdentity:]
- -[PCSCKKSItemModifyContext setRollItemReference:]
- -[PCSCKKSItemModifyContext setRollItemSHA1:]
- -[PCSCKKSItemModifyContext setServer_NextRollDate:]
- -[PCSCKKSItemModifyContext setService:]
- -[PCSCKKSSyncViewOperation setView:]
- -[PCSCKKSSyncViewOperation view]
- GCC_except_table77
- GCC_except_table89
- GCC_except_table93
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- OBJC_IVAR_$_PCSCKKSItemModifyContext._rollAttributes
- _AAAFoundationLibrary
- _AAAFoundationLibraryCore
- _AAAFoundationLibraryCore.frameworkLibrary
- _AssignedPreferred
- _OBJC_IVAR_$_AAFAnalyticsEventPCS._isAAAFoundationAvailable
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._currentIdentity
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._currentItemReference
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._existingItemReference
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._existingItemSHA1
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._retryLeftCount
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._returnedExistingIdentity
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._roll
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._rollIdentity
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._rollItemReference
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._rollItemSHA1
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._server_NextRollDate
- _OBJC_IVAR_$_PCSCKKSItemModifyContext._service
- _OBJC_IVAR_$_PCSCKKSSyncViewOperation._view
- _UserManagementLibraryCore.frameworkLibrary
- ___48+[AAFAnalyticsEventPCS isAAAFoundationAvailable]_block_invoke
- ___48+[AAFAnalyticsEventPCS isAAAFoundationAvailable]_block_invoke.cold.1
- ___51-[PCSCKKSCreateIdentityOperation storePCSIdentity:]_block_invoke
- ___51-[PCSCKKSCreateIdentityOperation storePCSIdentity:]_block_invoke.30
- ___51-[PCSCKKSCreateIdentityOperation storePCSIdentity:]_block_invoke_2
- ___54-[PCSCKKSCreateIdentityOperation setIdentityToCurrent]_block_invoke
- ___58-[PCSCKKS createNewIdentity:roll:sync:forceSync:complete:]_block_invoke
- ___AAAFoundationLibraryCore_block_invoke
- ___PCSEngineAddMissingCurrentPointers_block_invoke.870
- ___PCSEngineExtractKeys_block_invoke.595
- ___PCSEngineExtractKeys_block_invoke.600
- ___PCSEngineExtractKeys_block_invoke.611
- ___PCSEngineStoreHSM_block_invoke.747
- ___PCSEngineStoreHSM_block_invoke.747.cold.1
- ___PCSEngineStoreHSM_block_invoke.754
- ___PCSEngineStoreHSM_block_invoke.762
- ___PCSEngineStoreHSM_block_invoke.798
- ___PCSEngineStoreHSM_block_invoke.798.cold.1
- ___PCSEngineStoreRTHSM_block_invoke.825
- ___PCSGuitarfishCreateSetupParameters_block_invoke.244
- ___PCSGuitarfishRepairIdentities_block_invoke.203
- ___PCSGuitarfishRepairIdentities_block_invoke.206
- ___PCSGuitarfishRepairIdentities_block_invoke.208
- ___PCSGuitarfishRepairIdentities_block_invoke.219
- ___PCSGuitarfishSetupIdentities_block_invoke.260
- ___PCSGuitarfishValidateIdentities_block_invoke.267
- ___PCSGuitarfishValidateIdentities_block_invoke.275
- ___PCSGuitarfishValidateIdentities_block_invoke.279
- ___PCSGuitarfishValidateIdentities_block_invoke.287
- ___UserManagementLibraryCore_block_invoke
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.554
- ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.554.cold.1
- ___block_descriptor_48_e8_32s40s_e20_v16?0^{__CFError=}8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e44_v24?0"SecItemCurrentItemData"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64r72w_e23_v20?0B8^{__CFError=}12lw72l8s32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_tmp.171
- ___block_literal_global.1070
- ___block_literal_global.174
- ___block_literal_global.185
- ___block_literal_global.224
- ___block_literal_global.262
- ___block_literal_global.28
- ___block_literal_global.303
- ___block_literal_global.355
- ___block_literal_global.358
- ___block_literal_global.362
- ___block_literal_global.806
- ___block_literal_global.91
- ___connectionPCSKeySyncing_block_invoke.353
- ___connectionPCSKeySyncing_block_invoke.356
- ___getAAFAnalyticsEventClass_block_invoke
- ___getAAFAnalyticsEventClass_block_invoke.cold.1
- ___getAAFAnalyticsReporterClass_block_invoke
- ___getAAFAnalyticsReporterClass_block_invoke.cold.1
- ___getAAFAnalyticsTransportRTCClass_block_invoke
- ___getAAFAnalyticsTransportRTCClass_block_invoke.cold.1
- ___getUMUserManagerClass_block_invoke
- ___getUMUserManagerClass_block_invoke.cold.1
- ___getkAAFDeviceSessionIdSymbolLoc_block_invoke
- ___getkAAFFlowIdSymbolLoc_block_invoke
- ___initCloudKit_block_invoke
- _audit_stringAAAFoundation
- _audit_stringUserManagement
- _cloudKit
- _dlopen
- _getAAFAnalyticsEventClass.softClass
- _getAAFAnalyticsReporterClass.softClass
- _getAAFAnalyticsTransportRTCClass.softClass
- _getUMUserManagerClass
- _getUMUserManagerClass.softClass
- _getkAAFDeviceSessionId
- _getkAAFDeviceSessionId.cold.1
- _getkAAFDeviceSessionIdSymbolLoc.ptr
- _getkAAFFlowIdSymbolLoc.ptr
- _initCloudKit.onceToken
- _isAAAFoundationAvailable.available
- _isAAAFoundationAvailable.onceToken
- _objc_msgSend$addAndNotifyOnSync:attributes:returnAttributes:complete:
- _objc_msgSend$alloc
- _objc_msgSend$createPCSIdentity
- _objc_msgSend$earlierDate:
- _objc_msgSend$fetchComplete:point:error:
- _objc_msgSend$fetchPersistentRef:
- _objc_msgSend$initWithEventName:eventCategory:initData:
- _objc_msgSend$itemStored:
- _objc_msgSend$server_NextRollDate
- _objc_msgSend$setIdentityToCurrent
- _objc_msgSend$setView:
- _objc_msgSend$storePCSIdentity:
- _objc_msgSend$view
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "BUG: callback for service %@ invoked again, ignoring"
+ "CKKS response for active views: Likely good"
+ "CKKS response for active views: Needs unlock"
+ "CKKS response for active views: TLKs missing"
+ "CKKS response for active views: no CloudKit account"
+ "CKKS response for active views: unknown but likely fatal error: %d"
+ "CKKS response for active views: wait for Octagon"
+ "Checking if CKKS reports bad state for active views"
+ "Errored storing identity: %@"
+ "F"
+ "Failed to get view hint from identity %@"
+ "PCSCKKSPerServiceContext"
+ "PCSIdentitySetCreateAllManateeIdentities"
+ "PCSIdentitySetCreateAllManateeIdentities: %{public}@"
+ "Rolling when creating more than one identity is not supported."
+ "Starting creation of all manatee identities"
+ "SyncViewOperation"
+ "Syncing CKKS views failed with: %@"
+ "Syncing CKKS views successful"
+ "Syncing ckks views"
+ "T@\"NSMutableDictionary\",&,V_serviceContexts"
+ "T@?,V_blockAfterCreate"
+ "_blockAfterCreate"
+ "_serviceContexts"
+ "_setError"
+ "addAndNotifyOnSync:identity:attributes:returnAttributes:complete:"
+ "addOperations:completionOp:allOps:context:"
+ "allValues"
+ "blockAfterCreate"
+ "bulk operation, existing operation %@"
+ "bulk-service-identity-creation-identifier"
+ "com.apple.SafariShared.Bookmarks"
+ "com.apple.aaa"
+ "com.apple.icloud-accounts.attestation-framework"
+ "com.apple.pcks.createAllManateeIdentities"
+ "createIdentities:dsid:roll:sync:forceSync:complete:"
+ "createNewIdentities:roll:sync:forceSync:complete:"
+ "createPCSIdentity:complete:"
+ "dependencies"
+ "eventName"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "fetchComplete:currentItemData:point:error:"
+ "fetchPersistentRef:persistentRef:"
+ "getBytes:range:"
+ "hasError"
+ "i56@0:8@16^{_PCSIdentityData=}24^{__CFDictionary=}32r^^{__CFDictionary}40@?48"
+ "initWithEventName:eventCategory:initData:altDSID:"
+ "itemStored:complete:"
+ "objectEnumerator"
+ "removeDependency:"
+ "resetIdentity"
+ "service %@, existing (bulk) operation %@"
+ "service %@, existing operation %@"
+ "serviceContexts"
+ "setBlockAfterCreate:"
+ "setCompletionBlock:"
+ "setCurrentIdentityForService:identity:persistentReference:"
+ "setIdentityToCurrent:complete:"
+ "setPosition:"
+ "setServiceContexts:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup"
+ "softlink:r:path:/System/Library/Frameworks/Accounts.framework/Accounts"
+ "softlink:r:path:/System/Library/Frameworks/CloudKit.framework/CloudKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP"
+ "storePCSIdentity:identity:complete:"
+ "timed out waiting for identity creation"
+ "v32@?0@\"NSArray\"8@\"PCSMTT\"16@\"NSError\"24"
+ "v40@0:8@16^{_PCSIdentityData=}24@32"
+ "v40@0:8@16^{_PCSIdentityData=}24@?32"
+ "v52@0:8@\"NSArray\"16@\"NSString\"24B32B36B40@?<v@?@\"NSArray\"@\"PCSMTT\"@\"NSError\">44"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "/System/Library/Frameworks/CloudKit.framework/CloudKit"
- "/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup"
- "AAFAnalyticsEvent"
- "AAFAnalyticsReporter"
- "AAFAnalyticsTransportRTC"
- "CKKS response for known state(%@): Likely good"
- "CKKS response for known state(%@): unknown but likely fatal error: %d"
- "CKKS response for known state(%{public}@): Needs unlock"
- "CKKS response for known state(%{public}@): TLKs missing"
- "CKKS response for known state(%{public}@): no CloudKit account"
- "CKKS response for known state(%{public}@): wait for Octagon"
- "Checking if CKKS reports bad state: %@"
- "Failed  get view hint from identity %@"
- "Server denied keyrolling until %@"
- "Server wants service %@ to keyroll next time at %@"
- "SyncViewOperation service: %@"
- "Syncing CKKS view %@ failed with: %@"
- "Syncing CKKS view %@ successful"
- "Syncing ckks view: %@"
- "T@\"NSDate\",&,V_server_NextRollDate"
- "T@\"NSString\",&,V_view"
- "TB,V_isAAAFoundationAvailable"
- "UMUserManager"
- "_isAAAFoundationAvailable"
- "_server_NextRollDate"
- "_view"
- "addAndNotifyOnSync:attributes:returnAttributes:complete:"
- "alloc"
- "createNewIdentity:roll:sync:forceSync:complete:"
- "createPCSIdentity"
- "earlierDate:"
- "failed to open connection to %s\n"
- "failed to softlink AAAFoundation"
- "fetchComplete:point:error:"
- "fetchPersistentRef:"
- "i48@0:8^{_PCSIdentityData=}16^{__CFDictionary=}24r^^{__CFDictionary}32@?40"
- "initWithEventName:eventCategory:initData:"
- "itemStored:"
- "kAAFDeviceSessionId"
- "kAAFFlowId"
- "server_NextRollDate"
- "setIdentityToCurrent"
- "setIsAAAFoundationAvailable:"
- "setServer_NextRollDate:"
- "setView:"
- "softlink:o:path:/System/Library/Frameworks/Accounts.framework/Accounts"
- "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP"
- "softlink:o:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement"
- "storePCSIdentity:"
- "symbol %s is missing"

```
