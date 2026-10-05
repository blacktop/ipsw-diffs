## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2465.1.3.0.0
-  __TEXT.__text: 0xc3a00
-  __TEXT.__objc_methlist: 0x4c84
+2465.1.7.0.0
+  __TEXT.__text: 0xc7ab4
+  __TEXT.__objc_methlist: 0x4e04
   __TEXT.__const: 0x410
-  __TEXT.__cstring: 0x9c86
-  __TEXT.__gcc_except_tab: 0x48e4
-  __TEXT.__oslogstring: 0xd4dc
-  __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x3508
+  __TEXT.__cstring: 0x9e7f
+  __TEXT.__gcc_except_tab: 0x4a80
+  __TEXT.__oslogstring: 0xd686
+  __TEXT.__dlopen_cstrs: 0xf4
+  __TEXT.__unwind_info: 0x3618
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4810
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__const: 0x4980
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d88
+  __DATA_CONST.__objc_selrefs: 0x3ee0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x148
-  __DATA_CONST.__objc_arraydata: 0x310
-  __DATA_CONST.__got: 0xc10
-  __AUTH_CONST.__const: 0x13a8
-  __AUTH_CONST.__cfstring: 0x8200
-  __AUTH_CONST.__objc_const: 0x63a8
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_arraydata: 0x318
+  __DATA_CONST.__got: 0xc38
+  __AUTH_CONST.__const: 0x13e8
+  __AUTH_CONST.__cfstring: 0x8240
+  __AUTH_CONST.__objc_const: 0x6540
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
+  __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1130
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x558
+  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x56c
   __DATA.__data: 0x410
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x738
+  __DATA_DIRTY.__bss: 0x750
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3413
-  Symbols:   5119
-  CStrings:  2739
+  Functions: 3469
+  Symbols:   5209
+  CStrings:  2762
 
Symbols:
+ -[CSBundleFilterEscalatedIdentifiers .cxx_destruct]
+ -[CSBundleFilterEscalatedIdentifiers excludedAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers fileProviderExcludedBundleIDs]
+ -[CSBundleFilterEscalatedIdentifiers hiddenAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers initWithLockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:mdmRestrictedBundleIdentifiers:excludedAppBundleIdentifiers:fileProviderExcludedBundleIDs:]
+ -[CSBundleFilterEscalatedIdentifiers lockedAppBundleIdentifiers]
+ -[CSBundleFilterEscalatedIdentifiers mdmRestrictedBundleIdentifiers]
+ -[MDSearchableIndexService _decodeAttributeBackfillResultForGroup:plistBytes:]
+ -[MDSearchableIndexService _decodeBundleFilterEvaluationRequest:error:]
+ -[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]
+ -[MDSearchableIndexService _mergeFileProviderExcludedBundleIDsForRequest:lockedAppBundleIdentifiers:hiddenAppBundleIdentifiers:excludedAppBundleIdentifiers:]
+ -[MDSearchableIndexService _rejectIfDisallowedBundleID:]
+ -[MDSearchableIndexService _rejectIfNotInternal:reason:]
+ -[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]
+ -[MDSearchableIndexService _resolveEscalatedIdentifiersForRequest:]
+ -[MDSearchableIndexService _resolveExcludedAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]
+ -[MDSearchableIndexService _resolveHiddenAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveLockedAppBundleIdentifiers]
+ -[MDSearchableIndexService _resolveMDMRestrictedBundleIdentifiers]
+ -[MDSearchableIndexService _sendBundleFilterEvaluationReply:overConnection:indexID:evaluationReply:attributeBackfillResults:evaluationError:escalated:]
+ -[MDSearchableIndexService _validateAttributeBackfillGroup:]
+ -[MDSearchableIndexService _validateAttributeBackfillGroupsInRequest:]
+ -[MDSearchableIndexService _validateBundleFilterEvaluationRequest:]
+ -[MDSearchableIndexService _validateFileProviderContainerGroup:]
+ -[MDSearchableIndexService _validateFileProviderContainerGroupsInRequest:]
+ -[MDSearchableIndexService evaluateFilters:]
+ -[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer _oidPath:containsAnyOID:]
+ -[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]
+ GCC_except_table1004
+ GCC_except_table102
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table104
+ GCC_except_table1043
+ GCC_except_table1059
+ GCC_except_table1105
+ GCC_except_table1156
+ GCC_except_table1190
+ GCC_except_table1196
+ GCC_except_table1197
+ GCC_except_table1203
+ GCC_except_table1204
+ GCC_except_table1205
+ GCC_except_table1206
+ GCC_except_table1215
+ GCC_except_table1217
+ GCC_except_table1232
+ GCC_except_table1238
+ GCC_except_table1242
+ GCC_except_table1256
+ GCC_except_table127
+ GCC_except_table1272
+ GCC_except_table1279
+ GCC_except_table128
+ GCC_except_table1286
+ GCC_except_table129
+ GCC_except_table1293
+ GCC_except_table1300
+ GCC_except_table131
+ GCC_except_table1317
+ GCC_except_table1395
+ GCC_except_table1396
+ GCC_except_table1398
+ GCC_except_table1405
+ GCC_except_table1468
+ GCC_except_table1475
+ GCC_except_table1602
+ GCC_except_table1603
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table70
+ GCC_except_table743
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table770
+ GCC_except_table796
+ GCC_except_table862
+ GCC_except_table87
+ GCC_except_table886
+ GCC_except_table908
+ GCC_except_table912
+ GCC_except_table916
+ GCC_except_table944
+ GCC_except_table973
+ _MDItemEventSourceBundleIdentifier
+ _OBJC_CLASS_$_CSBundleFilterAttributeBackfillResult
+ _OBJC_CLASS_$_CSBundleFilterEscalatedIdentifiers
+ _OBJC_CLASS_$_CSBundleFilterEvaluationReply
+ _OBJC_CLASS_$_CSBundleFilterEvaluationRequest
+ _OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._excludedAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._fileProviderExcludedBundleIDs
+ _OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._hiddenAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._lockedAppBundleIdentifiers
+ _OBJC_IVAR_$_CSBundleFilterEscalatedIdentifiers._mdmRestrictedBundleIdentifiers
+ _OBJC_METACLASS_$_CSBundleFilterEscalatedIdentifiers
+ _SPBundleFilterAllowedAttributeBackfillAttributeNames.onceToken
+ _SPBundleFilterAllowedAttributeBackfillAttributeNames.sAllowed
+ _SpotlightServicesLibraryCore.frameworkLibrary
+ __MDPlistContainerAllocFailure
+ __OBJC_$_INSTANCE_METHODS_CSBundleFilterEscalatedIdentifiers
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleFilterEscalatedIdentifiers
+ __OBJC_$_PROP_LIST_CSBundleFilterEscalatedIdentifiers
+ __OBJC_CLASS_RO_$_CSBundleFilterEscalatedIdentifiers
+ __OBJC_METACLASS_RO_$_CSBundleFilterEscalatedIdentifiers
+ ___101-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]_block_invoke
+ ___101-[MDSearchableIndexService _evaluateFileProviderContainerGroups:excludedBundleIDs:completionHandler:]_block_invoke_2
+ ___107-[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]_block_invoke
+ ___107-[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]_block_invoke_2
+ ___107-[MDSearchableIndexService _resolveFileProviderAndAttributeBackfillForRequest:escalated:completionHandler:]_block_invoke_3
+ ___137-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke
+ ___137-[SPCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke_2
+ ___145-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke
+ ___145-[SPConcreteCoreSpotlightIndexer _matchFileProviderContainerExclusionsForBundleID:identifiers:knownOIDPaths:excludedBundleIDs:completionHandler:]_block_invoke_2
+ ___44-[MDSearchableIndexService evaluateFilters:]_block_invoke
+ ___58-[SPConcreteCoreSpotlightIndexer _oidPath:containsAnyOID:]_block_invoke
+ ___88-[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]_block_invoke
+ ___88-[MDSearchableIndexService _resolveAttributeBackfillResultsForGroups:completionHandler:]_block_invoke_2
+ ___SPBundleFilterAllowedAttributeBackfillAttributeNames_block_invoke
+ ___SpotlightServicesLibraryCore_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s_e63_v32?0"CSBundleFilterEvaluationReply"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e51_v24?0"CSBundleFilterEvaluationReply"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e20_v24?08"NSError"16ls32l8s40l8r64l8r72l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e41_v32?0"NSArray"8"NSArray"16"NSError"24lr64l8r72l8s32l8s40l8s48l8s56l8
+ ___getSSCopyExcludedAppBundleIDsFromPreferencesCacheSymbolLoc_block_invoke
+ __oidPath:containsAnyOID:.nonDigits
+ __oidPath:containsAnyOID:.onceToken
+ _audit_stringSpotlightServices
+ _getSSCopyExcludedAppBundleIDsFromPreferencesCacheSymbolLoc.ptr
- GCC_except_table1028
- GCC_except_table1029
- GCC_except_table1038
- GCC_except_table105
- GCC_except_table1054
- GCC_except_table108
- GCC_except_table1095
- GCC_except_table113
- GCC_except_table114
- GCC_except_table1151
- GCC_except_table1185
- GCC_except_table1191
- GCC_except_table1192
- GCC_except_table1198
- GCC_except_table1199
- GCC_except_table1200
- GCC_except_table1201
- GCC_except_table1210
- GCC_except_table1212
- GCC_except_table1227
- GCC_except_table123
- GCC_except_table1233
- GCC_except_table1237
- GCC_except_table124
- GCC_except_table125
- GCC_except_table1251
- GCC_except_table1267
- GCC_except_table1274
- GCC_except_table1281
- GCC_except_table1288
- GCC_except_table1295
- GCC_except_table1312
- GCC_except_table134
- GCC_except_table135
- GCC_except_table136
- GCC_except_table138
- GCC_except_table1390
- GCC_except_table1391
- GCC_except_table1393
- GCC_except_table1400
- GCC_except_table1460
- GCC_except_table1467
- GCC_except_table150
- GCC_except_table151
- GCC_except_table152
- GCC_except_table153
- GCC_except_table154
- GCC_except_table155
- GCC_except_table156
- GCC_except_table157
- GCC_except_table158
- GCC_except_table1594
- GCC_except_table1595
- GCC_except_table161
- GCC_except_table162
- GCC_except_table163
- GCC_except_table165
- GCC_except_table166
- GCC_except_table738
- GCC_except_table763
- GCC_except_table764
- GCC_except_table765
- GCC_except_table791
- GCC_except_table857
- GCC_except_table881
- GCC_except_table903
- GCC_except_table907
- GCC_except_table911
- GCC_except_table939
- GCC_except_table968
- GCC_except_table999
CStrings:
+ "#apphistory dropping action for %@: attribute set encoding was abandoned"
+ "-[MDSearchableIndexService evaluateFilters:]"
+ "0123456789"
+ "AppProtection bundle IDs"
+ "Attempt to access Mail by client %@"
+ "Excluded Apps bundle IDs"
+ "MDM-restricted bundle IDs"
+ "Non-internal client %@ requested %s"
+ "Re-serializing %lu donated items after collaboration lookup was refused by the plist builder (nesting too deep?); indexing them without the collaboration attributes"
+ "SSCopyExcludedAppBundleIDsFromPreferencesCache"
+ "_kMDItemOIDPath"
+ "attribute backfill"
+ "cross-bundle exclusion match"
+ "evaluate-filters-data"
+ "evaluate-filters-data-size"
+ "evaluate_filters"
+ "failed to encode bundle filter evaluation reply %@"
+ "fetchAttributes has no index for protectionClass:%@, bundleID:%@"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices"
+ "v24@?0@\"CSBundleFilterEvaluationReply\"8@\"NSError\"16"
+ "v32@?0@\"CSBundleFilterEvaluationReply\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
```
