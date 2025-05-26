## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3431.206.0.0.0
-  __TEXT.__text: 0x6f3e0
+3431.316.0.0.0
+  __TEXT.__text: 0x71790
   __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x9924
+  __TEXT.__objc_methlist: 0x9c0c
   __TEXT.__const: 0x448
-  __TEXT.__cstring: 0x12c2d
+  __TEXT.__cstring: 0x13413
   __TEXT.__ustring: 0x3fa2
   __TEXT.__dlopen_cstrs: 0x3ff
   __TEXT.__oslogstring: 0x499
-  __TEXT.__unwind_info: 0x1af4
-  __TEXT.__objc_classname: 0x14c6
-  __TEXT.__objc_methname: 0x16952
-  __TEXT.__objc_methtype: 0x3581
-  __TEXT.__objc_stubs: 0xbee0
+  __TEXT.__unwind_info: 0x1ba4
+  __TEXT.__objc_classname: 0x14d5
+  __TEXT.__objc_methname: 0x17072
+  __TEXT.__objc_methtype: 0x3599
+  __TEXT.__objc_stubs: 0xc1a0
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x2048
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__const: 0x20a0
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10268
-  __DATA_CONST.__objc_selrefs: 0x4c20
-  __DATA_CONST.__objc_arraydata: 0x22248
-  __AUTH_CONST.__cfstring: 0x37720
-  __AUTH_CONST.__objc_const: 0x52d0
-  __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__objc_dictobj: 0xbb80
-  __AUTH_CONST.__objc_arrayobj: 0x3918
-  __AUTH_CONST.__objc_intobj: 0xba0
+  __DATA_CONST.__objc_const: 0x10320
+  __DATA_CONST.__objc_selrefs: 0x4e48
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0x528
+  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_arraydata: 0x22a10
+  __AUTH_CONST.__cfstring: 0x37e80
+  __AUTH_CONST.__objc_const: 0x5318
+  __AUTH_CONST.__const: 0xc40
+  __AUTH_CONST.__objc_dictobj: 0xbdb0
+  __AUTH_CONST.__objc_arrayobj: 0x3960
+  __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x760
-  __AUTH.__objc_data: 0x23f0
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x520
-  __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0xa84
+  __AUTH.__objc_data: 0x2440
+  __DATA.__objc_ivar: 0xa8c
   __DATA.__data: 0xe40
-  __DATA.__bss: 0x488
+  __DATA.__bss: 0x498
   __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3569
-  Symbols:   12328
-  CStrings:  8897
+  Functions: 3637
+  Symbols:   12504
+  CStrings:  9032
 
Symbols:
+ +[TIFeedbackUtil clearStudyState]
+ +[TIFeedbackUtil getBucketedDuration]
+ +[TIFeedbackUtil getCompletionEventTimestamp]
+ +[TIFeedbackUtil getFeedbackState]
+ +[TIFeedbackUtil getFinalInputModes]
+ +[TIFeedbackUtil getFinalPreferenceValue]
+ +[TIFeedbackUtil getFinalTimestamp]
+ +[TIFeedbackUtil getFormIdentifier]
+ +[TIFeedbackUtil getFormMetadata]
+ +[TIFeedbackUtil getInitialInputModes]
+ +[TIFeedbackUtil getInitialPreferenceValue]
+ +[TIFeedbackUtil getInitialTimestamp]
+ +[TIFeedbackUtil getInitiationEventTimestamp]
+ +[TIFeedbackUtil getKeyNameFor:]
+ +[TIFeedbackUtil getPreferenceKey]
+ +[TIFeedbackUtil getRequestSurveyEventTimestamp]
+ +[TIFeedbackUtil getRetryTimestamp]
+ +[TIFeedbackUtil getStateKey]
+ +[TIFeedbackUtil getStudyID]
+ +[TIFeedbackUtil getStudyLanguageAndRegion]
+ +[TIFeedbackUtil getSupportedFeedbackLanguages]
+ +[TIFeedbackUtil getSupportedLangRegion]
+ +[TIFeedbackUtil getSurveyOutcome]
+ +[TIFeedbackUtil isEligibleDevice]
+ +[TIFeedbackUtil isFeatureEnabledForInternalBuilds]
+ +[TIFeedbackUtil migratePreviousStudyStateAndCheckPreviousEnrollment]
+ +[TIFeedbackUtil removeCompletionEventTimestamp]
+ +[TIFeedbackUtil removeFeedbackState]
+ +[TIFeedbackUtil removeFinalInputModes]
+ +[TIFeedbackUtil removeFinalPreferenceValue]
+ +[TIFeedbackUtil removeFinalTimestamp]
+ +[TIFeedbackUtil removeInitialInputModes]
+ +[TIFeedbackUtil removeInitialPreferenceValue]
+ +[TIFeedbackUtil removeInitialTimestamp]
+ +[TIFeedbackUtil removeInitiationEventTimestamp]
+ +[TIFeedbackUtil removeRequestSurveyEventTimestamp]
+ +[TIFeedbackUtil removeRetryTimestamp]
+ +[TIFeedbackUtil removeStudyLanguageAndRegion]
+ +[TIFeedbackUtil removeSurveyOutcome]
+ +[TIFeedbackUtil setCompletionEventTimestamp:]
+ +[TIFeedbackUtil setFeedbackState:]
+ +[TIFeedbackUtil setFinalInputModes:]
+ +[TIFeedbackUtil setFinalPreferenceValue:]
+ +[TIFeedbackUtil setFinalTimestamp:]
+ +[TIFeedbackUtil setInitialInputModes:]
+ +[TIFeedbackUtil setInitialPreferenceValue:]
+ +[TIFeedbackUtil setInitialTimestamp:]
+ +[TIFeedbackUtil setInitiationEventTimestamp:]
+ +[TIFeedbackUtil setRequestSurveyEventTimestamp:]
+ +[TIFeedbackUtil setRetryTimestamp:]
+ +[TIFeedbackUtil setStudyEnrollment:]
+ +[TIFeedbackUtil setStudyEnrollment]
+ +[TIFeedbackUtil setStudyLanguageAndRegion:]
+ +[TIFeedbackUtil setSurveyOutcome:]
+ +[TIFeedbackUtil shouldOverrideLanguageRegionCheck]
+ +[TIFeedbackUtil shouldPublishCAEventsImmediately]
+ -[TIKeyboardSecureCandidateRenderTraits setShouldForceDoubleLineCandidateForCellularAutofill:]
+ -[TIKeyboardSecureCandidateRenderTraits shouldForceDoubleLineCandidateForCellularAutofill]
+ -[TIKeyboardState needCellularAutofill]
+ -[TIKeyboardState setNeedCellularAutofill:]
+ -[TIMecabraCandidate singlePhrase]
+ -[TITypologyLog fileCreationOptions]
+ _IXAFeedbackLogFacility
+ _IXAFeedbackLogFacility.logFacility
+ _IXAFeedbackLogFacility.onceToken
+ _OBJC_CLASS_$_TIFeedbackUtil
+ _OBJC_IVAR_$_TIKeyboardSecureCandidateRenderTraits._shouldForceDoubleLineCandidateForCellularAutofill
+ _OBJC_IVAR_$_TIMecabraCandidate._singlePhrase
+ _OBJC_METACLASS_$_TIFeedbackUtil
+ _SecurityLibrary.11872
+ _SecurityLibraryCore.frameworkLibrary.11883
+ _TIKeyboardOutputInfoTypeCellularEIDStr
+ _TIKeyboardOutputInfoTypeCellularIMEIStr
+ _TIKeyboardSecureCandidateCellularEIDStr
+ _TIKeyboardSecureCandidateCellularIMEIStr
+ _TITextContentTypeCellularEID
+ _TITextContentTypeCellularIMEI
+ __OBJC_$_CLASS_METHODS_TIFeedbackUtil
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1014
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.11211
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1165
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.11910
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12691
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1296
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1364
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2462
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2598
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2683
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2830
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3192
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3559
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.359
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3646
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3834
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4092
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4309
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4823
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5323
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5448
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.587
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.6233
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.7167
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.769
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.7733
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.8053
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.8313
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9035
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.910
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9334
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9504
+ __OBJC_$_PROP_LIST_NSObject.10723
+ __OBJC_$_PROP_LIST_NSObject.10784
+ __OBJC_$_PROP_LIST_NSObject.12302
+ __OBJC_$_PROP_LIST_NSObject.2945
+ __OBJC_$_PROP_LIST_NSObject.3560
+ __OBJC_$_PROP_LIST_NSObject.4450
+ __OBJC_$_PROP_LIST_NSObject.497
+ __OBJC_$_PROP_LIST_NSObject.660
+ __OBJC_$_PROP_LIST_NSObject.6613
+ __OBJC_$_PROP_LIST_NSObject.7497
+ __OBJC_$_PROP_LIST_NSObject.8800
+ __OBJC_$_PROP_LIST_NSObject.9335
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1015
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.11212
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1166
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.11911
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12692
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1297
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1365
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2463
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2599
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2684
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2831
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3193
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3561
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.360
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3647
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3835
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4093
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4310
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4824
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5324
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5449
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.588
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.6234
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.7168
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.770
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.7734
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.8054
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.8314
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9036
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.911
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9336
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9505
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1016
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.11213
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1167
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.11912
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12693
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1298
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1366
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2464
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2600
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2685
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2832
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3194
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3562
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.361
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3648
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3836
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4094
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4311
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4825
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5325
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5450
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.589
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.6235
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.7169
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.771
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.7735
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.8055
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.8315
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9037
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.912
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9337
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9506
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1017
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.11214
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.12694
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1299
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1367
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2601
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2833
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3195
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3563
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3649
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3837
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.4826
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6614
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.7170
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8056
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8316
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.9038
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.913
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.9507
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10724
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10785
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12303
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2946
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3564
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4451
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.498
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.661
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6615
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7498
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8801
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9338
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10725
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10786
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12304
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2947
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3565
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4452
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.499
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6616
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.662
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7499
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8802
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9339
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1018
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.11215
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1168
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.11913
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12695
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1300
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1368
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2465
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2602
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2686
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2834
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3196
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3566
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.362
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3650
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3838
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4095
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4312
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4827
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5326
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5451
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.590
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.6236
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.7171
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.772
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.7736
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.8057
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.8317
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9039
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.914
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9340
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9508
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1019
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.11216
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.12696
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1301
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1369
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2603
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2835
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3197
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3567
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3651
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3839
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.4828
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6617
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.7172
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8058
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8318
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.9040
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.915
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.9509
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10726
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10787
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12305
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2948
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3568
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4453
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.500
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6618
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.663
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7500
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8803
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9341
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1020
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.11217
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1169
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.11914
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12697
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1302
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1370
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2466
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2604
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2687
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2836
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3198
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3569
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.363
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3652
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3840
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4096
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4313
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4829
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5327
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5452
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.591
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.6237
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.7173
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.773
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.7737
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.8059
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.8319
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9041
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.916
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9342
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9510
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1021
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.11218
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1170
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.11915
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12698
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1303
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1371
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2467
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2605
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2688
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2837
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3199
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3570
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.364
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3653
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3841
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4097
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4314
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4830
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5328
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5453
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.592
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.6238
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.7174
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.7738
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.774
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.8060
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.8320
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9042
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.917
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9343
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9511
+ __OBJC_CLASS_RO_$_TIFeedbackUtil
+ __OBJC_METACLASS_RO_$_TIFeedbackUtil
+ __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8un170006IPNS_6vectorI18TIHandwritingPointNS_9allocatorIS5_EEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorI18TIHandwritingPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8un170006INS_9allocatorINS_6vectorI18TIHandwritingPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__13setI8NSHolderI20_TIInputContextEntryENS_4lessIS3_EENS_9allocatorIS3_EEE6insertB8un170006INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEEEvT_SG_
+ __ZNSt3__16vectorI18TIHandwritingPointNS_9allocatorIS1_EEE11__vallocateB8un170006Em
+ __ZNSt3__16vectorINS0_I18TIHandwritingPointNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB8un170006Ev
+ __ZSt28__throw_bad_array_new_lengthB8un170006v
+ ___138-[TIAnalyticsService _dispatchEventToDomain:withName:payload:values:inputMode:testingParameters:allowSparsePayload:withCompletionHandler:]_block_invoke.268
+ ___40+[TIFeedbackUtil getSupportedLangRegion]_block_invoke
+ ___40+[TIFeedbackUtil getSupportedLangRegion]_block_invoke_2
+ ___Block_byref_object_copy_.10641
+ ___Block_byref_object_copy_.12077
+ ___Block_byref_object_copy_.224
+ ___Block_byref_object_copy_.2724
+ ___Block_byref_object_copy_.6484
+ ___Block_byref_object_copy_.883
+ ___Block_byref_object_dispose_.10642
+ ___Block_byref_object_dispose_.12078
+ ___Block_byref_object_dispose_.225
+ ___Block_byref_object_dispose_.2725
+ ___Block_byref_object_dispose_.6485
+ ___Block_byref_object_dispose_.884
+ ___IXAFeedbackLogFacility_block_invoke
+ ___SecurityLibraryCore_block_invoke.11884
+ ___block_descriptor_40_a8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.104.8921
+ ___block_literal_global.1064
+ ___block_literal_global.11259
+ ___block_literal_global.11538
+ ___block_literal_global.11589
+ ___block_literal_global.11829
+ ___block_literal_global.12371
+ ___block_literal_global.12809
+ ___block_literal_global.1735
+ ___block_literal_global.2197
+ ___block_literal_global.22.11866
+ ___block_literal_global.2388
+ ___block_literal_global.24.4547
+ ___block_literal_global.244
+ ___block_literal_global.253
+ ___block_literal_global.271
+ ___block_literal_global.290
+ ___block_literal_global.33
+ ___block_literal_global.3844
+ ___block_literal_global.3851
+ ___block_literal_global.3951
+ ___block_literal_global.4.8065
+ ___block_literal_global.4457
+ ___block_literal_global.4549
+ ___block_literal_global.5036
+ ___block_literal_global.5517
+ ___block_literal_global.61.9081
+ ___block_literal_global.625
+ ___block_literal_global.6273
+ ___block_literal_global.6548
+ ___block_literal_global.7.8068
+ ___block_literal_global.7.8331
+ ___block_literal_global.7231
+ ___block_literal_global.736
+ ___block_literal_global.7511
+ ___block_literal_global.769
+ ___block_literal_global.778
+ ___block_literal_global.794
+ ___block_literal_global.8042
+ ___block_literal_global.8061
+ ___block_literal_global.828
+ ___block_literal_global.830
+ ___block_literal_global.8327
+ ___block_literal_global.8781
+ ___block_literal_global.8918
+ ___block_literal_global.9109
+ ___block_literal_global.990
+ ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.11878
+ ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.11874
+ __unnamed_array_storage.12817
+ __unnamed_array_storage.1739
+ __unnamed_array_storage.175
+ __unnamed_array_storage.185
+ __unnamed_array_storage.192
+ __unnamed_array_storage.198
+ __unnamed_array_storage.207
+ __unnamed_array_storage.2204
+ __unnamed_array_storage.229
+ __unnamed_array_storage.2392
+ __unnamed_array_storage.6011
+ __unnamed_array_storage.6579
+ __unnamed_array_storage.8879
+ _audit_stringSecurity.11886
+ _generateIdentifier.count.9020
+ _getSecTaskCopySigningIdentifierSymbolLoc.ptr.11877
+ _getSecTaskCreateFromSelfSymbolLoc.ptr.11873
+ _objc_msgSend$fileCreationOptions
+ _objc_msgSend$getBucketedDuration
+ _objc_msgSend$getFinalTimestamp
+ _objc_msgSend$getInitialPreferenceValue
+ _objc_msgSend$getInitialTimestamp
+ _objc_msgSend$getKeyNameFor:
+ _objc_msgSend$getStateKey
+ _objc_msgSend$getStudyID
+ _objc_msgSend$getStudyLanguageAndRegion
+ _objc_msgSend$getSupportedFeedbackLanguages
+ _objc_msgSend$getSupportedLangRegion
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isInternalDeviceWithForcedTypologyLoggingForTesting
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$migratePreviousStudyStateAndCheckPreviousEnrollment
+ _objc_msgSend$needCellularAutofill
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setStudyEnrollment:
+ _objc_msgSend$shouldOverrideLanguageRegionCheck
+ _objc_msgSend$stringArrayForKey:
+ _objc_msgSend$stringForKey:
+ _sharedInstance.instance.12372
+ _sharedInstance.instance.250
+ _sharedInstance.instance.8043
+ _sharedInstance.onceToken.12370
+ _sharedInstance.onceToken.251
+ _sharedInstance.onceToken.7230
+ _sharedInstance.onceToken.8041
+ _sharedPreferencesController.once.709
+ _sharedPreferencesController.once.746
+ _sharedPreferencesController.sharedController.710
+ _sharedPreferencesController.sharedController.747
- _SecurityLibrary.11689
- _SecurityLibraryCore.frameworkLibrary.11700
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1046
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.11036
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.11728
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1178
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1246
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12493
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.227
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2302
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2438
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2523
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2670
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3029
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3389
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3476
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3664
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3922
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4144
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.4652
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.474
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5148
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5272
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.6054
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.659
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.6974
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.7535
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.7846
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.791
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.8107
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.8835
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.896
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9129
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9298
- __OBJC_$_PROP_LIST_NSObject.10544
- __OBJC_$_PROP_LIST_NSObject.10603
- __OBJC_$_PROP_LIST_NSObject.12116
- __OBJC_$_PROP_LIST_NSObject.2785
- __OBJC_$_PROP_LIST_NSObject.3390
- __OBJC_$_PROP_LIST_NSObject.379
- __OBJC_$_PROP_LIST_NSObject.4280
- __OBJC_$_PROP_LIST_NSObject.549
- __OBJC_$_PROP_LIST_NSObject.6426
- __OBJC_$_PROP_LIST_NSObject.7303
- __OBJC_$_PROP_LIST_NSObject.8602
- __OBJC_$_PROP_LIST_NSObject.9130
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1047
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.11037
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.11729
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1179
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1247
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12494
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.228
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2303
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2439
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2524
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2671
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3030
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3391
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3477
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3665
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3923
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4145
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.4653
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.475
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5149
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5273
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.6055
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.660
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.6975
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.7536
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.7847
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.792
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.8108
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.8836
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.897
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9131
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9299
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1048
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.11038
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.11730
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1180
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1248
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12495
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.229
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2304
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2440
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2525
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2672
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3031
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3392
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3478
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3666
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3924
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4146
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.4654
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.476
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5150
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5274
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.6056
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.661
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.6976
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.7537
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.7848
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.793
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.8109
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.8837
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.898
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9132
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9300
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.11039
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1181
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1249
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.12496
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2441
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2673
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3032
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3393
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3479
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3667
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.4655
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6427
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6977
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.7849
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.794
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8110
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8838
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.899
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.9301
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10545
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10604
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2786
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3394
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.380
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4281
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.550
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6428
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7304
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8603
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9133
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10546
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10605
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12118
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2787
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3395
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.381
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4282
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.551
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6429
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7305
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8604
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9134
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1049
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.11040
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.11731
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1182
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12497
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1250
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.230
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2305
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2442
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2526
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2674
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3033
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3396
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3480
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3668
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3925
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4147
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.4656
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.477
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5151
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5275
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.6057
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.662
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.6978
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.7538
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.7850
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.795
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.8111
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.8839
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.900
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9135
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9302
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.11041
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1183
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.12498
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1251
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2443
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2675
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3034
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3397
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3481
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3669
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.4657
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6430
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6979
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.7851
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.796
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8112
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8840
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.901
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.9303
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10547
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10606
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12119
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2788
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3398
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.382
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4283
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.552
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6431
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7306
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8605
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9136
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1050
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.11042
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.11732
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1184
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12499
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1252
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2306
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.231
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2444
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2527
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2676
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3035
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3399
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3482
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3670
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3926
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4148
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.4658
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.478
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5152
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5276
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.6058
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.663
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.6980
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.7539
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.7852
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.797
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.8113
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.8841
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.902
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9137
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9304
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1051
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.11043
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.11733
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1185
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12500
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1253
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2307
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.232
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2445
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2528
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2677
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3036
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3400
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3483
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3671
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3927
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4149
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.4659
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.479
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5153
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5277
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.6059
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.664
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.6981
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.7540
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.7853
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.798
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.8114
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.8842
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.903
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9138
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9305
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI18TIHandwritingPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_6vectorI18TIHandwritingPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPNS_6vectorI18TIHandwritingPointNS_9allocatorIS8_EEEESC_SC_Li0EEENS_4pairIT0_T2_EESE_T1_SF_
- __ZNSt3__13setI8NSHolderI20_TIInputContextEntryENS_4lessIS3_EENS_9allocatorIS3_EEE6insertB7v160006INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEEEvT_SG_
- __ZNSt3__16vectorI18TIHandwritingPointNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorINS0_I18TIHandwritingPointNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB7v160006Ev
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___138-[TIAnalyticsService _dispatchEventToDomain:withName:payload:values:inputMode:testingParameters:allowSparsePayload:withCompletionHandler:]_block_invoke.267
- ___Block_byref_object_copy_.10462
- ___Block_byref_object_copy_.11895
- ___Block_byref_object_copy_.2564
- ___Block_byref_object_copy_.6305
- ___Block_byref_object_copy_.768
- ___Block_byref_object_dispose_.10463
- ___Block_byref_object_dispose_.11896
- ___Block_byref_object_dispose_.2565
- ___Block_byref_object_dispose_.6306
- ___Block_byref_object_dispose_.769
- ___SecurityLibraryCore_block_invoke.11701
- ___block_literal_global.104.8724
- ___block_literal_global.11084
- ___block_literal_global.111
- ___block_literal_global.11361
- ___block_literal_global.11412
- ___block_literal_global.11647
- ___block_literal_global.12185
- ___block_literal_global.12611
- ___block_literal_global.1584
- ___block_literal_global.159
- ___block_literal_global.2013
- ___block_literal_global.22.11683
- ___block_literal_global.2205
- ___block_literal_global.24.4375
- ___block_literal_global.252
- ___block_literal_global.270
- ___block_literal_global.3674
- ___block_literal_global.3681
- ___block_literal_global.3781
- ___block_literal_global.4.7858
- ___block_literal_global.4287
- ___block_literal_global.4378
- ___block_literal_global.4863
- ___block_literal_global.514
- ___block_literal_global.5341
- ___block_literal_global.6094
- ___block_literal_global.61.8880
- ___block_literal_global.627
- ___block_literal_global.6364
- ___block_literal_global.7.7861
- ___block_literal_global.7.8125
- ___block_literal_global.7038
- ___block_literal_global.715
- ___block_literal_global.7317
- ___block_literal_global.768
- ___block_literal_global.777
- ___block_literal_global.7835
- ___block_literal_global.7854
- ___block_literal_global.793
- ___block_literal_global.8121
- ___block_literal_global.827
- ___block_literal_global.8582
- ___block_literal_global.872
- ___block_literal_global.8721
- ___block_literal_global.8908
- ___block_literal_global.946
- ___getSecTaskCopySigningIdentifierSymbolLoc_block_invoke.11695
- ___getSecTaskCreateFromSelfSymbolLoc_block_invoke.11691
- __unnamed_array_storage.12619
- __unnamed_array_storage.1586
- __unnamed_array_storage.184
- __unnamed_array_storage.190
- __unnamed_array_storage.196
- __unnamed_array_storage.2020
- __unnamed_array_storage.205
- __unnamed_array_storage.2209
- __unnamed_array_storage.5831
- __unnamed_array_storage.6393
- __unnamed_array_storage.8682
- _audit_stringSecurity.11703
- _generateIdentifier.count.8820
- _getSecTaskCopySigningIdentifierSymbolLoc.ptr.11694
- _getSecTaskCreateFromSelfSymbolLoc.ptr.11690
- _sharedInstance.instance.12186
- _sharedInstance.instance.249
- _sharedInstance.instance.7836
- _sharedInstance.onceToken.12184
- _sharedInstance.onceToken.250
- _sharedInstance.onceToken.7037
- _sharedInstance.onceToken.7834
- _sharedPreferencesController.once.708
- _sharedPreferencesController.once.745
- _sharedPreferencesController.sharedController.709
- _sharedPreferencesController.sharedController.746
CStrings:
+ "%ld"
+ "(?=\"integerValue\"q\"fields\"{?=\"userSelectedCurrentCandidate\"b1\"shouldSkipCandidateSelection\"b1\"suppressingCandidateSelection\"b1\"needsCandidateMetadata\"b1\"keyboardEventsLagging\"b1\"hardwareKeyboardMode\"b1\"splitKeyboardMode\"b1\"floatingKeyboardMode\"b1\"wordLearningEnabled\"b1\"autocorrectionEnabled\"b1\"shortcutConversionEnabled\"b1\"candidateSelectionPredictionEnabled\"b1\"autocapitalizationEnabled\"b1\"canSendCurrentLocation\"b1\"isScreenLocked\"b1\"longPredictionListEnabled\"b1\"needAutofill\"b1\"needOneTimeCodeAutofill\"b1\"landscapeOrientation\"b1\"omitEmojiCandidates\"b1\"emojiSearchMode\"b1\"emojiPopoverMode\"b1\"canSuggestSupplementalItemsForCurrentSelection\"b1\"inlineCompletionEnabled\"b1\"imageSuggestionEnabled\"b1\"needCellularAutofill\"b1})"
+ ":duration"
+ ":initialPreferenceValue"
+ "; needCellularAutofill = %s"
+ "AutofillCellularEID"
+ "AutofillCellularIMEI"
+ "Croatian - Standard"
+ "IXAFeedback"
+ "InputMode_en-WAVE2-XR.plist"
+ "Insert Cellular EID"
+ "Insert Cellular IMEI"
+ "Julev Sami - Norway"
+ "S01"
+ "S02"
+ "Sami-Julev-Norway"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_shouldForceDoubleLineCandidateForCellularAutofill"
+ "TB,R,N,V_singlePhrase"
+ "TIFeedbackUtil"
+ "_shouldForceDoubleLineCandidateForCellularAutofill"
+ "_singlePhrase"
+ "clearStudyState"
+ "esim-eid"
+ "esim-imei"
+ "feedbackCompletionEventTimestamp_"
+ "feedbackCompletionEventTimestamp_KeyboardAutocorrection"
+ "feedbackCompletionEventTimestamp_KeyboardAutocorrection_S02"
+ "feedbackCountsRetained_KeyboardAutocorrection"
+ "feedbackFeatureEnabled"
+ "feedbackFeatureEnabled_KeyboardAutocorrection"
+ "feedbackFinalInputModes_"
+ "feedbackFinalInputModes_KeyboardAutocorrection"
+ "feedbackFinalInputModes_KeyboardAutocorrection_S02"
+ "feedbackFinalPreferenceValue_"
+ "feedbackFinalPreferenceValue_KeyboardAutocorrection"
+ "feedbackFinalPreferenceValue_KeyboardAutocorrection_S02"
+ "feedbackFinalTimestamp_"
+ "feedbackFinalTimestamp_KeyboardAutocorrection"
+ "feedbackFinalTimestamp_KeyboardAutocorrection_S02"
+ "feedbackInitialInputModes_"
+ "feedbackInitialInputModes_KeyboardAutocorrection"
+ "feedbackInitialInputModes_KeyboardAutocorrection_S02"
+ "feedbackInitialPreferenceValue_"
+ "feedbackInitialPreferenceValue_KeyboardAutocorrection"
+ "feedbackInitialPreferenceValue_KeyboardAutocorrection_S02"
+ "feedbackInitialTimestamp_"
+ "feedbackInitialTimestamp_KeyboardAutocorrection"
+ "feedbackInitialTimestamp_KeyboardAutocorrection_S02"
+ "feedbackInitiationEventTimestamp_"
+ "feedbackInitiationEventTimestamp_KeyboardAutocorrection"
+ "feedbackInitiationEventTimestamp_KeyboardAutocorrection_S02"
+ "feedbackLastStudyEnrollment"
+ "feedbackOverrideDeviceLanguageCheck"
+ "feedbackPublishCAEventsImmediately"
+ "feedbackRetryTimestamp_"
+ "feedbackRetryTimestamp_KeyboardAutocorrection_S02"
+ "feedbackState_"
+ "feedbackState_KeyboardAutocorrection"
+ "feedbackState_KeyboardAutocorrection_S02"
+ "feedbackStudyLanguageRegionKey"
+ "feedbackSurveyOutcome_"
+ "feedbackSurveyOutcome_KeyboardAutocorrection"
+ "feedbackSurveyOutcome_KeyboardAutocorrection_S02"
+ "feedbackSurveyRequestEventTimestamp_"
+ "feedbackSurveyRequestEventTimestamp_KeyboardAutocorrection_S02"
+ "fileCreationOptions"
+ "framework-autocorrect_S02_"
+ "getBucketedDuration"
+ "getCompletionEventTimestamp"
+ "getFeedbackState"
+ "getFinalInputModes"
+ "getFinalPreferenceValue"
+ "getFinalTimestamp"
+ "getFormIdentifier"
+ "getFormMetadata"
+ "getInitialInputModes"
+ "getInitialPreferenceValue"
+ "getInitialTimestamp"
+ "getInitiationEventTimestamp"
+ "getKeyNameFor:"
+ "getPreferenceKey"
+ "getRequestSurveyEventTimestamp"
+ "getRetryTimestamp"
+ "getStateKey"
+ "getStudyID"
+ "getStudyLanguageAndRegion"
+ "getSupportedFeedbackLanguages"
+ "getSupportedLangRegion"
+ "getSurveyOutcome"
+ "integerForKey:"
+ "isEligibleDevice"
+ "isFeatureEnabledForInternalBuilds"
+ "isInternalDeviceWithForcedTypologyLoggingForTesting"
+ "languageIdentifier"
+ "migratePreviousStudyStateAndCheckPreviousEnrollment"
+ "needCellularAutofill"
+ "removeCompletionEventTimestamp"
+ "removeFeedbackState"
+ "removeFinalInputModes"
+ "removeFinalPreferenceValue"
+ "removeFinalTimestamp"
+ "removeInitialInputModes"
+ "removeInitialPreferenceValue"
+ "removeInitialTimestamp"
+ "removeInitiationEventTimestamp"
+ "removeRequestSurveyEventTimestamp"
+ "removeRetryTimestamp"
+ "removeStudyLanguageAndRegion"
+ "removeSurveyOutcome"
+ "setBool:forKey:"
+ "setCompletionEventTimestamp:"
+ "setFeedbackState:"
+ "setFinalInputModes:"
+ "setFinalPreferenceValue:"
+ "setFinalTimestamp:"
+ "setInitialInputModes:"
+ "setInitialPreferenceValue:"
+ "setInitialTimestamp:"
+ "setInitiationEventTimestamp:"
+ "setInteger:forKey:"
+ "setNeedCellularAutofill:"
+ "setRequestSurveyEventTimestamp:"
+ "setRetryTimestamp:"
+ "setShouldForceDoubleLineCandidateForCellularAutofill:"
+ "setStudyEnrollment"
+ "setStudyEnrollment:"
+ "setStudyLanguageAndRegion:"
+ "setSurveyOutcome:"
+ "shouldForceDoubleLineCandidateForCellularAutofill"
+ "shouldOverrideLanguageRegionCheck"
+ "shouldPublishCAEventsImmediately"
+ "singlePhrase"
+ "stringArrayForKey:"
+ "stringForKey:"
- "(?=\"integerValue\"q\"fields\"{?=\"userSelectedCurrentCandidate\"b1\"shouldSkipCandidateSelection\"b1\"suppressingCandidateSelection\"b1\"needsCandidateMetadata\"b1\"keyboardEventsLagging\"b1\"hardwareKeyboardMode\"b1\"splitKeyboardMode\"b1\"floatingKeyboardMode\"b1\"wordLearningEnabled\"b1\"autocorrectionEnabled\"b1\"shortcutConversionEnabled\"b1\"candidateSelectionPredictionEnabled\"b1\"autocapitalizationEnabled\"b1\"canSendCurrentLocation\"b1\"isScreenLocked\"b1\"longPredictionListEnabled\"b1\"needAutofill\"b1\"needOneTimeCodeAutofill\"b1\"landscapeOrientation\"b1\"omitEmojiCandidates\"b1\"emojiSearchMode\"b1\"emojiPopoverMode\"b1\"canSuggestSupplementalItemsForCurrentSelection\"b1\"inlineCompletionEnabled\"b1\"imageSuggestionEnabled\"b1})"

```
