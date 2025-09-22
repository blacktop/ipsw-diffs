## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1441.4.100.0.0
-  __TEXT.__text: 0x1a6428
-  __TEXT.__auth_stubs: 0x3060
+1441.9.100.0.0
+  __TEXT.__text: 0x1a9730
+  __TEXT.__auth_stubs: 0x3070
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
-  __TEXT.__objc_methlist: 0xcb54
+  __TEXT.__objc_methlist: 0xccac
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x241e6
-  __TEXT.__oslogstring: 0x13114
-  __TEXT.__gcc_except_tab: 0x26918
+  __TEXT.__cstring: 0x24692
+  __TEXT.__oslogstring: 0x133f5
+  __TEXT.__gcc_except_tab: 0x26d9c
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xaea8
+  __TEXT.__unwind_info: 0xb000
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x1cc40
-  __TEXT.__objc_methtype: 0x9f57
-  __TEXT.__objc_stubs: 0x10220
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x6c00
-  __DATA_CONST.__objc_classlist: 0x698
+  __TEXT.__objc_classname: 0x1ea9
+  __TEXT.__objc_methname: 0x1cffe
+  __TEXT.__objc_methtype: 0xa6a4
+  __TEXT.__objc_stubs: 0x10300
+  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__const: 0x6c28
+  __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e18
+  __DATA_CONST.__objc_selrefs: 0x5e88
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x1850
-  __AUTH_CONST.__const: 0x3588
-  __AUTH_CONST.__cfstring: 0x16820
-  __AUTH_CONST.__objc_const: 0x12be0
+  __AUTH_CONST.__auth_got: 0x1858
+  __AUTH_CONST.__const: 0x35f0
+  __AUTH_CONST.__cfstring: 0x169a0
+  __AUTH_CONST.__objc_const: 0x12f08
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x2a80
+  __AUTH.__objc_data: 0x2b70
   __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xa6c
+  __DATA.__objc_ivar: 0xa94
   __DATA.__data: 0x1260
-  __DATA.__bss: 0xe78
+  __DATA.__bss: 0xe90
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x8c8
+  __DATA_DIRTY.__bss: 0x8c0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0FFF723A-7DE6-3705-B327-ADD82FAEF345
-  Functions: 8553
-  Symbols:   27802
-  CStrings:  13516
+  UUID: 985FB0A3-4715-3860-A6D1-8D35EE9E476E
+  Functions: 8617
+  Symbols:   27999
+  CStrings:  13599
 
Symbols:
+ +[LSApplicationRecord(Enumeration) enumeratorForApplicationsOnSameVolumeWithinDirectoryAtURL:enumerationOptions:filteringOptions:]
+ +[LSBundleURLRelationshipPrecondition supportsSecureCoding]
+ +[LSPrecondition preconditionCheckingRelationshipToURL:ofBundleWithIdentifier:placeholderFetchBehavior:requiredRelationship:]
+ -[FSNode getFSID:error:]
+ -[LSApplicationRecord(MobileInstall) _LSRecord_resolve_serializedPlaceholderURL]
+ -[LSApplicationRecord(MobileInstall) serializedPlaceholderPath]
+ -[LSApplicationRecord(MobileInstall) serializedPlaceholderURLWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord(MobileInstall) serializedPlaceholderURL]
+ -[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:].cold.2
+ -[LSApplicationWorkspace(OpenAdditions) isBundleEligibleForOpenDocumentViaOpenURL:]
+ -[LSApplicationWorkspace(OpenAdditions) isCurrentProcessEligibleForOpenDocumentViaOpenURL]
+ -[LSBundleRecordBuilder serializedPlaceholderPath]
+ -[LSBundleURLRelationshipPrecondition .cxx_destruct]
+ -[LSBundleURLRelationshipPrecondition description]
+ -[LSBundleURLRelationshipPrecondition encodeWithCoder:]
+ -[LSBundleURLRelationshipPrecondition initWithCoder:]
+ -[LSBundleURLRelationshipPrecondition initWithURL:bundleIdentifier:placeholderFetchBehavior:requiredRelationship:]
+ -[LSBundleURLRelationshipPrecondition isMet]
+ -[LSBundleURLRelationshipPrecondition isMet].cold.1
+ -[_LSApplicationRecordsWithinDirectoryEnumerator .cxx_construct]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator .cxx_destruct]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator _createPostflightedApplicationRecordWithContext:bundleUnit:bundleData:]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator _getObject:atIndex:context:]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator _preflightPathOfBundleWithContext:bundleUnit:bundleData:]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator _prepareWithContext:error:]
+ -[_LSApplicationRecordsWithinDirectoryEnumerator initWithContext:directoryURL:volumeURL:enumerationOptions:filteringOptions:]
+ -[_LSDefaults simulatorSharedResourcesDirectoryURL]
+ -[_LSDefaults simulatorSharedResourcesDirectoryURL].cold.1
+ -[_LSErrorEnumerator .cxx_destruct]
+ -[_LSErrorEnumerator initWithPreparationError:]
+ -[_LSErrorEnumerator nextObject]
+ GCC_except_table118
+ GCC_except_table149
+ GCC_except_table177
+ GCC_except_table186
+ GCC_except_table256
+ GCC_except_table268
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table300
+ GCC_except_table305
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table321
+ GCC_except_table325
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table353
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table385
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table406
+ GCC_except_table410
+ _NSURLFileIdentifierKey
+ _NSURLVolumeIdentifierKey
+ _NSURLVolumeTypeNameKey
+ _OBJC_CLASS_$_LSBundleURLRelationshipPrecondition
+ _OBJC_CLASS_$__LSApplicationRecordsWithinDirectoryEnumerator
+ _OBJC_CLASS_$__LSErrorEnumerator
+ _OBJC_IVAR_$_LSBundleRecordBuilder._serializedPlaceholderPath
+ _OBJC_IVAR_$_LSBundleURLRelationshipPrecondition._bundleIdentifier
+ _OBJC_IVAR_$_LSBundleURLRelationshipPrecondition._placeholderFetchBehavior
+ _OBJC_IVAR_$_LSBundleURLRelationshipPrecondition._requiredRelationship
+ _OBJC_IVAR_$_LSBundleURLRelationshipPrecondition._url
+ _OBJC_IVAR_$__LSApplicationRecordEnumerator._volumeContainerAdapter
+ _OBJC_IVAR_$__LSApplicationRecordsWithinDirectoryEnumerator._bundleIdentifiersOrUnits
+ _OBJC_IVAR_$__LSApplicationRecordsWithinDirectoryEnumerator._directoryURL
+ _OBJC_IVAR_$__LSApplicationRecordsWithinDirectoryEnumerator._enumerationOptions
+ _OBJC_IVAR_$__LSApplicationRecordsWithinDirectoryEnumerator._filteringOptions
+ _OBJC_IVAR_$__LSApplicationRecordsWithinDirectoryEnumerator._volumeContainerAdapter
+ _OBJC_IVAR_$__LSErrorEnumerator._error
+ _OBJC_METACLASS_$_LSBundleURLRelationshipPrecondition
+ _OBJC_METACLASS_$__LSApplicationRecordsWithinDirectoryEnumerator
+ _OBJC_METACLASS_$__LSErrorEnumerator
+ __LSNodeIsOnCryptex
+ __LSPathMatchesPath_NoIO
+ __LSServer_LSDatabaseRemoveNonexistentCryptexBundlesForReboot
+ __LSServer_URLIsOnTrustedCryptex
+ __LSServer_URLIsOnTrustedCryptex.cold.1
+ __LSServer_URLIsOnTrustedCryptex.cold.2
+ __LSServer_URLIsOnTrustedCryptex.cold.3
+ __LSVersionNumberGetDYLDVersion
+ __LSVersionNumberMakeWithDYLDVersion
+ __OBJC_$_CLASS_METHODS_LSBundleURLRelationshipPrecondition
+ __OBJC_$_INSTANCE_METHODS_LSBundleURLRelationshipPrecondition
+ __OBJC_$_INSTANCE_METHODS__LSApplicationRecordsWithinDirectoryEnumerator
+ __OBJC_$_INSTANCE_METHODS__LSErrorEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_LSBundleURLRelationshipPrecondition
+ __OBJC_$_INSTANCE_VARIABLES__LSApplicationRecordsWithinDirectoryEnumerator
+ __OBJC_$_INSTANCE_VARIABLES__LSErrorEnumerator
+ __OBJC_CLASS_RO_$_LSBundleURLRelationshipPrecondition
+ __OBJC_CLASS_RO_$__LSApplicationRecordsWithinDirectoryEnumerator
+ __OBJC_CLASS_RO_$__LSErrorEnumerator
+ __OBJC_METACLASS_RO_$_LSBundleURLRelationshipPrecondition
+ __OBJC_METACLASS_RO_$__LSApplicationRecordsWithinDirectoryEnumerator
+ __OBJC_METACLASS_RO_$__LSErrorEnumerator
+ __ZL41_LSCreateRegistrationDataForDirectoryNodeP9LSContextP18LSRegistrationInfoPK7__CFURLP17_LSBundleProviderP6FSNodePK14__CFDictionaryPPK9__CFArray.cold.4
+ __ZN14LaunchServices17BindingEvaluationL28compareVendorsAndBundleClassERNS0_5StateEbRKNS0_15ExtendedBindingES5_
+ __ZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContext
+ __ZN14LaunchServices20AppRecordEnumerationL24evaluateBundleNoIOCommonEP9LSContextjPK12LSBundleDatayj
+ __ZN14LaunchServices20AppRecordEnumerationL24evaluateBundleNoIOCommonEP9LSContextjPK12LSBundleDatayj.cold.1
+ __ZN14LaunchServices20AppRecordEnumerationL32findAppByIdentifierForEnumeratorEP9LSContextP8NSStringj13LSBundleClassjyS4_U13block_pointerFbS2_jPK12LSBundleDataEPjPS8_
+ __ZN14LaunchServices20AppRecordEnumerationL32findAppByIdentifierForEnumeratorEP9LSContextP8NSStringj13LSBundleClassjyS4_U13block_pointerFbS2_jPK12LSBundleDataEPjPS8_.cold.1
+ __ZNK14LaunchServices17BindingEvaluation5State31getDefaultAppCategoryBeingBoundEv
+ __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB8nn200100IJRNS0_5__altILm1EU8__strongP5NSURLEEEEEDcDpOT_
+ __ZNKSt3__116__variant_detail12__visitation9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EclB8nn200100IJRNS0_5__altILm2EU8__strongP7NSErrorEEEEEDcDpOT_
+ __ZNSt3__114__split_bufferINS_4pairIjU8__strongP6FSNodeEERNS_9allocatorIS5_EEED2Ev
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB8nn200100ILm1ES5_RU8__strongKS4_EEvRNS0_5__altIXT_ET0_EEOT1_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE12__assign_altB8nn200100ILm2ES8_RU8__strongKS7_EEvRNS0_5__altIXT_ET0_EEOT1_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB8nn200100IRKNS0_17__copy_assignmentIS9_LNS0_6_TraitE1EEEEEvOT_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB8nn200100ILm1EJRU8__strongKS4_EEERDaDpOT0_
+ __ZNSt3__116__variant_detail12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE9__emplaceB8nn200100ILm2EJRU8__strongKS7_EEERDaDpOT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8nn200100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8nn200100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB8nn200100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0ELm0EEE10__dispatchB8nn200100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB8nn200100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8nn200100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8nn200100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB8nn200100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1ELm1EEE10__dispatchB8nn200100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB8nn200100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8nn200100IONS1_9__variant15__value_visitorIZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_EEJRNS0_6__baseILNS0_6_TraitE1EJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcSD_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8nn200100IOZNS0_6__dtorINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEELNS0_6_TraitE1EE9__destroyB8nn200100EvEUlRT_E_JRNS0_6__baseILSF_1EJjSA_SD_EEEEEEDcSH_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2ELm2EEE10__dispatchB8nn200100IOZNS0_12__assignmentINS0_8__traitsIJjU8__strongP5NSURLU8__strongP7NSErrorEEEE16__generic_assignB8nn200100IRKNS0_17__copy_assignmentISE_LNS0_6_TraitE1EEEEEvOT_EUlRSM_OT0_E_JRNS0_6__baseILSI_1EJjSA_SD_EEERKSU_EEEDcSM_DpT0_
+ __ZNSt3__116__variant_detail12__visitation9__variant13__visit_valueB8nn200100IZN14LaunchServices20AppRecordEnumeration32VolumeContainerResolutionAdapter7resolveEP9LSContextEUlRKT_E_JRNS_7variantIJjU8__strongP5NSURLU8__strongP7NSErrorEEEEEEDcOS9_DpOT0_
+ __ZNSt3__126__throw_bad_variant_accessB8nn200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorINS_4pairIjU8__strongP6FSNodeEEEEPS6_EEvRT_T0_SB_SB_
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIjU8__strongP6FSNodeEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRjRS4_EEEPS5_DpOT_
+ __ZNSt3__19allocatorINS_4pairIjU8__strongP6FSNodeEEE17allocate_at_leastB8nn200100Em
+ ___104-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]_block_invoke.168
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.376
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.376.cold.1
+ ___51-[_LSDefaults simulatorSharedResourcesDirectoryURL]_block_invoke
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.402
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.402.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.2
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.373
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.373.cold.1
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.309
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.312
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.315
+ ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.385
+ ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.377
+ ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.760
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.380
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.381
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.382
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.249
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.254
+ ___76-[_LSApplicationRecordsWithinDirectoryEnumerator _prepareWithContext:error:]_block_invoke
+ ___76-[_LSApplicationRecordsWithinDirectoryEnumerator _prepareWithContext:error:]_block_invoke_2
+ ___77-[_LSApplicationRecordsWithinDirectoryEnumerator _getObject:atIndex:context:]_block_invoke
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.633
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.633.cold.1
+ ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.289
+ ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.397
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.319
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.319.cold.1
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.320
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.320.cold.1
+ ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.308
+ ___Block_byref_object_copy_.1015
+ ___Block_byref_object_copy_.1197
+ ___Block_byref_object_copy_.32
+ ___Block_byref_object_copy_.388
+ ___Block_byref_object_copy_.619
+ ___Block_byref_object_copy_.686
+ ___Block_byref_object_dispose_.1016
+ ___Block_byref_object_dispose_.1198
+ ___Block_byref_object_dispose_.33
+ ___Block_byref_object_dispose_.389
+ ___Block_byref_object_dispose_.620
+ ___Block_byref_object_dispose_.687
+ ____LSServer_LSDatabaseRemoveNonexistentCryptexBundlesForReboot_block_invoke
+ ____LSServer_LSDatabaseRemoveNonexistentCryptexBundlesForReboot_block_invoke.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.943
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.943.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.947.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.950
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.948
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.952
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.952.cold.1
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1017
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1018
+ ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.39
+ ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.40
+ ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.42
+ ____ZN14LaunchServices20AppRecordEnumerationL32findAppByIdentifierForEnumeratorEP9LSContextP8NSStringj13LSBundleClassjyS4_U13block_pointerFbS2_jPK12LSBundleDataEPjPS8__block_invoke
+ ___assert_rtn
+ ___block_descriptor_32_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
+ ___block_descriptor_40_ea8_32s_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e379_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_44_e379_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20l
+ ___block_descriptor_48_ea8_32bs_e376_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20ls32l8
+ ___block_descriptor_52_ea8_32s_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8
+ ___block_descriptor_56_ea8_32bs40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e19_v32?0I8r^v12I20*24lr32l8r40l8
+ ___block_descriptor_56_ea8_32r40r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8
+ ___block_descriptor_608_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_608_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
+ ___block_descriptor_68_ea8_32s40s48bs_e31_B28?0I8^I12r^^{LSBundleData}20ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32bs40r48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e366_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20ls32l8s40l8r48l8
+ ___block_literal_global.1102
+ ___block_literal_global.1125
+ ___block_literal_global.1152
+ ___block_literal_global.1154
+ ___block_literal_global.1165
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.153
+ ___block_literal_global.236
+ ___block_literal_global.262
+ ___block_literal_global.274
+ ___block_literal_global.295
+ ___block_literal_global.311
+ ___block_literal_global.314
+ ___block_literal_global.317
+ ___block_literal_global.335
+ ___block_literal_global.396
+ ___block_literal_global.404
+ ___block_literal_global.428
+ ___block_literal_global.44
+ ___block_literal_global.474
+ ___block_literal_global.477
+ ___block_literal_global.479
+ ___block_literal_global.554
+ ___block_literal_global.582
+ ___block_literal_global.59
+ ___block_literal_global.630
+ ___block_literal_global.645
+ ___block_literal_global.659
+ ___block_literal_global.676
+ ___block_literal_global.678
+ ___block_literal_global.922
+ ___block_literal_global.952
+ ___block_literal_global.97
+ ___block_literal_global.991
+ _objc_msgSend$_createPostflightedApplicationRecordWithContext:bundleUnit:bundleData:
+ _objc_msgSend$_preflightPathOfBundleWithContext:bundleUnit:bundleData:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$initWithContext:directoryURL:volumeURL:enumerationOptions:filteringOptions:
+ _objc_msgSend$initWithURL:bundleIdentifier:placeholderFetchBehavior:requiredRelationship:
+ _objc_msgSend$isBundleEligibleForOpenDocumentViaOpenURL:
+ _objc_msgSend$isCurrentProcessEligibleForOpenDocumentViaOpenURL
+ _objc_msgSend$serializedPlaceholderURL
+ _preferredLocalizations.once.251
+ _simulatorSharedResourcesDirectoryURL.onceToken
+ _simulatorSharedResourcesDirectoryURL.result
- -[LSApplicationRecord(InfoPlistRarities) serializedPlaceholderPath]
- -[_LSApplicationRecordEnumerator(Private) _applicationRecordWithContext:bundleIdentifierOrUnit:].cold.1
- -[_LSApplicationRecordEnumerator(Private) _getContainer:context:error:]
- GCC_except_table165
- GCC_except_table174
- GCC_except_table260
- GCC_except_table269
- GCC_except_table271
- GCC_except_table273
- GCC_except_table276
- GCC_except_table283
- GCC_except_table288
- GCC_except_table291
- GCC_except_table303
- GCC_except_table310
- GCC_except_table312
- GCC_except_table322
- GCC_except_table328
- GCC_except_table341
- GCC_except_table344
- GCC_except_table350
- GCC_except_table369
- GCC_except_table370
- GCC_except_table371
- GCC_except_table376
- GCC_except_table382
- GCC_except_table384
- GCC_except_table400
- GCC_except_table407
- _OBJC_IVAR_$__LSApplicationRecordEnumerator._container
- _OBJC_IVAR_$__LSApplicationRecordEnumerator._volumeURL
- _OUTLINED_FUNCTION_22
- __LSMakeDYLDVersionFromVersionNumber
- __LSMakeVersionNumberFromDYLDVersion
- __ZL24evaluateBundleNoIOCommonP9LSContextjPK12LSBundleDatayj
- __ZL24evaluateBundleNoIOCommonP9LSContextjPK12LSBundleDatayj.cold.1
- __ZN14LaunchServices17BindingEvaluationL14compareVendorsERNS0_5StateERKNS0_15ExtendedBindingES5_
- __ZN14LaunchServices17BindingEvaluationL18compareBundleClassERNS0_5StateERKNS0_15ExtendedBindingES5_
- __ZN14LaunchServices17BindingEvaluationL28defaultAppCategoryBeingBoundERKNS0_5StateE
- ___104-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]_block_invoke_2
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.373
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.373.cold.1
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.399
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.399.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.643
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.643.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644.cold.2
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.370
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.370.cold.1
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.308
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.311
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.314
- ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.382
- ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.374
- ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.757
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.377
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.378
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.379
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.248
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.253
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.635
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.635.cold.1
- ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.288
- ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.394
- ___96-[_LSApplicationRecordEnumerator(Private) _applicationRecordWithContext:bundleIdentifierOrUnit:]_block_invoke_2
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.316
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.316.cold.1
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.317
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.317.cold.1
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.307
- ___Block_byref_object_copy_.1012
- ___Block_byref_object_copy_.1194
- ___Block_byref_object_copy_.387
- ___Block_byref_object_copy_.613
- ___Block_byref_object_copy_.688
- ___Block_byref_object_dispose_.1013
- ___Block_byref_object_dispose_.1195
- ___Block_byref_object_dispose_.388
- ___Block_byref_object_dispose_.614
- ___Block_byref_object_dispose_.689
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.940
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.940.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.944
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.944.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.946
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.942
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.949
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.949.cold.1
- ____LSServer_SyncWithMobileInstallation_block_invoke.1014
- ____LSServer_SyncWithMobileInstallation_block_invoke_2.1015
- ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.35
- ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.36
- ____ZL15_LSContainerAddP9LSContextP6FSNodeP6NSDataS2_S4_tyhU13block_pointerFvjP7NSErrorE_block_invoke.38
- ___block_descriptor_32_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
- ___block_descriptor_40_ea8_32s_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_44_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20l
- ___block_descriptor_48_ea8_32bs_e375_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20ls32l8
- ___block_descriptor_52_ea8_32s_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8
- ___block_descriptor_56_ea8_32bs40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8
- ___block_descriptor_604_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
- ___block_descriptor_604_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
- ___block_descriptor_60_ea8_32s40s_e31_B28?0I8^I12r^^{LSBundleData}20ls32l8s40l8
- ___block_descriptor_72_e8_32bs40r48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20ls32l8s40l8r48l8
- ___block_literal_global.1099
- ___block_literal_global.110
- ___block_literal_global.1122
- ___block_literal_global.1149
- ___block_literal_global.1151
- ___block_literal_global.1162
- ___block_literal_global.132
- ___block_literal_global.147
- ___block_literal_global.233
- ___block_literal_global.259
- ___block_literal_global.292
- ___block_literal_global.313
- ___block_literal_global.316
- ___block_literal_global.334
- ___block_literal_global.390
- ___block_literal_global.398
- ___block_literal_global.426
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.475
- ___block_literal_global.53
- ___block_literal_global.551
- ___block_literal_global.576
- ___block_literal_global.632
- ___block_literal_global.642
- ___block_literal_global.656
- ___block_literal_global.673
- ___block_literal_global.675
- ___block_literal_global.919
- ___block_literal_global.947
- ___block_literal_global.986
- _objc_msgSend$_getContainer:context:error:
- _preferredLocalizations.once.248
CStrings:
+ "%@ is on a trusted cryptex, setting kLSRegisterTrusted"
+ "-[FSNode getFSID:error:]"
+ "-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]"
+ "-[_LSApplicationRecordsWithinDirectoryEnumerator _preflightPathOfBundleWithContext:bundleUnit:bundleData:]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
+ "<LSBundleURLRelationshipPrecondition: %@ relationship to %@>"
+ "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
+ "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "@40@0:8@16Q24Q32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36"
+ "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20@28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28^@36"
+ "@48@0:8@16@24q32q40"
+ "@56@0:8^{LSContext=@}16@24@32Q40Q48"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "B32@0:8^{fsid=[2i]}16^@24"
+ "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28"
+ "B36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20^{LSContext=@}28@36^@44"
+ "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}36@44^@52"
+ "BOOL _LSAliasDataMatchesPath_NoIO(NSData *__strong, NSString *__strong, LSPathMatchType)"
+ "BOOL _LSAliasMatchesPath_NoIO(__strong LSDatabaseRef, LSAliasID, NSString *__strong, LSPathMatchType)"
+ "BOOL _LSPathMatchesPath_NoIO(NSString *__strong, NSString *__strong, LSPathMatchType)"
+ "Boolean _LSServer_NodeIsOnTrustedCryptex(FSNode *__strong)"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "Cleaning ephemeral mobile containers"
+ "Cleaning nonexistent cryptex bundles"
+ "Couldn't get URL relationship for %@ and %@: %@"
+ "Couldn't get path in %{public}s: %@"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "LSBundleURLRelationshipPrecondition"
+ "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "Removed bundle unit %llx, status: %d"
+ "SIMULATOR_SHARED_RESOURCES_DIRECTORY"
+ "SerializedPlaceholderPath"
+ "Skipping URL claims for bundle %llu because it is a remote placeholder"
+ "Skipping document claims for bundle %llu because it is a remote placeholder"
+ "T@\"NSString\",R,N,V_serializedPlaceholderPath"
+ "This process needs to be linked against Fall 2025 SDKs or later to open file: URLs with openURL interfaces."
+ "_LSApplicationRecordsWithinDirectoryEnumerator"
+ "_LSErrorEnumerator"
+ "_LSIsOnCryptex"
+ "_LSNodeIsOnCryptex"
+ "_LSRecord_resolve_serializedPlaceholderURL"
+ "_LSRegisterTypeDeclarationsForBundle"
+ "_LSRegisterTypeDeclarationsForPlugin"
+ "_LSServer_NodeIsOnTrustedCryptex"
+ "_LSServer_URLIsOnTrustedCryptex"
+ "_createPostflightedApplicationRecordWithContext:bundleUnit:bundleData:"
+ "_directoryURL"
+ "_enumerationOptions"
+ "_filteringOptions"
+ "_placeholderFetchBehavior"
+ "_preflightPathOfBundleWithContext:bundleUnit:bundleData:"
+ "_requiredRelationship"
+ "_serializedPlaceholderPath"
+ "_volumeContainerAdapter"
+ "apfs"
+ "bad_variant_access was thrown in -fno-exceptions mode"
+ "binding default app category with at least one system app placeholder, not preferring apple"
+ "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "couldn't copy node for unit %llx on cryptex, assuming it is gone: %d"
+ "couldn't get cryptex info: %@"
+ "couldn't get node in %{public}s: %@"
+ "couldn't get volume node in %{public}s: %@"
+ "cryptex unit %llx is not reachable at %@, will remove"
+ "enumeratorForApplicationsOnSameVolumeWithinDirectoryAtURL:enumerationOptions:filteringOptions:"
+ "fileURLWithPath:isDirectory:"
+ "getFSID:error:"
+ "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}24"
+ "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "inBundleData"
+ "inPluginData"
+ "initWithContext:directoryURL:volumeURL:enumerationOptions:filteringOptions:"
+ "initWithPreparationError:"
+ "initWithURL:bundleIdentifier:placeholderFetchBehavior:requiredRelationship:"
+ "isBundleEligibleForOpenDocumentViaOpenURL:"
+ "isCurrentProcessEligibleForOpenDocumentViaOpenURL"
+ "on-cryptex"
+ "org.reactjs.native.Popspedia"
+ "path1 != nil"
+ "path2 != nil"
+ "placeholderFetchBehavior"
+ "preconditionCheckingRelationshipToURL:ofBundleWithIdentifier:placeholderFetchBehavior:requiredRelationship:"
+ "requiredRelationship"
+ "serialized placeholder"
+ "serializedPlaceholderURL"
+ "serializedPlaceholderURLWithContext:tableID:unitID:unitBytes:"
+ "simulatorSharedResourcesDirectoryURL"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}12*20"
+ "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
+ "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"serializedPlaceholderPath\"I\"_reserved5\"I}"
+ "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32@0:8@16^@24"
+ "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"isOnCryptex\"b1}"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}32"
+ "{VolumeContainerResolutionAdapter=\"volumeURLOrContainerOrError\"{variant<unsigned int, NSURL *, NSError *>=\"__impl_\"{__impl<unsigned int, NSURL *, NSError *>=\"__data\"(__union<std::__variant_detail::_Trait::_Available, 0UL, unsigned int, NSURL *, NSError *>=\"__dummy\"c\"__head\"{__alt<0UL, unsigned int>=\"__value\"I}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 1UL, NSURL *, NSError *>=\"__dummy\"c\"__head\"{__alt<1UL, NSURL *>=\"__value\"@\"NSURL\"}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 2UL, NSError *>=\"__dummy\"c\"__head\"{__alt<2UL, NSError *>=\"__value\"@\"NSError\"}\"__tail\"(__union<std::__variant_detail::_Trait::_Available, 3UL>=))))\"__index\"I}}}"
+ "{expected<LSApplicationRecord *, NSError *>={__conditional_no_unique_address<true, std::__expected_base<LSApplicationRecord *, NSError *>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<LSApplicationRecord *, NSError *>::__union_t>=(__union_t=@@)}B}}}36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIIII}28"
- "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36"
- "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20@28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28^@36"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28"
- "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28@36^@44"
- "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36@44^@52"
- "BOOL _LSAliasDataMatchesPath_NoIO(NSData *__strong, NSString *__strong, LSAliasPathMatchType)"
- "BOOL _LSAliasMatchesPath_NoIO(__strong LSDatabaseRef, LSAliasID, NSString *__strong, LSAliasPathMatchType)"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "_container"
- "_getContainer:context:error:"
- "_volumeURL"
- "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "is Apple"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20"
- "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"_reserved\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"_reserved5\"I}"
- "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32@0:8@16^@24"
- "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"supportsDataExport\"b1\"hasSupportsGameModeKey\"b1\"supportsGameMode\"b1\"_reserved\"b1}"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"

```
