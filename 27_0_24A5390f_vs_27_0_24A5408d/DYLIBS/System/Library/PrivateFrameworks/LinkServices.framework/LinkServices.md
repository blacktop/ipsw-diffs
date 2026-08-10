## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-301.0.45.4.101
-  __TEXT.__text: 0x161ca8
-  __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0xaddc
+301.0.51.1.102
+  __TEXT.__text: 0x163af0
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_methlist: 0xae84
   __TEXT.__dlopen_cstrs: 0x565
-  __TEXT.__const: 0x8898
-  __TEXT.__constg_swiftt: 0x207c
-  __TEXT.__swift5_typeref: 0x3250
+  __TEXT.__const: 0x8928
+  __TEXT.__constg_swiftt: 0x20d4
+  __TEXT.__swift5_typeref: 0x32ac
   __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x1001
-  __TEXT.__swift5_fieldmd: 0x1664
+  __TEXT.__swift5_reflstr: 0x1071
+  __TEXT.__swift5_fieldmd: 0x16b4
   __TEXT.__swift5_assocty: 0x460
-  __TEXT.__swift5_capture: 0x15b8
-  __TEXT.__cstring: 0xc1b3
-  __TEXT.__swift5_proto: 0x370
-  __TEXT.__swift5_types: 0x1f8
-  __TEXT.__swift5_protos: 0x64
-  __TEXT.__oslogstring: 0x799e
-  __TEXT.__swift_as_entry: 0x100
+  __TEXT.__swift5_capture: 0x15ec
+  __TEXT.__cstring: 0xc357
+  __TEXT.__swift5_proto: 0x378
+  __TEXT.__swift5_types: 0x1fc
+  __TEXT.__swift5_protos: 0x68
+  __TEXT.__oslogstring: 0x7ad7
+  __TEXT.__swift_as_entry: 0x104
   __TEXT.__swift_as_ret: 0x120
-  __TEXT.__swift_as_cont: 0x198
+  __TEXT.__swift_as_cont: 0x19c
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__gcc_except_tab: 0x2064
-  __TEXT.__unwind_info: 0x6ba8
-  __TEXT.__eh_frame: 0x7870
+  __TEXT.__gcc_except_tab: 0x206c
+  __TEXT.__unwind_info: 0x6c28
+  __TEXT.__eh_frame: 0x78b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27e0
-  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__const: 0x27e8
+  __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5010
+  __DATA_CONST.__objc_selrefs: 0x5068
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x1898
-  __AUTH_CONST.__const: 0x7960
-  __AUTH_CONST.__cfstring: 0x8680
-  __AUTH_CONST.__objc_const: 0x16628
-  __AUTH_CONST.__lazy_load_got: 0x8
+  __DATA_CONST.__got: 0x18a0
+  __AUTH_CONST.__const: 0x7a98
+  __AUTH_CONST.__cfstring: 0x8780
+  __AUTH_CONST.__objc_const: 0x16748
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x16d0
-  __AUTH.__objc_data: 0x39a8
-  __AUTH.__data: 0x1650
-  __DATA.__objc_ivar: 0xae0
-  __DATA.__data: 0x31e0
-  __DATA.__bss: 0x4de8
+  __AUTH_CONST.__auth_got: 0x1700
+  __AUTH.__objc_data: 0x39f0
+  __AUTH.__data: 0x1660
+  __DATA.__objc_ivar: 0xaec
+  __DATA.__data: 0x31f4
+  __DATA.__bss: 0x4e68
   __DATA.__common: 0x658
   __DATA_DIRTY.__objc_data: 0x1fa0
   __DATA_DIRTY.__data: 0x328

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10347
-  Symbols:   11473
-  CStrings:  2098
+  Functions: 10399
+  Symbols:   11521
+  CStrings:  2116
 
Symbols:
+ -[LNActionExecutorMetrics executorPerformDurationNS]
+ -[LNActionExecutorMetrics setExecutorPerformDurationNS:]
+ -[LNConnection connectUsingProcessIdentifierWithOptions:fallbackHandler:]
+ -[LNConnectionManager _setRestrictionObservationActive:]
+ -[LNRuntimeAssertionsTakingConnectionOperation initWithIdentifier:connectionInterface:systemProtocols:assistantDefinedSchemas:priority:queue:activity:]
+ -[NSDictionary(LNAttributeSet) attributeIsDelete:]
+ -[_LNPatchAttributeSet .cxx_destruct]
+ -[_LNPatchAttributeSet attributeForKey:]
+ -[_LNPatchAttributeSet attributeIsDelete:]
+ -[_LNPatchAttributeSet filteredCustomAttributes]
+ -[_LNPatchAttributeSet initWithAttributeSet:]
+ GCC_except_table1001
+ GCC_except_table1007
+ GCC_except_table1009
+ GCC_except_table1027
+ GCC_except_table1091
+ GCC_except_table1093
+ GCC_except_table1095
+ GCC_except_table1105
+ GCC_except_table1106
+ GCC_except_table1116
+ GCC_except_table1141
+ GCC_except_table1157
+ GCC_except_table1159
+ GCC_except_table1160
+ GCC_except_table1161
+ GCC_except_table1196
+ GCC_except_table1199
+ GCC_except_table1221
+ GCC_except_table1222
+ GCC_except_table1230
+ GCC_except_table1241
+ GCC_except_table1252
+ GCC_except_table1258
+ GCC_except_table1269
+ GCC_except_table1270
+ GCC_except_table1271
+ GCC_except_table1272
+ GCC_except_table1287
+ GCC_except_table1307
+ GCC_except_table1319
+ GCC_except_table1342
+ GCC_except_table1346
+ GCC_except_table1517
+ GCC_except_table1621
+ GCC_except_table1632
+ GCC_except_table1664
+ GCC_except_table1667
+ GCC_except_table1669
+ GCC_except_table1682
+ GCC_except_table1683
+ GCC_except_table1815
+ GCC_except_table1836
+ GCC_except_table1847
+ GCC_except_table1856
+ GCC_except_table1874
+ GCC_except_table1908
+ GCC_except_table1924
+ GCC_except_table1982
+ GCC_except_table1987
+ GCC_except_table2014
+ GCC_except_table2020
+ GCC_except_table2022
+ GCC_except_table2084
+ GCC_except_table2112
+ GCC_except_table2159
+ GCC_except_table2169
+ GCC_except_table2183
+ GCC_except_table2205
+ GCC_except_table2230
+ GCC_except_table2244
+ GCC_except_table2255
+ GCC_except_table2266
+ GCC_except_table2293
+ GCC_except_table2304
+ GCC_except_table2591
+ GCC_except_table3044
+ GCC_except_table3047
+ GCC_except_table3097
+ GCC_except_table3205
+ GCC_except_table3255
+ GCC_except_table3260
+ GCC_except_table3264
+ GCC_except_table3277
+ GCC_except_table3295
+ GCC_except_table3300
+ GCC_except_table3309
+ GCC_except_table3313
+ GCC_except_table3428
+ GCC_except_table3443
+ GCC_except_table348
+ GCC_except_table368
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table424
+ GCC_except_table593
+ GCC_except_table616
+ GCC_except_table621
+ GCC_except_table632
+ GCC_except_table643
+ GCC_except_table647
+ GCC_except_table651
+ GCC_except_table662
+ GCC_except_table666
+ GCC_except_table670
+ GCC_except_table674
+ GCC_except_table678
+ GCC_except_table682
+ GCC_except_table693
+ GCC_except_table697
+ GCC_except_table701
+ GCC_except_table705
+ GCC_except_table709
+ GCC_except_table713
+ GCC_except_table717
+ GCC_except_table721
+ GCC_except_table725
+ GCC_except_table729
+ GCC_except_table733
+ GCC_except_table737
+ GCC_except_table741
+ GCC_except_table745
+ GCC_except_table749
+ GCC_except_table753
+ GCC_except_table757
+ GCC_except_table761
+ GCC_except_table765
+ GCC_except_table769
+ GCC_except_table778
+ GCC_except_table780
+ GCC_except_table784
+ GCC_except_table793
+ GCC_except_table795
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table803
+ GCC_except_table807
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table837
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table843
+ GCC_except_table845
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table851
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table859
+ GCC_except_table861
+ GCC_except_table863
+ GCC_except_table865
+ GCC_except_table867
+ GCC_except_table869
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_CLASS_$_TUCallCenter$lazyGOT
+ _OBJC_CLASS_$_TUCallCenter$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$__LNPatchAttributeSet
+ _OBJC_IVAR_$_LNActionExecutor._executorPerformStartMachTime
+ _OBJC_IVAR_$_LNActionExecutorMetrics._executorPerformDurationNS
+ _OBJC_IVAR_$_LNConnectionManager._restrictionObservationQueue
+ _OBJC_IVAR_$__LNPatchAttributeSet._underlyingSet
+ _OBJC_METACLASS_$__LNPatchAttributeSet
+ __OBJC_$_INSTANCE_METHODS__LNPatchAttributeSet
+ __OBJC_$_INSTANCE_VARIABLES__LNPatchAttributeSet
+ __OBJC_CLASS_PROTOCOLS_$__LNPatchAttributeSet
+ __OBJC_CLASS_RO_$__LNPatchAttributeSet
+ __OBJC_METACLASS_RO_$__LNPatchAttributeSet
+ ___44-[LNExtensionConnection connectWithOptions:]_block_invoke
+ ___54-[LNEmbeddedApplicationConnection connectWithOptions:]_block_invoke_3
+ ___56-[LNConnectionManager _setRestrictionObservationActive:]_block_invoke
+ ___73-[LNConnection connectUsingProcessIdentifierWithOptions:fallbackHandler:]_block_invoke
+ ___89-[LNSpotlightCascadeTranslator createItemRepresentationAttributesFromAttributeSet:error:]_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ ___swift_memcpy56_8
+ _dynamic_cast_existential_1_conditional
+ _lazyLoadFlag$TelephonyUtilities
+ _memcmp
+ _objc_msgSend$_setRestrictionObservationActive:
+ _objc_msgSend$attributeIsDelete:
+ _objc_msgSend$beginObservingOperationRestrictions
+ _objc_msgSend$callingProtocol
+ _objc_msgSend$connectUsingProcessIdentifierWithOptions:fallbackHandler:
+ _objc_msgSend$donateUserIntentForProviderWithIdentifier:
+ _objc_msgSend$endObservingOperationRestrictions
+ _objc_msgSend$enumerateValuesOfValueType:value:block:
+ _objc_msgSend$executorPerformDurationNS
+ _objc_msgSend$initWithAttributeSet:
+ _objc_msgSend$providerManager
+ _objc_msgSend$resolveEffectiveBundleIdentifiers:allowedTargets:appBundleIdentifier:extensionBundleIdentifier:daemonBundleIdentifier:frameworkBundleIdentifier:signals:identifier:
+ _objc_msgSend$setExecutorPerformDurationNS:
+ _swift_conformsToProtocol2
+ _swift_release_x3
+ _swift_release_x9
+ _swift_retain_x8
+ _symbolic $s12LinkServices32LNConnectionRestrictionObservingP
+ _symbolic So15NSXPCConnectionCSg
+ _symbolic _____ 12LinkServices22LNPerformActionMetricsC6PhasesV
+ _symbolic _____ySuG 15Synchronization5MutexVAARi_zrlE
+ _type_layout_string 12LinkServices22LNPerformActionMetricsC6PhasesV
- -[LNAppIntentConnectionPolicy initializationError]
- -[LNConnection connectUsingProcessIdentifierWithOptions:]
- -[LNRuntimeAssertionsTakingConnectionOperation initWithIdentifier:connectionInterface:systemProtocols:priority:queue:activity:]
- GCC_except_table1000
- GCC_except_table1002
- GCC_except_table1020
- GCC_except_table1084
- GCC_except_table1086
- GCC_except_table1088
- GCC_except_table1098
- GCC_except_table1099
- GCC_except_table1102
- GCC_except_table1134
- GCC_except_table1150
- GCC_except_table1152
- GCC_except_table1153
- GCC_except_table1154
- GCC_except_table1182
- GCC_except_table1185
- GCC_except_table1214
- GCC_except_table1215
- GCC_except_table1216
- GCC_except_table1234
- GCC_except_table1238
- GCC_except_table1250
- GCC_except_table1261
- GCC_except_table1262
- GCC_except_table1263
- GCC_except_table1264
- GCC_except_table1278
- GCC_except_table1298
- GCC_except_table1310
- GCC_except_table1331
- GCC_except_table1335
- GCC_except_table1507
- GCC_except_table1611
- GCC_except_table1622
- GCC_except_table1644
- GCC_except_table1657
- GCC_except_table1659
- GCC_except_table1672
- GCC_except_table1673
- GCC_except_table1803
- GCC_except_table1824
- GCC_except_table1835
- GCC_except_table1844
- GCC_except_table1862
- GCC_except_table1884
- GCC_except_table1912
- GCC_except_table1970
- GCC_except_table1975
- GCC_except_table2002
- GCC_except_table2008
- GCC_except_table2010
- GCC_except_table2012
- GCC_except_table2088
- GCC_except_table2111
- GCC_except_table2157
- GCC_except_table2171
- GCC_except_table2181
- GCC_except_table2218
- GCC_except_table2232
- GCC_except_table2243
- GCC_except_table2254
- GCC_except_table2268
- GCC_except_table2269
- GCC_except_table2579
- GCC_except_table3032
- GCC_except_table3035
- GCC_except_table3085
- GCC_except_table3181
- GCC_except_table3243
- GCC_except_table3248
- GCC_except_table3252
- GCC_except_table3265
- GCC_except_table3283
- GCC_except_table3288
- GCC_except_table3297
- GCC_except_table3301
- GCC_except_table3416
- GCC_except_table342
- GCC_except_table3431
- GCC_except_table352
- GCC_except_table353
- GCC_except_table354
- GCC_except_table355
- GCC_except_table356
- GCC_except_table357
- GCC_except_table417
- GCC_except_table586
- GCC_except_table609
- GCC_except_table614
- GCC_except_table618
- GCC_except_table629
- GCC_except_table633
- GCC_except_table644
- GCC_except_table648
- GCC_except_table659
- GCC_except_table663
- GCC_except_table667
- GCC_except_table671
- GCC_except_table675
- GCC_except_table679
- GCC_except_table683
- GCC_except_table694
- GCC_except_table698
- GCC_except_table702
- GCC_except_table706
- GCC_except_table710
- GCC_except_table714
- GCC_except_table718
- GCC_except_table722
- GCC_except_table726
- GCC_except_table730
- GCC_except_table734
- GCC_except_table738
- GCC_except_table742
- GCC_except_table746
- GCC_except_table750
- GCC_except_table754
- GCC_except_table758
- GCC_except_table762
- GCC_except_table771
- GCC_except_table773
- GCC_except_table777
- GCC_except_table779
- GCC_except_table781
- GCC_except_table783
- GCC_except_table792
- GCC_except_table794
- GCC_except_table796
- GCC_except_table800
- GCC_except_table815
- GCC_except_table824
- GCC_except_table826
- GCC_except_table830
- GCC_except_table832
- GCC_except_table834
- GCC_except_table836
- GCC_except_table838
- GCC_except_table840
- GCC_except_table842
- GCC_except_table844
- GCC_except_table846
- GCC_except_table848
- GCC_except_table850
- GCC_except_table852
- GCC_except_table854
- GCC_except_table856
- GCC_except_table858
- GCC_except_table860
- GCC_except_table862
- GCC_except_table994
- _OBJC_IVAR_$_LNAppIntentConnectionPolicy._initializationError
- ___57-[LNConnection connectUsingProcessIdentifierWithOptions:]_block_invoke
- ___block_descriptor_40_e8_32s_e50_v24?0"LNConnectionListenerEndpoint"8"NSError"16ls32l8
- _objc_msgSend$connectUsingProcessIdentifierWithOptions:
- _objc_msgSend$initializationError
- _objc_msgSend$resolveEffectiveBundleIdentifiers:allowedTargets:appBundleIdentifier:extensionBundleIdentifier:daemonBundleIdentifier:frameworkBundleIdentifier:signals:
CStrings:
+ "\nConnecting Duration: "
+ " ns\nEnd-to-End Latency: "
+ " ns\nExecutor Perform Duration: "
+ "%{public}@ Could not resolve processInstanceIdentifier %{public}@ (%{public}@); falling back to standard routing"
+ "%{public}@ Not falling back for processInstanceIdentifier %{public}@: connection is no longer connecting (state `%{public}@`)"
+ "A"
+ "Action:%@"
+ "Donating CallKit intent for %@"
+ "Entity:%@"
+ "Enum:%@"
+ "Failed to donate CallKit intent for %@"
+ "Policy dictates fallback to extension, but none available for `%@`"
+ "Policy dictates runInExtension=YES, but no app available for `%{public}@`"
+ "Policy dictates runInExtension=YES, but no extension available for `%{public}@`"
+ "Policy dictates shouldExecuteActionOnApplication=YES, but no app available for `%{public}@`"
+ "Query:%@"
+ "StartCallIntent"
+ "Target: %@, connectingNS: %llu, executorPerformNS: %llu, requiredLaunch: %@, didForeground: %@, liveActivity: %@"
+ "com.apple.link.LNConnectionManager.restriction-observation"
+ "com.apple.link.runtimeAssertion.Calling"
+ "com.apple.usernotificationsd"
+ "targetProcessExecutorPerformDuration"
+ "\xb1"
- "%{public}@ Failed to fetch listener endpoint for processInstanceIdentifier %{public}@: %{public}@"
- "%{public}@ No processInstanceIdentifier set, skipping process-based connection"
- "Initialized without an effectiveBundleIdentifier for: %{public}@"
- "Target: %@, bootstrapNS: %llu, requiredLaunch: %@, didForeground: %@, liveActivity: %@"
- "\xa1"
```
