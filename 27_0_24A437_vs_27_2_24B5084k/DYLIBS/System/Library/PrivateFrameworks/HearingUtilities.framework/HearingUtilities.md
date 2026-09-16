## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-539.1.1.0.0
-  __TEXT.__text: 0xb70a0
-  __TEXT.__objc_methlist: 0x9434
+543.2.0.0.0
+  __TEXT.__text: 0xb7df8
+  __TEXT.__objc_methlist: 0x9474
   __TEXT.__const: 0x7e4
   __TEXT.__dlopen_cstrs: 0x85c
   __TEXT.__cstring: 0x60da

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0xfdda
-  __TEXT.__gcc_except_tab: 0x290c
-  __TEXT.__unwind_info: 0x3690
+  __TEXT.__oslogstring: 0x10145
+  __TEXT.__gcc_except_tab: 0x2934
+  __TEXT.__unwind_info: 0x36a0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56b8
+  __DATA_CONST.__objc_selrefs: 0x56f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__got: 0x778
   __AUTH_CONST.__const: 0x1638
   __AUTH_CONST.__cfstring: 0x5d80
-  __AUTH_CONST.__objc_const: 0xc0a8
+  __AUTH_CONST.__objc_const: 0xc0d8
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x11d8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0xa28
+  __DATA.__objc_ivar: 0xa2c
   __DATA.__data: 0xf80
   __DATA_DIRTY.__objc_data: 0x5a8
   __DATA_DIRTY.__data: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4138
-  Symbols:   8674
-  CStrings:  2113
+  Functions: 4145
+  Symbols:   8689
+  CStrings:  2125
 
Symbols:
+ -[HUComfortSoundsController allActiveCallsEnded]
+ -[HUNoiseController addArtifactsDetectedIntervalWithStartDate:endDate:]
+ -[HUNoiseController artifactsDetectedIntervals]
+ -[HUNoiseController pruneExpiredArtifactsDetectedIntervalsForEndDate:]
+ -[HUNoiseController removeNoiseSamplesWithArtifacts:]
+ -[HUNoiseController setArtifactsDetectedIntervals:]
+ GCC_except_table3135
+ GCC_except_table3165
+ GCC_except_table3186
+ GCC_except_table3187
+ GCC_except_table3195
+ GCC_except_table3204
+ GCC_except_table3213
+ GCC_except_table3218
+ GCC_except_table3274
+ GCC_except_table3301
+ GCC_except_table3382
+ GCC_except_table3383
+ GCC_except_table3405
+ GCC_except_table3411
+ GCC_except_table3417
+ GCC_except_table3420
+ GCC_except_table3432
+ GCC_except_table3447
+ GCC_except_table3452
+ GCC_except_table3461
+ GCC_except_table3463
+ GCC_except_table3473
+ GCC_except_table3476
+ GCC_except_table3485
+ GCC_except_table3488
+ GCC_except_table3490
+ GCC_except_table3515
+ GCC_except_table3578
+ GCC_except_table3584
+ GCC_except_table3588
+ GCC_except_table3659
+ GCC_except_table3661
+ GCC_except_table3704
+ GCC_except_table3741
+ GCC_except_table3816
+ GCC_except_table3834
+ GCC_except_table3837
+ GCC_except_table3847
+ _OBJC_IVAR_$_HUNoiseController._artifactsDetectedIntervals
+ ___48-[HUComfortSoundsController allActiveCallsEnded]_block_invoke
+ _objc_msgSend$addArtifactsDetectedIntervalWithStartDate:endDate:
+ _objc_msgSend$artifactsDetectedIntervals
+ _objc_msgSend$endDate
+ _objc_msgSend$pruneExpiredArtifactsDetectedIntervalsForEndDate:
+ _objc_msgSend$removeNoiseSamplesWithArtifacts:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$setObject:atIndexedSubscript:
- GCC_except_table3133
- GCC_except_table3163
- GCC_except_table3184
- GCC_except_table3185
- GCC_except_table3193
- GCC_except_table3202
- GCC_except_table3211
- GCC_except_table3214
- GCC_except_table3272
- GCC_except_table3299
- GCC_except_table3378
- GCC_except_table3379
- GCC_except_table3398
- GCC_except_table3404
- GCC_except_table3410
- GCC_except_table3413
- GCC_except_table3425
- GCC_except_table3433
- GCC_except_table3445
- GCC_except_table3454
- GCC_except_table3456
- GCC_except_table3466
- GCC_except_table3469
- GCC_except_table3478
- GCC_except_table3481
- GCC_except_table3483
- GCC_except_table3508
- GCC_except_table3571
- GCC_except_table3577
- GCC_except_table3581
- GCC_except_table3652
- GCC_except_table3654
- GCC_except_table3697
- GCC_except_table3734
- GCC_except_table3809
- GCC_except_table3827
- GCC_except_table3830
- GCC_except_table3840
CStrings:
+ "Added artifacts interval (%@ - %@). Total intervals: %lu"
+ "Artifacts are detected without a last classification sample date, skipping in progress artifacts interval"
+ "Artifacts detected state cleared without a previous classification sample date, skipping artifacts interval"
+ "Artifacts detected with invalid sample interval (%@ - %@)"
+ "Checking buffer for artifacts"
+ "ComfortSoundsController: Active calls ended but a call is still present; keeping call hold"
+ "ComfortSoundsController: All calls ended, releasing call hold"
+ "Discarding %lu noise samples that coincided with detected artifacts"
+ "Extended artifacts interval (%@ - %@) to (%@ - %@). Total intervals: %lu"
+ "Last classification sample date (%@) is later than the current date"
+ "Sample date is nil. Using current date"
+ "Skipping artifacts interval (%@ - %@) already covered by (%@ - %@)"
+ "Skipping notification because noise buffer had samples removed due to artifacts"
- "Invalid classification date: %@"
```
