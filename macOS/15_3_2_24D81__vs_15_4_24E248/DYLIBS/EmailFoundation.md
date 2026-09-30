## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/Versions/A/EmailFoundation`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x6bbe4
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x5de4
-  __TEXT.__gcc_except_tab: 0xbd50
+3826.500.181.1.5
+  __TEXT.__text: 0x6c118
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_methlist: 0x6524
+  __TEXT.__gcc_except_tab: 0xbdb8
   __TEXT.__const: 0x1ca
-  __TEXT.__cstring: 0x4277
+  __TEXT.__cstring: 0x4207
   __TEXT.__oslogstring: 0xc9c
   __TEXT.__ustring: 0x58
   __TEXT.__swift5_typeref: 0xda

   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4900
+  __TEXT.__unwind_info: 0x4958
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0xe41
-  __TEXT.__objc_methname: 0xbecb
-  __TEXT.__objc_methtype: 0x1c0c
-  __TEXT.__objc_stubs: 0x8720
-  __DATA_CONST.__got: 0x6f0
+  __TEXT.__objc_methname: 0xbf67
+  __TEXT.__objc_methtype: 0x1c07
+  __TEXT.__objc_stubs: 0x8740
+  __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__objc_classlist: 0x440
-  __DATA_CONST.__objc_catlist: 0x108
+  __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3368
+  __DATA_CONST.__objc_selrefs: 0x3400
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH_CONST.__const: 0x2b18
-  __AUTH_CONST.__cfstring: 0x4fa0
-  __AUTH_CONST.__objc_const: 0xcd30
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__const: 0x2b48
+  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__objc_const: 0xc180
   __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x50c
+  __DATA.__objc_ivar: 0x510
   __DATA.__data: 0xec8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x320
+  __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x2260
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x138

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
-  - /System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D9FF2E3C-86BF-3A25-9D68-268EA70E50AB
-  Functions: 2581
-  Symbols:   7341
-  CStrings:  4169
+  UUID: C23452D8-ED2B-33D6-9062-0E9E5E14C132
+  Functions: 2632
+  Symbols:   7414
+  CStrings:  4184
 
Symbols:
+ +[EFAutoBugCaptureReporter sharedReporter].cold.1
+ +[EFByteSet asciiWhitespaceSet].cold.1
+ +[EFDevice currentDevice].cold.1
+ +[EFDevice setCurrentDevice:].cold.1
+ +[EFFileCompression _compressionLock].cold.1
+ +[EFFileCompression _compressionQueueContext].cold.1
+ +[EFNetworkStatus cellular].cold.1
+ +[EFNetworkStatus external].cold.1
+ +[EFNetworkStatus wifi].cold.1
+ +[EFNetworkStatus wired].cold.1
+ +[EFPrivacy redactedQueryStringForSearchableQueryString:]
+ +[EFSQLColumnSchema columnTypeForString:].cold.1
+ +[EFScheduler immediateScheduler].cold.1
+ +[EFScheduler mainThreadScheduler].cold.1
+ +[EFSchedulerTrampoline trampolineWithScheduler:object:].cold.1
+ +[NSCharacterSet(MailCoreAdditions) ef_asciiAlphaNumericCharacterSet].cold.1
+ +[NSCharacterSet(MailCoreAdditions) ef_rfc6376WhitespaceCharacterSet].cold.1
+ +[NSCharacterSet(MailCoreAdditions) ef_unsafeAddressLocalPartCharacterSet].cold.1
+ +[NSCharacterSet(MailCoreAdditions) ef_unsafeDomainNameCharacterSet].cold.1
+ +[NSData(EmailFoundationAdditions) ef_crlfData].cold.1
+ +[NSDateFormatter(MessageUIAdditions) ef_formatterForStyle:].cold.1
+ +[NSDateFormatter(MessageUIAdditions) ef_formatterForStyle:].cold.2
+ +[NSDateFormatter(MessageUIAdditions) ef_formatterForStyle:].cold.3
+ +[NSDateFormatter(MessageUIAdditions) ef_isoDateFormatter].cold.1
+ +[NSError(EFPubliclyDescribableAdditions) ef_setDecoder:forDomain:].cold.1
+ +[NSError(EFSQLite) ef_SQLiteErrorWithCode:].cold.1
+ +[NSLocale(EmailFoundationAdditions) ef_posixLocale].cold.1
+ -[EFDevice areInternalSecurityPoliciesAllowed]
+ -[EFDevice isMac]
+ -[EFDevice isPad]
+ -[EFDevice isVirtualMachine].cold.1
+ -[EFDevice setAreInternalSecurityPoliciesAllowed:]
+ -[EFDevice supportsGenerativeModelSystems].cold.1
+ -[EFSQLColumnExpression(EFCacheable) cachedSelf].cold.1
+ -[EFSQLDisqualifiedColumnExpression(EFCacheable) cachedSelf].cold.1
+ -[EFSQLIndexedColumnSchema name].cold.1
+ -[EFStringHash redactedStringValue].cold.1
+ -[NSError(EFPubliclyDescribableAdditions) ef_publicDescription].cold.1
+ -[NSString(EmailFoundationAdditions) ef_isUnsignedIntegerString].cold.1
+ EFContentProtectionGetObservedState.cold.1
+ EFContentProtectionValidateObservedStateIsUnlocked.cold.1
+ EFEncodeCacheableInstance.cold.2
+ EFEncodeCacheableInstance.cold.3
+ EFFetchSignpostLog.cold.1
+ EFFrameworkVersion.cold.1
+ EFIsRunningUnitTests.cold.1
+ EFProductName.cold.1
+ EFProtectedDataAvailable.cold.1
+ EFProtectedDataAvailable.cold.2
+ EFProtectedDataAvailableInState.cold.1
+ EFPurgeableFileLog.cold.1
+ EFSQLVerboseDebugLoggingEnabled.cold.1
+ EFSystemBuildVersion.cold.1
+ EFSystemVersion.cold.1
+ EFVerboseVersion.cold.1
+ OBJC_IVAR_$_EFDevice._areInternalSecurityPoliciesAllowed
+ _DiagnosticStateDictionary.cold.1
+ _InitAndPerformSync.cold.1
+ _Log.cold.1
+ _NotifyObserversWithContentProtectionState.cold.5
+ _NotifyObserversWithContentProtectionState.cold.6
+ __71-[NSCompoundPredicate(EmailFoundationAdditions) ef_simplifiedPredicate]_block_invoke.147
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EFPubliclyDescribable
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__115insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEaSB8ne190102ERKx
+ __ZNSt3__118__set_intersectionB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES9_S9_S9_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESJ_T2_SK_T4_SL_OT0_NS_20forward_iterator_tagESR_
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__122__lower_bound_onesidedB8ne190102INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES7_xKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
+ __ZNSt3__123__lower_bound_bisectingB8ne190102INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEExKNS_10__identityENS_6__lessIvvEEEET0_SC_RKT1_NS_15iterator_traitsISC_E15difference_typeERT3_RT2_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__138__set_intersection_add_output_if_equalB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES6_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEEvbRT_RT0_RT1_Rb
+ __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEE6insertB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvT_SD_
+ __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEEC2B8ne190102ERKS5_
+ __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE18_DetachedTreeCacheD2B8ne190102Ev
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE12__advance_toB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEENS_15iterator_traitsIT_E15difference_typeERSB_SD_RKSB_NS_26bidirectional_iterator_tagE
+ __ZNSt3__19__advanceB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
+ ___17-[EFDevice isMac]_block_invoke
+ ___57+[EFPrivacy redactedQueryStringForSearchableQueryString:]_block_invoke
+ ___InitObservation_block_invoke.83
+ ___block_descriptor_40_ea8_32r_e11_v24?0Q8q16l
+ ___block_descriptor_48_ea8_32s40s_e37_v32?0"NSTextCheckingResult"8Q16^B24l
+ __block_literal_global.121
+ __block_literal_global.146
+ __block_literal_global.85
+ _ef_log_EFNetworkStatus.cold.1
+ _ef_log_EFObservable.cold.1
+ _ef_log_EFProtectedFile.cold.1
+ _ef_log_EFSQLQueryGenerator.cold.1
+ _objc_msgSend$emailAddressValue
+ _objc_msgSend$fullyOrPartiallyRedactedStringForString:
+ _objc_msgSend$isPlatform:
+ _objc_msgSend$setAreInternalSecurityPoliciesAllowed:
+ _os_variant_allows_internal_security_policies
+ activityLog.cold.1
+ is32Bit.cold.1
+ isMac.isMac
+ isMac.onceToken
- -[NSBundle(EmailFoundationAdditions) ef_normalizedStringForLocale:]
- -[NSBundle(EmailFoundationAdditions) ef_preferredLanguageIdentifier]
- _OBJC_CLASS_$_IntlUtility
- __71-[NSCompoundPredicate(EmailFoundationAdditions) ef_simplifiedPredicate]_block_invoke.144
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSBundle_$_EmailFoundationAdditions
- __OBJC_$_CATEGORY_NSBundle_$_EmailFoundationAdditions
- __OBJC_$_PROP_LIST_NSBundle_$_EmailFoundationAdditions
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__115insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEaSB8ne180100ERKx
- __ZNSt3__118__set_intersectionB8ne180100INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES9_S9_S9_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESJ_T2_SK_T4_SL_OT0_
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEE6insertB8ne180100INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvT_SD_
- __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEEC2B8ne180100ERKS5_
- __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE18_DetachedTreeCacheD2B8ne180100Ev
- __ZSt9terminatev
- ___InitObservation_block_invoke.88
- ___block_descriptor_40_ea8_32rcd_e11_v24?0Q8q16l
- ___clang_call_terminate
- ___copy_helper_block_ea8_32rc
- ___cxa_begin_catch
- ___destroy_helper_block_ea8_32rd
- __block_literal_global.118
- __block_literal_global.143
- __block_literal_global.84
- _objc_msgSend$ef_normalizedStringForLocale:
- _objc_msgSend$normalizedLanguageIDFromString:
- _objc_msgSend$preferredLocalizations
CStrings:
+ "%@ = '%@'"
+ "%@|"
+ ") = '([^']+)'\\)"
+ "EFContentProtectionStateInvalid != EFContentProtectionGetObservedState()"
+ "EFInt64Set.mm"
+ "T@\"NSString\",?,R,C,N"
+ "TB,V_areInternalSecurityPoliciesAllowed"
+ "\\(("
+ "_areInternalSecurityPoliciesAllowed"
+ "areInternalSecurityPoliciesAllowed"
+ "ef_shortPublicDescription"
+ "emailAddressValue"
+ "isMac"
+ "isPad"
+ "kMDItemAuthorEmailAddresses"
+ "kMDItemAuthors"
+ "redactedQueryStringForSearchableQueryString:"
+ "setAreInternalSecurityPoliciesAllowed:"
+ "{set<long long, std::less<long long>, std::allocator<long long>>=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<long long, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<long long>>=\"__value_\"Q}}}"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/EmailFoundation/Containers/EFInt64Set.mm"
- "<Unknown File>"
- "EFContentProtectionStateInvalid != sContentProtectionState"
- "Invalid parameter not satisfying: %s"
- "ef_normalizedStringForLocale:"
- "ef_preferredLanguageIdentifier"
- "normalizedLanguageIDFromString:"
- "preferredLocalizations"
- "{set<long long, std::less<long long>, std::allocator<long long> >=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long> >=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<long long, void *> > >=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<long long> >=\"__value_\"Q}}}"

```
