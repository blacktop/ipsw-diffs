## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

 539.1.1.0.0
-  __TEXT.__text: 0xb9a80
-  __TEXT.__objc_methlist: 0x93e4
+  __TEXT.__text: 0xba044
+  __TEXT.__objc_methlist: 0x9434
   __TEXT.__const: 0x7e4
   __TEXT.__dlopen_cstrs: 0x85c
-  __TEXT.__cstring: 0x60b7
+  __TEXT.__cstring: 0x60da
   __TEXT.__swift5_typeref: 0x2a5
   __TEXT.__swift5_capture: 0x1d8
   __TEXT.__constg_swiftt: 0x1a0

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0xfd57
-  __TEXT.__gcc_except_tab: 0x2900
-  __TEXT.__unwind_info: 0x2cd8
+  __TEXT.__oslogstring: 0xfdda
+  __TEXT.__gcc_except_tab: 0x290c
+  __TEXT.__unwind_info: 0x2ce8
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5688
+  __DATA_CONST.__objc_selrefs: 0x56b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__got: 0x778
   __AUTH_CONST.__const: 0x1638
-  __AUTH_CONST.__cfstring: 0x5d60
-  __AUTH_CONST.__objc_const: 0xc078
+  __AUTH_CONST.__cfstring: 0x5d80
+  __AUTH_CONST.__objc_const: 0xc0a8
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x11d8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0xa24
+  __DATA.__objc_ivar: 0xa28
   __DATA.__data: 0xf80
   __DATA_DIRTY.__objc_data: 0x5a8
   __DATA_DIRTY.__data: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4130
-  Symbols:   8658
-  CStrings:  2109
+  Functions: 4138
+  Symbols:   8674
+  CStrings:  2113
 
Symbols:
+ -[HUNoiseController filterPendingNoiseSamplesForAOP2IfNeeded]
+ -[HUNoiseController lastClassificationSampleDate]
+ -[HUNoiseController processSoundClassificationMeasurementsAOP2:withMetadata:]
+ -[HUNoiseController setLastClassificationSampleDate:]
+ -[HUNoiseController updateLastClassificationSampleWithDetectionState:sampleDate:]
+ -[HUNoiseSettings internalOverrideSoundDetectionType]
+ GCC_except_table2630
+ GCC_except_table2656
+ GCC_except_table2663
+ GCC_except_table2717
+ GCC_except_table2720
+ GCC_except_table2729
+ GCC_except_table2733
+ GCC_except_table2772
+ GCC_except_table2777
+ GCC_except_table2784
+ GCC_except_table2792
+ GCC_except_table2797
+ GCC_except_table2799
+ GCC_except_table2808
+ GCC_except_table2812
+ GCC_except_table2914
+ GCC_except_table2936
+ GCC_except_table2968
+ GCC_except_table2996
+ GCC_except_table3133
+ GCC_except_table3163
+ GCC_except_table3185
+ GCC_except_table3193
+ GCC_except_table3202
+ GCC_except_table3211
+ GCC_except_table3214
+ GCC_except_table3216
+ GCC_except_table3272
+ GCC_except_table3299
+ GCC_except_table3378
+ GCC_except_table3379
+ GCC_except_table3398
+ GCC_except_table3404
+ GCC_except_table3410
+ GCC_except_table3413
+ GCC_except_table3425
+ GCC_except_table3440
+ GCC_except_table3445
+ GCC_except_table3454
+ GCC_except_table3456
+ GCC_except_table3466
+ GCC_except_table3469
+ GCC_except_table3478
+ GCC_except_table3481
+ GCC_except_table3483
+ GCC_except_table3508
+ GCC_except_table3571
+ GCC_except_table3577
+ GCC_except_table3581
+ GCC_except_table3652
+ GCC_except_table3654
+ GCC_except_table3697
+ GCC_except_table3734
+ GCC_except_table3809
+ GCC_except_table3827
+ GCC_except_table3830
+ GCC_except_table3840
+ _OBJC_IVAR_$_HUNoiseController._lastClassificationSampleDate
+ ___54-[HUNoiseController _startADAMClassificationReceiving]_block_invoke_2
+ ___77-[HUNoiseController processSoundClassificationMeasurementsAOP2:withMetadata:]_block_invoke
+ _objc_msgSend$deviceSupportsMedina
+ _objc_msgSend$filterPendingNoiseSamplesForAOP2IfNeeded
+ _objc_msgSend$lastClassificationSampleDate
+ _objc_msgSend$processSoundClassificationMeasurementsAOP2:withMetadata:
+ _objc_msgSend$removePendingNoiseSamplesWithinDateInterval:
+ _objc_msgSend$setLastClassificationSampleDate:
+ _objc_msgSend$updateLastClassificationSampleWithDetectionState:sampleDate:
- GCC_except_table2629
- GCC_except_table2655
- GCC_except_table2662
- GCC_except_table2716
- GCC_except_table2718
- GCC_except_table2724
- GCC_except_table2732
- GCC_except_table2771
- GCC_except_table2776
- GCC_except_table2783
- GCC_except_table2791
- GCC_except_table2796
- GCC_except_table2798
- GCC_except_table2807
- GCC_except_table2811
- GCC_except_table2913
- GCC_except_table2935
- GCC_except_table2967
- GCC_except_table2995
- GCC_except_table3132
- GCC_except_table3162
- GCC_except_table3183
- GCC_except_table3192
- GCC_except_table3201
- GCC_except_table3210
- GCC_except_table3213
- GCC_except_table3215
- GCC_except_table3271
- GCC_except_table3298
- GCC_except_table3375
- GCC_except_table3376
- GCC_except_table3391
- GCC_except_table3397
- GCC_except_table3403
- GCC_except_table3406
- GCC_except_table3418
- GCC_except_table3426
- GCC_except_table3437
- GCC_except_table3446
- GCC_except_table3448
- GCC_except_table3458
- GCC_except_table3461
- GCC_except_table3470
- GCC_except_table3473
- GCC_except_table3475
- GCC_except_table3500
- GCC_except_table3563
- GCC_except_table3569
- GCC_except_table3573
- GCC_except_table3644
- GCC_except_table3646
- GCC_except_table3689
- GCC_except_table3726
- GCC_except_table3801
- GCC_except_table3819
- GCC_except_table3822
- GCC_except_table3832
CStrings:
+ "InternalOverrideSoundDetectionType"
+ "Invalid classification date: %@"
+ "Last sample date is later than start date"
+ "Update last classification state from %d (%@) to %d (%@)"
```
