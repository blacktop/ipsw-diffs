## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-4015.0.0.0.0
-  __TEXT.__text: 0x450e08
+4015.1.5.0.0
+  __TEXT.__text: 0x451860
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x78bcc
+  __TEXT.__objc_methlist: 0x78bf4
   __TEXT.__const: 0x1eb0
   __TEXT.__dlopen_cstrs: 0xce9
-  __TEXT.__gcc_except_tab: 0x2380
-  __TEXT.__oslogstring: 0x57c4
-  __TEXT.__cstring: 0x47461
+  __TEXT.__gcc_except_tab: 0x2394
+  __TEXT.__oslogstring: 0x587b
+  __TEXT.__cstring: 0x47676
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x10e28
+  __TEXT.__unwind_info: 0x10e38
   __TEXT.__objc_classname: 0x12221
-  __TEXT.__objc_methname: 0x69e66
+  __TEXT.__objc_methname: 0x69e8b
   __TEXT.__objc_methtype: 0xcc5e
   __TEXT.__objc_stubs: 0x33c00
   __DATA_CONST.__got: 0x2898

   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1940
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15430
+  __DATA_CONST.__objc_selrefs: 0x15438
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1398
-  __DATA_CONST.__objc_arraydata: 0xc298
+  __DATA_CONST.__objc_arraydata: 0xc7f8
   __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0x1780
-  __AUTH_CONST.__cfstring: 0x425e0
-  __AUTH_CONST.__objc_const: 0xb4ce8
+  __AUTH_CONST.__cfstring: 0x428e0
+  __AUTH_CONST.__objc_const: 0xb4d00
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_arrayobj: 0x4cf8
-  __AUTH_CONST.__objc_dictobj: 0x3a48
+  __AUTH_CONST.__objc_arrayobj: 0x4da0
+  __AUTH_CONST.__objc_dictobj: 0x3b60
   __AUTH.__objc_data: 0x14500
   __DATA.__objc_ivar: 0x3d48
   __DATA.__data: 0x12f98
-  __DATA.__bss: 0xc58
+  __DATA.__bss: 0xc60
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x56e0
   __DATA_DIRTY.__bss: 0x278

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 204C11E4-EBBA-3208-8420-986ABEE85BC1
-  Functions: 30622
-  Symbols:   87221
-  CStrings:  37173
+  UUID: 1926C73C-C16D-3D74-A795-BFA88174CB69
+  Functions: 30625
+  Symbols:   87229
+  CStrings:  37227
 
Symbols:
+ +[INAppIntent INVCVoiceShortcutClientCreationBlock]
+ +[INAppIntent setINVCVoiceShortcutClientCreationBlock:]
+ +[INIntentCodableDescription(__Name) __NameKey].37617
+ -[INAppIntent isRetryableError:]
+ _AssistantServicesLibraryCore.frameworkLibrary.54945
+ _ChronoServicesLibraryCore.frameworkLibrary.123684
+ _ContactsLibrary.45497
+ _ContactsLibrary.60883
+ _ContactsLibraryCore.frameworkLibrary.111113
+ _ContactsLibraryCore.frameworkLibrary.45500
+ _ContactsLibraryCore.frameworkLibrary.60886
+ _CoreGraphicsLibrary.136721
+ _CoreGraphicsLibraryCore.frameworkLibrary.136726
+ _CoreSpotlightLibraryCore.frameworkLibrary.59716
+ _CoreSpotlightLibraryCore.frameworkLibrary.79779
+ _HealthKitLibraryCore.frameworkLibrary.95490
+ _IntentsUILibraryCore.frameworkLibrary.83652
+ _LinkServicesLibraryCore.frameworkLibrary.166029
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.113048
+ _VoiceShortcutClientLibraryCore.frameworkLibrary.123607
+ __INVCVoiceShortcutClientCreationBlock
+ __OBJC_$_CLASS_PROP_LIST_INAppIntent
+ ___62-[INIntentDeliverer _processIntent:intentResponse:completion:]_block_invoke.137
+ ___62-[INIntentDeliverer _processIntent:intentResponse:completion:]_block_invoke_2.140
+ ___AssistantServicesLibraryCore_block_invoke.54946
+ ___Block_byref_object_copy_.100534
+ ___Block_byref_object_copy_.104500
+ ___Block_byref_object_copy_.13079
+ ___Block_byref_object_copy_.20857
+ ___Block_byref_object_copy_.37076
+ ___Block_byref_object_copy_.49915
+ ___Block_byref_object_copy_.54534
+ ___Block_byref_object_copy_.54955
+ ___Block_byref_object_copy_.65243
+ ___Block_byref_object_copy_.68258
+ ___Block_byref_object_copy_.69067
+ ___Block_byref_object_copy_.71928
+ ___Block_byref_object_copy_.75141
+ ___Block_byref_object_copy_.90458
+ ___Block_byref_object_dispose_.100535
+ ___Block_byref_object_dispose_.104501
+ ___Block_byref_object_dispose_.13080
+ ___Block_byref_object_dispose_.20858
+ ___Block_byref_object_dispose_.37077
+ ___Block_byref_object_dispose_.49916
+ ___Block_byref_object_dispose_.54535
+ ___Block_byref_object_dispose_.54956
+ ___Block_byref_object_dispose_.65244
+ ___Block_byref_object_dispose_.68259
+ ___Block_byref_object_dispose_.69068
+ ___Block_byref_object_dispose_.71929
+ ___Block_byref_object_dispose_.75142
+ ___Block_byref_object_dispose_.90459
+ ___ChronoServicesLibraryCore_block_invoke.123685
+ ___ContactsLibraryCore_block_invoke.111114
+ ___ContactsLibraryCore_block_invoke.45501
+ ___ContactsLibraryCore_block_invoke.60887
+ ___CoreGraphicsLibraryCore_block_invoke.136727
+ ___CoreSpotlightLibraryCore_block_invoke.59717
+ ___CoreSpotlightLibraryCore_block_invoke.79780
+ ___HealthKitLibraryCore_block_invoke.95491
+ ___INFindMatchingAppsForIntent_block_invoke.216
+ ___IntentsUILibraryCore_block_invoke.83653
+ ___LinkServicesLibraryCore_block_invoke.166030
+ ___VoiceShortcutClientLibraryCore_block_invoke.113049
+ ___VoiceShortcutClientLibraryCore_block_invoke.123608
+ ___block_literal_global.10.103466
+ ___block_literal_global.10.54970
+ ___block_literal_global.100280
+ ___block_literal_global.100455
+ ___block_literal_global.102
+ ___block_literal_global.103456
+ ___block_literal_global.104601
+ ___block_literal_global.105617
+ ___block_literal_global.109
+ ___block_literal_global.11.111757
+ ___block_literal_global.111785
+ ___block_literal_global.119891
+ ___block_literal_global.12.158307
+ ___block_literal_global.123707
+ ___block_literal_global.13.103468
+ ___block_literal_global.13.98768
+ ___block_literal_global.13075
+ ___block_literal_global.158295
+ ___block_literal_global.20853
+ ___block_literal_global.21.59683
+ ___block_literal_global.22421
+ ___block_literal_global.227
+ ___block_literal_global.23234
+ ___block_literal_global.242
+ ___block_literal_global.3.111756
+ ___block_literal_global.332
+ ___block_literal_global.34335
+ ___block_literal_global.37098
+ ___block_literal_global.37489
+ ___block_literal_global.384
+ ___block_literal_global.40170
+ ___block_literal_global.40674
+ ___block_literal_global.42340
+ ___block_literal_global.43258
+ ___block_literal_global.43509
+ ___block_literal_global.44415
+ ___block_literal_global.47518
+ ___block_literal_global.5.94145
+ ___block_literal_global.53413
+ ___block_literal_global.53985
+ ___block_literal_global.54540
+ ___block_literal_global.54954
+ ___block_literal_global.59723
+ ___block_literal_global.6.111768
+ ___block_literal_global.6.72044
+ ___block_literal_global.60744
+ ___block_literal_global.62272
+ ___block_literal_global.66720
+ ___block_literal_global.68333
+ ___block_literal_global.68450
+ ___block_literal_global.69069
+ ___block_literal_global.70472
+ ___block_literal_global.71234
+ ___block_literal_global.71978
+ ___block_literal_global.72040
+ ___block_literal_global.75001
+ ___block_literal_global.77366
+ ___block_literal_global.82.66714
+ ___block_literal_global.82375
+ ___block_literal_global.91.71979
+ ___block_literal_global.91426
+ ___block_literal_global.92285
+ ___block_literal_global.94169
+ ___block_literal_global.98779
+ ___getAFPreferencesClass_block_invoke.54944
+ ___getCGColorCreateSRGBSymbolLoc_block_invoke.136772
+ ___getCGColorGetComponentsSymbolLoc_block_invoke.136720
+ ___getCNLabeledValueClass_block_invoke.60903
+ ___getCNPostalAddressClass_block_invoke.111112
+ ___getCSSearchableIndexClass_block_invoke.59715
+ ___getCSSearchableItemAttributeSetClass_block_invoke.79778
+ ___getHKUnitClass_block_invoke.95489
+ _audit_stringAssistantServices.54951
+ _audit_stringChronoServices.123690
+ _audit_stringContacts.111119
+ _audit_stringContacts.45503
+ _audit_stringContacts.60890
+ _audit_stringCoreGraphics.136729
+ _audit_stringCoreSpotlight.59722
+ _audit_stringCoreSpotlight.79785
+ _audit_stringHealthKit.95496
+ _audit_stringLinkServices.166035
+ _audit_stringVoiceShortcutClient.113054
+ _audit_stringVoiceShortcutClient.123613
+ _getAFPreferencesClass.softClass.54943
+ _getCGColorCreateSRGBSymbolLoc.ptr.136771
+ _getCGColorGetComponentsSymbolLoc.ptr.136719
+ _getCNLabeledValueClass.60868
+ _getCNLabeledValueClass.softClass.60902
+ _getCNPostalAddressClass.softClass.111111
+ _getCSSearchableIndexClass.softClass.59714
+ _getCSSearchableItemAttributeSetClass.softClass.79777
+ _getHKUnitClass.95487
+ _getHKUnitClass.softClass.95488
+ _intentDescription.intentDescription.39165
+ _intentDescription.intentDescription.42688
+ _intentDescription.intentDescription.64208
+ _intentDescription.intentDescription.68451
+ _intentDescription.onceToken.39164
+ _intentDescription.onceToken.42687
+ _intentDescription.onceToken.64207
+ _intentDescription.onceToken.68449
+ _objc_msgSend$INVCVoiceShortcutClientCreationBlock
+ _objc_msgSend$isRetryableError:
+ _serviceIdentifier.onceToken.83626
+ _serviceIdentifier.sServiceIdentifier.83627
+ _sharedCache.onceToken.82374
+ _sharedManager.onceToken.123706
+ _sharedManager.onceToken.59713
+ _sharedManager.sharedManager.123708
+ _sharedProvider.onceToken.158306
- +[INIntentCodableDescription(__Name) __NameKey].37615
- _AssistantServicesLibraryCore.frameworkLibrary.54944
- _ChronoServicesLibraryCore.frameworkLibrary.123625
- _ContactsLibrary.45495
- _ContactsLibrary.60882
- _ContactsLibraryCore.frameworkLibrary.111065
- _ContactsLibraryCore.frameworkLibrary.45498
- _ContactsLibraryCore.frameworkLibrary.60885
- _CoreGraphicsLibrary.136662
- _CoreGraphicsLibraryCore.frameworkLibrary.136667
- _CoreSpotlightLibraryCore.frameworkLibrary.59715
- _CoreSpotlightLibraryCore.frameworkLibrary.79775
- _HealthKitLibraryCore.frameworkLibrary.95482
- _IntentsUILibraryCore.frameworkLibrary.83647
- _LinkServicesLibraryCore.frameworkLibrary.165968
- _VoiceShortcutClientLibraryCore.frameworkLibrary.113000
- _VoiceShortcutClientLibraryCore.frameworkLibrary.123548
- ___62-[INIntentDeliverer _processIntent:intentResponse:completion:]_block_invoke.136
- ___62-[INIntentDeliverer _processIntent:intentResponse:completion:]_block_invoke_2.139
- ___AssistantServicesLibraryCore_block_invoke.54945
- ___Block_byref_object_copy_.100527
- ___Block_byref_object_copy_.104489
- ___Block_byref_object_copy_.13081
- ___Block_byref_object_copy_.20858
- ___Block_byref_object_copy_.37075
- ___Block_byref_object_copy_.49914
- ___Block_byref_object_copy_.54533
- ___Block_byref_object_copy_.54954
- ___Block_byref_object_copy_.65242
- ___Block_byref_object_copy_.68257
- ___Block_byref_object_copy_.69066
- ___Block_byref_object_copy_.71927
- ___Block_byref_object_copy_.75138
- ___Block_byref_object_copy_.90450
- ___Block_byref_object_dispose_.100528
- ___Block_byref_object_dispose_.104490
- ___Block_byref_object_dispose_.13082
- ___Block_byref_object_dispose_.20859
- ___Block_byref_object_dispose_.37076
- ___Block_byref_object_dispose_.49915
- ___Block_byref_object_dispose_.54534
- ___Block_byref_object_dispose_.54955
- ___Block_byref_object_dispose_.65243
- ___Block_byref_object_dispose_.68258
- ___Block_byref_object_dispose_.69067
- ___Block_byref_object_dispose_.71928
- ___Block_byref_object_dispose_.75139
- ___Block_byref_object_dispose_.90451
- ___ChronoServicesLibraryCore_block_invoke.123626
- ___ContactsLibraryCore_block_invoke.111066
- ___ContactsLibraryCore_block_invoke.45499
- ___ContactsLibraryCore_block_invoke.60886
- ___CoreGraphicsLibraryCore_block_invoke.136668
- ___CoreSpotlightLibraryCore_block_invoke.59716
- ___CoreSpotlightLibraryCore_block_invoke.79776
- ___HealthKitLibraryCore_block_invoke.95483
- ___INFindMatchingAppsForIntent_block_invoke.215
- ___IntentsUILibraryCore_block_invoke.83648
- ___LinkServicesLibraryCore_block_invoke.165969
- ___VoiceShortcutClientLibraryCore_block_invoke.113001
- ___VoiceShortcutClientLibraryCore_block_invoke.123549
- ___block_literal_global.10.103455
- ___block_literal_global.10.54969
- ___block_literal_global.100.75133
- ___block_literal_global.100273
- ___block_literal_global.100449
- ___block_literal_global.103445
- ___block_literal_global.104590
- ___block_literal_global.105606
- ___block_literal_global.108
- ___block_literal_global.11.111709
- ___block_literal_global.111737
- ___block_literal_global.119832
- ___block_literal_global.12.158247
- ___block_literal_global.123648
- ___block_literal_global.13.103457
- ___block_literal_global.13.98761
- ___block_literal_global.13077
- ___block_literal_global.158235
- ___block_literal_global.20854
- ___block_literal_global.21.59682
- ___block_literal_global.22422
- ___block_literal_global.226
- ___block_literal_global.23235
- ___block_literal_global.239
- ___block_literal_global.3.111708
- ___block_literal_global.331
- ___block_literal_global.34334
- ___block_literal_global.37097
- ___block_literal_global.37487
- ___block_literal_global.383
- ___block_literal_global.40168
- ___block_literal_global.40672
- ___block_literal_global.42338
- ___block_literal_global.43256
- ___block_literal_global.43507
- ___block_literal_global.44413
- ___block_literal_global.47516
- ___block_literal_global.5.94137
- ___block_literal_global.53412
- ___block_literal_global.53984
- ___block_literal_global.54539
- ___block_literal_global.54953
- ___block_literal_global.59722
- ___block_literal_global.6.111720
- ___block_literal_global.6.72043
- ___block_literal_global.60743
- ___block_literal_global.62271
- ___block_literal_global.66719
- ___block_literal_global.68332
- ___block_literal_global.68449
- ___block_literal_global.69068
- ___block_literal_global.70471
- ___block_literal_global.71233
- ___block_literal_global.71977
- ___block_literal_global.72039
- ___block_literal_global.74996
- ___block_literal_global.77363
- ___block_literal_global.82.66713
- ___block_literal_global.82371
- ___block_literal_global.91.71978
- ___block_literal_global.91418
- ___block_literal_global.92277
- ___block_literal_global.94161
- ___block_literal_global.98772
- ___getAFPreferencesClass_block_invoke.54943
- ___getCGColorCreateSRGBSymbolLoc_block_invoke.136713
- ___getCGColorGetComponentsSymbolLoc_block_invoke.136661
- ___getCNLabeledValueClass_block_invoke.60902
- ___getCNPostalAddressClass_block_invoke.111064
- ___getCSSearchableIndexClass_block_invoke.59714
- ___getCSSearchableItemAttributeSetClass_block_invoke.79774
- ___getHKUnitClass_block_invoke.95481
- _audit_stringAssistantServices.54950
- _audit_stringChronoServices.123631
- _audit_stringContacts.111071
- _audit_stringContacts.45501
- _audit_stringContacts.60889
- _audit_stringCoreGraphics.136670
- _audit_stringCoreSpotlight.59721
- _audit_stringCoreSpotlight.79781
- _audit_stringHealthKit.95488
- _audit_stringLinkServices.165974
- _audit_stringVoiceShortcutClient.113006
- _audit_stringVoiceShortcutClient.123554
- _getAFPreferencesClass.softClass.54942
- _getCGColorCreateSRGBSymbolLoc.ptr.136712
- _getCGColorGetComponentsSymbolLoc.ptr.136660
- _getCNLabeledValueClass.60867
- _getCNLabeledValueClass.softClass.60901
- _getCNPostalAddressClass.softClass.111063
- _getCSSearchableIndexClass.softClass.59713
- _getCSSearchableItemAttributeSetClass.softClass.79773
- _getHKUnitClass.95479
- _getHKUnitClass.softClass.95480
- _intentDescription.intentDescription.39163
- _intentDescription.intentDescription.42686
- _intentDescription.intentDescription.64207
- _intentDescription.intentDescription.68450
- _intentDescription.onceToken.39162
- _intentDescription.onceToken.42685
- _intentDescription.onceToken.64206
- _intentDescription.onceToken.68448
- _objc_msgSend$objectForInfoDictionaryKey:ofClass:
- _objc_msgSend$pluginKitProxyForIdentifier:
- _serviceIdentifier.onceToken.83621
- _serviceIdentifier.sServiceIdentifier.83622
- _sharedCache.onceToken.82370
- _sharedManager.onceToken.123647
- _sharedManager.onceToken.59712
- _sharedManager.sharedManager.123649
- _sharedProvider.onceToken.158246
CStrings:
+ "%s No linkAction due to XPC interruption %{public}@ - attempting a retry"
+ "%s Unable to get serialized parameters for %{public}@ due to XPC interruption %{public}@ - attempting a retry"
+ "-[INCodableCustomObjectAttribute _unsafeObjectClass]"
+ "-[INCodableCustomObjectAttribute objectClass]"
+ "INMediaItem *"
+ "INMediaSearch *"
+ "INMessage *"
+ "INPersonHandle *"
+ "INRecurrenceRule *"
+ "INSendMessageAttachment *"
+ "INVCVoiceShortcutClientCreationBlock"
+ "MediaItem"
+ "MediaSearch"
+ "Message"
+ "Message Attachment"
+ "NSPersonNameComponents"
+ "NSPersonNameComponents *"
+ "Person Handle"
+ "Person Name Components"
+ "Recurrence Rule"
+ "T@?,C"
+ "com.apple.Bridge"
+ "com.apple.TVRemote"
+ "com.apple.TVRemoteUIService.TVRemoteIntentExtension"
+ "isRetryableError:"
+ "setINVCVoiceShortcutClientCreationBlock:"
- "objectForInfoDictionaryKey:ofClass:"
- "pluginKitProxyForIdentifier:"

```
