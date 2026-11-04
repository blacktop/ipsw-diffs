## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`

```diff

-301.1.16.0.0
-  __TEXT.__text: 0x147790
+301.2.7.2.0
+  __TEXT.__text: 0x14a014
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb3b0
-  __TEXT.__dlopen_cstrs: 0x5cd
-  __TEXT.__const: 0x78d8
-  __TEXT.__constg_swiftt: 0x1b40
-  __TEXT.__swift5_typeref: 0x2efa
+  __TEXT.__objc_methlist: 0xb360
+  __TEXT.__dlopen_cstrs: 0x618
+  __TEXT.__const: 0x78f8
+  __TEXT.__constg_swiftt: 0x1b6c
+  __TEXT.__swift5_typeref: 0x2f3e
   __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_reflstr: 0xe7c
-  __TEXT.__swift5_fieldmd: 0x11dc
+  __TEXT.__swift5_reflstr: 0xeac
+  __TEXT.__swift5_fieldmd: 0x120c
   __TEXT.__swift5_assocty: 0x2b8
-  __TEXT.__cstring: 0xc975
+  __TEXT.__cstring: 0xcac1
   __TEXT.__swift5_proto: 0x284
   __TEXT.__swift5_types: 0x1a4
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_capture: 0x1318
-  __TEXT.__oslogstring: 0xa16e
+  __TEXT.__swift5_capture: 0x1330
+  __TEXT.__oslogstring: 0xa353
   __TEXT.__swift_as_entry: 0x11c
   __TEXT.__swift_as_ret: 0x13c
   __TEXT.__swift_as_cont: 0x1d8
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__gcc_except_tab: 0x208c
-  __TEXT.__unwind_info: 0x6b60
-  __TEXT.__eh_frame: 0x4cc0
+  __TEXT.__gcc_except_tab: 0x20c4
+  __TEXT.__unwind_info: 0x6be0
+  __TEXT.__eh_frame: 0x4d18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a38
-  __DATA_CONST.__objc_classlist: 0x888
+  __DATA_CONST.__const: 0x2a88
+  __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_selrefs: 0x55a0
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x608
+  __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x19e8
-  __AUTH_CONST.__const: 0x64e0
-  __AUTH_CONST.__cfstring: 0x8ee0
-  __AUTH_CONST.__objc_const: 0x16fb0
+  __DATA_CONST.__got: 0x1a00
+  __AUTH_CONST.__const: 0x6538
+  __AUTH_CONST.__cfstring: 0x8f20
+  __AUTH_CONST.__objc_const: 0x16e48
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x18b8
-  __AUTH.__objc_data: 0x3dc8
-  __AUTH.__data: 0x1388
-  __DATA.__objc_ivar: 0xb10
-  __DATA.__data: 0x2934
+  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH.__objc_data: 0x3db0
+  __AUTH.__data: 0x1378
+  __DATA.__objc_ivar: 0xb04
+  __DATA.__data: 0x2974
   __DATA.__common: 0x78
-  __DATA_DIRTY.__objc_data: 0x2440
+  __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/AppIntentsTypeSupport.framework/AppIntentsTypeSupport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8890
-  Symbols:   9290
-  CStrings:  2280
+  Functions: 8926
+  Symbols:   9286
+  CStrings:  2294
 
Symbols:
+ +[LNFeatureFlags isSideEffectConfirmationSPIEnabled]
+ +[LNFeatureFlags isSnippetContentLayersEnabled]
+ +[LNFeatureFlags resetSideEffectConfirmationSPIOverride]
+ +[LNFeatureFlags resetSnippetContentLayersOverride]
+ +[LNFeatureFlags setIsSideEffectConfirmationSPIEnabled:]
+ +[LNFeatureFlags setIsSnippetContentLayersEnabled:]
+ -[LNActionExecutor linkUndoManagerToMainAppIfNecessary:undoToken:completionHandler:]
+ -[LNActionExecutorOptions setSideEffectConfirmationDeferredToApp:]
+ -[LNActionExecutorOptions sideEffectConfirmationDeferredToApp]
+ -[LNMetadataProvider bundlesWithSkillsWithError:]
+ -[LNMetadataProvider skillForBundleIdentifier:skillName:error:]
+ -[LNMetadataProvider skillsForBundleIdentifier:error:]
+ -[LNPerformActionConnectionOperation actionGrantingColorBundleAccessToRecipient]
+ -[LNSnippetEnvironment initWithSize:locale:dynamicTypeSize:legibilityWeight:layoutDirection:colorScheme:colorSchemeContrast:displayScale:displayGamut:accessibilityDifferentiateWithoutColor:accessibilityInvertColors:accessibilityReduceMotion:accessibilityReduceTransparency:supportsContentLayers:]
+ -[LNSnippetEnvironment supportsContentLayers]
+ -[LNSpotlightCascadeTranslator createMessageAttributesFromAttributeSet:options:error:]
+ -[LNSpotlightCascadeTranslator createSpotlightDefinedAttributesFromAttributeSet:options:error:]
+ -[LNSpotlightCascadeTranslator translateSpotlightPersonWithAttributeKey:fromAttributeSet:options:error:]
+ GCC_except_table1006
+ GCC_except_table1074
+ GCC_except_table1076
+ GCC_except_table1087
+ GCC_except_table1090
+ GCC_except_table1097
+ GCC_except_table1123
+ GCC_except_table1141
+ GCC_except_table1142
+ GCC_except_table1143
+ GCC_except_table1171
+ GCC_except_table1178
+ GCC_except_table1181
+ GCC_except_table1206
+ GCC_except_table1207
+ GCC_except_table1208
+ GCC_except_table1215
+ GCC_except_table1230
+ GCC_except_table1237
+ GCC_except_table1243
+ GCC_except_table1267
+ GCC_except_table1273
+ GCC_except_table1275
+ GCC_except_table1284
+ GCC_except_table1293
+ GCC_except_table1294
+ GCC_except_table1295
+ GCC_except_table1296
+ GCC_except_table1311
+ GCC_except_table1331
+ GCC_except_table1340
+ GCC_except_table1345
+ GCC_except_table1355
+ GCC_except_table1367
+ GCC_except_table1394
+ GCC_except_table1576
+ GCC_except_table1688
+ GCC_except_table1699
+ GCC_except_table1721
+ GCC_except_table1732
+ GCC_except_table1748
+ GCC_except_table1750
+ GCC_except_table1756
+ GCC_except_table1762
+ GCC_except_table1763
+ GCC_except_table1901
+ GCC_except_table1922
+ GCC_except_table1933
+ GCC_except_table1942
+ GCC_except_table1960
+ GCC_except_table1982
+ GCC_except_table1994
+ GCC_except_table2010
+ GCC_except_table2070
+ GCC_except_table2101
+ GCC_except_table2107
+ GCC_except_table2109
+ GCC_except_table2111
+ GCC_except_table2123
+ GCC_except_table2135
+ GCC_except_table2147
+ GCC_except_table2159
+ GCC_except_table2175
+ GCC_except_table2186
+ GCC_except_table2198
+ GCC_except_table2210
+ GCC_except_table2222
+ GCC_except_table2232
+ GCC_except_table2246
+ GCC_except_table2256
+ GCC_except_table2268
+ GCC_except_table2295
+ GCC_except_table2309
+ GCC_except_table2320
+ GCC_except_table2332
+ GCC_except_table2346
+ GCC_except_table2347
+ GCC_except_table2358
+ GCC_except_table2359
+ GCC_except_table2370
+ GCC_except_table2661
+ GCC_except_table3129
+ GCC_except_table3184
+ GCC_except_table3280
+ GCC_except_table3292
+ GCC_except_table3342
+ GCC_except_table3347
+ GCC_except_table3351
+ GCC_except_table3364
+ GCC_except_table3388
+ GCC_except_table3392
+ GCC_except_table3529
+ GCC_except_table3544
+ GCC_except_table587
+ GCC_except_table596
+ GCC_except_table600
+ GCC_except_table608
+ GCC_except_table609
+ GCC_except_table614
+ GCC_except_table618
+ GCC_except_table623
+ GCC_except_table624
+ GCC_except_table628
+ GCC_except_table633
+ GCC_except_table641
+ GCC_except_table642
+ GCC_except_table646
+ GCC_except_table647
+ GCC_except_table651
+ GCC_except_table656
+ GCC_except_table661
+ GCC_except_table666
+ GCC_except_table671
+ GCC_except_table676
+ GCC_except_table685
+ GCC_except_table708
+ GCC_except_table720
+ GCC_except_table729
+ GCC_except_table734
+ GCC_except_table747
+ GCC_except_table756
+ GCC_except_table761
+ GCC_except_table766
+ GCC_except_table771
+ GCC_except_table776
+ GCC_except_table781
+ GCC_except_table786
+ GCC_except_table791
+ GCC_except_table796
+ GCC_except_table801
+ GCC_except_table806
+ GCC_except_table811
+ GCC_except_table816
+ GCC_except_table821
+ GCC_except_table826
+ GCC_except_table980
+ GCC_except_table986
+ GCC_except_table988
+ _LNSpotlightAppEntityKeyDisplayRepresentationImageColorization
+ _LNStaticDefaultValueForColor
+ _MDItemMessageRead
+ _NSSelectorFromString
+ _OBJC_CLASS_$_LNColor
+ _OBJC_CLASS_$_LNSkillMetadata
+ _OBJC_IVAR_$_LNActionExecutorOptions._sideEffectConfirmationDeferredToApp
+ _OBJC_IVAR_$_LNSnippetEnvironment._supportsContentLayers
+ ___49-[LNMetadataProvider bundlesWithSkillsWithError:]_block_invoke
+ ___49-[LNMetadataProvider bundlesWithSkillsWithError:]_block_invoke_2
+ ___49-[LNMetadataProvider bundlesWithSkillsWithError:]_block_invoke_3
+ ___49-[LNMetadataProvider bundlesWithSkillsWithError:]_block_invoke_4
+ ___54-[LNMetadataProvider skillsForBundleIdentifier:error:]_block_invoke
+ ___54-[LNMetadataProvider skillsForBundleIdentifier:error:]_block_invoke_2
+ ___54-[LNMetadataProvider skillsForBundleIdentifier:error:]_block_invoke_3
+ ___54-[LNMetadataProvider skillsForBundleIdentifier:error:]_block_invoke_4
+ ___63-[LNMetadataProvider skillForBundleIdentifier:skillName:error:]_block_invoke
+ ___63-[LNMetadataProvider skillForBundleIdentifier:skillName:error:]_block_invoke_2
+ ___63-[LNMetadataProvider skillForBundleIdentifier:skillName:error:]_block_invoke_3
+ ___63-[LNMetadataProvider skillForBundleIdentifier:skillName:error:]_block_invoke_4
+ ___80-[LNPerformActionConnectionOperation actionGrantingColorBundleAccessToRecipient]_block_invoke
+ ___84-[LNActionExecutor linkUndoManagerToMainAppIfNecessary:undoToken:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e37_v24?0"LNSkillMetadata"8"NSError"16lr32l8r40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _actionGrantingColorBundleAccessToRecipient.grantSelector
+ _actionGrantingColorBundleAccessToRecipient.onceToken
+ _isSideEffectConfirmationSPIOverride
+ _isSnippetContentLayersOverride
+ _symbolic SDySSSo8LNEntityCG16hydratedEntities_t
+ _symbolic So20LNSnippetEnvironmentCSg
- +[LNIntentEnablement disabledWithReason:]
- +[LNIntentEnablement enabled]
- +[LNIntentEnablement supportsSecureCoding]
- -[LNActionExecutor linkUndoManagerToMainAppIfNecessary:completionHandler:]
- -[LNFetchAppIntentStateConnectionOperation .cxx_destruct]
- -[LNFetchAppIntentStateConnectionOperation appIntentIdentifiers]
- -[LNFetchAppIntentStateConnectionOperation completionHandler]
- -[LNFetchAppIntentStateConnectionOperation finishWithError:]
- -[LNFetchAppIntentStateConnectionOperation initWithConnectionInterface:appIntentIdentifiers:queue:completionHandler:]
- -[LNFetchAppIntentStateConnectionOperation results]
- -[LNFetchAppIntentStateConnectionOperation setAppIntentIdentifiers:]
- -[LNFetchAppIntentStateConnectionOperation setCompletionHandler:]
- -[LNFetchAppIntentStateConnectionOperation setResults:]
- -[LNFetchAppIntentStateConnectionOperation start]
- -[LNIntentEnablement .cxx_destruct]
- -[LNIntentEnablement copyWithZone:]
- -[LNIntentEnablement description]
- -[LNIntentEnablement disabledReason]
- -[LNIntentEnablement encodeWithCoder:]
- -[LNIntentEnablement hash]
- -[LNIntentEnablement initWithCoder:]
- -[LNIntentEnablement initWithValue:disabledReason:]
- -[LNIntentEnablement isEqual:]
- -[LNIntentEnablement value]
- -[LNSpotlightCascadeTranslator createMessageAttributesFromAttributeSet:error:]
- -[LNSpotlightCascadeTranslator createSpotlightDefinedAttributesFromAttributeSet:error:]
- -[LNSpotlightCascadeTranslator translateSpotlightPersonWithAttributeKey:fromAttributeSet:error:]
- GCC_except_table1002
- GCC_except_table1068
- GCC_except_table1070
- GCC_except_table1082
- GCC_except_table1083
- GCC_except_table1093
- GCC_except_table1119
- GCC_except_table1135
- GCC_except_table1137
- GCC_except_table1138
- GCC_except_table1167
- GCC_except_table1170
- GCC_except_table1177
- GCC_except_table1202
- GCC_except_table1203
- GCC_except_table1204
- GCC_except_table1211
- GCC_except_table1222
- GCC_except_table1233
- GCC_except_table1239
- GCC_except_table1263
- GCC_except_table1269
- GCC_except_table1271
- GCC_except_table1280
- GCC_except_table1289
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1292
- GCC_except_table1307
- GCC_except_table1327
- GCC_except_table1336
- GCC_except_table1341
- GCC_except_table1351
- GCC_except_table1363
- GCC_except_table1386
- GCC_except_table1572
- GCC_except_table1684
- GCC_except_table1695
- GCC_except_table1717
- GCC_except_table1728
- GCC_except_table1744
- GCC_except_table1746
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1758
- GCC_except_table1895
- GCC_except_table1916
- GCC_except_table1927
- GCC_except_table1936
- GCC_except_table1954
- GCC_except_table1976
- GCC_except_table1988
- GCC_except_table2004
- GCC_except_table2060
- GCC_except_table2096
- GCC_except_table2102
- GCC_except_table2104
- GCC_except_table2106
- GCC_except_table2118
- GCC_except_table2130
- GCC_except_table2142
- GCC_except_table2154
- GCC_except_table2166
- GCC_except_table2182
- GCC_except_table2193
- GCC_except_table2205
- GCC_except_table2217
- GCC_except_table2229
- GCC_except_table2239
- GCC_except_table2253
- GCC_except_table2263
- GCC_except_table2275
- GCC_except_table2300
- GCC_except_table2314
- GCC_except_table2325
- GCC_except_table2337
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2363
- GCC_except_table2364
- GCC_except_table2375
- GCC_except_table2664
- GCC_except_table3135
- GCC_except_table3187
- GCC_except_table3283
- GCC_except_table3295
- GCC_except_table3345
- GCC_except_table3350
- GCC_except_table3354
- GCC_except_table3367
- GCC_except_table3391
- GCC_except_table3395
- GCC_except_table3526
- GCC_except_table3541
- GCC_except_table585
- GCC_except_table607
- GCC_except_table611
- GCC_except_table620
- GCC_except_table625
- GCC_except_table630
- GCC_except_table635
- GCC_except_table639
- GCC_except_table640
- GCC_except_table644
- GCC_except_table645
- GCC_except_table653
- GCC_except_table658
- GCC_except_table662
- GCC_except_table663
- GCC_except_table667
- GCC_except_table668
- GCC_except_table672
- GCC_except_table677
- GCC_except_table704
- GCC_except_table716
- GCC_except_table725
- GCC_except_table730
- GCC_except_table735
- GCC_except_table744
- GCC_except_table749
- GCC_except_table758
- GCC_except_table763
- GCC_except_table772
- GCC_except_table773
- GCC_except_table782
- GCC_except_table783
- GCC_except_table788
- GCC_except_table793
- GCC_except_table798
- GCC_except_table807
- GCC_except_table812
- GCC_except_table817
- GCC_except_table822
- GCC_except_table976
- GCC_except_table982
- GCC_except_table984
- _OBJC_CLASS_$_LNFetchAppIntentStateConnectionOperation
- _OBJC_CLASS_$_LNIntentEnablement
- _OBJC_IVAR_$_LNFetchAppIntentStateConnectionOperation._appIntentIdentifiers
- _OBJC_IVAR_$_LNFetchAppIntentStateConnectionOperation._completionHandler
- _OBJC_IVAR_$_LNFetchAppIntentStateConnectionOperation._results
- _OBJC_IVAR_$_LNIntentEnablement._disabledReason
- _OBJC_IVAR_$_LNIntentEnablement._value
- _OBJC_METACLASS_$_LNFetchAppIntentStateConnectionOperation
- _OBJC_METACLASS_$_LNIntentEnablement
- __OBJC_$_CLASS_METHODS_LNIntentEnablement
- __OBJC_$_CLASS_PROP_LIST_LNIntentEnablement
- __OBJC_$_INSTANCE_METHODS_LNFetchAppIntentStateConnectionOperation
- __OBJC_$_INSTANCE_METHODS_LNIntentEnablement
- __OBJC_$_INSTANCE_VARIABLES_LNFetchAppIntentStateConnectionOperation
- __OBJC_$_INSTANCE_VARIABLES_LNIntentEnablement
- __OBJC_$_PROP_LIST_LNFetchAppIntentStateConnectionOperation
- __OBJC_$_PROP_LIST_LNIntentEnablement
- __OBJC_CLASS_PROTOCOLS_$_LNIntentEnablement
- __OBJC_CLASS_RO_$_LNFetchAppIntentStateConnectionOperation
- __OBJC_CLASS_RO_$_LNIntentEnablement
- __OBJC_METACLASS_RO_$_LNFetchAppIntentStateConnectionOperation
- __OBJC_METACLASS_RO_$_LNIntentEnablement
- ___117-[LNFetchAppIntentStateConnectionOperation initWithConnectionInterface:appIntentIdentifiers:queue:completionHandler:]_block_invoke
- ___49-[LNFetchAppIntentStateConnectionOperation start]_block_invoke
- ___74-[LNActionExecutor linkUndoManagerToMainAppIfNecessary:completionHandler:]_block_invoke
- ___89-[LNConnection(FetchAppIntentState) fetchStateForAppIntentIdentifiers:completionHandler:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
CStrings:
+ "-[LNMetadataProvider bundlesWithSkillsWithError:]_block_invoke"
+ "-[LNMetadataProvider skillForBundleIdentifier:skillName:error:]_block_invoke"
+ "-[LNMetadataProvider skillsForBundleIdentifier:error:]_block_invoke"
+ "Granted bundle access for %lu color parameter(s) of `%{public}@`"
+ "Pre-confirmation for action %{public}s: metadataBundleIdentifier=%{public}s sourceBundleIdentifier=%{public}s"
+ "Pre-confirmation hydration incomplete for action %{public}s: %{public}ld of %{public}ld entity parameter(s) unresolved (%{public}s)"
+ "Pre-confirmation: deferring to the app's confirmation closure"
+ "Pre-confirmation: deferring to the confirmation closure of action %{public}s in the app"
+ "Pre-confirmation: skipping shared-entity confirmation for action %{public}s without full hydration. Reasons: %{public}s"
+ "Side Effect Confirmation SPI"
+ "Snippet Content Layers"
+ "_kMDItemAppEntityDisplayRepresentationImageColorization"
+ "appintents:fetch bundles with skills"
+ "appintents:fetch skill for bundle"
+ "appintents:fetch skills for bundle"
+ "deferToApp"
+ "ln_valueGrantingColorBundleAccessToRecipient:"
+ "sideEffectConfirmationDeferredToApp"
+ "sideEffectConfirmationSPI"
+ "snippetContentLayers"
+ "softlink:o:path:/System/Library/Frameworks/AppIntents.framework/AppIntents"
+ "supportsContentLayers"
+ "v24@?0@\"LNSkillMetadata\"8@\"NSError\"16"
- "<%@: %p, value: %ld, disabledReason: %@>"
- "Conditionally Enabled Intents"
- "Fetching intent state"
- "LNFetchAppIntentStateConnectionOperation.m"
- "Pre-confirmation hydration incomplete for action %{public}s: %{public}ld of %{public}ld entity parameter(s) unresolved (%{public}s); confirming with the generic dialog"
- "appIntentIdentifiers"
- "appintents:fetch intent state"
- "conditionallyEnabledIntents"
- "disabledReason"
```
