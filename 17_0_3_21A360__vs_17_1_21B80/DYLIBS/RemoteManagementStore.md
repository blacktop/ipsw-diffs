## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

```diff

-500.25.0.0.0
-  __TEXT.__text: 0x251cc
+500.25.2.2.0
+  __TEXT.__text: 0x25964
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x17a8
+  __TEXT.__objc_methlist: 0x1830
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0xd63
   __TEXT.__oslogstring: 0x2a6d
   __TEXT.__gcc_except_tab: 0x308
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x874
   __TEXT.__objc_classname: 0x5d1
-  __TEXT.__objc_methname: 0x54f2
-  __TEXT.__objc_methtype: 0xff9
-  __TEXT.__objc_stubs: 0x35a0
+  __TEXT.__objc_methname: 0x561a
+  __TEXT.__objc_methtype: 0x102b
+  __TEXT.__objc_stubs: 0x3660
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2568
-  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_const: 0x2598
+  __DATA_CONST.__objc_selrefs: 0x1070
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0xcc0
   __AUTH_CONST.__objc_const: 0x90

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x248
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x98
   __DATA_DIRTY.__const: 0x260

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB8520EE-B1C1-3B39-BA88-84E026319A10
-  Functions: 933
-  Symbols:   3014
-  CStrings:  1376
+  UUID: CF3DF5AC-730E-3436-A5DE-8972553837C6
+  Functions: 944
+  Symbols:   3043
+  CStrings:  1388
 
Symbols:
+ -[RMConfigurationCombineApplicator _beginProcessingWithScope:error:]
+ -[RMConfigurationCombineApplicator _beginProcessingWithScope:error:].cold.1
+ -[RMConfigurationCombineApplicator _endProcessing:scope:error:]
+ -[RMConfigurationCombineApplicator _endProcessing:scope:error:].cold.1
+ -[RMConfigurationCombineApplicator _oldDeclarationKeysWithScope:error:]
+ -[RMConfigurationCombineApplicator _oldDeclarationKeysWithScope:error:].cold.1
+ -[RMConfigurationMultipleApplicator _beginProcessingWithScope:error:]
+ -[RMConfigurationMultipleApplicator _beginProcessingWithScope:error:].cold.1
+ -[RMConfigurationMultipleApplicator _cleanupDeclarationKeysIfNeeded:scope:actionGroup:]
+ -[RMConfigurationMultipleApplicator _endProcessing:scope:error:]
+ -[RMConfigurationMultipleApplicator _endProcessing:scope:error:].cold.1
+ -[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]
+ -[RMConfigurationMultipleApplicator _oldDeclarationKeysWithScope:error:]
+ -[RMConfigurationMultipleApplicator _oldDeclarationKeysWithScope:error:].cold.1
+ -[RMConfigurationMultipleApplicator _uninstallDeclarationKeys:scope:actionGroup:]
+ -[RMConfigurationMultipleApplicator removeBeforeApply]
+ -[RMConfigurationMultipleApplicator setRemoveBeforeApply:]
+ -[RMConfigurationSingleApplicator _beginProcessingWithScope:error:]
+ -[RMConfigurationSingleApplicator _beginProcessingWithScope:error:].cold.1
+ -[RMConfigurationSingleApplicator _endProcessing:scope:error:]
+ -[RMConfigurationSingleApplicator _endProcessing:scope:error:].cold.1
+ -[RMConfigurationSingleApplicator _oldDeclarationKeysWithScope:error:]
+ -[RMConfigurationSingleApplicator _oldDeclarationKeysWithScope:error:].cold.1
+ _OBJC_IVAR_$_RMConfigurationMultipleApplicator._removeBeforeApply
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.13
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.13.cold.1
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.14
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.14.cold.1
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.15
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.15.cold.1
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.16
+ ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.16.cold.1
+ ___94-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]_block_invoke
+ ___94-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]_block_invoke.18
+ ___94-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]_block_invoke.19
+ ___94-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]_block_invoke.20
+ ___94-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:actionGroup:]_block_invoke_2
+ ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.10
+ ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.11
+ ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.12
+ ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.13
+ ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke_2.14
+ _objc_msgSend$_beginProcessingWithScope:error:
+ _objc_msgSend$_cleanupDeclarationKeysIfNeeded:scope:actionGroup:
+ _objc_msgSend$_endProcessing:scope:error:
+ _objc_msgSend$_installDeclarationKeys:scope:configurations:actionGroup:
+ _objc_msgSend$_oldDeclarationKeysWithScope:error:
+ _objc_msgSend$_uninstallDeclarationKeys:scope:actionGroup:
+ _objc_msgSend$removeBeforeApply
- -[RMConfigurationCombineApplicator _endProcessing:scope:completionHandler:]
- -[RMConfigurationCombineApplicator _endProcessing:scope:completionHandler:].cold.1
- -[RMConfigurationCombineApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.2
- -[RMConfigurationCombineApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.3
- -[RMConfigurationMultipleApplicator _endProcessing:scope:completionHandler:]
- -[RMConfigurationMultipleApplicator _endProcessing:scope:completionHandler:].cold.1
- -[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.1
- -[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.2
- -[RMConfigurationSingleApplicator _endProcessing:scope:completionHandler:]
- -[RMConfigurationSingleApplicator _endProcessing:scope:completionHandler:].cold.1
- -[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.7
- -[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:].cold.8
- GCC_except_table17
- ___100-[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.13
- ___100-[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.14
- ___100-[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.15
- ___100-[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.16
- ___100-[RMConfigurationMultipleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke_2
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.17
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.17.cold.1
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.18
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.18.cold.1
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.19
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.19.cold.1
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.20
- ___102-[RMConfigurationCombineApplicator _processConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.20.cold.1
- ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.14
- ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.16
- ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.17
- ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke.19
- ___98-[RMConfigurationSingleApplicator applyConfigurations:storesByIdentifier:scope:completionHandler:]_block_invoke_2.18
- _objc_msgSend$_endProcessing:scope:completionHandler:
CStrings:
+ "@32@0:8q16^@24"
+ "B32@0:8q16^@24"
+ "B36@0:8B16q20^@28"
+ "TB,N,V_removeBeforeApply"
+ "_beginProcessingWithScope:error:"
+ "_cleanupDeclarationKeysIfNeeded:scope:actionGroup:"
+ "_endProcessing:scope:error:"
+ "_installDeclarationKeys:scope:configurations:actionGroup:"
+ "_oldDeclarationKeysWithScope:error:"
+ "_removeBeforeApply"
+ "_uninstallDeclarationKeys:scope:actionGroup:"
+ "removeBeforeApply"
+ "setRemoveBeforeApply:"
+ "v48@0:8@16q24@32@40"
- "_endProcessing:scope:completionHandler:"
- "v36@0:8B16q20@?28"

```
