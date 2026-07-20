## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`

```diff

-5032.5.0.0.0
-  __TEXT.__text: 0x8e09a4
-  __TEXT.__objc_methlist: 0x2e6a4
-  __TEXT.__const: 0x23d48
+5034.0.12.100.0
+  __TEXT.__text: 0x8ecc08
+  __TEXT.__objc_methlist: 0x2e7c8
+  __TEXT.__const: 0x241f8
   __TEXT.__dlopen_cstrs: 0x110b
-  __TEXT.__swift5_typeref: 0xcf8a
-  __TEXT.__cstring: 0x8c702
-  __TEXT.__oslogstring: 0x223f9
-  __TEXT.__constg_swiftt: 0x959c
-  __TEXT.__swift5_reflstr: 0x5ff8
-  __TEXT.__swift5_fieldmd: 0x763c
-  __TEXT.__swift5_builtin: 0x668
-  __TEXT.__swift5_assocty: 0x22f0
-  __TEXT.__swift5_proto: 0x1a30
-  __TEXT.__swift5_types: 0xb00
-  __TEXT.__swift5_capture: 0x588c
+  __TEXT.__swift5_typeref: 0xd12a
+  __TEXT.__cstring: 0x8ccbc
+  __TEXT.__oslogstring: 0x22dd6
+  __TEXT.__constg_swiftt: 0x9684
+  __TEXT.__swift5_reflstr: 0x6078
+  __TEXT.__swift5_fieldmd: 0x7714
+  __TEXT.__swift5_builtin: 0x67c
+  __TEXT.__swift5_assocty: 0x2308
+  __TEXT.__swift5_proto: 0x1a54
+  __TEXT.__swift5_types: 0xb1c
+  __TEXT.__swift5_capture: 0x5aec
   __TEXT.__swift_as_entry: 0xae0
   __TEXT.__swift_as_ret: 0xc3c
-  __TEXT.__swift_as_cont: 0x1450
+  __TEXT.__swift_as_cont: 0x1454
   __TEXT.__swift5_protos: 0x138
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__gcc_except_tab: 0x4cd0
+  __TEXT.__gcc_except_tab: 0x4d04
   __TEXT.__ustring: 0x3f0c
-  __TEXT.__unwind_info: 0x1bd60
-  __TEXT.__eh_frame: 0x22b40
+  __TEXT.__unwind_info: 0x1bfa0
+  __TEXT.__eh_frame: 0x22e80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf088
-  __DATA_CONST.__objc_classlist: 0x23e0
+  __DATA_CONST.__const: 0xf068
+  __DATA_CONST.__objc_classlist: 0x23f8
   __DATA_CONST.__objc_catlist: 0x3e8
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x136e8
+  __DATA_CONST.__objc_selrefs: 0x13758
   __DATA_CONST.__objc_protorefs: 0x2a8
-  __DATA_CONST.__objc_superrefs: 0x1368
+  __DATA_CONST.__objc_superrefs: 0x1370
   __DATA_CONST.__objc_arraydata: 0x16e8
-  __DATA_CONST.__got: 0x5c30
-  __AUTH_CONST.__const: 0x3f248
-  __AUTH_CONST.__cfstring: 0x2bd80
-  __AUTH_CONST.__objc_const: 0x54f88
+  __DATA_CONST.__got: 0x5cd8
+  __AUTH_CONST.__const: 0x3fad0
+  __AUTH_CONST.__cfstring: 0x2bc20
+  __AUTH_CONST.__objc_const: 0x55250
   __AUTH_CONST.__objc_dictobj: 0x500
   __AUTH_CONST.__objc_intobj: 0xf90
   __AUTH_CONST.__objc_arrayobj: 0x960
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x50e0
-  __AUTH.__objc_data: 0x10b88
-  __AUTH.__data: 0x70a8
-  __DATA.__objc_ivar: 0x2148
-  __DATA.__data: 0xd4e0
-  __DATA.__bss: 0x2e248
-  __DATA.__common: 0x2328
-  __DATA_DIRTY.__objc_data: 0x8f20
-  __DATA_DIRTY.__data: 0xce8
+  __AUTH_CONST.__auth_got: 0x5160
+  __AUTH.__objc_data: 0x10cd8
+  __AUTH.__data: 0x70b8
+  __DATA.__objc_ivar: 0x2164
+  __DATA.__data: 0xd648
+  __DATA.__bss: 0x2e6d8
+  __DATA.__common: 0x2410
+  __DATA_DIRTY.__objc_data: 0x8f18
+  __DATA_DIRTY.__data: 0xcd8
   __DATA_DIRTY.__bss: 0x1880
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 43378
-  Symbols:   42958
-  CStrings:  17873
+  Functions: 43626
+  Symbols:   43057
+  CStrings:  17923
 
Symbols:
+ +[WFLinkEntityContentItem isPhotosAlbumEntity]
+ +[WFLinkEntityContentItem photosAssetCollectionCoercionHandler]
+ +[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]
+ -[WFAction addExtendedOperation:]
+ -[WFAction extendedOperationsLock]
+ -[WFAction extendedOperations]
+ -[WFAction removeExtendedOperation:]
+ -[WFAppIntentExecutionAction executor:updateOpensIntentRequest:]
+ -[WFLinkAction executor:didCompleteExecutionWithResult:error:]
+ -[WFLinkPhotosFindAlbumAction localizedNameWithContext:]
+ -[WFManualExtendedOperation .cxx_destruct]
+ -[WFManualExtendedOperation addCompletionHandlerIfRunning:]
+ -[WFManualExtendedOperation cancel]
+ -[WFManualExtendedOperation finish]
+ -[WFManualExtendedOperation init]
+ -[WFShortcutExporter validateBeforeExportWithErrorHandler:]
+ -[WFTestUIPresenterInterface updateOpensIntent:completionHandler:]
+ -[WFWalletTransactionProvider queue_finishWithIdentifier:transaction:]
+ -[WFWalletTransactionProvider setTimeoutInterval:]
+ -[WFWalletTransactionProvider timeoutInterval]
+ GCC_except_table10139
+ GCC_except_table10145
+ GCC_except_table10164
+ GCC_except_table10330
+ GCC_except_table10365
+ GCC_except_table10431
+ GCC_except_table10438
+ GCC_except_table10440
+ GCC_except_table10442
+ GCC_except_table10484
+ GCC_except_table10489
+ GCC_except_table10529
+ GCC_except_table10532
+ GCC_except_table10535
+ GCC_except_table10538
+ GCC_except_table10727
+ GCC_except_table10829
+ GCC_except_table10846
+ GCC_except_table10862
+ GCC_except_table10908
+ GCC_except_table11152
+ GCC_except_table11182
+ GCC_except_table11198
+ GCC_except_table11258
+ GCC_except_table11402
+ GCC_except_table11493
+ GCC_except_table11499
+ GCC_except_table11502
+ GCC_except_table11508
+ GCC_except_table11511
+ GCC_except_table11514
+ GCC_except_table11521
+ GCC_except_table11530
+ GCC_except_table11542
+ GCC_except_table11545
+ GCC_except_table11548
+ GCC_except_table11551
+ GCC_except_table11554
+ GCC_except_table11557
+ GCC_except_table11560
+ GCC_except_table11563
+ GCC_except_table11566
+ GCC_except_table11569
+ GCC_except_table11572
+ GCC_except_table11575
+ GCC_except_table11578
+ GCC_except_table11683
+ GCC_except_table11838
+ GCC_except_table11854
+ GCC_except_table12048
+ GCC_except_table12063
+ GCC_except_table12069
+ GCC_except_table12071
+ GCC_except_table12076
+ GCC_except_table12121
+ GCC_except_table12128
+ GCC_except_table12182
+ GCC_except_table12221
+ GCC_except_table12235
+ GCC_except_table12239
+ GCC_except_table12241
+ GCC_except_table1232
+ GCC_except_table12336
+ GCC_except_table12352
+ GCC_except_table12457
+ GCC_except_table12509
+ GCC_except_table12564
+ GCC_except_table12593
+ GCC_except_table12649
+ GCC_except_table12660
+ GCC_except_table12705
+ GCC_except_table12707
+ GCC_except_table12902
+ GCC_except_table12936
+ GCC_except_table13055
+ GCC_except_table13083
+ GCC_except_table13089
+ GCC_except_table1309
+ GCC_except_table13138
+ GCC_except_table13179
+ GCC_except_table13192
+ GCC_except_table13197
+ GCC_except_table13211
+ GCC_except_table13218
+ GCC_except_table13219
+ GCC_except_table13220
+ GCC_except_table13229
+ GCC_except_table13240
+ GCC_except_table13395
+ GCC_except_table13433
+ GCC_except_table13438
+ GCC_except_table13440
+ GCC_except_table13443
+ GCC_except_table13503
+ GCC_except_table13515
+ GCC_except_table13519
+ GCC_except_table13754
+ GCC_except_table13822
+ GCC_except_table14037
+ GCC_except_table14078
+ GCC_except_table1414
+ GCC_except_table1419
+ GCC_except_table14207
+ GCC_except_table14310
+ GCC_except_table14315
+ GCC_except_table14324
+ GCC_except_table14327
+ GCC_except_table14392
+ GCC_except_table14415
+ GCC_except_table14426
+ GCC_except_table14428
+ GCC_except_table14441
+ GCC_except_table14558
+ GCC_except_table14696
+ GCC_except_table14717
+ GCC_except_table14728
+ GCC_except_table14742
+ GCC_except_table14745
+ GCC_except_table14960
+ GCC_except_table15056
+ GCC_except_table1599
+ GCC_except_table1601
+ GCC_except_table1603
+ GCC_except_table1674
+ GCC_except_table1688
+ GCC_except_table1693
+ GCC_except_table1695
+ GCC_except_table1697
+ GCC_except_table1962
+ GCC_except_table2038
+ GCC_except_table2133
+ GCC_except_table2344
+ GCC_except_table2354
+ GCC_except_table2359
+ GCC_except_table2387
+ GCC_except_table2558
+ GCC_except_table2585
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table2659
+ GCC_except_table2700
+ GCC_except_table2811
+ GCC_except_table2825
+ GCC_except_table284
+ GCC_except_table2892
+ GCC_except_table2936
+ GCC_except_table2942
+ GCC_except_table2994
+ GCC_except_table3004
+ GCC_except_table3012
+ GCC_except_table3020
+ GCC_except_table3048
+ GCC_except_table3091
+ GCC_except_table3393
+ GCC_except_table3416
+ GCC_except_table3417
+ GCC_except_table3424
+ GCC_except_table3425
+ GCC_except_table3426
+ GCC_except_table3427
+ GCC_except_table3452
+ GCC_except_table3456
+ GCC_except_table3481
+ GCC_except_table3486
+ GCC_except_table3519
+ GCC_except_table3535
+ GCC_except_table3539
+ GCC_except_table3599
+ GCC_except_table3610
+ GCC_except_table3612
+ GCC_except_table3615
+ GCC_except_table3726
+ GCC_except_table3730
+ GCC_except_table3732
+ GCC_except_table3736
+ GCC_except_table3737
+ GCC_except_table384
+ GCC_except_table387
+ GCC_except_table3876
+ GCC_except_table4002
+ GCC_except_table4006
+ GCC_except_table4386
+ GCC_except_table4387
+ GCC_except_table4505
+ GCC_except_table4594
+ GCC_except_table4607
+ GCC_except_table4626
+ GCC_except_table4634
+ GCC_except_table4783
+ GCC_except_table4979
+ GCC_except_table4985
+ GCC_except_table4991
+ GCC_except_table5040
+ GCC_except_table5054
+ GCC_except_table5113
+ GCC_except_table5184
+ GCC_except_table5211
+ GCC_except_table5215
+ GCC_except_table5259
+ GCC_except_table5320
+ GCC_except_table5329
+ GCC_except_table5351
+ GCC_except_table5391
+ GCC_except_table5447
+ GCC_except_table5452
+ GCC_except_table5454
+ GCC_except_table5558
+ GCC_except_table5564
+ GCC_except_table5580
+ GCC_except_table570
+ GCC_except_table5906
+ GCC_except_table6052
+ GCC_except_table6085
+ GCC_except_table6159
+ GCC_except_table6171
+ GCC_except_table6284
+ GCC_except_table6363
+ GCC_except_table6431
+ GCC_except_table6432
+ GCC_except_table6433
+ GCC_except_table6533
+ GCC_except_table6600
+ GCC_except_table666
+ GCC_except_table6959
+ GCC_except_table696
+ GCC_except_table6972
+ GCC_except_table6981
+ GCC_except_table699
+ GCC_except_table701
+ GCC_except_table7013
+ GCC_except_table703
+ GCC_except_table7064
+ GCC_except_table7065
+ GCC_except_table707
+ GCC_except_table7070
+ GCC_except_table7071
+ GCC_except_table7074
+ GCC_except_table7080
+ GCC_except_table7085
+ GCC_except_table7090
+ GCC_except_table7091
+ GCC_except_table7130
+ GCC_except_table7135
+ GCC_except_table7193
+ GCC_except_table7204
+ GCC_except_table7267
+ GCC_except_table7268
+ GCC_except_table7477
+ GCC_except_table7487
+ GCC_except_table7564
+ GCC_except_table7574
+ GCC_except_table7637
+ GCC_except_table7814
+ GCC_except_table7857
+ GCC_except_table7904
+ GCC_except_table7905
+ GCC_except_table7945
+ GCC_except_table8076
+ GCC_except_table8214
+ GCC_except_table8219
+ GCC_except_table8230
+ GCC_except_table8351
+ GCC_except_table8362
+ GCC_except_table8420
+ GCC_except_table8431
+ GCC_except_table8433
+ GCC_except_table8435
+ GCC_except_table8436
+ GCC_except_table869
+ GCC_except_table8960
+ GCC_except_table9001
+ GCC_except_table9006
+ GCC_except_table9009
+ GCC_except_table9011
+ GCC_except_table9013
+ GCC_except_table9042
+ GCC_except_table9084
+ GCC_except_table9182
+ GCC_except_table9234
+ GCC_except_table943
+ GCC_except_table9454
+ GCC_except_table9458
+ GCC_except_table9460
+ GCC_except_table9462
+ GCC_except_table9470
+ GCC_except_table9482
+ GCC_except_table9486
+ GCC_except_table9499
+ GCC_except_table9512
+ GCC_except_table9518
+ GCC_except_table952
+ GCC_except_table9526
+ GCC_except_table9573
+ GCC_except_table9579
+ GCC_except_table9585
+ GCC_except_table96
+ GCC_except_table9724
+ GCC_except_table9783
+ GCC_except_table9812
+ GCC_except_table9814
+ GCC_except_table9820
+ GCC_except_table9822
+ GCC_except_table9824
+ GCC_except_table9831
+ GCC_except_table985
+ GCC_except_table9852
+ GCC_except_table9853
+ GCC_except_table9854
+ GCC_except_table9856
+ GCC_except_table9861
+ GCC_except_table99
+ GCC_except_table9969
+ _LNActionConfigurationContextWidgetFamilySystemExtraLargePortrait
+ _OBJC_CLASS_$_LNAnyEntityType
+ _OBJC_CLASS_$_LNEntityQueryRequestType
+ _OBJC_CLASS_$_WFLinkPhotosFindAlbumAction
+ _OBJC_CLASS_$_WFManualExtendedOperation
+ _OBJC_CLASS_$_WFPhotoAlbumLibraryFiltering
+ _OBJC_CLASS_$_WFShortcutValidator
+ _OBJC_IVAR_$_WFAction._extendedOperations
+ _OBJC_IVAR_$_WFAction._extendedOperationsLock
+ _OBJC_IVAR_$_WFLinkAction._donationOperation
+ _OBJC_IVAR_$_WFManualExtendedOperation._completionHandlers
+ _OBJC_IVAR_$_WFManualExtendedOperation._lock
+ _OBJC_IVAR_$_WFManualExtendedOperation._running
+ _OBJC_IVAR_$_WFParameter._localizedStringCacheLock
+ _OBJC_IVAR_$_WFWalletTransactionProvider._timeoutInterval
+ _OBJC_METACLASS_$_WFLinkPhotosFindAlbumAction
+ _OBJC_METACLASS_$_WFManualExtendedOperation
+ _OBJC_METACLASS_$_WFShortcutValidator
+ _PhotosLibrary
+ _WFLinkActionIdentifierPhotosFindAlbum
+ _WFLinkEntityPropertyDenyList
+ _WFLinkPhotoAlbumEntityTypeName
+ _WFPhotoAlbumPropertyAlbumType
+ _WFPhotoAlbumPropertyDateCreated
+ _WFWorkflowBundleIdentifierForRunDescriptor
+ _WFWorkflowIntentIdentifierForRunDescriptor
+ __CLASS_METHODS_WFShortcutValidator
+ __DATA_WFShortcutValidator
+ __INSTANCE_METHODS_WFShortcutValidator
+ __METACLASS_DATA_WFShortcutValidator
+ __OBJC_$_INSTANCE_METHODS_WFLinkPhotosFindAlbumAction
+ __OBJC_$_INSTANCE_METHODS_WFManualExtendedOperation
+ __OBJC_$_INSTANCE_VARIABLES_WFManualExtendedOperation
+ __OBJC_$_PROP_LIST_WFManualExtendedOperation
+ __OBJC_CLASS_PROTOCOLS_$_WFManualExtendedOperation
+ __OBJC_CLASS_RO_$_WFLinkPhotosFindAlbumAction
+ __OBJC_CLASS_RO_$_WFManualExtendedOperation
+ __OBJC_METACLASS_RO_$_WFLinkPhotosFindAlbumAction
+ __OBJC_METACLASS_RO_$_WFManualExtendedOperation
+ ___52+[WFFileValue createBookmarkWithFileURL:workflowID:]_block_invoke
+ ___53-[WFAppIntentExecutionAction finishRunningWithError:]_block_invoke
+ ___55-[WFAppIntentExecutionAction lastKnownConnectionPolicy]_block_invoke
+ ___63+[WFLinkEntityContentItem photosAssetCollectionCoercionHandler]_block_invoke
+ ___64-[WFAppIntentExecutionAction executor:updateOpensIntentRequest:]_block_invoke
+ ___64-[WFAppIntentExecutionAction executor:updateOpensIntentRequest:]_block_invoke_2
+ ___64-[WFSmartPromptDialogRequest initWithConfiguration:attribution:]_block_invoke
+ ___84+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]_block_invoke
+ ___84+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]_block_invoke_2
+ ___block_descriptor_32_e50_"LNEntityIdentifier"24?0"PHAssetCollection"8Q16l
+ ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s_e57_"WFContentPropertyBuilder"24?0"LNPropertyMetadata"8Q16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e35_v16?0"WFStepwiseExecutionResult"8ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___swift_closure_destructor.139Tm
+ ___swift_closure_destructor.161Tm
+ ___swift_exist.box.addr_destructor.198Tm
+ ___swift_memcpy256_8
+ _associated conformance 11WorkflowKit15TopHitIconStyleOSHAASQ
+ _associated conformance 11WorkflowKit32WFShortcutSharingValidationErrorV10Foundation09LocalizedF0AAs0F0
+ _associated conformance 11WorkflowKit32WFShortcutSharingValidationErrorV10Foundation13CustomNSErrorAAs0F0
+ _associated conformance 11WorkflowKit34WFShortcutSharingValidationContextOSHAASQ
+ _objc_msgSend$ISOCountryCode
+ _objc_msgSend$addExtendedOperation:
+ _objc_msgSend$allowLinkContextualActionRunningForBundleIdentifier:intentIdentifier:
+ _objc_msgSend$appShortcutBundles:
+ _objc_msgSend$city
+ _objc_msgSend$extendedOperations
+ _objc_msgSend$getItemsMatchingQuery:withInput:resultHandler:
+ _objc_msgSend$initWithBackgroundColorValue:glyphCharacter:
+ _objc_msgSend$initWithEntityIdentifiers:
+ _objc_msgSend$isPhotosAlbumEntity
+ _objc_msgSend$opensIntent
+ _objc_msgSend$photosAssetCollectionCoercionHandler
+ _objc_msgSend$queue_finishWithIdentifier:transaction:
+ _objc_msgSend$removeExtendedOperation:
+ _objc_msgSend$removeObjectIdenticalTo:
+ _objc_msgSend$timeoutInterval
+ _objc_msgSend$updateOpensIntent:completionHandler:
+ _objc_msgSend$validateBeforeExportWithErrorHandler:
+ _objc_msgSend$validateForExportWorkflow:error:
+ _symbolic $s11WorkflowKit32WFShortcutSharingValidationCheckP
+ _symbolic SS12parameterKey_SS15typeDescriptiont
+ _symbolic SS16actionIdentifier_t
+ _symbolic Say_____G 11WorkflowKit32WFShortcutSharingRejectionReasonO
+ _symbolic Say_____y_____GG 12HybridSearch6ResultV AA11MailContentV
+ _symbolic So10LNPropertyC
+ _symbolic So26WFActionDefinitionRegistryCXMT
+ _symbolic _____ 11WorkflowKit15TopHitIconStyleO
+ _symbolic _____ 11WorkflowKit26WFShortcutSharingValidatorC
+ _symbolic _____ 11WorkflowKit27WFNonAllowlistedActionCheckV
+ _symbolic _____ 11WorkflowKit32WFShortcutSharingRejectionReasonO
+ _symbolic _____ 11WorkflowKit32WFShortcutSharingValidationErrorV
+ _symbolic _____ 11WorkflowKit34WFShortcutSharingValidationContextO
+ _symbolic _____ So19WFLocationParameterC11WorkflowKitE13NamedLocation33_DE2B75C4610EAE9BC7AC5CC4088F8574LLV
+ _symbolic _____7wrapped_t 12ToolRenderer15PythonTypeProxyO
+ _symbolic _____Sg 7ToolKit19ContainerDefinitionV6DeviceO
+ _symbolic _____Sg_ABt 7ToolKit19ContainerDefinitionV6DeviceO
+ _symbolic _____ySS3key______5valuetG s23_ContiguousArrayStorageC 7ToolKit18ConcreteResolvableO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11WorkflowKit32WFShortcutSharingRejectionReasonO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12HybridSearch11MailContentV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So19WFLocationParameterC11WorkflowKitE13NamedLocation33_DE2B75C4610EAE9BC7AC5CC4088F8574LLV
+ _symbolic _____y______So17OS_dispatch_queueCG 7Combine10PublishersO8DebounceV So20NSNotificationCenterC10FoundationE9PublisherV
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 11WorkflowKit32WFShortcutSharingValidationCheckP
+ _symbolic _____y______y______So17OS_dispatch_queueCGAEG 7Combine10PublishersO9ReceiveOnV AC8DebounceV So20NSNotificationCenterC10FoundationE9PublisherV
+ _type_layout_string 11WorkflowKit22ActionDrawerDataLoader33_3DEEF7B2499E1B37D3EC5450A935870FLLC17ToolkitLoadResultV
+ _type_layout_string 11WorkflowKit32WFShortcutSharingRejectionReasonO
+ _type_layout_string 11WorkflowKit32WFShortcutSharingValidationErrorV
+ _type_layout_string So19WFLocationParameterC11WorkflowKitE13NamedLocation33_DE2B75C4610EAE9BC7AC5CC4088F8574LLV
- -[WFAction extendedOperation]
- -[WFAction setExtendedOperation:]
- -[WFParameter localizedStringCache]
- -[WFParameter setLocalizedStringCache:]
- -[WFWalletTransactionProvider queue_finishWithPaymentTransaction:]
- GCC_except_table10121
- GCC_except_table10127
- GCC_except_table10146
- GCC_except_table10311
- GCC_except_table10346
- GCC_except_table10412
- GCC_except_table10419
- GCC_except_table10421
- GCC_except_table10423
- GCC_except_table10465
- GCC_except_table10470
- GCC_except_table10510
- GCC_except_table10513
- GCC_except_table10516
- GCC_except_table10519
- GCC_except_table10708
- GCC_except_table10810
- GCC_except_table10827
- GCC_except_table10843
- GCC_except_table10889
- GCC_except_table11133
- GCC_except_table11160
- GCC_except_table11163
- GCC_except_table11239
- GCC_except_table11382
- GCC_except_table11473
- GCC_except_table11479
- GCC_except_table11482
- GCC_except_table11485
- GCC_except_table11488
- GCC_except_table11491
- GCC_except_table11494
- GCC_except_table11497
- GCC_except_table11501
- GCC_except_table11510
- GCC_except_table11522
- GCC_except_table11528
- GCC_except_table11531
- GCC_except_table11534
- GCC_except_table11540
- GCC_except_table11543
- GCC_except_table11546
- GCC_except_table11549
- GCC_except_table11552
- GCC_except_table11555
- GCC_except_table11558
- GCC_except_table11663
- GCC_except_table11818
- GCC_except_table11834
- GCC_except_table12028
- GCC_except_table12043
- GCC_except_table12049
- GCC_except_table12051
- GCC_except_table12056
- GCC_except_table12088
- GCC_except_table12101
- GCC_except_table12163
- GCC_except_table12202
- GCC_except_table12216
- GCC_except_table12218
- GCC_except_table12220
- GCC_except_table1224
- GCC_except_table12311
- GCC_except_table12327
- GCC_except_table12432
- GCC_except_table12484
- GCC_except_table12539
- GCC_except_table12568
- GCC_except_table12624
- GCC_except_table12635
- GCC_except_table12680
- GCC_except_table12682
- GCC_except_table12877
- GCC_except_table12911
- GCC_except_table1301
- GCC_except_table13030
- GCC_except_table13058
- GCC_except_table13064
- GCC_except_table13113
- GCC_except_table13154
- GCC_except_table13167
- GCC_except_table13172
- GCC_except_table13186
- GCC_except_table13193
- GCC_except_table13194
- GCC_except_table13195
- GCC_except_table13204
- GCC_except_table13215
- GCC_except_table13370
- GCC_except_table13406
- GCC_except_table13411
- GCC_except_table13413
- GCC_except_table13416
- GCC_except_table13476
- GCC_except_table13488
- GCC_except_table13492
- GCC_except_table13727
- GCC_except_table13795
- GCC_except_table14010
- GCC_except_table14051
- GCC_except_table1406
- GCC_except_table1411
- GCC_except_table14180
- GCC_except_table14283
- GCC_except_table14288
- GCC_except_table14297
- GCC_except_table14300
- GCC_except_table14365
- GCC_except_table14388
- GCC_except_table14399
- GCC_except_table14401
- GCC_except_table14414
- GCC_except_table14531
- GCC_except_table14669
- GCC_except_table14690
- GCC_except_table14701
- GCC_except_table14715
- GCC_except_table14718
- GCC_except_table14906
- GCC_except_table15028
- GCC_except_table1587
- GCC_except_table1591
- GCC_except_table1593
- GCC_except_table1666
- GCC_except_table1680
- GCC_except_table1685
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table1954
- GCC_except_table2030
- GCC_except_table2113
- GCC_except_table2335
- GCC_except_table2345
- GCC_except_table2350
- GCC_except_table2378
- GCC_except_table251
- GCC_except_table2549
- GCC_except_table255
- GCC_except_table2576
- GCC_except_table2647
- GCC_except_table266
- GCC_except_table2683
- GCC_except_table2791
- GCC_except_table2794
- GCC_except_table2875
- GCC_except_table2902
- GCC_except_table2925
- GCC_except_table2977
- GCC_except_table2987
- GCC_except_table2995
- GCC_except_table3003
- GCC_except_table3031
- GCC_except_table3074
- GCC_except_table3376
- GCC_except_table3399
- GCC_except_table3400
- GCC_except_table3407
- GCC_except_table3408
- GCC_except_table3409
- GCC_except_table3410
- GCC_except_table3435
- GCC_except_table3439
- GCC_except_table3464
- GCC_except_table3469
- GCC_except_table3502
- GCC_except_table3518
- GCC_except_table3522
- GCC_except_table3582
- GCC_except_table3593
- GCC_except_table3595
- GCC_except_table3598
- GCC_except_table3709
- GCC_except_table3713
- GCC_except_table3715
- GCC_except_table3719
- GCC_except_table3720
- GCC_except_table375
- GCC_except_table378
- GCC_except_table3859
- GCC_except_table3985
- GCC_except_table3989
- GCC_except_table4369
- GCC_except_table4370
- GCC_except_table4488
- GCC_except_table4576
- GCC_except_table4589
- GCC_except_table4608
- GCC_except_table4616
- GCC_except_table4765
- GCC_except_table4961
- GCC_except_table4967
- GCC_except_table4973
- GCC_except_table5022
- GCC_except_table5036
- GCC_except_table5095
- GCC_except_table5166
- GCC_except_table5193
- GCC_except_table5197
- GCC_except_table5241
- GCC_except_table5302
- GCC_except_table5311
- GCC_except_table5333
- GCC_except_table5373
- GCC_except_table5429
- GCC_except_table5434
- GCC_except_table5436
- GCC_except_table5540
- GCC_except_table5546
- GCC_except_table5562
- GCC_except_table561
- GCC_except_table5889
- GCC_except_table6035
- GCC_except_table6068
- GCC_except_table6142
- GCC_except_table6154
- GCC_except_table6267
- GCC_except_table6345
- GCC_except_table6413
- GCC_except_table6414
- GCC_except_table6415
- GCC_except_table6515
- GCC_except_table6564
- GCC_except_table657
- GCC_except_table6603
- GCC_except_table687
- GCC_except_table690
- GCC_except_table692
- GCC_except_table694
- GCC_except_table6941
- GCC_except_table6954
- GCC_except_table6963
- GCC_except_table698
- GCC_except_table6995
- GCC_except_table7046
- GCC_except_table7047
- GCC_except_table7052
- GCC_except_table7053
- GCC_except_table7056
- GCC_except_table7062
- GCC_except_table7067
- GCC_except_table7072
- GCC_except_table7073
- GCC_except_table7112
- GCC_except_table7117
- GCC_except_table7175
- GCC_except_table7186
- GCC_except_table7249
- GCC_except_table7250
- GCC_except_table7459
- GCC_except_table7469
- GCC_except_table7546
- GCC_except_table7556
- GCC_except_table7619
- GCC_except_table7796
- GCC_except_table7839
- GCC_except_table7886
- GCC_except_table7887
- GCC_except_table7927
- GCC_except_table8058
- GCC_except_table8196
- GCC_except_table8201
- GCC_except_table8212
- GCC_except_table8326
- GCC_except_table8333
- GCC_except_table8402
- GCC_except_table8413
- GCC_except_table8415
- GCC_except_table8417
- GCC_except_table8418
- GCC_except_table859
- GCC_except_table87
- GCC_except_table8942
- GCC_except_table8983
- GCC_except_table8988
- GCC_except_table8991
- GCC_except_table8993
- GCC_except_table8995
- GCC_except_table9024
- GCC_except_table9066
- GCC_except_table9164
- GCC_except_table9216
- GCC_except_table933
- GCC_except_table942
- GCC_except_table9428
- GCC_except_table9434
- GCC_except_table9436
- GCC_except_table9440
- GCC_except_table9442
- GCC_except_table9444
- GCC_except_table9450
- GCC_except_table9481
- GCC_except_table9494
- GCC_except_table9500
- GCC_except_table9508
- GCC_except_table9555
- GCC_except_table9561
- GCC_except_table9567
- GCC_except_table9706
- GCC_except_table975
- GCC_except_table9765
- GCC_except_table9794
- GCC_except_table9796
- GCC_except_table9802
- GCC_except_table9804
- GCC_except_table9806
- GCC_except_table9813
- GCC_except_table9834
- GCC_except_table9835
- GCC_except_table9836
- GCC_except_table9838
- GCC_except_table9843
- GCC_except_table9951
- _OBJC_IVAR_$_WFAction._extendedOperation
- _WFSerializedRepresentationFromWFINObject
- _WFShortcutSourceAddToSiri
- _WFShortcutSourceAutomatorMigration
- _WFShortcutSourceDescribeAShortcut
- _WFShortcutSourceEditorDocumentMenu
- _WFShortcutSourceSiriTopLevelShortcut
- ___block_descriptor_64_e8_32s40s48s_e57_"WFContentPropertyBuilder"24?0"LNPropertyMetadata"8Q16ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e35_v16?0"WFStepwiseExecutionResult"8ls32l8s40l8s48l8s56l8s72l8s64l8
- ___swift_closure_destructor.106Tm
- ___swift_closure_destructor.128Tm
- ___swift_exist.box.addr_destructor.195Tm
- ___swift_memcpy248_8
- _objc_msgSend$allowLinkContextualActionRunningForBundleIdentifier:
- _objc_msgSend$bundlesWithError:
- _objc_msgSend$escapedPatternForString:
- _objc_msgSend$extendedOperation
- _objc_msgSend$initWithBackgroundColorValue:glyphCharacter:customImageData:
- _objc_msgSend$localizedStringCache
- _objc_msgSend$queue_finishWithPaymentTransaction:
- _objc_msgSend$setExtendedOperation:
- _symbolic $s11WorkflowKit25AppShortcutBundleProviderP
- _symbolic ______p 11WorkflowKit25AppShortcutBundleProviderP
CStrings:
+ "%K >= 0 AND %K < %d"
+ "%s Cannot export shortcut because we failed to init WFWorkflow from record. Error: %{public}@"
+ "%s Cannot finish payment transaction with a nil identifier"
+ "%s Cannot observe for transaction updates with a nil identifier; finishing."
+ "%s Decoded out-of-range WFTriggerNotificationLevel %d; treating as Never"
+ "%s Errored out while trying to do photo album querying - %@"
+ "%s Failed to init WFEmailAddress from %{private}@"
+ "%s Failed to init WFPhoneNumber from %{private}@"
+ "%s Hiding property '%@' from entity '%@' because denylisted"
+ "%s Hit this for a %@ entity type on the %@ bundle. This is very wrong"
+ "%s No PHAssetCollection found for collection identifier: %{public}@, library: %li"
+ "%s Refusing to create bookmark for URL that is not a file URL or has an empty path: %@"
+ "%s Unable to form a LNConnection with app connection policy for %@"
+ "%s Unable to perform identifier based query for album entity - %@"
+ "+[WFLinkEntityContentItem photosAssetCollectionCoercionHandler]_block_invoke"
+ "+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]"
+ "+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]_block_invoke"
+ "+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]_block_invoke_2"
+ "-[WFAppIntentExecutionAction executor:updateOpensIntentRequest:]_block_invoke_2"
+ "-[WFEmailAddressSubstitutableState stringInterpretedAsContactHandle:allowsCustomHandles:]"
+ "-[WFPhoneNumberSubstitutableState stringInterpretedAsContactHandle:allowsCustomHandles:]"
+ "-[WFShortcutExporter validateBeforeExportWithErrorHandler:]"
+ "-[WFWalletTransactionProvider queue_finishWithIdentifier:transaction:]"
+ "@\"LNEntityIdentifier\"24@?0@\"PHAssetCollection\"8Q16"
+ "At time"
+ "Attempted to unregister trigger %{public}@ but no matching registration was found"
+ "Biome trigger (remote) fired with identifier: %{public}@, input: %{private}s"
+ "Biome trigger fired with identifier: %{public}@, input: %{private}s"
+ "Cancelling Biome trigger registration with identifier: %{public}@"
+ "Cancelling CoreDuet trigger registration with identifier: %{public}@"
+ "Cancelling remote Biome trigger registration with identifier: %{public}@"
+ "Can’t Import Shortcut"
+ "Can’t Share Shortcut"
+ "CoreDuet trigger callback fired with identifier: %{public}@, input: %{private}s"
+ "Error while firing CoreDuet trigger %{public}@: %{public}@"
+ "Failed register for updates from context sync client for stream %{public}s (trigger %{public}@) with error: %{public}@"
+ "Failed to convert link value for parameter '%s' to typed value due to error: %s."
+ "Failed to convert string into WFContactFieldEntry"
+ "Failed to create WFContactFieldEntry from handle string: %{private}s"
+ "Failed to create catalog entry for Me Card address: %s"
+ "Failed to initialize WFTriggerRegistrationStore: _CDClientContext.user() returned nil for client identifier %{public}s. CoreDuet triggers will not be registered."
+ "Failed to register CoreDuet (watch) trigger %{public}@: predicate is not a _CDMDCSContextualPredicate (invalid for platform)"
+ "Failed to register CoreDuet trigger %{public}@: _CDContextualChangeRegistration creation failed"
+ "Failed to unregister context sync client for stream %{public}s (trigger %{public}@) with error: %{public}@"
+ "Find Albums"
+ "Focus trigger skipped from firing due to identifier mismatch. target: (%s, semantic:%s mode:%s)"
+ "Migrated focus trigger with identifier %s for trigger: %s"
+ "No dedicated contextSync identifier for stream %{public}s, falling back to com.apple.shortcuts — add a unique identifier to avoid subscription collisions"
+ "No existing registration to remove before registering %{public}@: %{public}@"
+ "Refusing to %{public}s shortcut with reasons: %s"
+ "Registering Biome trigger with identifier: %{public}@, stream: %{public}@"
+ "Registering CoreDuet trigger with identifier: %{public}@, registration: %{public}@"
+ "Registering remote Biome trigger with identifier: %{public}@, stream: %{public}@"
+ "Remote tool %s parameter '%s' has type(s) [%s] incompatible with target %s — should be .attributed to the target device before remote execution"
+ "SMS"
+ "Successfully registered for updates with context sync client for stream: %{public}s"
+ "Successfully unregistered from context sync client for stream: %{public}s"
+ "This shortcut can’t be imported because it contains features not supported on this device."
+ "This shortcut can’t be shared because it contains unsupported features."
+ "Trigger %{public}@ fired with event info: %{private}s"
+ "Unable to fire trigger %{public}@ since delegate is nil"
+ "Unknown(%d)"
+ "WFEnforceSharingValidation"
+ "WFLinkContentItemFilterAction.executeGLPMailQuery: hydrated %ld/%ld items (%ld distinct from scan) orderBy=%{public}s random=%{bool}d"
+ "WFMailGLPSearchClient.scan orderBy=%{public}s scanLimit=%ld raw=%ld distinct=%ld"
+ "WFMailGLPSearchClient.search limit=%ld scanLimit=%ld raw=%ld distinct=%ld returned=%ld"
+ "WFValidatedTriggerNotificationLevel"
+ "When I close an app"
+ "When I open an app"
+ "When I receive a message"
+ "When I receive a notification"
+ "When I receive an email"
+ "When enabled, any shortcut on your device can access and update this stored value. Otherwise, the value is only accessible within this shortcut."
+ "When enabled, any shortcut on your device can access and update this stored value. Otherwise, the value is only accessible within this shortcut. (WFStoredContentGlobalValue)"
+ "[%s] [AskLLM] Unable to get generative model name from value properties (keys: %s)"
+ "[%s] [AskLLM] Unable to get text from value properties (keys: %s)"
+ "automatic"
+ "automation"
+ "changed"
+ "com.apple.mobileslideshow.AlbumEntity"
+ "iMessage"
+ "launch"
+ "mail"
+ "misattributed attributed<"
+ "public.stored-url"
+ "pull: refusing .local-stamped container in tool %s; local data must not arrive via sync"
+ "quit"
+ "scanned"
+ "tapped"
+ "unconverted custom<"
+ "\xf0\xf0a"
- "Biome trigger (remote) fired with identifier: %@, input: %s"
- "Biome trigger fired with identifier: %@, input: %s"
- "Cancelling Biome trigger registration with identifier: %@"
- "Cancelling CoreDuet trigger registration with identifier: %@"
- "Cancelling remote Biome trigger registration with identifier: %@"
- "CoreDuet trigger callback fired with identifier: %@, input: %s"
- "Error while firing trigger: %@"
- "Failed register for updates from context sync client with error: %@"
- "Failed to convert link value: (%s) to typed value due to error: %s."
- "Failed to unregister client with error: %@"
- "Focus trigger not firing: identifier mismatch (%s vs %s)"
- "No dedicated contextSync identifier for stream %s, falling back to com.apple.shortcuts — add a unique identifier to avoid subscription collisions"
- "Registering Biome trigger with identifier: %@, stream: %@"
- "Registering CoreDuet trigger with identifier: %@, registration: %@"
- "Registering remote Biome trigger with identifier: %@, stream: %@"
- "ShortcutSourceActiveStarterShortcut"
- "ShortcutSourceAddToSiri"
- "ShortcutSourceAppShortcut"
- "ShortcutSourceAutomatorMigration"
- "ShortcutSourceCloudLink"
- "ShortcutSourceDefaultShortcut"
- "ShortcutSourceDescribeAShortcut"
- "ShortcutSourceEditorDocumentMenu"
- "ShortcutSourceFileKnownContacts"
- "ShortcutSourceFilePersonal"
- "ShortcutSourceFilePublic"
- "ShortcutSourceGallery"
- "ShortcutSourceOnDevice"
- "ShortcutSourceSiriTopLevelShortcut"
- "ShortcutSourceUnknown"
- "Successfully registered for updates with context sync client for stream: %s"
- "Successfully unregistered from context sync client for stream: %s"
- "Trigger %@ fired with event info: %s"
- "Unable to fire trigger since delegate is nil"
- "WFLinkContentItemFilterAction.executeGLPMailQuery: hydrated %ld/%ld items (scanned %ld) orderBy=%{public}s random=%{bool}d"
- "WFMailGLPSearchClient.scan orderBy=%{public}s limit=%ld raw=%ld identifiers=%ld"
- "WFMailGLPSearchClient.search limit=%ld raw=%ld identifiers=%ld"
- "WFWorkflowIconImageData"
- "[%s] [AskLLM] Unable to get generative model name from value properties: %s"
- "[%s] [AskLLM] Unable to get text from value properties: %s"
- "\xf0\xf0Q"
```
