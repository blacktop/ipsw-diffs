## TipKitCore

> `/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0xb1f6c
-  __TEXT.__auth_stubs: 0x2600
+85.0.0.0.0
+  __TEXT.__text: 0xb1d80
+  __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0x7e80
-  __TEXT.__cstring: 0x3892
-  __TEXT.__constg_swiftt: 0x1990
-  __TEXT.__swift5_typeref: 0x2da6
-  __TEXT.__swift5_reflstr: 0x1856
+  __TEXT.__const: 0x8128
+  __TEXT.__cstring: 0x3872
+  __TEXT.__constg_swiftt: 0x196c
+  __TEXT.__swift5_typeref: 0x2db0
+  __TEXT.__swift5_reflstr: 0x1836
   __TEXT.__swift5_fieldmd: 0x2138
   __TEXT.__swift5_assocty: 0x688
   __TEXT.__swift5_capture: 0x4dc

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__oslogstring: 0x3
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x3c10
-  __TEXT.__eh_frame: 0x7758
+  __TEXT.__unwind_info: 0x3c80
+  __TEXT.__eh_frame: 0x7990
   __TEXT.__objc_classname: 0x9
   __TEXT.__objc_methname: 0x72a
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__const: 0x408
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x208
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1300
-  __AUTH_CONST.__auth_ptr: 0xb88
+  __AUTH_CONST.__auth_got: 0x1318
+  __AUTH_CONST.__auth_ptr: 0xbe0
   __AUTH_CONST.__const: 0x4d18
-  __AUTH_CONST.__objc_const: 0x1600
-  __AUTH.__objc_data: 0x178
-  __AUTH.__data: 0x3b8
-  __DATA.__data: 0x1020
-  __DATA.__bss: 0x7040
-  __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x3f0
-  __DATA_DIRTY.__data: 0x2500
-  __DATA_DIRTY.__bss: 0x6e80
-  __DATA_DIRTY.__common: 0x78
+  __AUTH_CONST.__objc_const: 0x1648
+  __DATA.__data: 0xc10
+  __DATA.__bss: 0x6a20
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x518
+  __DATA_DIRTY.__data: 0x2c80
+  __DATA_DIRTY.__bss: 0x7500
+  __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5483
-  Symbols:   210
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5518
+  Symbols:   218
+  CStrings:  266
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "_$s10Foundation10CocoaErrorV03_nsC0So7NSErrorCvg"
+ "_$s10Foundation10CocoaErrorV10underlyings0C0_pSgvg"
+ "_$s10Foundation10CocoaErrorV11errorDomainSSvgZ"
+ "_$s10Foundation10CocoaErrorV4CodeV8rawValueAESi_tcfC"
+ "_$s10Foundation10CocoaErrorV4CodeV8rawValueSivg"
+ "_$s10Foundation10CocoaErrorV5error_8userInfo3urls0C0_pAC4CodeV_SDys11AnyHashableVypGSgAA3URLVSgtFZ"
+ "_$s10Foundation11FormatStylePA2A4DateV07ISO8601bC0VRszrlE7iso8601AGvgZ"
+ "_$s10Foundation11JSONDecoderC11allowsJSON5SbvsTj"
+ "_$s10Foundation11JSONDecoderC6decode_4from13configurationxxm_AA4DataV21DecodingConfigurationQztKAA013DecodableWithH0RzlFTj"
+ "_$s10Foundation11JSONDecoderC6decode_4from13configurationxxm_AA4DataVq_mtKAA26DecodableWithConfigurationRzAA08DecodingI9ProvidingR_0jI0Qy_AKRtzr0_lFTj"
+ "_$s10Foundation11JSONDecoderCACycfC"
+ "_$s10Foundation13ParseStrategyP5parsey0B6OutputQz0B5InputQzKFTj"
+ "_$s10Foundation13ParseStrategyPA2A4DateV18ISO8601FormatStyleVRszrlE7iso8601AGvgZ"
+ "_$s10Foundation14LocalizedErrorP10helpAnchorSSSgvgTj"
+ "_$s10Foundation14LocalizedErrorPAAE10helpAnchorSSSgvg"
+ "_$s10Foundation14LocalizedErrorPAAE16errorDescriptionSSSgvg"
+ "_$s10Foundation14SortComparatorP5orderAA0B5OrderOvgTj"
+ "_$s10Foundation14SortComparatorP5orderAA0B5OrderOvsTj"
+ "_$s10Foundation14SortComparatorP7compareySo18NSComparisonResultV8ComparedQz_AHtFTj"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV011MeasurementB0V9ComponentOMa"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV012NumberFormatD0V06SymbolB0O0G0OMa"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV012NumberFormatD0V12numberSymbolAG0hB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV013DurationFieldB0O0F0OMa"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV09DateFieldB0O0F0O2eeoiySbAI_AItFZ"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV09DateFieldB0O0F0OMa"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV10morphologyAE010MorphologyB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV11measurementAE011MeasurementB0Vvg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV13durationFieldAE08DurationfB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV18languageIdentifierAE08LanguagefB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV24inlinePresentationIntentAE06InlinefgB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV4linkAE04LinkB0Ovg"
+ "_$s10Foundation15AttributeScopesO0A10AttributesV9dateFieldAE04DatefB0Ovg"
+ "_$s10Foundation15AttributeScopesO10foundationAC0A10AttributesVmvg"
+ "_$s10Foundation16AttributedStringV10charactersAC13CharacterViewVvM"
+ "_$s10Foundation16AttributedStringV13CharacterViewV10startIndexAC0G0Vvg"
+ "_$s10Foundation16AttributedStringV13CharacterViewV15replaceSubrange_4withySnyAC5IndexVG_xtSlRzSJ7ElementRtzlF"
+ "_$s10Foundation16AttributedStringV13CharacterViewV6_countSivg"
+ "_$s10Foundation16AttributedStringV13CharacterViewV6_index_8offsetByAC5IndexVAI_SitF"
+ "_$s10Foundation16AttributedStringV13CharacterViewV9_distance4from2toSiAC5IndexV_AJtF"
+ "_$s10Foundation16AttributedStringV13CharacterViewVySJAC5IndexVcig"
+ "_$s10Foundation16AttributedStringV13CharacterViewVySJAC5IndexVcis"
+ "_$s10Foundation16AttributedStringV13CharacterViewVys5SliceVyAEGSnyAC5IndexVGcig"
+ "_$s10Foundation16AttributedStringV8markdown7options7baseURLACSS_AC22MarkdownParsingOptionsVAA0G0VSgtKcfC"
+ "_$s10Foundation16AttributedStringV8markdown7options7baseURLAcA4DataV_AC22MarkdownParsingOptionsVAA0G0VSgtKcfC"
+ "_$s10Foundation16AttributedStringV8markdown9including7options7baseURLACSS_xmAC22MarkdownParsingOptionsVAA0H0VSgtKcAA14AttributeScopeRzlufC"
+ "_$s10Foundation17URLResourceValuesV03allC0SDySo16NSURLResourceKeyaypGvg"
+ "_$s10Foundation17URLResourceValuesV10isReadableSbSgvg"
+ "_$s10Foundation17URLResourceValuesV11isPurgeableSbSgvg"
+ "_$s10Foundation17URLResourceValuesV12isExecutableSbSgvg"
+ "_$s10Foundation17URLResourceValuesV13canonicalPathSSSgvg"
+ "_$s10Foundation17URLResourceValuesV13isRegularFileSbSgvg"
+ "_$s10Foundation17URLResourceValuesV13totalFileSizeSiSgvg"
+ "_$s10Foundation17URLResourceValuesV13volumeIsLocalSbSgvg"
+ "_$s10Foundation17URLResourceValuesV14fileProtectionSo09NSURLFileE4TypeaSgvg"
+ "_$s10Foundation17URLResourceValuesV14isSymbolicLinkSbSgvg"
+ "_$s10Foundation17URLResourceValuesV16volumeIsInternalSbSgvg"
+ "_$s10Foundation17URLResourceValuesV17contentAccessDateAA0F0VSgvg"
+ "_$s10Foundation17URLResourceValuesV17fileAllocatedSizeSiSgvg"
+ "_$s10Foundation17URLResourceValuesV18documentIdentifierSiSgvg"
+ "_$s10Foundation17URLResourceValuesV19volumeLocalizedNameSSSgvg"
+ "_$s10Foundation17URLResourceValuesV19volumeTotalCapacitySiSgvg"
+ "_$s10Foundation17URLResourceValuesV20isExcludedFromBackupSbSgvg"
+ "_$s10Foundation17URLResourceValuesV22fileResourceIdentifierSo9NSCopying_So14NSSecureCodingSo8NSObjectpSgvg"
+ "_$s10Foundation17URLResourceValuesV22totalFileAllocatedSizeSiSgvg"
+ "_$s10Foundation17URLResourceValuesV23volumeAvailableCapacitySiSgvg"
+ "_$s10Foundation17URLResourceValuesV32volumeSupportsCaseSensitiveNamesSbSgvg"
+ "_$s10Foundation17URLResourceValuesV40volumeAvailableCapacityForImportantUsages5Int64VSgvg"
+ "_$s10Foundation17URLResourceValuesV4nameSSSgvg"
+ "_$s10Foundation17URLResourceValuesV9isPackageSbSgvg"
+ "_$s10Foundation17URLResourceValuesV9isPackageSbSgvs"
+ "_$s10Foundation18AttributeContainerV13dynamicMember5ValueQzSgs7KeyPathCyAA0B13DynamicLookupOxG_tcAA016AttributedStringG0Rzluig"
+ "_$s10Foundation18AttributeContainerV13dynamicMemberAC7BuilderVy_xGs7KeyPathCyAA0B13DynamicLookupOxG_tcAA016AttributedStringG0Rzluig"
+ "_$s10Foundation18AttributeContainerV13dynamicMemberAC7BuilderVy_xGs7KeyPathCyAA0B13DynamicLookupOxG_tcAA016AttributedStringG0RzluigZ"
+ "_$s10Foundation18AttributeContainerV2eeoiySbAC_ACtFZ"
+ "_$s10Foundation18AttributeContainerV5merge_0D6PolicyyAC_AA16AttributedStringV0b5MergeE0OtF"
+ "_$s10Foundation18AttributeContainerV7BuilderV14callAsFunctionyAC5ValueQzF"
+ "_$s10Foundation18AttributeContainerV7BuilderVMa"
+ "_$s10Foundation18AttributeContainerV7merging_11mergePolicyA2C_AA16AttributedStringV0b5MergeF0OtF"
+ "_$s10Foundation18AttributeContainerVy5ValueQzSgxmcAA19AttributedStringKeyRzluig"
+ "_$s10Foundation18AttributeContainerVy5ValueQzSgxmcAA19AttributedStringKeyRzluis"
+ "_$s10Foundation18NSIndexSetIteratorVMa"
+ "_$s10Foundation18_ErrorCodeProtocolPAAE2teoiySbx_s0B0_ptFZ"
+ "_$s10Foundation20ParseableFormatStylePA2A4DateV07ISO8601cD0VRszrlE7iso8601AGvgZ"
+ "_$s10Foundation20PredicateExpressionsO0B8EvaluateV5inputq_q_Qp_tvg"
+ "_$s10Foundation20PredicateExpressionsO0B8EvaluateV9predicatexvg"
+ "_$s10Foundation20PredicateExpressionsO11ConjunctionV3lhs3rhsAEy_xq_Gx_q_tcfC"
+ "_$s10Foundation20PredicateExpressionsO11ConjunctionV3lhsxvg"
+ "_$s10Foundation20PredicateExpressionsO11ConjunctionV3rhsq_vg"
+ "_$s10Foundation20PredicateExpressionsO15SequenceMaximumV8elementsxvg"
+ "_$s10Foundation20PredicateExpressionsO15SequenceMinimumV8elementsxvg"
+ "_$s10Foundation20PredicateExpressionsO17build_Conjunction3lhs3rhsAC0E0Vy_xq_Gx_q_tAA0B10ExpressionRzAaJR_Sb6OutputRtzSbAKRt_r0_lFZ"
+ "_$s10Foundation20PredicateExpressionsO8NegationV7wrappedxvg"
+ "_$s10Foundation22AttributeDynamicLookupO13dynamicMemberxs7KeyPathCyAA0B6ScopesO0A10AttributesV012NumberFormatJ0VxG_tcAA016AttributedStringG0Rzluig"
+ "_$s10Foundation22AttributeDynamicLookupO13dynamicMemberxs7KeyPathCyAA0B6ScopesO0A10AttributesVxG_tcAA016AttributedStringG0Rzluig"
+ "_$s10Foundation24FloatingPointFormatStyleV10AttributedVMa"
+ "_$s10Foundation24FloatingPointFormatStyleV16decimalSeparator8strategyACyxGAA06NumberdE13ConfigurationO07DecimalG15DisplayStrategyV_tF"
+ "_$s10Foundation24FloatingPointFormatStyleV7PercentV10attributedAC10AttributedVyx_Gvg"
+ "_$s10Foundation24FloatingPointFormatStyleV7PercentV4sign8strategyAEyx_GAA06NumberdE13ConfigurationO19SignDisplayStrategyV_tF"
+ "_$s10Foundation24FloatingPointFormatStyleV7PercentV7rounded4rule9incrementAEyx_Gs0bC12RoundingRuleO_SdSgtF"
+ "_$s10Foundation24FloatingPointFormatStyleV7PercentV9precisionyAEyx_GAA06NumberdE13ConfigurationO9PrecisionVF"
+ "_$s10Foundation24FloatingPointFormatStyleV7rounded4rule9incrementACyxGs0bC12RoundingRuleO_SdSgtF"
+ "_$s10Foundation24FloatingPointFormatStyleV8notationyACyxGAA06NumberdE13ConfigurationO8NotationVF"
+ "_$s10Foundation3URLV04baseB0ACSgvg"
+ "_$s10Foundation3URLV12bookmarkData7options30includingResourceValuesForKeys10relativeToAA0D0VSo28NSURLBookmarkCreationOptionsV_ShySo16NSURLResourceKeyaGSgACSgtKF"
+ "_$s10Foundation3URLV15cachesDirectoryACvgZ"
+ "_$s10Foundation3URLV15fileURLWithPath10relativeToACSSh_ACSghtcfC"
+ "_$s10Foundation3URLV16libraryDirectoryACvgZ"
+ "_$s10Foundation3URLV18dataRepresentation10relativeTo10isAbsoluteACSgAA4DataVh_AGhSbtcfC"
+ "_$s10Foundation3URLV18dataRepresentationAA4DataVvg"
+ "_$s10Foundation3URLV18documentsDirectoryACvgZ"
+ "_$s10Foundation3URLV19deletePathExtensionyyF"
+ "_$s10Foundation3URLV21resolvingBookmarkData7options10relativeTo08bookmarkE7IsStaleAcA0E0Vh_So30NSURLBookmarkResolutionOptionsVACSghSbztKcfC"
+ "_$s10Foundation3URLV23deleteLastPathComponentyyF"
+ "_$s10Foundation3URLV26promisedItemResourceValues7forKeysAA011URLResourceF0VShySo16NSURLResourceKeyaG_tKF"
+ "_$s10Foundation3URLV28checkPromisedItemIsReachableSbyKF"
+ "_$s10Foundation3URLV29removeAllCachedResourceValuesyyF"
+ "_$s10Foundation3URLV35stopAccessingSecurityScopedResourceyyF"
+ "_$s10Foundation3URLV4hash4intoys6HasherVz_tF"
+ "_$s10Foundation3URLV4host14percentEncodedSSSgSb_tF"
+ "_$s10Foundation3URLV4portSiSgvg"
+ "_$s10Foundation3URLV4userSSSgvg"
+ "_$s10Foundation3URLV5querySSSgvg"
+ "_$s10Foundation3URLV6append10queryItemsySayAA12URLQueryItemVG_tF"
+ "_$s10Foundation3URLV6append4path13directoryHintyx_AC09DirectoryF0OtSyRzlF"
+ "_$s10Foundation3URLV6append9component13directoryHintyx_AC09DirectoryF0OtSyRzlF"
+ "_$s10Foundation3URLV6string25encodingInvalidCharactersACSgSSh_SbtcfC"
+ "_$s10Foundation3URLV8fragment14percentEncodedSSSgSb_tF"
+ "_$s10Foundation3URLV8fragmentSSSgvg"
+ "_$s10Foundation3URLV9appending10queryItemsACSayAA12URLQueryItemVG_tF"
+ "_$s10Foundation3URLV9hashValueSivg"
+ "_$s10Foundation4DataV10LargeSliceV21ensureUniqueReferenceyyF"
+ "_$s10Foundation4DataV10LargeSliceVyAESWcfC"
+ "_$s10Foundation4DataV10contentsOf7optionsAcA3URLVh_So20NSDataReadingOptionsVtKcfC"
+ "_$s10Foundation4DataV11bytesNoCopy5count11deallocatorACSv_SiAC11DeallocatorOtcfC"
+ "_$s10Foundation4DataV14RangeReferenceCMa"
+ "_$s10Foundation4DataV14RangeReferenceCfD"
+ "_$s10Foundation4DataV15_RepresentationO15reserveCapacityyySiF"
+ "_$s10Foundation4DataV15_RepresentationO_5countAeA02__B7StorageC_SitcfC"
+ "_$s10Foundation4DataV15withUnsafeBytesyxxSPyq_GKXEKr0_lF"
+ "_$s10Foundation4DataV22withUnsafeMutableBytesyxxSpyq_GKXEKr0_lF"
+ "_$s10Foundation4DataV22withUnsafeMutableBytesyxxSwKXEKlF"
+ "_$s10Foundation4DataV4fromACs7Decoder_p_tKcfC"
+ "_$s10Foundation4DataV5bytesACx_tcSTRzs5UInt8V7ElementRtzlufC"
+ "_$s10Foundation4DataV5range2of7options2inSnySiGSgAC_So19NSDataSearchOptionsVAItF"
+ "_$s10Foundation4DataV6append10contentsOfySays5UInt8VG_tF"
+ "_$s10Foundation4DataV6append10contentsOfyx_tSTRzs5UInt8V7ElementRtzlF"
+ "_$s10Foundation4DataV6append_5countySPys5UInt8VG_SitF"
+ "_$s10Foundation4DataV6appendyySRyxGlF"
+ "_$s10Foundation4DataV6bufferACSRyxG_tclufC"
+ "_$s10Foundation4DataV6encode2toys7Encoder_p_tKF"
+ "_$s10Foundation4DataV7indicesSnySiGvg"
+ "_$s10Foundation4DataV8advanced2byACSi_tF"
+ "_$s10Foundation4DataV8capacityACSi_tcfC"
+ "_$s10Foundation4DataV9copyBytes2to4fromSiSryxG_SnySiGSgtlF"
+ "_$s10Foundation4DataV9hashValueSivg"
+ "_$s10Foundation4DataV9repeating5countACs5UInt8V_SitcfC"
+ "_$s10Foundation4DataVACycfC"
+ "_$s10Foundation4DataVyACSnySiGcig"
+ "_$s10Foundation4DateV11description4withSSAA6LocaleVSg_tF"
+ "_$s10Foundation4DateV13ISO8601FormatySSAC0cD5StyleVF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV13dateSeparatoryA2E0bG0OF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV13parseStrategyAEvg"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV13timeSeparatoryA2E04TimeG0OF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV17timeZoneSeparatoryA2E04TimegH0OF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV3dayAEyF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV4time26includingFractionalSecondsAESb_tF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV4yearAEyF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV5monthAEyF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV5parseyACSSKF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV6formatySSACF"
+ "_$s10Foundation4DateV18ISO8601FormatStyleV8timeZoneAA04TimeG0Vvs"
+ "_$s10Foundation9SortOrderO2eeoiySbAC_ACtFZ"
+ "_$s10Foundation9SortOrderO4hash4intoys6HasherVz_tF"
+ "_$s17_StringProcessing14RegexComponentP10FoundationAD4DateV18ISO8601FormatStyleVRszrlE19iso8601WithTimeZone26includingFractionalSeconds13dateSeparator0qlR004timeR00smR0AHSb_AH0fR0OAH0flR0OAH0lR0OAH0lmR0OtFZ"
+ "_$s17_StringProcessing14RegexComponentP10FoundationAD4DateV18ISO8601FormatStyleVRszrlE7iso86018timeZone26includingFractionalSeconds13dateSeparator0p4TimeQ00kQ0AhD0rL0V_SbAH0fQ0OAH0frQ0OAH0rQ0OtFZ"
+ "_$sSM10FoundationSkRzrlE4sort5usingyqd___tAA14SortComparatorRd__8ComparedQyd__7ElementSTRtzlF"
+ "_$sSM10FoundationSkRzrlE4sort5usingyqd___tSTRd__AA14SortComparatorRd_0_7ElementQyd__Rsd_0_8ComparedQyd_0_AESTRtzr0_lF"
+ "_$sSS10FoundationE11bytesNoCopy6length8encoding12freeWhenDoneSSSgSv_SiSSAAE8EncodingVSbtcfC"
+ "_$sSS10FoundationE14contentsOfFileS2Sh_tKcfC"
+ "_$sSS10FoundationE7cString8encodingSSSgSPys4Int8VG_SSAAE8EncodingVtcfC"
+ "_$sSo10NSIndexSetC10FoundationE12makeIteratorAC0abE0VyF"
+ "_$sSo7NSTimerC10FoundationE14TimerPublisherC7connect7Combine11Cancellable_pyF"
+ "_$sSo7NSTimerC10FoundationE7publish5every9tolerance2on2in7optionsAbCE14TimerPublisherCSd_SdSgSo9NSRunLoopCSo0kL4ModeaAnCE16SchedulerOptionsVSgtFZ"
+ "_$sSy10FoundationE12commonPrefix4with7optionsSSqd___So22NSStringCompareOptionsVtSyRd__lF"
+ "_$sSy10FoundationE13lengthOfBytes5usingSiSSAAE8EncodingV_tF"
+ "_$sSy10FoundationE14enumerateLines8invokingyySS_Sbztc_tF"
+ "_$sSy10FoundationE15appendingFormatySSqd___s7CVarArg_pdtSyRd__lF"
+ "_$sSy10FoundationE16localizedCompareySo18NSComparisonResultVqd__SyRd__lF"
+ "_$sSy10FoundationE17applyingTransform_7reverseSSSgSo08NSStringC0a_SbtF"
+ "_$sSy10FoundationE24localizedStandardCompareySo18NSComparisonResultVqd__SyRd__lF"
+ "_$sSy10FoundationE25localizedStandardContainsySbqd__SyRd__lF"
+ "_$sSy10FoundationE31localizedCaseInsensitiveCompareySo18NSComparisonResultVqd__SyRd__lF"
+ "_$sSy10FoundationE32rangeOfComposedCharacterSequence2atSnySS5IndexVGAE_tF"
+ "_$sSy10FoundationE36decomposedStringWithCanonicalMappingSSvg"
+ "_$sSy10FoundationE37precomposedStringWithCanonicalMappingSSvg"
+ "_$sSy10FoundationE41precomposedStringWithCompatibilityMappingSSvg"
+ "_$sSy10FoundationE7compare_7options5range6localeSo18NSComparisonResultVqd___So22NSStringCompareOptionsVSnySS5IndexVGSgAA6LocaleVSgtSyRd__lF"
+ "_$sSy10FoundationE7folding7options6localeSSSo22NSStringCompareOptionsV_AA6LocaleVSgtF"
+ "_$sSy10FoundationE7padding8toLength7withPad10startingAtSSSi_qd__SitSyRd__lF"
+ "_$sSy10FoundationE9appendingySSqd__SyRd__lF"
+ "_$sSy10FoundationE9substring2toS2S5IndexV_tF"
+ "_$sSy10FoundationE9substring4fromS2S5IndexV_tF"
+ "_NSLinguisticTagAdjective"
+ "_NSLinguisticTagAdverb"
+ "_NSLinguisticTagClassifier"
+ "_NSLinguisticTagCloseParenthesis"
+ "_NSLinguisticTagCloseQuote"
+ "_NSLinguisticTagConjunction"
+ "_NSLinguisticTagDash"
+ "_NSLinguisticTagDeterminer"
+ "_NSLinguisticTagInterjection"
+ "_NSLinguisticTagNoun"
+ "_NSLinguisticTagNumber"
+ "_NSLinguisticTagOpenParenthesis"
+ "_NSLinguisticTagOpenQuote"
+ "_NSLinguisticTagOrganizationName"
+ "_NSLinguisticTagOtherPunctuation"
+ "_NSLinguisticTagOtherWord"
+ "_NSLinguisticTagParticle"
+ "_NSLinguisticTagPersonalName"
+ "_NSLinguisticTagPlaceName"
+ "_NSLinguisticTagPreposition"
+ "_NSLinguisticTagPronoun"
+ "_NSLinguisticTagSentenceTerminator"
+ "_NSLinguisticTagVerb"
+ "_NSLinguisticTagWordJoiner"
+ "_NSPersonNameComponentFamilyName"
+ "_NSPersonNameComponentGivenName"
+ "_NSPersonNameComponentKey"
+ "_NSPersonNameComponentMiddleName"
+ "_NSPersonNameComponentNickname"
+ "_NSPersonNameComponentPrefix"
+ "_NSPersonNameComponentSuffix"
+ "_NSPresentationIntentAttributeName"
+ "_NSProgressByteCompletedCountKey"
+ "_NSProgressByteTotalCountKey"
+ "_NSProgressCategoryKey"
+ "_NSProgressEstimatedTimeKey"
+ "_NSProgressEstimatedTimeRemainingKey"
+ "_NSProgressFileDisplayNameKey"
+ "_NSProgressFileDownloadingSourceURLKey"
+ "_NSProgressFileIconKey"
+ "_NSProgressFileOperationKindAirDropping"
+ "_NSProgressFileOperationKindArchiving"
+ "_NSProgressFileOperationKindCopying"
+ "_NSProgressFileOperationKindDownloading"
+ "_NSProgressFileOperationKindDuplicating"
+ "_NSProgressFileOperationKindKey"
+ "_NSProgressFileOperationKindReceiving"
+ "_NSProgressFileOperationKindUnarchiving"
+ "_NSProgressFileOperationKindUploading"
+ "_NSProgressFileTotalCountKey"
+ "_NSProgressFileURLKey"
+ "_NSProgressKindFile"
+ "_NSProgressLocalizedDescriptionFileSizeFormatterOptionsKey"
+ "_NSProgressPhysicalFileURLKey"
+ "_NSProgressThroughputKey"
+ "_NSUbiquitousKeyValueStoreChangeReasonKey"
+ "_NSUbiquitousKeyValueStoreChangedKeysKey"
+ "_NSUbiquitousKeyValueStoreDidChangeExternallyNotification"
+ "__NSProgressRemoteLocalizedAdditionalDescriptionKey"
+ "__NSXPCConnectionInvocationReplyToSelectorKey"
+ "__NSXPCConnectionInvocationReplyUserInfoKey"
+ "eVvs"
+ "gOther"
+ "tKey"

```
