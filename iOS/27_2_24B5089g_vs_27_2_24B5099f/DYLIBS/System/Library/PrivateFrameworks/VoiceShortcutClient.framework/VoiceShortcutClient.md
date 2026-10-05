## VoiceShortcutClient

> `/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`

```diff

-5111.0.2.0.0
-  __TEXT.__text: 0x14611c
-  __TEXT.__objc_methlist: 0xceec
+5113.0.1.1.1
+  __TEXT.__text: 0x146978
+  __TEXT.__objc_methlist: 0xcf14
   __TEXT.__const: 0xf780
   __TEXT.__dlopen_cstrs: 0xdb4
-  __TEXT.__cstring: 0x18414
+  __TEXT.__cstring: 0x1848a
   __TEXT.__swift5_typeref: 0x3809
   __TEXT.__swift5_reflstr: 0x1544
   __TEXT.__swift5_assocty: 0x4c8

   __TEXT.__swift5_types: 0x434
   __TEXT.__swift5_capture: 0x758
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__oslogstring: 0x4065
+  __TEXT.__oslogstring: 0x41be
   __TEXT.__swift_as_entry: 0xfc
   __TEXT.__swift_as_ret: 0xe8
   __TEXT.__swift_as_cont: 0x1c0
   __TEXT.__swift5_mpenum: 0x8c
-  __TEXT.__gcc_except_tab: 0x1934
+  __TEXT.__gcc_except_tab: 0x19e0
   __TEXT.__ustring: 0x1a8
-  __TEXT.__unwind_info: 0x89f0
-  __TEXT.__eh_frame: 0x61d8
+  __TEXT.__unwind_info: 0x8a48
+  __TEXT.__eh_frame: 0x6228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6178
+  __DATA_CONST.__objc_selrefs: 0x6190
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x7f0
   __DATA_CONST.__objc_arraydata: 0x4740
   __DATA_CONST.__got: 0x1210
   __AUTH_CONST.__const: 0xa138
-  __AUTH_CONST.__cfstring: 0x19d80
-  __AUTH_CONST.__objc_const: 0x1a808
+  __AUTH_CONST.__cfstring: 0x19da0
+  __AUTH_CONST.__objc_const: 0x1a8d0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x4d88
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH_CONST.__auth_got: 0x1e58
+  __AUTH_CONST.__auth_got: 0x1e60
   __AUTH.__objc_data: 0x3e00
   __AUTH.__data: 0x1a90
-  __DATA.__objc_ivar: 0xd18
+  __DATA.__objc_ivar: 0xd30
   __DATA.__data: 0x4550
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x2368

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10686
-  Symbols:   11668
-  CStrings:  4422
+  Functions: 10695
+  Symbols:   11685
+  CStrings:  4430
 
Symbols:
+ -[WFDispatchSourceTimer isPaused]
+ -[WFDispatchSourceTimer pause]
+ -[WFDispatchSourceTimer remainingInterval]
+ -[WFDispatchSourceTimer resume]
+ -[WFStateMachine isCurrentStateTimeoutPaused]
+ -[WFStateMachine pauseCurrentStateTimeoutWithReason:]
+ -[WFStateMachine resumeCurrentStateTimeoutWithReason:]
+ GCC_except_table2134
+ GCC_except_table2177
+ GCC_except_table2206
+ GCC_except_table2261
+ GCC_except_table2272
+ GCC_except_table2297
+ GCC_except_table2320
+ GCC_except_table2325
+ GCC_except_table2328
+ GCC_except_table2410
+ GCC_except_table2416
+ GCC_except_table2483
+ GCC_except_table2490
+ GCC_except_table2498
+ GCC_except_table2716
+ GCC_except_table2769
+ GCC_except_table2773
+ GCC_except_table2778
+ GCC_except_table2809
+ GCC_except_table2929
+ GCC_except_table2933
+ GCC_except_table2935
+ GCC_except_table2938
+ GCC_except_table2945
+ GCC_except_table2951
+ GCC_except_table2956
+ GCC_except_table2975
+ GCC_except_table2981
+ GCC_except_table3198
+ GCC_except_table3271
+ GCC_except_table3283
+ GCC_except_table3286
+ GCC_except_table3362
+ GCC_except_table3368
+ GCC_except_table3374
+ GCC_except_table3527
+ GCC_except_table3528
+ GCC_except_table3595
+ GCC_except_table3682
+ GCC_except_table3701
+ GCC_except_table3702
+ GCC_except_table3710
+ GCC_except_table3718
+ GCC_except_table3719
+ GCC_except_table3720
+ GCC_except_table3722
+ GCC_except_table3762
+ GCC_except_table3861
+ GCC_except_table3890
+ GCC_except_table3891
+ GCC_except_table3892
+ GCC_except_table4111
+ GCC_except_table4114
+ GCC_except_table4117
+ GCC_except_table4119
+ GCC_except_table4127
+ GCC_except_table4232
+ GCC_except_table4236
+ GCC_except_table4249
+ GCC_except_table4356
+ GCC_except_table4407
+ GCC_except_table4438
+ GCC_except_table4443
+ GCC_except_table4446
+ GCC_except_table4449
+ GCC_except_table4452
+ GCC_except_table4455
+ GCC_except_table4464
+ GCC_except_table4467
+ GCC_except_table4469
+ GCC_except_table4472
+ GCC_except_table4482
+ GCC_except_table4487
+ GCC_except_table4492
+ GCC_except_table4509
+ GCC_except_table4513
+ GCC_except_table4526
+ GCC_except_table4544
+ _OBJC_IVAR_$_WFDispatchSourceTimer._deadline
+ _OBJC_IVAR_$_WFDispatchSourceTimer._lock
+ _OBJC_IVAR_$_WFDispatchSourceTimer._paused
+ _OBJC_IVAR_$_WFDispatchSourceTimer._remainingWhenPaused
+ _OBJC_IVAR_$_WFDispatchSourceTimer._repeats
+ _OBJC_IVAR_$_WFDispatchSourceTimer._started
+ ___45-[WFStateMachine isCurrentStateTimeoutPaused]_block_invoke
+ ___53-[WFStateMachine pauseCurrentStateTimeoutWithReason:]_block_invoke
+ ___54-[WFStateMachine resumeCurrentStateTimeoutWithReason:]_block_invoke
+ _clock_gettime_nsec_np
- -[VCVoiceShortcutClient(VoiceShortcuts) getVoiceShortcutsForAppWithBundleIdentifier:completion:]
- -[WFDispatchSourceTimer setHasFired:]
- GCC_except_table2136
- GCC_except_table2179
- GCC_except_table2208
- GCC_except_table2263
- GCC_except_table2274
- GCC_except_table2299
- GCC_except_table2322
- GCC_except_table2327
- GCC_except_table2330
- GCC_except_table2412
- GCC_except_table2418
- GCC_except_table2485
- GCC_except_table2492
- GCC_except_table2500
- GCC_except_table2718
- GCC_except_table2771
- GCC_except_table2775
- GCC_except_table2780
- GCC_except_table2811
- GCC_except_table2934
- GCC_except_table2941
- GCC_except_table2947
- GCC_except_table2952
- GCC_except_table2971
- GCC_except_table2977
- GCC_except_table3194
- GCC_except_table3264
- GCC_except_table3276
- GCC_except_table3279
- GCC_except_table3355
- GCC_except_table3361
- GCC_except_table3367
- GCC_except_table3520
- GCC_except_table3521
- GCC_except_table3588
- GCC_except_table3675
- GCC_except_table3694
- GCC_except_table3695
- GCC_except_table3696
- GCC_except_table3705
- GCC_except_table3706
- GCC_except_table3711
- GCC_except_table3715
- GCC_except_table3755
- GCC_except_table3854
- GCC_except_table3883
- GCC_except_table3884
- GCC_except_table3885
- GCC_except_table4097
- GCC_except_table4107
- GCC_except_table4110
- GCC_except_table4112
- GCC_except_table4120
- GCC_except_table4225
- GCC_except_table4229
- GCC_except_table4242
- GCC_except_table4349
- GCC_except_table4400
- GCC_except_table4431
- GCC_except_table4436
- GCC_except_table4439
- GCC_except_table4442
- GCC_except_table4445
- GCC_except_table4448
- GCC_except_table4453
- GCC_except_table4457
- GCC_except_table4462
- GCC_except_table4465
- GCC_except_table4468
- GCC_except_table4480
- GCC_except_table4485
- GCC_except_table4502
- GCC_except_table4506
- GCC_except_table4519
- GCC_except_table4537
- ___96-[VCVoiceShortcutClient(VoiceShortcuts) getVoiceShortcutsForAppWithBundleIdentifier:completion:]_block_invoke
CStrings:
+ "%s Asked to pause the timeout of state %@, but it has no timeout left to pause, reason: %{public}@"
+ "%s Asked to resume the timeout of state %@, but it wasn't paused, reason: %{public}@"
+ "%s Paused the timeout of state %@ with %f seconds remaining, reason: %{public}@"
+ "%s Resumed the timeout of state %@ with %f seconds remaining, reason: %{public}@"
+ "-[WFStateMachine pauseCurrentStateTimeoutWithReason:]"
+ "-[WFStateMachine resumeCurrentStateTimeoutWithReason:]"
+ "B"
+ "reason"
```
