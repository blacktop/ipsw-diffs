## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`

```diff

-301.1.15.0.0
-  __TEXT.__text: 0x146eb4
+301.1.16.0.0
+  __TEXT.__text: 0x147790
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb370
+  __TEXT.__objc_methlist: 0xb3b0
   __TEXT.__dlopen_cstrs: 0x5cd
-  __TEXT.__const: 0x78c8
-  __TEXT.__cstring: 0xc851
+  __TEXT.__const: 0x78d8
   __TEXT.__constg_swiftt: 0x1b40
-  __TEXT.__swift5_typeref: 0x2ec6
+  __TEXT.__swift5_typeref: 0x2efa
   __TEXT.__swift5_builtin: 0x258
   __TEXT.__swift5_reflstr: 0xe7c
   __TEXT.__swift5_fieldmd: 0x11dc
   __TEXT.__swift5_assocty: 0x2b8
-  __TEXT.__swift5_capture: 0x1318
-  __TEXT.__oslogstring: 0xa049
+  __TEXT.__cstring: 0xc975
   __TEXT.__swift5_proto: 0x284
   __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift5_protos: 0x44
+  __TEXT.__swift5_capture: 0x1318
+  __TEXT.__oslogstring: 0xa16e
   __TEXT.__swift_as_entry: 0x11c
   __TEXT.__swift_as_ret: 0x13c
   __TEXT.__swift_as_cont: 0x1d8
-  __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__gcc_except_tab: 0x2060
-  __TEXT.__unwind_info: 0x6b40
+  __TEXT.__gcc_except_tab: 0x208c
+  __TEXT.__unwind_info: 0x6b60
   __TEXT.__eh_frame: 0x4cc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a30
+  __DATA_CONST.__const: 0x2a38
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5518
+  __DATA_CONST.__objc_selrefs: 0x5548
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x19e8
   __AUTH_CONST.__const: 0x64e0
-  __AUTH_CONST.__cfstring: 0x8e80
-  __AUTH_CONST.__objc_const: 0x16fa8
+  __AUTH_CONST.__cfstring: 0x8ee0
+  __AUTH_CONST.__objc_const: 0x16fb0
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__objc_data: 0x3dc8
   __AUTH.__data: 0x1388
   __DATA.__objc_ivar: 0xb10
-  __DATA.__data: 0x296c
+  __DATA.__data: 0x2934
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x2440
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8879
-  Symbols:   9275
-  CStrings:  2273
+  Functions: 8890
+  Symbols:   9290
+  CStrings:  2280
 
Symbols:
+ -[LNActionExecutor connectAndEnqueuePerformWithOptions:]
+ -[LNActionExecutor enqueuePerformReconnectingIfNeededWithConnectionInterface:action:connection:connectionOptions:]
+ -[LNActionExecutor evaluatePreConfirmationForAction:connection:connectionInterface:connectionOptions:]
+ -[LNActionExecutor prepareConnectionInterfaceOrComplete:connection:error:]
+ -[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:connectionOptions:]
+ -[LNActionExecutor subscribeToProgressUpdates]
+ GCC_except_table1744
+ GCC_except_table1746
+ GCC_except_table1751
+ GCC_except_table1755
+ GCC_except_table1758
+ GCC_except_table1759
+ GCC_except_table1895
+ GCC_except_table1916
+ GCC_except_table1927
+ GCC_except_table1936
+ GCC_except_table1954
+ GCC_except_table1976
+ GCC_except_table1988
+ GCC_except_table2004
+ GCC_except_table2060
+ GCC_except_table2065
+ GCC_except_table2102
+ GCC_except_table2104
+ GCC_except_table2106
+ GCC_except_table2118
+ GCC_except_table2130
+ GCC_except_table2142
+ GCC_except_table2154
+ GCC_except_table2166
+ GCC_except_table2182
+ GCC_except_table2193
+ GCC_except_table2205
+ GCC_except_table2217
+ GCC_except_table2229
+ GCC_except_table2239
+ GCC_except_table2253
+ GCC_except_table2263
+ GCC_except_table2275
+ GCC_except_table2300
+ GCC_except_table2314
+ GCC_except_table2325
+ GCC_except_table2337
+ GCC_except_table2351
+ GCC_except_table2352
+ GCC_except_table2363
+ GCC_except_table2364
+ GCC_except_table2375
+ GCC_except_table2664
+ GCC_except_table3132
+ GCC_except_table3135
+ GCC_except_table3187
+ GCC_except_table3283
+ GCC_except_table3295
+ GCC_except_table3345
+ GCC_except_table3350
+ GCC_except_table3354
+ GCC_except_table3367
+ GCC_except_table3391
+ GCC_except_table3395
+ GCC_except_table3526
+ GCC_except_table3541
+ _LNInterfaceIdiomHomeAccessory
+ _LNTVDisplayAttentionStateIsAsleep
+ _LNTVDisplayIsAsleep
+ ___102-[LNActionExecutor evaluatePreConfirmationForAction:connection:connectionInterface:connectionOptions:]_block_invoke
+ ___116-[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:connectionOptions:]_block_invoke
+ ___116-[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:connectionOptions:]_block_invoke_2
+ ___46-[LNActionExecutor subscribeToProgressUpdates]_block_invoke
+ ___46-[LNActionExecutor subscribeToProgressUpdates]_block_invoke_2
+ ___56-[LNActionExecutor connectAndEnqueuePerformWithOptions:]_block_invoke
+ ___block_descriptor_59_e8_32s40s_e79_v40?0"LNConnection"8"LNAction"16"<LNConnectionHostInterface>"24"NSError"32ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e40_v16?0"LNPreConfirmationResultWrapper"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e50_v24?0"LNActionConfirmationResponse"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___swift_closure_destructor.27Tm
+ _symbolic So14LSBundleRecordCSg
+ _symbolic _____ySo14LSBundleRecordCSgG s23_ContiguousArrayStorageC
- -[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:]
- GCC_except_table1742
- GCC_except_table1745
- GCC_except_table1747
- GCC_except_table1753
- GCC_except_table1889
- GCC_except_table1910
- GCC_except_table1921
- GCC_except_table1930
- GCC_except_table1948
- GCC_except_table1970
- GCC_except_table1982
- GCC_except_table1998
- GCC_except_table2054
- GCC_except_table2059
- GCC_except_table2090
- GCC_except_table2098
- GCC_except_table2100
- GCC_except_table2112
- GCC_except_table2124
- GCC_except_table2136
- GCC_except_table2148
- GCC_except_table2160
- GCC_except_table2176
- GCC_except_table2187
- GCC_except_table2199
- GCC_except_table2211
- GCC_except_table2223
- GCC_except_table2233
- GCC_except_table2247
- GCC_except_table2257
- GCC_except_table2269
- GCC_except_table2294
- GCC_except_table2308
- GCC_except_table2319
- GCC_except_table2331
- GCC_except_table2345
- GCC_except_table2346
- GCC_except_table2357
- GCC_except_table2358
- GCC_except_table2369
- GCC_except_table2658
- GCC_except_table3124
- GCC_except_table3127
- GCC_except_table3179
- GCC_except_table3275
- GCC_except_table3287
- GCC_except_table3337
- GCC_except_table3342
- GCC_except_table3346
- GCC_except_table3359
- GCC_except_table3383
- GCC_except_table3387
- GCC_except_table3518
- GCC_except_table3533
- ___44-[LNActionExecutor performWithoutValidation]_block_invoke_3
- ___98-[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:]_block_invoke
- ___98-[LNActionExecutor requestSideEffectConfirmationFromResult:connectionInterface:action:connection:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56s_e40_v16?0"LNPreConfirmationResultWrapper"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e50_v24?0"LNActionConfirmationResponse"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___swift_closure_destructor.38Tm
CStrings:
+ "Connection dropped during pre-confirmation (state: %{public}@); reconnecting before performing"
+ "Connection resolved after executor teardown; not performing"
+ "Resolved localizedApplicationName `%{public}@` for extension `%{public}@`"
+ "Resolved the application name for extension `%{public}s`"
+ "connect"
+ "homeAccessory"
+ "state == LNActionExecutorStateClassifyingParameters || state == LNActionExecutorStateResolving || state == LNActionExecutorStatePerforming || state == LNActionExecutorStateCompleted || state == LNActionExecutorStateConnecting"
+ "state == LNActionExecutorStateWaitingForActionConfirmation || state == LNActionExecutorStatePerforming || state == LNActionExecutorStateCompleted || state == LNActionExecutorStateConnecting"
- "state == LNActionExecutorStateWaitingForActionConfirmation || state == LNActionExecutorStatePerforming || state == LNActionExecutorStateCompleted"
```
