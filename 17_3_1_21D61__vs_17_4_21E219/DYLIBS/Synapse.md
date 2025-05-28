## Synapse

> `/System/Library/PrivateFrameworks/Synapse.framework/Synapse`

```diff

-124.0.0.0.0
-  __TEXT.__text: 0x3819c
+126.1.0.0.0
+  __TEXT.__text: 0x38ae8
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x2bf0
+  __TEXT.__objc_methlist: 0x2c50
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x8d8
-  __TEXT.__cstring: 0x2e16
-  __TEXT.__oslogstring: 0x41f3
+  __TEXT.__gcc_except_tab: 0x908
+  __TEXT.__cstring: 0x2e4a
+  __TEXT.__oslogstring: 0x43d3
   __TEXT.__dlopen_cstrs: 0x502
   __TEXT.__ustring: 0x154
-  __TEXT.__unwind_info: 0x111c
-  __TEXT.__objc_classname: 0xb64
-  __TEXT.__objc_methname: 0x7f68
+  __TEXT.__unwind_info: 0x1138
+  __TEXT.__objc_classname: 0xb89
+  __TEXT.__objc_methname: 0x8038
   __TEXT.__objc_methtype: 0x1378
-  __TEXT.__objc_stubs: 0x5a00
+  __TEXT.__objc_stubs: 0x5ac0
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x1478
-  __DATA_CONST.__objc_classlist: 0x238
+  __DATA_CONST.__const: 0x14c8
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc7e0
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_const: 0xcb30
+  __DATA_CONST.__objc_selrefs: 0x1b78
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x3d0
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__objc_const: 0x1a18
-  __AUTH_CONST.__cfstring: 0x23c0
-  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__objc_const: 0x1af0
+  __AUTH_CONST.__cfstring: 0x2400
+  __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x398
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x3c8
-  __DATA.__objc_superrefs: 0x180
+  __AUTH.__objc_data: 0xa50
   __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0xb40
-  __DATA.__bss: 0x161
+  __DATA.__bss: 0x171
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1447
-  Symbols:   5332
-  CStrings:  2217
+  Functions: 1458
+  Symbols:   5381
+  CStrings:  2236
 
Symbols:
+ +[SYDocumentWorkflowsCoreDataStore _persistentStoreDirURL]
+ +[SYDocumentWorkflowsCoreDataStore removePersistentStoreWithError:]
+ +[SYDocumentWorkflowsCoreDataStore removePersistentStoreWithError:].cold.1
+ +[SYDocumentWorkflowsDisabledDataStore _disabledRepositoryError]
+ -[SYActivityObserver _q_reportActiveUserActivityChangeIfNeeded:context:]
+ -[SYDocumentWorkflowsCoreDataStore persistentContainer].cold.4
+ -[SYDocumentWorkflowsDisabledDataStore fetchUserActivityWithRelatedUniqueIdentifier:error:]
+ -[SYDocumentWorkflowsDisabledDataStore saveUserActivity:forRelatedUniqueIdentifier:sourceBundleIdentifier:error:]
+ GCC_except_table24
+ _OBJC_CLASS_$_SYDocumentWorkflowsDisabledDataStore
+ _OBJC_METACLASS_$_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_$_CLASS_METHODS_SYDocumentWorkflowsCoreDataStore
+ __OBJC_$_CLASS_METHODS_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_$_INSTANCE_METHODS_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_$_PROP_LIST_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_CLASS_PROTOCOLS_$_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_CLASS_RO_$_SYDocumentWorkflowsDisabledDataStore
+ __OBJC_METACLASS_RO_$_SYDocumentWorkflowsDisabledDataStore
+ ___55-[SYDocumentWorkflowsCoreDataStore persistentContainer]_block_invoke.22
+ ___55-[SYDocumentWorkflowsCoreDataStore persistentContainer]_block_invoke.22.cold.1
+ ___57-[SYDocumentWorkflowsClient _createConnectionIfNecessary]_block_invoke.127
+ ___64+[SYDocumentWorkflowsDisabledDataStore _disabledRepositoryError]_block_invoke
+ ___72-[SYActivityObserver _q_reportActiveUserActivityChangeIfNeeded:context:]_block_invoke
+ ___72-[SYActivityObserver _q_reportActiveUserActivityChangeIfNeeded:context:]_block_invoke_2
+ ___72-[SYActivityObserver _q_reportActiveUserActivityChangeIfNeeded:context:]_block_invoke_3
+ ___81-[SYDocumentWorkflowsActivityObserver _handleActiveUserActivityChangeAfterDelay:]_block_invoke.12
+ ___81-[SYDocumentWorkflowsActivityObserver _handleActiveUserActivityChangeAfterDelay:]_block_invoke.12.cold.1
+ ___96+[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:]_block_invoke.130
+ ___96+[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:]_block_invoke.130.cold.1
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_literal_global.17
+ __disabledRepositoryError.error
+ __disabledRepositoryError.onceToken
+ _objc_msgSend$_disabledRepositoryError
+ _objc_msgSend$_persistentStoreDirURL
+ _objc_msgSend$_q_reportActiveUserActivityChangeIfNeeded:context:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removePersistentStoreWithError:
+ _objc_msgSend$setBool:forKey:
- GCC_except_table22
- ___55-[SYDocumentWorkflowsCoreDataStore persistentContainer]_block_invoke.cold.1
- ___57-[SYDocumentWorkflowsClient _createConnectionIfNecessary]_block_invoke.126
- ___70-[SYActivityObserver _reportActiveUserActivityChangeIfNeeded:context:]_block_invoke_2
- ___70-[SYActivityObserver _reportActiveUserActivityChangeIfNeeded:context:]_block_invoke_3
- ___81-[SYDocumentWorkflowsActivityObserver _handleActiveUserActivityChangeAfterDelay:]_block_invoke_2
- ___81-[SYDocumentWorkflowsActivityObserver _handleActiveUserActivityChangeAfterDelay:]_block_invoke_2.cold.1
- ___96+[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:]_block_invoke.129
- ___96+[SYItemIndexingManager _fetchIndexedItemsLinkedToUserActivity:extraFetchAttributes:completion:]_block_invoke.129.cold.1
CStrings:
+ "Persistent store directory cleaned up successfully: %{BOOL}d"
+ "Persistent store directory exists: %{BOOL}d, isClean: %{BOOL}d"
+ "Persistent store directory needs cleanup."
+ "Remove to persistent store directory at: %{private}@"
+ "Repository is disabled."
+ "SYDocumentWorkflowsDisabledDataStore"
+ "SYPersistentStoreDirIsClean"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "Unable to fetch original user activity for index key: %@, error: %@"
+ "Unable to find persistent store directory at: %{private}@"
+ "Unable to remove persistent store directory at: %{private}@, error: %{private}@"
+ "Unable to remove persistent store directory, error: %@"
+ "_disabledRepositoryError"
+ "_persistentStoreDirURL"
+ "_q_reportActiveUserActivityChangeIfNeeded:context:"
+ "removeItemAtURL:error:"
+ "removePersistentStoreWithError:"
+ "setBool:forKey:"

```
