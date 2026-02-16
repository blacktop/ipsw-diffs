## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2094.40.71.0.0
-  __TEXT.__text: 0xc75c4
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x11324
+2094.50.11.2.1
+  __TEXT.__text: 0xd7264
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x1133c
   __TEXT.__const: 0x628
-  __TEXT.__gcc_except_tab: 0x2308
+  __TEXT.__gcc_except_tab: 0x2178
   __TEXT.__oslogstring: 0x6caf
-  __TEXT.__cstring: 0x6c50
+  __TEXT.__cstring: 0x6c8b
   __TEXT.__dlopen_cstrs: 0xa59
   __TEXT.__ustring: 0xca
-  __TEXT.__unwind_info: 0x33d0
-  __TEXT.__objc_classname: 0x24b0
-  __TEXT.__objc_methname: 0x2dd85
-  __TEXT.__objc_methtype: 0x7688
+  __TEXT.__unwind_info: 0x3e68
+  __TEXT.__objc_classname: 0x24b3
+  __TEXT.__objc_methname: 0x2dd2a
+  __TEXT.__objc_methtype: 0x769c
   __TEXT.__objc_stubs: 0x1c8e0
   __DATA_CONST.__got: 0xfe0
-  __DATA_CONST.__const: 0x2800
+  __DATA_CONST.__const: 0x2820
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c60
+  __DATA_CONST.__objc_selrefs: 0x8c58
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__auth_got: 0x7b0
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x57c0
-  __AUTH_CONST.__objc_const: 0x2a5b8
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__const: 0x10e0
+  __AUTH_CONST.__cfstring: 0x57e0
+  __AUTH_CONST.__objc_const: 0x2a5e8
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2300
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x14dc
+  __DATA.__objc_ivar: 0x14e0
   __DATA.__data: 0x2be8
   __DATA.__bss: 0x800
   __DATA_DIRTY.__objc_data: 0x1b80

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F94739E-E112-3C1E-8192-0367D9A3EB22
-  Functions: 5857
-  Symbols:   20941
-  CStrings:  9728
+  UUID: C19F0E28-9E8F-34F6-ACDB-DFDCCBCC850F
+  Functions: 5889
+  Symbols:   21032
+  CStrings:  9731
 
Symbols:
+ -[SFShareSheetSlotManager activityViewControllerSessionDidEndWithSessionID:testingDataDump:completionHandler:]
+ -[SHSheetContext dataDumpHandler]
+ -[SHSheetContext setDataDumpHandler:]
+ -[SHSheetContext setTestingReferenceDataDump:]
+ -[SHSheetContext testingReferenceDataDump]
+ -[SHSheetRemoteConnectionContext linkMetadata]
+ -[SHSheetRemoteConnectionContext setLinkMetadata:]
+ -[SHSheetSession _updateTestingDataDumpIfNeededForResolvedItems:activityType:]
+ -[SHSheetSession dataDumpHandler]
+ -[SHSheetSession setDataDumpHandler:]
+ -[SHSheetSession setTestingDataDump:]
+ -[SHSheetSession setTestingReferenceDataDump:]
+ -[SHSheetSession testingDataDump]
+ -[SHSheetSession testingReferenceDataDump]
+ -[UIActivityViewController dataDumpHandler]
+ -[UIActivityViewController setDataDumpHandler:]
+ -[UIActivityViewController setTestingReferenceDataDump:]
+ -[UIActivityViewController testingReferenceDataDump]
+ -[UISUIActivityViewControllerConfiguration setTestingDataDump:]
+ -[UISUIActivityViewControllerConfiguration setTestingReferenceDataDump:]
+ -[UISUIActivityViewControllerConfiguration testingDataDump]
+ -[UISUIActivityViewControllerConfiguration testingReferenceDataDump]
+ -[_UIActivityMatchingContext setTestingReferenceDataDump:]
+ -[_UIActivityMatchingContext testingReferenceDataDump]
+ _OBJC_CLASS_$_SFShareSheetSessionTestingDataDump
+ _OBJC_IVAR_$_SHSheetContext._dataDumpHandler
+ _OBJC_IVAR_$_SHSheetContext._testingReferenceDataDump
+ _OBJC_IVAR_$_SHSheetRemoteConnectionContext._linkMetadata
+ _OBJC_IVAR_$_SHSheetSession._dataDumpHandler
+ _OBJC_IVAR_$_SHSheetSession._testingDataDump
+ _OBJC_IVAR_$_SHSheetSession._testingReferenceDataDump
+ _OBJC_IVAR_$_UIActivityViewController._dataDumpHandler
+ _OBJC_IVAR_$_UIActivityViewController._testingReferenceDataDump
+ _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._testingDataDump
+ _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._testingReferenceDataDump
+ _OBJC_IVAR_$__UIActivityMatchingContext._testingReferenceDataDump
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_PROP_LIST_SHSheetInteractor.398
+ __OBJC_$_PROP_LIST_SHSheetPresenter.650
+ ___72-[SHSheetInteractor performActivityWithRequest:forExtension:completion:]_block_invoke_2
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.151
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.152
+ ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.146
+ ___block_descriptor_32_e15_B32?08Q16^B24l
+ ___block_literal_global.127
+ ___block_literal_global.197
+ ___block_literal_global.201
+ ___block_literal_global.224
+ ___block_literal_global.230
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.359
+ _objc_msgSend$_setCKShare:setupContainerInfo:shareOptions:
+ _objc_msgSend$_setCKShareURLWrapper:share:shareOptions:
+ _objc_msgSend$_updateTestingDataDumpIfNeededForResolvedItems:activityType:
+ _objc_msgSend$activityViewControllerSessionDidEndWithSessionID:testingDataDump:completionHandler:
+ _objc_msgSend$dataDumpHandler
+ _objc_msgSend$didFinishPreparingForExecution
+ _objc_msgSend$extensionsResultWithMatchingAttributes:testingReferenceDataDump:
+ _objc_msgSend$setDataDumpHandler:
+ _objc_msgSend$setTestingDataDump:
+ _objc_msgSend$setTestingReferenceDataDump:
+ _objc_msgSend$testingDataDump
+ _objc_msgSend$testingReferenceDataDump
- -[SFShareSheetSlotManager activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:]
- -[SHSheetContext setSnapshotHandler:]
- -[SHSheetContext setTestingReferenceSnapshot:]
- -[SHSheetContext snapshotHandler]
- -[SHSheetContext testingReferenceSnapshot]
- -[SHSheetSession _updateTestingSnapshotIfNeededForResolvedItems:activityType:]
- -[SHSheetSession setSnapshotHandler:]
- -[SHSheetSession setTestingReferenceSnapshot:]
- -[SHSheetSession setTestingSnapshot:]
- -[SHSheetSession snapshotHandler]
- -[SHSheetSession testingReferenceSnapshot]
- -[SHSheetSession testingSnapshot]
- -[UIActivityViewController setSnapshotHandler:]
- -[UIActivityViewController setTestingReferenceSnapshot:]
- -[UIActivityViewController snapshotHandler]
- -[UIActivityViewController testingReferenceSnapshot]
- -[UISUIActivityViewControllerConfiguration setTestingReferenceSnapshot:]
- -[UISUIActivityViewControllerConfiguration setTestingSnapshot:]
- -[UISUIActivityViewControllerConfiguration testingReferenceSnapshot]
- -[UISUIActivityViewControllerConfiguration testingSnapshot]
- -[_UIActivityMatchingContext setTestingReferenceSnapshot:]
- -[_UIActivityMatchingContext testingReferenceSnapshot]
- _OBJC_CLASS_$_SFShareSheetSessionTestingSnapshot
- _OBJC_IVAR_$_SHSheetContext._snapshotHandler
- _OBJC_IVAR_$_SHSheetContext._testingReferenceSnapshot
- _OBJC_IVAR_$_SHSheetSession._snapshotHandler
- _OBJC_IVAR_$_SHSheetSession._testingReferenceSnapshot
- _OBJC_IVAR_$_SHSheetSession._testingSnapshot
- _OBJC_IVAR_$_UIActivityViewController._snapshotHandler
- _OBJC_IVAR_$_UIActivityViewController._testingReferenceSnapshot
- _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._testingReferenceSnapshot
- _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._testingSnapshot
- _OBJC_IVAR_$__UIActivityMatchingContext._testingReferenceSnapshot
- __OBJC_$_PROP_LIST_SHSheetInteractor.390
- __OBJC_$_PROP_LIST_SHSheetPresenter.647
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.148
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.149
- ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.143
- ___block_literal_global.124
- ___block_literal_global.194
- ___block_literal_global.198
- ___block_literal_global.221
- ___block_literal_global.227
- ___block_literal_global.312
- ___block_literal_global.316
- ___block_literal_global.324
- ___block_literal_global.356
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_setCKShare:setupContainerInfo:permissionType:allowOthersToInvite:
- _objc_msgSend$_setCKShareURLWrapper:share:permissionType:allowOthersToInvite:
- _objc_msgSend$_updateTestingSnapshotIfNeededForResolvedItems:activityType:
- _objc_msgSend$activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:
- _objc_msgSend$extensionsResultWithMatchingAttributes:testingReferenceSnapshot:
- _objc_msgSend$getCKSharingOptionsFromOptions:accessType:permissionType:allowOthersToInvite:
- _objc_msgSend$setSnapshotHandler:
- _objc_msgSend$setTestingReferenceSnapshot:
- _objc_msgSend$setTestingSnapshot:
- _objc_msgSend$snapshotHandler
- _objc_msgSend$testingReferenceSnapshot
- _objc_msgSend$testingSnapshot
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ ", usingTestingReferenceDataDump"
+ "@\"SFShareSheetSessionTestingDataDump\""
+ "B32@?0@8Q16^B24"
+ "T@\"NSArray\",C,N,V_linkMetadata"
+ "T@\"SFShareSheetSessionTestingDataDump\",&,N,V_testingDataDump"
+ "T@\"SFShareSheetSessionTestingDataDump\",&,N,V_testingReferenceDataDump"
+ "T@?,C,N,V_dataDumpHandler"
+ "The activity was canceled while preparing."
+ "_dataDumpHandler"
+ "_setCKShare:setupContainerInfo:shareOptions:"
+ "_setCKShareURLWrapper:share:shareOptions:"
+ "_testingDataDump"
+ "_testingReferenceDataDump"
+ "_updateTestingDataDumpIfNeededForResolvedItems:activityType:"
+ "activityViewControllerSessionDidEndWithSessionID:testingDataDump:completionHandler:"
+ "dataDumpHandler"
+ "extensionsResultWithMatchingAttributes:testingReferenceDataDump:"
+ "setDataDumpHandler:"
+ "setTestingDataDump:"
+ "setTestingReferenceDataDump:"
+ "testingDataDump"
+ "testingReferenceDataDump"
+ "v40@0:8@\"NSString\"16@\"SFShareSheetSessionTestingDataDump\"24@?<v@?@\"NSSecurityScopedURLWrapper\">32"
+ "v40@0:8@\"SFAirDropViewController\"16@\"UISUIActivityExtensionItemDataRequest\"24@?<v@?@\"UISUIActivityExtensionItemData\"@\"NSArray\">32"
+ "v40@0:8@\"UISUIActivityExtensionItemDataRequest\"16@\"NSExtension\"24@?<v@?@\"UISUIActivityExtensionItemData\"@\"NSArray\">32"
- ", usingTestingReferenceSnapshot"
- "@\"SFShareSheetSessionTestingSnapshot\""
- "T@\"SFShareSheetSessionTestingSnapshot\",&,N,V_testingReferenceSnapshot"
- "T@\"SFShareSheetSessionTestingSnapshot\",&,N,V_testingSnapshot"
- "T@?,C,N,V_snapshotHandler"
- "_setCKShare:setupContainerInfo:permissionType:allowOthersToInvite:"
- "_setCKShareURLWrapper:share:permissionType:allowOthersToInvite:"
- "_snapshotHandler"
- "_testingReferenceSnapshot"
- "_testingSnapshot"
- "_updateTestingSnapshotIfNeededForResolvedItems:activityType:"
- "activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:"
- "extensionsResultWithMatchingAttributes:testingReferenceSnapshot:"
- "getCKSharingOptionsFromOptions:accessType:permissionType:allowOthersToInvite:"
- "setSnapshotHandler:"
- "setTestingReferenceSnapshot:"
- "setTestingSnapshot:"
- "snapshotHandler"
- "testingReferenceSnapshot"
- "testingSnapshot"
- "v40@0:8@\"NSString\"16@\"SFShareSheetSessionTestingSnapshot\"24@?<v@?@\"NSSecurityScopedURLWrapper\">32"
- "v40@0:8@\"SFAirDropViewController\"16@\"UISUIActivityExtensionItemDataRequest\"24@?<v@?@\"UISUIActivityExtensionItemData\">32"
- "v40@0:8@\"UISUIActivityExtensionItemDataRequest\"16@\"NSExtension\"24@?<v@?@\"UISUIActivityExtensionItemData\">32"

```
