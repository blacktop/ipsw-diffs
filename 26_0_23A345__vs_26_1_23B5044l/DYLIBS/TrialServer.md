## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-474.0.0.0.0
-  __TEXT.__text: 0x1502dc
+474.2.0.0.0
+  __TEXT.__text: 0x150ab0
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__delay_helper: 0x540
-  __TEXT.__objc_methlist: 0xbe64
+  __TEXT.__objc_methlist: 0xbe7c
   __TEXT.__const: 0xe60
-  __TEXT.__cstring: 0x1582c
-  __TEXT.__oslogstring: 0x1d021
-  __TEXT.__gcc_except_tab: 0x9a80
-  __TEXT.__unwind_info: 0x43a0
+  __TEXT.__cstring: 0x1582e
+  __TEXT.__oslogstring: 0x1d27e
+  __TEXT.__gcc_except_tab: 0x9a94
+  __TEXT.__unwind_info: 0x4398
   __TEXT.__objc_classname: 0x288b
-  __TEXT.__objc_methname: 0x1e815
+  __TEXT.__objc_methname: 0x1e893
   __TEXT.__objc_methtype: 0x572d
-  __TEXT.__objc_stubs: 0x154a0
+  __TEXT.__objc_stubs: 0x15540
   __DATA_CONST.__got: 0x1370
   __DATA_CONST.__const: 0x6b30
   __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6148
+  __DATA_CONST.__objc_selrefs: 0x6170
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x338

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3DA987BA-CD4E-34DB-82B6-1D9930B4378C
-  Functions: 4850
-  Symbols:   17528
-  CStrings:  10641
+  UUID: C00988E2-3140-329C-A370-8D2E2E64BB7B
+  Functions: 4851
+  Symbols:   17534
+  CStrings:  10652
 
Symbols:
+ -[TRICKNativeArtifactProvider _applyBoostIfNeededToOperation:fromOptions:]
+ -[TRIXPCNamespaceManagementRequestHandler shouldBoostPriorityWithOptions:]
+ GCC_except_table77
+ GCC_except_table85
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e8_v12?0i8ls32l8s40l8s56l8s48l8r64l8
+ ___block_literal_global.518
+ _objc_msgSend$_applyBoostIfNeededToOperation:fromOptions:
+ _objc_msgSend$boostPriority
+ _objc_msgSend$setBoostPriority:
+ _objc_msgSend$setQueuePriority:
+ _objc_msgSend$shouldBoostPriorityWithOptions:
- GCC_except_table76
- ___114-[TRIXPCNamespaceManagementRequestHandler immediateDownloadForNamespaceNames:allowExpensiveNetworking:completion:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48bs56r_e8_v12?0i8ls32l8s40l8s48l8r56l8
- ___block_descriptor_81_e8_32s40s48s56s64bs72bs_e47_v24?0"TRIServerContext"8"<TRITaskQueuing>"16ls64l8s72l8s32l8s40l8s48l8s56l8
- ___block_literal_global.512
CStrings:
+ "%{public}@ %p: %s immediateDownloadForNamesqpaceNames:%{public}@ allowExpensiveNetworking:%s qos:%{public}u completion:"
+ "Boosted query operation, now: %@"
+ "Boosting downloadOptions: %@ for immediateDownloadWithNamespaceNames: %@"
+ "Can't register setup assistant activity (once), server context not available."
+ "Can't register setup assistant activity, server context not available."
+ "Failed to update experiment end date, ignoring. For experiment: %{public}@.%d"
+ "Sep  7 2025"
+ "TrialXP-474.2"
+ "Updated experiment end date for experiment id: %{public}@.%d. New End Date: %{public}@"
+ "_applyBoostIfNeededToOperation:fromOptions:"
+ "boostPriority"
+ "created cloudkit query with cursor: {%@} operation: %{public}@"
+ "created cloudkit query with predicate {%@} zoneID:%{public}@ operation:%{public}@"
+ "setBoostPriority:"
+ "setQueuePriority:"
+ "shouldBoostPriorityWithOptions:"
+ "updateSavedFactorLevelsWithFactorPackId failed to link temp based factor pack for: name based directory (%d): %{public}@ OR identifier based directory (%d): %{public}@."
- "Aug  2 2025"
- "Failed to update experiment end date, ignoring. ID: %{public}@"
- "TrialXP-474"
- "Updated experiment end date for experiment id: %{public}@ . New End Date: %{public}@"
- "created cloudkit query with cursor {%@}"
- "created cloudkit query with predicate {%@} zoneID:%{public}@"

```
