## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

```diff

-3532.1.100.0.0
-  __TEXT.__text: 0x21cc00
+3532.3.0.0.0
+  __TEXT.__text: 0x21d454
   __TEXT.__auth_stubs: 0x35e0
   __TEXT.__init_offsets: 0xbc
-  __TEXT.__objc_methlist: 0x106c8
+  __TEXT.__objc_methlist: 0x10720
   __TEXT.__dlopen_cstrs: 0x781
   __TEXT.__const: 0x2d08
-  __TEXT.__cstring: 0x19b40
+  __TEXT.__cstring: 0x19c03
   __TEXT.__oslogstring: 0x4073
   __TEXT.__ustring: 0x3ca
-  __TEXT.__unwind_info: 0x6430
-  __TEXT.__objc_classname: 0x221f
-  __TEXT.__objc_methname: 0x30824
-  __TEXT.__objc_methtype: 0x66df
-  __TEXT.__objc_stubs: 0x21b80
-  __DATA_CONST.__got: 0x1748
-  __DATA_CONST.__const: 0x4e28
-  __DATA_CONST.__objc_classlist: 0x830
+  __TEXT.__unwind_info: 0x6448
+  __TEXT.__objc_classname: 0x2230
+  __TEXT.__objc_methname: 0x30a3d
+  __TEXT.__objc_methtype: 0x6796
+  __TEXT.__objc_stubs: 0x21cc0
+  __DATA_CONST.__got: 0x1760
+  __DATA_CONST.__const: 0x4e50
+  __DATA_CONST.__objc_classlist: 0x838
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d78
-  __DATA_CONST.__objc_superrefs: 0x710
+  __DATA_CONST.__objc_selrefs: 0x9dd8
+  __DATA_CONST.__objc_superrefs: 0x718
   __DATA_CONST.__objc_arraydata: 0xcb0
   __AUTH_CONST.__auth_got: 0x1af8
-  __AUTH_CONST.__const: 0x8588
-  __AUTH_CONST.__cfstring: 0x12820
-  __AUTH_CONST.__objc_const: 0x19fd0
+  __AUTH_CONST.__const: 0x85a8
+  __AUTH_CONST.__cfstring: 0x128a0
+  __AUTH_CONST.__objc_const: 0x1a0b8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x20d0
+  __AUTH.__objc_data: 0x2120
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x1278
+  __DATA.__objc_ivar: 0x1280
   __DATA.__data: 0x2280
-  __DATA.__bss: 0x1f08
+  __DATA.__bss: 0x1f18
   __DATA.__common: 0x408
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0xb0
-  __DATA_DIRTY.__bss: 0xb68
+  __DATA_DIRTY.__bss: 0xb78
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/Transliteration.framework/Transliteration
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 16CD9EC7-F7BF-301C-91FD-3917F82F9048
-  Functions: 10302
-  Symbols:   31009
-  CStrings:  14198
+  UUID: 1ED9E8A8-891E-3D4D-A4A7-A0B09B72C3CD
+  Functions: 10312
+  Symbols:   31056
+  CStrings:  14228
 
Symbols:
+ +[TIAppAutofillManager isSuggestingStrongPasswordsAvailableForApplicationFromAuditToken:]
+ +[TITrialMonitor sharedInstance]
+ -[TITrialManager monitor]
+ -[TITrialMonitor .cxx_destruct]
+ -[TITrialMonitor init]
+ -[TITrialMonitor updateValueForFactor:]
+ -[TITrialMonitor updateValues]
+ _CoreServicesLibraryCore.frameworkLibrary.9070
+ _KeyboardServicesLibrary.15042
+ _KeyboardServicesLibraryCore.frameworkLibrary.15044
+ _ManagedConfigurationLibrary.15031
+ _ManagedConfigurationLibraryCore.frameworkLibrary.15034
+ _OBJC_CLASS_$_TITrialMonitor
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_IVAR_$_TITrialManager._monitor
+ _OBJC_IVAR_$_TITrialMonitor._trialClient
+ _OBJC_METACLASS_$_TITrialMonitor
+ _SensorKitLibrary.19766
+ _SensorKitLibraryCore.frameworkLibrary.19769
+ _SpringBoardServicesLibraryCore.frameworkLibrary.19074
+ _TIKeyboardOutputInfoTypeExternalProviderBundleIDStr
+ _TIKeyboardOutputInfoTypeExternalProviderExtensionBundleIDStr
+ _TITrialMonitorOSLogFacility
+ _TITrialMonitorOSLogFacility.logFacility
+ _TITrialMonitorOSLogFacility.onceToken
+ __OBJC_$_CLASS_METHODS_TITrialMonitor
+ __OBJC_$_INSTANCE_METHODS_TITrialMonitor
+ __OBJC_$_INSTANCE_VARIABLES_TITrialMonitor
+ __OBJC_$_PROP_LIST_TITrialManager.138
+ __OBJC_CLASS_RO_$_TITrialMonitor
+ __OBJC_METACLASS_RO_$_TITrialMonitor
+ __ZL13kTITokenIDUNK.11986
+ __ZL13kTITokenIDUNK.12140
+ __ZL13kTITokenIDUNK.12365
+ __ZL13kTITokenIDUNK.12458
+ __ZL13kTITokenIDUNK.21286
+ __ZL13kTITokenIDUNK.24526
+ __ZL17__testingInstance.16152
+ __ZN2KBL26k_invalid_likelihood_valueE.10020
+ __ZN2KBL26k_invalid_likelihood_valueE.10613
+ __ZN2KBL26k_invalid_likelihood_valueE.10861
+ __ZN2KBL26k_invalid_likelihood_valueE.10890
+ __ZN2KBL26k_invalid_likelihood_valueE.11760
+ __ZN2KBL26k_invalid_likelihood_valueE.11965
+ __ZN2KBL26k_invalid_likelihood_valueE.12021
+ __ZN2KBL26k_invalid_likelihood_valueE.12476
+ __ZN2KBL26k_invalid_likelihood_valueE.12708
+ __ZN2KBL26k_invalid_likelihood_valueE.12930
+ __ZN2KBL26k_invalid_likelihood_valueE.1311
+ __ZN2KBL26k_invalid_likelihood_valueE.13585
+ __ZN2KBL26k_invalid_likelihood_valueE.15720
+ __ZN2KBL26k_invalid_likelihood_valueE.16390
+ __ZN2KBL26k_invalid_likelihood_valueE.16482
+ __ZN2KBL26k_invalid_likelihood_valueE.16487
+ __ZN2KBL26k_invalid_likelihood_valueE.18150
+ __ZN2KBL26k_invalid_likelihood_valueE.18389
+ __ZN2KBL26k_invalid_likelihood_valueE.1846
+ __ZN2KBL26k_invalid_likelihood_valueE.18796
+ __ZN2KBL26k_invalid_likelihood_valueE.18869
+ __ZN2KBL26k_invalid_likelihood_valueE.18934
+ __ZN2KBL26k_invalid_likelihood_valueE.18943
+ __ZN2KBL26k_invalid_likelihood_valueE.19721
+ __ZN2KBL26k_invalid_likelihood_valueE.21287
+ __ZN2KBL26k_invalid_likelihood_valueE.21317
+ __ZN2KBL26k_invalid_likelihood_valueE.2662
+ __ZN2KBL26k_invalid_likelihood_valueE.3315
+ __ZN2KBL26k_invalid_likelihood_valueE.3660
+ __ZN2KBL26k_invalid_likelihood_valueE.3698
+ __ZN2KBL26k_invalid_likelihood_valueE.3914
+ __ZN2KBL26k_invalid_likelihood_valueE.4020
+ __ZN2KBL26k_invalid_likelihood_valueE.4520
+ __ZN2KBL26k_invalid_likelihood_valueE.4613
+ __ZN2KBL26k_invalid_likelihood_valueE.4949
+ __ZN2KBL26k_invalid_likelihood_valueE.5075
+ __ZN2KBL26k_invalid_likelihood_valueE.5079
+ __ZN2KBL26k_invalid_likelihood_valueE.5166
+ __ZN2KBL26k_invalid_likelihood_valueE.5402
+ __ZN2KBL26k_invalid_likelihood_valueE.5503
+ __ZN2KBL26k_invalid_likelihood_valueE.6257
+ __ZN2KBL26k_invalid_likelihood_valueE.7454
+ __ZN2KBL26k_invalid_likelihood_valueE.831
+ __ZN2KBL26k_invalid_likelihood_valueE.9943
+ ___100-[TIAppAutofillManager generateAutofillFormCandidatesWithRenderTraits:withKeyboardState:completion:]_block_invoke.202
+ ___100-[TIAppAutofillManager generateAutofillFormCandidatesWithRenderTraits:withKeyboardState:completion:]_block_invoke_2.203
+ ___114-[TIAppAutofillManager generateAutofillFormSuggestedUsernameWithRenderTraits:withKeyboardState:completionHandler:]_block_invoke.304
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.321
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.326
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.331
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.357
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke_2.328
+ ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke_2.354
+ ___22-[TITrialMonitor init]_block_invoke
+ ___32+[TITrialMonitor sharedInstance]_block_invoke
+ ___68-[TIAppAutofillManager shouldAcceptAutofill:withPayload:completion:]_block_invoke.402
+ ___68-[TIAppAutofillManager shouldAcceptAutofill:withPayload:completion:]_block_invoke_2.403
+ ___70-[TIAppAutofillManager presentHideMyEmailUI:keyboardState:completion:]_block_invoke.409
+ ___Block_byref_object_copy_.10214
+ ___Block_byref_object_copy_.10596
+ ___Block_byref_object_copy_.10690
+ ___Block_byref_object_copy_.11463
+ ___Block_byref_object_copy_.11976
+ ___Block_byref_object_copy_.12461
+ ___Block_byref_object_copy_.12925
+ ___Block_byref_object_copy_.12960
+ ___Block_byref_object_copy_.13873
+ ___Block_byref_object_copy_.15605
+ ___Block_byref_object_copy_.1577
+ ___Block_byref_object_copy_.16338
+ ___Block_byref_object_copy_.17726
+ ___Block_byref_object_copy_.17834
+ ___Block_byref_object_copy_.18020
+ ___Block_byref_object_copy_.1825
+ ___Block_byref_object_copy_.18492
+ ___Block_byref_object_copy_.19530
+ ___Block_byref_object_copy_.1994
+ ___Block_byref_object_copy_.20044
+ ___Block_byref_object_copy_.20103
+ ___Block_byref_object_copy_.20186
+ ___Block_byref_object_copy_.20808
+ ___Block_byref_object_copy_.21273
+ ___Block_byref_object_copy_.21310
+ ___Block_byref_object_copy_.21748
+ ___Block_byref_object_copy_.22283
+ ___Block_byref_object_copy_.23439
+ ___Block_byref_object_copy_.2348
+ ___Block_byref_object_copy_.23571
+ ___Block_byref_object_copy_.23734
+ ___Block_byref_object_copy_.23905
+ ___Block_byref_object_copy_.24257
+ ___Block_byref_object_copy_.24511
+ ___Block_byref_object_copy_.2591
+ ___Block_byref_object_copy_.2709
+ ___Block_byref_object_copy_.3254
+ ___Block_byref_object_copy_.4225
+ ___Block_byref_object_copy_.473
+ ___Block_byref_object_copy_.5380
+ ___Block_byref_object_copy_.5829
+ ___Block_byref_object_copy_.6362
+ ___Block_byref_object_copy_.6510
+ ___Block_byref_object_copy_.7053
+ ___Block_byref_object_copy_.7418
+ ___Block_byref_object_copy_.7576
+ ___Block_byref_object_copy_.8023
+ ___Block_byref_object_copy_.824
+ ___Block_byref_object_copy_.8319
+ ___Block_byref_object_copy_.8466
+ ___Block_byref_object_copy_.9606
+ ___Block_byref_object_copy_.9893
+ ___Block_byref_object_dispose_.10215
+ ___Block_byref_object_dispose_.10597
+ ___Block_byref_object_dispose_.10691
+ ___Block_byref_object_dispose_.11464
+ ___Block_byref_object_dispose_.11977
+ ___Block_byref_object_dispose_.12462
+ ___Block_byref_object_dispose_.12926
+ ___Block_byref_object_dispose_.12961
+ ___Block_byref_object_dispose_.13874
+ ___Block_byref_object_dispose_.15606
+ ___Block_byref_object_dispose_.1578
+ ___Block_byref_object_dispose_.16339
+ ___Block_byref_object_dispose_.17727
+ ___Block_byref_object_dispose_.17835
+ ___Block_byref_object_dispose_.18021
+ ___Block_byref_object_dispose_.1826
+ ___Block_byref_object_dispose_.18493
+ ___Block_byref_object_dispose_.19531
+ ___Block_byref_object_dispose_.1995
+ ___Block_byref_object_dispose_.20045
+ ___Block_byref_object_dispose_.20104
+ ___Block_byref_object_dispose_.20187
+ ___Block_byref_object_dispose_.20809
+ ___Block_byref_object_dispose_.21274
+ ___Block_byref_object_dispose_.21311
+ ___Block_byref_object_dispose_.21749
+ ___Block_byref_object_dispose_.22284
+ ___Block_byref_object_dispose_.23440
+ ___Block_byref_object_dispose_.2349
+ ___Block_byref_object_dispose_.23572
+ ___Block_byref_object_dispose_.23735
+ ___Block_byref_object_dispose_.23906
+ ___Block_byref_object_dispose_.24258
+ ___Block_byref_object_dispose_.24512
+ ___Block_byref_object_dispose_.2592
+ ___Block_byref_object_dispose_.2710
+ ___Block_byref_object_dispose_.3255
+ ___Block_byref_object_dispose_.4226
+ ___Block_byref_object_dispose_.474
+ ___Block_byref_object_dispose_.5381
+ ___Block_byref_object_dispose_.5830
+ ___Block_byref_object_dispose_.6363
+ ___Block_byref_object_dispose_.6511
+ ___Block_byref_object_dispose_.7054
+ ___Block_byref_object_dispose_.7419
+ ___Block_byref_object_dispose_.7577
+ ___Block_byref_object_dispose_.8024
+ ___Block_byref_object_dispose_.825
+ ___Block_byref_object_dispose_.8320
+ ___Block_byref_object_dispose_.8467
+ ___Block_byref_object_dispose_.9607
+ ___Block_byref_object_dispose_.9894
+ ___CoreServicesLibraryCore_block_invoke.9071
+ ___KeyboardServicesLibraryCore_block_invoke.15045
+ ___ManagedConfigurationLibraryCore_block_invoke.15035
+ ___SensorKitLibraryCore_block_invoke.19770
+ ___SpringBoardServicesLibraryCore_block_invoke.19075
+ ___TITrialMonitorOSLogFacility_block_invoke
+ ___block_descriptor_104_a8_32s40s48s56r64w72c16_ZTSN2KB6StringE_e149_v44?0"TIAutocorrectionList"8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16B40l
+ ___block_descriptor_40_8_32w_e38_v16?0"<TRINamespaceUpdateProtocol>"8lw32l8
+ ___block_descriptor_99_8_32s40s48s56s64s72s80s88bs_e22_v20?0B8"LAContext"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_tmp.10594
+ ___block_descriptor_tmp.11.12024
+ ___block_descriptor_tmp.11.12460
+ ___block_descriptor_tmp.11.18165
+ ___block_descriptor_tmp.11958
+ ___block_descriptor_tmp.11978
+ ___block_descriptor_tmp.12366
+ ___block_descriptor_tmp.12388
+ ___block_descriptor_tmp.13.12385
+ ___block_descriptor_tmp.13.18168
+ ___block_descriptor_tmp.13391
+ ___block_descriptor_tmp.14.18167
+ ___block_descriptor_tmp.14030
+ ___block_descriptor_tmp.15.12463
+ ___block_descriptor_tmp.15.18166
+ ___block_descriptor_tmp.15607
+ ___block_descriptor_tmp.15635
+ ___block_descriptor_tmp.16604
+ ___block_descriptor_tmp.17750
+ ___block_descriptor_tmp.17836
+ ___block_descriptor_tmp.18173
+ ___block_descriptor_tmp.18860
+ ___block_descriptor_tmp.2.15611
+ ___block_descriptor_tmp.2.15647
+ ___block_descriptor_tmp.2.17728
+ ___block_descriptor_tmp.2.18177
+ ___block_descriptor_tmp.2.18861
+ ___block_descriptor_tmp.2.20046
+ ___block_descriptor_tmp.20048
+ ___block_descriptor_tmp.20068
+ ___block_descriptor_tmp.21312
+ ___block_descriptor_tmp.21750
+ ___block_descriptor_tmp.24.12378
+ ___block_descriptor_tmp.24289
+ ___block_descriptor_tmp.24513
+ ___block_descriptor_tmp.3.10598
+ ___block_descriptor_tmp.3.12466
+ ___block_descriptor_tmp.3.18180
+ ___block_descriptor_tmp.30.12389
+ ___block_descriptor_tmp.3670
+ ___block_descriptor_tmp.4.12387
+ ___block_descriptor_tmp.4.17731
+ ___block_descriptor_tmp.4.18183
+ ___block_descriptor_tmp.5.18876
+ ___block_descriptor_tmp.5.5156
+ ___block_descriptor_tmp.5157
+ ___block_descriptor_tmp.5382
+ ___block_descriptor_tmp.5486
+ ___block_descriptor_tmp.6.12012
+ ___block_descriptor_tmp.6.18190
+ ___block_descriptor_tmp.6.3676
+ ___block_descriptor_tmp.6.6250
+ ___block_descriptor_tmp.6249
+ ___block_descriptor_tmp.7.10590
+ ___block_descriptor_tmp.7.12456
+ ___block_descriptor_tmp.7.15609
+ ___block_descriptor_tmp.7.5123
+ ___block_descriptor_tmp.8.12454
+ ___block_descriptor_tmp.8.18187
+ ___block_descriptor_tmp.8.20052
+ ___block_descriptor_tmp.8016
+ ___block_descriptor_tmp.9.10586
+ ___block_descriptor_tmp.9.18186
+ ___block_descriptor_tmp.9.20056
+ ___block_descriptor_tmp.9933
+ ___block_literal_global.10.16717
+ ___block_literal_global.10271
+ ___block_literal_global.11670
+ ___block_literal_global.11985
+ ___block_literal_global.12126
+ ___block_literal_global.12357
+ ___block_literal_global.12362
+ ___block_literal_global.1251
+ ___block_literal_global.13.17059
+ ___block_literal_global.13022
+ ___block_literal_global.13389
+ ___block_literal_global.13578
+ ___block_literal_global.13966
+ ___block_literal_global.14028
+ ___block_literal_global.143
+ ___block_literal_global.14400
+ ___block_literal_global.15072
+ ___block_literal_global.15276
+ ___block_literal_global.15645
+ ___block_literal_global.15728
+ ___block_literal_global.158.6376
+ ___block_literal_global.15966
+ ___block_literal_global.16149
+ ___block_literal_global.16738
+ ___block_literal_global.16892
+ ___block_literal_global.17.14403
+ ___block_literal_global.17.15059
+ ___block_literal_global.17.16704
+ ___block_literal_global.17074
+ ___block_literal_global.17729
+ ___block_literal_global.17772
+ ___block_literal_global.17790
+ ___block_literal_global.1795
+ ___block_literal_global.18100
+ ___block_literal_global.18171
+ ___block_literal_global.18335
+ ___block_literal_global.1866
+ ___block_literal_global.18685
+ ___block_literal_global.19.12465
+ ___block_literal_global.19088
+ ___block_literal_global.19169
+ ___block_literal_global.19555
+ ___block_literal_global.19662
+ ___block_literal_global.20096
+ ___block_literal_global.2013
+ ___block_literal_global.20823
+ ___block_literal_global.21123
+ ___block_literal_global.2123
+ ___block_literal_global.21702
+ ___block_literal_global.21866
+ ___block_literal_global.22221
+ ___block_literal_global.2281
+ ___block_literal_global.23.17051
+ ___block_literal_global.23601
+ ___block_literal_global.23931
+ ___block_literal_global.23982
+ ___block_literal_global.24128
+ ___block_literal_global.24135
+ ___block_literal_global.24247
+ ___block_literal_global.24287
+ ___block_literal_global.2452
+ ___block_literal_global.2624
+ ___block_literal_global.2755
+ ___block_literal_global.290
+ ___block_literal_global.3.17069
+ ___block_literal_global.31.15274
+ ___block_literal_global.3102
+ ___block_literal_global.3652
+ ___block_literal_global.3749
+ ___block_literal_global.3769
+ ___block_literal_global.3999
+ ___block_literal_global.4089
+ ___block_literal_global.4105
+ ___block_literal_global.417
+ ___block_literal_global.4248
+ ___block_literal_global.4361
+ ___block_literal_global.46.24149
+ ___block_literal_global.4639
+ ___block_literal_global.48.24152
+ ___block_literal_global.5069
+ ___block_literal_global.540
+ ___block_literal_global.5484
+ ___block_literal_global.6075
+ ___block_literal_global.61.24169
+ ___block_literal_global.6209
+ ___block_literal_global.6375
+ ___block_literal_global.64.24174
+ ___block_literal_global.6669
+ ___block_literal_global.7172
+ ___block_literal_global.725
+ ___block_literal_global.7450
+ ___block_literal_global.7676
+ ___block_literal_global.7817
+ ___block_literal_global.79.24191
+ ___block_literal_global.8.17064
+ ___block_literal_global.82.24196
+ ___block_literal_global.8428
+ ___block_literal_global.87.16927
+ ___block_literal_global.87.19716
+ ___block_literal_global.8763
+ ___block_literal_global.88
+ ___block_literal_global.9095
+ ___block_literal_global.9189
+ ___block_literal_global.97.16918
+ ___block_literal_global.9897
+ ___getLSApplicationProxyClass_block_invoke.9052
+ ___getMCProfileConnectionClass_block_invoke.15028
+ ___testingInstance.21870
+ ___testingInstance.23928
+ ___testingInstance.3754
+ ___testingInstance.6671
+ ___testingInstance.7208
+ ___testingInstance.7679
+ _audit_stringCoreServices.9074
+ _audit_stringKeyboardServices.15047
+ _audit_stringManagedConfiguration.15037
+ _audit_stringSensorKit.19773
+ _audit_stringSpringBoardServices.19077
+ _getLSApplicationProxyClass.softClass.9051
+ _getMCProfileConnectionClass.softClass.15027
+ _objc_msgSend$addUpdateHandlerForNamespaceName:usingBlock:
+ _objc_msgSend$booleanValue
+ _objc_msgSend$canOfferToSuggestStrongPasswordsForApplicationFromAuditToken:
+ _objc_msgSend$client
+ _objc_msgSend$didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:
+ _objc_msgSend$externalProviderBundleID
+ _objc_msgSend$externalProviderExtensionBundleID
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$refresh
+ _objc_msgSend$updateValueForFactor:
+ _objc_msgSend$updateValues
+ _sharedInstance.instance.9096
+ _sharedInstance.onceToken.12356
+ _sharedInstance.onceToken.13965
+ _sharedInstance.onceToken.24127
+ _sharedInstance.onceToken.3165
+ _sharedInstance.onceToken.5273
+ _sharedInstance.onceToken.9094
+ _sharedInstance.result
+ _singletonInstance.onceToken.15071
+ _singletonInstance.onceToken.19554
+ _singletonInstance.onceToken.21865
+ _singletonInstance.onceToken.23930
+ _singletonInstance.onceToken.6668
+ _singletonInstance.onceToken.7675
+ _singletonInstance.singleton.19556
+ _singletonInstance.singletonInstance.15073
+ _singletonInstance.singletonInstance.21867
+ _singletonInstance.singletonInstance.23932
+ _singletonInstance.singletonInstance.7677
- +[TIAppAutofillManager isSuggestingStrongPasswordsAvailable]
- _CoreServicesLibraryCore.frameworkLibrary.9073
- _KeyboardServicesLibrary.15017
- _KeyboardServicesLibraryCore.frameworkLibrary.15019
- _ManagedConfigurationLibrary.15006
- _ManagedConfigurationLibraryCore.frameworkLibrary.15009
- _SensorKitLibrary.19737
- _SensorKitLibraryCore.frameworkLibrary.19740
- _SpringBoardServicesLibraryCore.frameworkLibrary.19045
- __OBJC_$_PROP_LIST_TITrialManager.132
- __ZL13kTITokenIDUNK.11975
- __ZL13kTITokenIDUNK.12129
- __ZL13kTITokenIDUNK.12354
- __ZL13kTITokenIDUNK.12447
- __ZL13kTITokenIDUNK.21250
- __ZL13kTITokenIDUNK.24481
- __ZL17__testingInstance.16125
- __ZN2KBL26k_invalid_likelihood_valueE.10024
- __ZN2KBL26k_invalid_likelihood_valueE.10616
- __ZN2KBL26k_invalid_likelihood_valueE.10864
- __ZN2KBL26k_invalid_likelihood_valueE.10893
- __ZN2KBL26k_invalid_likelihood_valueE.11750
- __ZN2KBL26k_invalid_likelihood_valueE.11954
- __ZN2KBL26k_invalid_likelihood_valueE.12010
- __ZN2KBL26k_invalid_likelihood_valueE.12465
- __ZN2KBL26k_invalid_likelihood_valueE.12697
- __ZN2KBL26k_invalid_likelihood_valueE.12919
- __ZN2KBL26k_invalid_likelihood_valueE.1306
- __ZN2KBL26k_invalid_likelihood_valueE.13567
- __ZN2KBL26k_invalid_likelihood_valueE.15696
- __ZN2KBL26k_invalid_likelihood_valueE.16363
- __ZN2KBL26k_invalid_likelihood_valueE.16455
- __ZN2KBL26k_invalid_likelihood_valueE.16460
- __ZN2KBL26k_invalid_likelihood_valueE.18121
- __ZN2KBL26k_invalid_likelihood_valueE.18360
- __ZN2KBL26k_invalid_likelihood_valueE.1869
- __ZN2KBL26k_invalid_likelihood_valueE.18767
- __ZN2KBL26k_invalid_likelihood_valueE.18840
- __ZN2KBL26k_invalid_likelihood_valueE.18905
- __ZN2KBL26k_invalid_likelihood_valueE.18914
- __ZN2KBL26k_invalid_likelihood_valueE.19692
- __ZN2KBL26k_invalid_likelihood_valueE.21251
- __ZN2KBL26k_invalid_likelihood_valueE.21281
- __ZN2KBL26k_invalid_likelihood_valueE.2687
- __ZN2KBL26k_invalid_likelihood_valueE.3361
- __ZN2KBL26k_invalid_likelihood_valueE.3706
- __ZN2KBL26k_invalid_likelihood_valueE.3744
- __ZN2KBL26k_invalid_likelihood_valueE.3961
- __ZN2KBL26k_invalid_likelihood_valueE.4067
- __ZN2KBL26k_invalid_likelihood_valueE.4567
- __ZN2KBL26k_invalid_likelihood_valueE.4660
- __ZN2KBL26k_invalid_likelihood_valueE.4965
- __ZN2KBL26k_invalid_likelihood_valueE.5091
- __ZN2KBL26k_invalid_likelihood_valueE.5095
- __ZN2KBL26k_invalid_likelihood_valueE.5182
- __ZN2KBL26k_invalid_likelihood_valueE.5381
- __ZN2KBL26k_invalid_likelihood_valueE.5482
- __ZN2KBL26k_invalid_likelihood_valueE.6236
- __ZN2KBL26k_invalid_likelihood_valueE.7458
- __ZN2KBL26k_invalid_likelihood_valueE.821
- __ZN2KBL26k_invalid_likelihood_valueE.9947
- ___100-[TIAppAutofillManager generateAutofillFormCandidatesWithRenderTraits:withKeyboardState:completion:]_block_invoke.198
- ___100-[TIAppAutofillManager generateAutofillFormCandidatesWithRenderTraits:withKeyboardState:completion:]_block_invoke_2.199
- ___114-[TIAppAutofillManager generateAutofillFormSuggestedUsernameWithRenderTraits:withKeyboardState:completionHandler:]_block_invoke.300
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.317
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.322
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.327
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke.349
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke_2.324
- ___199-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke_2.350
- ___68-[TIAppAutofillManager shouldAcceptAutofill:withPayload:completion:]_block_invoke.396
- ___68-[TIAppAutofillManager shouldAcceptAutofill:withPayload:completion:]_block_invoke_2.397
- ___70-[TIAppAutofillManager presentHideMyEmailUI:keyboardState:completion:]_block_invoke.403
- ___Block_byref_object_copy_.10217
- ___Block_byref_object_copy_.10599
- ___Block_byref_object_copy_.10693
- ___Block_byref_object_copy_.11451
- ___Block_byref_object_copy_.11965
- ___Block_byref_object_copy_.12450
- ___Block_byref_object_copy_.12914
- ___Block_byref_object_copy_.12949
- ___Block_byref_object_copy_.13855
- ___Block_byref_object_copy_.15581
- ___Block_byref_object_copy_.1572
- ___Block_byref_object_copy_.16311
- ___Block_byref_object_copy_.17698
- ___Block_byref_object_copy_.17805
- ___Block_byref_object_copy_.17991
- ___Block_byref_object_copy_.18463
- ___Block_byref_object_copy_.1847
- ___Block_byref_object_copy_.19501
- ___Block_byref_object_copy_.20014
- ___Block_byref_object_copy_.20073
- ___Block_byref_object_copy_.20156
- ___Block_byref_object_copy_.2019
- ___Block_byref_object_copy_.20778
- ___Block_byref_object_copy_.21237
- ___Block_byref_object_copy_.21274
- ___Block_byref_object_copy_.21712
- ___Block_byref_object_copy_.22247
- ___Block_byref_object_copy_.23396
- ___Block_byref_object_copy_.23529
- ___Block_byref_object_copy_.23692
- ___Block_byref_object_copy_.2373
- ___Block_byref_object_copy_.23863
- ___Block_byref_object_copy_.24212
- ___Block_byref_object_copy_.24466
- ___Block_byref_object_copy_.2616
- ___Block_byref_object_copy_.2734
- ___Block_byref_object_copy_.3300
- ___Block_byref_object_copy_.4272
- ___Block_byref_object_copy_.454
- ___Block_byref_object_copy_.5359
- ___Block_byref_object_copy_.5808
- ___Block_byref_object_copy_.6341
- ___Block_byref_object_copy_.6482
- ___Block_byref_object_copy_.7036
- ___Block_byref_object_copy_.7422
- ___Block_byref_object_copy_.7580
- ___Block_byref_object_copy_.8026
- ___Block_byref_object_copy_.814
- ___Block_byref_object_copy_.8322
- ___Block_byref_object_copy_.8469
- ___Block_byref_object_copy_.9609
- ___Block_byref_object_copy_.9897
- ___Block_byref_object_dispose_.10218
- ___Block_byref_object_dispose_.10600
- ___Block_byref_object_dispose_.10694
- ___Block_byref_object_dispose_.11452
- ___Block_byref_object_dispose_.11966
- ___Block_byref_object_dispose_.12451
- ___Block_byref_object_dispose_.12915
- ___Block_byref_object_dispose_.12950
- ___Block_byref_object_dispose_.13856
- ___Block_byref_object_dispose_.15582
- ___Block_byref_object_dispose_.1573
- ___Block_byref_object_dispose_.16312
- ___Block_byref_object_dispose_.17699
- ___Block_byref_object_dispose_.17806
- ___Block_byref_object_dispose_.17992
- ___Block_byref_object_dispose_.18464
- ___Block_byref_object_dispose_.1848
- ___Block_byref_object_dispose_.19502
- ___Block_byref_object_dispose_.20015
- ___Block_byref_object_dispose_.20074
- ___Block_byref_object_dispose_.20157
- ___Block_byref_object_dispose_.2020
- ___Block_byref_object_dispose_.20779
- ___Block_byref_object_dispose_.21238
- ___Block_byref_object_dispose_.21275
- ___Block_byref_object_dispose_.21713
- ___Block_byref_object_dispose_.22248
- ___Block_byref_object_dispose_.23397
- ___Block_byref_object_dispose_.23530
- ___Block_byref_object_dispose_.23693
- ___Block_byref_object_dispose_.2374
- ___Block_byref_object_dispose_.23864
- ___Block_byref_object_dispose_.24213
- ___Block_byref_object_dispose_.24467
- ___Block_byref_object_dispose_.2617
- ___Block_byref_object_dispose_.2735
- ___Block_byref_object_dispose_.3301
- ___Block_byref_object_dispose_.4273
- ___Block_byref_object_dispose_.455
- ___Block_byref_object_dispose_.5360
- ___Block_byref_object_dispose_.5809
- ___Block_byref_object_dispose_.6342
- ___Block_byref_object_dispose_.6483
- ___Block_byref_object_dispose_.7037
- ___Block_byref_object_dispose_.7423
- ___Block_byref_object_dispose_.7581
- ___Block_byref_object_dispose_.8027
- ___Block_byref_object_dispose_.815
- ___Block_byref_object_dispose_.8323
- ___Block_byref_object_dispose_.8470
- ___Block_byref_object_dispose_.9610
- ___Block_byref_object_dispose_.9898
- ___CoreServicesLibraryCore_block_invoke.9074
- ___KeyboardServicesLibraryCore_block_invoke.15020
- ___ManagedConfigurationLibraryCore_block_invoke.15010
- ___SensorKitLibraryCore_block_invoke.19741
- ___SpringBoardServicesLibraryCore_block_invoke.19046
- ___block_descriptor_104_a8_32s40s48s56r64w72c16_ZTSN2KB6StringE_e145_v44?0"TIAutocorrectionList"8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16B40l
- ___block_descriptor_75_8_32s40s48s56s64bs_e22_v20?0B8"LAContext"12ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_tmp.10597
- ___block_descriptor_tmp.11.12013
- ___block_descriptor_tmp.11.12449
- ___block_descriptor_tmp.11.18136
- ___block_descriptor_tmp.11947
- ___block_descriptor_tmp.11967
- ___block_descriptor_tmp.12355
- ___block_descriptor_tmp.12377
- ___block_descriptor_tmp.13.12374
- ___block_descriptor_tmp.13.18139
- ___block_descriptor_tmp.13373
- ___block_descriptor_tmp.14.18138
- ___block_descriptor_tmp.14012
- ___block_descriptor_tmp.15.12452
- ___block_descriptor_tmp.15.18137
- ___block_descriptor_tmp.15583
- ___block_descriptor_tmp.15611
- ___block_descriptor_tmp.16577
- ___block_descriptor_tmp.17722
- ___block_descriptor_tmp.17807
- ___block_descriptor_tmp.18144
- ___block_descriptor_tmp.18831
- ___block_descriptor_tmp.2.15587
- ___block_descriptor_tmp.2.15623
- ___block_descriptor_tmp.2.17700
- ___block_descriptor_tmp.2.18148
- ___block_descriptor_tmp.2.18832
- ___block_descriptor_tmp.2.20016
- ___block_descriptor_tmp.20018
- ___block_descriptor_tmp.20038
- ___block_descriptor_tmp.21276
- ___block_descriptor_tmp.21714
- ___block_descriptor_tmp.24.12367
- ___block_descriptor_tmp.24244
- ___block_descriptor_tmp.24468
- ___block_descriptor_tmp.3.10601
- ___block_descriptor_tmp.3.12455
- ___block_descriptor_tmp.3.18151
- ___block_descriptor_tmp.30.12378
- ___block_descriptor_tmp.3716
- ___block_descriptor_tmp.4.12376
- ___block_descriptor_tmp.4.17703
- ___block_descriptor_tmp.4.18154
- ___block_descriptor_tmp.5.18847
- ___block_descriptor_tmp.5.5172
- ___block_descriptor_tmp.5173
- ___block_descriptor_tmp.5361
- ___block_descriptor_tmp.5465
- ___block_descriptor_tmp.6.12001
- ___block_descriptor_tmp.6.18161
- ___block_descriptor_tmp.6.3722
- ___block_descriptor_tmp.6.6229
- ___block_descriptor_tmp.6228
- ___block_descriptor_tmp.7.10593
- ___block_descriptor_tmp.7.12445
- ___block_descriptor_tmp.7.15585
- ___block_descriptor_tmp.7.5139
- ___block_descriptor_tmp.8.12443
- ___block_descriptor_tmp.8.18158
- ___block_descriptor_tmp.8.20022
- ___block_descriptor_tmp.8019
- ___block_descriptor_tmp.9.10589
- ___block_descriptor_tmp.9.18157
- ___block_descriptor_tmp.9.20026
- ___block_descriptor_tmp.9937
- ___block_literal_global.10.16690
- ___block_literal_global.10274
- ___block_literal_global.11663
- ___block_literal_global.11974
- ___block_literal_global.12115
- ___block_literal_global.12346
- ___block_literal_global.12351
- ___block_literal_global.1246
- ___block_literal_global.13.17032
- ___block_literal_global.13011
- ___block_literal_global.13371
- ___block_literal_global.13560
- ___block_literal_global.137
- ___block_literal_global.13948
- ___block_literal_global.14010
- ___block_literal_global.14382
- ___block_literal_global.15047
- ___block_literal_global.15251
- ___block_literal_global.15621
- ___block_literal_global.15704
- ___block_literal_global.158.6355
- ___block_literal_global.15939
- ___block_literal_global.16122
- ___block_literal_global.16711
- ___block_literal_global.16865
- ___block_literal_global.17.14385
- ___block_literal_global.17.15034
- ___block_literal_global.17.16677
- ___block_literal_global.17047
- ___block_literal_global.17701
- ___block_literal_global.17744
- ___block_literal_global.17761
- ___block_literal_global.1797
- ___block_literal_global.18071
- ___block_literal_global.18142
- ___block_literal_global.18306
- ___block_literal_global.18656
- ___block_literal_global.1889
- ___block_literal_global.19.12454
- ___block_literal_global.19059
- ___block_literal_global.19140
- ___block_literal_global.19526
- ___block_literal_global.19633
- ___block_literal_global.20036
- ___block_literal_global.2038
- ___block_literal_global.20793
- ___block_literal_global.21087
- ___block_literal_global.2148
- ___block_literal_global.21666
- ___block_literal_global.21830
- ___block_literal_global.22185
- ___block_literal_global.23.17024
- ___block_literal_global.2306
- ___block_literal_global.23559
- ___block_literal_global.23889
- ___block_literal_global.23940
- ___block_literal_global.24086
- ___block_literal_global.24093
- ___block_literal_global.24202
- ___block_literal_global.24242
- ___block_literal_global.2477
- ___block_literal_global.2649
- ___block_literal_global.2780
- ___block_literal_global.286
- ___block_literal_global.3.17042
- ___block_literal_global.31.15249
- ___block_literal_global.3158
- ___block_literal_global.3698
- ___block_literal_global.3795
- ___block_literal_global.3815
- ___block_literal_global.399
- ___block_literal_global.4046
- ___block_literal_global.4136
- ___block_literal_global.4152
- ___block_literal_global.4295
- ___block_literal_global.4408
- ___block_literal_global.46.24107
- ___block_literal_global.4683
- ___block_literal_global.48.24110
- ___block_literal_global.5085
- ___block_literal_global.519
- ___block_literal_global.5463
- ___block_literal_global.6054
- ___block_literal_global.61.24127
- ___block_literal_global.6188
- ___block_literal_global.6354
- ___block_literal_global.64.24132
- ___block_literal_global.6638
- ___block_literal_global.715
- ___block_literal_global.7176
- ___block_literal_global.7454
- ___block_literal_global.7680
- ___block_literal_global.7820
- ___block_literal_global.79.24149
- ___block_literal_global.8.17037
- ___block_literal_global.82.24154
- ___block_literal_global.8431
- ___block_literal_global.87.16900
- ___block_literal_global.87.19687
- ___block_literal_global.8766
- ___block_literal_global.9098
- ___block_literal_global.9192
- ___block_literal_global.97.16891
- ___block_literal_global.9901
- ___getLSApplicationProxyClass_block_invoke.9055
- ___getMCProfileConnectionClass_block_invoke.15003
- ___testingInstance.21834
- ___testingInstance.23886
- ___testingInstance.3800
- ___testingInstance.6640
- ___testingInstance.7212
- ___testingInstance.7683
- _audit_stringCoreServices.9077
- _audit_stringKeyboardServices.15022
- _audit_stringManagedConfiguration.15012
- _audit_stringSensorKit.19744
- _audit_stringSpringBoardServices.19048
- _getLSApplicationProxyClass.softClass.9054
- _getMCProfileConnectionClass.softClass.15002
- _objc_msgSend$isFeatureEnabledForInternalBuilds
- _sharedInstance.instance.9099
- _sharedInstance.onceToken.12345
- _sharedInstance.onceToken.13947
- _sharedInstance.onceToken.24085
- _sharedInstance.onceToken.3210
- _sharedInstance.onceToken.9097
- _singletonInstance.onceToken.15046
- _singletonInstance.onceToken.19525
- _singletonInstance.onceToken.21829
- _singletonInstance.onceToken.23888
- _singletonInstance.onceToken.6637
- _singletonInstance.onceToken.7679
- _singletonInstance.singleton.19527
- _singletonInstance.singletonInstance.15048
- _singletonInstance.singletonInstance.21831
- _singletonInstance.singletonInstance.23890
- _singletonInstance.singletonInstance.7681
CStrings:
+ "%s Updating factor: %@ %d"
+ "-[TITrialMonitor updateValueForFactor:]"
+ "@\"TITrialMonitor\""
+ "@\"TRIClient\""
+ "@152@0:8{CandidateCollection={vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}iI}16{String=SSSC*[16c]}120"
+ "B48@0:8{?=[8I]}16"
+ "GENMOJI_GROWTH"
+ "I256@0:8{Word={String=SSSC*[16c]}{ByteString=(?={?=S*}{?=S[14C]})}fff{String=SSSC*[16c]}ffIQIIII{TITokenID=II}iQ{String=SSSC*[16c]}B{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<unsigned long long, void *> *>=^v}}{?=Q}{?=f}}}}16"
+ "IsMixmojiSuggestionsEnabled"
+ "T@\"TITrialMonitor\",R,V_monitor"
+ "TITrialMonitor"
+ "_monitor"
+ "_trialClient"
+ "addUpdateHandlerForNamespaceName:usingBlock:"
+ "booleanValue"
+ "canOfferToSuggestStrongPasswordsForApplicationFromAuditToken:"
+ "client"
+ "didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:"
+ "externalProviderBundleID"
+ "externalProviderExtensionBundleID"
+ "isMixmojiSuggestionsEnabled"
+ "isSuggestingStrongPasswordsAvailableForApplicationFromAuditToken:"
+ "levelForFactor:withNamespaceName:"
+ "monitor"
+ "refresh"
+ "updateValueForFactor:"
+ "updateValues"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
+ "v44@?0@\"TIAutocorrectionList\"8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16B40"
+ "{CandidateCollection={vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}{?=^{Candidate}}}iI}16@0:8"
+ "{LanguageModelContext={shared_ptr<std::vector<KB::LanguageModelContext>>=^v^{__shared_weak_count}}{vector<TITokenID, std::allocator<TITokenID>>=^{TITokenID}^{TITokenID}{?=^{TITokenID}}}QQQ{LinguisticContext={unique_ptr<language_modeling::LinguisticContextImpl, std::default_delete<language_modeling::LinguisticContextImpl>>={?=^{LinguisticContextImpl}}}}{LinguisticContext={unique_ptr<language_modeling::LinguisticContextImpl, std::default_delete<language_modeling::LinguisticContextImpl>>={?=^{LinguisticContextImpl}}}}{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}}32@0:8@16@24"
+ "{PathResampler=\"m_params\"{PathResamplerParams=\"segment_length\"d\"inflection_point_detection_mode\"i\"inflection_point_type\"i\"should_downsample\"B\"minimum_pause_length\"d\"should_flush_on_pause\"B}\"m_resampled_path\"{Path=\"m_samples\"{vector<TI::CP::PathSample, std::allocator<TI::CP::PathSample>>=\"__begin_\"^{PathSample}\"__end_\"^{PathSample}\"\"{?=\"__cap_\"^{PathSample}}}\"m_inflection_points\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}}\"m_raw_path\"{Path=\"m_samples\"{vector<TI::CP::PathSample, std::allocator<TI::CP::PathSample>>=\"__begin_\"^{PathSample}\"__end_\"^{PathSample}\"\"{?=\"__cap_\"^{PathSample}}}\"m_inflection_points\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}}\"m_is_final\"B\"m_processed_sample_count\"I\"m_retroactively_processed_sample_count\"I}"
+ "{unique_ptr<KB::StaticDictionary, std::default_delete<KB::StaticDictionary>>=\"\"{?=\"__ptr_\"^{StaticDictionary}}}"
+ "{unique_ptr<TI::RejectionsDatabase, std::default_delete<TI::RejectionsDatabase>>=\"\"{?=\"__ptr_\"^{RejectionsDatabase}}}"
+ "{vector<KB::LexiconInfo, std::allocator<KB::LexiconInfo>>=^{?}^{?}{?=^{?}}}16@0:8"
+ "{vector<RecentMessage, std::allocator<RecentMessage>>=\"__begin_\"^{RecentMessage}\"__end_\"^{RecentMessage}\"\"{?=\"__cap_\"^{RecentMessage}}}"
+ "{vector<TITokenID, std::allocator<TITokenID>>=\"__begin_\"^{TITokenID}\"__end_\"^{TITokenID}\"\"{?=\"__cap_\"^{TITokenID}}}"
+ "{vector<float, std::allocator<float>>=^f^f{?=^f}}24@0:8^v16"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}16@0:8"
+ "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}"
- "@152@0:8{CandidateCollection={vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}iI}16{String=SSSC*[16c]}120"
- "I256@0:8{Word={String=SSSC*[16c]}{ByteString=(?={?=S*}{?=S[14C]})}fff{String=SSSC*[16c]}ffIQIIII{TITokenID=II}iQ{String=SSSC*[16c]}B{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<unsigned long long, void *> *>=^v}Qf}}}16"
- "isFeatureEnabledForInternalBuilds"
- "v44@?0@\"TIAutocorrectionList\"8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16B40"
- "{CandidateCollection={vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}{vector<KB::Candidate, std::allocator<KB::Candidate>>=^{Candidate}^{Candidate}^{Candidate}}iI}16@0:8"
- "{LanguageModelContext={shared_ptr<std::vector<KB::LanguageModelContext>>=^v^{__shared_weak_count}}{vector<TITokenID, std::allocator<TITokenID>>=^{TITokenID}^{TITokenID}^{TITokenID}}QQQ{LinguisticContext={unique_ptr<language_modeling::LinguisticContextImpl, std::default_delete<language_modeling::LinguisticContextImpl>>=^{LinguisticContextImpl}}}{LinguisticContext={unique_ptr<language_modeling::LinguisticContextImpl, std::default_delete<language_modeling::LinguisticContextImpl>>=^{LinguisticContextImpl}}}{vector<std::string, std::allocator<std::string>>=^v^v^v}}32@0:8@16@24"
- "{PathResampler=\"m_params\"{PathResamplerParams=\"segment_length\"d\"inflection_point_detection_mode\"i\"inflection_point_type\"i\"should_downsample\"B\"minimum_pause_length\"d\"should_flush_on_pause\"B}\"m_resampled_path\"{Path=\"m_samples\"{vector<TI::CP::PathSample, std::allocator<TI::CP::PathSample>>=\"__begin_\"^{PathSample}\"__end_\"^{PathSample}\"__cap_\"^{PathSample}}\"m_inflection_points\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}}\"m_raw_path\"{Path=\"m_samples\"{vector<TI::CP::PathSample, std::allocator<TI::CP::PathSample>>=\"__begin_\"^{PathSample}\"__end_\"^{PathSample}\"__cap_\"^{PathSample}}\"m_inflection_points\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}}\"m_is_final\"B\"m_processed_sample_count\"I\"m_retroactively_processed_sample_count\"I}"
- "{unique_ptr<KB::StaticDictionary, std::default_delete<KB::StaticDictionary>>=\"__ptr_\"^{StaticDictionary}}"
- "{unique_ptr<TI::RejectionsDatabase, std::default_delete<TI::RejectionsDatabase>>=\"__ptr_\"^{RejectionsDatabase}}"
- "{vector<KB::LexiconInfo, std::allocator<KB::LexiconInfo>>=^{?}^{?}^{?}}16@0:8"
- "{vector<RecentMessage, std::allocator<RecentMessage>>=\"__begin_\"^{RecentMessage}\"__end_\"^{RecentMessage}\"__cap_\"^{RecentMessage}}"
- "{vector<TITokenID, std::allocator<TITokenID>>=\"__begin_\"^{TITokenID}\"__end_\"^{TITokenID}\"__cap_\"^{TITokenID}}"
- "{vector<float, std::allocator<float>>=^f^f^f}24@0:8^v16"
- "{vector<std::string, std::allocator<std::string>>=^v^v^v}16@0:8"
- "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"

```
