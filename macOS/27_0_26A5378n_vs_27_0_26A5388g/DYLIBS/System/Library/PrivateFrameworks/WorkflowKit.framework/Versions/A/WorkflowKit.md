## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`

```diff

-5032.5.0.0.0
-  __TEXT.__text: 0x90f230
-  __TEXT.__objc_methlist: 0x2ebfc
-  __TEXT.__const: 0x23b98
+5034.0.10.0.0
+  __TEXT.__text: 0x91b5dc
+  __TEXT.__objc_methlist: 0x2ed38
+  __TEXT.__const: 0x24038
   __TEXT.__dlopen_cstrs: 0xeec
-  __TEXT.__swift5_typeref: 0xcc1a
-  __TEXT.__cstring: 0x8be35
-  __TEXT.__oslogstring: 0x21609
-  __TEXT.__constg_swiftt: 0x94e4
-  __TEXT.__swift5_reflstr: 0x5fa8
-  __TEXT.__swift5_fieldmd: 0x7568
-  __TEXT.__swift5_builtin: 0x654
-  __TEXT.__swift5_assocty: 0x2320
-  __TEXT.__swift5_proto: 0x1a48
-  __TEXT.__swift5_types: 0xaf0
-  __TEXT.__swift5_capture: 0x5188
+  __TEXT.__swift5_typeref: 0xcdba
+  __TEXT.__cstring: 0x8c3ef
+  __TEXT.__oslogstring: 0x21fe6
+  __TEXT.__constg_swiftt: 0x95cc
+  __TEXT.__swift5_reflstr: 0x6028
+  __TEXT.__swift5_fieldmd: 0x7640
+  __TEXT.__swift5_builtin: 0x668
+  __TEXT.__swift5_assocty: 0x2338
+  __TEXT.__swift5_proto: 0x1a6c
+  __TEXT.__swift5_types: 0xb0c
+  __TEXT.__swift5_capture: 0x53e8
   __TEXT.__swift_as_entry: 0xac0
   __TEXT.__swift_as_ret: 0xbe4
-  __TEXT.__swift_as_cont: 0x1364
+  __TEXT.__swift_as_cont: 0x1368
   __TEXT.__swift5_protos: 0x138
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__gcc_except_tab: 0x4cfc
+  __TEXT.__gcc_except_tab: 0x4d30
   __TEXT.__ustring: 0x3d82
-  __TEXT.__unwind_info: 0x1b1f0
-  __TEXT.__eh_frame: 0x21a20
+  __TEXT.__unwind_info: 0x1b398
+  __TEXT.__eh_frame: 0x21d80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5050
-  __DATA_CONST.__objc_classlist: 0x2418
+  __DATA_CONST.__const: 0x5008
+  __DATA_CONST.__objc_classlist: 0x2430
   __DATA_CONST.__objc_catlist: 0x3e8
-  __DATA_CONST.__objc_protolist: 0x680
+  __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x136b8
+  __DATA_CONST.__objc_selrefs: 0x13728
   __DATA_CONST.__objc_protorefs: 0x298
-  __DATA_CONST.__objc_superrefs: 0x1388
+  __DATA_CONST.__objc_superrefs: 0x1390
   __DATA_CONST.__objc_arraydata: 0x1728
-  __DATA_CONST.__got: 0x5b20
-  __AUTH_CONST.__const: 0x49840
-  __AUTH_CONST.__cfstring: 0x2c780
-  __AUTH_CONST.__objc_const: 0x55718
+  __DATA_CONST.__got: 0x5bc0
+  __AUTH_CONST.__const: 0x4a0c8
+  __AUTH_CONST.__cfstring: 0x2c620
+  __AUTH_CONST.__objc_const: 0x55a08
   __AUTH_CONST.__objc_dictobj: 0x528
   __AUTH_CONST.__objc_intobj: 0x1038
   __AUTH_CONST.__objc_arrayobj: 0x978
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x4d88
-  __AUTH.__objc_data: 0xf4c8
-  __AUTH.__data: 0x6378
-  __DATA.__objc_ivar: 0x21c4
-  __DATA.__data: 0xc780
-  __DATA.__bss: 0x2d680
-  __DATA.__common: 0x2310
-  __DATA_DIRTY.__objc_data: 0xa730
-  __DATA_DIRTY.__data: 0x1e78
+  __AUTH_CONST.__auth_got: 0x4e08
+  __AUTH.__objc_data: 0xf618
+  __AUTH.__data: 0x63b8
+  __DATA.__objc_ivar: 0x21e0
+  __DATA.__data: 0xc8a8
+  __DATA.__bss: 0x2db10
+  __DATA.__common: 0x23f8
+  __DATA_DIRTY.__objc_data: 0xa728
+  __DATA_DIRTY.__data: 0x1e98
   __DATA_DIRTY.__bss: 0x2358
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 42839
-  Symbols:   43033
-  CStrings:  17820
+  Functions: 43081
+  Symbols:   43137
+  CStrings:  17870
 
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
+ GCC_except_table10035
+ GCC_except_table1007
+ GCC_except_table10205
+ GCC_except_table10211
+ GCC_except_table10230
+ GCC_except_table10396
+ GCC_except_table1040
+ GCC_except_table10431
+ GCC_except_table10464
+ GCC_except_table10466
+ GCC_except_table10491
+ GCC_except_table10498
+ GCC_except_table10500
+ GCC_except_table10502
+ GCC_except_table10544
+ GCC_except_table10549
+ GCC_except_table10589
+ GCC_except_table10592
+ GCC_except_table10595
+ GCC_except_table10598
+ GCC_except_table10787
+ GCC_except_table10899
+ GCC_except_table10915
+ GCC_except_table10961
+ GCC_except_table11203
+ GCC_except_table11230
+ GCC_except_table11245
+ GCC_except_table11305
+ GCC_except_table11449
+ GCC_except_table11530
+ GCC_except_table11536
+ GCC_except_table11539
+ GCC_except_table11545
+ GCC_except_table11548
+ GCC_except_table11551
+ GCC_except_table11558
+ GCC_except_table11567
+ GCC_except_table11579
+ GCC_except_table11582
+ GCC_except_table11585
+ GCC_except_table11588
+ GCC_except_table11591
+ GCC_except_table11594
+ GCC_except_table11597
+ GCC_except_table11600
+ GCC_except_table11603
+ GCC_except_table11606
+ GCC_except_table11609
+ GCC_except_table11612
+ GCC_except_table11615
+ GCC_except_table11720
+ GCC_except_table11910
+ GCC_except_table12070
+ GCC_except_table12085
+ GCC_except_table12091
+ GCC_except_table12093
+ GCC_except_table12098
+ GCC_except_table12143
+ GCC_except_table12150
+ GCC_except_table12204
+ GCC_except_table12243
+ GCC_except_table12257
+ GCC_except_table12261
+ GCC_except_table12263
+ GCC_except_table12358
+ GCC_except_table12374
+ GCC_except_table12479
+ GCC_except_table12540
+ GCC_except_table12592
+ GCC_except_table12621
+ GCC_except_table12677
+ GCC_except_table12688
+ GCC_except_table12733
+ GCC_except_table12735
+ GCC_except_table12900
+ GCC_except_table12962
+ GCC_except_table13011
+ GCC_except_table13089
+ GCC_except_table13117
+ GCC_except_table13123
+ GCC_except_table13172
+ GCC_except_table13216
+ GCC_except_table13229
+ GCC_except_table13234
+ GCC_except_table13248
+ GCC_except_table13255
+ GCC_except_table13256
+ GCC_except_table13257
+ GCC_except_table13266
+ GCC_except_table13277
+ GCC_except_table133
+ GCC_except_table13427
+ GCC_except_table13453
+ GCC_except_table13455
+ GCC_except_table13515
+ GCC_except_table1352
+ GCC_except_table13527
+ GCC_except_table13531
+ GCC_except_table136
+ GCC_except_table13767
+ GCC_except_table13835
+ GCC_except_table14110
+ GCC_except_table14151
+ GCC_except_table14280
+ GCC_except_table14383
+ GCC_except_table14388
+ GCC_except_table14397
+ GCC_except_table14400
+ GCC_except_table14465
+ GCC_except_table14494
+ GCC_except_table14505
+ GCC_except_table14507
+ GCC_except_table14520
+ GCC_except_table1459
+ GCC_except_table14637
+ GCC_except_table1464
+ GCC_except_table14775
+ GCC_except_table14796
+ GCC_except_table14807
+ GCC_except_table14821
+ GCC_except_table14824
+ GCC_except_table15064
+ GCC_except_table15160
+ GCC_except_table1649
+ GCC_except_table1651
+ GCC_except_table1653
+ GCC_except_table1724
+ GCC_except_table1738
+ GCC_except_table1743
+ GCC_except_table1745
+ GCC_except_table1747
+ GCC_except_table2017
+ GCC_except_table2096
+ GCC_except_table2190
+ GCC_except_table2406
+ GCC_except_table2609
+ GCC_except_table2639
+ GCC_except_table2715
+ GCC_except_table2756
+ GCC_except_table2867
+ GCC_except_table2881
+ GCC_except_table2949
+ GCC_except_table299
+ GCC_except_table2999
+ GCC_except_table3005
+ GCC_except_table305
+ GCC_except_table3057
+ GCC_except_table3067
+ GCC_except_table3075
+ GCC_except_table3083
+ GCC_except_table3111
+ GCC_except_table3154
+ GCC_except_table319
+ GCC_except_table328
+ GCC_except_table3456
+ GCC_except_table3509
+ GCC_except_table3514
+ GCC_except_table3547
+ GCC_except_table3565
+ GCC_except_table3569
+ GCC_except_table3631
+ GCC_except_table3642
+ GCC_except_table3644
+ GCC_except_table3647
+ GCC_except_table3749
+ GCC_except_table3757
+ GCC_except_table3761
+ GCC_except_table3763
+ GCC_except_table3767
+ GCC_except_table3768
+ GCC_except_table3907
+ GCC_except_table4033
+ GCC_except_table4037
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table4416
+ GCC_except_table4529
+ GCC_except_table4618
+ GCC_except_table4632
+ GCC_except_table4651
+ GCC_except_table4659
+ GCC_except_table4809
+ GCC_except_table5012
+ GCC_except_table5018
+ GCC_except_table5024
+ GCC_except_table5075
+ GCC_except_table5089
+ GCC_except_table5151
+ GCC_except_table5222
+ GCC_except_table5249
+ GCC_except_table5255
+ GCC_except_table526
+ GCC_except_table5299
+ GCC_except_table5360
+ GCC_except_table5369
+ GCC_except_table5430
+ GCC_except_table5487
+ GCC_except_table5492
+ GCC_except_table5494
+ GCC_except_table5606
+ GCC_except_table5689
+ GCC_except_table5692
+ GCC_except_table5698
+ GCC_except_table5703
+ GCC_except_table5708
+ GCC_except_table5710
+ GCC_except_table5712
+ GCC_except_table5716
+ GCC_except_table5718
+ GCC_except_table5722
+ GCC_except_table5726
+ GCC_except_table5982
+ GCC_except_table613
+ GCC_except_table6132
+ GCC_except_table6165
+ GCC_except_table6241
+ GCC_except_table6253
+ GCC_except_table6366
+ GCC_except_table6445
+ GCC_except_table6511
+ GCC_except_table6512
+ GCC_except_table6513
+ GCC_except_table6613
+ GCC_except_table6680
+ GCC_except_table6923
+ GCC_except_table6924
+ GCC_except_table6925
+ GCC_except_table6926
+ GCC_except_table6927
+ GCC_except_table7082
+ GCC_except_table709
+ GCC_except_table7133
+ GCC_except_table7137
+ GCC_except_table7138
+ GCC_except_table7147
+ GCC_except_table7152
+ GCC_except_table7157
+ GCC_except_table7158
+ GCC_except_table7162
+ GCC_except_table7202
+ GCC_except_table7207
+ GCC_except_table7265
+ GCC_except_table7276
+ GCC_except_table7339
+ GCC_except_table7340
+ GCC_except_table739
+ GCC_except_table742
+ GCC_except_table744
+ GCC_except_table746
+ GCC_except_table750
+ GCC_except_table7549
+ GCC_except_table7559
+ GCC_except_table7636
+ GCC_except_table7646
+ GCC_except_table7929
+ GCC_except_table7976
+ GCC_except_table7977
+ GCC_except_table8015
+ GCC_except_table8071
+ GCC_except_table8139
+ GCC_except_table8278
+ GCC_except_table8289
+ GCC_except_table8408
+ GCC_except_table8417
+ GCC_except_table8429
+ GCC_except_table8487
+ GCC_except_table8498
+ GCC_except_table8500
+ GCC_except_table8502
+ GCC_except_table8503
+ GCC_except_table9024
+ GCC_except_table9065
+ GCC_except_table9070
+ GCC_except_table9074
+ GCC_except_table9076
+ GCC_except_table9078
+ GCC_except_table9080
+ GCC_except_table909
+ GCC_except_table9109
+ GCC_except_table9247
+ GCC_except_table9299
+ GCC_except_table9503
+ GCC_except_table9509
+ GCC_except_table9514
+ GCC_except_table9518
+ GCC_except_table9520
+ GCC_except_table9522
+ GCC_except_table9530
+ GCC_except_table9542
+ GCC_except_table9546
+ GCC_except_table9559
+ GCC_except_table9572
+ GCC_except_table9578
+ GCC_except_table9586
+ GCC_except_table9633
+ GCC_except_table9639
+ GCC_except_table9645
+ GCC_except_table9683
+ GCC_except_table9692
+ GCC_except_table9790
+ GCC_except_table9849
+ GCC_except_table9878
+ GCC_except_table9880
+ GCC_except_table9886
+ GCC_except_table9888
+ GCC_except_table9890
+ GCC_except_table9897
+ GCC_except_table9918
+ GCC_except_table9919
+ GCC_except_table9920
+ GCC_except_table9922
+ GCC_except_table9927
+ GCC_except_table994
+ OBJC_IVAR_$_WFAction._extendedOperations
+ OBJC_IVAR_$_WFAction._extendedOperationsLock
+ OBJC_IVAR_$_WFLinkAction._donationOperation
+ OBJC_IVAR_$_WFManualExtendedOperation._completionHandlers
+ OBJC_IVAR_$_WFManualExtendedOperation._lock
+ OBJC_IVAR_$_WFManualExtendedOperation._running
+ OBJC_IVAR_$_WFParameter._localizedStringCacheLock
+ OBJC_IVAR_$_WFWalletTransactionProvider._timeoutInterval
+ _LNActionConfigurationContextWidgetFamilySystemExtraLargePortrait
+ _OBJC_CLASS_$_LNEntityQueryRequestType
+ _OBJC_CLASS_$_WFLinkPhotosFindAlbumAction
+ _OBJC_CLASS_$_WFManualExtendedOperation
+ _OBJC_CLASS_$_WFPhotoAlbumLibraryFiltering
+ _OBJC_CLASS_$_WFShortcutValidator
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
+ __84+[WFLinkEntityContentItem runQuery:withItems:permissionRequestor:completionHandler:]_block_invoke
+ __CLASS_METHODS_WFShortcutValidator
+ __DATA_WFShortcutValidator
+ __INSTANCE_METHODS_WFShortcutValidator
+ __METACLASS_DATA_WFShortcutValidator
+ __OBJC_$_INSTANCE_METHODS_WFLinkPhotosFindAlbumAction
+ __OBJC_$_INSTANCE_METHODS_WFManualExtendedOperation
+ __OBJC_$_INSTANCE_VARIABLES_WFManualExtendedOperation
+ __OBJC_$_PROP_LIST_WFManualExtendedOperation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WFActionExtendedOperation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WFActionExtendedOperation
+ __OBJC_$_PROTOCOL_REFS_WFActionExtendedOperation
+ __OBJC_CLASS_PROTOCOLS_$_WFManualExtendedOperation
+ __OBJC_CLASS_RO_$_WFLinkPhotosFindAlbumAction
+ __OBJC_CLASS_RO_$_WFManualExtendedOperation
+ __OBJC_LABEL_PROTOCOL_$_WFActionExtendedOperation
+ __OBJC_METACLASS_RO_$_WFLinkPhotosFindAlbumAction
+ __OBJC_METACLASS_RO_$_WFManualExtendedOperation
+ __OBJC_PROTOCOL_$_WFActionExtendedOperation
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
+ ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s_e57_"WFContentPropertyBuilder"24?0"LNPropertyMetadata"8Q16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e35_v16?0"WFStepwiseExecutionResult"8l
+ ___swift_memcpy256_8
+ __getPHAssetCollectionClass_block_invoke
+ __swift_closure_destructor.139Tm
+ __swift_closure_destructor.161Tm
+ __swift_exist.box.addr_destructor.198Tm
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
- GCC_except_table10017
- GCC_except_table10187
- GCC_except_table10193
- GCC_except_table10212
- GCC_except_table1030
- GCC_except_table10377
- GCC_except_table10412
- GCC_except_table10445
- GCC_except_table10447
- GCC_except_table10472
- GCC_except_table10479
- GCC_except_table10481
- GCC_except_table10483
- GCC_except_table10525
- GCC_except_table10530
- GCC_except_table10570
- GCC_except_table10573
- GCC_except_table10576
- GCC_except_table10579
- GCC_except_table10768
- GCC_except_table10880
- GCC_except_table10896
- GCC_except_table10942
- GCC_except_table11184
- GCC_except_table11211
- GCC_except_table11226
- GCC_except_table11286
- GCC_except_table11429
- GCC_except_table11510
- GCC_except_table11516
- GCC_except_table11519
- GCC_except_table11522
- GCC_except_table11525
- GCC_except_table11528
- GCC_except_table11531
- GCC_except_table11534
- GCC_except_table11538
- GCC_except_table11547
- GCC_except_table11559
- GCC_except_table11565
- GCC_except_table11568
- GCC_except_table11571
- GCC_except_table11577
- GCC_except_table11580
- GCC_except_table11583
- GCC_except_table11586
- GCC_except_table11589
- GCC_except_table11592
- GCC_except_table11595
- GCC_except_table11700
- GCC_except_table11890
- GCC_except_table12050
- GCC_except_table12065
- GCC_except_table12071
- GCC_except_table12073
- GCC_except_table12078
- GCC_except_table12110
- GCC_except_table12123
- GCC_except_table12185
- GCC_except_table12224
- GCC_except_table12238
- GCC_except_table12240
- GCC_except_table12242
- GCC_except_table12333
- GCC_except_table12349
- GCC_except_table124
- GCC_except_table12454
- GCC_except_table12515
- GCC_except_table12567
- GCC_except_table12596
- GCC_except_table12652
- GCC_except_table12663
- GCC_except_table12708
- GCC_except_table12710
- GCC_except_table12875
- GCC_except_table12937
- GCC_except_table12986
- GCC_except_table13064
- GCC_except_table13092
- GCC_except_table13098
- GCC_except_table13147
- GCC_except_table13191
- GCC_except_table13204
- GCC_except_table13209
- GCC_except_table13223
- GCC_except_table13230
- GCC_except_table13231
- GCC_except_table13232
- GCC_except_table13241
- GCC_except_table13252
- GCC_except_table13402
- GCC_except_table13426
- GCC_except_table13428
- GCC_except_table1344
- GCC_except_table13488
- GCC_except_table13500
- GCC_except_table13504
- GCC_except_table13740
- GCC_except_table13808
- GCC_except_table14083
- GCC_except_table14124
- GCC_except_table14253
- GCC_except_table14356
- GCC_except_table14361
- GCC_except_table14370
- GCC_except_table14373
- GCC_except_table14438
- GCC_except_table14467
- GCC_except_table14478
- GCC_except_table14480
- GCC_except_table14493
- GCC_except_table1451
- GCC_except_table1456
- GCC_except_table14610
- GCC_except_table14748
- GCC_except_table14769
- GCC_except_table14780
- GCC_except_table14794
- GCC_except_table14797
- GCC_except_table15010
- GCC_except_table15132
- GCC_except_table1637
- GCC_except_table1641
- GCC_except_table1643
- GCC_except_table1716
- GCC_except_table1730
- GCC_except_table1735
- GCC_except_table1737
- GCC_except_table1739
- GCC_except_table2009
- GCC_except_table2088
- GCC_except_table2180
- GCC_except_table2397
- GCC_except_table2600
- GCC_except_table2630
- GCC_except_table2703
- GCC_except_table2739
- GCC_except_table2847
- GCC_except_table2850
- GCC_except_table290
- GCC_except_table2932
- GCC_except_table296
- GCC_except_table2965
- GCC_except_table2988
- GCC_except_table3040
- GCC_except_table3050
- GCC_except_table3058
- GCC_except_table3066
- GCC_except_table309
- GCC_except_table3094
- GCC_except_table3137
- GCC_except_table318
- GCC_except_table3439
- GCC_except_table3492
- GCC_except_table3497
- GCC_except_table3530
- GCC_except_table3548
- GCC_except_table3552
- GCC_except_table3614
- GCC_except_table3625
- GCC_except_table3627
- GCC_except_table3630
- GCC_except_table3732
- GCC_except_table3740
- GCC_except_table3744
- GCC_except_table3746
- GCC_except_table3750
- GCC_except_table3751
- GCC_except_table3890
- GCC_except_table4016
- GCC_except_table4020
- GCC_except_table414
- GCC_except_table417
- GCC_except_table4399
- GCC_except_table4512
- GCC_except_table4600
- GCC_except_table4614
- GCC_except_table4633
- GCC_except_table4641
- GCC_except_table4791
- GCC_except_table4994
- GCC_except_table5000
- GCC_except_table5006
- GCC_except_table5057
- GCC_except_table5071
- GCC_except_table5133
- GCC_except_table516
- GCC_except_table5204
- GCC_except_table5231
- GCC_except_table5237
- GCC_except_table5281
- GCC_except_table5342
- GCC_except_table5351
- GCC_except_table5412
- GCC_except_table5469
- GCC_except_table5474
- GCC_except_table5476
- GCC_except_table5588
- GCC_except_table5669
- GCC_except_table5672
- GCC_except_table5675
- GCC_except_table5678
- GCC_except_table5681
- GCC_except_table5684
- GCC_except_table5688
- GCC_except_table5691
- GCC_except_table5693
- GCC_except_table5699
- GCC_except_table5709
- GCC_except_table5965
- GCC_except_table603
- GCC_except_table6115
- GCC_except_table6148
- GCC_except_table6224
- GCC_except_table6236
- GCC_except_table6349
- GCC_except_table6427
- GCC_except_table6493
- GCC_except_table6494
- GCC_except_table6495
- GCC_except_table6595
- GCC_except_table6644
- GCC_except_table6683
- GCC_except_table6906
- GCC_except_table6907
- GCC_except_table6908
- GCC_except_table6909
- GCC_except_table6910
- GCC_except_table699
- GCC_except_table7065
- GCC_except_table7116
- GCC_except_table7120
- GCC_except_table7121
- GCC_except_table7124
- GCC_except_table7130
- GCC_except_table7135
- GCC_except_table7140
- GCC_except_table7145
- GCC_except_table7185
- GCC_except_table7190
- GCC_except_table7248
- GCC_except_table7259
- GCC_except_table729
- GCC_except_table732
- GCC_except_table7322
- GCC_except_table7323
- GCC_except_table734
- GCC_except_table736
- GCC_except_table740
- GCC_except_table7532
- GCC_except_table7542
- GCC_except_table7619
- GCC_except_table7629
- GCC_except_table7912
- GCC_except_table7959
- GCC_except_table7960
- GCC_except_table7997
- GCC_except_table8053
- GCC_except_table8121
- GCC_except_table8260
- GCC_except_table8271
- GCC_except_table8390
- GCC_except_table8399
- GCC_except_table8411
- GCC_except_table8469
- GCC_except_table8480
- GCC_except_table8482
- GCC_except_table8484
- GCC_except_table8485
- GCC_except_table898
- GCC_except_table9006
- GCC_except_table9047
- GCC_except_table9052
- GCC_except_table9056
- GCC_except_table9058
- GCC_except_table9060
- GCC_except_table9062
- GCC_except_table9091
- GCC_except_table9229
- GCC_except_table9281
- GCC_except_table9485
- GCC_except_table9491
- GCC_except_table9496
- GCC_except_table9500
- GCC_except_table9502
- GCC_except_table9504
- GCC_except_table9506
- GCC_except_table9510
- GCC_except_table9512
- GCC_except_table9541
- GCC_except_table9554
- GCC_except_table9560
- GCC_except_table9568
- GCC_except_table9615
- GCC_except_table9621
- GCC_except_table9627
- GCC_except_table9665
- GCC_except_table9674
- GCC_except_table9772
- GCC_except_table9831
- GCC_except_table984
- GCC_except_table9860
- GCC_except_table9862
- GCC_except_table9868
- GCC_except_table9870
- GCC_except_table9872
- GCC_except_table9879
- GCC_except_table9900
- GCC_except_table9901
- GCC_except_table9902
- GCC_except_table9904
- GCC_except_table9909
- GCC_except_table997
- OBJC_IVAR_$_WFAction._extendedOperation
- _WFSerializedRepresentationFromWFINObject
- _WFShortcutSourceAddToSiri
- _WFShortcutSourceAutomatorMigration
- _WFShortcutSourceDescribeAShortcut
- _WFShortcutSourceEditorDocumentMenu
- _WFShortcutSourceSiriTopLevelShortcut
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48s_e57_"WFContentPropertyBuilder"24?0"LNPropertyMetadata"8Q16l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e35_v16?0"WFStepwiseExecutionResult"8l
- ___swift_memcpy248_8
- __swift_closure_destructor.106Tm
- __swift_closure_destructor.128Tm
- __swift_exist.box.addr_destructor.195Tm
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
+ "\xf0\xf0A"
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
- "\xf0\xf01"
```
