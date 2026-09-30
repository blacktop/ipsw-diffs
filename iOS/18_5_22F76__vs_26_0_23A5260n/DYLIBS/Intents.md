## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-3604.0.0.0.0
-  __TEXT.__text: 0x43cc7c
+4009.1.0.0.0
+  __TEXT.__text: 0x450644
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x78b04
-  __TEXT.__const: 0x1e10
+  __TEXT.__objc_methlist: 0x78ba4
+  __TEXT.__const: 0x1e40
   __TEXT.__dlopen_cstrs: 0xce9
-  __TEXT.__gcc_except_tab: 0x2230
-  __TEXT.__oslogstring: 0x57cc
-  __TEXT.__cstring: 0x47431
+  __TEXT.__gcc_except_tab: 0x2260
+  __TEXT.__oslogstring: 0x580d
+  __TEXT.__cstring: 0x474ca
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x10d50
+  __TEXT.__unwind_info: 0x10c40
   __TEXT.__objc_classname: 0x12221
-  __TEXT.__objc_methname: 0x69bfc
-  __TEXT.__objc_methtype: 0xcd53
-  __TEXT.__objc_stubs: 0x33aa0
-  __DATA_CONST.__got: 0x28c0
-  __DATA_CONST.__const: 0xb8f0
+  __TEXT.__objc_methname: 0x69e28
+  __TEXT.__objc_methtype: 0xcc5e
+  __TEXT.__objc_stubs: 0x33ba0
+  __DATA_CONST.__got: 0x28a0
+  __DATA_CONST.__const: 0xb910
   __DATA_CONST.__objc_classlist: 0x2930
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1940
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x153d0
+  __DATA_CONST.__objc_selrefs: 0x15420
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1398
   __DATA_CONST.__objc_arraydata: 0xc298
   __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x1780
-  __AUTH_CONST.__cfstring: 0x42520
-  __AUTH_CONST.__objc_const: 0xb4c40
+  __AUTH_CONST.__cfstring: 0x425e0
+  __AUTH_CONST.__objc_const: 0xb4ce8
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x4cf8
   __AUTH_CONST.__objc_dictobj: 0x3a48
-  __AUTH.__objc_data: 0x14488
-  __DATA.__objc_ivar: 0x3d40
+  __AUTH.__objc_data: 0x14500
+  __DATA.__objc_ivar: 0x3d48
   __DATA.__data: 0x12f98
   __DATA.__bss: 0xc50
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5758
+  __DATA_DIRTY.__objc_data: 0x56e0
   __DATA_DIRTY.__bss: 0x278
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAE77FAC-3B14-3CCD-A949-97A28C22B930
-  Functions: 30607
-  Symbols:   87172
-  CStrings:  37150
+  UUID: 5B74B771-F826-31BA-B782-8AD935D2334E
+  Functions: 30619
+  Symbols:   87205
+  CStrings:  37177
 
Symbols:
+ +[INIntentCodableDescription(__Name) __NameKey].37613
+ -[INAppIntent(Summary) _hasTitle]
+ -[INAppIntent(Summary) _subtitleForLanguage:]
+ -[INAppIntent(Summary) _subtitleWithLocalizer:fromBundleURL:]
+ -[INAppIntent(Summary) _titleForLanguage:]
+ -[INAppIntent(Summary) _titleWithLocalizer:fromBundleURL:]
+ -[INMessage initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:translatedToLanguage:]
+ -[INMessage setTranslatedToLanguage:]
+ -[INMessage translatedToLanguage]
+ -[_INPBMessage hasTranslatedToLanguage]
+ -[_INPBMessage setTranslatedToLanguage:]
+ -[_INPBMessage translatedToLanguage]
+ GCC_except_table10125
+ GCC_except_table10135
+ GCC_except_table10137
+ GCC_except_table10142
+ GCC_except_table10207
+ GCC_except_table10213
+ GCC_except_table10766
+ GCC_except_table10891
+ GCC_except_table10895
+ GCC_except_table11008
+ GCC_except_table11121
+ GCC_except_table11148
+ GCC_except_table11149
+ GCC_except_table11371
+ GCC_except_table11813
+ GCC_except_table12103
+ GCC_except_table12546
+ GCC_except_table12553
+ GCC_except_table12556
+ GCC_except_table12564
+ GCC_except_table12585
+ GCC_except_table13190
+ GCC_except_table13721
+ GCC_except_table13760
+ GCC_except_table13764
+ GCC_except_table14009
+ GCC_except_table14536
+ GCC_except_table15214
+ GCC_except_table15218
+ GCC_except_table16355
+ GCC_except_table16458
+ GCC_except_table16466
+ GCC_except_table16467
+ GCC_except_table16769
+ GCC_except_table18415
+ GCC_except_table19070
+ GCC_except_table19240
+ GCC_except_table19267
+ GCC_except_table19832
+ GCC_except_table19834
+ GCC_except_table19837
+ GCC_except_table19915
+ GCC_except_table20915
+ GCC_except_table21010
+ GCC_except_table21231
+ GCC_except_table22299
+ GCC_except_table22302
+ GCC_except_table22305
+ GCC_except_table22920
+ GCC_except_table22937
+ GCC_except_table23653
+ GCC_except_table25127
+ GCC_except_table25139
+ GCC_except_table27010
+ GCC_except_table27013
+ GCC_except_table27014
+ GCC_except_table27015
+ GCC_except_table27016
+ GCC_except_table2793
+ GCC_except_table2794
+ GCC_except_table28708
+ GCC_except_table28713
+ GCC_except_table28715
+ GCC_except_table28723
+ GCC_except_table28725
+ GCC_except_table28734
+ GCC_except_table2876
+ GCC_except_table2912
+ GCC_except_table29790
+ GCC_except_table29797
+ GCC_except_table29800
+ GCC_except_table29803
+ GCC_except_table29805
+ GCC_except_table29806
+ GCC_except_table29807
+ GCC_except_table29808
+ GCC_except_table29810
+ GCC_except_table29999
+ GCC_except_table3167
+ GCC_except_table3175
+ GCC_except_table3188
+ GCC_except_table4166
+ GCC_except_table4170
+ GCC_except_table4177
+ GCC_except_table4179
+ GCC_except_table4192
+ GCC_except_table4405
+ GCC_except_table5379
+ GCC_except_table5380
+ GCC_except_table5437
+ GCC_except_table5597
+ GCC_except_table5604
+ GCC_except_table5606
+ GCC_except_table5843
+ GCC_except_table5852
+ GCC_except_table6400
+ GCC_except_table6402
+ GCC_except_table6434
+ GCC_except_table6435
+ GCC_except_table6436
+ GCC_except_table6437
+ GCC_except_table6471
+ GCC_except_table7032
+ GCC_except_table7117
+ GCC_except_table7118
+ GCC_except_table7839
+ GCC_except_table8105
+ GCC_except_table8450
+ GCC_except_table8454
+ GCC_except_table8702
+ GCC_except_table8704
+ GCC_except_table9381
+ GCC_except_table9937
+ _AssistantServicesLibraryCore.frameworkLibrary.54943
+ _ChronoServicesLibraryCore.frameworkLibrary.123622
+ _ContactsLibrary.19422
+ _ContactsLibrary.33518
+ _ContactsLibrary.45494
+ _ContactsLibrary.60881
+ _ContactsLibraryCore.frameworkLibrary.111061
+ _ContactsLibraryCore.frameworkLibrary.19410
+ _ContactsLibraryCore.frameworkLibrary.19436
+ _ContactsLibraryCore.frameworkLibrary.33523
+ _ContactsLibraryCore.frameworkLibrary.45497
+ _ContactsLibraryCore.frameworkLibrary.60884
+ _CoreGraphicsLibrary.136659
+ _CoreGraphicsLibraryCore.frameworkLibrary.136664
+ _CoreSpotlightLibrary.19403
+ _CoreSpotlightLibraryCore.frameworkLibrary.19406
+ _CoreSpotlightLibraryCore.frameworkLibrary.59714
+ _CoreSpotlightLibraryCore.frameworkLibrary.79776
+ _HealthKitLibraryCore.frameworkLibrary.95481
+ _IntentsUILibraryCore.frameworkLibrary.83647
+ _LinkServicesLibraryCore.frameworkLibrary.165970
+ _OBJC_IVAR_$_INMessage._translatedToLanguage
+ _OBJC_IVAR_$__INPBMessage._translatedToLanguage
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.112997
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.123545
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.27955
+ __INMessageReactionTypeCustomAcknowledgement
+ __INSendMessageRecipientUnsupportedReasonBlocked
+ __OBJC_$_INSTANCE_METHODS_INAppIntent(Summary)
+ __OBJC_$_PROP_LIST__INPBMessage.434
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZnwmSt19__type_descriptor_t
+ ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke.30
+ ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke.31
+ ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke_2.33
+ ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke_4
+ ___AssistantServicesLibraryCore_block_invoke.54944
+ ___Block_byref_object_copy_.100523
+ ___Block_byref_object_copy_.104485
+ ___Block_byref_object_copy_.11851
+ ___Block_byref_object_copy_.13081
+ ___Block_byref_object_copy_.20858
+ ___Block_byref_object_copy_.26717
+ ___Block_byref_object_copy_.26996
+ ___Block_byref_object_copy_.29650
+ ___Block_byref_object_copy_.37073
+ ___Block_byref_object_copy_.49913
+ ___Block_byref_object_copy_.54532
+ ___Block_byref_object_copy_.54953
+ ___Block_byref_object_copy_.65241
+ ___Block_byref_object_copy_.68255
+ ___Block_byref_object_copy_.69064
+ ___Block_byref_object_copy_.71925
+ ___Block_byref_object_copy_.75139
+ ___Block_byref_object_copy_.90449
+ ___Block_byref_object_dispose_.100524
+ ___Block_byref_object_dispose_.104486
+ ___Block_byref_object_dispose_.11852
+ ___Block_byref_object_dispose_.13082
+ ___Block_byref_object_dispose_.20859
+ ___Block_byref_object_dispose_.26718
+ ___Block_byref_object_dispose_.26997
+ ___Block_byref_object_dispose_.29651
+ ___Block_byref_object_dispose_.37074
+ ___Block_byref_object_dispose_.49914
+ ___Block_byref_object_dispose_.54533
+ ___Block_byref_object_dispose_.54954
+ ___Block_byref_object_dispose_.65242
+ ___Block_byref_object_dispose_.68256
+ ___Block_byref_object_dispose_.69065
+ ___Block_byref_object_dispose_.71926
+ ___Block_byref_object_dispose_.75140
+ ___Block_byref_object_dispose_.90450
+ ___ChronoServicesLibraryCore_block_invoke.123623
+ ___ContactsLibraryCore_block_invoke.111062
+ ___ContactsLibraryCore_block_invoke.19411
+ ___ContactsLibraryCore_block_invoke.19437
+ ___ContactsLibraryCore_block_invoke.33524
+ ___ContactsLibraryCore_block_invoke.45498
+ ___ContactsLibraryCore_block_invoke.60885
+ ___CoreGraphicsLibraryCore_block_invoke.136665
+ ___CoreSpotlightLibraryCore_block_invoke.19407
+ ___CoreSpotlightLibraryCore_block_invoke.59715
+ ___CoreSpotlightLibraryCore_block_invoke.79777
+ ___HealthKitLibraryCore_block_invoke.95482
+ ___IntentsUILibraryCore_block_invoke.83648
+ ___LinkServicesLibraryCore_block_invoke.165971
+ ___VoiceShortcutClientLibraryCore_block_invoke.112998
+ ___VoiceShortcutClientLibraryCore_block_invoke.123546
+ ___VoiceShortcutClientLibraryCore_block_invoke.27956
+ ___block_literal_global.10.103451
+ ___block_literal_global.10.54968
+ ___block_literal_global.100.75134
+ ___block_literal_global.100269
+ ___block_literal_global.100445
+ ___block_literal_global.103441
+ ___block_literal_global.104586
+ ___block_literal_global.105602
+ ___block_literal_global.11.111705
+ ___block_literal_global.111733
+ ___block_literal_global.11952
+ ___block_literal_global.119829
+ ___block_literal_global.12.158244
+ ___block_literal_global.123645
+ ___block_literal_global.13.103453
+ ___block_literal_global.13.98758
+ ___block_literal_global.13077
+ ___block_literal_global.158232
+ ___block_literal_global.17680
+ ___block_literal_global.18385
+ ___block_literal_global.20854
+ ___block_literal_global.21.59681
+ ___block_literal_global.22422
+ ___block_literal_global.23235
+ ___block_literal_global.26709
+ ___block_literal_global.29077
+ ___block_literal_global.29672
+ ___block_literal_global.3.111704
+ ___block_literal_global.31043
+ ___block_literal_global.31211
+ ___block_literal_global.31775
+ ___block_literal_global.34331
+ ___block_literal_global.37095
+ ___block_literal_global.37485
+ ___block_literal_global.40166
+ ___block_literal_global.40670
+ ___block_literal_global.42336
+ ___block_literal_global.43254
+ ___block_literal_global.43505
+ ___block_literal_global.44412
+ ___block_literal_global.47515
+ ___block_literal_global.5.94136
+ ___block_literal_global.53411
+ ___block_literal_global.53983
+ ___block_literal_global.54538
+ ___block_literal_global.54952
+ ___block_literal_global.59721
+ ___block_literal_global.6.111716
+ ___block_literal_global.6.72041
+ ___block_literal_global.60742
+ ___block_literal_global.62270
+ ___block_literal_global.66717
+ ___block_literal_global.68330
+ ___block_literal_global.68447
+ ___block_literal_global.69066
+ ___block_literal_global.70469
+ ___block_literal_global.71231
+ ___block_literal_global.71975
+ ___block_literal_global.72037
+ ___block_literal_global.74997
+ ___block_literal_global.77364
+ ___block_literal_global.82.66711
+ ___block_literal_global.82371
+ ___block_literal_global.91.71976
+ ___block_literal_global.91417
+ ___block_literal_global.92276
+ ___block_literal_global.94160
+ ___block_literal_global.98769
+ ___getAFPreferencesClass_block_invoke.54942
+ ___getCGColorCreateSRGBSymbolLoc_block_invoke.136710
+ ___getCGColorGetComponentsSymbolLoc_block_invoke.136658
+ ___getCNContactEmailAddressesKeySymbolLoc_block_invoke.33528
+ ___getCNContactPhoneNumbersKeySymbolLoc_block_invoke.33531
+ ___getCNLabeledValueClass_block_invoke.60901
+ ___getCNPostalAddressClass_block_invoke.111060
+ ___getCSSearchableIndexClass_block_invoke.59713
+ ___getCSSearchableItemAttributeSetClass_block_invoke.79775
+ ___getHKUnitClass_block_invoke.95480
+ _audit_stringAssistantServices.54949
+ _audit_stringChronoServices.123628
+ _audit_stringContacts.111067
+ _audit_stringContacts.19413
+ _audit_stringContacts.19439
+ _audit_stringContacts.33526
+ _audit_stringContacts.45500
+ _audit_stringContacts.60888
+ _audit_stringCoreGraphics.136667
+ _audit_stringCoreSpotlight.19408
+ _audit_stringCoreSpotlight.59720
+ _audit_stringCoreSpotlight.79782
+ _audit_stringHealthKit.95487
+ _audit_stringLinkServices.165976
+ _audit_stringVoiceShortcutClient.113003
+ _audit_stringVoiceShortcutClient.123551
+ _audit_stringVoiceShortcutClient.27957
+ _getAFPreferencesClass.softClass.54941
+ _getCGColorCreateSRGBSymbolLoc.ptr.136709
+ _getCGColorGetComponentsSymbolLoc.ptr.136657
+ _getCNContactEmailAddressesKeySymbolLoc.ptr.33527
+ _getCNContactPhoneNumbersKeySymbolLoc.ptr.33530
+ _getCNLabeledValueClass.60866
+ _getCNLabeledValueClass.softClass.60900
+ _getCNPostalAddressClass.softClass.111059
+ _getCSSearchableIndexClass.softClass.59712
+ _getCSSearchableItemAttributeSetClass.softClass.79774
+ _getHKUnitClass.95478
+ _getHKUnitClass.softClass.95479
+ _getUISIntentForwardingActionClass
+ _intentDescription.intentDescription.31776
+ _intentDescription.intentDescription.39161
+ _intentDescription.intentDescription.42684
+ _intentDescription.intentDescription.64206
+ _intentDescription.intentDescription.68448
+ _intentDescription.onceToken.31774
+ _intentDescription.onceToken.39160
+ _intentDescription.onceToken.42683
+ _intentDescription.onceToken.64205
+ _intentDescription.onceToken.68446
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:translatedToLanguage:
+ _objc_msgSend$initWithIntentForwardingAction:responseQueue:responseHandler:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setTranslatedToLanguage:
+ _objc_msgSend$translatedToLanguage
+ _serviceIdentifier.onceToken.83621
+ _serviceIdentifier.sServiceIdentifier.83622
+ _sharedCache.onceToken.82370
+ _sharedManager.onceToken.123644
+ _sharedManager.onceToken.59711
+ _sharedManager.sharedManager.123646
+ _sharedProvider.onceToken.158243
- +[INIntentCodableDescription(__Name) __NameKey].37465
- GCC_except_table10112
- GCC_except_table10122
- GCC_except_table10124
- GCC_except_table10129
- GCC_except_table10194
- GCC_except_table10200
- GCC_except_table10753
- GCC_except_table10878
- GCC_except_table10882
- GCC_except_table10995
- GCC_except_table11108
- GCC_except_table11135
- GCC_except_table11136
- GCC_except_table11358
- GCC_except_table11800
- GCC_except_table12090
- GCC_except_table12533
- GCC_except_table12540
- GCC_except_table12543
- GCC_except_table12551
- GCC_except_table12572
- GCC_except_table13177
- GCC_except_table13708
- GCC_except_table13747
- GCC_except_table13751
- GCC_except_table13996
- GCC_except_table14523
- GCC_except_table15201
- GCC_except_table15205
- GCC_except_table16342
- GCC_except_table16445
- GCC_except_table16453
- GCC_except_table16454
- GCC_except_table16756
- GCC_except_table18402
- GCC_except_table19057
- GCC_except_table19227
- GCC_except_table19254
- GCC_except_table19819
- GCC_except_table19821
- GCC_except_table19824
- GCC_except_table19902
- GCC_except_table20902
- GCC_except_table20997
- GCC_except_table21218
- GCC_except_table22286
- GCC_except_table22289
- GCC_except_table22292
- GCC_except_table22907
- GCC_except_table22924
- GCC_except_table23640
- GCC_except_table25114
- GCC_except_table25126
- GCC_except_table26997
- GCC_except_table27000
- GCC_except_table27001
- GCC_except_table27002
- GCC_except_table27003
- GCC_except_table2790
- GCC_except_table2791
- GCC_except_table28695
- GCC_except_table28700
- GCC_except_table28702
- GCC_except_table28710
- GCC_except_table28712
- GCC_except_table28721
- GCC_except_table2873
- GCC_except_table2909
- GCC_except_table29769
- GCC_except_table29777
- GCC_except_table29778
- GCC_except_table29783
- GCC_except_table29784
- GCC_except_table29785
- GCC_except_table29787
- GCC_except_table29793
- GCC_except_table29794
- GCC_except_table29987
- GCC_except_table3161
- GCC_except_table3172
- GCC_except_table3185
- GCC_except_table4160
- GCC_except_table4164
- GCC_except_table4171
- GCC_except_table4173
- GCC_except_table4186
- GCC_except_table4399
- GCC_except_table5373
- GCC_except_table5374
- GCC_except_table5431
- GCC_except_table5591
- GCC_except_table5594
- GCC_except_table5598
- GCC_except_table5832
- GCC_except_table5841
- GCC_except_table6389
- GCC_except_table6391
- GCC_except_table6423
- GCC_except_table6424
- GCC_except_table6425
- GCC_except_table6426
- GCC_except_table6460
- GCC_except_table7021
- GCC_except_table7106
- GCC_except_table7107
- GCC_except_table7828
- GCC_except_table8094
- GCC_except_table8439
- GCC_except_table8443
- GCC_except_table8691
- GCC_except_table9368
- GCC_except_table9924
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AssistantServicesLibraryCore.frameworkLibrary.54798
- _ChronoServicesLibraryCore.frameworkLibrary.123588
- _ContactsLibrary.19273
- _ContactsLibrary.33370
- _ContactsLibrary.45340
- _ContactsLibrary.60767
- _ContactsLibraryCore.frameworkLibrary.111026
- _ContactsLibraryCore.frameworkLibrary.19261
- _ContactsLibraryCore.frameworkLibrary.19287
- _ContactsLibraryCore.frameworkLibrary.33375
- _ContactsLibraryCore.frameworkLibrary.45343
- _ContactsLibraryCore.frameworkLibrary.60770
- _CoreGraphicsLibrary.136626
- _CoreGraphicsLibraryCore.frameworkLibrary.136631
- _CoreSpotlightLibrary.19254
- _CoreSpotlightLibraryCore.frameworkLibrary.19257
- _CoreSpotlightLibraryCore.frameworkLibrary.59600
- _CoreSpotlightLibraryCore.frameworkLibrary.79661
- _HealthKitLibraryCore.frameworkLibrary.95458
- _IntentsUILibraryCore.frameworkLibrary.83532
- _LinkServicesLibraryCore.frameworkLibrary.165936
- _VoiceShortcutClientLibraryCore.frameworkLibrary.112962
- _VoiceShortcutClientLibraryCore.frameworkLibrary.123511
- _VoiceShortcutClientLibraryCore.frameworkLibrary.27807
- __OBJC_$_INSTANCE_METHODS_INAppIntent
- __OBJC_$_PROP_LIST__INPBMessage.424
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __Znwm
- ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke.28
- ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke.29
- ___74-[INAppIntentDeliverer _deliverIntentForwardingActionWithResponseHandler:]_block_invoke_2.31
- ___AssistantServicesLibraryCore_block_invoke.54799
- ___Block_byref_object_copy_.100500
- ___Block_byref_object_copy_.104452
- ___Block_byref_object_copy_.11702
- ___Block_byref_object_copy_.12947
- ___Block_byref_object_copy_.20709
- ___Block_byref_object_copy_.26569
- ___Block_byref_object_copy_.26848
- ___Block_byref_object_copy_.29502
- ___Block_byref_object_copy_.36925
- ___Block_byref_object_copy_.49768
- ___Block_byref_object_copy_.54387
- ___Block_byref_object_copy_.54808
- ___Block_byref_object_copy_.65127
- ___Block_byref_object_copy_.68140
- ___Block_byref_object_copy_.68949
- ___Block_byref_object_copy_.71810
- ___Block_byref_object_copy_.75024
- ___Block_byref_object_copy_.90333
- ___Block_byref_object_dispose_.100501
- ___Block_byref_object_dispose_.104453
- ___Block_byref_object_dispose_.11703
- ___Block_byref_object_dispose_.12948
- ___Block_byref_object_dispose_.20710
- ___Block_byref_object_dispose_.26570
- ___Block_byref_object_dispose_.26849
- ___Block_byref_object_dispose_.29503
- ___Block_byref_object_dispose_.36926
- ___Block_byref_object_dispose_.49769
- ___Block_byref_object_dispose_.54388
- ___Block_byref_object_dispose_.54809
- ___Block_byref_object_dispose_.65128
- ___Block_byref_object_dispose_.68141
- ___Block_byref_object_dispose_.68950
- ___Block_byref_object_dispose_.71811
- ___Block_byref_object_dispose_.75025
- ___Block_byref_object_dispose_.90334
- ___ChronoServicesLibraryCore_block_invoke.123589
- ___ContactsLibraryCore_block_invoke.111027
- ___ContactsLibraryCore_block_invoke.19262
- ___ContactsLibraryCore_block_invoke.19288
- ___ContactsLibraryCore_block_invoke.33376
- ___ContactsLibraryCore_block_invoke.45344
- ___ContactsLibraryCore_block_invoke.60771
- ___CoreGraphicsLibraryCore_block_invoke.136632
- ___CoreSpotlightLibraryCore_block_invoke.19258
- ___CoreSpotlightLibraryCore_block_invoke.59601
- ___CoreSpotlightLibraryCore_block_invoke.79662
- ___HealthKitLibraryCore_block_invoke.95459
- ___IntentsUILibraryCore_block_invoke.83533
- ___LinkServicesLibraryCore_block_invoke.165937
- ___VoiceShortcutClientLibraryCore_block_invoke.112963
- ___VoiceShortcutClientLibraryCore_block_invoke.123512
- ___VoiceShortcutClientLibraryCore_block_invoke.27808
- ___block_literal_global.10.103427
- ___block_literal_global.10.54823
- ___block_literal_global.100.75019
- ___block_literal_global.100246
- ___block_literal_global.100422
- ___block_literal_global.103417
- ___block_literal_global.104553
- ___block_literal_global.105568
- ___block_literal_global.11.111670
- ___block_literal_global.111698
- ___block_literal_global.11803
- ___block_literal_global.119795
- ___block_literal_global.12.158210
- ___block_literal_global.123611
- ___block_literal_global.12943
- ___block_literal_global.13.103429
- ___block_literal_global.13.98735
- ___block_literal_global.158198
- ___block_literal_global.17546
- ___block_literal_global.18236
- ___block_literal_global.20705
- ___block_literal_global.21.59567
- ___block_literal_global.22273
- ___block_literal_global.23086
- ___block_literal_global.26561
- ___block_literal_global.28929
- ___block_literal_global.29524
- ___block_literal_global.3.111669
- ___block_literal_global.30895
- ___block_literal_global.31063
- ___block_literal_global.31627
- ___block_literal_global.34183
- ___block_literal_global.36947
- ___block_literal_global.37337
- ___block_literal_global.40018
- ___block_literal_global.40522
- ___block_literal_global.42182
- ___block_literal_global.43100
- ___block_literal_global.43351
- ___block_literal_global.44258
- ___block_literal_global.47365
- ___block_literal_global.5.94021
- ___block_literal_global.53266
- ___block_literal_global.53838
- ___block_literal_global.54393
- ___block_literal_global.54807
- ___block_literal_global.59607
- ___block_literal_global.6.111681
- ___block_literal_global.6.71926
- ___block_literal_global.60628
- ___block_literal_global.62156
- ___block_literal_global.66616
- ___block_literal_global.68215
- ___block_literal_global.68332
- ___block_literal_global.68951
- ___block_literal_global.70354
- ___block_literal_global.71116
- ___block_literal_global.71860
- ___block_literal_global.71922
- ___block_literal_global.74882
- ___block_literal_global.77249
- ___block_literal_global.82.66610
- ___block_literal_global.82256
- ___block_literal_global.91.71861
- ___block_literal_global.91302
- ___block_literal_global.92161
- ___block_literal_global.94045
- ___block_literal_global.98746
- ___getAFPreferencesClass_block_invoke.54797
- ___getCGColorCreateSRGBSymbolLoc_block_invoke.136677
- ___getCGColorGetComponentsSymbolLoc_block_invoke.136625
- ___getCNContactEmailAddressesKeySymbolLoc_block_invoke.33380
- ___getCNContactPhoneNumbersKeySymbolLoc_block_invoke.33383
- ___getCNLabeledValueClass_block_invoke.60787
- ___getCNPostalAddressClass_block_invoke.111025
- ___getCSSearchableIndexClass_block_invoke.59599
- ___getCSSearchableItemAttributeSetClass_block_invoke.79660
- ___getHKUnitClass_block_invoke.95457
- _audit_stringAssistantServices.54804
- _audit_stringChronoServices.123594
- _audit_stringContacts.111032
- _audit_stringContacts.19264
- _audit_stringContacts.19290
- _audit_stringContacts.33378
- _audit_stringContacts.45346
- _audit_stringContacts.60774
- _audit_stringCoreGraphics.136634
- _audit_stringCoreSpotlight.19259
- _audit_stringCoreSpotlight.59606
- _audit_stringCoreSpotlight.79667
- _audit_stringHealthKit.95464
- _audit_stringLinkServices.165942
- _audit_stringVoiceShortcutClient.112968
- _audit_stringVoiceShortcutClient.123517
- _audit_stringVoiceShortcutClient.27809
- _getAFPreferencesClass.softClass.54796
- _getCGColorCreateSRGBSymbolLoc.ptr.136676
- _getCGColorGetComponentsSymbolLoc.ptr.136624
- _getCNContactEmailAddressesKeySymbolLoc.ptr.33379
- _getCNContactPhoneNumbersKeySymbolLoc.ptr.33382
- _getCNLabeledValueClass.60752
- _getCNLabeledValueClass.softClass.60786
- _getCNPostalAddressClass.softClass.111024
- _getCSSearchableIndexClass.softClass.59598
- _getCSSearchableItemAttributeSetClass.softClass.79659
- _getHKUnitClass.95455
- _getHKUnitClass.softClass.95456
- _intentDescription.intentDescription.31628
- _intentDescription.intentDescription.39013
- _intentDescription.intentDescription.42530
- _intentDescription.intentDescription.64092
- _intentDescription.intentDescription.68333
- _intentDescription.onceToken.31626
- _intentDescription.onceToken.39012
- _intentDescription.onceToken.42529
- _intentDescription.onceToken.64091
- _intentDescription.onceToken.68331
- _objc_msgSend$initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:
- _serviceIdentifier.onceToken.83506
- _serviceIdentifier.sServiceIdentifier.83507
- _sharedCache.onceToken.82255
- _sharedManager.onceToken.123610
- _sharedManager.onceToken.59597
- _sharedManager.sharedManager.123612
- _sharedProvider.onceToken.158209
CStrings:
+ "%s This should not happen! Unable to get a bundle for %{public}@"
+ "-[INStringLocalizer bundleWithIdentifier:fileURL:]"
+ "@176@0:8@16@24@32@40@48@56@64@72@80q88q96@104@112@120@128@136@144@152@160@168"
+ "BLOCKED"
+ "CUSTOM_ACKNOWLEDGEMENT"
+ "POLL"
+ "T@\"NSString\",C,N,V_translatedToLanguage"
+ "_setError"
+ "_translatedToLanguage"
+ "custom acknowledgement"
+ "customAcknowledgement"
+ "getBytes:range:"
+ "hasTranslatedToLanguage"
+ "initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:translatedToLanguage:"
+ "initWithIntentForwardingAction:responseQueue:responseHandler:"
+ "instancesRespondToSelector:"
+ "setPosition:"
+ "setTranslatedToLanguage:"
+ "translatedToLanguage"
+ "{map<std::string, INSystemApp, std::less<std::string>, std::allocator<std::pair<const std::string, INSystemApp>>>=\"__tree_\"{__tree<std::__value_type<std::string, INSystemApp>, std::__map_value_compare<std::string, std::__value_type<std::string, INSystemApp>, std::less<std::string>>, std::allocator<std::__value_type<std::string, INSystemApp>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<std::string, INSystemApp, std::less<std::string>, std::allocator<std::pair<const std::string, INSystemApp>>>=\"__tree_\"{__tree<std::__value_type<std::string, INSystemApp>, std::__map_value_compare<std::string, std::__value_type<std::string, INSystemApp>, std::less<std::string>>, std::allocator<std::__value_type<std::string, INSystemApp>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, INSystemApp>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, INSystemApp>, std::less<std::string>>>=\"__value_\"Q}}}"

```
