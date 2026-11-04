## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-259.0.0.0.0
-  __TEXT.__text: 0xa9f48
-  __TEXT.__objc_methlist: 0x6604
-  __TEXT.__const: 0x4238
-  __TEXT.__gcc_except_tab: 0x1640
-  __TEXT.__cstring: 0x9387
-  __TEXT.__oslogstring: 0x5460
+259.2.0.2.0
+  __TEXT.__text: 0xb1d2c
+  __TEXT.__objc_methlist: 0x6a64
+  __TEXT.__const: 0x4598
+  __TEXT.__gcc_except_tab: 0x16e8
+  __TEXT.__cstring: 0xa007
+  __TEXT.__oslogstring: 0x5792
   __TEXT.__dlopen_cstrs: 0x3d8
-  __TEXT.__swift5_typeref: 0xf73
-  __TEXT.__constg_swiftt: 0x1848
-  __TEXT.__swift5_reflstr: 0x1494
-  __TEXT.__swift5_fieldmd: 0x1be4
-  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_typeref: 0x1025
+  __TEXT.__constg_swiftt: 0x199c
+  __TEXT.__swift5_reflstr: 0x16ed
+  __TEXT.__swift5_fieldmd: 0x1da4
+  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x68
-  __TEXT.__swift5_proto: 0x254
-  __TEXT.__swift5_types: 0x1f8
+  __TEXT.__swift5_proto: 0x26c
+  __TEXT.__swift5_types: 0x210
   __TEXT.__swift5_capture: 0x230
-  __TEXT.__swift5_mpenum: 0xd8
-  __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x3f30
-  __TEXT.__eh_frame: 0x2d18
+  __TEXT.__swift5_mpenum: 0x100
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__unwind_info: 0x4170
+  __TEXT.__eh_frame: 0x2fc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c08
-  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__const: 0x1cd0
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3230
+  __DATA_CONST.__objc_selrefs: 0x33e0
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x6e0
-  __AUTH_CONST.__const: 0x4010
-  __AUTH_CONST.__cfstring: 0x5b80
-  __AUTH_CONST.__objc_const: 0x12290
+  __DATA_CONST.__got: 0x710
+  __AUTH_CONST.__const: 0x43b8
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0x13120
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xd78
-  __AUTH.__objc_data: 0x1b8
-  __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x66c
-  __DATA.__data: 0x1a88
+  __AUTH_CONST.__auth_got: 0xd90
+  __AUTH.__objc_data: 0x398
+  __AUTH.__data: 0x268
+  __DATA.__objc_ivar: 0x6e0
+  __DATA.__data: 0x1b50
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x2910
-  __DATA_DIRTY.__data: 0x1a50
+  __DATA_DIRTY.__data: 0x1a90
   __DATA_DIRTY.__bss: 0x658
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4713
-  Symbols:   5100
-  CStrings:  1327
+  Functions: 4919
+  Symbols:   5302
+  CStrings:  1402
 
Symbols:
+ +[CCDatabaseItemFieldIndexer descriptorAllowList:allowsDescriptors:]
+ +[CCDatabaseItemFieldIndexer fieldTypeForIndexedFieldType:inConfiguration:]
+ +[CCDatabaseItemFieldIndexer indexerForPredicate:contentIndexer:metaContentIndexer:error:]
+ +[CCDatabaseItemFieldIndexer indexerFromConfiguration:forBlobTable:descriptors:itemType:]
+ +[CCDatabaseItemFieldIndexer validatePredicate:againstConfiguration:descriptors:itemType:error:]
+ +[CCDerivationPropagationSummary supportsSecureCoding]
+ +[CCDerivationReconciliationSummary supportsSecureCoding]
+ +[CCItemFieldPredicate _predicateWithCompoundOperator:subPredicates:error:]
+ +[CCItemFieldPredicate predicateWithAndSubPredicates:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:betweenNumberValue:andNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:equalsAnyOfNumberValues:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:equalsAnyOfStringValues:error:]
+ +[CCItemFieldPredicate predicateWithNotSubPredicate:error:]
+ +[CCItemFieldPredicate predicateWithOrSubPredicates:error:]
+ +[CCSQLCommandCriterion criterionWithColumnName:onTable:LESSTHANColumnValue:]
+ +[CCSetConfiguration allSetConfigurations]
+ +[CCSetConfiguration derivationSourceSetConfigurations]
+ +[CCSetConfiguration partitionConfigurationForItemType:descriptors:error:]
+ +[CCSetDonation donationWithName:itemType:descriptors:service:serviceOptions:errorCode:priors:]
+ +[CCSetStoreAdminXPCClient propagateDerivationFromSet:clientId:attribution:error:]
+ +[CCSetStoreAdminXPCClient reconcileDerivationOnAllSets:clientId:shouldDeferBlock:error:]
+ -[CCDatabaseItemRetriever _criterionForPredicate:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:writtenBeforeMicros:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingPredicate:writtenBeforeMicros:resumeFromWrittenDate:outMaxWrittenDateSeen:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:writtenBeforeMicros:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithSourceItemIdentifier:writtenBeforeMicros:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWrittenBeforeMicros:resumeFromWrittenDate:outMaxWrittenDateSeen:error:usingBlock:]
+ -[CCDatabaseItemRetriever _selectForEnumeratingSourceItemIdHashesMatchingPredicate:writtenBeforeMicros:error:]
+ -[CCDatabaseItemRetriever enumerateSourceItemIdHashesMatchingPredicate:writtenBeforeMicros:error:usingBlock:]
+ -[CCDatabaseItemRetriever enumerateSourceItemIdHashesMatchingPredicate:writtenBeforeMicros:resumeFromWrittenDate:outMaxWrittenDateSeen:error:usingBlock:]
+ -[CCDatabaseWriter enumerateUnwrittenLocalInstancesMatchingPredicate:resumeFromWrittenDate:outMaxWrittenDateSeen:error:usingBlock:]
+ -[CCDatabaseWriter validateItemFieldPredicate:error:]
+ -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:scanSummary:error:]
+ -[CCDatabaseWriter(CorruptionRecovery) _checkLocalSequenceCounterRegressionForKey:scanSummary:deletionAllowed:outCorruptionDetected:error:]
+ -[CCDerivationPropagationSummary copyWithZone:]
+ -[CCDerivationPropagationSummary description]
+ -[CCDerivationPropagationSummary encodeWithCoder:]
+ -[CCDerivationPropagationSummary failedPartitionCount]
+ -[CCDerivationPropagationSummary initWithCoder:]
+ -[CCDerivationPropagationSummary initWithVisitedPartitionCount:refusedLivePrimaryCount:skippedProtectionClassCount:failedPartitionCount:]
+ -[CCDerivationPropagationSummary isComplete]
+ -[CCDerivationPropagationSummary refusedLivePrimaryCount]
+ -[CCDerivationPropagationSummary skippedProtectionClassCount]
+ -[CCDerivationPropagationSummary visitedPartitionCount]
+ -[CCDerivationReconciliationSummary completedPartitionCount]
+ -[CCDerivationReconciliationSummary copyWithZone:]
+ -[CCDerivationReconciliationSummary deferred]
+ -[CCDerivationReconciliationSummary description]
+ -[CCDerivationReconciliationSummary encodeWithCoder:]
+ -[CCDerivationReconciliationSummary failedPartitionCount]
+ -[CCDerivationReconciliationSummary initWithCoder:]
+ -[CCDerivationReconciliationSummary initWithScannedItemCount:missingPrimaryCount:completedPartitionCount:failedPartitionCount:deferred:]
+ -[CCDerivationReconciliationSummary isComplete]
+ -[CCDerivationReconciliationSummary missingPrimaryCount]
+ -[CCDerivationReconciliationSummary scannedItemCount]
+ -[CCDonationXPCClient endSetDonationWithOptions:fullSetPredicate:revisionToken:reply:]
+ -[CCIncrementalSetDonation designateAsFullSetForItemsMatchingPredicate:error:]
+ -[CCItemFieldPredicate subPredicates]
+ -[CCProvenanceScanSummary duplicateSequenceCount]
+ -[CCProvenanceScanSummary firstDuplicateSequence]
+ -[CCProvenanceScanSummary highestSequenceNumber]
+ -[CCProvenanceScanSummary initWithHighestSequenceNumber:scanComplete:duplicateSequenceCount:firstDuplicateSequence:scannedRowCount:]
+ -[CCProvenanceScanSummary scanComplete]
+ -[CCProvenanceScanSummary scannedRowCount]
+ -[CCProvenanceStateSets duplicateSequenceCount]
+ -[CCProvenanceStateSets firstDuplicateSequence]
+ -[CCProvenanceStateSets initWithEligibleSequences:compactedSequences:ineligibleRowCount:highestSequenceNumber:scanComplete:duplicateSequenceCount:firstDuplicateSequence:scannedRowCount:]
+ -[CCProvenanceStateSets scannedRowCount]
+ -[CCSet keyPrefixedSourceItemIdentifierForSourceItemIdentifierHash:]
+ -[CCSetDerivationConfiguration .cxx_destruct]
+ -[CCSetDerivationConfiguration copyWithZone:]
+ -[CCSetDerivationConfiguration description]
+ -[CCSetDerivationConfiguration hash]
+ -[CCSetDerivationConfiguration initWithMode:sources:]
+ -[CCSetDerivationConfiguration isEqual:]
+ -[CCSetDerivationConfiguration mode]
+ -[CCSetDerivationConfiguration sources]
+ -[CCSetDerivationDependent .cxx_destruct]
+ -[CCSetDerivationDependent copyWithZone:]
+ -[CCSetDerivationDependent description]
+ -[CCSetDerivationDependent descriptors]
+ -[CCSetDerivationDependent hash]
+ -[CCSetDerivationDependent initWithSetIdentifier:descriptors:mode:]
+ -[CCSetDerivationDependent isEqual:]
+ -[CCSetDerivationDependent mode]
+ -[CCSetDerivationDependent setIdentifier]
+ -[CCSetDerivationSource .cxx_destruct]
+ -[CCSetDerivationSource copyWithZone:]
+ -[CCSetDerivationSource description]
+ -[CCSetDerivationSource descriptors]
+ -[CCSetDerivationSource hash]
+ -[CCSetDerivationSource initWithSetIdentifier:descriptors:]
+ -[CCSetDerivationSource isEqual:]
+ -[CCSetDerivationSource setIdentifier]
+ -[CCSetDonation _designateAsFullSetForItemsMatchingPredicate:error:]
+ -[CCSetDonation initWithName:itemType:descriptors:service:serviceOptions:errorCode:priors:flushThreshold:]
+ -[CCSetPartitionConfiguration derivationAttributionFrame]
+ -[CCSetPartitionConfiguration derivationConfiguration]
+ -[CCSetPartitionConfiguration derivationReferenceFieldType]
+ -[CCSetPartitionConfiguration derivedByPartitions]
+ -[CCSetPartitionConfiguration initWithConfiguredDescriptors:syncPolicy:indexedFields:dataProtectionClass:releaseToken:customTombstoneTTL:compressionType:derivationConfiguration:derivedByPartitions:derivationAttributionFrame:]
+ -[CCSetStoreAdminXPCClient initWithClientId:useCase:shouldDeferBlock:]
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table70
+ GCC_except_table79
+ _BMUseCaseCascadeDerivation
+ _CCSetStoreAdminServiceRegisterDerivationClasses
+ _OBJC_CLASS_$_CCDerivationPropagationSummary
+ _OBJC_CLASS_$_CCDerivationReconciliationSummary
+ _OBJC_CLASS_$_CCProvenanceScanSummary
+ _OBJC_CLASS_$_CCSetDerivationConfiguration
+ _OBJC_CLASS_$_CCSetDerivationDependent
+ _OBJC_CLASS_$_CCSetDerivationSource
+ _OBJC_IVAR_$_CCDerivationPropagationSummary._failedPartitionCount
+ _OBJC_IVAR_$_CCDerivationPropagationSummary._refusedLivePrimaryCount
+ _OBJC_IVAR_$_CCDerivationPropagationSummary._skippedProtectionClassCount
+ _OBJC_IVAR_$_CCDerivationPropagationSummary._visitedPartitionCount
+ _OBJC_IVAR_$_CCDerivationReconciliationSummary._completedPartitionCount
+ _OBJC_IVAR_$_CCDerivationReconciliationSummary._deferred
+ _OBJC_IVAR_$_CCDerivationReconciliationSummary._failedPartitionCount
+ _OBJC_IVAR_$_CCDerivationReconciliationSummary._missingPrimaryCount
+ _OBJC_IVAR_$_CCDerivationReconciliationSummary._scannedItemCount
+ _OBJC_IVAR_$_CCItemFieldPredicate._subPredicates
+ _OBJC_IVAR_$_CCProvenanceScanSummary._duplicateSequenceCount
+ _OBJC_IVAR_$_CCProvenanceScanSummary._firstDuplicateSequence
+ _OBJC_IVAR_$_CCProvenanceScanSummary._highestSequenceNumber
+ _OBJC_IVAR_$_CCProvenanceScanSummary._scanComplete
+ _OBJC_IVAR_$_CCProvenanceScanSummary._scannedRowCount
+ _OBJC_IVAR_$_CCProvenanceStateSets._duplicateSequenceCount
+ _OBJC_IVAR_$_CCProvenanceStateSets._firstDuplicateSequence
+ _OBJC_IVAR_$_CCProvenanceStateSets._scannedRowCount
+ _OBJC_IVAR_$_CCSetDerivationConfiguration._mode
+ _OBJC_IVAR_$_CCSetDerivationConfiguration._sources
+ _OBJC_IVAR_$_CCSetDerivationDependent._descriptors
+ _OBJC_IVAR_$_CCSetDerivationDependent._mode
+ _OBJC_IVAR_$_CCSetDerivationDependent._setIdentifier
+ _OBJC_IVAR_$_CCSetDerivationSource._descriptors
+ _OBJC_IVAR_$_CCSetDerivationSource._setIdentifier
+ _OBJC_IVAR_$_CCSetDonation._descriptors
+ _OBJC_IVAR_$_CCSetDonation._fullSetPredicate
+ _OBJC_IVAR_$_CCSetPartitionConfiguration._derivationAttributionFrame
+ _OBJC_IVAR_$_CCSetPartitionConfiguration._derivationConfiguration
+ _OBJC_IVAR_$_CCSetPartitionConfiguration._derivedByPartitions
+ _OBJC_METACLASS_$_CCDerivationPropagationSummary
+ _OBJC_METACLASS_$_CCDerivationReconciliationSummary
+ _OBJC_METACLASS_$_CCProvenanceScanSummary
+ _OBJC_METACLASS_$_CCSetDerivationConfiguration
+ _OBJC_METACLASS_$_CCSetDerivationDependent
+ _OBJC_METACLASS_$_CCSetDerivationSource
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ __DATA__TtCCO11CascadeSets9SetChange18ItemInstanceReader17RemovalEnumerator
+ __IVARS__TtCC11CascadeSets18ItemInstanceReader17RemovalEnumerator
+ __IVARS__TtCCO11CascadeSets9SetChange18ItemInstanceReader17RemovalEnumerator
+ __METACLASS_DATA__TtCCO11CascadeSets9SetChange18ItemInstanceReader17RemovalEnumerator
+ __OBJC_$_CLASS_METHODS_CCDerivationPropagationSummary
+ __OBJC_$_CLASS_METHODS_CCDerivationReconciliationSummary
+ __OBJC_$_CLASS_PROP_LIST_CCDerivationPropagationSummary
+ __OBJC_$_CLASS_PROP_LIST_CCDerivationReconciliationSummary
+ __OBJC_$_INSTANCE_METHODS_CCDerivationPropagationSummary
+ __OBJC_$_INSTANCE_METHODS_CCDerivationReconciliationSummary
+ __OBJC_$_INSTANCE_METHODS_CCProvenanceScanSummary
+ __OBJC_$_INSTANCE_METHODS_CCSetDerivationConfiguration
+ __OBJC_$_INSTANCE_METHODS_CCSetDerivationDependent
+ __OBJC_$_INSTANCE_METHODS_CCSetDerivationSource
+ __OBJC_$_INSTANCE_VARIABLES_CCDerivationPropagationSummary
+ __OBJC_$_INSTANCE_VARIABLES_CCDerivationReconciliationSummary
+ __OBJC_$_INSTANCE_VARIABLES_CCProvenanceScanSummary
+ __OBJC_$_INSTANCE_VARIABLES_CCSetDerivationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CCSetDerivationDependent
+ __OBJC_$_INSTANCE_VARIABLES_CCSetDerivationSource
+ __OBJC_$_PROP_LIST_CCDerivationPropagationSummary
+ __OBJC_$_PROP_LIST_CCDerivationReconciliationSummary
+ __OBJC_$_PROP_LIST_CCProvenanceScanSummary
+ __OBJC_$_PROP_LIST_CCSetDerivationConfiguration
+ __OBJC_$_PROP_LIST_CCSetDerivationDependent
+ __OBJC_$_PROP_LIST_CCSetDerivationSource
+ __OBJC_CLASS_PROTOCOLS_$_CCDerivationPropagationSummary
+ __OBJC_CLASS_PROTOCOLS_$_CCDerivationReconciliationSummary
+ __OBJC_CLASS_PROTOCOLS_$_CCSetDerivationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CCSetDerivationDependent
+ __OBJC_CLASS_PROTOCOLS_$_CCSetDerivationSource
+ __OBJC_CLASS_RO_$_CCDerivationPropagationSummary
+ __OBJC_CLASS_RO_$_CCDerivationReconciliationSummary
+ __OBJC_CLASS_RO_$_CCProvenanceScanSummary
+ __OBJC_CLASS_RO_$_CCSetDerivationConfiguration
+ __OBJC_CLASS_RO_$_CCSetDerivationDependent
+ __OBJC_CLASS_RO_$_CCSetDerivationSource
+ __OBJC_METACLASS_RO_$_CCDerivationPropagationSummary
+ __OBJC_METACLASS_RO_$_CCDerivationReconciliationSummary
+ __OBJC_METACLASS_RO_$_CCProvenanceScanSummary
+ __OBJC_METACLASS_RO_$_CCSetDerivationConfiguration
+ __OBJC_METACLASS_RO_$_CCSetDerivationDependent
+ __OBJC_METACLASS_RO_$_CCSetDerivationSource
+ ___122-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:writtenBeforeMicros:error:usingBlock:]_block_invoke
+ ___130-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:writtenBeforeMicros:error:usingBlock:]_block_invoke
+ ___136-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWrittenBeforeMicros:resumeFromWrittenDate:outMaxWrittenDateSeen:error:usingBlock:]_block_invoke
+ ___136-[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:scanSummary:error:]_block_invoke
+ ___53-[CCDatabaseWriter validateItemFieldPredicate:error:]_block_invoke
+ ___82+[CCSetStoreAdminXPCClient propagateDerivationFromSet:clientId:attribution:error:]_block_invoke
+ ___82+[CCSetStoreAdminXPCClient propagateDerivationFromSet:clientId:attribution:error:]_block_invoke_2
+ ___86-[CCDonationXPCClient endSetDonationWithOptions:fullSetPredicate:revisionToken:reply:]_block_invoke
+ ___89+[CCDatabaseItemFieldIndexer indexerFromConfiguration:forBlobTable:descriptors:itemType:]_block_invoke
+ ___89+[CCSetStoreAdminXPCClient reconcileDerivationOnAllSets:clientId:shouldDeferBlock:error:]_block_invoke
+ ___89+[CCSetStoreAdminXPCClient reconcileDerivationOnAllSets:clientId:shouldDeferBlock:error:]_block_invoke_2
+ ___block_descriptor_137_e8_32s40s48s56s64s72bs80r88r96r104r112r120r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r80l8s72l8r88l8r96l8s48l8r104l8r112l8s56l8s64l8r120l8
+ ___block_descriptor_32_e22_v24?0"NSNumber"8^B16l
+ ___block_descriptor_48_e8_32r40r_e52_v24?0"CCDerivationPropagationSummary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e55_v24?0"CCDerivationReconciliationSummary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e21_v16?0"CCItemField"8ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_76_e8_32s40s48s56r64r_e48_v28?0C8"NSError"12"CCDonationServicePriors"20ls32l8r56l8r64l8s40l8s48l8
+ ___swift_exist.box.addr_destructor.124Tm
+ ___swift_exist.box.addr_destructor.133Tm
+ ___unnamed_10
+ ___unnamed_24
+ ___unnamed_26
+ ___unnamed_27
+ _associated conformance 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV10Foundation09LocalizedG0AAs0G0
+ _get_enum_tag_for_layout_string 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV9ViolationO
+ _symbolic $s11CascadeSets21ItemInstanceRowSourceP
+ _symbolic Si10clockLimit_Si11bucketCountt
+ _symbolic SiSg16persistedCounter_Si9highWatert
+ _symbolic SiSgSg
+ _symbolic _____ 11CascadeSets18ItemInstanceReaderC17RemovalEnumeratorC
+ _symbolic _____ 11CascadeSets9SetChangeO010SharedItemD8ProviderC10StatementsC30MetaContentClockLimitStatementV
+ _symbolic _____ 11CascadeSets9SetChangeO18ItemInstanceReaderC17RemovalEnumeratorC
+ _symbolic _____ 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV
+ _symbolic _____ 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV11BucketStateV
+ _symbolic _____ 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV9ViolationO
+ _symbolic _____Sg 11CascadeSets9SetChangeO010SharedItemD8ProviderC10StatementsC30MetaContentClockLimitStatementV
+ _symbolic _____Sg 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV
+ _type_layout_string 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV
+ _type_layout_string 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV11BucketStateV
+ _type_layout_string 11CascadeSets9SetChangeO25ProvenanceCorruptionErrorV9ViolationO
- +[CCDatabaseItemFieldIndexer descriptorAllowList:allowsSet:]
- +[CCSetDonation donationWithName:itemType:service:serviceOptions:errorCode:priors:]
- -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:error:usingBlock:]
- -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:]
- -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:error:usingBlock:]
- -[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithSourceItemIdentifier:error:usingBlock:]
- -[CCDatabaseItemRetriever _selectForEnumeratingSourceItemIdHashesMatchingPredicate:error:]
- -[CCDatabaseWriter enumerateUnwrittenLocalInstancesWithError:usingBlock:]
- -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:error:]
- -[CCDatabaseWriter(CorruptionRecovery) _checkLocalSequenceCounterRegressionForKey:derivedHighWater:outCorruptionDetected:error:]
- -[CCDonationXPCClient endSetDonationWithOptions:revisionToken:reply:]
- -[CCProvenanceStateSets hasDuplicateSequenceNumbers]
- -[CCProvenanceStateSets initWithEligibleSequences:compactedSequences:ineligibleRowCount:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:]
- -[CCSetDonation initWithName:itemType:service:serviceOptions:errorCode:priors:flushThreshold:]
- GCC_except_table35
- GCC_except_table43
- GCC_except_table47
- GCC_except_table54
- GCC_except_table58
- GCC_except_table71
- GCC_except_table77
- _OBJC_IVAR_$_CCProvenanceStateSets._hasDuplicateSequenceNumbers
- __OBJC_$_PROTOCOL_CLASS_METHODS_CCSetConfigurationProtocol
- ___102-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke
- ___110-[CCDatabaseItemRetriever _enumerateSourceItemIdHashesWithItemIdentifier:itemIdentifierType:error:usingBlock:]_block_invoke
- ___187-[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:error:]_block_invoke
- ___69-[CCDonationXPCClient endSetDonationWithOptions:revisionToken:reply:]_block_invoke
- ___72+[CCDatabaseItemFieldIndexer indexerFromConfiguration:forBlobTable:set:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64s72bs80r88r96r104r112r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r80l8s72l8r88l8r96l8s48l8r104l8s56l8s64l8r112l8
- ___block_descriptor_56_e8_32s40s48r_e21_v16?0"CCItemField"8ls32l8s40l8r48l8
- ___block_descriptor_68_e8_32s40s48r56r_e48_v28?0C8"NSError"12"CCDonationServicePriors"20ls32l8r48l8r56l8s40l8
- ___swift_exist.box.addr_destructor.113Tm
- ___swift_exist.box.addr_destructor.122Tm
- ___unnamed_23
- ___unnamed_25
- ___unnamed_8
- _os_variant_allows_internal_security_policies
CStrings:
+ " (absent)"
+ " (rdar://181541573)"
+ " are uncounted, enumerating from the table (rdar://181440946)"
+ " beyond clock limit "
+ " bookmarkWrittenSeqNum="
+ " currentDevice=none"
+ " currentDeviceRowId="
+ " hasBookmarkData="
+ " is behind the metacontent_provenance "
+ " localResourceGeneration="
+ "%@:%@ (operator: %u) subPredicates: %@"
+ ") in fully covered bucket "
+ ": localHighestMetaContent "
+ "; external build keeps the set"
+ "; external build skips the run"
+ "<%@: %@ default partition>"
+ "<%@: %@ descriptors:%@ mode:%ld>"
+ "<%@: %@ descriptors:%@>"
+ "<%@: %@ mode:%ld>"
+ "<%@: %@ whole set>"
+ "<%@: mode:%ld sources:%@>"
+ "<%@: partitions:%lu refused:%lu locked:%lu failed:%lu>"
+ "<%@: scanned:%lu missingPrimaries:%lu completed:%lu failed:%lu deferred:%d>"
+ "BETWEEN predicate requires a value array of exactly two bounds: %@"
+ "CCItemFieldPredicate.m"
+ "Cascade provenance corruption in set %{public}s itemType=%{public}u protectionClass=%{public}d descriptors=%{public}ld during %{public}s: %{public}s"
+ "Cascade provenance corruption: %{public}s"
+ "Compaction: %@: no rows for claimed run %{public}@ (length %lu) in %{public}@ for device %{public}@ of set %{public}@ (%@)%{public}s. rdar://182604090."
+ "Compound"
+ "Compound predicate mixes fields indexed on different tables (%@ and %@), which is not supported: %@"
+ "Compound predicate requires at least one sub-predicate"
+ "Compound predicate requires at least one sub-predicate: %@"
+ "Compound predicates may only combine indexed-field predicates, not: %@"
+ "Derivation descriptors failed to be sorted: %@"
+ "Detected %{public}@ regression for set %{public}@ (%@): persisted %lld%{public}s is %lld below derived high-water %lld across %lu scanned rows (%lu duplicate sequence numbers)%{public}s. rdar://182750141."
+ "Donation %@ called -designateAsFullSetForItemsMatchingPredicate:error: more than once. A donation may designate at most one predicate; combine the scopes or use a separate donation."
+ "Found %lu duplicate content sequence number(s) for set %{public}@ (%@) (first %lld) among %lu scanned rows, derived high-water %lld%{public}s. rdar://182750141."
+ "Found %lu duplicate metacontent sequence number(s) for set %{public}@ (%@) (first %lld) among %lu scanned rows, derived high-water %lld%{public}s. rdar://181440946."
+ "Indexed field %hu nests more than %lu repeated levels, which cannot be addressed; its values are appended rather than aligned"
+ "NOT compound predicate requires exactly one sub-predicate: %@"
+ "Removal enumeration for %@ skipped a compacted tombstone at seqNum=%ld, written after the bookmark, because its items are unknown"
+ "SELECT clock_end FROM (\n    SELECT * FROM (\n        SELECT sequence_number + MAX(1, deleted_run_length) AS clock_end\n        FROM metacontent_provenance\n        WHERE (deleted_run_length != 0) = 0\n        ORDER BY sequence_number DESC\n        LIMIT 1\n    )\n    UNION ALL\n    SELECT * FROM (\n        SELECT sequence_number + MAX(1, deleted_run_length) AS clock_end\n        FROM metacontent_provenance\n        WHERE (deleted_run_length != 0) = 1\n        ORDER BY sequence_number DESC\n        LIMIT 1\n    )\n)\nORDER BY clock_end DESC\nLIMIT 1"
+ "Unexpected compound operator for DocumentCache translation: %@"
+ "Unexpected compound predicate operator: %ld"
+ "bookmarkWrittenSeqNum="
+ "completedPartitionCount"
+ "copyWithFieldType: is not supported on compound predicates"
+ "copyWithFieldType:value: is not supported on compound predicates"
+ "deferred"
+ "designateAsFullSetForItemsMatchingPredicate: %@"
+ "equalsAnyOfNumberValues requires at least one value"
+ "equalsAnyOfStringValues requires at least one value"
+ "failedPartitionCount"
+ "item instance enumeration"
+ "item instance enumerator creation"
+ "item instance removal enumeration"
+ "loadDbTombstoneCounts"
+ "localCounterCheck"
+ "localResourceGeneration="
+ "lowerNumberValue"
+ "markPresent"
+ "maxWrittenSeqNum="
+ "missingPrimaryCount"
+ "numberValues"
+ "numberValues element"
+ "refusedLivePrimaryCount"
+ "scannedItemCount"
+ "shared item enumeration"
+ "shared item enumerator creation"
+ "skippedProtectionClassCount"
+ "stringValues"
+ "stringValues element"
+ "subPredicate"
+ "subPredicates"
+ "subPredicates element"
+ "tombstone counts are ahead of the provenance high-water (rdar://181440946)"
+ "upperNumberValue"
+ "v24@?0@\"CCDerivationPropagationSummary\"8@\"NSError\"16"
+ "v24@?0@\"CCDerivationReconciliationSummary\"8@\"NSError\"16"
+ "visitedPartitionCount"
- "Compaction: %@: no rows for claimed run %@ in %@%{public}s. rdar://182604090."
- "Detected %{public}@ regression for set %{public}@: persisted %lld below derived high-water %lld. rdar://182750141."
- "Found duplicate content sequence number(s) for set %{public}@%{public}s. rdar://182750141."
- "Found duplicate metacontent sequence number(s) for set %{public}@%{public}s. rdar://181440946."
- "com.apple.Cascade"
```
