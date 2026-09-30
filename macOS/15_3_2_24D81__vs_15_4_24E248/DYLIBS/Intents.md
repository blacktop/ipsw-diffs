## Intents

> `/System/Library/Frameworks/Intents.framework/Versions/A/Intents`

```diff

-3208.0.0.0.0
-  __TEXT.__text: 0x4af3c4
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x571a8
-  __TEXT.__const: 0x1d28
-  __TEXT.__gcc_except_tab: 0x1f40
-  __TEXT.__oslogstring: 0x527a
-  __TEXT.__cstring: 0x4ba90
+3506.0.1.0.0
+  __TEXT.__text: 0x4b04a8
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x7a9b4
+  __TEXT.__const: 0x1dc8
   __TEXT.__dlopen_cstrs: 0xb0a
+  __TEXT.__gcc_except_tab: 0x1fa4
+  __TEXT.__oslogstring: 0x527a
+  __TEXT.__cstring: 0x4bace
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0xfd08
+  __TEXT.__unwind_info: 0xf588
   __TEXT.__objc_classname: 0x12514
-  __TEXT.__objc_methname: 0x6a511
-  __TEXT.__objc_methtype: 0xcc06
-  __TEXT.__objc_stubs: 0x33260
+  __TEXT.__objc_methname: 0x6a8de
+  __TEXT.__objc_methtype: 0xcc89
+  __TEXT.__objc_stubs: 0x333a0
   __DATA_CONST.__got: 0x2908
-  __DATA_CONST.__const: 0x9950
+  __DATA_CONST.__const: 0x9ae8
   __DATA_CONST.__objc_classlist: 0x29e0
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x19b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x152e0
+  __DATA_CONST.__objc_selrefs: 0x15468
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1438
   __DATA_CONST.__objc_arraydata: 0xcbc0
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6b0
   __AUTH_CONST.__const: 0x3e20
-  __AUTH_CONST.__cfstring: 0x45000
-  __AUTH_CONST.__objc_const: 0xfa660
+  __AUTH_CONST.__cfstring: 0x45100
+  __AUTH_CONST.__objc_const: 0xb6fe8
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x5310
   __AUTH_CONST.__objc_dictobj: 0x3a20
   __AUTH.__objc_data: 0x2710
-  __DATA.__objc_ivar: 0x3d04
+  __DATA.__objc_ivar: 0x3d18
   __DATA.__data: 0x13538
   __DATA.__bss: 0xd38
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2C8F9E0-4BCA-3BF7-AB4B-2C271E439900
-  Functions: 31599
-  Symbols:   59806
-  CStrings:  37914
+  UUID: A6C05395-CA89-3815-AFB8-FCA0F6C9E861
+  Functions: 31117
+  Symbols:   59851
+  CStrings:  37956
 
Symbols:
+ +[INIntentCodableDescription(__Name) __NameKey].37465
+ +[INSystemAppGrouping groupingForKey:iOS:macOS:watchOS:tvOS:]
+ +[INSystemAppMatch matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:]
+ +[_INPBMessage inlineGlyphContentType]
+ -[INMessage initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:]
+ -[INMessage inlineGlyphContent]
+ -[INMessage setInlineGlyphContent:]
+ -[INSendMessageIntent setShouldHideSiriAttribution:]
+ -[INSendMessageIntent shouldHideSiriAttribution]
+ -[INSystemAppGrouping setTvOS:]
+ -[INSystemAppGrouping tvOS]
+ -[INSystemAppMatch initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:]
+ -[INSystemAppMatch tvOSBundleIdentifier]
+ -[_INPBMessage addInlineGlyphContent:]
+ -[_INPBMessage clearInlineGlyphContents]
+ -[_INPBMessage inlineGlyphContentAtIndex:]
+ -[_INPBMessage inlineGlyphContentsCount]
+ -[_INPBMessage inlineGlyphContents]
+ -[_INPBMessage setInlineGlyphContents:]
+ -[_INPBSendMessageIntent hasShouldHideSiriAttribution]
+ -[_INPBSendMessageIntent setHasShouldHideSiriAttribution:]
+ -[_INPBSendMessageIntent setShouldHideSiriAttribution:]
+ -[_INPBSendMessageIntent shouldHideSiriAttribution]
+ AssistantServicesLibraryCore.frameworkLibrary.54698
+ ContactsLibrary.19277
+ ContactsLibrary.33384
+ ContactsLibrary.45347
+ ContactsLibrary.60703
+ ContactsLibraryCore.frameworkLibrary.114272
+ ContactsLibraryCore.frameworkLibrary.19264
+ ContactsLibraryCore.frameworkLibrary.19291
+ ContactsLibraryCore.frameworkLibrary.33389
+ ContactsLibraryCore.frameworkLibrary.45350
+ ContactsLibraryCore.frameworkLibrary.60706
+ CoreGraphicsLibrary.139849
+ CoreGraphicsLibraryCore.frameworkLibrary.139854
+ CoreSpotlightLibrary.19256
+ CoreSpotlightLibraryCore.frameworkLibrary.19259
+ CoreSpotlightLibraryCore.frameworkLibrary.59529
+ CoreSpotlightLibraryCore.frameworkLibrary.79724
+ GCC_except_table10108
+ GCC_except_table10120
+ GCC_except_table10122
+ GCC_except_table10127
+ GCC_except_table10192
+ GCC_except_table10752
+ GCC_except_table10877
+ GCC_except_table10881
+ GCC_except_table10994
+ GCC_except_table11107
+ GCC_except_table11134
+ GCC_except_table11135
+ GCC_except_table11357
+ GCC_except_table11799
+ GCC_except_table12528
+ GCC_except_table12539
+ GCC_except_table12542
+ GCC_except_table12550
+ GCC_except_table12571
+ GCC_except_table13176
+ GCC_except_table13743
+ GCC_except_table13747
+ GCC_except_table13992
+ GCC_except_table14519
+ GCC_except_table15197
+ GCC_except_table15201
+ GCC_except_table16329
+ GCC_except_table16432
+ GCC_except_table16440
+ GCC_except_table16441
+ GCC_except_table16743
+ GCC_except_table18389
+ GCC_except_table19044
+ GCC_except_table19201
+ GCC_except_table19229
+ GCC_except_table20234
+ GCC_except_table20236
+ GCC_except_table20239
+ GCC_except_table20393
+ GCC_except_table21420
+ GCC_except_table21721
+ GCC_except_table22789
+ GCC_except_table22792
+ GCC_except_table22795
+ GCC_except_table23410
+ GCC_except_table23840
+ GCC_except_table24150
+ GCC_except_table25625
+ GCC_except_table25637
+ GCC_except_table27508
+ GCC_except_table27511
+ GCC_except_table27512
+ GCC_except_table27513
+ GCC_except_table27514
+ GCC_except_table2878
+ GCC_except_table2914
+ GCC_except_table29211
+ GCC_except_table29213
+ GCC_except_table29221
+ GCC_except_table29223
+ GCC_except_table29232
+ GCC_except_table30280
+ GCC_except_table30289
+ GCC_except_table30293
+ GCC_except_table30294
+ GCC_except_table30295
+ GCC_except_table30296
+ GCC_except_table30298
+ GCC_except_table30302
+ GCC_except_table30304
+ GCC_except_table30305
+ GCC_except_table30306
+ GCC_except_table30307
+ GCC_except_table30309
+ GCC_except_table30498
+ GCC_except_table3167
+ GCC_except_table3170
+ GCC_except_table3180
+ GCC_except_table3194
+ GCC_except_table4169
+ GCC_except_table4173
+ GCC_except_table4180
+ GCC_except_table4182
+ GCC_except_table4195
+ GCC_except_table4408
+ GCC_except_table5388
+ GCC_except_table5389
+ GCC_except_table5596
+ GCC_except_table5599
+ GCC_except_table5603
+ GCC_except_table5605
+ GCC_except_table5840
+ GCC_except_table5849
+ GCC_except_table6389
+ GCC_except_table6392
+ GCC_except_table6424
+ GCC_except_table6425
+ GCC_except_table6426
+ GCC_except_table6427
+ GCC_except_table6461
+ GCC_except_table7024
+ GCC_except_table7109
+ GCC_except_table7110
+ GCC_except_table7833
+ GCC_except_table8099
+ GCC_except_table8444
+ GCC_except_table8448
+ GCC_except_table9365
+ GCC_except_table9921
+ HealthKitLibraryCore.frameworkLibrary.95599
+ IntentsUILibraryCore.frameworkLibrary.83601
+ LinkServicesLibraryCore.frameworkLibrary.169144
+ OBJC_IVAR_$_INMessage._inlineGlyphContent
+ OBJC_IVAR_$_INSystemAppGrouping._tvOS
+ OBJC_IVAR_$_INSystemAppMatch._tvOSBundleIdentifier
+ OBJC_IVAR_$__INPBMessage._inlineGlyphContents
+ OBJC_IVAR_$__INPBSendMessageIntent._shouldHideSiriAttribution
+ VoiceShortcutClientLibraryCore.frameworkLibrary.116180
+ VoiceShortcutClientLibraryCore.frameworkLibrary.126697
+ VoiceShortcutClientLibraryCore.frameworkLibrary.27796
+ _OBJC_$_PROP_LIST__INPBMessage.424
+ _OBJC_$_PROP_LIST__INPBSendMessageIntent.267
+ __28-[INCodable _writeTo:error:]_block_invoke.85
+ __29-[INCodable _readFrom:error:]_block_invoke.66
+ __AssistantServicesLibraryCore_block_invoke.54699
+ __Block_byref_object_copy_.100612
+ __Block_byref_object_copy_.107665
+ __Block_byref_object_copy_.11666
+ __Block_byref_object_copy_.12939
+ __Block_byref_object_copy_.20714
+ __Block_byref_object_copy_.26604
+ __Block_byref_object_copy_.29504
+ __Block_byref_object_copy_.36934
+ __Block_byref_object_copy_.49716
+ __Block_byref_object_copy_.54319
+ __Block_byref_object_copy_.65065
+ __Block_byref_object_copy_.68230
+ __Block_byref_object_copy_.69045
+ __Block_byref_object_copy_.71912
+ __Block_byref_object_copy_.75112
+ __Block_byref_object_copy_.90389
+ __Block_byref_object_dispose_.100613
+ __Block_byref_object_dispose_.107666
+ __Block_byref_object_dispose_.11667
+ __Block_byref_object_dispose_.12940
+ __Block_byref_object_dispose_.20715
+ __Block_byref_object_dispose_.26605
+ __Block_byref_object_dispose_.29505
+ __Block_byref_object_dispose_.36935
+ __Block_byref_object_dispose_.49717
+ __Block_byref_object_dispose_.54320
+ __Block_byref_object_dispose_.65066
+ __Block_byref_object_dispose_.68231
+ __Block_byref_object_dispose_.69046
+ __Block_byref_object_dispose_.71913
+ __Block_byref_object_dispose_.75113
+ __Block_byref_object_dispose_.90390
+ __ContactsLibraryCore_block_invoke.114273
+ __ContactsLibraryCore_block_invoke.19265
+ __ContactsLibraryCore_block_invoke.19292
+ __ContactsLibraryCore_block_invoke.33390
+ __ContactsLibraryCore_block_invoke.45351
+ __ContactsLibraryCore_block_invoke.60707
+ __CoreGraphicsLibraryCore_block_invoke.139855
+ __CoreSpotlightLibraryCore_block_invoke.19260
+ __CoreSpotlightLibraryCore_block_invoke.59530
+ __CoreSpotlightLibraryCore_block_invoke.79725
+ __HealthKitLibraryCore_block_invoke.95600
+ __INMessageGlyphAvatarDescriptionKey
+ __INMessageGlyphBundleIDKey
+ __INMessageGlyphCountKey
+ __INMessageGlyphExpressionDescriptionKey
+ __INMessageGlyphGenmojiDescriptionKey
+ __INMessageGlyphIndexKey
+ __INMessageGlyphTypeKey
+ __IntentsUILibraryCore_block_invoke.83602
+ __LinkServicesLibraryCore_block_invoke.169145
+ __VoiceShortcutClientLibraryCore_block_invoke.116181
+ __VoiceShortcutClientLibraryCore_block_invoke.126698
+ __VoiceShortcutClientLibraryCore_block_invoke.27797
+ __ZL35INSystemAppBundleIdentifierAlarmsTV
+ __ZL35INSystemAppBundleIdentifierTimersTV
+ __ZL37INSystemAppBundleIdentifierFaceTimeTV
+ __ZL37INSystemAppBundleIdentifierSettingsTV
+ __ZL38INSystemAppBundleIdentifierCalendarMac
+ __ZL39INSystemAppBundleIdentifierWorldClockTV
+ __ZL40INSystemAppBundleIdentifierCalendarPhone
+ __ZL40INSystemAppBundleIdentifierCalendarWatch
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __block_literal_global.10.105646
+ __block_literal_global.100394
+ __block_literal_global.100521
+ __block_literal_global.105636
+ __block_literal_global.107899
+ __block_literal_global.108916
+ __block_literal_global.114915
+ __block_literal_global.11768
+ __block_literal_global.12.161430
+ __block_literal_global.122980
+ __block_literal_global.126770
+ __block_literal_global.129178
+ __block_literal_global.12935
+ __block_literal_global.13.105648
+ __block_literal_global.161418
+ __block_literal_global.17554
+ __block_literal_global.18242
+ __block_literal_global.20711
+ __block_literal_global.21.53798
+ __block_literal_global.22288
+ __block_literal_global.23105
+ __block_literal_global.26596
+ __block_literal_global.28913
+ __block_literal_global.30897
+ __block_literal_global.31067
+ __block_literal_global.31637
+ __block_literal_global.34200
+ __block_literal_global.36946
+ __block_literal_global.37337
+ __block_literal_global.40016
+ __block_literal_global.40514
+ __block_literal_global.42180
+ __block_literal_global.43103
+ __block_literal_global.43353
+ __block_literal_global.44260
+ __block_literal_global.47314
+ __block_literal_global.5.40515
+ __block_literal_global.5.94099
+ __block_literal_global.53222
+ __block_literal_global.53803
+ __block_literal_global.54327
+ __block_literal_global.59537
+ __block_literal_global.60564
+ __block_literal_global.62096
+ __block_literal_global.66543
+ __block_literal_global.68309
+ __block_literal_global.68426
+ __block_literal_global.69047
+ __block_literal_global.70.75027
+ __block_literal_global.70457
+ __block_literal_global.71221
+ __block_literal_global.71963
+ __block_literal_global.72025
+ __block_literal_global.74986
+ __block_literal_global.77310
+ __block_literal_global.78
+ __block_literal_global.82323
+ __block_literal_global.91.71964
+ __block_literal_global.91370
+ __block_literal_global.92231
+ __block_literal_global.94123
+ __block_literal_global.98891
+ __getAFPreferencesClass_block_invoke.54697
+ __getCGColorCreateSRGBSymbolLoc_block_invoke.139901
+ __getCGColorGetComponentsSymbolLoc_block_invoke.139848
+ __getCNContactEmailAddressesKeySymbolLoc_block_invoke.33396
+ __getCNContactPhoneNumbersKeySymbolLoc_block_invoke.33399
+ __getCNLabeledValueClass_block_invoke.60724
+ __getCNPostalAddressClass_block_invoke.114271
+ __getCSSearchableIndexClass_block_invoke.59528
+ __getCSSearchableItemAttributeSetClass_block_invoke.79723
+ __getHKUnitClass_block_invoke.95598
+ _objc_msgSend$addInlineGlyphContent:
+ _objc_msgSend$groupingForKey:iOS:macOS:watchOS:tvOS:
+ _objc_msgSend$hasShouldHideSiriAttribution
+ _objc_msgSend$initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:
+ _objc_msgSend$initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:
+ _objc_msgSend$inlineGlyphContent
+ _objc_msgSend$inlineGlyphContents
+ _objc_msgSend$matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:
+ _objc_msgSend$setHasShouldHideSiriAttribution:
+ _objc_msgSend$setInlineGlyphContents:
+ _objc_msgSend$setShouldHideSiriAttribution:
+ _objc_msgSend$setTvOS:
+ _objc_msgSend$shouldHideSiriAttribution
+ audit_stringAssistantServices.54704
+ audit_stringContacts.114278
+ audit_stringContacts.19267
+ audit_stringContacts.19294
+ audit_stringContacts.33392
+ audit_stringContacts.45353
+ audit_stringContacts.60710
+ audit_stringCoreGraphics.139857
+ audit_stringCoreSpotlight.19261
+ audit_stringCoreSpotlight.59535
+ audit_stringCoreSpotlight.79730
+ audit_stringHealthKit.95605
+ audit_stringLinkServices.169150
+ audit_stringVoiceShortcutClient.116186
+ audit_stringVoiceShortcutClient.126703
+ audit_stringVoiceShortcutClient.27798
+ getAFPreferencesClass.softClass.54696
+ getCGColorCreateSRGBSymbolLoc.ptr.139900
+ getCGColorGetComponentsSymbolLoc.ptr.139847
+ getCNContactEmailAddressesKeySymbolLoc.ptr.33395
+ getCNContactPhoneNumbersKeySymbolLoc.ptr.33398
+ getCNLabeledValueClass.60688
+ getCNLabeledValueClass.softClass.60723
+ getCNPostalAddressClass.softClass.114270
+ getCSSearchableIndexClass.softClass.59527
+ getCSSearchableItemAttributeSetClass.softClass.79722
+ getHKUnitClass.95596
+ getHKUnitClass.softClass.95597
+ intentDescription.intentDescription.31638
+ intentDescription.intentDescription.39010
+ intentDescription.intentDescription.42533
+ intentDescription.intentDescription.64033
+ intentDescription.intentDescription.68427
+ intentDescription.onceToken.31636
+ intentDescription.onceToken.39009
+ intentDescription.onceToken.42532
+ intentDescription.onceToken.64032
+ intentDescription.onceToken.68425
+ serviceIdentifier.onceToken.83573
+ serviceIdentifier.sServiceIdentifier.83574
+ sharedCache.onceToken.82322
+ sharedManager.onceToken.126769
+ sharedManager.onceToken.59526
+ sharedManager.sharedManager.126771
+ sharedProvider.onceToken.161429
- +[INIntentCodableDescription(__Name) __NameKey].37591
- +[INSystemAppMatch matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:]
- -[INSendMessageIntent _isUserConfirmationRequired]
- -[INSystemAppMatch initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:]
- AssistantServicesLibraryCore.frameworkLibrary.54808
- ContactsLibrary.19411
- ContactsLibrary.33521
- ContactsLibrary.45468
- ContactsLibrary.60758
- ContactsLibraryCore.frameworkLibrary.114223
- ContactsLibraryCore.frameworkLibrary.19398
- ContactsLibraryCore.frameworkLibrary.19425
- ContactsLibraryCore.frameworkLibrary.33526
- ContactsLibraryCore.frameworkLibrary.45471
- ContactsLibraryCore.frameworkLibrary.60761
- CoreGraphicsLibrary.139803
- CoreGraphicsLibraryCore.frameworkLibrary.139808
- CoreSpotlightLibrary.19390
- CoreSpotlightLibraryCore.frameworkLibrary.19393
- CoreSpotlightLibraryCore.frameworkLibrary.59584
- CoreSpotlightLibraryCore.frameworkLibrary.79770
- GCC_except_table10098
- GCC_except_table10110
- GCC_except_table10112
- GCC_except_table10117
- GCC_except_table10182
- GCC_except_table10742
- GCC_except_table10863
- GCC_except_table10867
- GCC_except_table10980
- GCC_except_table11093
- GCC_except_table11120
- GCC_except_table11121
- GCC_except_table11342
- GCC_except_table11784
- GCC_except_table12513
- GCC_except_table12524
- GCC_except_table12527
- GCC_except_table12535
- GCC_except_table12556
- GCC_except_table13161
- GCC_except_table13728
- GCC_except_table13732
- GCC_except_table13977
- GCC_except_table14504
- GCC_except_table15182
- GCC_except_table15186
- GCC_except_table16314
- GCC_except_table16417
- GCC_except_table16425
- GCC_except_table16426
- GCC_except_table16728
- GCC_except_table18374
- GCC_except_table19029
- GCC_except_table19186
- GCC_except_table19214
- GCC_except_table20219
- GCC_except_table20221
- GCC_except_table20224
- GCC_except_table20378
- GCC_except_table21405
- GCC_except_table21706
- GCC_except_table22774
- GCC_except_table22777
- GCC_except_table22780
- GCC_except_table23395
- GCC_except_table23825
- GCC_except_table24135
- GCC_except_table25610
- GCC_except_table25622
- GCC_except_table27493
- GCC_except_table27496
- GCC_except_table27497
- GCC_except_table27498
- GCC_except_table27499
- GCC_except_table2871
- GCC_except_table2907
- GCC_except_table29191
- GCC_except_table29196
- GCC_except_table29198
- GCC_except_table29208
- GCC_except_table29217
- GCC_except_table30262
- GCC_except_table30269
- GCC_except_table30270
- GCC_except_table30274
- GCC_except_table30275
- GCC_except_table30276
- GCC_except_table30277
- GCC_except_table30279
- GCC_except_table30283
- GCC_except_table30285
- GCC_except_table30286
- GCC_except_table30287
- GCC_except_table30290
- GCC_except_table30479
- GCC_except_table3160
- GCC_except_table3163
- GCC_except_table3173
- GCC_except_table3187
- GCC_except_table4159
- GCC_except_table4163
- GCC_except_table4170
- GCC_except_table4172
- GCC_except_table4185
- GCC_except_table4398
- GCC_except_table5378
- GCC_except_table5379
- GCC_except_table5586
- GCC_except_table5589
- GCC_except_table5593
- GCC_except_table5595
- GCC_except_table5830
- GCC_except_table5839
- GCC_except_table6379
- GCC_except_table6382
- GCC_except_table6414
- GCC_except_table6415
- GCC_except_table6416
- GCC_except_table6417
- GCC_except_table6451
- GCC_except_table7014
- GCC_except_table7099
- GCC_except_table7100
- GCC_except_table7823
- GCC_except_table8089
- GCC_except_table8434
- GCC_except_table8438
- GCC_except_table9355
- GCC_except_table9911
- HealthKitLibraryCore.frameworkLibrary.95556
- IntentsUILibraryCore.frameworkLibrary.83648
- LinkServicesLibraryCore.frameworkLibrary.169092
- VoiceShortcutClientLibraryCore.frameworkLibrary.116131
- VoiceShortcutClientLibraryCore.frameworkLibrary.126648
- VoiceShortcutClientLibraryCore.frameworkLibrary.27929
- _OBJC_$_PROP_LIST__INPBMessage.407
- _OBJC_$_PROP_LIST__INPBSendMessageIntent.254
- __28-[INCodable _writeTo:error:]_block_invoke.84
- __29-[INCodable _readFrom:error:]_block_invoke.65
- __AssistantServicesLibraryCore_block_invoke.54809
- __Block_byref_object_copy_.100578
- __Block_byref_object_copy_.107632
- __Block_byref_object_copy_.11846
- __Block_byref_object_copy_.13095
- __Block_byref_object_copy_.20848
- __Block_byref_object_copy_.26737
- __Block_byref_object_copy_.29640
- __Block_byref_object_copy_.37071
- __Block_byref_object_copy_.49826
- __Block_byref_object_copy_.54429
- __Block_byref_object_copy_.65111
- __Block_byref_object_copy_.68278
- __Block_byref_object_copy_.69093
- __Block_byref_object_copy_.71957
- __Block_byref_object_copy_.75157
- __Block_byref_object_copy_.90438
- __Block_byref_object_dispose_.100579
- __Block_byref_object_dispose_.107633
- __Block_byref_object_dispose_.11847
- __Block_byref_object_dispose_.13096
- __Block_byref_object_dispose_.20849
- __Block_byref_object_dispose_.26738
- __Block_byref_object_dispose_.29641
- __Block_byref_object_dispose_.37072
- __Block_byref_object_dispose_.49827
- __Block_byref_object_dispose_.54430
- __Block_byref_object_dispose_.65112
- __Block_byref_object_dispose_.68279
- __Block_byref_object_dispose_.69094
- __Block_byref_object_dispose_.71958
- __Block_byref_object_dispose_.75158
- __Block_byref_object_dispose_.90439
- __ContactsLibraryCore_block_invoke.114224
- __ContactsLibraryCore_block_invoke.19399
- __ContactsLibraryCore_block_invoke.19426
- __ContactsLibraryCore_block_invoke.33527
- __ContactsLibraryCore_block_invoke.45472
- __ContactsLibraryCore_block_invoke.60762
- __CoreGraphicsLibraryCore_block_invoke.139809
- __CoreSpotlightLibraryCore_block_invoke.19394
- __CoreSpotlightLibraryCore_block_invoke.59585
- __CoreSpotlightLibraryCore_block_invoke.79771
- __HealthKitLibraryCore_block_invoke.95557
- __IntentsUILibraryCore_block_invoke.83649
- __LinkServicesLibraryCore_block_invoke.169093
- __VoiceShortcutClientLibraryCore_block_invoke.116132
- __VoiceShortcutClientLibraryCore_block_invoke.126649
- __VoiceShortcutClientLibraryCore_block_invoke.27930
- __ZL40INSystemAppBundleIdentifierFaceTimePhone
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __block_literal_global.10.105613
- __block_literal_global.100360
- __block_literal_global.100487
- __block_literal_global.105603
- __block_literal_global.107866
- __block_literal_global.108866
- __block_literal_global.114866
- __block_literal_global.11938
- __block_literal_global.12.161385
- __block_literal_global.122931
- __block_literal_global.126721
- __block_literal_global.129129
- __block_literal_global.13.105615
- __block_literal_global.13091
- __block_literal_global.161373
- __block_literal_global.17709
- __block_literal_global.18376
- __block_literal_global.20845
- __block_literal_global.21.53908
- __block_literal_global.22422
- __block_literal_global.23239
- __block_literal_global.26729
- __block_literal_global.29049
- __block_literal_global.31034
- __block_literal_global.31204
- __block_literal_global.31774
- __block_literal_global.34337
- __block_literal_global.37083
- __block_literal_global.37463
- __block_literal_global.40137
- __block_literal_global.40635
- __block_literal_global.42301
- __block_literal_global.43224
- __block_literal_global.43474
- __block_literal_global.44381
- __block_literal_global.47432
- __block_literal_global.5.40636
- __block_literal_global.5.94149
- __block_literal_global.53332
- __block_literal_global.53913
- __block_literal_global.54437
- __block_literal_global.59592
- __block_literal_global.60619
- __block_literal_global.62144
- __block_literal_global.66595
- __block_literal_global.68357
- __block_literal_global.68474
- __block_literal_global.69095
- __block_literal_global.70.75072
- __block_literal_global.70502
- __block_literal_global.71266
- __block_literal_global.72008
- __block_literal_global.72070
- __block_literal_global.75031
- __block_literal_global.77
- __block_literal_global.77356
- __block_literal_global.82369
- __block_literal_global.91.72009
- __block_literal_global.91419
- __block_literal_global.92281
- __block_literal_global.94173
- __block_literal_global.98857
- __getAFPreferencesClass_block_invoke.54807
- __getCGColorCreateSRGBSymbolLoc_block_invoke.139855
- __getCGColorGetComponentsSymbolLoc_block_invoke.139802
- __getCNContactEmailAddressesKeySymbolLoc_block_invoke.33533
- __getCNContactPhoneNumbersKeySymbolLoc_block_invoke.33536
- __getCNLabeledValueClass_block_invoke.60779
- __getCNPostalAddressClass_block_invoke.114222
- __getCSSearchableIndexClass_block_invoke.59583
- __getCSSearchableItemAttributeSetClass_block_invoke.79769
- __getHKUnitClass_block_invoke.95555
- _fmod
- _objc_msgSend$groupingForKey:iOS:macOS:watchOS:
- _objc_msgSend$initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:
- _objc_msgSend$matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:
- _strcmp
- _strncmp
- audit_stringAssistantServices.54814
- audit_stringContacts.114229
- audit_stringContacts.19401
- audit_stringContacts.19428
- audit_stringContacts.33529
- audit_stringContacts.45474
- audit_stringContacts.60765
- audit_stringCoreGraphics.139811
- audit_stringCoreSpotlight.19395
- audit_stringCoreSpotlight.59590
- audit_stringCoreSpotlight.79776
- audit_stringHealthKit.95562
- audit_stringLinkServices.169098
- audit_stringVoiceShortcutClient.116137
- audit_stringVoiceShortcutClient.126654
- audit_stringVoiceShortcutClient.27931
- getAFPreferencesClass.softClass.54806
- getCGColorCreateSRGBSymbolLoc.ptr.139854
- getCGColorGetComponentsSymbolLoc.ptr.139801
- getCNContactEmailAddressesKeySymbolLoc.ptr.33532
- getCNContactPhoneNumbersKeySymbolLoc.ptr.33535
- getCNLabeledValueClass.60743
- getCNLabeledValueClass.softClass.60778
- getCNPostalAddressClass.softClass.114221
- getCSSearchableIndexClass.softClass.59582
- getCSSearchableItemAttributeSetClass.softClass.79768
- getHKUnitClass.95553
- getHKUnitClass.softClass.95554
- intentDescription.intentDescription.31775
- intentDescription.intentDescription.39135
- intentDescription.intentDescription.42654
- intentDescription.intentDescription.64079
- intentDescription.intentDescription.68475
- intentDescription.onceToken.31773
- intentDescription.onceToken.39134
- intentDescription.onceToken.42653
- intentDescription.onceToken.64078
- intentDescription.onceToken.68473
- serviceIdentifier.onceToken.83620
- serviceIdentifier.sServiceIdentifier.83621
- sharedCache.onceToken.82368
- sharedManager.onceToken.126720
- sharedManager.onceToken.59581
- sharedManager.sharedManager.126722
- sharedProvider.onceToken.161384
CStrings:
+ "@\"_INPBDictionary\"24@0:8Q16"
+ "@168@0:8@16@24@32@40@48@56@64@72@80q88q96@104@112@120@128@136@144@152@160"
+ "AvatarDescription"
+ "BundleID"
+ "Count"
+ "GenmojiDescription"
+ "Index"
+ "StickerDescription"
+ "T@\"NSArray\",&,N,V_tvOS"
+ "T@\"NSArray\",C,N,V_inlineGlyphContents"
+ "T@\"NSArray\",C,V_inlineGlyphContent"
+ "T@\"NSString\",R,N,V_tvOSBundleIdentifier"
+ "TB,N,V_shouldHideSiriAttribution"
+ "_inlineGlyphContent"
+ "_inlineGlyphContents"
+ "_shouldHideSiriAttribution"
+ "_tvOS"
+ "_tvOSBundleIdentifier"
+ "addInlineGlyphContent:"
+ "clearInlineGlyphContents"
+ "groupingForKey:iOS:macOS:watchOS:tvOS:"
+ "hasShouldHideSiriAttribution"
+ "initWithIdentifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:dateMessageWasLastRead:numberOfAttachments:messageType:messageEffectType:referencedMessage:serviceName:attachmentFiles:location:linkMetadata:reaction:sticker:inlineGlyphContent:"
+ "initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:"
+ "inlineGlyphContent"
+ "inlineGlyphContentAtIndex:"
+ "inlineGlyphContentType"
+ "inlineGlyphContents"
+ "inlineGlyphContentsCount"
+ "matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:tvOSBundleIdentifier:"
+ "setHasShouldHideSiriAttribution:"
+ "setInlineGlyphContent:"
+ "setInlineGlyphContents:"
+ "setShouldHideSiriAttribution:"
+ "setTvOS:"
+ "shouldHideSiriAttribution"
+ "tvOS"
+ "tvOSBundleIdentifier"
+ "{?=\"effect\"b1\"outgoingMessageType\"b1\"shouldHideSiriAttribution\"b1}"
- "com.apple.NanoCalendar"
- "com.apple.iCal"
- "com.apple.mobilecal"
- "initWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:"
- "matchWithiOSBundleIdentifier:macOSBundleIdentifier:watchOSBundleIdentifier:"
- "{?=\"effect\"b1\"outgoingMessageType\"b1}"

```
