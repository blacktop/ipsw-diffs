## ActionKit

> `/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-5034.0.12.100.0
-  __TEXT.__text: 0x40ad5c
-  __TEXT.__objc_methlist: 0x21a2c
-  __TEXT.__const: 0x2a9c8
+5037.103.100.0.0
+  __TEXT.__text: 0x40da38
+  __TEXT.__objc_methlist: 0x21b44
+  __TEXT.__const: 0x2a9d8
   __TEXT.__dlopen_cstrs: 0x27a3
-  __TEXT.__cstring: 0x53d64
+  __TEXT.__cstring: 0x54077
   __TEXT.__constg_swiftt: 0x1ec8
-  __TEXT.__swift5_typeref: 0x3e67
+  __TEXT.__swift5_typeref: 0x3e85
   __TEXT.__swift5_builtin: 0x21c
   __TEXT.__swift5_reflstr: 0x151b
   __TEXT.__swift5_fieldmd: 0x12a4

   __TEXT.__swift_as_cont: 0x848
   __TEXT.__swift5_capture: 0xc14
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__oslogstring: 0x6781
+  __TEXT.__oslogstring: 0x6a00
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__gcc_except_tab: 0x3d48
-  __TEXT.__ustring: 0x41d8
-  __TEXT.__unwind_info: 0xe5d8
-  __TEXT.__eh_frame: 0x9ef0
+  __TEXT.__gcc_except_tab: 0x3e18
+  __TEXT.__ustring: 0x4352
+  __TEXT.__unwind_info: 0xe650
+  __TEXT.__eh_frame: 0x9f38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1ac8
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x108
-  __DATA_CONST.__objc_protolist: 0x548
+  __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf768
-  __DATA_CONST.__objc_protorefs: 0x1e0
-  __DATA_CONST.__objc_superrefs: 0xc78
+  __DATA_CONST.__objc_selrefs: 0xf7e8
+  __DATA_CONST.__objc_protorefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0xc88
   __DATA_CONST.__objc_arraydata: 0xd88
-  __DATA_CONST.__got: 0x4778
-  __AUTH_CONST.__const: 0x11220
-  __AUTH_CONST.__cfstring: 0x2ba80
-  __AUTH_CONST.__objc_const: 0x3e5a0
+  __DATA_CONST.__got: 0x47b0
+  __AUTH_CONST.__const: 0x11240
+  __AUTH_CONST.__cfstring: 0x2bc40
+  __AUTH_CONST.__objc_const: 0x3e5c8
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x1bc0
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x3598
+  __AUTH_CONST.__auth_got: 0x3628
   __AUTH.__objc_data: 0x8000
   __AUTH.__data: 0xd70
   __DATA.__objc_ivar: 0x1d5c
-  __DATA.__data: 0xb568
-  __DATA.__bss: 0xa1d8
+  __DATA.__data: 0xb5d8
+  __DATA.__bss: 0xa1e8
   __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x9b20
   __DATA_DIRTY.__data: 0x1698

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23969
-  Symbols:   38083
-  CStrings:  13205
+  Functions: 24015
+  Symbols:   38154
+  CStrings:  13237
 
Symbols:
+ +[WFHealthKitAccessResource userInterfaceClasses]
+ +[WFHealthKitAccessResource userInterfaceProtocol]
+ -[WFChooseFromListAction localizedDefaultOutputNameWithContext:]
+ -[WFChooseFromListAction setParameterState:forKey:]
+ -[WFExtractTextFromImageAction setOutputInFinishRunningWithResult:]
+ -[WFGetDeviceDetailsAction isRateLimitedDeviceDetail]
+ -[WFGetDeviceDetailsAction rateLimitDelay]
+ -[WFGetDeviceDetailsAction rateLimitKeySuffix]
+ -[WFGetDeviceDetailsAction rateLimitMaxDelay]
+ -[WFGetDeviceDetailsAction rateLimitMultiplier]
+ -[WFGetDeviceDetailsAction rateLimitThreshold]
+ -[WFGetDeviceDetailsAction rateLimitTimeout]
+ -[WFGetDistanceAction missingLocationErrorWithMissingOrigin:missingDestination:]
+ -[WFHealthKitAccessResource makeAvailableWithRemoteInterface:completionHandler:]
+ -[WFHealthKitAccessResource requestHealthKitAuthorizationWithCompletionHandler:]
+ -[WFLogWorkoutAction initializeParameters]
+ -[WFMakeArchiveAction contentDestinationWithError:]
+ -[WFMakeArchiveAction smartPromptWithContentDescription:contentDestination:workflowName:]
+ -[WFSendMessageAppIntentAction isApprovedForPublicShortcutsDrawer]
+ -[WFSetVolumeAction minimumSupportedClientVersion]
+ -[WFSetVolumeAction setAlarmsAndTimersVolume:]
+ -[WFSetVolumeAction setAlertsAndSystemSoundsVolume:]
+ GCC_except_table10024
+ GCC_except_table10373
+ GCC_except_table10376
+ GCC_except_table10377
+ GCC_except_table10412
+ GCC_except_table10413
+ GCC_except_table10416
+ GCC_except_table10419
+ GCC_except_table10420
+ GCC_except_table10421
+ GCC_except_table10422
+ GCC_except_table10423
+ GCC_except_table10424
+ GCC_except_table10425
+ GCC_except_table10426
+ GCC_except_table10547
+ GCC_except_table10548
+ GCC_except_table10549
+ GCC_except_table10550
+ GCC_except_table10569
+ GCC_except_table10577
+ GCC_except_table10590
+ GCC_except_table10663
+ GCC_except_table10668
+ GCC_except_table10672
+ GCC_except_table10683
+ GCC_except_table10769
+ GCC_except_table10773
+ GCC_except_table10777
+ GCC_except_table10787
+ GCC_except_table10791
+ GCC_except_table10804
+ GCC_except_table10812
+ GCC_except_table10891
+ GCC_except_table10929
+ GCC_except_table11066
+ GCC_except_table11120
+ GCC_except_table11135
+ GCC_except_table11187
+ GCC_except_table11190
+ GCC_except_table11193
+ GCC_except_table11197
+ GCC_except_table11218
+ GCC_except_table11220
+ GCC_except_table11244
+ GCC_except_table11245
+ GCC_except_table11246
+ GCC_except_table11247
+ GCC_except_table11248
+ GCC_except_table11250
+ GCC_except_table11267
+ GCC_except_table11272
+ GCC_except_table11279
+ GCC_except_table11280
+ GCC_except_table11346
+ GCC_except_table11349
+ GCC_except_table11352
+ GCC_except_table11355
+ GCC_except_table11378
+ GCC_except_table11480
+ GCC_except_table11484
+ GCC_except_table11486
+ GCC_except_table11488
+ GCC_except_table11502
+ GCC_except_table11573
+ GCC_except_table11595
+ GCC_except_table11602
+ GCC_except_table11633
+ GCC_except_table11635
+ GCC_except_table11655
+ GCC_except_table11673
+ GCC_except_table11698
+ GCC_except_table11703
+ GCC_except_table11808
+ GCC_except_table11852
+ GCC_except_table11882
+ GCC_except_table11886
+ GCC_except_table11888
+ GCC_except_table11939
+ GCC_except_table11942
+ GCC_except_table11945
+ GCC_except_table11948
+ GCC_except_table11959
+ GCC_except_table11962
+ GCC_except_table1220
+ GCC_except_table1328
+ GCC_except_table1384
+ GCC_except_table1387
+ GCC_except_table1449
+ GCC_except_table1470
+ GCC_except_table1484
+ GCC_except_table1499
+ GCC_except_table1502
+ GCC_except_table1503
+ GCC_except_table1505
+ GCC_except_table1518
+ GCC_except_table1526
+ GCC_except_table1532
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1558
+ GCC_except_table1559
+ GCC_except_table1560
+ GCC_except_table1575
+ GCC_except_table1644
+ GCC_except_table1658
+ GCC_except_table1748
+ GCC_except_table1749
+ GCC_except_table1830
+ GCC_except_table1915
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1992
+ GCC_except_table1996
+ GCC_except_table2013
+ GCC_except_table2027
+ GCC_except_table2030
+ GCC_except_table2034
+ GCC_except_table2052
+ GCC_except_table2101
+ GCC_except_table2135
+ GCC_except_table2159
+ GCC_except_table2164
+ GCC_except_table2176
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table2281
+ GCC_except_table2283
+ GCC_except_table2294
+ GCC_except_table2298
+ GCC_except_table2314
+ GCC_except_table2318
+ GCC_except_table2322
+ GCC_except_table2364
+ GCC_except_table2422
+ GCC_except_table2573
+ GCC_except_table266
+ GCC_except_table2690
+ GCC_except_table2709
+ GCC_except_table2712
+ GCC_except_table2886
+ GCC_except_table2887
+ GCC_except_table2890
+ GCC_except_table2963
+ GCC_except_table2986
+ GCC_except_table3000
+ GCC_except_table3001
+ GCC_except_table3083
+ GCC_except_table3089
+ GCC_except_table3145
+ GCC_except_table3188
+ GCC_except_table3213
+ GCC_except_table3248
+ GCC_except_table3261
+ GCC_except_table3267
+ GCC_except_table3273
+ GCC_except_table3276
+ GCC_except_table3278
+ GCC_except_table3308
+ GCC_except_table338
+ GCC_except_table348
+ GCC_except_table358
+ GCC_except_table4409
+ GCC_except_table4472
+ GCC_except_table4474
+ GCC_except_table4480
+ GCC_except_table4484
+ GCC_except_table4563
+ GCC_except_table4593
+ GCC_except_table4671
+ GCC_except_table4715
+ GCC_except_table4747
+ GCC_except_table4751
+ GCC_except_table4753
+ GCC_except_table4756
+ GCC_except_table4797
+ GCC_except_table4888
+ GCC_except_table5043
+ GCC_except_table5044
+ GCC_except_table5052
+ GCC_except_table5053
+ GCC_except_table5090
+ GCC_except_table5095
+ GCC_except_table5100
+ GCC_except_table5105
+ GCC_except_table5110
+ GCC_except_table5115
+ GCC_except_table5119
+ GCC_except_table5123
+ GCC_except_table5158
+ GCC_except_table5220
+ GCC_except_table5252
+ GCC_except_table5268
+ GCC_except_table5277
+ GCC_except_table5281
+ GCC_except_table5317
+ GCC_except_table5321
+ GCC_except_table5330
+ GCC_except_table5335
+ GCC_except_table5346
+ GCC_except_table5363
+ GCC_except_table5368
+ GCC_except_table5371
+ GCC_except_table5418
+ GCC_except_table5420
+ GCC_except_table5424
+ GCC_except_table5464
+ GCC_except_table5467
+ GCC_except_table5507
+ GCC_except_table5529
+ GCC_except_table5531
+ GCC_except_table5552
+ GCC_except_table5575
+ GCC_except_table5579
+ GCC_except_table5588
+ GCC_except_table5662
+ GCC_except_table5692
+ GCC_except_table5700
+ GCC_except_table5704
+ GCC_except_table5761
+ GCC_except_table5798
+ GCC_except_table5833
+ GCC_except_table5842
+ GCC_except_table5902
+ GCC_except_table5925
+ GCC_except_table5940
+ GCC_except_table6018
+ GCC_except_table6072
+ GCC_except_table6087
+ GCC_except_table6159
+ GCC_except_table6244
+ GCC_except_table6245
+ GCC_except_table6544
+ GCC_except_table6554
+ GCC_except_table6558
+ GCC_except_table6597
+ GCC_except_table6628
+ GCC_except_table6671
+ GCC_except_table6701
+ GCC_except_table6720
+ GCC_except_table6734
+ GCC_except_table6758
+ GCC_except_table6803
+ GCC_except_table6808
+ GCC_except_table6812
+ GCC_except_table6814
+ GCC_except_table6833
+ GCC_except_table6838
+ GCC_except_table6891
+ GCC_except_table6920
+ GCC_except_table6977
+ GCC_except_table6998
+ GCC_except_table7032
+ GCC_except_table7081
+ GCC_except_table7086
+ GCC_except_table7239
+ GCC_except_table7241
+ GCC_except_table7247
+ GCC_except_table7260
+ GCC_except_table7269
+ GCC_except_table7272
+ GCC_except_table7283
+ GCC_except_table7285
+ GCC_except_table7295
+ GCC_except_table7330
+ GCC_except_table7350
+ GCC_except_table7355
+ GCC_except_table7377
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7400
+ GCC_except_table7435
+ GCC_except_table7439
+ GCC_except_table7480
+ GCC_except_table7587
+ GCC_except_table7600
+ GCC_except_table7638
+ GCC_except_table7823
+ GCC_except_table7833
+ GCC_except_table7836
+ GCC_except_table7900
+ GCC_except_table8189
+ GCC_except_table8243
+ GCC_except_table8441
+ GCC_except_table8445
+ GCC_except_table8526
+ GCC_except_table8569
+ GCC_except_table8598
+ GCC_except_table8611
+ GCC_except_table8612
+ GCC_except_table8618
+ GCC_except_table8625
+ GCC_except_table8628
+ GCC_except_table8680
+ GCC_except_table8757
+ GCC_except_table8766
+ GCC_except_table8786
+ GCC_except_table8798
+ GCC_except_table8804
+ GCC_except_table8893
+ GCC_except_table8939
+ GCC_except_table8948
+ GCC_except_table9099
+ GCC_except_table9103
+ GCC_except_table9116
+ GCC_except_table9118
+ GCC_except_table9120
+ GCC_except_table9143
+ GCC_except_table9153
+ GCC_except_table9155
+ GCC_except_table9157
+ GCC_except_table9203
+ GCC_except_table9216
+ GCC_except_table9217
+ GCC_except_table9220
+ GCC_except_table9223
+ GCC_except_table9239
+ GCC_except_table9240
+ GCC_except_table9241
+ GCC_except_table9243
+ GCC_except_table9312
+ GCC_except_table9318
+ GCC_except_table9397
+ GCC_except_table9403
+ GCC_except_table9404
+ GCC_except_table9434
+ GCC_except_table9447
+ GCC_except_table9466
+ GCC_except_table9520
+ GCC_except_table9590
+ GCC_except_table9775
+ GCC_except_table9846
+ GCC_except_table9992
+ _MediaExperienceLibrary
+ _OBJC_CLASS_$_WFModelTranscriptContentItem
+ _OBJC_CLASS_$_WFScreenTimeHelper
+ _OUTLINED_FUNCTION_330
+ _OUTLINED_FUNCTION_464
+ _OUTLINED_FUNCTION_465
+ _OUTLINED_FUNCTION_466
+ _OUTLINED_FUNCTION_467
+ _OUTLINED_FUNCTION_468
+ _OUTLINED_FUNCTION_469
+ _OUTLINED_FUNCTION_470
+ _OUTLINED_FUNCTION_471
+ _OUTLINED_FUNCTION_472
+ _OUTLINED_FUNCTION_473
+ _OUTLINED_FUNCTION_474
+ _OUTLINED_FUNCTION_475
+ _OUTLINED_FUNCTION_476
+ _OUTLINED_FUNCTION_477
+ _OUTLINED_FUNCTION_478
+ _OUTLINED_FUNCTION_479
+ _OUTLINED_FUNCTION_480
+ _OUTLINED_FUNCTION_481
+ _WFVariableTypeCurrentApp
+ __OBJC_$_INSTANCE_METHODS_WFAskLLMAction(ActionKit|ActionKit1|ActionKit2)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WFHealthKitAccessResourceUserInterfaceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WFHealthKitAccessResourceUserInterfaceProtocol
+ __OBJC_$_PROTOCOL_REFS_WFHealthKitAccessResourceUserInterfaceProtocol
+ __OBJC_LABEL_PROTOCOL_$_WFHealthKitAccessResourceUserInterfaceProtocol
+ __OBJC_PROTOCOL_$_WFHealthKitAccessResourceUserInterfaceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_WFHealthKitAccessResourceUserInterfaceProtocol
+ ___52-[WFExtractTextFromImageAction parameterDefinitions]_block_invoke
+ ___80-[WFHealthKitAccessResource makeAvailableWithRemoteInterface:completionHandler:]_block_invoke
+ ___80-[WFHealthKitAccessResource requestHealthKitAuthorizationWithCompletionHandler:]_block_invoke
+ ___80-[WFHealthKitAccessResource requestHealthKitAuthorizationWithCompletionHandler:]_block_invoke_2
+ ___getAVSystemController_IsAlarmVolumeFollowingRingtoneVolumeAttributeSymbolLoc_block_invoke
+ ___getAVSystemController_IsSystemSoundsAndHapticsVolumeFollowingRingtoneVolumeAttributeSymbolLoc_block_invoke
+ _getAVSystemController_IsAlarmVolumeFollowingRingtoneVolumeAttributeSymbolLoc.ptr
+ _getAVSystemController_IsSystemSoundsAndHapticsVolumeFollowingRingtoneVolumeAttributeSymbolLoc.ptr
+ _objc_msgSend$areWebContentRestrictionsEnabled
+ _objc_msgSend$fileArchivingLocation
+ _objc_msgSend$isRateLimitedDeviceDetail
+ _objc_msgSend$linkValueFromParameterState:action:forUseCase:
+ _objc_msgSend$missingLocationErrorWithMissingOrigin:missingDestination:
+ _objc_msgSend$requestHealthKitAuthorizationWithCompletionHandler:
+ _objc_msgSend$requestHealthKitAuthorizationWithResourceDefinition:completionHandler:
+ _objc_msgSend$setAlarmsAndTimersVolume:
+ _objc_msgSend$setAlertsAndSystemSoundsVolume:
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setRenderAsMarkdown:
+ _objc_msgSend$wf_contentItemClassUsingOwnEntityMetadata
+ _symbolic _____Sg 12ModelCatalog17UseCaseIdentifierV
+ _symbolic _____Sg_ABt 10ContentKit21WFGenerativeModelNameO
+ _symbolic ______pSg 24GenerativePartnerService11LLMProviderP
- -[WFExtractTextFromImageAction parameterSummary]
- -[WFGetDistanceAction noLocationError]
- GCC_except_table10008
- GCC_except_table10357
- GCC_except_table10360
- GCC_except_table10361
- GCC_except_table10388
- GCC_except_table10396
- GCC_except_table10397
- GCC_except_table10400
- GCC_except_table10403
- GCC_except_table10405
- GCC_except_table10406
- GCC_except_table10407
- GCC_except_table10408
- GCC_except_table10409
- GCC_except_table10410
- GCC_except_table10531
- GCC_except_table10532
- GCC_except_table10533
- GCC_except_table10534
- GCC_except_table10553
- GCC_except_table10561
- GCC_except_table10574
- GCC_except_table10647
- GCC_except_table10652
- GCC_except_table10656
- GCC_except_table10667
- GCC_except_table10753
- GCC_except_table10757
- GCC_except_table10761
- GCC_except_table10771
- GCC_except_table10775
- GCC_except_table10788
- GCC_except_table10796
- GCC_except_table10875
- GCC_except_table10913
- GCC_except_table11050
- GCC_except_table11104
- GCC_except_table11119
- GCC_except_table11171
- GCC_except_table11174
- GCC_except_table11177
- GCC_except_table11181
- GCC_except_table11202
- GCC_except_table11204
- GCC_except_table11216
- GCC_except_table11228
- GCC_except_table11229
- GCC_except_table11230
- GCC_except_table11231
- GCC_except_table11234
- GCC_except_table11251
- GCC_except_table11256
- GCC_except_table11263
- GCC_except_table11264
- GCC_except_table11330
- GCC_except_table11333
- GCC_except_table11336
- GCC_except_table11339
- GCC_except_table11361
- GCC_except_table11461
- GCC_except_table11465
- GCC_except_table11467
- GCC_except_table11469
- GCC_except_table11483
- GCC_except_table11554
- GCC_except_table11576
- GCC_except_table11583
- GCC_except_table11614
- GCC_except_table11616
- GCC_except_table11636
- GCC_except_table11654
- GCC_except_table11679
- GCC_except_table11684
- GCC_except_table11789
- GCC_except_table11833
- GCC_except_table11862
- GCC_except_table11914
- GCC_except_table11917
- GCC_except_table11920
- GCC_except_table11923
- GCC_except_table11934
- GCC_except_table11937
- GCC_except_table1215
- GCC_except_table1323
- GCC_except_table1379
- GCC_except_table1382
- GCC_except_table1439
- GCC_except_table1465
- GCC_except_table1479
- GCC_except_table1487
- GCC_except_table1494
- GCC_except_table1498
- GCC_except_table1500
- GCC_except_table1508
- GCC_except_table1521
- GCC_except_table1522
- GCC_except_table1549
- GCC_except_table1550
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1553
- GCC_except_table1570
- GCC_except_table1639
- GCC_except_table1653
- GCC_except_table1739
- GCC_except_table1743
- GCC_except_table1825
- GCC_except_table1910
- GCC_except_table1972
- GCC_except_table1973
- GCC_except_table1987
- GCC_except_table1991
- GCC_except_table2008
- GCC_except_table2022
- GCC_except_table2025
- GCC_except_table2029
- GCC_except_table2047
- GCC_except_table2096
- GCC_except_table2128
- GCC_except_table2152
- GCC_except_table2157
- GCC_except_table2169
- GCC_except_table223
- GCC_except_table2274
- GCC_except_table2276
- GCC_except_table2284
- GCC_except_table2287
- GCC_except_table2307
- GCC_except_table2311
- GCC_except_table2315
- GCC_except_table2357
- GCC_except_table2415
- GCC_except_table2566
- GCC_except_table261
- GCC_except_table2683
- GCC_except_table2702
- GCC_except_table2705
- GCC_except_table2879
- GCC_except_table2880
- GCC_except_table2883
- GCC_except_table2956
- GCC_except_table2979
- GCC_except_table2987
- GCC_except_table2993
- GCC_except_table3076
- GCC_except_table3082
- GCC_except_table3138
- GCC_except_table3181
- GCC_except_table3206
- GCC_except_table3241
- GCC_except_table3247
- GCC_except_table3260
- GCC_except_table3266
- GCC_except_table3269
- GCC_except_table3271
- GCC_except_table3301
- GCC_except_table333
- GCC_except_table343
- GCC_except_table353
- GCC_except_table4402
- GCC_except_table4465
- GCC_except_table4467
- GCC_except_table4473
- GCC_except_table4477
- GCC_except_table4556
- GCC_except_table4586
- GCC_except_table4664
- GCC_except_table4708
- GCC_except_table4740
- GCC_except_table4744
- GCC_except_table4746
- GCC_except_table4749
- GCC_except_table4790
- GCC_except_table4881
- GCC_except_table5029
- GCC_except_table5037
- GCC_except_table5045
- GCC_except_table5046
- GCC_except_table5083
- GCC_except_table5088
- GCC_except_table5093
- GCC_except_table5098
- GCC_except_table5103
- GCC_except_table5108
- GCC_except_table5112
- GCC_except_table5116
- GCC_except_table5151
- GCC_except_table5213
- GCC_except_table5245
- GCC_except_table5261
- GCC_except_table5270
- GCC_except_table5274
- GCC_except_table5307
- GCC_except_table5310
- GCC_except_table5323
- GCC_except_table5328
- GCC_except_table5339
- GCC_except_table5356
- GCC_except_table5361
- GCC_except_table5364
- GCC_except_table5411
- GCC_except_table5413
- GCC_except_table5417
- GCC_except_table5457
- GCC_except_table5460
- GCC_except_table5500
- GCC_except_table5522
- GCC_except_table5524
- GCC_except_table5545
- GCC_except_table5568
- GCC_except_table5572
- GCC_except_table5581
- GCC_except_table5655
- GCC_except_table5685
- GCC_except_table5690
- GCC_except_table5693
- GCC_except_table5754
- GCC_except_table5791
- GCC_except_table5826
- GCC_except_table5835
- GCC_except_table5895
- GCC_except_table5918
- GCC_except_table5933
- GCC_except_table6011
- GCC_except_table6065
- GCC_except_table6080
- GCC_except_table6152
- GCC_except_table6237
- GCC_except_table6238
- GCC_except_table6530
- GCC_except_table6547
- GCC_except_table6551
- GCC_except_table6590
- GCC_except_table6621
- GCC_except_table6664
- GCC_except_table6694
- GCC_except_table6713
- GCC_except_table6727
- GCC_except_table6751
- GCC_except_table6796
- GCC_except_table6801
- GCC_except_table6805
- GCC_except_table6807
- GCC_except_table6826
- GCC_except_table6831
- GCC_except_table6884
- GCC_except_table6913
- GCC_except_table6970
- GCC_except_table6991
- GCC_except_table7025
- GCC_except_table7074
- GCC_except_table7079
- GCC_except_table7232
- GCC_except_table7233
- GCC_except_table7234
- GCC_except_table7253
- GCC_except_table7262
- GCC_except_table7265
- GCC_except_table7276
- GCC_except_table7278
- GCC_except_table7288
- GCC_except_table7323
- GCC_except_table7343
- GCC_except_table7348
- GCC_except_table7370
- GCC_except_table7371
- GCC_except_table7372
- GCC_except_table7393
- GCC_except_table7428
- GCC_except_table7432
- GCC_except_table7473
- GCC_except_table7580
- GCC_except_table7593
- GCC_except_table7631
- GCC_except_table7816
- GCC_except_table7819
- GCC_except_table7829
- GCC_except_table7893
- GCC_except_table8182
- GCC_except_table8236
- GCC_except_table8434
- GCC_except_table8438
- GCC_except_table8518
- GCC_except_table8561
- GCC_except_table8590
- GCC_except_table8603
- GCC_except_table8604
- GCC_except_table8609
- GCC_except_table8610
- GCC_except_table8620
- GCC_except_table8672
- GCC_except_table8749
- GCC_except_table8758
- GCC_except_table8778
- GCC_except_table8790
- GCC_except_table8796
- GCC_except_table8885
- GCC_except_table8931
- GCC_except_table8940
- GCC_except_table9090
- GCC_except_table9094
- GCC_except_table9098
- GCC_except_table9102
- GCC_except_table9109
- GCC_except_table9134
- GCC_except_table9144
- GCC_except_table9146
- GCC_except_table9148
- GCC_except_table9194
- GCC_except_table9205
- GCC_except_table9207
- GCC_except_table9208
- GCC_except_table9211
- GCC_except_table9230
- GCC_except_table9231
- GCC_except_table9232
- GCC_except_table9234
- GCC_except_table9296
- GCC_except_table9302
- GCC_except_table9381
- GCC_except_table9387
- GCC_except_table9388
- GCC_except_table9418
- GCC_except_table9431
- GCC_except_table9450
- GCC_except_table9504
- GCC_except_table9574
- GCC_except_table9759
- GCC_except_table9830
- GCC_except_table9976
- _OUTLINED_FUNCTION_342
- __OBJC_$_INSTANCE_METHODS_WFAskLLMAction(ActionKit|ActionKit1)
- ___78-[WFHealthKitAccessResource makeAvailableWithUserInterface:completionHandler:]_block_invoke
- ___78-[WFHealthKitAccessResource makeAvailableWithUserInterface:completionHandler:]_block_invoke_2
- _objc_msgSend$linkValueFromParameterState:action:
CStrings:
+ "%s Failed to set alarm volume coupling attribute: %@"
+ "%s Failed to set system sounds volume coupling attribute: %@"
+ "%s Unable to get HealthKit authorization request status: %{public}@"
+ "%s Unable to request HealthKit authorization: %{public}@"
+ "-[WFHealthKitAccessResource refreshAvailability]"
+ "-[WFHealthKitAccessResource requestHealthKitAuthorizationWithCompletionHandler:]"
+ "-[WFSetVolumeAction setAlarmsAndTimersVolume:]"
+ "-[WFSetVolumeAction setAlertsAndSystemSoundsVolume:]"
+ "5032.1"
+ "AVSystemController_IsAlarmVolumeFollowingRingtoneVolumeAttribute"
+ "AVSystemController_IsSystemSoundsAndHapticsVolumeFollowingRingtoneVolumeAttribute"
+ "Alarm"
+ "Alarms & Timers"
+ "Alerts & System Sounds"
+ "Allow “%1$@” to create an archive file?"
+ "Allow “%1$@” to store %2$@ in an archive file?"
+ "AutomationTools.Pro"
+ "AutomationTools.Zap"
+ "Can’t Write Health Data"
+ "Could not check usage limit as no model is currently serialized"
+ "Extract Text from Image"
+ "NSString *getAVSystemController_IsAlarmVolumeFollowingRingtoneVolumeAttribute(void)"
+ "NSString *getAVSystemController_IsSystemSoundsAndHapticsVolumeFollowingRingtoneVolumeAttribute(void)"
+ "No end location was specified."
+ "No start location was specified."
+ "No start or end location was specified."
+ "Selected Item"
+ "Selected Items"
+ "SystemSoundsAndHaptics"
+ "This type of Health data can’t be written to. Please choose a different type."
+ "Throwing WFAskLLMError.broadWorldKnowledgeRestricted because Assistant User Generated Content is disallowed by device management / parental controls."
+ "Throwing WFAskLLMError.webContentRestricted because Screen Time web content restrictions are enabled on this device."
+ "Unexpected model %{public}s when checking PCC usage limit"
+ "WFHealthKitAccessResourceUserInterface"
+ "WFHealthKitAccessResourceWatchUserInterface"
+ "WFSpotlightSearchAction: Mail routed to %{public}s"
+ "tables"
- "Extract from ${imageFile}"
- "Extract from ${imageFile} (Parameter Summary)"
- "Extract from Image"
- "The location specified in the Get Distance action could not be found."
- "WFSpotlightSearchAction: Mail routed to %{public}s (rdar://179176856)"
```
