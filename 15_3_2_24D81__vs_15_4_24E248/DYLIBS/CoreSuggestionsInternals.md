## CoreSuggestionsInternals

> `/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/Versions/A/CoreSuggestionsInternals`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x296c18
-  __TEXT.__auth_stubs: 0x23c0
-  __TEXT.__objc_methlist: 0x1424c
-  __TEXT.__const: 0x74aa
-  __TEXT.__gcc_except_tab: 0xb1a8
-  __TEXT.__cstring: 0x307da
-  __TEXT.__oslogstring: 0x21c7e
+1276.10.4.0.0
+  __TEXT.__text: 0x29b76c
+  __TEXT.__auth_stubs: 0x23a0
+  __TEXT.__objc_methlist: 0x157cc
+  __TEXT.__const: 0x749a
   __TEXT.__dlopen_cstrs: 0x2a1
+  __TEXT.__gcc_except_tab: 0xb148
+  __TEXT.__cstring: 0x30859
+  __TEXT.__oslogstring: 0x2248f
   __TEXT.__ustring: 0xc4
-  __TEXT.__unwind_info: 0x8260
-  __TEXT.__objc_classname: 0x29ac
-  __TEXT.__objc_methname: 0x3b4f9
-  __TEXT.__objc_methtype: 0x704f
-  __TEXT.__objc_stubs: 0x2a7e0
-  __DATA_CONST.__got: 0x2148
-  __DATA_CONST.__const: 0x4de0
-  __DATA_CONST.__objc_classlist: 0xb10
+  __TEXT.__unwind_info: 0x8168
+  __TEXT.__objc_classname: 0x29fa
+  __TEXT.__objc_methname: 0x3cf8b
+  __TEXT.__objc_methtype: 0x710f
+  __TEXT.__objc_stubs: 0x2b740
+  __DATA_CONST.__got: 0x2200
+  __DATA_CONST.__const: 0x4da8
+  __DATA_CONST.__objc_classlist: 0xb30
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce78
+  __DATA_CONST.__objc_selrefs: 0xd3e8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x750
+  __DATA_CONST.__objc_superrefs: 0x758
   __DATA_CONST.__objc_arraydata: 0x37c0
-  __AUTH_CONST.__auth_got: 0x11f8
-  __AUTH_CONST.__const: 0xc538
-  __AUTH_CONST.__cfstring: 0x255a0
-  __AUTH_CONST.__objc_const: 0x21628
-  __AUTH_CONST.__objc_intobj: 0x1050
+  __AUTH_CONST.__auth_got: 0x11e8
+  __AUTH_CONST.__const: 0xc568
+  __AUTH_CONST.__cfstring: 0x257a0
+  __AUTH_CONST.__objc_const: 0x1f9b0
+  __AUTH_CONST.__objc_intobj: 0x1260
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x58c0
+  __AUTH.__objc_data: 0x5a00
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0x1460
+  __DATA.__objc_ivar: 0x147c
   __DATA.__data: 0x1b60
-  __DATA.__bss: 0x9f90
+  __DATA.__bss: 0x9f98
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x1c8
-  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__bss: 0x188
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory
+  - /System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets
   - /System/Library/PrivateFrameworks/ContextKit.framework/Versions/A/ContextKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet

   - /System/Library/PrivateFrameworks/EmailCore.framework/Versions/A/EmailCore
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/InternationalTextSearch.framework/Versions/A/InternationalTextSearch
   - /System/Library/PrivateFrameworks/LanguageModeling.framework/Versions/A/LanguageModeling
   - /System/Library/PrivateFrameworks/Lexicon.framework/Versions/A/Lexicon

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2C7C20F8-4970-3FA1-A87E-EF3351C6C814
-  Functions: 10072
-  Symbols:   24278
-  CStrings:  22795
+  UUID: 7676A11A-3A5E-366F-9F24-CE961654747E
+  Functions: 10042
+  Symbols:   24515
+  CStrings:  23006
 
Symbols:
+ +[SGCascadeWritebackAdapter _loggingIdentifiersFromEvents:]
+ +[SGDSuggestManager filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:]
+ +[SGDSuggestManager filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:]
+ +[SGDSuggestManager filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealTime:]
+ +[SGEKCalendarAdapter _isStructuredEventEligibleForDonation:]
+ +[SGEntityTagsHelper extractSchemasFromEntityTags:]
+ +[SGEntityTagsHelper schemasInEntityTagsBelongsToPendingConfirmationEvent:]
+ +[SGEventSchemaCreator isTimePresentInDURawDateTime:]
+ -[SGAppointmentEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGBoatEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGBusEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGCarEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGCascadeWritebackAdapter _cascadeEntityItemsFromEvents:]
+ -[SGCascadeWritebackAdapter addEvent:]
+ -[SGCascadeWritebackAdapter addEvents:]
+ -[SGCascadeWritebackAdapter calendarDeleted]
+ -[SGCascadeWritebackAdapter cancelEvent:]
+ -[SGCascadeWritebackAdapter cancelEvents:]
+ -[SGCascadeWritebackAdapter confirmEventFromOtherDevice:]
+ -[SGCascadeWritebackAdapter confirmEventFromThisDevice:]
+ -[SGCascadeWritebackAdapter orphanEvent:]
+ -[SGCascadeWritebackAdapter rejectEventFromOtherDevice:]
+ -[SGCascadeWritebackAdapter rejectEventFromThisDevice:]
+ -[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:]
+ -[SGEKCalendarAdapter _newEventEligibleForDonation:]
+ -[SGEventDonationEnablementManager .cxx_destruct]
+ -[SGEventDonationEnablementManager initWithLLMPreferredLocales:]
+ -[SGEventDonationEnablementManager init]
+ -[SGEventDonationEnablementManager isLLMPreferredForLocale:]
+ -[SGEventDonationEnablementManager isLLMPreferredForLocale]
+ -[SGEventDonationEnablementManager isUnsupportedEventCategoryStatusForTextMessage:]
+ -[SGEventDonationEnablementManager llmPreferredLocales]
+ -[SGEventDonationEnablementManager overallUnsupportedCategories]
+ -[SGEventDonationEnablementManager overallUnsupportedStatuses]
+ -[SGEventDonationEnablementManager setLlmPreferredLocales:]
+ -[SGEventDonationEnablementManager setOverallUnsupportedCategories:]
+ -[SGEventDonationEnablementManager setOverallUnsupportedStatuses:]
+ -[SGEventDonationEnablementManager setTextMessageUnsupportedCategories:]
+ -[SGEventDonationEnablementManager setTextMessageUnsupportedStatuses:]
+ -[SGEventDonationEnablementManager textMessageUnsupportedCategories]
+ -[SGEventDonationEnablementManager textMessageUnsupportedStatuses]
+ -[SGExtractionDissector _completeRegexExtractionforMail:entity:forMail:]
+ -[SGExtractionDissector _isMailCategoryUnsupportedForLLMExtraction:]
+ -[SGExtractionDissector _shouldProcessMailMessage:havingSignificantSender:]
+ -[SGExtractionDissector _subjectResemblesForwardedMailSubjectForMail:]
+ -[SGExtractionDissector isMessageCandidateForExtraction:]
+ -[SGExtractionDissector mlExtractionEnabledForTextMessage]
+ -[SGFlightData synonymAirportNamesForAirportCode:]
+ -[SGFlightEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGHotelEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGInvitationEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGRestaurantEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGSimpleMailMessage mailCategories]
+ -[SGStorageEvent _appointmentEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _flightEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _hotelEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _partyEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _rentalCarEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _restaurantEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _ticketedShowEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent _ticketedTransportationEntityItemFromAttributeSet:error:]
+ -[SGStorageEvent cascadeEntityItemForEvent]
+ -[SGTicketEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGTicketedTransportationEventSchemaCreator _transportationSchemaCreatorFromTransportType:]
+ -[SGTicketedTransportationEventSchemaCreator reservationIDPresentInEventSchema:]
+ -[SGTrainEventSchemaCreator reservationIDPresentInEventSchema:]
+ GCC_except_table10031
+ GCC_except_table10033
+ GCC_except_table1026
+ GCC_except_table1152
+ GCC_except_table1169
+ GCC_except_table1187
+ GCC_except_table1214
+ GCC_except_table1269
+ GCC_except_table1326
+ GCC_except_table1351
+ GCC_except_table1369
+ GCC_except_table1372
+ GCC_except_table1380
+ GCC_except_table1407
+ GCC_except_table1451
+ GCC_except_table1485
+ GCC_except_table1589
+ GCC_except_table1645
+ GCC_except_table1669
+ GCC_except_table1683
+ GCC_except_table1685
+ GCC_except_table1692
+ GCC_except_table1694
+ GCC_except_table1703
+ GCC_except_table1706
+ GCC_except_table1707
+ GCC_except_table1712
+ GCC_except_table1713
+ GCC_except_table1715
+ GCC_except_table1716
+ GCC_except_table1718
+ GCC_except_table1722
+ GCC_except_table1725
+ GCC_except_table1727
+ GCC_except_table1731
+ GCC_except_table1772
+ GCC_except_table1782
+ GCC_except_table1784
+ GCC_except_table1833
+ GCC_except_table1860
+ GCC_except_table1861
+ GCC_except_table1862
+ GCC_except_table1863
+ GCC_except_table1864
+ GCC_except_table1867
+ GCC_except_table1869
+ GCC_except_table1944
+ GCC_except_table1946
+ GCC_except_table1955
+ GCC_except_table1956
+ GCC_except_table1976
+ GCC_except_table1977
+ GCC_except_table1990
+ GCC_except_table2002
+ GCC_except_table2007
+ GCC_except_table2011
+ GCC_except_table2013
+ GCC_except_table2014
+ GCC_except_table2023
+ GCC_except_table2033
+ GCC_except_table2034
+ GCC_except_table2035
+ GCC_except_table2080
+ GCC_except_table2087
+ GCC_except_table2091
+ GCC_except_table2181
+ GCC_except_table2192
+ GCC_except_table2195
+ GCC_except_table2196
+ GCC_except_table2212
+ GCC_except_table2215
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2330
+ GCC_except_table2350
+ GCC_except_table2353
+ GCC_except_table2356
+ GCC_except_table2357
+ GCC_except_table2361
+ GCC_except_table2365
+ GCC_except_table2369
+ GCC_except_table2370
+ GCC_except_table2372
+ GCC_except_table2373
+ GCC_except_table2378
+ GCC_except_table2379
+ GCC_except_table2381
+ GCC_except_table2393
+ GCC_except_table2466
+ GCC_except_table2467
+ GCC_except_table2470
+ GCC_except_table2476
+ GCC_except_table2477
+ GCC_except_table2478
+ GCC_except_table2480
+ GCC_except_table2481
+ GCC_except_table2482
+ GCC_except_table2483
+ GCC_except_table2484
+ GCC_except_table2487
+ GCC_except_table2488
+ GCC_except_table2490
+ GCC_except_table2542
+ GCC_except_table2549
+ GCC_except_table2551
+ GCC_except_table2553
+ GCC_except_table2557
+ GCC_except_table2573
+ GCC_except_table2575
+ GCC_except_table2577
+ GCC_except_table2579
+ GCC_except_table2581
+ GCC_except_table2583
+ GCC_except_table2585
+ GCC_except_table2588
+ GCC_except_table2590
+ GCC_except_table2618
+ GCC_except_table2666
+ GCC_except_table2672
+ GCC_except_table2674
+ GCC_except_table2690
+ GCC_except_table2694
+ GCC_except_table2705
+ GCC_except_table2737
+ GCC_except_table2762
+ GCC_except_table2768
+ GCC_except_table2770
+ GCC_except_table2773
+ GCC_except_table2782
+ GCC_except_table2830
+ GCC_except_table2836
+ GCC_except_table2857
+ GCC_except_table2867
+ GCC_except_table2893
+ GCC_except_table2898
+ GCC_except_table2907
+ GCC_except_table2915
+ GCC_except_table2919
+ GCC_except_table2936
+ GCC_except_table2941
+ GCC_except_table2956
+ GCC_except_table2966
+ GCC_except_table2968
+ GCC_except_table2971
+ GCC_except_table2995
+ GCC_except_table2998
+ GCC_except_table3003
+ GCC_except_table3007
+ GCC_except_table3020
+ GCC_except_table3049
+ GCC_except_table3057
+ GCC_except_table3078
+ GCC_except_table3091
+ GCC_except_table3095
+ GCC_except_table3100
+ GCC_except_table3102
+ GCC_except_table3125
+ GCC_except_table3225
+ GCC_except_table3249
+ GCC_except_table3258
+ GCC_except_table3259
+ GCC_except_table3260
+ GCC_except_table3314
+ GCC_except_table3324
+ GCC_except_table3329
+ GCC_except_table3338
+ GCC_except_table3339
+ GCC_except_table3342
+ GCC_except_table3409
+ GCC_except_table3609
+ GCC_except_table3614
+ GCC_except_table3622
+ GCC_except_table3676
+ GCC_except_table3680
+ GCC_except_table3684
+ GCC_except_table3686
+ GCC_except_table3694
+ GCC_except_table3697
+ GCC_except_table3698
+ GCC_except_table3706
+ GCC_except_table3735
+ GCC_except_table3755
+ GCC_except_table3757
+ GCC_except_table3760
+ GCC_except_table3762
+ GCC_except_table3773
+ GCC_except_table3790
+ GCC_except_table3807
+ GCC_except_table3844
+ GCC_except_table3850
+ GCC_except_table3907
+ GCC_except_table4005
+ GCC_except_table4027
+ GCC_except_table4034
+ GCC_except_table4043
+ GCC_except_table4047
+ GCC_except_table4050
+ GCC_except_table4076
+ GCC_except_table408
+ GCC_except_table4095
+ GCC_except_table4099
+ GCC_except_table4104
+ GCC_except_table4115
+ GCC_except_table4120
+ GCC_except_table413
+ GCC_except_table4132
+ GCC_except_table4134
+ GCC_except_table4138
+ GCC_except_table4140
+ GCC_except_table416
+ GCC_except_table4163
+ GCC_except_table4166
+ GCC_except_table4167
+ GCC_except_table4168
+ GCC_except_table4169
+ GCC_except_table4170
+ GCC_except_table4171
+ GCC_except_table4172
+ GCC_except_table4173
+ GCC_except_table4174
+ GCC_except_table4175
+ GCC_except_table4176
+ GCC_except_table4177
+ GCC_except_table4178
+ GCC_except_table4179
+ GCC_except_table4180
+ GCC_except_table4181
+ GCC_except_table4182
+ GCC_except_table4183
+ GCC_except_table4184
+ GCC_except_table4185
+ GCC_except_table4220
+ GCC_except_table4229
+ GCC_except_table423
+ GCC_except_table4238
+ GCC_except_table4245
+ GCC_except_table4257
+ GCC_except_table426
+ GCC_except_table4266
+ GCC_except_table4277
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table4321
+ GCC_except_table437
+ GCC_except_table4376
+ GCC_except_table4378
+ GCC_except_table4379
+ GCC_except_table4383
+ GCC_except_table4387
+ GCC_except_table4398
+ GCC_except_table4399
+ GCC_except_table4404
+ GCC_except_table4406
+ GCC_except_table4416
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4420
+ GCC_except_table4421
+ GCC_except_table4436
+ GCC_except_table4439
+ GCC_except_table4462
+ GCC_except_table4505
+ GCC_except_table4524
+ GCC_except_table4527
+ GCC_except_table4593
+ GCC_except_table4619
+ GCC_except_table4625
+ GCC_except_table4630
+ GCC_except_table4641
+ GCC_except_table4707
+ GCC_except_table4720
+ GCC_except_table4746
+ GCC_except_table4766
+ GCC_except_table4767
+ GCC_except_table4774
+ GCC_except_table4777
+ GCC_except_table4848
+ GCC_except_table4851
+ GCC_except_table4873
+ GCC_except_table4879
+ GCC_except_table4881
+ GCC_except_table4887
+ GCC_except_table5005
+ GCC_except_table5068
+ GCC_except_table5077
+ GCC_except_table5078
+ GCC_except_table5085
+ GCC_except_table5097
+ GCC_except_table5104
+ GCC_except_table5106
+ GCC_except_table5111
+ GCC_except_table5116
+ GCC_except_table5152
+ GCC_except_table5158
+ GCC_except_table5159
+ GCC_except_table5164
+ GCC_except_table5169
+ GCC_except_table5174
+ GCC_except_table526
+ GCC_except_table5293
+ GCC_except_table5297
+ GCC_except_table5298
+ GCC_except_table5299
+ GCC_except_table5312
+ GCC_except_table5337
+ GCC_except_table5372
+ GCC_except_table5374
+ GCC_except_table5384
+ GCC_except_table540
+ GCC_except_table5402
+ GCC_except_table544
+ GCC_except_table5448
+ GCC_except_table5507
+ GCC_except_table5512
+ GCC_except_table5515
+ GCC_except_table5518
+ GCC_except_table5522
+ GCC_except_table5531
+ GCC_except_table5551
+ GCC_except_table5559
+ GCC_except_table5562
+ GCC_except_table5565
+ GCC_except_table5597
+ GCC_except_table5630
+ GCC_except_table5645
+ GCC_except_table5652
+ GCC_except_table5669
+ GCC_except_table5677
+ GCC_except_table5684
+ GCC_except_table5692
+ GCC_except_table5701
+ GCC_except_table5709
+ GCC_except_table5722
+ GCC_except_table5725
+ GCC_except_table5730
+ GCC_except_table5755
+ GCC_except_table5784
+ GCC_except_table5797
+ GCC_except_table5882
+ GCC_except_table5911
+ GCC_except_table5914
+ GCC_except_table5916
+ GCC_except_table5921
+ GCC_except_table5924
+ GCC_except_table5930
+ GCC_except_table5932
+ GCC_except_table5934
+ GCC_except_table5997
+ GCC_except_table6007
+ GCC_except_table6019
+ GCC_except_table6021
+ GCC_except_table6025
+ GCC_except_table6029
+ GCC_except_table6031
+ GCC_except_table6033
+ GCC_except_table6035
+ GCC_except_table6037
+ GCC_except_table6039
+ GCC_except_table6041
+ GCC_except_table6047
+ GCC_except_table6091
+ GCC_except_table6107
+ GCC_except_table6110
+ GCC_except_table6128
+ GCC_except_table6144
+ GCC_except_table6147
+ GCC_except_table6157
+ GCC_except_table6160
+ GCC_except_table6168
+ GCC_except_table6181
+ GCC_except_table6185
+ GCC_except_table6197
+ GCC_except_table6247
+ GCC_except_table6248
+ GCC_except_table6251
+ GCC_except_table6253
+ GCC_except_table6254
+ GCC_except_table6396
+ GCC_except_table6406
+ GCC_except_table6409
+ GCC_except_table6413
+ GCC_except_table6414
+ GCC_except_table6425
+ GCC_except_table6435
+ GCC_except_table6448
+ GCC_except_table6453
+ GCC_except_table6461
+ GCC_except_table6489
+ GCC_except_table6493
+ GCC_except_table6552
+ GCC_except_table6554
+ GCC_except_table6557
+ GCC_except_table6562
+ GCC_except_table6568
+ GCC_except_table6588
+ GCC_except_table6594
+ GCC_except_table6597
+ GCC_except_table6608
+ GCC_except_table6612
+ GCC_except_table6618
+ GCC_except_table6627
+ GCC_except_table6642
+ GCC_except_table6643
+ GCC_except_table667
+ GCC_except_table6671
+ GCC_except_table6679
+ GCC_except_table6713
+ GCC_except_table6719
+ GCC_except_table6725
+ GCC_except_table6731
+ GCC_except_table6733
+ GCC_except_table6734
+ GCC_except_table6735
+ GCC_except_table6736
+ GCC_except_table6742
+ GCC_except_table6744
+ GCC_except_table6745
+ GCC_except_table6750
+ GCC_except_table6766
+ GCC_except_table6768
+ GCC_except_table677
+ GCC_except_table6803
+ GCC_except_table6817
+ GCC_except_table6819
+ GCC_except_table6845
+ GCC_except_table6848
+ GCC_except_table6850
+ GCC_except_table6852
+ GCC_except_table6855
+ GCC_except_table6857
+ GCC_except_table6859
+ GCC_except_table6861
+ GCC_except_table6871
+ GCC_except_table690
+ GCC_except_table6903
+ GCC_except_table6905
+ GCC_except_table6907
+ GCC_except_table6909
+ GCC_except_table6933
+ GCC_except_table6934
+ GCC_except_table6936
+ GCC_except_table695
+ GCC_except_table6951
+ GCC_except_table6954
+ GCC_except_table697
+ GCC_except_table702
+ GCC_except_table704
+ GCC_except_table7094
+ GCC_except_table7095
+ GCC_except_table7130
+ GCC_except_table7133
+ GCC_except_table7205
+ GCC_except_table7240
+ GCC_except_table7245
+ GCC_except_table7248
+ GCC_except_table7251
+ GCC_except_table7254
+ GCC_except_table7285
+ GCC_except_table7330
+ GCC_except_table7344
+ GCC_except_table7350
+ GCC_except_table736
+ GCC_except_table740
+ GCC_except_table742
+ GCC_except_table744
+ GCC_except_table746
+ GCC_except_table750
+ GCC_except_table7533
+ GCC_except_table7542
+ GCC_except_table7561
+ GCC_except_table7589
+ GCC_except_table7590
+ GCC_except_table7591
+ GCC_except_table7604
+ GCC_except_table7606
+ GCC_except_table7608
+ GCC_except_table7741
+ GCC_except_table7745
+ GCC_except_table7758
+ GCC_except_table7804
+ GCC_except_table7911
+ GCC_except_table7950
+ GCC_except_table7955
+ GCC_except_table7964
+ GCC_except_table7998
+ GCC_except_table8002
+ GCC_except_table8019
+ GCC_except_table8035
+ GCC_except_table8046
+ GCC_except_table8048
+ GCC_except_table8050
+ GCC_except_table8061
+ GCC_except_table8063
+ GCC_except_table8089
+ GCC_except_table8094
+ GCC_except_table8098
+ GCC_except_table8108
+ GCC_except_table8115
+ GCC_except_table8119
+ GCC_except_table8126
+ GCC_except_table8133
+ GCC_except_table8142
+ GCC_except_table8146
+ GCC_except_table8149
+ GCC_except_table8152
+ GCC_except_table8161
+ GCC_except_table8170
+ GCC_except_table8176
+ GCC_except_table8188
+ GCC_except_table8190
+ GCC_except_table8198
+ GCC_except_table8202
+ GCC_except_table8204
+ GCC_except_table8207
+ GCC_except_table8214
+ GCC_except_table8219
+ GCC_except_table8225
+ GCC_except_table8239
+ GCC_except_table8276
+ GCC_except_table8277
+ GCC_except_table8282
+ GCC_except_table8286
+ GCC_except_table8291
+ GCC_except_table8305
+ GCC_except_table8321
+ GCC_except_table8332
+ GCC_except_table8351
+ GCC_except_table8353
+ GCC_except_table8354
+ GCC_except_table8355
+ GCC_except_table8356
+ GCC_except_table8357
+ GCC_except_table8360
+ GCC_except_table8362
+ GCC_except_table8364
+ GCC_except_table8367
+ GCC_except_table8370
+ GCC_except_table8373
+ GCC_except_table8374
+ GCC_except_table8375
+ GCC_except_table8377
+ GCC_except_table8379
+ GCC_except_table8380
+ GCC_except_table8381
+ GCC_except_table8382
+ GCC_except_table8383
+ GCC_except_table8384
+ GCC_except_table8385
+ GCC_except_table8386
+ GCC_except_table8387
+ GCC_except_table8388
+ GCC_except_table8389
+ GCC_except_table8403
+ GCC_except_table8416
+ GCC_except_table844
+ GCC_except_table8497
+ GCC_except_table8501
+ GCC_except_table8518
+ GCC_except_table8525
+ GCC_except_table8526
+ GCC_except_table8530
+ GCC_except_table855
+ GCC_except_table8565
+ GCC_except_table858
+ GCC_except_table8585
+ GCC_except_table8615
+ GCC_except_table8621
+ GCC_except_table8629
+ GCC_except_table863
+ GCC_except_table8630
+ GCC_except_table8633
+ GCC_except_table8648
+ GCC_except_table8652
+ GCC_except_table8667
+ GCC_except_table8677
+ GCC_except_table868
+ GCC_except_table8697
+ GCC_except_table8702
+ GCC_except_table8721
+ GCC_except_table8725
+ GCC_except_table8744
+ GCC_except_table8749
+ GCC_except_table8761
+ GCC_except_table877
+ GCC_except_table8840
+ GCC_except_table8850
+ GCC_except_table8874
+ GCC_except_table8875
+ GCC_except_table8879
+ GCC_except_table8880
+ GCC_except_table8893
+ GCC_except_table8908
+ GCC_except_table8922
+ GCC_except_table8932
+ GCC_except_table8953
+ GCC_except_table8971
+ GCC_except_table8976
+ GCC_except_table8977
+ GCC_except_table8981
+ GCC_except_table8982
+ GCC_except_table8985
+ GCC_except_table9053
+ GCC_except_table9065
+ GCC_except_table9088
+ GCC_except_table9089
+ GCC_except_table9093
+ GCC_except_table9095
+ GCC_except_table9156
+ GCC_except_table9181
+ GCC_except_table9203
+ GCC_except_table9208
+ GCC_except_table9211
+ GCC_except_table9212
+ GCC_except_table9213
+ GCC_except_table9215
+ GCC_except_table9216
+ GCC_except_table9217
+ GCC_except_table9220
+ GCC_except_table9224
+ GCC_except_table9225
+ GCC_except_table9226
+ GCC_except_table9253
+ GCC_except_table9316
+ GCC_except_table9318
+ GCC_except_table9319
+ GCC_except_table9322
+ GCC_except_table9331
+ GCC_except_table9332
+ GCC_except_table9333
+ GCC_except_table9347
+ GCC_except_table9349
+ GCC_except_table9351
+ GCC_except_table9352
+ GCC_except_table9354
+ GCC_except_table9359
+ GCC_except_table9360
+ GCC_except_table9362
+ GCC_except_table9365
+ GCC_except_table9366
+ GCC_except_table9371
+ GCC_except_table9372
+ GCC_except_table9373
+ GCC_except_table9383
+ GCC_except_table9384
+ GCC_except_table9389
+ GCC_except_table9390
+ GCC_except_table9410
+ GCC_except_table9415
+ GCC_except_table9429
+ GCC_except_table9517
+ GCC_except_table9519
+ GCC_except_table9521
+ GCC_except_table9523
+ GCC_except_table9525
+ GCC_except_table9527
+ GCC_except_table9529
+ GCC_except_table9531
+ GCC_except_table9533
+ GCC_except_table9535
+ GCC_except_table9537
+ GCC_except_table9539
+ GCC_except_table9541
+ GCC_except_table9543
+ GCC_except_table9545
+ GCC_except_table9547
+ GCC_except_table9549
+ GCC_except_table9551
+ GCC_except_table9553
+ GCC_except_table9555
+ GCC_except_table9557
+ GCC_except_table9559
+ GCC_except_table9561
+ GCC_except_table9563
+ GCC_except_table9569
+ GCC_except_table9573
+ GCC_except_table9575
+ GCC_except_table9622
+ GCC_except_table9625
+ GCC_except_table9627
+ GCC_except_table9628
+ GCC_except_table9631
+ GCC_except_table9651
+ GCC_except_table9670
+ GCC_except_table9846
+ GCC_except_table9855
+ GCC_except_table9860
+ OBJC_IVAR_$_SGDSpotlightReceiver._summarizationPipeline
+ OBJC_IVAR_$_SGEventDonationEnablementManager._llmPreferredLocales
+ OBJC_IVAR_$_SGEventDonationEnablementManager._overallUnsupportedCategories
+ OBJC_IVAR_$_SGEventDonationEnablementManager._overallUnsupportedStatuses
+ OBJC_IVAR_$_SGEventDonationEnablementManager._textMessageUnsupportedCategories
+ OBJC_IVAR_$_SGEventDonationEnablementManager._textMessageUnsupportedStatuses
+ OBJC_IVAR_$_SGSimpleMailMessage._mailCategories
+ ProactiveSummarizationLibraryCore.frameworkLibrary.32907
+ SGNotUserInitiated._pasExprOnceResult.5
+ _DUExtractionAttributeKeyDetailedEventStatus
+ _DUExtractionAttributeValueEventStatusOther
+ _DUExtractionAttributeValueEventStatusPendingCancellation
+ _DUExtractionAttributeValueEventStatusPendingConfirmation
+ _DUExtractionAttributeValueEventStatusPostEventSummary
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityAppointment
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityContent
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityFlightReservation
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityHotelReservation
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityMetaContent
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityParty
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityRentalCarReservation
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityRestaurantReservation
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityTicketedShow
+ _OBJC_CLASS_$_CCAppIntentsExtractedEntityTicketedTransportation
+ _OBJC_CLASS_$_CCFullSetDonation
+ _OBJC_CLASS_$_CCIncrementalSetDonation
+ _OBJC_CLASS_$_CCItemInstance
+ _OBJC_CLASS_$_CCSetDonation
+ _OBJC_CLASS_$_SGCascadeWritebackAdapter
+ _OBJC_CLASS_$_SGEntityTagsHelper
+ _OBJC_CLASS_$_SGEventDonationEnablementManager
+ _OBJC_CLASS_$_SGEventSchemaCreator
+ _OBJC_METACLASS_$_SGCascadeWritebackAdapter
+ _OBJC_METACLASS_$_SGEntityTagsHelper
+ _OBJC_METACLASS_$_SGEventDonationEnablementManager
+ _OBJC_METACLASS_$_SGEventSchemaCreator
+ _PASValidatedFormat.38112
+ __102-[SGMIFeatureStore _highlyDiscriminantTokensForFeature:minCount:minRatio:domains:limit:usingDatabase:]_block_invoke.553
+ __102-[SGMessageEventDissector logMLMessageEventExtractionForSchema:message:category:timingProcessingInMs:]_block_invoke.362
+ __103-[SGDetectedAttributeDissector handleTextMessageBirthdayCongratulation:entity:withConversationHistory:]_block_invoke.138
+ __104-[SGDSuggestManager waitForEventWithIdentifier:toAppearInEventStoreWithLastModificationDate:completion:]_block_invoke.838
+ __104-[SGSqlEntityStore initWithEntityDbPath:snippetDbPath:isEphemeral:sharedLock:executeJournals:noMigrate:]_block_invoke.104
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.269
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.276
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.283
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.290
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.297
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.304
+ __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.311
+ __105-[SGSqlEntityStore(Spotlight) domainIdentifierForSpotlightReferenceForBundleIdentifier:uniqueIdentifier:]_block_invoke.11
+ __105-[SGSqlEntityStore(Spotlight) domainIdentifierForSpotlightReferenceForBundleIdentifier:uniqueIdentifier:]_block_invoke.13
+ __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke.290
+ __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke.292
+ __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke_2.295
+ __107-[SGDSuggestManager namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.638
+ __111-[SGSqlEntityStore(IdentityStore) registerAndLinkIdentity:recordId:phones:socialProfiles:email:curated:isSent:]_block_invoke.141
+ __111-[SGSqlEntityStore(IdentityStore) registerAndLinkIdentity:recordId:phones:socialProfiles:email:curated:isSent:]_block_invoke.149
+ __111-[SGSqlEntityStore(Spotlight) _recordIdsFromRemovingSpotlightReferencesWithBundleIdentifier:uniqueIdentifiers:]_block_invoke.137
+ __112+[SGDetection detectionWithType:text:matchRange:matchString:label:hasPhoneLabel:extractionInfo:isUnlikelyPhone:]_block_invoke.5
+ __112-[SGSqlEntityStore(SpotlightMapping) commitSpotlightMapping:bundleIdentifier:domainIdentifier:uniqueIdentifier:]_block_invoke.51
+ __115-[SGDetectedAttributeML detectionFromMessage:ddMatch:matchedContext:withSupervision:inConversation:entityLanguage:]_block_invoke.136
+ __115-[SGDetectedAttributeML detectionFromMessage:ddMatch:matchedContext:withSupervision:inConversation:entityLanguage:]_block_invoke.140
+ __116-[SGSqlEntityStore(Deleting) deleteEntitiesByDuplicateKey:preserveEventConfirmationHistory:emitChangeNotifications:]_block_invoke.290
+ __121-[SGSqlEntityStore(Saliency) sortedSaliencyResultsRestrictedToMailboxTypes:mailboxIds:receivedOnOrAfter:ascending:limit:]_block_invoke.75
+ __122-[SGSqlEntityStore(Spotlight) tombstoneExistsForSpotlightReferenceWithBundleIdentifier:uniqueIdentifier:domainIdentifier:]_block_invoke.243
+ __124-[SGSqlEntityStore(URLs) urlsFoundBetweenStartDate:endDate:excludingBundleIdentifiers:containingSubstring:flagFilter:limit:]_block_invoke.34
+ __125-[SGSqlEntityStore(Spotlight) reindexSearchableItemsWithMinimumEntityId:searchableIndex:acknowledgementHandler:reindexCount:]_block_invoke.278
+ __125-[SGSqlEntityStore(Spotlight) reindexSearchableItemsWithMinimumEntityId:searchableIndex:acknowledgementHandler:reindexCount:]_block_invoke.282
+ __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.585
+ __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.655
+ __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.716
+ __131+[SGCuratedContactMatcher _compareContact:cnContact:newDetails:matchedDetails:matchPreference:stopOnNewDetail:stopOnMatchedDetail:]_block_invoke.39
+ __132+[SGWordBoundaryQuickTypeInference quickTypeTriggerForContext:localeIdentifier:modelConfigPath:espressoBinFilePath:useContactNames:]_block_invoke.31
+ __132+[SGWordBoundaryQuickTypeInference quickTypeTriggerForContext:localeIdentifier:modelConfigPath:espressoBinFilePath:useContactNames:]_block_invoke.33
+ __136-[SGDSuggestManager(RealtimeDonations) suggestionsFromSingleMessage:options:completionDelivery:completionHandler:fullCompletionHandler:]_block_invoke.47
+ __139+[SGMISpotlightUtility queryEmailsFromDaysAgo:throughDaysAgo:fetchAttributes:filterQuery:queryString:bundleIds:spotlightTimeOut:withError:]_block_invoke.55
+ __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.60
+ __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.62
+ __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.64
+ __146-[SGDSuggestManager(BatchDonations) batchSuggestionsFromMessages:options:completionDelivery:batchCompletion:writeBackCompletion:shouldStopSignal:]_block_invoke.31
+ __153-[SGDSuggestManager(RealtimeDonations) _suggestionsFromSingleSearchableItem:options:dissectIfNecessary:processingType:completionDelivery:withCompletion:]_block_invoke.20
+ __165+[SGMISubmodelsManager incrementalSubmodelUpdateWithSaliencyModelConfig:store:shouldContinue:finalGroundTruthDate:withSimulatedCSSearchableItemForTesting:limit:log:]_block_invoke.46
+ __187-[SGDSuggestManager(BatchDonations) batchSuggestionsFromSearchableItems:options:dissectIfNecessary:processingType:completionDelivery:batchCompletion:writeBackCompletion:shouldStopSignal:]_block_invoke.25
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.118
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.122
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.127
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.132
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.136
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.137
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.87
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.96
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_2.88
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_2.97
+ __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_3.98
+ __20-[SGFlightData init]_block_invoke.83
+ __20-[SGFlightData init]_block_invoke.95
+ __20-[SGFlightData init]_block_invoke.96
+ __20-[SGFlightData init]_block_invoke_2.91
+ __223+[SGMIOmissionAnalyzer identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.13
+ __223+[SGMIOmissionAnalyzer identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.16
+ __224+[SGMIOmissionAnalyzer _identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.59
+ __23-[SGDCloudKitSync init]_block_invoke.247
+ __23-[SGDCloudKitSync init]_block_invoke.252
+ __25-[SGAccountsAdapter init]_block_invoke.10
+ __253-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:]_block_invoke.583
+ __26-[SGSqliteDatabase vacuum]_block_invoke.210
+ __26-[SGSqliteDatabase vacuum]_block_invoke.218
+ __26-[SGSqliteDatabase vacuum]_block_invoke_2.214
+ __26-[SGSqliteDatabase vacuum]_block_invoke_2.219
+ __27-[SGPatterns regex2ForKey:]_block_invoke.122
+ __27-[SGReverseTemplateJS init]_block_invoke.13
+ __28-[SGDSpotlightReceiver init]_block_invoke.16
+ __28-[SGDSpotlightReceiver init]_block_invoke.26
+ __28-[SGDSpotlightReceiver init]_block_invoke.31
+ __28-[SGDSpotlightReceiver init]_block_invoke.35
+ __28-[SGDSpotlightReceiver init]_block_invoke_2.25
+ __28-[SGDSpotlightReceiver init]_block_invoke_2.34
+ __29-[SGMIFeatureVector feature:]_block_invoke.50
+ __29-[SGMIFeatureVector feature:]_block_invoke.53
+ __29-[SGMIFeatureVector feature:]_block_invoke.71
+ __30-[SGDCloudKitSync accountInfo]_block_invoke.278
+ __30-[SGDCloudKitSync privacySalt]_block_invoke.377
+ __30-[SGDCloudKitSync privacySalt]_block_invoke.378
+ __30-[SGDCloudKitSync privacySalt]_block_invoke.381
+ __30-[SGDCloudKitSync privacySalt]_block_invoke.385
+ __30-[SGDOMParser _parseDocument:]_block_invoke.20
+ __31+[SGPipeline parallelPipeline:]_block_invoke.57
+ __31-[SGDCloudKitSync setDatabase:]_block_invoke.313
+ __31-[SGDCloudKitSync setDatabase:]_block_invoke.314
+ __31-[SGDCloudKitSync setDatabase:]_block_invoke.330
+ __31-[SGDCloudKitSync setDatabase:]_block_invoke.331
+ __31-[SGDCloudKitSync setDatabase:]_block_invoke.335
+ __32+[SGDomainWhitelistChecker lock]_block_invoke.12
+ __33+[SGDSuggestManager requestCache]_block_invoke.238
+ __33+[SGDSuggestManager requestCache]_block_invoke_2.239
+ __33-[SGDCloudKitSync deleteGroupId:]_block_invoke.348
+ __33-[SGDCloudKitSync deleteGroupId:]_block_invoke.352
+ __34-[SGSqliteDatabase maxIdForTable:]_block_invoke.180
+ __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.77
+ __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.80
+ __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.81
+ __36+[SGNames stripAndReturnHonorifics:]_block_invoke.75
+ __36+[SGNames stripAndReturnHonorifics:]_block_invoke.77
+ __36-[SGSqlEntityStore(Tags) commitTag:]_block_invoke.12
+ __37+[SGThreadParser nextMessage:entity:]_block_invoke.23
+ __38-[SGDCloudKitSync processStateChanges]_block_invoke.270
+ __38-[SGDCloudKitSync processStateChanges]_block_invoke.271
+ __39-[SGIdentityName initWithJapaneseName:]_block_invoke.86
+ __39-[SGPipeline _dissectOperations:block:]_block_invoke.70
+ __39-[SGPipeline _dissectOperations:block:]_block_invoke.71
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.108
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.115
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.124
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.173
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.203
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.269
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.282
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.289
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.80
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.84
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.95
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.132
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.178
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.213
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.88
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_3.191
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_3.220
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_4.227
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_5.233
+ __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_6.239
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.109
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.122
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.131
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.141
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.160
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.170
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.180
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.193
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.206
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.225
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.234
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.88
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.95
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.135
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.145
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.164
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.174
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.184
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.197
+ __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.210
+ __40-[SGDSuggestManager bumptTTLForNLEvent:]_block_invoke.571
+ __40-[SGMailClientUtil allVIPEmailAddresses]_block_invoke.19
+ __40-[SGSqlEntityStore(Events) insertEvent:]_block_invoke.25
+ __41-[SGDCloudKitSync addCreateZoneOperation]_block_invoke.157
+ __41-[SGDCloudKitSync addDeleteZoneOperation]_block_invoke.146
+ __41-[SGDManagerForCTS _performTrimActivity:]_block_invoke.46
+ __41-[SGDManagerForCTS _performTrimActivity:]_block_invoke.55
+ __41-[SGSqlEntityStore(Writing) writeEntity:]_block_invoke.45
+ __41-[SGSqlEntityStore(Writing) writeEntity:]_block_invoke.49
+ __42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.281
+ __42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.282
+ __42+[SGModel transformerInstanceForLanguage:]_block_invoke.41
+ __42+[SGModel transformerInstanceForLanguage:]_block_invoke_2.43
+ __43+[SGPatterns pauseCacheEvictionTemporarily]_block_invoke.129
+ __43-[SGMIFeatureStore warningStatsForLogging:]_block_invoke.643
+ __43-[SGReverseTemplateJS emailToOutput:reply:]_block_invoke.547
+ __43-[SGSqlEntityStore(Reminders) getReminder:]_block_invoke.11
+ __43-[SGSqlEntityStore(SqlHelpers) entityCount]_block_invoke.67
+ __44-[SGDManagerForCTS _performSendRTCActivity:]_block_invoke.66
+ __45-[SGCNContactIdentifierCollection proxyArray]_block_invoke.13
+ __45-[SGReminderTrialClientWrapper updateFactors]_block_invoke.61
+ __45-[SGSqlEntityStore emailsPendingVerification]_block_invoke.156
+ __45-[SGSqlEntityStore(DatabaseMigrator) migrate]_block_invoke.166
+ __46-[SGDatabaseJournal executeQueriesOnDatabase:]_block_invoke.63
+ __46-[SGSqlEntityStore(Spotlight) recordIdForKey:]_block_invoke.88
+ __46-[SGSqlEntityStore(SqlHelpers) clearAllTables]_block_invoke.295
+ __47-[SGDCloudKitSync addFetchNewEntitiesOperation]_block_invoke.194
+ __47-[SGDCloudKitSync addFetchNewEntitiesOperation]_block_invoke.203
+ __47-[SGSqlEntityStore(Loading) _loadMessageByKey:]_block_invoke.110
+ __47-[SGSqlEntityStore(Tags) loadTagForPrimaryKey:]_block_invoke.18
+ __47-[SGSqlEntityStore(Writing) _loadIdentityBlobs]_block_invoke.394
+ __47-[SGSqlEntityStore(Writing) _loadIdentityBlobs]_block_invoke_2.399
+ __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_2.36
+ __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_3.40
+ __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_4.43
+ __48+[SGMailClientUtil convertLineEndingsToNetwork:]_block_invoke.45
+ __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.161
+ __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.168
+ __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.169
+ __49-[SGDCloudKitSync createSubscriptionWithRetries:]_block_invoke.299
+ __49-[SGMIDomainCountingTable deleteDomainSelection:]_block_invoke.378
+ __49-[SGSqlEntityStore confirmRealtimeContact:error:]_block_invoke.600
+ __49-[SGSqlEntityStore(IdentityStore) loadInterdicts]_block_invoke.62
+ __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke.410
+ __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke.421
+ __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke_2.411
+ __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke_2.422
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.22
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.25
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.26
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_2.23
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_2.27
+ __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_3.24
+ __50-[SGDCloudKitSync addEnrichment:withParentEntity:]_block_invoke.338
+ __50-[SGDCloudKitSync addEnrichment:withParentEntity:]_block_invoke.346
+ __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.105
+ __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.106
+ __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.119
+ __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.128
+ __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.129
+ __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.54
+ __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.62
+ __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.63
+ __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke_2.55
+ __51-[SGSqlEntityStore(Events) updateEvent:primaryKey:]_block_invoke.10
+ __51-[SGSqlEntityStore(Saliency) saliencyForMessageId:]_block_invoke.27
+ __52+[SGDCloudKitSync apsEnvironmentStringForContainer:]_block_invoke.291
+ __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.36
+ __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.59
+ __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.64
+ __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.68
+ __52-[SGSqlEntityStore(Deleting) childrenFromParentKey:]_block_invoke.108
+ __52-[SGSqlEntityStore(IdentityStore) _computeBlobsRaw:]_block_invoke.305
+ __52-[SGSqlEntityStore(IdentityStore) _computeBlobsRaw:]_block_invoke_2.306
+ __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.223
+ __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.227
+ __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.237
+ __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.246
+ __52-[SGStructuredEventTrialClientWrapper updateFactors]_block_invoke.47
+ __53-[NSMutableString(EncodedWord) sg_decodeEncodedWords]_block_invoke.19
+ __53-[SGDSuggestManager messagesToRefreshWithCompletion:]_block_invoke.668
+ __53-[SGDSuggestManager updateMessages:state:completion:]_block_invoke.678
+ __53-[SGMIFeatureStore shouldExposeWarning:updateAction:]_block_invoke.606
+ __53-[SGMIFeatureStore shouldExposeWarning:updateAction:]_block_invoke_2.608
+ __53-[SGSqlEntityStore(Loading) loadSourceKeyByRecordId:]_block_invoke.26
+ __53-[SGSqlEntityStore(Reminders) commitStorageReminder:]_block_invoke.33
+ __53-[SGSqlEntityStore(Writing) _writeMessageEntityToDb:]_block_invoke.223
+ __53-[SGSqlEntityStore(Writing) _writeMessageEntityToDb:]_block_invoke_2.271
+ __54-[SGSqlEntityStore(DatabaseMigrator) _renameTable:to:]_block_invoke.114
+ __54-[SGSqlEntityStore(DatabaseMigrator) migrateDatabases]_block_invoke.9
+ __55+[SGMISpotlightUtility itemWithUniqueIdentifier:error:]_block_invoke.43
+ __55-[SGSqlEntityStore mostRecentParentKeyForDuplicateKey:]_block_invoke.168
+ __55-[SGSqlEntityStore(Spotlight) contactsWithIdentifiers:]_block_invoke.266
+ __55-[SGSqlEntityStore(Spotlight) contactsWithIdentifiers:]_block_invoke.271
+ __56-[SGExtractionDissector jsonLdOutputFromPackedJSEntity:]_block_invoke.930
+ __56-[SGSqlEntityStore(ContactDetails) commitContactDetail:]_block_invoke.18
+ __56-[SGSqlEntityStore(IdentityStore) rebuildIdentityTables]_block_invoke.130
+ __56-[SGSqlEntityStore(Loading) loadDuplicateKeyByRecordId:]_block_invoke.12
+ __57-[SGDSuggestManager addInteractions:bundleId:completion:]_block_invoke.776
+ __57-[SGMIFeatureStore _getSGMIStoredAddressesUsingDatabase:]_block_invoke.757
+ __57-[SGSqlEntityStore(IdentityStore) link:to:type:strength:]_block_invoke.215
+ __57-[SGSqlEntityStore(MessageManagement) markMessagesFound:]_block_invoke.84
+ __57-[SGSqlEntityStore(TestHelpers) lastSeenTimestampForKey:]_block_invoke.12
+ __57-[SGSqliteDatabase prepAndRunQuery:onPrep:onRow:onError:]_block_invoke.116
+ __58+[SGMIBiomeUtility summarizeStreamByMessageWithPublisher:]_block_invoke.17
+ __58+[SGSimpleMailMessage(RFC822Parsing) dateFromEmailString:]_block_invoke.141
+ __58-[SGPOSTagger tokenizeTextContent:languageHint:gazetteer:]_block_invoke.17
+ __58-[SGPOSTagger tokenizeTextContent:languageHint:gazetteer:]_block_invoke.18
+ __58-[SGSqlEntityStore _rankSGContacts:bySimilarityToContact:]_block_invoke.318
+ __58-[SGSqlEntityStore(DatabaseMigrator) selectMigrationQueue]_block_invoke.22
+ __58-[SGSqlEntityStore(ExtractionInfos) commitExtractionInfo:]_block_invoke.14
+ __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke.59
+ __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke.70
+ __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke_2.72
+ __59-[SGSqlEntityStore(IdentityStore) _popMergeBlobForAnalysis]_block_invoke.366
+ __59-[SGSqlEntityStore(StatsCounters) loadStatsCounterWithKey:]_block_invoke.42
+ __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke.195
+ __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke.203
+ __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke_2.212
+ __60-[SGMIFeatureStore updateFollowUpDetectionStatsWithWarning:]_block_invoke.624
+ __60-[SGSqlEntityStore(Events) checkExistsEventForDuplicateKey:]_block_invoke.84
+ __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.157
+ __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.178
+ __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.179
+ __60-[SGSuggestHistory hasConfirmedField:value:forStorageEvent:]_block_invoke.222
+ __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_3.65
+ __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_4.68
+ __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_5.71
+ __61-[SGDSuggestManager reportMessagesFound:lost:withCompletion:]_block_invoke.687
+ __61-[SGSqlEntityStore(Locations) storageLocationWithPrimaryKey:]_block_invoke.11
+ __62-[SGDSuggestManager titleSuggestionForMessage:withCompletion:]_block_invoke.938
+ __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.288
+ __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.290
+ __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.297
+ __62-[SGSqlEntityStore _filterOutAllButAcceptedWithUpdatedFields:]_block_invoke.506
+ __62-[SGSqlEntityStore _filterOutAllButAcceptedWithUpdatedFields:]_block_invoke_2.513
+ __62-[SGSqlEntityStore(Saliency) topSalienciesForMailboxId:limit:]_block_invoke.51
+ __62-[SGStorageContact convertToContact:sourceEntity:enrichments:]_block_invoke.92
+ __62-[SGStorageContact convertToContact:sourceEntity:enrichments:]_block_invoke_2.97
+ __63-[SGAppLaunchHistory launchCountsForBundleIds:afterDate:limit:]_block_invoke.22
+ __63-[SGAppLaunchHistory launchCountsForBundleIds:afterDate:limit:]_block_invoke.27
+ __63-[SGDSuggestManager extractAttributesAndDonate:withCompletion:]_block_invoke.1032
+ __63-[SGEKCalendarAdapter _eventsAssociatedWithStorageEvent:store:]_block_invoke.56
+ __63-[SGMIFeatureStore incrementUserEngagement:forFollowUpWarning:]_block_invoke.592
+ __63-[SGSqlEntityStore _matchableUTF8TokenRangesInMatchExpression:]_block_invoke.385
+ __63-[SGSqlEntityStore _matchableUTF8TokenRangesInMatchExpression:]_block_invoke.406
+ __63-[SGSqlEntityStore(CNtoSGContacts) _fullSyncContactsWithStore:]_block_invoke.141
+ __63-[SGSqlEntityStore(DatabaseCheck) databasecheck_IntegrityCheck]_block_invoke.40
+ __63-[SGSqlEntityStore(DatabaseCheck) databasecheck_IntegrityCheck]_block_invoke.50
+ __63-[SGSqlEntityStore(SerializedContacts) _trimSerializedContacts]_block_invoke.89
+ __64-[SGDManagerForCTS _performMobileAssetMetadataDownloadActivity:]_block_invoke.36
+ __64-[SGDManagerForCTS _performMobileAssetMetadataDownloadActivity:]_block_invoke.37
+ __64-[SGSqlEntityStore storageContactByMasterEntityId:withSnippets:]_block_invoke.193
+ __64-[SGSqlEntityStore storageContactByMasterEntityId:withSnippets:]_block_invoke.206
+ __64-[SGSqlEntityStore(CNtoSGContacts) _enqueueBatchOfCNContactIds:]_block_invoke.101
+ __64-[SGSqlEntityStore(Reminders) reminderSourceKeyForDuplicateKey:]_block_invoke.40
+ __65+[SGSelfIdentification processConversation:threadLength:options:]_block_invoke.27
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.1005
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.1013
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.1018
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.1006
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.1014
+ __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.1019
+ __65-[SGSqlEntityStore masterEntityIDsForMasterEntityQuery:bindings:]_block_invoke.211
+ __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke.381
+ __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke_2.391
+ __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke_3.398
+ __65-[SGSqlEntityStore(SerializedContacts) loadAllSerializedContacts]_block_invoke.76
+ __65-[SGSqlEntityStore(SqlHelpers) entityFromSqlResult:withSnippets:]_block_invoke.33
+ __65-[SGSqlEntityStore(SqlHelpers) entityFromSqlResult:withSnippets:]_block_invoke.37
+ __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.66
+ __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.72
+ __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.81
+ __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke_2.74
+ __65-[SGSqlEntityStoreCNContactMatcherHelper prefilterNameMatchTerms]_block_invoke.10
+ __66-[SGDCloudKitSync addFetchNewEntitiesAttemptOperationWithRetries:]_block_invoke.215
+ __66-[SGDCloudKitSync addFetchNewEntitiesAttemptOperationWithRetries:]_block_invoke.217
+ __66-[SGDCloudKitSync pauseIfNeededAndReturnRetryEligibilityForError:]_block_invoke.141
+ __66-[SGSqlEntityStore(DatabaseMigrator) migration_deleteInteractions]_block_invoke.452
+ __66-[SGSqlEntityStore(Deleting) deleteMailIntelligenceForMessageIds:]_block_invoke.61
+ __66-[SGSqlEntityStore(Deleting) deleteMailIntelligenceForMessageIds:]_block_invoke.69
+ __66-[SGSqlEntityStore(Spotlight) batchOf:contactsStartingAtEntityId:]_block_invoke.257
+ __67+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersForContact:]_block_invoke.309
+ __67+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersForContact:]_block_invoke.313
+ __67+[SGTokenizerMappingTransformer _purgeableNLTaggerWithNameTagging:]_block_invoke.184
+ __67-[SGSqlEntityStore(DatabaseMigrator) migration_deleteNilDateEvents]_block_invoke.479
+ __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke.39
+ __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke_2.40
+ __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke_3.41
+ __67-[SGSqlEntityStore(SerializedContacts) loadSerializedContactForId:]_block_invoke.57
+ __67-[SGSqlEntityStore(SerializedContacts) loadSerializedContactForId:]_block_invoke_2.62
+ __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.18
+ __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.21
+ __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.28
+ __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.29
+ __68-[SGDManagerForCTS _processMessage:pipeline:context:harvestMetrics:]_block_invoke.158
+ __68-[SGDManagerForCTS _processMessage:pipeline:context:harvestMetrics:]_block_invoke.163
+ __68-[SGSqlEntityStore suggestContactMatchesWithFullTextSearch:limitTo:]_block_invoke.370
+ __68-[SGSqlEntityStore suggestContactMatchesWithFullTextSearch:limitTo:]_block_invoke_2.371
+ __69-[SGMIFeatureStore _applyCappingPolicy:shouldContinue:usingDatabase:]_block_invoke.769
+ __69-[SGMIFeatureStore _applyCappingPolicy:shouldContinue:usingDatabase:]_block_invoke.771
+ __69-[SGSqlEntityStore suggestContactMatchesWithMessagingPrefix:limitTo:]_block_invoke.341
+ __69-[SGSqlEntityStore suggestContactMatchesWithMessagingPrefix:limitTo:]_block_invoke.346
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.184
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.188
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.195
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.202
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.206
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke_2.198
+ __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke_2.209
+ __69-[SGSqlEntityStore(Deleting) _deleteChildEntitiesByRecordIdsInTable:]_block_invoke.139
+ __69-[SGSqlEntityStore(ExtractionInfos) loadExtractionInfoForPrimaryKey:]_block_invoke.20
+ __70-[SGSqlEntityStore(IdentityStore) _writeMergeBlobSnapshotForAnalysis:]_block_invoke.358
+ __71-[SGDSuggestManager cachedResultForKey:generateResult:validateResults:]_block_invoke.562
+ __71-[SGDSuggestManager geocodeEnrichmentsInPipelineEntity:withCompletion:]_block_invoke.829
+ __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.105
+ __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.117
+ __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.120
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.369
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.376
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.383
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.372
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.379
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.386
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke.397
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke.401
+ __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke_2.398
+ __71-[SGSqlEntityStore(IdentityStore) processPseudoContactEntity:recordId:]_block_invoke.77
+ __71-[SGSqlEntityStore(IdentityStore) processPseudoContactEntity:recordId:]_block_invoke.82
+ __71-[SGSqlEntityStore(Writing) _writeLabeledBlobs:deletedMasterEntityIds:]_block_invoke.431
+ __72-[SGSqlEntityStore(CNtoSGContacts) initRefreshSuggestionsContactDropBox]_block_invoke.170
+ __72-[SGSqlEntityStore(DatabaseMigrator) migration_AddNewishTablesIfMissing]_block_invoke.243
+ __72-[SGSqlEntityStore(DatabaseMigrator) migration_AddNewishTablesIfMissing]_block_invoke.256
+ __72-[SGSqlEntityStore(StatsCounters) addValue:toMessageTracerKey:inDomain:]_block_invoke.53
+ __73-[SGDSuggestManager _processReservationInteractions:bundleId:completion:]_block_invoke.799
+ __73-[SGDSuggestManager suggestionsFromURL:title:HTMLPayload:withCompletion:]_block_invoke.823
+ __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.690
+ __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.714
+ __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.718
+ __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke_2.720
+ __73-[SGSqlEntityStore(DatabaseCheck) databasecheck_BrokenEntityIDReferences]_block_invoke.71
+ __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.321
+ __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.325
+ __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.329
+ __73-[SGSqlEntityStore(MessageManagement) pruneLostMessagesWithSource:count:]_block_invoke.69
+ __73-[SGSqlEntityStore(MessageManagement) pruneLostMessagesWithSource:count:]_block_invoke_2.73
+ __73-[SGSqlEntityStore(SerializedContacts) deleteSerializedContactsForIdSet:]_block_invoke.41
+ __73-[SGSqlEntityStore(SerializedContacts) deleteSerializedContactsForIdSet:]_block_invoke.46
+ __74-[SGDSuggestManager launchAppForSuggestedEventUsingLaunchInfo:completion:]_block_invoke.721
+ __74-[SGSqlEntityStore(IdentityStore) makeInterdictsForBlob:withContactStore:]_block_invoke.342
+ __74-[SGSqlEntityStore(IdentityStore) makeInterdictsForBlob:withContactStore:]_block_invoke.347
+ __74-[SGSqlEntityStore(SpotlightMapping) messageIdsForBundleIdentifier:limit:]_block_invoke.21
+ __75-[SGSqlEntityStore(ContactDetails) contactDetailPrimaryKeyForDuplicateKey:]_block_invoke.23
+ __75-[SGSqlEntityStore(DatabaseMigrator) updateLanguageForFTSTablesToLanguage:]_block_invoke.123
+ __75-[SGSqlEntityStore(ReimportRequests) _loadReimportRequestsWithWhereClause:]_block_invoke.106
+ __75-[SGSqlEntityStore(SqlHelpers) selectAuthoritativeDetailsForContactWithId:]_block_invoke.327
+ __76-[SGSqlEntityStore(Loading) entityKeyCountsForEntityType:startDate:endDate:]_block_invoke.212
+ __76-[SGSqlEntityStore(SpotlightMapping_Internal) uniqueIdentifierForMessageId:]_block_invoke.12
+ __77+[SGLowMemoryContactEnumeration enumerateContactIdentifierBatchesUsingBlock:]_block_invoke.17
+ __77+[SGLowMemoryContactEnumeration enumerateContactIdentifierBatchesUsingBlock:]_block_invoke_2.18
+ __77+[SGMIFollowUpAnalyzer analyzeForFollowUpMailWithBody:isSent:messageId:date:]_block_invoke.95
+ __77+[SGMIFollowUpAnalyzer analyzeForFollowUpMailWithBody:isSent:messageId:date:]_block_invoke_2.99
+ __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke.90
+ __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke.94
+ __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke_2.108
+ __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke_3.110
+ __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke.501
+ __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke.509
+ __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke_2.504
+ __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke.173
+ __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke.180
+ __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke_2.177
+ __77-[SGSqlEntityStore(URLs) urlsFoundBetweenStartDate:endDate:bundleIdentifier:]_block_invoke.91
+ __78-[SGSqlEntityStore(ContactDetails) loadAllContactDetailsFromTableForRecordId:]_block_invoke.32
+ __79-[SGSqlEntityStore _contactIdsForContactNameMatches:strongNameIds:weakNameIds:]_block_invoke.268
+ __80-[SGDetectedAttributeML birthdayCongratsTextMessage:andLanguage:andHealthStore:]_block_invoke.164
+ __80-[SGPipeline verificationOperation:overrideVerificationStatus:withDependencies:]_block_invoke.144
+ __81-[SGDSuggestManager dissectAttachmentsFromSearchableItem:options:withCompletion:]_block_invoke.958
+ __81-[SGSqlEntityStore(Deleting) pruneEntitiesOlderThan:suspensionHandler:batchSize:]_block_invoke.40
+ __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.425
+ __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.430
+ __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.437
+ __82-[SGSqlEntityStore(IdentityStore) _uniqueGoodDetailMatchFrom:toDetails:nonUnique:]_block_invoke.329
+ __82-[SGSqlEntityStore(Loading) loadEntitiesByEntityKey:entityType:resolveDuplicates:]_block_invoke.131
+ __83-[SGDSpotlightCommander _reimportQueryForPersonHandle:startDate:endDate:requestId:]_block_invoke.56
+ __83-[SGDSpotlightReceiver deleteInteractionsWithIdentifiers:bundleID:protectionClass:]_block_invoke.99
+ __83-[SGDSuggestManager logEventInteractionForEventWithUniqueKey:interface:actionType:]_block_invoke.889
+ __84-[SGDSuggestManager _harvestReservationsFromInteractions:bundleId:queue:completion:]_block_invoke.790
+ __84-[SGDSuggestManager _harvestReservationsFromInteractions:bundleId:queue:completion:]_block_invoke.791
+ __84-[SGDSuggestManager realtimeContactsFromEntity:enrichments:sourceTextMessage:store:]_block_invoke.631
+ __84-[SGSqlEntityStore(DatabaseMigrator) _slowCopyFromTable:toTable:startingAtEntityId:]_block_invoke.97
+ __84-[SGSqlEntityStore(DatabaseMigrator) _slowCopyFromTable:toTable:startingAtEntityId:]_block_invoke.98
+ __84-[SGSqlEntityStore(SpotlightMapping) messageIdForBundleIdentifier:uniqueIdentifier:]_block_invoke.13
+ __84-[SGSqlEntityStore(Writing) _deleteOldInteractionContactDetails:currentIdentifiers:]_block_invoke.96
+ __85-[SGSqlEntityStore(CNtoSGContacts) loadCNContactMatchesForContact:andGetMaxEntityId:]_block_invoke.41
+ __85-[SGSqlEntityStore(CNtoSGContacts) loadCNContactMatchesForContact:andGetMaxEntityId:]_block_invoke.44
+ __86-[SGMIFeatureStore _purgeTokensWhichLastUpdateWasBefore:shouldContinue:usingDatabase:]_block_invoke.736
+ __86-[SGSqlEntityStore(Spotlight) _duplicateKeysWithZeroSpotlightReferencesFromRecordIds:]_block_invoke.118
+ __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.194
+ __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.219
+ __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.238
+ __87-[SGDSuggestManager suggestionsFromEmailContent:headers:source:options:withCompletion:]_block_invoke.950
+ __87-[SGDetectedAttributeML handleTextMessageContactSharingWithNegativeSample:andLanguage:]_block_invoke.167
+ __87-[SGDetectedAttributeML selfIdDetectionWithTextMessage:inConversation:withSupervision:]_block_invoke.153
+ __87-[SGDetectedAttributeML selfIdDetectionWithTextMessage:inConversation:withSupervision:]_block_invoke.156
+ __87-[SGSqlEntityStore(Loading) loadAllContactDetailsWithWhereClause:onPrep:dedupeAgainst:]_block_invoke.199
+ __87-[SGSqlEntityStore(Writing) writeEmailVerificationResultForEmailWithKey:eventEntities:]_block_invoke.201
+ __87-[SGSqlEntityStore(Writing) writeEmailVerificationResultForEmailWithKey:eventEntities:]_block_invoke.206
+ __88-[SGDCloudKitSync addWriteOperationForRecordGetter:deleteGetter:withRetries:isFirstTry:]_block_invoke.227
+ __88-[SGMIDomainCountingTable enumerateChildrenOfDomain:greaterThan:depth:limit:usingBlock:]_block_invoke.310
+ __89-[SGSqlEntityStore(Deleting) pruneMailIntelligenceOlderThanOneYearWithSuspensionHandler:]_block_invoke.50
+ __90-[SGSqlEntityStore(ReimportRequests) markReimportItemsAsSeenByReceiverWithBundleId:items:]_block_invoke.68
+ __91+[SGSqlEntityStore _initializeDatabaseNolock:withProtection:sharedLock:newDatabaseCreated:]_block_invoke.54
+ __91-[SGEnrichmentWritebackAdapter _deleteEventsMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.49
+ __92+[SGContactsInterface enumerateContactsWithFetchRequest:usingContactStore:error:usingBlock:]_block_invoke.34
+ __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.318
+ __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.326
+ __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.329
+ __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke_2.319
+ __92-[SGSqlEntityStore(ReimportRequests) markReimportItemAsSeenByReceiverWithBundleId:uniqueId:]_block_invoke.79
+ __94+[SGMISpotlightUtility findDeletedEmailAddresses:mdSearchableItemAttribute:fromDaysAgo:error:]_block_invoke.51
+ __94-[SGSqlEntityStore(ReimportRequests) updateReimportItemUniqueIdForBundleId:oldValue:newValue:]_block_invoke.87
+ __95+[SGMISpotlightUtility queryFromDaysAgo:throughDaysAgo:limit:withError:simulatedCSSIs:handler:]_block_invoke.24
+ __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke.291
+ __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke_2.294
+ __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke_3.298
+ __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke.123
+ __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke.132
+ __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke_2.129
+ __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke_2.133
+ __95-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:domainIdentifiers:]_block_invoke.162
+ __95-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:domainIdentifiers:]_block_invoke_2.164
+ __95-[SGSqlEntityStore(StatsCounters) persistStatisticsDictionary:andAdditiveStatisticsDictionary:]_block_invoke.69
+ __95-[SGSqlEntityStore(StatsCounters) persistStatisticsDictionary:andAdditiveStatisticsDictionary:]_block_invoke_2.70
+ __96-[SGEnrichmentWritebackAdapter _uniqueIdentifiersMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.39
+ __96-[SGEnrichmentWritebackAdapter _uniqueIdentifiersMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.43
+ __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.233
+ __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.252
+ __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.256
+ __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke_2.260
+ __97-[SGDSuggestManager harvestedSuggestionsFromMessages:bundleIdentifier:options:completionHandler:]_block_invoke.969
+ __97-[SGDSuggestManager harvestedSuggestionsFromMessages:bundleIdentifier:options:completionHandler:]_block_invoke_2.970
+ __98-[SGSqlEntityStore suggestEventsStartingAt:endingAt:limitTo:additionalWhereClause:options:onPrep:]_block_invoke.539
+ __98-[SGSqlEntityStore(Loading) loadContactDetailsWithWhereClause:onPrep:type:dedupeAgainst:recordId:]_block_invoke.181
+ __99+[SGReminderMessage detectedTitleInModelOutput:enrichedTaggedCharacterRanges:textContent:language:]_block_invoke.136
+ __99-[SGDetectedAttributeDissector handleTextMessageSelfIdentification:entity:withConversationHistory:]_block_invoke.158
+ __99-[SGMIFeatureStore _naiveBayesModelQueryResultForFeature:unigramTokens:bigramTokens:usingDatabase:]_block_invoke.543
+ __99-[SGMIFeatureStore _naiveBayesModelQueryResultForFeature:unigramTokens:bigramTokens:usingDatabase:]_block_invoke_2.544
+ __99-[SGSqlEntityStore(IdentityStore) _joinIncompleteIdentityPhonesWithOthersOfTheirIlk:name:recordId:]_block_invoke.188
+ __Block_byref_object_copy_.10036
+ __Block_byref_object_copy_.10254
+ __Block_byref_object_copy_.11354
+ __Block_byref_object_copy_.11447
+ __Block_byref_object_copy_.1162
+ __Block_byref_object_copy_.12318
+ __Block_byref_object_copy_.13033
+ __Block_byref_object_copy_.13502
+ __Block_byref_object_copy_.14588
+ __Block_byref_object_copy_.1484
+ __Block_byref_object_copy_.1511
+ __Block_byref_object_copy_.15176
+ __Block_byref_object_copy_.15531
+ __Block_byref_object_copy_.15785
+ __Block_byref_object_copy_.16384
+ __Block_byref_object_copy_.16504
+ __Block_byref_object_copy_.17104
+ __Block_byref_object_copy_.17502
+ __Block_byref_object_copy_.18311
+ __Block_byref_object_copy_.1875
+ __Block_byref_object_copy_.18962
+ __Block_byref_object_copy_.21409
+ __Block_byref_object_copy_.2142
+ __Block_byref_object_copy_.21737
+ __Block_byref_object_copy_.21909
+ __Block_byref_object_copy_.22260
+ __Block_byref_object_copy_.22971
+ __Block_byref_object_copy_.23560
+ __Block_byref_object_copy_.23932
+ __Block_byref_object_copy_.24017
+ __Block_byref_object_copy_.24450
+ __Block_byref_object_copy_.24728
+ __Block_byref_object_copy_.26390
+ __Block_byref_object_copy_.2658
+ __Block_byref_object_copy_.26706
+ __Block_byref_object_copy_.268
+ __Block_byref_object_copy_.26853
+ __Block_byref_object_copy_.27614
+ __Block_byref_object_copy_.29088
+ __Block_byref_object_copy_.29248
+ __Block_byref_object_copy_.29650
+ __Block_byref_object_copy_.30419
+ __Block_byref_object_copy_.31804
+ __Block_byref_object_copy_.32872
+ __Block_byref_object_copy_.32987
+ __Block_byref_object_copy_.33898
+ __Block_byref_object_copy_.33964
+ __Block_byref_object_copy_.34257
+ __Block_byref_object_copy_.34545
+ __Block_byref_object_copy_.3456
+ __Block_byref_object_copy_.35245
+ __Block_byref_object_copy_.35551
+ __Block_byref_object_copy_.35649
+ __Block_byref_object_copy_.36446
+ __Block_byref_object_copy_.36822
+ __Block_byref_object_copy_.37033
+ __Block_byref_object_copy_.37955
+ __Block_byref_object_copy_.38230
+ __Block_byref_object_copy_.38483
+ __Block_byref_object_copy_.38640
+ __Block_byref_object_copy_.4056
+ __Block_byref_object_copy_.40576
+ __Block_byref_object_copy_.40921
+ __Block_byref_object_copy_.41484
+ __Block_byref_object_copy_.42641
+ __Block_byref_object_copy_.5435
+ __Block_byref_object_copy_.6772
+ __Block_byref_object_copy_.7656
+ __Block_byref_object_copy_.8438
+ __Block_byref_object_copy_.9445
+ __Block_byref_object_copy_.9746
+ __Block_byref_object_copy_.9880
+ __Block_byref_object_dispose_.10037
+ __Block_byref_object_dispose_.10255
+ __Block_byref_object_dispose_.11355
+ __Block_byref_object_dispose_.11448
+ __Block_byref_object_dispose_.1163
+ __Block_byref_object_dispose_.12319
+ __Block_byref_object_dispose_.13034
+ __Block_byref_object_dispose_.13503
+ __Block_byref_object_dispose_.14589
+ __Block_byref_object_dispose_.1485
+ __Block_byref_object_dispose_.1512
+ __Block_byref_object_dispose_.15177
+ __Block_byref_object_dispose_.15532
+ __Block_byref_object_dispose_.15786
+ __Block_byref_object_dispose_.16385
+ __Block_byref_object_dispose_.16505
+ __Block_byref_object_dispose_.17105
+ __Block_byref_object_dispose_.17503
+ __Block_byref_object_dispose_.18312
+ __Block_byref_object_dispose_.1876
+ __Block_byref_object_dispose_.18963
+ __Block_byref_object_dispose_.21410
+ __Block_byref_object_dispose_.2143
+ __Block_byref_object_dispose_.21738
+ __Block_byref_object_dispose_.21910
+ __Block_byref_object_dispose_.22261
+ __Block_byref_object_dispose_.22972
+ __Block_byref_object_dispose_.23561
+ __Block_byref_object_dispose_.23933
+ __Block_byref_object_dispose_.24018
+ __Block_byref_object_dispose_.24451
+ __Block_byref_object_dispose_.24729
+ __Block_byref_object_dispose_.26391
+ __Block_byref_object_dispose_.2659
+ __Block_byref_object_dispose_.26707
+ __Block_byref_object_dispose_.26854
+ __Block_byref_object_dispose_.269
+ __Block_byref_object_dispose_.27615
+ __Block_byref_object_dispose_.29089
+ __Block_byref_object_dispose_.29249
+ __Block_byref_object_dispose_.29651
+ __Block_byref_object_dispose_.30420
+ __Block_byref_object_dispose_.31805
+ __Block_byref_object_dispose_.32873
+ __Block_byref_object_dispose_.32988
+ __Block_byref_object_dispose_.33899
+ __Block_byref_object_dispose_.33965
+ __Block_byref_object_dispose_.34258
+ __Block_byref_object_dispose_.34546
+ __Block_byref_object_dispose_.3457
+ __Block_byref_object_dispose_.35246
+ __Block_byref_object_dispose_.35552
+ __Block_byref_object_dispose_.35650
+ __Block_byref_object_dispose_.36447
+ __Block_byref_object_dispose_.36823
+ __Block_byref_object_dispose_.37034
+ __Block_byref_object_dispose_.37956
+ __Block_byref_object_dispose_.38231
+ __Block_byref_object_dispose_.38484
+ __Block_byref_object_dispose_.38641
+ __Block_byref_object_dispose_.4057
+ __Block_byref_object_dispose_.40577
+ __Block_byref_object_dispose_.40922
+ __Block_byref_object_dispose_.41485
+ __Block_byref_object_dispose_.42642
+ __Block_byref_object_dispose_.5436
+ __Block_byref_object_dispose_.6773
+ __Block_byref_object_dispose_.7657
+ __Block_byref_object_dispose_.8439
+ __Block_byref_object_dispose_.9446
+ __Block_byref_object_dispose_.9747
+ __Block_byref_object_dispose_.9881
+ __OBJC_$_CLASS_METHODS_SGCascadeWritebackAdapter
+ __OBJC_$_CLASS_METHODS_SGEKCalendarAdapter
+ __OBJC_$_CLASS_METHODS_SGEntityTagsHelper
+ __OBJC_$_CLASS_METHODS_SGEventSchemaCreator
+ __OBJC_$_INSTANCE_METHODS_SGCascadeWritebackAdapter
+ __OBJC_$_INSTANCE_METHODS_SGEventDonationEnablementManager
+ __OBJC_$_INSTANCE_VARIABLES_SGEventDonationEnablementManager
+ __OBJC_$_PROP_LIST_SGCascadeWritebackAdapter
+ __OBJC_$_PROP_LIST_SGEventDonationEnablementManager
+ __OBJC_CLASS_PROTOCOLS_$_SGCascadeWritebackAdapter
+ __OBJC_CLASS_RO_$_SGCascadeWritebackAdapter
+ __OBJC_CLASS_RO_$_SGEntityTagsHelper
+ __OBJC_CLASS_RO_$_SGEventDonationEnablementManager
+ __OBJC_CLASS_RO_$_SGEventSchemaCreator
+ __OBJC_METACLASS_RO_$_SGCascadeWritebackAdapter
+ __OBJC_METACLASS_RO_$_SGEntityTagsHelper
+ __OBJC_METACLASS_RO_$_SGEventDonationEnablementManager
+ __OBJC_METACLASS_RO_$_SGEventSchemaCreator
+ __ProactiveSummarizationLibraryCore_block_invoke.32908
+ __SGNotUserInitiated_block_invoke.11
+ __SGNotUserInitiated_block_invoke.12
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN3re211SparseArrayIPNS1_3NFA6ThreadEE10IndexValueENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN3re29RuneRangeENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPK9_vertex_tNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKNS0_IPK9_vertex_tNS_9allocatorIS3_EEEENS4_IS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN3re23DFA5StateENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN3re23RE2ENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN3re26RegexpENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN3re29PrefilterENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiEEPvEENS_22__tree_node_destructorINS6_ISB_EEEEED1B8ne190102Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__tree_node_destructorINS5_IS9_EEEEED1B8ne190102Ev
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_setIPN3re23DFA5StateENS2_9StateHashENS2_10StateEqualENS_9allocatorIS4_EEED1B8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPK9_vertex_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKNS_6vectorIPK9_vertex_tNS1_IS5_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPK9_vertex_tNS_6vectorIS6_NS1_IS6_EEEEEEPvEEEEEclB8ne190102EPSC_
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__15dequeIN3re29WalkStateINS1_4FragEEENS_9allocatorIS4_EEED2B8ne190102Ev
+ __ZNSt3__15dequeIN3re29WalkStateIPNS1_6RegexpEEENS_9allocatorIS5_EEED2B8ne190102Ev
+ __ZNSt3__15dequeIN3re29WalkStateIPNS1_9Prefilter4InfoEEENS_9allocatorIS6_EEED2B8ne190102Ev
+ __ZNSt3__15dequeIN3re29WalkStateIbEENS_9allocatorIS3_EEED2B8ne190102Ev
+ __ZNSt3__15dequeIN3re29WalkStateIiEENS_9allocatorIS3_EEED2B8ne190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___208+[SGDSuggestManager filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealTime:]_block_invoke
+ ___253-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:]_block_invoke
+ ___253-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:]_block_invoke_2
+ ___39-[SGCascadeWritebackAdapter addEvents:]_block_invoke
+ ___51+[SGEntityTagsHelper extractSchemasFromEntityTags:]_block_invoke
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80bs88r96r_e33_"SGRealtimeSuggestionsTuple"8?0l
+ ___block_descriptor_47_e8_32s_e28_"SGEntity"16?0"SGEntity"8l
+ ___block_descriptor_56_e8_32s40s_e35_v24?0"CCSetDonation"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0l
+ __block_literal_global.10.38002
+ __block_literal_global.100
+ __block_literal_global.100.14312
+ __block_literal_global.1001
+ __block_literal_global.102.17594
+ __block_literal_global.102.32811
+ __block_literal_global.10211
+ __block_literal_global.1028
+ __block_literal_global.1031
+ __block_literal_global.10659
+ __block_literal_global.10676
+ __block_literal_global.107.22859
+ __block_literal_global.107.35636
+ __block_literal_global.108.13963
+ __block_literal_global.109
+ __block_literal_global.1090
+ __block_literal_global.10924
+ __block_literal_global.111
+ __block_literal_global.1112
+ __block_literal_global.11167
+ __block_literal_global.113
+ __block_literal_global.113.32785
+ __block_literal_global.11308
+ __block_literal_global.11363
+ __block_literal_global.114.30278
+ __block_literal_global.11487
+ __block_literal_global.117
+ __block_literal_global.118.26367
+ __block_literal_global.11819
+ __block_literal_global.12.24173
+ __block_literal_global.12387
+ __block_literal_global.124.17597
+ __block_literal_global.124.22800
+ __block_literal_global.125.13944
+ __block_literal_global.125.34910
+ __block_literal_global.125.36819
+ __block_literal_global.126
+ __block_literal_global.12727
+ __block_literal_global.12799
+ __block_literal_global.13.34273
+ __block_literal_global.13.37977
+ __block_literal_global.130
+ __block_literal_global.13106
+ __block_literal_global.134
+ __block_literal_global.134.14853
+ __block_literal_global.134.22548
+ __block_literal_global.135.13946
+ __block_literal_global.135.17031
+ __block_literal_global.135.19274
+ __block_literal_global.1352
+ __block_literal_global.13741
+ __block_literal_global.13994
+ __block_literal_global.14.11492
+ __block_literal_global.14.21843
+ __block_literal_global.141.16627
+ __block_literal_global.14170
+ __block_literal_global.143.20995
+ __block_literal_global.143.27182
+ __block_literal_global.14323
+ __block_literal_global.145
+ __block_literal_global.146
+ __block_literal_global.147.17601
+ __block_literal_global.147.20989
+ __block_literal_global.147.31643
+ __block_literal_global.1482
+ __block_literal_global.15038
+ __block_literal_global.15060
+ __block_literal_global.15117
+ __block_literal_global.1522
+ __block_literal_global.15224
+ __block_literal_global.15367
+ __block_literal_global.155
+ __block_literal_global.15676
+ __block_literal_global.157
+ __block_literal_global.157.8559
+ __block_literal_global.158
+ __block_literal_global.158.27162
+ __block_literal_global.16.37970
+ __block_literal_global.16189
+ __block_literal_global.16254
+ __block_literal_global.165
+ __block_literal_global.166
+ __block_literal_global.16685
+ __block_literal_global.168
+ __block_literal_global.17.33167
+ __block_literal_global.17.40623
+ __block_literal_global.17.41172
+ __block_literal_global.17162
+ __block_literal_global.17590
+ __block_literal_global.176.17607
+ __block_literal_global.17834
+ __block_literal_global.18.35554
+ __block_literal_global.180.32435
+ __block_literal_global.181.14924
+ __block_literal_global.182
+ __block_literal_global.185
+ __block_literal_global.186
+ __block_literal_global.18876
+ __block_literal_global.19380
+ __block_literal_global.197
+ __block_literal_global.1977
+ __block_literal_global.19791
+ __block_literal_global.19865
+ __block_literal_global.20
+ __block_literal_global.201
+ __block_literal_global.201.32545
+ __block_literal_global.20357
+ __block_literal_global.205
+ __block_literal_global.208
+ __block_literal_global.208.34813
+ __block_literal_global.210.32436
+ __block_literal_global.21076
+ __block_literal_global.212
+ __block_literal_global.213
+ __block_literal_global.215.37128
+ __block_literal_global.21679
+ __block_literal_global.217
+ __block_literal_global.217.17074
+ __block_literal_global.21813
+ __block_literal_global.21838
+ __block_literal_global.22.40629
+ __block_literal_global.220
+ __block_literal_global.2203
+ __block_literal_global.22583
+ __block_literal_global.227
+ __block_literal_global.228.13650
+ __block_literal_global.22965
+ __block_literal_global.23.31710
+ __block_literal_global.23.32902
+ __block_literal_global.232
+ __block_literal_global.232.17210
+ __block_literal_global.232.19271
+ __block_literal_global.234.17212
+ __block_literal_global.235.19265
+ __block_literal_global.23608
+ __block_literal_global.23855
+ __block_literal_global.239
+ __block_literal_global.23949
+ __block_literal_global.24096
+ __block_literal_global.241.26460
+ __block_literal_global.24170
+ __block_literal_global.242
+ __block_literal_global.243
+ __block_literal_global.24311
+ __block_literal_global.244.16541
+ __block_literal_global.244.17088
+ __block_literal_global.24435
+ __block_literal_global.247
+ __block_literal_global.247.22883
+ __block_literal_global.25
+ __block_literal_global.250.19104
+ __block_literal_global.251
+ __block_literal_global.252.22881
+ __block_literal_global.25229
+ __block_literal_global.254
+ __block_literal_global.254.22926
+ __block_literal_global.255
+ __block_literal_global.2566
+ __block_literal_global.258
+ __block_literal_global.259
+ __block_literal_global.26427
+ __block_literal_global.26710
+ __block_literal_global.268.19633
+ __block_literal_global.27.38274
+ __block_literal_global.27.40617
+ __block_literal_global.271
+ __block_literal_global.272
+ __block_literal_global.27299
+ __block_literal_global.273
+ __block_literal_global.274
+ __block_literal_global.28.31704
+ __block_literal_global.28017
+ __block_literal_global.28240
+ __block_literal_global.283
+ __block_literal_global.28319
+ __block_literal_global.284
+ __block_literal_global.286.13579
+ __block_literal_global.288
+ __block_literal_global.29
+ __block_literal_global.29.38275
+ __block_literal_global.29079
+ __block_literal_global.29224
+ __block_literal_global.293.36679
+ __block_literal_global.296
+ __block_literal_global.29963
+ __block_literal_global.30073
+ __block_literal_global.301
+ __block_literal_global.301.17522
+ __block_literal_global.30388
+ __block_literal_global.304
+ __block_literal_global.306
+ __block_literal_global.306.10826
+ __block_literal_global.306.16492
+ __block_literal_global.30769
+ __block_literal_global.308
+ __block_literal_global.311
+ __block_literal_global.311.13552
+ __block_literal_global.313
+ __block_literal_global.31336
+ __block_literal_global.31719
+ __block_literal_global.31829
+ __block_literal_global.32
+ __block_literal_global.321
+ __block_literal_global.321.27067
+ __block_literal_global.32388
+ __block_literal_global.324
+ __block_literal_global.324.27068
+ __block_literal_global.32900
+ __block_literal_global.33.32904
+ __block_literal_global.33065
+ __block_literal_global.33165
+ __block_literal_global.332
+ __block_literal_global.335
+ __block_literal_global.33531
+ __block_literal_global.33701
+ __block_literal_global.34154
+ __block_literal_global.34271
+ __block_literal_global.347
+ __block_literal_global.3471
+ __block_literal_global.34988
+ __block_literal_global.355
+ __block_literal_global.35550
+ __block_literal_global.356
+ __block_literal_global.35600
+ __block_literal_global.357.36988
+ __block_literal_global.35711
+ __block_literal_global.36.11456
+ __block_literal_global.36.33148
+ __block_literal_global.36.6339
+ __block_literal_global.36265
+ __block_literal_global.363
+ __block_literal_global.36311
+ __block_literal_global.36488
+ __block_literal_global.3659
+ __block_literal_global.36892
+ __block_literal_global.37203
+ __block_literal_global.374
+ __block_literal_global.376
+ __block_literal_global.377
+ __block_literal_global.378
+ __block_literal_global.37998
+ __block_literal_global.38267
+ __block_literal_global.38415
+ __block_literal_global.385
+ __block_literal_global.38513
+ __block_literal_global.3863
+ __block_literal_global.38668
+ __block_literal_global.387
+ __block_literal_global.39.27302
+ __block_literal_global.39.34242
+ __block_literal_global.39.38268
+ __block_literal_global.396
+ __block_literal_global.398
+ __block_literal_global.40611
+ __block_literal_global.41.33150
+ __block_literal_global.41132
+ __block_literal_global.41175
+ __block_literal_global.4126
+ __block_literal_global.41982
+ __block_literal_global.42.41242
+ __block_literal_global.42441
+ __block_literal_global.42601
+ __block_literal_global.42806
+ __block_literal_global.4296
+ __block_literal_global.43.34243
+ __block_literal_global.43269
+ __block_literal_global.434
+ __block_literal_global.444
+ __block_literal_global.449
+ __block_literal_global.45
+ __block_literal_global.45.38269
+ __block_literal_global.45.41243
+ __block_literal_global.451
+ __block_literal_global.453
+ __block_literal_global.456
+ __block_literal_global.464
+ __block_literal_global.467
+ __block_literal_global.469
+ __block_literal_global.4691
+ __block_literal_global.47.36873
+ __block_literal_global.472.32672
+ __block_literal_global.478
+ __block_literal_global.479
+ __block_literal_global.48.38488
+ __block_literal_global.488.34537
+ __block_literal_global.49.34239
+ __block_literal_global.49.38247
+ __block_literal_global.494
+ __block_literal_global.499
+ __block_literal_global.50
+ __block_literal_global.50.10212
+ __block_literal_global.50.24139
+ __block_literal_global.5012
+ __block_literal_global.503
+ __block_literal_global.506
+ __block_literal_global.507
+ __block_literal_global.509
+ __block_literal_global.52.33129
+ __block_literal_global.52.38259
+ __block_literal_global.5324
+ __block_literal_global.5384
+ __block_literal_global.543
+ __block_literal_global.549
+ __block_literal_global.560
+ __block_literal_global.573
+ __block_literal_global.577
+ __block_literal_global.5896
+ __block_literal_global.59
+ __block_literal_global.61.42731
+ __block_literal_global.615
+ __block_literal_global.62
+ __block_literal_global.62.31681
+ __block_literal_global.62.35520
+ __block_literal_global.626
+ __block_literal_global.63
+ __block_literal_global.630
+ __block_literal_global.632
+ __block_literal_global.6368
+ __block_literal_global.64.24318
+ __block_literal_global.64.31678
+ __block_literal_global.641
+ __block_literal_global.6426
+ __block_literal_global.647
+ __block_literal_global.657
+ __block_literal_global.658
+ __block_literal_global.67.38248
+ __block_literal_global.671
+ __block_literal_global.6725
+ __block_literal_global.681
+ __block_literal_global.681.37464
+ __block_literal_global.684
+ __block_literal_global.6873
+ __block_literal_global.691
+ __block_literal_global.6935
+ __block_literal_global.698
+ __block_literal_global.70.38249
+ __block_literal_global.719
+ __block_literal_global.73.38250
+ __block_literal_global.74.21001
+ __block_literal_global.74.29226
+ __block_literal_global.7457
+ __block_literal_global.747
+ __block_literal_global.75
+ __block_literal_global.76.37262
+ __block_literal_global.7635
+ __block_literal_global.765
+ __block_literal_global.773
+ __block_literal_global.78.29228
+ __block_literal_global.788
+ __block_literal_global.790
+ __block_literal_global.792
+ __block_literal_global.794
+ __block_literal_global.795
+ __block_literal_global.796
+ __block_literal_global.7964
+ __block_literal_global.80
+ __block_literal_global.84.22922
+ __block_literal_global.846
+ __block_literal_global.866
+ __block_literal_global.8663
+ __block_literal_global.868
+ __block_literal_global.87
+ __block_literal_global.87.32814
+ __block_literal_global.886
+ __block_literal_global.891
+ __block_literal_global.899
+ __block_literal_global.90.30323
+ __block_literal_global.90.37251
+ __block_literal_global.91.38448
+ __block_literal_global.912
+ __block_literal_global.912.27682
+ __block_literal_global.9124
+ __block_literal_global.924
+ __block_literal_global.927
+ __block_literal_global.932
+ __block_literal_global.935
+ __block_literal_global.9396
+ __block_literal_global.94.34926
+ __block_literal_global.945
+ __block_literal_global.9452
+ __block_literal_global.95
+ __block_literal_global.957
+ __block_literal_global.9577
+ __block_literal_global.965
+ __block_literal_global.97
+ __block_literal_global.97.14846
+ __block_literal_global.97.17593
+ __block_literal_global.97.26381
+ __block_literal_global.97.30852
+ __block_literal_global.9745
+ __block_literal_global.977
+ __block_literal_global.98
+ __finishSuggestionsSetup_block_invoke.46
+ __finishSuggestionsSetup_block_invoke.47
+ __patterns_block_invoke.17041
+ __patterns_block_invoke.22895
+ __patterns_block_invoke.23953
+ __patterns_block_invoke.25233
+ __patterns_block_invoke.9581
+ __writeIdentity_block_invoke.469
+ __writeIdentity_block_invoke_2.473
+ _addEKEventToCalendar:storageEvent:ekStore:commit:._pasOnceToken46
+ _kEntitySetCascadeDonationVersion
+ _objc_msgSend$_appointmentEntityItemFromAttributeSet:error:
+ _objc_msgSend$_cascadeEntityItemsFromEvents:
+ _objc_msgSend$_completeRegexExtractionforMail:entity:forMail:
+ _objc_msgSend$_flightEntityItemFromAttributeSet:error:
+ _objc_msgSend$_hotelEntityItemFromAttributeSet:error:
+ _objc_msgSend$_isMailCategoryUnsupportedForLLMExtraction:
+ _objc_msgSend$_isStructuredEventEligibleForDonation:
+ _objc_msgSend$_loggingIdentifiersFromEvents:
+ _objc_msgSend$_newEventEligibleForDonation:
+ _objc_msgSend$_partyEntityItemFromAttributeSet:error:
+ _objc_msgSend$_rentalCarEntityItemFromAttributeSet:error:
+ _objc_msgSend$_restaurantEntityItemFromAttributeSet:error:
+ _objc_msgSend$_shouldProcessMailMessage:havingSignificantSender:
+ _objc_msgSend$_subjectResemblesForwardedMailSubjectForMail:
+ _objc_msgSend$_ticketedShowEntityItemFromAttributeSet:error:
+ _objc_msgSend$_ticketedTransportationEntityItemFromAttributeSet:error:
+ _objc_msgSend$_transportationSchemaCreatorFromTransportType:
+ _objc_msgSend$addOrUpdateItem:error:
+ _objc_msgSend$cascadeEntityItemForEvent
+ _objc_msgSend$cascadeEntitySetVersion:
+ _objc_msgSend$costCode
+ _objc_msgSend$deleteItemsWithIdentifiers:bundleId:
+ _objc_msgSend$endDateTimeZone
+ _objc_msgSend$eventCustomerNames
+ _objc_msgSend$eventEndLocationAddress
+ _objc_msgSend$eventEndLocationName
+ _objc_msgSend$eventEndLocationTelephone
+ _objc_msgSend$eventExtractedFromLLM
+ _objc_msgSend$eventNumberOfRooms
+ _objc_msgSend$eventProvider
+ _objc_msgSend$eventReservationForName
+ _objc_msgSend$eventReservationID
+ _objc_msgSend$eventRoomNumbers
+ _objc_msgSend$eventSeatNumbers
+ _objc_msgSend$eventSourceMetadata
+ _objc_msgSend$eventStartLocationAddress
+ _objc_msgSend$eventStartLocationName
+ _objc_msgSend$eventStartLocationTelephone
+ _objc_msgSend$eventStatus
+ _objc_msgSend$eventSubType
+ _objc_msgSend$eventTicketType
+ _objc_msgSend$eventTotalCost
+ _objc_msgSend$eventType
+ _objc_msgSend$eventURL
+ _objc_msgSend$extractSchemasFromEntityTags:
+ _objc_msgSend$filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:
+ _objc_msgSend$filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:
+ _objc_msgSend$filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealTime:
+ _objc_msgSend$finish:
+ _objc_msgSend$flightArrivalAirportAddress
+ _objc_msgSend$flightArrivalAirportAddressSynonyms
+ _objc_msgSend$flightArrivalAirportCode
+ _objc_msgSend$flightArrivalAirportCountry
+ _objc_msgSend$flightArrivalAirportLocality
+ _objc_msgSend$flightArrivalAirportName
+ _objc_msgSend$flightArrivalAirportPostalCode
+ _objc_msgSend$flightArrivalAirportRegion
+ _objc_msgSend$flightArrivalAirportStreetAddress
+ _objc_msgSend$flightArrivalDateTime
+ _objc_msgSend$flightArrivalGate
+ _objc_msgSend$flightArrivalTerminal
+ _objc_msgSend$flightArrivalTimeZone
+ _objc_msgSend$flightBoardingDateTime
+ _objc_msgSend$flightCarrier
+ _objc_msgSend$flightCheckInUrl
+ _objc_msgSend$flightConfirmationNumber
+ _objc_msgSend$flightDepartureAirportAddress
+ _objc_msgSend$flightDepartureAirportAddressSynonyms
+ _objc_msgSend$flightDepartureAirportCode
+ _objc_msgSend$flightDepartureAirportCountry
+ _objc_msgSend$flightDepartureAirportLocality
+ _objc_msgSend$flightDepartureAirportName
+ _objc_msgSend$flightDepartureAirportPostalCode
+ _objc_msgSend$flightDepartureAirportRegion
+ _objc_msgSend$flightDepartureAirportStreetAddress
+ _objc_msgSend$flightDepartureDateTime
+ _objc_msgSend$flightDepartureGate
+ _objc_msgSend$flightDepartureTerminal
+ _objc_msgSend$flightDepartureTimeZone
+ _objc_msgSend$hotelCheckinDate
+ _objc_msgSend$hotelCheckinTime
+ _objc_msgSend$hotelCheckoutDate
+ _objc_msgSend$hotelCheckoutTime
+ _objc_msgSend$hotelProvider
+ _objc_msgSend$hotelReservationForAddress
+ _objc_msgSend$hotelReservationForName
+ _objc_msgSend$hotelReservationForStreetAddress
+ _objc_msgSend$hotelReservationForTelephone
+ _objc_msgSend$hotelReservationId
+ _objc_msgSend$hotelTimeZone
+ _objc_msgSend$hotelUnderName
+ _objc_msgSend$incrementalSetDonationWithItemType:descriptors:version:validity:completion:
+ _objc_msgSend$initWithContactStore:
+ _objc_msgSend$initWithContent:metaContent:error:
+ _objc_msgSend$initWithCustomerNames:eventName:startLocationName:startLocationAddress:startDate:startDateTimeZone:seatNumbers:endLocationName:endLocationAddress:endDate:endDateTimeZone:duration:eventSubType:error:
+ _objc_msgSend$initWithEntity:entityType:error:
+ _objc_msgSend$initWithEventName:startLocationName:startAddress:startDate:startDateTimeZone:endDate:endDateTimeZone:link:eventSubType:error:
+ _objc_msgSend$initWithEventName:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:endDate:endDateTimeZone:duration:cost:costCode:eventSubType:error:
+ _objc_msgSend$initWithFlightDesignator:flightConfirmationNumber:flightCarrier:flightCarrierCode:provider:customerNames:flightDepartureDateTime:flightDepartureTimeZone:flightBoardingDateTime:flightDepartureAirportCode:flightDepartureAirportName:flightDepartureAirportAddress:flightDepartureAirportLocality:flightDepartureAirportRegion:flightDepartureAirportPostalCode:flightDepartureAirportCountry:flightDepartureTerminal:flightDepartureGate:seatNumbers:flightArrivalDateTime:flightArrivalTimeZone:flightArrivalAirportCode:flightArrivalAirportName:flightArrivalAirportAddress:flightArrivalAirportLocality:flightArrivalAirportRegion:flightArrivalAirportPostalCode:flightArrivalAirportCountry:flightArrivalTerminal:flightArrivalGate:duration:flightCheckInUrl:cost:costCurrencyCode:flightNumber:eventStatus:error:
+ _objc_msgSend$initWithHotelReservationForName:provider:hotelReservationId:customerNames:roomNumbers:numberOfRooms:hotelReservationForAddress:hotelCheckinDate:hotelCheckinTime:hotelCheckoutDate:hotelCheckoutTime:hotelTimeZone:duration:hotelReservationForTelephone:cost:costCode:eventStatus:error:
+ _objc_msgSend$initWithLLMPreferredLocales:
+ _objc_msgSend$initWithProvider:reservationID:customerNames:restaurantPartySize:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:restaurantMealType:eventStatus:error:
+ _objc_msgSend$initWithReservationID:eventName:provider:customerNames:startLocationName:startLocationAddress:seatNumbers:startDate:startDateTimeZone:endDate:endDateTimeZone:duration:ticketType:link:cost:costCode:eventSubType:error:
+ _objc_msgSend$initWithReservationID:eventName:provider:customerNames:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:endLocationName:endLocationAddress:endLocationTelephone:endDate:endDateTimeZone:reservationForName:duration:cost:costCode:eventStatus:error:
+ _objc_msgSend$initWithSourceItemIdentifier:error:
+ _objc_msgSend$isCascadeEntitySetVersion
+ _objc_msgSend$isLLMPreferredForLocale
+ _objc_msgSend$isLLMPreferredForLocale:
+ _objc_msgSend$isMessageCandidateForExtraction:
+ _objc_msgSend$isTimePresentInDURawDateTime:
+ _objc_msgSend$isUnsupportedEventCategoryStatusForTextMessage:
+ _objc_msgSend$isValidEventForSpotlightDonation:
+ _objc_msgSend$mailCategories
+ _objc_msgSend$metaContent
+ _objc_msgSend$mlExtractionEnabledForTextMessage
+ _objc_msgSend$processItem:receivedDate:positionInReceivedItems:
+ _objc_msgSend$registerItem:error:
+ _objc_msgSend$reservationIDPresentInEventSchema:
+ _objc_msgSend$restaurantMealType
+ _objc_msgSend$restaurantPartySize
+ _objc_msgSend$schemasInEntityTagsBelongsToPendingConfirmationEvent:
+ _objc_msgSend$setEventStatus:
+ _objc_msgSend$setEventUpdateStatus:
+ _objc_msgSend$setFlightArrivalAirportAddressSynonyms:
+ _objc_msgSend$setFlightDepartureAirportAddressSynonyms:
+ _objc_msgSend$setTimeIsUnknown:
+ _objc_msgSend$shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:
+ _objc_msgSend$sourceItemIdentifier
+ _objc_msgSend$startDateTimeZone
+ _objc_msgSend$synonymAirportNamesForAirportCode:
+ _processReservationInteractions:bundleId:completion:._pasOnceToken160
+ _serialQueueForTitleGeneration._pasOnceToken200
+ addInteractions:bundleId:completion:._pasOnceToken150
+ analyzeForFollowUpMailWithBody:isSent:messageId:date:._pasExprOnceResult.94
+ asDictionary.onceToken.30768
+ asDictionary.sharedKeySet.30771
+ audit_stringProactiveSummarization.32911
+ bumptTTLForNLEvent:._pasOnceToken55
+ charactersSAX.36263
+ consumeInteractionWithContext:._pasOnceToken244
+ dateFromEmailString:._pasExprOnceResult.140
+ eventClassificationWithoutXPCForMailMessage:._pasOnceToken103
+ identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:._pasExprOnceResult.15
+ isLowercaseAscii.17069
+ jsonLdOutputFromPackedJSEntity:._pasOnceToken105
+ kSqlEventFired_block_invoke._pasExprOnceResult
+ kSqlEventFired_block_invoke._pasExprOnceResult.15118
+ kSqlEventFired_block_invoke._pasOnceToken3
+ kSqlEventFired_block_invoke._pasOnceToken7
+ kSqlEventFired_block_invoke.onceToken
+ kSqlEventFired_block_invoke.version
+ logEventInteractionForEventWithExternalIdentifier:interface:actionType:._pasOnceToken187
+ logEventInteractionForEventWithUniqueKey:interface:actionType:._pasOnceToken195
+ patterns.17034
+ patterns.22843
+ patterns.23934
+ patterns.25224
+ patterns.9561
+ patterns.onceToken.17038
+ patterns.onceToken.22892
+ patterns.onceToken.23948
+ patterns.onceToken.24973
+ patterns.onceToken.25228
+ patterns.onceToken.9576
+ patterns.patterns.17039
+ patterns.patterns.22893
+ patterns.patterns.23950
+ patterns.patterns.24974
+ patterns.patterns.25230
+ patterns.patterns.9578
+ resolveCandidatesWithoutXPC:forCategory:label:rawIndexSet:taggedCharacterRanges:._pasOnceToken104
+ reverseMapMailMessage:withPreprocessedHTML:forCategory:withSchemExpectation:._pasOnceToken106
+ sg_decodeEncodedWords._pasExprOnceResult.18
+ sharedInstance.28020
+ sharedInstance._pasExprOnceResult.11820
+ sharedInstance._pasExprOnceResult.12800
+ sharedInstance._pasExprOnceResult.13107
+ sharedInstance._pasExprOnceResult.14171
+ sharedInstance._pasExprOnceResult.15225
+ sharedInstance._pasExprOnceResult.16150
+ sharedInstance._pasExprOnceResult.21680
+ sharedInstance._pasExprOnceResult.2204
+ sharedInstance._pasExprOnceResult.24097
+ sharedInstance._pasExprOnceResult.28320
+ sharedInstance._pasExprOnceResult.31830
+ sharedInstance._pasExprOnceResult.33066
+ sharedInstance._pasExprOnceResult.33532
+ sharedInstance._pasExprOnceResult.36395
+ sharedInstance._pasExprOnceResult.36489
+ sharedInstance._pasExprOnceResult.37999
+ sharedInstance._pasExprOnceResult.41133
+ sharedInstance._pasExprOnceResult.4692
+ sharedInstance._pasExprOnceResult.6508
+ sharedInstance._pasExprOnceResult.6874
+ sharedInstance._pasExprOnceResult.94
+ sharedInstance._pasOnceToken2.11818
+ sharedInstance._pasOnceToken2.12798
+ sharedInstance._pasOnceToken2.13105
+ sharedInstance._pasOnceToken2.14169
+ sharedInstance._pasOnceToken2.15223
+ sharedInstance._pasOnceToken2.24095
+ sharedInstance._pasOnceToken2.28318
+ sharedInstance._pasOnceToken2.36394
+ sharedInstance._pasOnceToken2.41131
+ sharedInstance._pasOnceToken2.4690
+ sharedInstance._pasOnceToken2.6507
+ sharedInstance._pasOnceToken2.6872
+ sharedInstance._pasOnceToken3.21678
+ sharedInstance._pasOnceToken3.31828
+ sharedInstance._pasOnceToken3.33064
+ sharedInstance._pasOnceToken3.33530
+ sharedInstance._pasOnceToken3.36487
+ sharedInstance._pasOnceToken9.37997
+ titleSuggestionForMessage:withCompletion:._pasOnceToken202
- -[SGDSpotlightReceiver _accessSummarizationPipelineForBundleId:block:]
- -[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:]
- -[SGExtractionDissector mlExtractionEnabledForTextMessage:]
- GCC_except_table1025
- GCC_except_table1151
- GCC_except_table1168
- GCC_except_table1185
- GCC_except_table1213
- GCC_except_table1268
- GCC_except_table1325
- GCC_except_table1350
- GCC_except_table1368
- GCC_except_table1371
- GCC_except_table1379
- GCC_except_table1406
- GCC_except_table1450
- GCC_except_table1481
- GCC_except_table1585
- GCC_except_table1628
- GCC_except_table1652
- GCC_except_table1666
- GCC_except_table1668
- GCC_except_table1671
- GCC_except_table1673
- GCC_except_table1675
- GCC_except_table1677
- GCC_except_table1679
- GCC_except_table1681
- GCC_except_table1684
- GCC_except_table1686
- GCC_except_table1689
- GCC_except_table1693
- GCC_except_table1695
- GCC_except_table1699
- GCC_except_table1708
- GCC_except_table1714
- GCC_except_table1750
- GCC_except_table1755
- GCC_except_table1765
- GCC_except_table1816
- GCC_except_table1843
- GCC_except_table1844
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1850
- GCC_except_table1852
- GCC_except_table1926
- GCC_except_table1928
- GCC_except_table1937
- GCC_except_table1938
- GCC_except_table1959
- GCC_except_table1960
- GCC_except_table1972
- GCC_except_table1973
- GCC_except_table1984
- GCC_except_table1987
- GCC_except_table1993
- GCC_except_table1995
- GCC_except_table1996
- GCC_except_table1999
- GCC_except_table2015
- GCC_except_table2016
- GCC_except_table2062
- GCC_except_table2069
- GCC_except_table2073
- GCC_except_table2159
- GCC_except_table2160
- GCC_except_table2163
- GCC_except_table2174
- GCC_except_table2176
- GCC_except_table2197
- GCC_except_table2301
- GCC_except_table2306
- GCC_except_table2307
- GCC_except_table2312
- GCC_except_table2320
- GCC_except_table2321
- GCC_except_table2332
- GCC_except_table2333
- GCC_except_table2335
- GCC_except_table2341
- GCC_except_table2342
- GCC_except_table2343
- GCC_except_table2347
- GCC_except_table2352
- GCC_except_table2354
- GCC_except_table2362
- GCC_except_table2374
- GCC_except_table2447
- GCC_except_table2448
- GCC_except_table2449
- GCC_except_table2450
- GCC_except_table2451
- GCC_except_table2457
- GCC_except_table2458
- GCC_except_table2459
- GCC_except_table2461
- GCC_except_table2462
- GCC_except_table2463
- GCC_except_table2464
- GCC_except_table2465
- GCC_except_table2471
- GCC_except_table2523
- GCC_except_table2530
- GCC_except_table2532
- GCC_except_table2534
- GCC_except_table2538
- GCC_except_table2543
- GCC_except_table2545
- GCC_except_table2547
- GCC_except_table2552
- GCC_except_table2554
- GCC_except_table2556
- GCC_except_table2558
- GCC_except_table2560
- GCC_except_table2569
- GCC_except_table2599
- GCC_except_table2647
- GCC_except_table2653
- GCC_except_table2655
- GCC_except_table2671
- GCC_except_table2675
- GCC_except_table2686
- GCC_except_table2718
- GCC_except_table2743
- GCC_except_table2744
- GCC_except_table2749
- GCC_except_table2751
- GCC_except_table2754
- GCC_except_table2811
- GCC_except_table2817
- GCC_except_table2838
- GCC_except_table2848
- GCC_except_table2874
- GCC_except_table2879
- GCC_except_table2888
- GCC_except_table2896
- GCC_except_table2900
- GCC_except_table2917
- GCC_except_table2922
- GCC_except_table2937
- GCC_except_table2947
- GCC_except_table2949
- GCC_except_table2952
- GCC_except_table2973
- GCC_except_table2976
- GCC_except_table2979
- GCC_except_table2984
- GCC_except_table2988
- GCC_except_table3001
- GCC_except_table3038
- GCC_except_table3059
- GCC_except_table3072
- GCC_except_table3076
- GCC_except_table3081
- GCC_except_table3083
- GCC_except_table3106
- GCC_except_table3202
- GCC_except_table3226
- GCC_except_table3235
- GCC_except_table3236
- GCC_except_table3237
- GCC_except_table3291
- GCC_except_table3293
- GCC_except_table3301
- GCC_except_table3306
- GCC_except_table3315
- GCC_except_table3319
- GCC_except_table3385
- GCC_except_table3585
- GCC_except_table3590
- GCC_except_table3598
- GCC_except_table3652
- GCC_except_table3656
- GCC_except_table3658
- GCC_except_table3660
- GCC_except_table3662
- GCC_except_table3670
- GCC_except_table3673
- GCC_except_table3674
- GCC_except_table3707
- GCC_except_table3709
- GCC_except_table3711
- GCC_except_table3736
- GCC_except_table3738
- GCC_except_table3749
- GCC_except_table3766
- GCC_except_table3783
- GCC_except_table3820
- GCC_except_table3826
- GCC_except_table3883
- GCC_except_table3957
- GCC_except_table3979
- GCC_except_table4010
- GCC_except_table4019
- GCC_except_table4023
- GCC_except_table4026
- GCC_except_table4052
- GCC_except_table407
- GCC_except_table4071
- GCC_except_table4075
- GCC_except_table4080
- GCC_except_table4091
- GCC_except_table4094
- GCC_except_table4096
- GCC_except_table4108
- GCC_except_table4110
- GCC_except_table4114
- GCC_except_table4116
- GCC_except_table412
- GCC_except_table4124
- GCC_except_table4129
- GCC_except_table4135
- GCC_except_table4139
- GCC_except_table4143
- GCC_except_table4144
- GCC_except_table4145
- GCC_except_table4146
- GCC_except_table4147
- GCC_except_table4149
- GCC_except_table415
- GCC_except_table4150
- GCC_except_table4151
- GCC_except_table4152
- GCC_except_table4154
- GCC_except_table4155
- GCC_except_table4156
- GCC_except_table4157
- GCC_except_table4158
- GCC_except_table4160
- GCC_except_table4161
- GCC_except_table4196
- GCC_except_table4205
- GCC_except_table4214
- GCC_except_table4218
- GCC_except_table422
- GCC_except_table4221
- GCC_except_table4233
- GCC_except_table425
- GCC_except_table4253
- GCC_except_table428
- GCC_except_table4297
- GCC_except_table431
- GCC_except_table4350
- GCC_except_table4352
- GCC_except_table4354
- GCC_except_table4355
- GCC_except_table4358
- GCC_except_table4359
- GCC_except_table436
- GCC_except_table4363
- GCC_except_table4368
- GCC_except_table4369
- GCC_except_table4373
- GCC_except_table4375
- GCC_except_table4380
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4412
- GCC_except_table4415
- GCC_except_table4438
- GCC_except_table4481
- GCC_except_table4500
- GCC_except_table4503
- GCC_except_table4569
- GCC_except_table4595
- GCC_except_table4601
- GCC_except_table4606
- GCC_except_table4617
- GCC_except_table4683
- GCC_except_table4696
- GCC_except_table4722
- GCC_except_table4742
- GCC_except_table4743
- GCC_except_table4750
- GCC_except_table4753
- GCC_except_table4824
- GCC_except_table4827
- GCC_except_table4849
- GCC_except_table4855
- GCC_except_table4857
- GCC_except_table4863
- GCC_except_table4981
- GCC_except_table5013
- GCC_except_table5044
- GCC_except_table5053
- GCC_except_table5054
- GCC_except_table5063
- GCC_except_table5073
- GCC_except_table5080
- GCC_except_table5082
- GCC_except_table5092
- GCC_except_table5128
- GCC_except_table5134
- GCC_except_table5135
- GCC_except_table5140
- GCC_except_table5145
- GCC_except_table5150
- GCC_except_table525
- GCC_except_table5269
- GCC_except_table5273
- GCC_except_table5274
- GCC_except_table5275
- GCC_except_table5288
- GCC_except_table5313
- GCC_except_table5348
- GCC_except_table5350
- GCC_except_table5360
- GCC_except_table5377
- GCC_except_table539
- GCC_except_table5423
- GCC_except_table543
- GCC_except_table5482
- GCC_except_table5487
- GCC_except_table5490
- GCC_except_table5493
- GCC_except_table5497
- GCC_except_table5506
- GCC_except_table5526
- GCC_except_table5534
- GCC_except_table5537
- GCC_except_table5540
- GCC_except_table5572
- GCC_except_table5604
- GCC_except_table5617
- GCC_except_table5619
- GCC_except_table5626
- GCC_except_table5651
- GCC_except_table5658
- GCC_except_table5666
- GCC_except_table5675
- GCC_except_table5683
- GCC_except_table5696
- GCC_except_table5699
- GCC_except_table5703
- GCC_except_table5728
- GCC_except_table5757
- GCC_except_table5770
- GCC_except_table5855
- GCC_except_table5884
- GCC_except_table5887
- GCC_except_table5889
- GCC_except_table5894
- GCC_except_table5897
- GCC_except_table5903
- GCC_except_table5905
- GCC_except_table5907
- GCC_except_table5970
- GCC_except_table5980
- GCC_except_table5992
- GCC_except_table5994
- GCC_except_table5998
- GCC_except_table6002
- GCC_except_table6004
- GCC_except_table6006
- GCC_except_table6008
- GCC_except_table6010
- GCC_except_table6012
- GCC_except_table6014
- GCC_except_table6020
- GCC_except_table6064
- GCC_except_table6080
- GCC_except_table6083
- GCC_except_table6090
- GCC_except_table6101
- GCC_except_table6114
- GCC_except_table6120
- GCC_except_table6130
- GCC_except_table6133
- GCC_except_table6154
- GCC_except_table6158
- GCC_except_table6170
- GCC_except_table6220
- GCC_except_table6221
- GCC_except_table6224
- GCC_except_table6226
- GCC_except_table6227
- GCC_except_table6369
- GCC_except_table6379
- GCC_except_table6382
- GCC_except_table6386
- GCC_except_table6387
- GCC_except_table6398
- GCC_except_table6408
- GCC_except_table6421
- GCC_except_table6426
- GCC_except_table6434
- GCC_except_table6462
- GCC_except_table6466
- GCC_except_table6525
- GCC_except_table6527
- GCC_except_table6530
- GCC_except_table6535
- GCC_except_table6541
- GCC_except_table6561
- GCC_except_table6567
- GCC_except_table6570
- GCC_except_table6581
- GCC_except_table6585
- GCC_except_table6591
- GCC_except_table6600
- GCC_except_table6615
- GCC_except_table6616
- GCC_except_table6644
- GCC_except_table6652
- GCC_except_table666
- GCC_except_table6686
- GCC_except_table6692
- GCC_except_table6698
- GCC_except_table6704
- GCC_except_table6706
- GCC_except_table6707
- GCC_except_table6708
- GCC_except_table6709
- GCC_except_table6715
- GCC_except_table6717
- GCC_except_table6718
- GCC_except_table6723
- GCC_except_table6739
- GCC_except_table6741
- GCC_except_table676
- GCC_except_table6776
- GCC_except_table6790
- GCC_except_table6792
- GCC_except_table6818
- GCC_except_table6821
- GCC_except_table6823
- GCC_except_table6825
- GCC_except_table6828
- GCC_except_table6830
- GCC_except_table6832
- GCC_except_table6834
- GCC_except_table6844
- GCC_except_table6870
- GCC_except_table6872
- GCC_except_table6874
- GCC_except_table6876
- GCC_except_table6878
- GCC_except_table689
- GCC_except_table6902
- GCC_except_table6904
- GCC_except_table6919
- GCC_except_table6922
- GCC_except_table694
- GCC_except_table696
- GCC_except_table700
- GCC_except_table703
- GCC_except_table7062
- GCC_except_table7063
- GCC_except_table7098
- GCC_except_table7101
- GCC_except_table7173
- GCC_except_table7208
- GCC_except_table7213
- GCC_except_table7216
- GCC_except_table7219
- GCC_except_table7222
- GCC_except_table7252
- GCC_except_table7297
- GCC_except_table7311
- GCC_except_table7317
- GCC_except_table735
- GCC_except_table739
- GCC_except_table741
- GCC_except_table743
- GCC_except_table745
- GCC_except_table749
- GCC_except_table7497
- GCC_except_table7506
- GCC_except_table7525
- GCC_except_table7553
- GCC_except_table7554
- GCC_except_table7555
- GCC_except_table7568
- GCC_except_table7570
- GCC_except_table7572
- GCC_except_table7698
- GCC_except_table7701
- GCC_except_table7718
- GCC_except_table7764
- GCC_except_table7871
- GCC_except_table7910
- GCC_except_table7915
- GCC_except_table7924
- GCC_except_table7958
- GCC_except_table7962
- GCC_except_table7978
- GCC_except_table7979
- GCC_except_table7995
- GCC_except_table8006
- GCC_except_table8008
- GCC_except_table8010
- GCC_except_table8014
- GCC_except_table8021
- GCC_except_table8023
- GCC_except_table8049
- GCC_except_table8068
- GCC_except_table8075
- GCC_except_table8079
- GCC_except_table8086
- GCC_except_table8093
- GCC_except_table8102
- GCC_except_table8106
- GCC_except_table8109
- GCC_except_table8112
- GCC_except_table8121
- GCC_except_table8130
- GCC_except_table8134
- GCC_except_table8136
- GCC_except_table8148
- GCC_except_table8150
- GCC_except_table8158
- GCC_except_table8162
- GCC_except_table8164
- GCC_except_table8167
- GCC_except_table8179
- GCC_except_table8185
- GCC_except_table8199
- GCC_except_table8236
- GCC_except_table8237
- GCC_except_table8242
- GCC_except_table8246
- GCC_except_table8251
- GCC_except_table8256
- GCC_except_table8265
- GCC_except_table8281
- GCC_except_table8292
- GCC_except_table8293
- GCC_except_table8294
- GCC_except_table8300
- GCC_except_table8301
- GCC_except_table8303
- GCC_except_table8304
- GCC_except_table8309
- GCC_except_table8311
- GCC_except_table8313
- GCC_except_table8314
- GCC_except_table8315
- GCC_except_table8316
- GCC_except_table8317
- GCC_except_table8320
- GCC_except_table8322
- GCC_except_table8323
- GCC_except_table8324
- GCC_except_table8327
- GCC_except_table8330
- GCC_except_table8335
- GCC_except_table8337
- GCC_except_table8339
- GCC_except_table8342
- GCC_except_table8345
- GCC_except_table8346
- GCC_except_table8347
- GCC_except_table8348
- GCC_except_table843
- GCC_except_table8457
- GCC_except_table8461
- GCC_except_table8478
- GCC_except_table8485
- GCC_except_table8486
- GCC_except_table8490
- GCC_except_table8524
- GCC_except_table854
- GCC_except_table8544
- GCC_except_table857
- GCC_except_table8574
- GCC_except_table8580
- GCC_except_table8588
- GCC_except_table8589
- GCC_except_table8592
- GCC_except_table8607
- GCC_except_table8611
- GCC_except_table862
- GCC_except_table8626
- GCC_except_table8636
- GCC_except_table8656
- GCC_except_table8661
- GCC_except_table867
- GCC_except_table8680
- GCC_except_table8684
- GCC_except_table8703
- GCC_except_table8708
- GCC_except_table8720
- GCC_except_table8758
- GCC_except_table876
- GCC_except_table8809
- GCC_except_table8811
- GCC_except_table8833
- GCC_except_table8834
- GCC_except_table8838
- GCC_except_table8839
- GCC_except_table8867
- GCC_except_table8881
- GCC_except_table8891
- GCC_except_table8912
- GCC_except_table8930
- GCC_except_table8935
- GCC_except_table8936
- GCC_except_table8940
- GCC_except_table8941
- GCC_except_table8944
- GCC_except_table9012
- GCC_except_table9024
- GCC_except_table9047
- GCC_except_table9048
- GCC_except_table9052
- GCC_except_table9054
- GCC_except_table9115
- GCC_except_table9133
- GCC_except_table9137
- GCC_except_table9140
- GCC_except_table9154
- GCC_except_table9162
- GCC_except_table9166
- GCC_except_table9169
- GCC_except_table9170
- GCC_except_table9171
- GCC_except_table9173
- GCC_except_table9175
- GCC_except_table9182
- GCC_except_table9183
- GCC_except_table9184
- GCC_except_table9257
- GCC_except_table9259
- GCC_except_table9260
- GCC_except_table9263
- GCC_except_table9264
- GCC_except_table9271
- GCC_except_table9272
- GCC_except_table9273
- GCC_except_table9274
- GCC_except_table9288
- GCC_except_table9290
- GCC_except_table9292
- GCC_except_table9293
- GCC_except_table9295
- GCC_except_table9300
- GCC_except_table9301
- GCC_except_table9303
- GCC_except_table9305
- GCC_except_table9306
- GCC_except_table9311
- GCC_except_table9312
- GCC_except_table9313
- GCC_except_table9324
- GCC_except_table9329
- GCC_except_table9350
- GCC_except_table9355
- GCC_except_table9369
- GCC_except_table9441
- GCC_except_table9445
- GCC_except_table9447
- GCC_except_table9449
- GCC_except_table9451
- GCC_except_table9453
- GCC_except_table9455
- GCC_except_table9457
- GCC_except_table9459
- GCC_except_table9461
- GCC_except_table9463
- GCC_except_table9465
- GCC_except_table9467
- GCC_except_table9469
- GCC_except_table9471
- GCC_except_table9473
- GCC_except_table9475
- GCC_except_table9477
- GCC_except_table9479
- GCC_except_table9481
- GCC_except_table9483
- GCC_except_table9485
- GCC_except_table9487
- GCC_except_table9489
- GCC_except_table9491
- GCC_except_table9493
- GCC_except_table9495
- GCC_except_table9497
- GCC_except_table9499
- GCC_except_table9503
- GCC_except_table9562
- GCC_except_table9568
- GCC_except_table9591
- GCC_except_table9610
- GCC_except_table9785
- GCC_except_table9794
- GCC_except_table9799
- GCC_except_table9968
- GCC_except_table9970
- ProactiveSummarizationLibraryCore.frameworkLibrary.32695
- SGNotUserInitiated._pasExprOnceResult.1
- _PASValidatedFormat.37934
- __102-[SGMIFeatureStore _highlyDiscriminantTokensForFeature:minCount:minRatio:domains:limit:usingDatabase:]_block_invoke.547
- __102-[SGMessageEventDissector logMLMessageEventExtractionForSchema:message:category:timingProcessingInMs:]_block_invoke.356
- __103-[SGDetectedAttributeDissector handleTextMessageBirthdayCongratulation:entity:withConversationHistory:]_block_invoke.132
- __104-[SGDSuggestManager waitForEventWithIdentifier:toAppearInEventStoreWithLastModificationDate:completion:]_block_invoke.829
- __104-[SGSqlEntityStore initWithEntityDbPath:snippetDbPath:isEphemeral:sharedLock:executeJournals:noMigrate:]_block_invoke.97
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.263
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.270
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.277
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.284
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.291
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.298
- __105-[SGSqlEntityStore(DatabaseMigrator) migration_FixUpColumnsForDevicesWhoMissedTheImprovedLegacyMigration]_block_invoke.305
- __105-[SGSqlEntityStore(Spotlight) domainIdentifierForSpotlightReferenceForBundleIdentifier:uniqueIdentifier:]_block_invoke.5
- __105-[SGSqlEntityStore(Spotlight) domainIdentifierForSpotlightReferenceForBundleIdentifier:uniqueIdentifier:]_block_invoke.7
- __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke.284
- __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke.286
- __106-[SGDSuggestManager setupManagerWithConnection:store:ctsManager:ekStoreProvider:contactStore:pet2Tracker:]_block_invoke_2.289
- __107-[SGDSuggestManager namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.629
- __111-[SGSqlEntityStore(IdentityStore) registerAndLinkIdentity:recordId:phones:socialProfiles:email:curated:isSent:]_block_invoke.135
- __111-[SGSqlEntityStore(IdentityStore) registerAndLinkIdentity:recordId:phones:socialProfiles:email:curated:isSent:]_block_invoke.143
- __111-[SGSqlEntityStore(Spotlight) _recordIdsFromRemovingSpotlightReferencesWithBundleIdentifier:uniqueIdentifiers:]_block_invoke.131
- __112+[SGDetection detectionWithType:text:matchRange:matchString:label:hasPhoneLabel:extractionInfo:isUnlikelyPhone:]_block_invoke.1
- __112-[SGSqlEntityStore(SpotlightMapping) commitSpotlightMapping:bundleIdentifier:domainIdentifier:uniqueIdentifier:]_block_invoke.45
- __115-[SGDetectedAttributeML detectionFromMessage:ddMatch:matchedContext:withSupervision:inConversation:entityLanguage:]_block_invoke.130
- __115-[SGDetectedAttributeML detectionFromMessage:ddMatch:matchedContext:withSupervision:inConversation:entityLanguage:]_block_invoke.134
- __116-[SGSqlEntityStore(Deleting) deleteEntitiesByDuplicateKey:preserveEventConfirmationHistory:emitChangeNotifications:]_block_invoke.284
- __121-[SGSqlEntityStore(Saliency) sortedSaliencyResultsRestrictedToMailboxTypes:mailboxIds:receivedOnOrAfter:ascending:limit:]_block_invoke.69
- __122-[SGSqlEntityStore(Spotlight) tombstoneExistsForSpotlightReferenceWithBundleIdentifier:uniqueIdentifier:domainIdentifier:]_block_invoke.237
- __124-[SGSqlEntityStore(URLs) urlsFoundBetweenStartDate:endDate:excludingBundleIdentifiers:containingSubstring:flagFilter:limit:]_block_invoke.28
- __125-[SGSqlEntityStore(Spotlight) reindexSearchableItemsWithMinimumEntityId:searchableIndex:acknowledgementHandler:reindexCount:]_block_invoke.272
- __125-[SGSqlEntityStore(Spotlight) reindexSearchableItemsWithMinimumEntityId:searchableIndex:acknowledgementHandler:reindexCount:]_block_invoke.276
- __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.582
- __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.652
- __128-[SGExtractionDissector entityForOutputItem:withSiblings:parentEntity:outputExceptions:outputInfos:interaction:tagPartialEvent:]_block_invoke.713
- __131+[SGCuratedContactMatcher _compareContact:cnContact:newDetails:matchedDetails:matchPreference:stopOnNewDetail:stopOnMatchedDetail:]_block_invoke.33
- __132+[SGWordBoundaryQuickTypeInference quickTypeTriggerForContext:localeIdentifier:modelConfigPath:espressoBinFilePath:useContactNames:]_block_invoke.25
- __132+[SGWordBoundaryQuickTypeInference quickTypeTriggerForContext:localeIdentifier:modelConfigPath:espressoBinFilePath:useContactNames:]_block_invoke.27
- __136-[SGDSuggestManager(RealtimeDonations) suggestionsFromSingleMessage:options:completionDelivery:completionHandler:fullCompletionHandler:]_block_invoke.41
- __139+[SGMISpotlightUtility queryEmailsFromDaysAgo:throughDaysAgo:fetchAttributes:filterQuery:queryString:bundleIds:spotlightTimeOut:withError:]_block_invoke.49
- __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.54
- __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.56
- __142+[SGMIFollowUpAnalyzer _analyzeFeatureVector:withRegExpDictionary:forOutgoingMail:withDetectedLanguage:withRegExLanguage:withCustomTimeRange:]_block_invoke.58
- __145-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:]_block_invoke.574
- __146-[SGDSuggestManager(BatchDonations) batchSuggestionsFromMessages:options:completionDelivery:batchCompletion:writeBackCompletion:shouldStopSignal:]_block_invoke.27
- __153-[SGDSuggestManager(RealtimeDonations) _suggestionsFromSingleSearchableItem:options:dissectIfNecessary:processingType:completionDelivery:withCompletion:]_block_invoke.14
- __165+[SGMISubmodelsManager incrementalSubmodelUpdateWithSaliencyModelConfig:store:shouldContinue:finalGroundTruthDate:withSimulatedCSSearchableItemForTesting:limit:log:]_block_invoke.40
- __187-[SGDSuggestManager(BatchDonations) batchSuggestionsFromSearchableItems:options:dissectIfNecessary:processingType:completionDelivery:batchCompletion:writeBackCompletion:shouldStopSignal:]_block_invoke.21
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.110
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.112
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.121
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.126
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.130
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.131
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.81
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke.90
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_2.82
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_2.91
- __196-[SGDSuggestManager(RealtimeDonations) realtimeSuggestionsForMailOrMessageWithHash:options:completion:completionDelivery:providedBy:searchableItem:dissectIfNecessary:processingType:isTextMessage:]_block_invoke_3.92
- __20-[SGFlightData init]_block_invoke.77
- __20-[SGFlightData init]_block_invoke.84
- __20-[SGFlightData init]_block_invoke.89
- __20-[SGFlightData init]_block_invoke_2.85
- __223+[SGMIOmissionAnalyzer identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.10
- __223+[SGMIOmissionAnalyzer identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.7
- __224+[SGMIOmissionAnalyzer _identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:]_block_invoke.53
- __23-[SGDCloudKitSync init]_block_invoke.241
- __23-[SGDCloudKitSync init]_block_invoke.246
- __25-[SGAccountsAdapter init]_block_invoke.4
- __26-[SGSqliteDatabase vacuum]_block_invoke.204
- __26-[SGSqliteDatabase vacuum]_block_invoke.212
- __26-[SGSqliteDatabase vacuum]_block_invoke_2.208
- __26-[SGSqliteDatabase vacuum]_block_invoke_2.213
- __27-[SGPatterns regex2ForKey:]_block_invoke.116
- __27-[SGReverseTemplateJS init]_block_invoke.9
- __28-[SGDSpotlightReceiver init]_block_invoke.10
- __28-[SGDSpotlightReceiver init]_block_invoke.14
- __28-[SGDSpotlightReceiver init]_block_invoke.25
- __28-[SGDSpotlightReceiver init]_block_invoke.29
- __28-[SGDSpotlightReceiver init]_block_invoke_2.19
- __28-[SGDSpotlightReceiver init]_block_invoke_2.28
- __28-[SGDSpotlightReceiver init]_block_invoke_2.31
- __29-[SGMIFeatureVector feature:]_block_invoke.44
- __29-[SGMIFeatureVector feature:]_block_invoke.47
- __29-[SGMIFeatureVector feature:]_block_invoke.65
- __30-[SGDCloudKitSync accountInfo]_block_invoke.272
- __30-[SGDCloudKitSync privacySalt]_block_invoke.371
- __30-[SGDCloudKitSync privacySalt]_block_invoke.372
- __30-[SGDCloudKitSync privacySalt]_block_invoke.375
- __30-[SGDCloudKitSync privacySalt]_block_invoke.379
- __30-[SGDOMParser _parseDocument:]_block_invoke.14
- __31+[SGPipeline parallelPipeline:]_block_invoke.51
- __31-[SGDCloudKitSync setDatabase:]_block_invoke.307
- __31-[SGDCloudKitSync setDatabase:]_block_invoke.308
- __31-[SGDCloudKitSync setDatabase:]_block_invoke.324
- __31-[SGDCloudKitSync setDatabase:]_block_invoke.325
- __31-[SGDCloudKitSync setDatabase:]_block_invoke.329
- __32+[SGDomainWhitelistChecker lock]_block_invoke.6
- __33+[SGDSuggestManager requestCache]_block_invoke.232
- __33+[SGDSuggestManager requestCache]_block_invoke_2.233
- __33-[SGDCloudKitSync deleteGroupId:]_block_invoke.342
- __33-[SGDCloudKitSync deleteGroupId:]_block_invoke.346
- __34-[SGSqliteDatabase maxIdForTable:]_block_invoke.174
- __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.71
- __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.74
- __35-[SGSuggestHistory migrateIfNeeded]_block_invoke.75
- __36+[SGNames stripAndReturnHonorifics:]_block_invoke.69
- __36+[SGNames stripAndReturnHonorifics:]_block_invoke.71
- __36-[SGSqlEntityStore(Tags) commitTag:]_block_invoke.6
- __37+[SGThreadParser nextMessage:entity:]_block_invoke.17
- __38-[SGDCloudKitSync processStateChanges]_block_invoke.264
- __38-[SGDCloudKitSync processStateChanges]_block_invoke.265
- __39-[SGIdentityName initWithJapaneseName:]_block_invoke.80
- __39-[SGPipeline _dissectOperations:block:]_block_invoke.64
- __39-[SGPipeline _dissectOperations:block:]_block_invoke.65
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.102
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.109
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.118
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.167
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.197
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.263
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.270
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.283
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.74
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.78
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke.89
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.126
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.172
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.207
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_2.82
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_3.185
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_3.214
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_4.221
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_5.227
- __39-[SGReverseTemplateJS initCurrentAsset]_block_invoke_6.233
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.103
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.116
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.125
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.135
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.154
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.164
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.174
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.187
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.200
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.213
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.228
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.82
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke.89
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.129
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.139
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.158
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.168
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.178
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.191
- __39-[SGSqlEntityStore(SqlHelpers) dbStats]_block_invoke_2.204
- __40-[SGDSuggestManager bumptTTLForNLEvent:]_block_invoke.562
- __40-[SGMailClientUtil allVIPEmailAddresses]_block_invoke.13
- __40-[SGSqlEntityStore(Events) insertEvent:]_block_invoke.19
- __41-[SGDCloudKitSync addCreateZoneOperation]_block_invoke.151
- __41-[SGDCloudKitSync addDeleteZoneOperation]_block_invoke.140
- __41-[SGDManagerForCTS _performTrimActivity:]_block_invoke.40
- __41-[SGDManagerForCTS _performTrimActivity:]_block_invoke.49
- __41-[SGSqlEntityStore(Writing) writeEntity:]_block_invoke.34
- __42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.275
- __42+[SGAsset downloadMetadataWithCompletion:]_block_invoke.276
- __42+[SGModel transformerInstanceForLanguage:]_block_invoke.35
- __42+[SGModel transformerInstanceForLanguage:]_block_invoke_2.37
- __43+[SGPatterns pauseCacheEvictionTemporarily]_block_invoke.123
- __43-[SGMIFeatureStore warningStatsForLogging:]_block_invoke.637
- __43-[SGReverseTemplateJS emailToOutput:reply:]_block_invoke.541
- __43-[SGSqlEntityStore(Reminders) getReminder:]_block_invoke.5
- __43-[SGSqlEntityStore(SqlHelpers) entityCount]_block_invoke.61
- __44-[SGDManagerForCTS _performSendRTCActivity:]_block_invoke.60
- __45-[SGCNContactIdentifierCollection proxyArray]_block_invoke.7
- __45-[SGReminderTrialClientWrapper updateFactors]_block_invoke.55
- __45-[SGSqlEntityStore emailsPendingVerification]_block_invoke.149
- __45-[SGSqlEntityStore(DatabaseMigrator) migrate]_block_invoke.154
- __46-[SGDatabaseJournal executeQueriesOnDatabase:]_block_invoke.57
- __46-[SGSqlEntityStore(Spotlight) recordIdForKey:]_block_invoke.82
- __46-[SGSqlEntityStore(SqlHelpers) clearAllTables]_block_invoke.289
- __47-[SGDCloudKitSync addFetchNewEntitiesOperation]_block_invoke.188
- __47-[SGDCloudKitSync addFetchNewEntitiesOperation]_block_invoke.197
- __47-[SGSqlEntityStore(Loading) _loadMessageByKey:]_block_invoke.104
- __47-[SGSqlEntityStore(Tags) loadTagForPrimaryKey:]_block_invoke.12
- __47-[SGSqlEntityStore(Writing) _loadIdentityBlobs]_block_invoke.380
- __47-[SGSqlEntityStore(Writing) _loadIdentityBlobs]_block_invoke_2.385
- __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_2.30
- __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_3.34
- __48+[SGContactAggregator mergeContact:withContact:]_block_invoke_4.37
- __48+[SGMailClientUtil convertLineEndingsToNetwork:]_block_invoke.39
- __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.155
- __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.157
- __49+[SGMIOmissionAnalyzer matchRecentContact:store:]_block_invoke.162
- __49-[SGDCloudKitSync createSubscriptionWithRetries:]_block_invoke.293
- __49-[SGMIDomainCountingTable deleteDomainSelection:]_block_invoke.372
- __49-[SGSqlEntityStore confirmRealtimeContact:error:]_block_invoke.593
- __49-[SGSqlEntityStore(IdentityStore) loadInterdicts]_block_invoke.56
- __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke.398
- __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke.409
- __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke_2.399
- __49-[SGSqlEntityStore(Writing) _labelIdentityBlobs:]_block_invoke_2.410
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.16
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.19
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke.20
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_2.17
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_2.21
- __50+[SGMailQuoteParser _tofuRegions:utf8:isAOSPMail:]_block_invoke_3.18
- __50-[SGDCloudKitSync addEnrichment:withParentEntity:]_block_invoke.332
- __50-[SGDCloudKitSync addEnrichment:withParentEntity:]_block_invoke.340
- __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.100
- __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.113
- __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.117
- __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.122
- __50-[SGSuggestHistory migrateFromKVS:withCompletion:]_block_invoke.99
- __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.48
- __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.56
- __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke.57
- __51-[SGSqlEntityStore(Events) loadEventForPrimaryKey:]_block_invoke_2.49
- __51-[SGSqlEntityStore(Events) updateEvent:primaryKey:]_block_invoke.4
- __51-[SGSqlEntityStore(Saliency) saliencyForMessageId:]_block_invoke.21
- __52+[SGDCloudKitSync apsEnvironmentStringForContainer:]_block_invoke.285
- __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.30
- __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.53
- __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.58
- __52-[SGSqlEntityStore(DatabaseMigrator) clearDatabase:]_block_invoke.62
- __52-[SGSqlEntityStore(Deleting) childrenFromParentKey:]_block_invoke.102
- __52-[SGSqlEntityStore(IdentityStore) _computeBlobsRaw:]_block_invoke.299
- __52-[SGSqlEntityStore(IdentityStore) _computeBlobsRaw:]_block_invoke_2.300
- __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.217
- __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.221
- __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.225
- __52-[SGSqlEntityStore(IdentityStore) deleteByRecordId:]_block_invoke.240
- __52-[SGStructuredEventTrialClientWrapper updateFactors]_block_invoke.41
- __53-[NSMutableString(EncodedWord) sg_decodeEncodedWords]_block_invoke.13
- __53-[SGDSuggestManager messagesToRefreshWithCompletion:]_block_invoke.659
- __53-[SGDSuggestManager updateMessages:state:completion:]_block_invoke.669
- __53-[SGMIFeatureStore shouldExposeWarning:updateAction:]_block_invoke.600
- __53-[SGMIFeatureStore shouldExposeWarning:updateAction:]_block_invoke_2.602
- __53-[SGSqlEntityStore(Loading) loadSourceKeyByRecordId:]_block_invoke.20
- __53-[SGSqlEntityStore(Reminders) commitStorageReminder:]_block_invoke.27
- __53-[SGSqlEntityStore(Writing) _writeMessageEntityToDb:]_block_invoke.211
- __53-[SGSqlEntityStore(Writing) _writeMessageEntityToDb:]_block_invoke_2.259
- __54-[SGSqlEntityStore(DatabaseMigrator) _renameTable:to:]_block_invoke.108
- __54-[SGSqlEntityStore(DatabaseMigrator) migrateDatabases]_block_invoke.3
- __55+[SGMISpotlightUtility itemWithUniqueIdentifier:error:]_block_invoke.37
- __55-[SGSqlEntityStore mostRecentParentKeyForDuplicateKey:]_block_invoke.161
- __55-[SGSqlEntityStore(Spotlight) contactsWithIdentifiers:]_block_invoke.260
- __55-[SGSqlEntityStore(Spotlight) contactsWithIdentifiers:]_block_invoke.265
- __56-[SGExtractionDissector jsonLdOutputFromPackedJSEntity:]_block_invoke.922
- __56-[SGSqlEntityStore(ContactDetails) commitContactDetail:]_block_invoke.12
- __56-[SGSqlEntityStore(IdentityStore) rebuildIdentityTables]_block_invoke.124
- __56-[SGSqlEntityStore(Loading) loadDuplicateKeyByRecordId:]_block_invoke.6
- __57-[SGDSuggestManager addInteractions:bundleId:completion:]_block_invoke.767
- __57-[SGMIFeatureStore _getSGMIStoredAddressesUsingDatabase:]_block_invoke.745
- __57-[SGSqlEntityStore(IdentityStore) link:to:type:strength:]_block_invoke.203
- __57-[SGSqlEntityStore(MessageManagement) markMessagesFound:]_block_invoke.78
- __57-[SGSqlEntityStore(TestHelpers) lastSeenTimestampForKey:]_block_invoke.6
- __57-[SGSqliteDatabase prepAndRunQuery:onPrep:onRow:onError:]_block_invoke.110
- __58+[SGMIBiomeUtility summarizeStreamByMessageWithPublisher:]_block_invoke.11
- __58+[SGSimpleMailMessage(RFC822Parsing) dateFromEmailString:]_block_invoke.135
- __58-[SGPOSTagger tokenizeTextContent:languageHint:gazetteer:]_block_invoke.11
- __58-[SGPOSTagger tokenizeTextContent:languageHint:gazetteer:]_block_invoke.12
- __58-[SGSqlEntityStore _rankSGContacts:bySimilarityToContact:]_block_invoke.311
- __58-[SGSqlEntityStore(DatabaseMigrator) selectMigrationQueue]_block_invoke.16
- __58-[SGSqlEntityStore(ExtractionInfos) commitExtractionInfo:]_block_invoke.8
- __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke.53
- __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke.64
- __58-[SGSqlEntityStore(Spotlight) duplicateKeysFromRecordIds:]_block_invoke_2.66
- __59-[SGSqlEntityStore(IdentityStore) _popMergeBlobForAnalysis]_block_invoke.360
- __59-[SGSqlEntityStore(StatsCounters) loadStatsCounterWithKey:]_block_invoke.36
- __60-[SGDSpotlightReceiver addOrUpdateSearchableItems:bundleID:]_block_invoke.47
- __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke.189
- __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke.197
- __60-[SGMIDomainCountingTable _commitDomainsAndCounts:toColumn:]_block_invoke_2.206
- __60-[SGMIFeatureStore updateFollowUpDetectionStatsWithWarning:]_block_invoke.618
- __60-[SGSqlEntityStore(Events) checkExistsEventForDuplicateKey:]_block_invoke.78
- __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.151
- __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.172
- __60-[SGSqlEntityStore(ReimportRequests) reimportRequestDBStats]_block_invoke.173
- __60-[SGSuggestHistory hasConfirmedField:value:forStorageEvent:]_block_invoke.216
- __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_3.59
- __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_4.62
- __61+[SGContactAggregator replaceDetailsInContact:onDiskContact:]_block_invoke_5.65
- __61-[SGDSuggestManager reportMessagesFound:lost:withCompletion:]_block_invoke.678
- __61-[SGSqlEntityStore(Locations) storageLocationWithPrimaryKey:]_block_invoke.5
- __62-[SGDSuggestManager titleSuggestionForMessage:withCompletion:]_block_invoke.929
- __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.282
- __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.284
- __62-[SGRTCLogging sendRTCLogsWithShouldContinueBlock:completion:]_block_invoke.291
- __62-[SGSqlEntityStore _filterOutAllButAcceptedWithUpdatedFields:]_block_invoke.499
- __62-[SGSqlEntityStore _filterOutAllButAcceptedWithUpdatedFields:]_block_invoke_2.506
- __62-[SGSqlEntityStore(Saliency) topSalienciesForMailboxId:limit:]_block_invoke.45
- __62-[SGStorageContact convertToContact:sourceEntity:enrichments:]_block_invoke.86
- __62-[SGStorageContact convertToContact:sourceEntity:enrichments:]_block_invoke_2.91
- __63-[SGAppLaunchHistory launchCountsForBundleIds:afterDate:limit:]_block_invoke.16
- __63-[SGAppLaunchHistory launchCountsForBundleIds:afterDate:limit:]_block_invoke.21
- __63-[SGDSuggestManager extractAttributesAndDonate:withCompletion:]_block_invoke.1023
- __63-[SGEKCalendarAdapter _eventsAssociatedWithStorageEvent:store:]_block_invoke.42
- __63-[SGMIFeatureStore incrementUserEngagement:forFollowUpWarning:]_block_invoke.586
- __63-[SGSqlEntityStore _matchableUTF8TokenRangesInMatchExpression:]_block_invoke.378
- __63-[SGSqlEntityStore _matchableUTF8TokenRangesInMatchExpression:]_block_invoke.399
- __63-[SGSqlEntityStore(CNtoSGContacts) _fullSyncContactsWithStore:]_block_invoke.135
- __63-[SGSqlEntityStore(DatabaseCheck) databasecheck_IntegrityCheck]_block_invoke.34
- __63-[SGSqlEntityStore(DatabaseCheck) databasecheck_IntegrityCheck]_block_invoke.44
- __63-[SGSqlEntityStore(SerializedContacts) _trimSerializedContacts]_block_invoke.77
- __64-[SGDManagerForCTS _performMobileAssetMetadataDownloadActivity:]_block_invoke.30
- __64-[SGDManagerForCTS _performMobileAssetMetadataDownloadActivity:]_block_invoke.31
- __64-[SGSqlEntityStore storageContactByMasterEntityId:withSnippets:]_block_invoke.179
- __64-[SGSqlEntityStore storageContactByMasterEntityId:withSnippets:]_block_invoke.199
- __64-[SGSqlEntityStore(CNtoSGContacts) _enqueueBatchOfCNContactIds:]_block_invoke.95
- __64-[SGSqlEntityStore(Reminders) reminderSourceKeyForDuplicateKey:]_block_invoke.34
- __65+[SGSelfIdentification processConversation:threadLength:options:]_block_invoke.21
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.1004
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.1009
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke.996
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.1005
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.1010
- __65-[SGDSuggestManager deleteDataDerivedFromContentMatchingRequest:]_block_invoke_2.997
- __65-[SGSqlEntityStore masterEntityIDsForMasterEntityQuery:bindings:]_block_invoke.204
- __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke.375
- __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke_2.385
- __65-[SGSqlEntityStore(IdentityStore) _analyzeMergeBlobsIncremental:]_block_invoke_3.392
- __65-[SGSqlEntityStore(SerializedContacts) loadAllSerializedContacts]_block_invoke.70
- __65-[SGSqlEntityStore(SqlHelpers) entityFromSqlResult:withSnippets:]_block_invoke.27
- __65-[SGSqlEntityStore(SqlHelpers) entityFromSqlResult:withSnippets:]_block_invoke.31
- __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.49
- __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.55
- __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.61
- __65-[SGSqlEntityStore(Writing) _prunePseudoContactGeneratingEmails:]_block_invoke.67
- __65-[SGSqlEntityStoreCNContactMatcherHelper prefilterNameMatchTerms]_block_invoke.4
- __66-[SGDCloudKitSync addFetchNewEntitiesAttemptOperationWithRetries:]_block_invoke.209
- __66-[SGDCloudKitSync addFetchNewEntitiesAttemptOperationWithRetries:]_block_invoke.211
- __66-[SGDCloudKitSync pauseIfNeededAndReturnRetryEligibilityForError:]_block_invoke.135
- __66-[SGSqlEntityStore(DatabaseMigrator) migration_deleteInteractions]_block_invoke.446
- __66-[SGSqlEntityStore(Deleting) deleteMailIntelligenceForMessageIds:]_block_invoke.55
- __66-[SGSqlEntityStore(Deleting) deleteMailIntelligenceForMessageIds:]_block_invoke.63
- __66-[SGSqlEntityStore(Spotlight) batchOf:contactsStartingAtEntityId:]_block_invoke.251
- __67+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersForContact:]_block_invoke.303
- __67+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersForContact:]_block_invoke.307
- __67+[SGTokenizerMappingTransformer _purgeableNLTaggerWithNameTagging:]_block_invoke.178
- __67-[SGSqlEntityStore(DatabaseMigrator) migration_deleteNilDateEvents]_block_invoke.473
- __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke.33
- __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke_2.34
- __67-[SGSqlEntityStore(ReimportRequests) storeReimportItems:requestId:]_block_invoke_3.35
- __67-[SGSqlEntityStore(SerializedContacts) loadSerializedContactForId:]_block_invoke.51
- __67-[SGSqlEntityStore(SerializedContacts) loadSerializedContactForId:]_block_invoke_2.56
- __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.12
- __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.15
- __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.16
- __68-[SGAutonamingConsumer deleteDataDerivedFromContentMatchingRequest:]_block_invoke.23
- __68-[SGDManagerForCTS _processMessage:pipeline:context:harvestMetrics:]_block_invoke.152
- __68-[SGDManagerForCTS _processMessage:pipeline:context:harvestMetrics:]_block_invoke.157
- __68-[SGSqlEntityStore suggestContactMatchesWithFullTextSearch:limitTo:]_block_invoke.363
- __68-[SGSqlEntityStore suggestContactMatchesWithFullTextSearch:limitTo:]_block_invoke_2.364
- __69-[SGMIFeatureStore _applyCappingPolicy:shouldContinue:usingDatabase:]_block_invoke.763
- __69-[SGMIFeatureStore _applyCappingPolicy:shouldContinue:usingDatabase:]_block_invoke.765
- __69-[SGSqlEntityStore suggestContactMatchesWithMessagingPrefix:limitTo:]_block_invoke.334
- __69-[SGSqlEntityStore suggestContactMatchesWithMessagingPrefix:limitTo:]_block_invoke.339
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.178
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.182
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.189
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.196
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke.200
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke_2.192
- __69-[SGSqlEntityStore(DatabaseMigrator) migration_MoveContentToSnippets]_block_invoke_2.203
- __69-[SGSqlEntityStore(Deleting) _deleteChildEntitiesByRecordIdsInTable:]_block_invoke.133
- __69-[SGSqlEntityStore(ExtractionInfos) loadExtractionInfoForPrimaryKey:]_block_invoke.14
- __70-[SGSqlEntityStore(IdentityStore) _writeMergeBlobSnapshotForAnalysis:]_block_invoke.352
- __71-[SGDSuggestManager cachedResultForKey:generateResult:validateResults:]_block_invoke.556
- __71-[SGDSuggestManager geocodeEnrichmentsInPipelineEntity:withCompletion:]_block_invoke.820
- __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.108
- __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.111
- __71-[SGSignatureDissector shouldIgnoreSignature:signatureRange:isInhuman:]_block_invoke.99
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.363
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.370
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke.377
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.366
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.373
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageEntities]_block_invoke_2.380
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke.391
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke.395
- __71-[SGSqlEntityStore(DatabaseMigrator) migration_separateMessageSnippets]_block_invoke_2.392
- __71-[SGSqlEntityStore(IdentityStore) processPseudoContactEntity:recordId:]_block_invoke.71
- __71-[SGSqlEntityStore(IdentityStore) processPseudoContactEntity:recordId:]_block_invoke.76
- __71-[SGSqlEntityStore(Writing) _writeLabeledBlobs:deletedMasterEntityIds:]_block_invoke.419
- __72-[SGSqlEntityStore(CNtoSGContacts) initRefreshSuggestionsContactDropBox]_block_invoke.164
- __72-[SGSqlEntityStore(DatabaseMigrator) migration_AddNewishTablesIfMissing]_block_invoke.237
- __72-[SGSqlEntityStore(DatabaseMigrator) migration_AddNewishTablesIfMissing]_block_invoke.250
- __72-[SGSqlEntityStore(StatsCounters) addValue:toMessageTracerKey:inDomain:]_block_invoke.47
- __73-[SGDSuggestManager _processReservationInteractions:bundleId:completion:]_block_invoke.790
- __73-[SGDSuggestManager suggestionsFromURL:title:HTMLPayload:withCompletion:]_block_invoke.814
- __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.684
- __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.708
- __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke.712
- __73-[SGMIFeatureStore _subModelsStatsWithShouldContinueBlock:usingDatabase:]_block_invoke_2.714
- __73-[SGSqlEntityStore(DatabaseCheck) databasecheck_BrokenEntityIDReferences]_block_invoke.65
- __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.315
- __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.319
- __73-[SGSqlEntityStore(DatabaseMigrator) migration_DeduplicateIdentityPhones]_block_invoke.323
- __73-[SGSqlEntityStore(MessageManagement) pruneLostMessagesWithSource:count:]_block_invoke.63
- __73-[SGSqlEntityStore(MessageManagement) pruneLostMessagesWithSource:count:]_block_invoke_2.67
- __73-[SGSqlEntityStore(SerializedContacts) deleteSerializedContactsForIdSet:]_block_invoke.35
- __73-[SGSqlEntityStore(SerializedContacts) deleteSerializedContactsForIdSet:]_block_invoke.40
- __74-[SGDSuggestManager launchAppForSuggestedEventUsingLaunchInfo:completion:]_block_invoke.712
- __74-[SGSqlEntityStore(IdentityStore) makeInterdictsForBlob:withContactStore:]_block_invoke.336
- __74-[SGSqlEntityStore(IdentityStore) makeInterdictsForBlob:withContactStore:]_block_invoke.341
- __74-[SGSqlEntityStore(SpotlightMapping) messageIdsForBundleIdentifier:limit:]_block_invoke.15
- __75-[SGSqlEntityStore(ContactDetails) contactDetailPrimaryKeyForDuplicateKey:]_block_invoke.17
- __75-[SGSqlEntityStore(DatabaseMigrator) updateLanguageForFTSTablesToLanguage:]_block_invoke.117
- __75-[SGSqlEntityStore(ReimportRequests) _loadReimportRequestsWithWhereClause:]_block_invoke.100
- __75-[SGSqlEntityStore(SqlHelpers) selectAuthoritativeDetailsForContactWithId:]_block_invoke.321
- __76-[SGSqlEntityStore(Loading) entityKeyCountsForEntityType:startDate:endDate:]_block_invoke.206
- __76-[SGSqlEntityStore(SpotlightMapping_Internal) uniqueIdentifierForMessageId:]_block_invoke.6
- __77+[SGLowMemoryContactEnumeration enumerateContactIdentifierBatchesUsingBlock:]_block_invoke.11
- __77+[SGLowMemoryContactEnumeration enumerateContactIdentifierBatchesUsingBlock:]_block_invoke_2.12
- __77+[SGMIFollowUpAnalyzer analyzeForFollowUpMailWithBody:isSent:messageId:date:]_block_invoke.89
- __77+[SGMIFollowUpAnalyzer analyzeForFollowUpMailWithBody:isSent:messageId:date:]_block_invoke_2.93
- __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke.84
- __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke.88
- __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke_2.102
- __77-[SGSqlEntityStore(DatabaseCheck) databasecheck_contactMergeGroupConsistency]_block_invoke_3.104
- __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke.495
- __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke.503
- __77-[SGSqlEntityStore(DatabaseMigrator) migration_addAppleMailMessageIdToEvents]_block_invoke_2.498
- __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke.167
- __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke.174
- __77-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:]_block_invoke_2.171
- __77-[SGSqlEntityStore(URLs) urlsFoundBetweenStartDate:endDate:bundleIdentifier:]_block_invoke.85
- __78-[SGSqlEntityStore(ContactDetails) loadAllContactDetailsFromTableForRecordId:]_block_invoke.26
- __79-[SGSqlEntityStore _contactIdsForContactNameMatches:strongNameIds:weakNameIds:]_block_invoke.261
- __80-[SGDetectedAttributeML birthdayCongratsTextMessage:andLanguage:andHealthStore:]_block_invoke.158
- __80-[SGPipeline verificationOperation:overrideVerificationStatus:withDependencies:]_block_invoke.138
- __81-[SGDSuggestManager dissectAttachmentsFromSearchableItem:options:withCompletion:]_block_invoke.949
- __81-[SGSqlEntityStore(Deleting) pruneEntitiesOlderThan:suspensionHandler:batchSize:]_block_invoke.34
- __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.419
- __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.424
- __82-[SGSqlEntityStore(DatabaseMigrator) migration_rebuildFTSWithDetailEntityIDDocIDs]_block_invoke.431
- __82-[SGSqlEntityStore(IdentityStore) _uniqueGoodDetailMatchFrom:toDetails:nonUnique:]_block_invoke.323
- __82-[SGSqlEntityStore(Loading) loadEntitiesByEntityKey:entityType:resolveDuplicates:]_block_invoke.125
- __83-[SGDSpotlightCommander _reimportQueryForPersonHandle:startDate:endDate:requestId:]_block_invoke.50
- __83-[SGDSpotlightReceiver deleteInteractionsWithIdentifiers:bundleID:protectionClass:]_block_invoke.104
- __83-[SGDSuggestManager logEventInteractionForEventWithUniqueKey:interface:actionType:]_block_invoke.880
- __84-[SGDSuggestManager _harvestReservationsFromInteractions:bundleId:queue:completion:]_block_invoke.781
- __84-[SGDSuggestManager _harvestReservationsFromInteractions:bundleId:queue:completion:]_block_invoke.782
- __84-[SGDSuggestManager realtimeContactsFromEntity:enrichments:sourceTextMessage:store:]_block_invoke.613
- __84-[SGSqlEntityStore(DatabaseMigrator) _slowCopyFromTable:toTable:startingAtEntityId:]_block_invoke.86
- __84-[SGSqlEntityStore(DatabaseMigrator) _slowCopyFromTable:toTable:startingAtEntityId:]_block_invoke.91
- __84-[SGSqlEntityStore(SpotlightMapping) messageIdForBundleIdentifier:uniqueIdentifier:]_block_invoke.7
- __84-[SGSqlEntityStore(Writing) _deleteOldInteractionContactDetails:currentIdentifiers:]_block_invoke.82
- __85-[SGSqlEntityStore(CNtoSGContacts) loadCNContactMatchesForContact:andGetMaxEntityId:]_block_invoke.35
- __85-[SGSqlEntityStore(CNtoSGContacts) loadCNContactMatchesForContact:andGetMaxEntityId:]_block_invoke.38
- __86-[SGMIFeatureStore _purgeTokensWhichLastUpdateWasBefore:shouldContinue:usingDatabase:]_block_invoke.730
- __86-[SGSqlEntityStore(Spotlight) _duplicateKeysWithZeroSpotlightReferencesFromRecordIds:]_block_invoke.112
- __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.188
- __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.213
- __87+[SGSqlEntityStore(CNtoSGContacts) cnContactIdentifiersSpotlightQueryStringForContact:]_block_invoke.232
- __87-[SGDSuggestManager suggestionsFromEmailContent:headers:source:options:withCompletion:]_block_invoke.941
- __87-[SGDetectedAttributeML handleTextMessageContactSharingWithNegativeSample:andLanguage:]_block_invoke.161
- __87-[SGDetectedAttributeML selfIdDetectionWithTextMessage:inConversation:withSupervision:]_block_invoke.147
- __87-[SGDetectedAttributeML selfIdDetectionWithTextMessage:inConversation:withSupervision:]_block_invoke.150
- __87-[SGSqlEntityStore(Loading) loadAllContactDetailsWithWhereClause:onPrep:dedupeAgainst:]_block_invoke.193
- __87-[SGSqlEntityStore(Writing) writeEmailVerificationResultForEmailWithKey:eventEntities:]_block_invoke.189
- __87-[SGSqlEntityStore(Writing) writeEmailVerificationResultForEmailWithKey:eventEntities:]_block_invoke.194
- __88-[SGDCloudKitSync addWriteOperationForRecordGetter:deleteGetter:withRetries:isFirstTry:]_block_invoke.221
- __88-[SGMIDomainCountingTable enumerateChildrenOfDomain:greaterThan:depth:limit:usingBlock:]_block_invoke.304
- __89-[SGSqlEntityStore(Deleting) pruneMailIntelligenceOlderThanOneYearWithSuspensionHandler:]_block_invoke.44
- __90-[SGSqlEntityStore(ReimportRequests) markReimportItemsAsSeenByReceiverWithBundleId:items:]_block_invoke.62
- __91+[SGSqlEntityStore _initializeDatabaseNolock:withProtection:sharedLock:newDatabaseCreated:]_block_invoke.47
- __91-[SGEnrichmentWritebackAdapter _deleteEventsMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.39
- __92+[SGContactsInterface enumerateContactsWithFetchRequest:usingContactStore:error:usingBlock:]_block_invoke.28
- __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.312
- __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.320
- __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke.323
- __92-[SGSqlEntityStore(Deleting) deleteInteractionEntitiesExceedingLimit:withSuspensionHandler:]_block_invoke_2.313
- __92-[SGSqlEntityStore(ReimportRequests) markReimportItemAsSeenByReceiverWithBundleId:uniqueId:]_block_invoke.73
- __94+[SGMISpotlightUtility findDeletedEmailAddresses:mdSearchableItemAttribute:fromDaysAgo:error:]_block_invoke.45
- __94-[SGSqlEntityStore(ReimportRequests) updateReimportItemUniqueIdForBundleId:oldValue:newValue:]_block_invoke.81
- __95+[SGMISpotlightUtility queryFromDaysAgo:throughDaysAgo:limit:withError:simulatedCSSIs:handler:]_block_invoke.18
- __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke.284
- __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke_2.287
- __95-[SGSqlEntityStore suggestContactsWithContact:withSnippets:filterConfirmRejectDetails:limitTo:]_block_invoke_3.291
- __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke.117
- __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke.126
- __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke_2.123
- __95-[SGSqlEntityStore(ReimportRequests) reimportRequestsContainBundleIdentifier:uniqueIdentifier:]_block_invoke_2.127
- __95-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:domainIdentifiers:]_block_invoke.156
- __95-[SGSqlEntityStore(Spotlight) deleteSpotlightReferencesWithBundleIdentifier:domainIdentifiers:]_block_invoke_2.158
- __95-[SGSqlEntityStore(StatsCounters) persistStatisticsDictionary:andAdditiveStatisticsDictionary:]_block_invoke.63
- __95-[SGSqlEntityStore(StatsCounters) persistStatisticsDictionary:andAdditiveStatisticsDictionary:]_block_invoke_2.64
- __96-[SGEnrichmentWritebackAdapter _uniqueIdentifiersMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.30
- __96-[SGEnrichmentWritebackAdapter _uniqueIdentifiersMatchingGroupId:fallbackGroupId:olderThanDate:]_block_invoke.34
- __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.226
- __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.245
- __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke.249
- __96-[SGSqlEntityStore _contactIdsForContactDetailMatches:detailContactIds:socialProfileContactIds:]_block_invoke_2.253
- __97-[SGDSuggestManager harvestedSuggestionsFromMessages:bundleIdentifier:options:completionHandler:]_block_invoke.960
- __97-[SGDSuggestManager harvestedSuggestionsFromMessages:bundleIdentifier:options:completionHandler:]_block_invoke_2.961
- __98-[SGSqlEntityStore suggestEventsStartingAt:endingAt:limitTo:additionalWhereClause:options:onPrep:]_block_invoke.532
- __98-[SGSqlEntityStore(Loading) loadContactDetailsWithWhereClause:onPrep:type:dedupeAgainst:recordId:]_block_invoke.175
- __99+[SGReminderMessage detectedTitleInModelOutput:enrichedTaggedCharacterRanges:textContent:language:]_block_invoke.130
- __99-[SGDetectedAttributeDissector handleTextMessageSelfIdentification:entity:withConversationHistory:]_block_invoke.152
- __99-[SGMIFeatureStore _naiveBayesModelQueryResultForFeature:unigramTokens:bigramTokens:usingDatabase:]_block_invoke.537
- __99-[SGMIFeatureStore _naiveBayesModelQueryResultForFeature:unigramTokens:bigramTokens:usingDatabase:]_block_invoke_2.538
- __99-[SGSqlEntityStore(IdentityStore) _joinIncompleteIdentityPhonesWithOthersOfTheirIlk:name:recordId:]_block_invoke.182
- __Block_byref_object_copy_.10168
- __Block_byref_object_copy_.11269
- __Block_byref_object_copy_.11362
- __Block_byref_object_copy_.1154
- __Block_byref_object_copy_.12228
- __Block_byref_object_copy_.12944
- __Block_byref_object_copy_.13416
- __Block_byref_object_copy_.14494
- __Block_byref_object_copy_.1462
- __Block_byref_object_copy_.1489
- __Block_byref_object_copy_.15080
- __Block_byref_object_copy_.15436
- __Block_byref_object_copy_.15692
- __Block_byref_object_copy_.16291
- __Block_byref_object_copy_.16409
- __Block_byref_object_copy_.17008
- __Block_byref_object_copy_.17409
- __Block_byref_object_copy_.18210
- __Block_byref_object_copy_.1840
- __Block_byref_object_copy_.18860
- __Block_byref_object_copy_.2113
- __Block_byref_object_copy_.21291
- __Block_byref_object_copy_.21624
- __Block_byref_object_copy_.21796
- __Block_byref_object_copy_.22130
- __Block_byref_object_copy_.22843
- __Block_byref_object_copy_.23430
- __Block_byref_object_copy_.23803
- __Block_byref_object_copy_.23888
- __Block_byref_object_copy_.24321
- __Block_byref_object_copy_.24598
- __Block_byref_object_copy_.262
- __Block_byref_object_copy_.2626
- __Block_byref_object_copy_.26264
- __Block_byref_object_copy_.26581
- __Block_byref_object_copy_.26729
- __Block_byref_object_copy_.27498
- __Block_byref_object_copy_.28949
- __Block_byref_object_copy_.29109
- __Block_byref_object_copy_.29512
- __Block_byref_object_copy_.30267
- __Block_byref_object_copy_.31640
- __Block_byref_object_copy_.32706
- __Block_byref_object_copy_.32817
- __Block_byref_object_copy_.33727
- __Block_byref_object_copy_.33795
- __Block_byref_object_copy_.34090
- __Block_byref_object_copy_.3435
- __Block_byref_object_copy_.34374
- __Block_byref_object_copy_.35074
- __Block_byref_object_copy_.35380
- __Block_byref_object_copy_.35479
- __Block_byref_object_copy_.36276
- __Block_byref_object_copy_.36634
- __Block_byref_object_copy_.36844
- __Block_byref_object_copy_.37777
- __Block_byref_object_copy_.38051
- __Block_byref_object_copy_.38304
- __Block_byref_object_copy_.38461
- __Block_byref_object_copy_.40283
- __Block_byref_object_copy_.4037
- __Block_byref_object_copy_.40627
- __Block_byref_object_copy_.41189
- __Block_byref_object_copy_.42337
- __Block_byref_object_copy_.5340
- __Block_byref_object_copy_.6672
- __Block_byref_object_copy_.7562
- __Block_byref_object_copy_.8337
- __Block_byref_object_copy_.9360
- __Block_byref_object_copy_.9661
- __Block_byref_object_copy_.9795
- __Block_byref_object_copy_.9944
- __Block_byref_object_dispose_.10169
- __Block_byref_object_dispose_.11270
- __Block_byref_object_dispose_.11363
- __Block_byref_object_dispose_.1155
- __Block_byref_object_dispose_.12229
- __Block_byref_object_dispose_.12945
- __Block_byref_object_dispose_.13417
- __Block_byref_object_dispose_.14495
- __Block_byref_object_dispose_.1463
- __Block_byref_object_dispose_.1490
- __Block_byref_object_dispose_.15081
- __Block_byref_object_dispose_.15437
- __Block_byref_object_dispose_.15693
- __Block_byref_object_dispose_.16292
- __Block_byref_object_dispose_.16410
- __Block_byref_object_dispose_.17009
- __Block_byref_object_dispose_.17410
- __Block_byref_object_dispose_.18211
- __Block_byref_object_dispose_.1841
- __Block_byref_object_dispose_.18861
- __Block_byref_object_dispose_.2114
- __Block_byref_object_dispose_.21292
- __Block_byref_object_dispose_.21625
- __Block_byref_object_dispose_.21797
- __Block_byref_object_dispose_.22131
- __Block_byref_object_dispose_.22844
- __Block_byref_object_dispose_.23431
- __Block_byref_object_dispose_.23804
- __Block_byref_object_dispose_.23889
- __Block_byref_object_dispose_.24322
- __Block_byref_object_dispose_.24599
- __Block_byref_object_dispose_.26265
- __Block_byref_object_dispose_.2627
- __Block_byref_object_dispose_.263
- __Block_byref_object_dispose_.26582
- __Block_byref_object_dispose_.26730
- __Block_byref_object_dispose_.27499
- __Block_byref_object_dispose_.28950
- __Block_byref_object_dispose_.29110
- __Block_byref_object_dispose_.29513
- __Block_byref_object_dispose_.30268
- __Block_byref_object_dispose_.31641
- __Block_byref_object_dispose_.32707
- __Block_byref_object_dispose_.32818
- __Block_byref_object_dispose_.33728
- __Block_byref_object_dispose_.33796
- __Block_byref_object_dispose_.34091
- __Block_byref_object_dispose_.3436
- __Block_byref_object_dispose_.34375
- __Block_byref_object_dispose_.35075
- __Block_byref_object_dispose_.35381
- __Block_byref_object_dispose_.35480
- __Block_byref_object_dispose_.36277
- __Block_byref_object_dispose_.36635
- __Block_byref_object_dispose_.36845
- __Block_byref_object_dispose_.37778
- __Block_byref_object_dispose_.38052
- __Block_byref_object_dispose_.38305
- __Block_byref_object_dispose_.38462
- __Block_byref_object_dispose_.40284
- __Block_byref_object_dispose_.4038
- __Block_byref_object_dispose_.40628
- __Block_byref_object_dispose_.41190
- __Block_byref_object_dispose_.42338
- __Block_byref_object_dispose_.5341
- __Block_byref_object_dispose_.6673
- __Block_byref_object_dispose_.7563
- __Block_byref_object_dispose_.8338
- __Block_byref_object_dispose_.9361
- __Block_byref_object_dispose_.9662
- __Block_byref_object_dispose_.9796
- __Block_byref_object_dispose_.9945
- __ProactiveSummarizationLibraryCore_block_invoke.32696
- __SGNotUserInitiated_block_invoke.7
- __SGNotUserInitiated_block_invoke.8
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN3re211SparseArrayIPNS1_3NFA6ThreadEE10IndexValueENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN3re29RuneRangeENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPK9_vertex_tNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKNS0_IPK9_vertex_tNS_9allocatorIS3_EEEENS4_IS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN3re23DFA5StateENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN3re23RE2ENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN3re26RegexpENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN3re29PrefilterENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_setIPN3re23DFA5StateENS2_9StateHashENS2_10StateEqualENS_9allocatorIS4_EEED1B8ne180100Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPK9_vertex_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKNS_6vectorIPK9_vertex_tNS1_IS5_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPK9_vertex_tNS_6vectorIS6_NS1_IS6_EEEEEEPvEEEEEclB8ne180100EPSC_
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__15dequeIN3re29WalkStateINS1_4FragEEENS_9allocatorIS4_EEED2B8ne180100Ev
- __ZNSt3__15dequeIN3re29WalkStateIPNS1_6RegexpEEENS_9allocatorIS5_EEED2B8ne180100Ev
- __ZNSt3__15dequeIN3re29WalkStateIPNS1_9Prefilter4InfoEEENS_9allocatorIS6_EEED2B8ne180100Ev
- __ZNSt3__15dequeIN3re29WalkStateIbEENS_9allocatorIS3_EEED2B8ne180100Ev
- __ZNSt3__15dequeIN3re29WalkStateIiEENS_9allocatorIS3_EEED2B8ne180100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___100+[SGDSuggestManager filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:]_block_invoke
- ___145-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:]_block_invoke
- ___145-[SGDSuggestManager shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:]_block_invoke_2
- ___70-[SGDSpotlightReceiver _accessSummarizationPipelineForBundleId:block:]_block_invoke
- ___70-[SGDSpotlightReceiver deleteSearchableItemsWithIdentifiers:bundleID:]_block_invoke
- ___block_descriptor_149_e8_32s40s48s56s64s72s80bs88r96r_e33_"SGRealtimeSuggestionsTuple"8?0l
- ___block_descriptor_32_e34_v16?0"PSUSummarizationPipeline"8l
- ___block_descriptor_35_e28_"SGEntity"16?0"SGEntity"8l
- ___block_descriptor_40_e8_32bs_e34_v16?0"PSUSummarizationPipeline"8l
- ___block_descriptor_48_e8_32s40s_e34_v16?0"PSUSummarizationPipeline"8l
- __block_literal_global.10.37792
- __block_literal_global.101
- __block_literal_global.101.22731
- __block_literal_global.101.35465
- __block_literal_global.10123
- __block_literal_global.1019
- __block_literal_global.102.13879
- __block_literal_global.1022
- __block_literal_global.103
- __block_literal_global.103.27087
- __block_literal_global.10590
- __block_literal_global.107.32634
- __block_literal_global.108.30126
- __block_literal_global.10839
- __block_literal_global.1084
- __block_literal_global.11
- __block_literal_global.11.40879
- __block_literal_global.110.27080
- __block_literal_global.110.32625
- __block_literal_global.1106
- __block_literal_global.11083
- __block_literal_global.112.26241
- __block_literal_global.11223
- __block_literal_global.11278
- __block_literal_global.11402
- __block_literal_global.115
- __block_literal_global.11730
- __block_literal_global.118.17502
- __block_literal_global.118.22670
- __block_literal_global.118.32605
- __block_literal_global.119
- __block_literal_global.119.13860
- __block_literal_global.119.34739
- __block_literal_global.119.36631
- __block_literal_global.12.31555
- __block_literal_global.12.35383
- __block_literal_global.121.22420
- __block_literal_global.12297
- __block_literal_global.123
- __block_literal_global.12638
- __block_literal_global.12708
- __block_literal_global.128.14759
- __block_literal_global.129.13862
- __block_literal_global.129.16935
- __block_literal_global.129.19170
- __block_literal_global.13.36700
- __block_literal_global.13.40330
- __block_literal_global.13017
- __block_literal_global.1337
- __block_literal_global.135.16530
- __block_literal_global.136
- __block_literal_global.13654
- __block_literal_global.137.20882
- __block_literal_global.13910
- __block_literal_global.140
- __block_literal_global.14086
- __block_literal_global.141.17506
- __block_literal_global.141.20876
- __block_literal_global.141.31478
- __block_literal_global.14227
- __block_literal_global.1460
- __block_literal_global.14942
- __block_literal_global.14964
- __block_literal_global.1499
- __block_literal_global.150
- __block_literal_global.15021
- __block_literal_global.151
- __block_literal_global.151.27039
- __block_literal_global.151.8461
- __block_literal_global.15128
- __block_literal_global.152
- __block_literal_global.15271
- __block_literal_global.15583
- __block_literal_global.16.40336
- __block_literal_global.160
- __block_literal_global.160.32266
- __block_literal_global.16097
- __block_literal_global.16161
- __block_literal_global.16588
- __block_literal_global.17.31545
- __block_literal_global.17.32737
- __block_literal_global.170
- __block_literal_global.170.17512
- __block_literal_global.17066
- __block_literal_global.171
- __block_literal_global.173
- __block_literal_global.174
- __block_literal_global.17495
- __block_literal_global.175
- __block_literal_global.175.14828
- __block_literal_global.17738
- __block_literal_global.178
- __block_literal_global.181.33986
- __block_literal_global.18774
- __block_literal_global.188
- __block_literal_global.190.32267
- __block_literal_global.191
- __block_literal_global.19278
- __block_literal_global.1949
- __block_literal_global.19689
- __block_literal_global.19763
- __block_literal_global.200
- __block_literal_global.20254
- __block_literal_global.204
- __block_literal_global.207
- __block_literal_global.209
- __block_literal_global.209.36937
- __block_literal_global.20963
- __block_literal_global.21.38095
- __block_literal_global.21.40324
- __block_literal_global.211
- __block_literal_global.211.16978
- __block_literal_global.214
- __block_literal_global.21565
- __block_literal_global.21700
- __block_literal_global.21725
- __block_literal_global.2174
- __block_literal_global.218
- __block_literal_global.22.31539
- __block_literal_global.222.13564
- __block_literal_global.223
- __block_literal_global.22455
- __block_literal_global.226
- __block_literal_global.226.17114
- __block_literal_global.226.19167
- __block_literal_global.228.17116
- __block_literal_global.22837
- __block_literal_global.229.19161
- __block_literal_global.23.38096
- __block_literal_global.231
- __block_literal_global.233
- __block_literal_global.23480
- __block_literal_global.235.26334
- __block_literal_global.23726
- __block_literal_global.238
- __block_literal_global.238.16446
- __block_literal_global.238.16992
- __block_literal_global.23820
- __block_literal_global.23967
- __block_literal_global.24041
- __block_literal_global.241.22755
- __block_literal_global.24182
- __block_literal_global.24306
- __block_literal_global.244.19000
- __block_literal_global.245
- __block_literal_global.246.22753
- __block_literal_global.248
- __block_literal_global.248.22798
- __block_literal_global.249
- __block_literal_global.25102
- __block_literal_global.253
- __block_literal_global.2531
- __block_literal_global.26
- __block_literal_global.260
- __block_literal_global.262.19531
- __block_literal_global.26301
- __block_literal_global.264
- __block_literal_global.265
- __block_literal_global.26585
- __block_literal_global.267
- __block_literal_global.27.32739
- __block_literal_global.27195
- __block_literal_global.277
- __block_literal_global.278
- __block_literal_global.27879
- __block_literal_global.280
- __block_literal_global.280.13493
- __block_literal_global.28100
- __block_literal_global.28180
- __block_literal_global.287
- __block_literal_global.289
- __block_literal_global.28940
- __block_literal_global.29085
- __block_literal_global.292
- __block_literal_global.293.26948
- __block_literal_global.295
- __block_literal_global.295.26949
- __block_literal_global.298.10737
- __block_literal_global.29812
- __block_literal_global.29922
- __block_literal_global.3
- __block_literal_global.30.11371
- __block_literal_global.30.32978
- __block_literal_global.30.6251
- __block_literal_global.300.16397
- __block_literal_global.30236
- __block_literal_global.305
- __block_literal_global.305.13466
- __block_literal_global.30605
- __block_literal_global.307
- __block_literal_global.31
- __block_literal_global.31171
- __block_literal_global.314
- __block_literal_global.315
- __block_literal_global.31554
- __block_literal_global.31665
- __block_literal_global.317
- __block_literal_global.318
- __block_literal_global.32218
- __block_literal_global.326
- __block_literal_global.32735
- __block_literal_global.32895
- __block_literal_global.329
- __block_literal_global.32995
- __block_literal_global.33.27198
- __block_literal_global.33.34075
- __block_literal_global.33.38089
- __block_literal_global.33359
- __block_literal_global.33530
- __block_literal_global.33985
- __block_literal_global.34.32741
- __block_literal_global.341
- __block_literal_global.34104
- __block_literal_global.343
- __block_literal_global.3449
- __block_literal_global.345
- __block_literal_global.34817
- __block_literal_global.35
- __block_literal_global.35.32980
- __block_literal_global.350
- __block_literal_global.350.34479
- __block_literal_global.35379
- __block_literal_global.35429
- __block_literal_global.35541
- __block_literal_global.36.40949
- __block_literal_global.36095
- __block_literal_global.36141
- __block_literal_global.36318
- __block_literal_global.3639
- __block_literal_global.364
- __block_literal_global.365
- __block_literal_global.36706
- __block_literal_global.368
- __block_literal_global.37.34076
- __block_literal_global.37012
- __block_literal_global.372
- __block_literal_global.373
- __block_literal_global.37820
- __block_literal_global.379
- __block_literal_global.38
- __block_literal_global.38088
- __block_literal_global.382
- __block_literal_global.38236
- __block_literal_global.38334
- __block_literal_global.3845
- __block_literal_global.38489
- __block_literal_global.39.38090
- __block_literal_global.39.40950
- __block_literal_global.4
- __block_literal_global.4.37824
- __block_literal_global.40318
- __block_literal_global.40839
- __block_literal_global.40882
- __block_literal_global.41.36685
- __block_literal_global.4108
- __block_literal_global.41690
- __block_literal_global.42.38309
- __block_literal_global.42137
- __block_literal_global.422
- __block_literal_global.42297
- __block_literal_global.42489
- __block_literal_global.4278
- __block_literal_global.42945
- __block_literal_global.43.34072
- __block_literal_global.43.38068
- __block_literal_global.430
- __block_literal_global.433
- __block_literal_global.436
- __block_literal_global.437
- __block_literal_global.438
- __block_literal_global.44.10124
- __block_literal_global.44.24010
- __block_literal_global.441
- __block_literal_global.450
- __block_literal_global.452
- __block_literal_global.46.32959
- __block_literal_global.46.38080
- __block_literal_global.461
- __block_literal_global.462
- __block_literal_global.465
- __block_literal_global.4676
- __block_literal_global.473
- __block_literal_global.481
- __block_literal_global.482
- __block_literal_global.486
- __block_literal_global.4904
- __block_literal_global.491
- __block_literal_global.500
- __block_literal_global.501
- __block_literal_global.502
- __block_literal_global.5225
- __block_literal_global.5285
- __block_literal_global.536
- __block_literal_global.54
- __block_literal_global.546
- __block_literal_global.554
- __block_literal_global.56
- __block_literal_global.56.31516
- __block_literal_global.56.35349
- __block_literal_global.564
- __block_literal_global.57
- __block_literal_global.571
- __block_literal_global.58.24189
- __block_literal_global.58.31513
- __block_literal_global.5804
- __block_literal_global.6
- __block_literal_global.6.24044
- __block_literal_global.609
- __block_literal_global.61.38069
- __block_literal_global.612
- __block_literal_global.623
- __block_literal_global.625
- __block_literal_global.628
- __block_literal_global.6280
- __block_literal_global.6338
- __block_literal_global.638
- __block_literal_global.64.38070
- __block_literal_global.652
- __block_literal_global.654
- __block_literal_global.662
- __block_literal_global.6624
- __block_literal_global.666
- __block_literal_global.67.38071
- __block_literal_global.675
- __block_literal_global.677
- __block_literal_global.6774
- __block_literal_global.68
- __block_literal_global.68.20888
- __block_literal_global.68.29087
- __block_literal_global.682
- __block_literal_global.6840
- __block_literal_global.69
- __block_literal_global.7.34106
- __block_literal_global.7.37799
- __block_literal_global.70.37072
- __block_literal_global.710
- __block_literal_global.716
- __block_literal_global.72.29089
- __block_literal_global.7362
- __block_literal_global.738
- __block_literal_global.7541
- __block_literal_global.759
- __block_literal_global.764
- __block_literal_global.78.22794
- __block_literal_global.783
- __block_literal_global.784
- __block_literal_global.785
- __block_literal_global.787
- __block_literal_global.7874
- __block_literal_global.789
- __block_literal_global.79.23433
- __block_literal_global.791
- __block_literal_global.8
- __block_literal_global.8.21730
- __block_literal_global.81
- __block_literal_global.838
- __block_literal_global.84.30171
- __block_literal_global.84.37061
- __block_literal_global.85.38269
- __block_literal_global.8566
- __block_literal_global.857
- __block_literal_global.859
- __block_literal_global.86
- __block_literal_global.88.34755
- __block_literal_global.880
- __block_literal_global.882
- __block_literal_global.89
- __block_literal_global.890
- __block_literal_global.895
- __block_literal_global.9
- __block_literal_global.9034
- __block_literal_global.904
- __block_literal_global.91.14752
- __block_literal_global.91.17498
- __block_literal_global.91.26255
- __block_literal_global.91.30688
- __block_literal_global.918
- __block_literal_global.919
- __block_literal_global.92.32637
- __block_literal_global.926
- __block_literal_global.929
- __block_literal_global.931
- __block_literal_global.9310
- __block_literal_global.9367
- __block_literal_global.948
- __block_literal_global.9492
- __block_literal_global.956
- __block_literal_global.96.17499
- __block_literal_global.9660
- __block_literal_global.968
- __block_literal_global.99
- __block_literal_global.992
- __finishSuggestionsSetup_block_invoke.40
- __finishSuggestionsSetup_block_invoke.41
- __patterns_block_invoke.16945
- __patterns_block_invoke.22767
- __patterns_block_invoke.23824
- __patterns_block_invoke.25106
- __patterns_block_invoke.9496
- __writeIdentity_block_invoke.463
- __writeIdentity_block_invoke_2.467
- _addEKEventToCalendar:storageEvent:ekStore:commit:._pasOnceToken37
- _block_invoke._pasExprOnceResult
- _block_invoke._pasExprOnceResult.15022
- _block_invoke._pasOnceToken3
- _block_invoke._pasOnceToken7
- _block_invoke.onceToken
- _block_invoke.version
- _fmod
- _fmodf
- _objc_msgSend$_accessSummarizationPipelineForBundleId:block:
- _objc_msgSend$author:
- _objc_msgSend$handleDeletionOfItemsWithIdentifiers:bundleIdentifier:
- _objc_msgSend$isAuthorTag
- _objc_msgSend$mlExtractionEnabledForTextMessage:
- _objc_msgSend$sharedPipelineWithContactStore:incomingBundleId:
- _objc_msgSend$shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:
- _processReservationInteractions:bundleId:completion:._pasOnceToken158
- _serialQueueForTitleGeneration._pasOnceToken198
- addInteractions:bundleId:completion:._pasOnceToken148
- analyzeForFollowUpMailWithBody:isSent:messageId:date:._pasExprOnceResult.88
- asDictionary.onceToken.30604
- asDictionary.sharedKeySet.30607
- audit_stringProactiveSummarization.32699
- bumptTTLForNLEvent:._pasOnceToken53
- charactersSAX.36093
- consumeInteractionWithContext:._pasOnceToken242
- dateFromEmailString:._pasExprOnceResult.134
- eventClassificationWithoutXPCForMailMessage:._pasOnceToken99
- identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:language:store:disableConservativeCheckRequirement:._pasExprOnceResult.9
- isLowercaseAscii.16973
- jsonLdOutputFromPackedJSEntity:._pasOnceToken101
- logEventInteractionForEventWithExternalIdentifier:interface:actionType:._pasOnceToken185
- logEventInteractionForEventWithUniqueKey:interface:actionType:._pasOnceToken193
- patterns.16938
- patterns.22715
- patterns.23805
- patterns.25097
- patterns.9476
- patterns.onceToken.16942
- patterns.onceToken.22764
- patterns.onceToken.23819
- patterns.onceToken.24845
- patterns.onceToken.25101
- patterns.onceToken.9491
- patterns.patterns.16943
- patterns.patterns.22765
- patterns.patterns.23821
- patterns.patterns.24846
- patterns.patterns.25103
- patterns.patterns.9493
- resolveCandidatesWithoutXPC:forCategory:label:rawIndexSet:taggedCharacterRanges:._pasOnceToken100
- reverseMapMailMessage:withPreprocessedHTML:forCategory:withSchemExpectation:._pasOnceToken102
- sg_decodeEncodedWords._pasExprOnceResult.12
- sharedInstance.27882
- sharedInstance._pasExprOnceResult.11731
- sharedInstance._pasExprOnceResult.12709
- sharedInstance._pasExprOnceResult.13018
- sharedInstance._pasExprOnceResult.14087
- sharedInstance._pasExprOnceResult.15129
- sharedInstance._pasExprOnceResult.16058
- sharedInstance._pasExprOnceResult.21566
- sharedInstance._pasExprOnceResult.2175
- sharedInstance._pasExprOnceResult.23968
- sharedInstance._pasExprOnceResult.28181
- sharedInstance._pasExprOnceResult.31666
- sharedInstance._pasExprOnceResult.32896
- sharedInstance._pasExprOnceResult.33360
- sharedInstance._pasExprOnceResult.36225
- sharedInstance._pasExprOnceResult.36319
- sharedInstance._pasExprOnceResult.37821
- sharedInstance._pasExprOnceResult.40840
- sharedInstance._pasExprOnceResult.4677
- sharedInstance._pasExprOnceResult.6420
- sharedInstance._pasExprOnceResult.6775
- sharedInstance._pasExprOnceResult.88
- sharedInstance._pasOnceToken2.11729
- sharedInstance._pasOnceToken2.12707
- sharedInstance._pasOnceToken2.13016
- sharedInstance._pasOnceToken2.14085
- sharedInstance._pasOnceToken2.15127
- sharedInstance._pasOnceToken2.23966
- sharedInstance._pasOnceToken2.28179
- sharedInstance._pasOnceToken2.36224
- sharedInstance._pasOnceToken2.40838
- sharedInstance._pasOnceToken2.4675
- sharedInstance._pasOnceToken2.6419
- sharedInstance._pasOnceToken2.6773
- sharedInstance._pasOnceToken3.21564
- sharedInstance._pasOnceToken3.31664
- sharedInstance._pasOnceToken3.32894
- sharedInstance._pasOnceToken3.33358
- sharedInstance._pasOnceToken3.36317
- sharedInstance._pasOnceToken9.37819
- titleSuggestionForMessage:withCompletion:._pasOnceToken200
CStrings:
+ "%@: cascade entity item not supported for event type: %@"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_nfa.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_prefilter.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_regexp.h"
+ "@\"PSUSummarizationPipeline\""
+ "@44@0:8@16B24B28B32B36B40"
+ "@48@0:8@16B24B28B32B36B40B44"
+ "@72@0:8@16@24@32@40B48B52B56B60B64B68"
+ "DetailedEventStatus"
+ "Error constructing cascade entity item for event type %@: %@"
+ "SGCascadeWritebackAdapter"
+ "SGEKCalendarAdapter addEvent: New event not eligible for donation."
+ "SGEKCalendarAdapter addEvent: Skipping event extraction since it's an LLM extraction is not preferrable."
+ "SGEKCalendarAdapter: Checking eligibility of %@ event for calendar donation"
+ "SGEKCalendarAdapter: Checking eligibility of structured event donation to Calendar"
+ "SGEKCalendarAdapter: Event not belonging to structured event categories. Early returning as an eligible event."
+ "SGEKCalendarAdapter: Event reservationID present: %@"
+ "SGEKCalendarAdapter: Found nil structured category for tag: %@"
+ "SGEKCalendarAdapter: New event eligible for donation - %@"
+ "SGEkCalendarAdapter addEvent: Skipping donation of event from text message with unsupported category/status."
+ "SGEntityTagsHelper"
+ "SGEventDonationEnablementManager"
+ "SGEventDonationEnablementManager: %@ status not supported for text messages."
+ "SGEventDonationEnablementManager: Category not supported for text messages."
+ "SGExtractionDissector: LLM extraction was empty, falling back to Regex."
+ "SGExtractionDissector: No LLM extraction exception, but empty extraction count."
+ "SGExtractionDissector: Preferring Regex output over LLM."
+ "SGTicketedTransportationEventSchemaCreator: unidentified category of ticketed transportation - %@"
+ "Skipping extraction from LLM since it's not preferred in this locale."
+ "Skipping text message extraction since the category/status was unsupported."
+ "T@\"NSNumber\",R,GmailCategories,V_mailCategories"
+ "T@\"NSSet\",&,N,V_llmPreferredLocales"
+ "T@\"NSSet\",&,N,V_overallUnsupportedCategories"
+ "T@\"NSSet\",&,N,V_overallUnsupportedStatuses"
+ "T@\"NSSet\",&,N,V_textMessageUnsupportedCategories"
+ "T@\"NSSet\",&,N,V_textMessageUnsupportedStatuses"
+ "^(?i)(fw|fwd|forward)\\s*:\\s*"
+ "_appointmentEntityItemFromAttributeSet:error:"
+ "_cascadeEntityItemsFromEvents:"
+ "_completeRegexExtractionforMail:entity:forMail:"
+ "_flightEntityItemFromAttributeSet:error:"
+ "_hotelEntityItemFromAttributeSet:error:"
+ "_isMailCategoryUnsupportedForLLMExtraction:"
+ "_isStructuredEventEligibleForDonation:"
+ "_llmPreferredLocales"
+ "_loggingIdentifiersFromEvents:"
+ "_mailCategories"
+ "_newEventEligibleForDonation:"
+ "_overallUnsupportedCategories"
+ "_overallUnsupportedStatuses"
+ "_partyEntityItemFromAttributeSet:error:"
+ "_rentalCarEntityItemFromAttributeSet:error:"
+ "_restaurantEntityItemFromAttributeSet:error:"
+ "_shouldProcessMailMessage:havingSignificantSender:"
+ "_subjectResemblesForwardedMailSubjectForMail:"
+ "_summarizationPipeline"
+ "_textMessageUnsupportedCategories"
+ "_textMessageUnsupportedStatuses"
+ "_ticketedShowEntityItemFromAttributeSet:error:"
+ "_ticketedTransportationEntityItemFromAttributeSet:error:"
+ "_transportationSchemaCreatorFromTransportType:"
+ "addEvent:%{sensitive}@ bailing because event is not valid for spotlight donation"
+ "addEvents:[SGEvent ids: %@] bailing because events do not contain a cascade set version."
+ "addEvents:[SGEvent ids: %@] bailing because events do not contain eligible cascade items."
+ "addEvents:[SGEvent ids: %@] cascade donation failed to add or update item with id: %@ error: %@"
+ "addEvents:[SGEvent ids: %@] cascade donation failed to register item with id: %@ error: %@"
+ "addEvents:[SGEvent ids: %@] cascade donation failed with error %@"
+ "addEvents:[SGEvent ids: %@] failed to finish cascade donation with error: %@"
+ "addEvents:[SGEvent ids: %@] fallback to a full set donation of cascade items."
+ "addEvents:[SGEvent ids: %@] finished donating version: %llu"
+ "addOrUpdateItem:error:"
+ "cascadeEntityItemForEvent"
+ "cascadeEntitySetVersion:"
+ "costCode"
+ "deleteItemsWithIdentifiers:bundleId:"
+ "en_AU"
+ "en_CA"
+ "en_CN"
+ "en_GB"
+ "en_IN"
+ "en_JP"
+ "en_NZ"
+ "en_SG"
+ "en_ZA"
+ "endDateTimeZone"
+ "eventCustomerNames"
+ "eventEndLocationAddress"
+ "eventEndLocationName"
+ "eventEndLocationTelephone"
+ "eventExtractedFromLLM"
+ "eventNumberOfRooms"
+ "eventProvider"
+ "eventReservationForName"
+ "eventReservationID"
+ "eventRoomNumbers"
+ "eventSeatNumbers"
+ "eventSourceMetadata"
+ "eventStartLocationAddress"
+ "eventStartLocationName"
+ "eventStartLocationTelephone"
+ "eventStatus"
+ "eventTicketType"
+ "eventTotalCost"
+ "eventType"
+ "eventURL"
+ "extractSchemasFromEntityTags:"
+ "filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:"
+ "filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:"
+ "filterPseudoEvents:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealTime:"
+ "finish:"
+ "flightArrivalAirportAddress"
+ "flightArrivalAirportAddressSynonyms"
+ "flightArrivalAirportCode"
+ "flightArrivalAirportCountry"
+ "flightArrivalAirportLocality"
+ "flightArrivalAirportName"
+ "flightArrivalAirportPostalCode"
+ "flightArrivalAirportRegion"
+ "flightArrivalAirportStreetAddress"
+ "flightArrivalDateTime"
+ "flightArrivalGate"
+ "flightArrivalTerminal"
+ "flightArrivalTimeZone"
+ "flightBoardingDateTime"
+ "flightCarrier"
+ "flightCheckInUrl"
+ "flightConfirmationNumber"
+ "flightDepartureAirportAddress"
+ "flightDepartureAirportAddressSynonyms"
+ "flightDepartureAirportCode"
+ "flightDepartureAirportCountry"
+ "flightDepartureAirportLocality"
+ "flightDepartureAirportName"
+ "flightDepartureAirportPostalCode"
+ "flightDepartureAirportRegion"
+ "flightDepartureAirportStreetAddress"
+ "flightDepartureDateTime"
+ "flightDepartureGate"
+ "flightDepartureTerminal"
+ "flightDepartureTimeZone"
+ "hotelCheckinDate"
+ "hotelCheckinTime"
+ "hotelCheckoutDate"
+ "hotelCheckoutTime"
+ "hotelProvider"
+ "hotelReservationForAddress"
+ "hotelReservationForName"
+ "hotelReservationForStreetAddress"
+ "hotelReservationForTelephone"
+ "hotelReservationId"
+ "hotelTimeZone"
+ "hotelUnderName"
+ "incrementalSetDonationWithItemType:descriptors:version:validity:completion:"
+ "initWithContactStore:"
+ "initWithContent:metaContent:error:"
+ "initWithCustomerNames:eventName:startLocationName:startLocationAddress:startDate:startDateTimeZone:seatNumbers:endLocationName:endLocationAddress:endDate:endDateTimeZone:duration:eventSubType:error:"
+ "initWithEntity:entityType:error:"
+ "initWithEventName:startLocationName:startAddress:startDate:startDateTimeZone:endDate:endDateTimeZone:link:eventSubType:error:"
+ "initWithEventName:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:endDate:endDateTimeZone:duration:cost:costCode:eventSubType:error:"
+ "initWithFlightDesignator:flightConfirmationNumber:flightCarrier:flightCarrierCode:provider:customerNames:flightDepartureDateTime:flightDepartureTimeZone:flightBoardingDateTime:flightDepartureAirportCode:flightDepartureAirportName:flightDepartureAirportAddress:flightDepartureAirportLocality:flightDepartureAirportRegion:flightDepartureAirportPostalCode:flightDepartureAirportCountry:flightDepartureTerminal:flightDepartureGate:seatNumbers:flightArrivalDateTime:flightArrivalTimeZone:flightArrivalAirportCode:flightArrivalAirportName:flightArrivalAirportAddress:flightArrivalAirportLocality:flightArrivalAirportRegion:flightArrivalAirportPostalCode:flightArrivalAirportCountry:flightArrivalTerminal:flightArrivalGate:duration:flightCheckInUrl:cost:costCurrencyCode:flightNumber:eventStatus:error:"
+ "initWithHotelReservationForName:provider:hotelReservationId:customerNames:roomNumbers:numberOfRooms:hotelReservationForAddress:hotelCheckinDate:hotelCheckinTime:hotelCheckoutDate:hotelCheckoutTime:hotelTimeZone:duration:hotelReservationForTelephone:cost:costCode:eventStatus:error:"
+ "initWithLLMPreferredLocales:"
+ "initWithProvider:reservationID:customerNames:restaurantPartySize:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:restaurantMealType:eventStatus:error:"
+ "initWithReservationID:eventName:provider:customerNames:startLocationName:startLocationAddress:seatNumbers:startDate:startDateTimeZone:endDate:endDateTimeZone:duration:ticketType:link:cost:costCode:eventSubType:error:"
+ "initWithReservationID:eventName:provider:customerNames:startLocationName:startLocationAddress:startLocationTelephone:startDate:startDateTimeZone:endLocationName:endLocationAddress:endLocationTelephone:endDate:endDateTimeZone:reservationForName:duration:cost:costCode:eventStatus:error:"
+ "initWithSourceItemIdentifier:error:"
+ "isCascadeEntitySetVersion"
+ "isLLMPreferredForLocale"
+ "isLLMPreferredForLocale:"
+ "isMessageCandidateForExtraction:"
+ "isTimePresentInDURawDateTime:"
+ "isUnsupportedEventCategoryStatusForTextMessage:"
+ "isValidEventForSpotlightDonation:"
+ "kEntitySetCascadeDonationVersion"
+ "llmPreferredLocales"
+ "mailCategories"
+ "metaContent"
+ "mlExtractionEnabledForTextMessage"
+ "overallUnsupportedCategories"
+ "overallUnsupportedStatuses"
+ "processItem:receivedDate:positionInReceivedItems:"
+ "public.voice-audio"
+ "registerItem:error:"
+ "reservationIDPresentInEventSchema:"
+ "restaurantMealType"
+ "restaurantPartySize"
+ "schemasInEntityTagsBelongsToPendingConfirmationEvent:"
+ "searchableItemsDidUpdate:"
+ "searchableItemsForIdentifiers:searchableItemsHandler:"
+ "setEventStatus:"
+ "setEventUpdateStatus:"
+ "setFlightArrivalAirportAddressSynonyms:"
+ "setFlightDepartureAirportAddressSynonyms:"
+ "setLlmPreferredLocales:"
+ "setOverallUnsupportedCategories:"
+ "setOverallUnsupportedStatuses:"
+ "setTextMessageUnsupportedCategories:"
+ "setTextMessageUnsupportedStatuses:"
+ "setTimeIsUnknown:"
+ "shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:keepPendingConfirmationEvents:keepUnsupportedEventCategoryStatusForTextMessage:keepLLMExtractionForRealtime:"
+ "sourceItemIdentifier"
+ "startDateTimeZone"
+ "startTimeIsUnknown"
+ "synonymAirportNamesForAirportCode:"
+ "textMessageUnsupportedCategories"
+ "textMessageUnsupportedStatuses"
+ "update"
+ "v1.0"
+ "v24@?0@\"CCSetDonation\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_nfa.cc"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_prefilter.h"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/Suggestions/re2/re2/re2_regexp.h"
- "@60@0:8@16@24@32@40B48B52B56"
- "CatchUp"
- "Event not complete. Not donating events to events bundle."
- "PrecomputeSmartReplies"
- "PrecomputeSmartRepliesMail"
- "_accessSummarizationPipelineForBundleId:block:"
- "author:"
- "handleDeletionOfItemsWithIdentifiers:bundleIdentifier:"
- "isAuthorTag"
- "mlExtractionEnabledForTextMessage:"
- "sharedPipelineWithContactStore:incomingBundleId:"
- "shortNamesAndRealtimeEventsFromEntity:message:enrichments:store:keepPastEvents:keepPartialEvents:keepEventsFromOldDocuments:"
- "unidentified category of ticketed transportation - %@"
- "v16@?0@\"PSUSummarizationPipeline\"8"

```
