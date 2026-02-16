## ContactsUI

> `/System/Library/Frameworks/ContactsUI.framework/ContactsUI`

```diff

-1424.400.11.0.0
-  __TEXT.__text: 0x381f08
-  __TEXT.__auth_stubs: 0x56b0
-  __TEXT.__objc_methlist: 0x38d9c
+1424.500.142.0.0
+  __TEXT.__text: 0x3c6210
+  __TEXT.__auth_stubs: 0x5830
+  __TEXT.__objc_methlist: 0x38f54
   __TEXT.__dlopen_cstrs: 0x183b
-  __TEXT.__const: 0xd668
-  __TEXT.__cstring: 0x16d96
-  __TEXT.__oslogstring: 0xa725
-  __TEXT.__swift5_typeref: 0xff5a
-  __TEXT.__constg_swiftt: 0x5a40
-  __TEXT.__swift5_reflstr: 0x3a61
-  __TEXT.__swift5_fieldmd: 0x3824
-  __TEXT.__swift5_builtin: 0x230
-  __TEXT.__swift5_assocty: 0xfe0
-  __TEXT.__swift5_capture: 0x1380
-  __TEXT.__swift5_proto: 0x498
-  __TEXT.__swift5_types: 0x418
+  __TEXT.__const: 0xd9c8
+  __TEXT.__oslogstring: 0xa87c
+  __TEXT.__swift5_typeref: 0xff1a
+  __TEXT.__cstring: 0x136ad
+  __TEXT.__constg_swiftt: 0x5cfc
+  __TEXT.__swift5_reflstr: 0x3ae1
+  __TEXT.__swift5_fieldmd: 0x388c
+  __TEXT.__swift5_builtin: 0x244
+  __TEXT.__swift5_assocty: 0x1010
+  __TEXT.__swift5_capture: 0x13c0
+  __TEXT.__swift5_proto: 0x4bc
+  __TEXT.__swift5_types: 0x424
+  __TEXT.__swift5_protos: 0x18
   __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x94
+  __TEXT.__swift_as_ret: 0x98
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x376c
+  __TEXT.__gcc_except_tab: 0x34fc
   __TEXT.__ustring: 0x79a
-  __TEXT.__unwind_info: 0xde80
-  __TEXT.__eh_frame: 0x2408
-  __TEXT.__objc_classname: 0x747a
-  __TEXT.__objc_methname: 0x7a453
-  __TEXT.__objc_methtype: 0x1068a
-  __TEXT.__objc_stubs: 0x4fc40
-  __DATA_CONST.__got: 0x28b0
-  __DATA_CONST.__const: 0x66f8
-  __DATA_CONST.__objc_classlist: 0x1768
+  __TEXT.__unwind_info: 0x10fa0
+  __TEXT.__eh_frame: 0x24ac
+  __TEXT.__objc_classname: 0x88dc
+  __TEXT.__objc_methname: 0x7ca70
+  __TEXT.__objc_methtype: 0x1125a
+  __TEXT.__objc_stubs: 0x51760
+  __DATA_CONST.__got: 0x2910
+  __DATA_CONST.__const: 0x67b0
+  __DATA_CONST.__objc_classlist: 0x1778
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x978
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18188
+  __DATA_CONST.__objc_selrefs: 0x182d8
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0xf28
-  __DATA_CONST.__objc_arraydata: 0x5d8
-  __AUTH_CONST.__auth_got: 0x2b68
-  __AUTH_CONST.__const: 0xa6d0
-  __AUTH_CONST.__cfstring: 0xb940
-  __AUTH_CONST.__objc_const: 0x58b78
+  __DATA_CONST.__objc_arraydata: 0x5f0
+  __AUTH_CONST.__auth_got: 0x2c28
+  __AUTH_CONST.__const: 0xa790
+  __AUTH_CONST.__cfstring: 0xb9e0
+  __AUTH_CONST.__objc_const: 0x58ec0
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xf980
-  __AUTH.__data: 0x3940
-  __DATA.__objc_ivar: 0x3bc8
-  __DATA.__data: 0xafc8
-  __DATA.__bss: 0xadf8
-  __DATA.__common: 0x330
-  __DATA_DIRTY.__objc_data: 0x2290
-  __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x140
+  __AUTH.__objc_data: 0xfa30
+  __AUTH.__data: 0x3b40
+  __DATA.__objc_ivar: 0x3be4
+  __DATA.__data: 0xb008
+  __DATA.__bss: 0xb2b8
+  __DATA.__common: 0x338
+  __DATA_DIRTY.__objc_data: 0x22a0
+  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__bss: 0x148
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4702E6E2-CC7F-3DB7-BDAB-9C48B50999B2
-  Functions: 24393
-  Symbols:   64280
-  CStrings:  24961
+  UUID: DC4AF6CD-8625-310E-86EB-845E467C56E2
+  Functions: 24512
+  Symbols:   64645
+  CStrings:  24895
 
Symbols:
+ +[CNOOPContactContentViewController classForContentViewControllerImpl]
+ +[CNUIFavoritesEntryPicker actionTypes]
+ +[CNUIVCardUtilities fileNameForContactName:]
+ -[CNContactAddFavoriteAction actionsDataSource]
+ -[CNContactAddFavoriteAction initWithContact:propertyItems:favorites:actionsDataSource:]
+ -[CNContactContentUnitaryViewController canModifySharingLocations]
+ -[CNContactContentUnitaryViewController editInAppAction]
+ -[CNContactContentUnitaryViewController editingToolbar]
+ -[CNContactContentUnitaryViewController ensureContactStoreExists]
+ -[CNContactContentUnitaryViewController locationSharingModificationCheck]
+ -[CNContactContentUnitaryViewController setEditInAppAction:]
+ -[CNContactContentUnitaryViewController setEditingToolbar:]
+ -[CNContactListCollectionViewCell configuredAsBlocked]
+ -[CNContactListCollectionViewCell setConfiguredAsBlocked:]
+ -[CNContactListStyleApplier applyContactListStyleToContact:usingFormatter:ofCell:]
+ -[CNContactListStyleApplier applyContentConfigurationUsingState:forCell:]
+ -[CNContactListStyleApplier attributedTextForContact:usingFormatter:isBlocked:hasSubtitle:]
+ -[CNContactListStyleApplier blockedIcon]
+ -[CNContactListStyleApplier createNewBlockedIconIfNecessary]
+ -[CNContactListStyleApplier setBlockedIcon:]
+ -[CNContactListViewController addContactsToListTappedWithSender:]
+ -[CNContactListViewController createNewContactTapped:]
+ -[CNContactListViewController refreshForCurrentlySelectedContact]
+ -[CNContactListViewController updateSearchBarMaxSizeWithSize:]
+ -[CNContactNavigationController addContact:animated:sender:]
+ -[CNContactNavigationController contactListAddContactButtonTapped:sender:]
+ -[CNContactNavigationController contactListViewControllerSelectedAddContactToList:sender:]
+ -[CNContactNavigationController contactListViewControllerSelectedCreateNewContact:sender:]
+ -[CNContactNavigationController executeAddContact:]
+ -[CNContactNavigationController isShowingGroups]
+ -[CNContactNavigationController presentAddToGroupPickerWithSender:]
+ -[CNContactPhotoView didPhotoChangeFromContact:toContact:]
+ -[CNContactPickerContentViewController isOutOfProcess]
+ -[CNContactViewController _hasInProcessContactsDatabaseEntitlement]
+ -[CNPropertySendMessageAction initWithContact:propertyItems:actionsDataSource:]
+ -[CNSharedProfileBannerView avatarSizeForWidth:]
+ -[CNSharedProfileBannerView setFrame:]
+ -[CNSharedProfileBannerView useVerticalLayoutForWidth:]
+ -[CNStarkContactViewController contactNameViewWidthContraint]
+ -[CNStarkContactViewController maximumWidthForNameView]
+ -[CNStarkContactViewController setContactNameViewWidthContraint:]
+ -[CNStarkContactViewController updateViewConstraints]
+ -[CNUIAcceptedContactConfiguration formattedHandle]
+ GCC_except_table10048
+ GCC_except_table10054
+ GCC_except_table10276
+ GCC_except_table10477
+ GCC_except_table10491
+ GCC_except_table10505
+ GCC_except_table10761
+ GCC_except_table10763
+ GCC_except_table10833
+ GCC_except_table10834
+ GCC_except_table10849
+ GCC_except_table11130
+ GCC_except_table11136
+ GCC_except_table11187
+ GCC_except_table11191
+ GCC_except_table11395
+ GCC_except_table11587
+ GCC_except_table11590
+ GCC_except_table11600
+ GCC_except_table11602
+ GCC_except_table11603
+ GCC_except_table11613
+ GCC_except_table11647
+ GCC_except_table11652
+ GCC_except_table11710
+ GCC_except_table11822
+ GCC_except_table11916
+ GCC_except_table11943
+ GCC_except_table12062
+ GCC_except_table12124
+ GCC_except_table12186
+ GCC_except_table12187
+ GCC_except_table12197
+ GCC_except_table12198
+ GCC_except_table12625
+ GCC_except_table12642
+ GCC_except_table12663
+ GCC_except_table12961
+ GCC_except_table12995
+ GCC_except_table13098
+ GCC_except_table13295
+ GCC_except_table13363
+ GCC_except_table13369
+ GCC_except_table13443
+ GCC_except_table13444
+ GCC_except_table13452
+ GCC_except_table13532
+ GCC_except_table13537
+ GCC_except_table13710
+ GCC_except_table13729
+ GCC_except_table13878
+ GCC_except_table13907
+ GCC_except_table13908
+ GCC_except_table14042
+ GCC_except_table14128
+ GCC_except_table14135
+ GCC_except_table14172
+ GCC_except_table14430
+ GCC_except_table14433
+ GCC_except_table14539
+ GCC_except_table14558
+ GCC_except_table14824
+ GCC_except_table14898
+ GCC_except_table15019
+ GCC_except_table15023
+ GCC_except_table15097
+ GCC_except_table15163
+ GCC_except_table15177
+ GCC_except_table15196
+ GCC_except_table15198
+ GCC_except_table15367
+ GCC_except_table15468
+ GCC_except_table15548
+ GCC_except_table15552
+ GCC_except_table15570
+ GCC_except_table15620
+ GCC_except_table15743
+ GCC_except_table16048
+ GCC_except_table16063
+ GCC_except_table16079
+ GCC_except_table16092
+ GCC_except_table16097
+ GCC_except_table16098
+ GCC_except_table16118
+ GCC_except_table16194
+ GCC_except_table16580
+ GCC_except_table16582
+ GCC_except_table16591
+ GCC_except_table16686
+ GCC_except_table16749
+ GCC_except_table16789
+ GCC_except_table16919
+ GCC_except_table17196
+ GCC_except_table17200
+ GCC_except_table17665
+ GCC_except_table17682
+ GCC_except_table17734
+ GCC_except_table17773
+ GCC_except_table17787
+ GCC_except_table17807
+ GCC_except_table17839
+ GCC_except_table17840
+ GCC_except_table17847
+ GCC_except_table17848
+ GCC_except_table17873
+ GCC_except_table18000
+ GCC_except_table18010
+ GCC_except_table18026
+ GCC_except_table18030
+ GCC_except_table18034
+ GCC_except_table18036
+ GCC_except_table18082
+ GCC_except_table18288
+ GCC_except_table18345
+ GCC_except_table18346
+ GCC_except_table18353
+ GCC_except_table18358
+ GCC_except_table18363
+ GCC_except_table18372
+ GCC_except_table18400
+ GCC_except_table18422
+ GCC_except_table18440
+ GCC_except_table18441
+ GCC_except_table18452
+ GCC_except_table18459
+ GCC_except_table18460
+ GCC_except_table18463
+ GCC_except_table18465
+ GCC_except_table18467
+ GCC_except_table18480
+ GCC_except_table18621
+ GCC_except_table2101
+ GCC_except_table2184
+ GCC_except_table2884
+ GCC_except_table2950
+ GCC_except_table3024
+ GCC_except_table3025
+ GCC_except_table3026
+ GCC_except_table3141
+ GCC_except_table3271
+ GCC_except_table3443
+ GCC_except_table3445
+ GCC_except_table3578
+ GCC_except_table3580
+ GCC_except_table3658
+ GCC_except_table3773
+ GCC_except_table3978
+ GCC_except_table3979
+ GCC_except_table4150
+ GCC_except_table4192
+ GCC_except_table4226
+ GCC_except_table4343
+ GCC_except_table4433
+ GCC_except_table4709
+ GCC_except_table4747
+ GCC_except_table4757
+ GCC_except_table4918
+ GCC_except_table4959
+ GCC_except_table5033
+ GCC_except_table5034
+ GCC_except_table5040
+ GCC_except_table5042
+ GCC_except_table5097
+ GCC_except_table5117
+ GCC_except_table5158
+ GCC_except_table5165
+ GCC_except_table5166
+ GCC_except_table5234
+ GCC_except_table5378
+ GCC_except_table5745
+ GCC_except_table5754
+ GCC_except_table5845
+ GCC_except_table5873
+ GCC_except_table5881
+ GCC_except_table5996
+ GCC_except_table6169
+ GCC_except_table6315
+ GCC_except_table6331
+ GCC_except_table6630
+ GCC_except_table6669
+ GCC_except_table6742
+ GCC_except_table6920
+ GCC_except_table6925
+ GCC_except_table7056
+ GCC_except_table7132
+ GCC_except_table7276
+ GCC_except_table7532
+ GCC_except_table7630
+ GCC_except_table8027
+ GCC_except_table8084
+ GCC_except_table8118
+ GCC_except_table8237
+ GCC_except_table8281
+ GCC_except_table8660
+ GCC_except_table8703
+ GCC_except_table8768
+ GCC_except_table8774
+ GCC_except_table8942
+ GCC_except_table8977
+ GCC_except_table9017
+ GCC_except_table9041
+ GCC_except_table9106
+ GCC_except_table9233
+ GCC_except_table9237
+ GCC_except_table9363
+ GCC_except_table9370
+ GCC_except_table9376
+ GCC_except_table9380
+ GCC_except_table9383
+ GCC_except_table9388
+ GCC_except_table9398
+ GCC_except_table9401
+ GCC_except_table9415
+ GCC_except_table9421
+ GCC_except_table9424
+ GCC_except_table9427
+ GCC_except_table9429
+ GCC_except_table9635
+ GCC_except_table9643
+ GCC_except_table9718
+ GCC_except_table9721
+ GCC_except_table9816
+ GCC_except_table9854
+ GCC_except_table9869
+ GCC_except_table9874
+ _AFPreferencesFunction.46245
+ _AssistantServicesLibraryCore.frameworkLibrary.49001
+ _AssistantServicesLibraryCore.frameworkLibrary.54932
+ _AvatarKitLibraryCore.frameworkLibrary.30394
+ _AvatarKitLibraryCore.frameworkLibrary.32835
+ _AvatarKitLibraryCore.frameworkLibrary.50968
+ _AvatarKitLibraryCore.frameworkLibrary.55495
+ _AvatarUILibrary.19945
+ _AvatarUILibrary.32816
+ _AvatarUILibrary.37794
+ _AvatarUILibrary.41897
+ _AvatarUILibrary.53392
+ _AvatarUILibraryCore.frameworkLibrary.13211
+ _AvatarUILibraryCore.frameworkLibrary.16226
+ _AvatarUILibraryCore.frameworkLibrary.19956
+ _AvatarUILibraryCore.frameworkLibrary.30410
+ _AvatarUILibraryCore.frameworkLibrary.32823
+ _AvatarUILibraryCore.frameworkLibrary.33667
+ _AvatarUILibraryCore.frameworkLibrary.34337
+ _AvatarUILibraryCore.frameworkLibrary.36526
+ _AvatarUILibraryCore.frameworkLibrary.37801
+ _AvatarUILibraryCore.frameworkLibrary.41907
+ _AvatarUILibraryCore.frameworkLibrary.53402
+ _AvatarUILibraryCore.frameworkLibrary.55471
+ _AvatarUILibraryCore.frameworkLibrary.6096
+ _CRRecentContactsLibraryFunction.50582
+ _FBSOpenApplicationServiceFunction.50203
+ _FBSOpenApplicationServiceFunction.51594
+ _GameCenterFoundationLibraryCore.frameworkLibrary.42195
+ _GameCenterFoundationLibraryCore.frameworkLibrary.49582
+ _GameCenterUICoreLibraryCore.frameworkLibrary.42178
+ _GameCenterUILibraryCore.frameworkLibrary.49550
+ _HealthKitLibraryCore.frameworkLibrary.41715
+ _IDSLibrary.22976
+ _IDSLibrary.46325
+ _IDSLibraryCore.frameworkLibrary.23011
+ _IDSLibraryCore.frameworkLibrary.30941
+ _IDSLibraryCore.frameworkLibrary.42718
+ _IDSLibraryCore.frameworkLibrary.46341
+ _IDSLibraryCore.frameworkLibrary.50567
+ _IDSLibraryCore.frameworkLibrary.52194
+ _IMCoreLibraryCore.frameworkLibrary.10767
+ _IMCoreLibraryCore.frameworkLibrary.47423
+ _IMCoreLibraryCore.frameworkLibrary.64558
+ _IntlPreferencesUILibraryCore.frameworkLibrary.13960
+ _IntlPreferencesUILibraryCore.frameworkLibrary.58477
+ _LoadAppleAccount.frameworkLibrary.51350
+ _LoadAppleAccount.loadPredicate.51343
+ _LoadAssistantServices.frameworkLibrary.46250
+ _LoadAssistantServices.loadPredicate.46240
+ _LoadCarPlayServices.frameworkLibrary.50208
+ _LoadCarPlayServices.frameworkLibrary.51599
+ _LoadCarPlayServices.loadPredicate.50198
+ _LoadCarPlayServices.loadPredicate.51589
+ _LoadCoreRecents.frameworkLibrary.50586
+ _LoadCoreRecents.loadPredicate.50578
+ _LoadCoreSuggestions.frameworkLibrary.50563
+ _LoadCoreSuggestions.loadPredicate.50558
+ _LoadMapKit.frameworkLibrary.22274
+ _LoadMapKit.frameworkLibrary.24443
+ _LoadMapKit.loadPredicate.22267
+ _LoadMapKit.loadPredicate.24440
+ _LoadMedicalIDUI.frameworkLibrary.41697
+ _LoadMedicalIDUI.loadPredicate.41690
+ _LoadPhotos.frameworkLibrary.38295
+ _LoadPhotos.frameworkLibrary.44753
+ _LoadPhotos.frameworkLibrary.47860
+ _LoadPhotos.loadPredicate.38290
+ _LoadPhotos.loadPredicate.44749
+ _LoadPhotos.loadPredicate.47855
+ _LoadPhotosUI.frameworkLibrary.44793
+ _LoadPhotosUI.loadPredicate.44785
+ _MIUIDisplayConfigurationFunction.41704
+ _MIUIMedicalIDViewControllerFunction.41693
+ _MobileCoreServicesLibrary.57921
+ _MobileCoreServicesLibraryCore.frameworkLibrary.47262
+ _MobileCoreServicesLibraryCore.frameworkLibrary.57934
+ _OBJC_CLASS_$_CNContactsAppIntentDonationManager
+ _OBJC_CLASS_$_CNOOPContactContentViewController
+ _OBJC_CLASS_$_CNUICoreLocationSharingModificationInspector
+ _OBJC_CLASS_$_UIToolbar
+ _OBJC_CLASS_$_UIViewControllerTransition
+ _OBJC_IVAR_$_CNContactAddFavoriteAction._actionsDataSource
+ _OBJC_IVAR_$_CNContactContentUnitaryViewController._editInAppAction
+ _OBJC_IVAR_$_CNContactContentUnitaryViewController._editingToolbar
+ _OBJC_IVAR_$_CNContactContentUnitaryViewController._locationSharingModificationCheck
+ _OBJC_IVAR_$_CNContactListCollectionViewCell._configuredAsBlocked
+ _OBJC_IVAR_$_CNContactListStyleApplier._blockedIcon
+ _OBJC_IVAR_$_CNStarkContactViewController._contactNameViewWidthContraint
+ _OBJC_METACLASS_$_CNOOPContactContentViewController
+ _OUTLINED_FUNCTION_0
+ _PHPhotoLibraryFunction.47875
+ _PHPickerViewControllerFunction.44789
+ _PosterBoardServicesLibrary.65485
+ _PosterBoardServicesLibraryCore.frameworkLibrary.65489
+ _PosterBoardUIServicesLibraryCore.frameworkLibrary.65537
+ _PosterKitLibraryCore.frameworkLibrary.65673
+ _SharingLibraryCore.frameworkLibrary.64604
+ _SiriActivationLibrary.54914
+ _SiriActivationLibraryCore.frameworkLibrary.54920
+ _SocialLibraryCore.frameworkLibrary.22629
+ _SocialLibraryCore.frameworkLibrary.59577
+ _SocialLibraryCore.frameworkLibrary.64687
+ _ToneKitLibraryCore.frameworkLibrary.57694
+ _UTTypeUTF8PlainText
+ __DATA__TtC10ContactsUI23ContactHeaderAppearance
+ __IVARS__TtC10ContactsUI23ContactHeaderAppearance
+ __METACLASS_DATA__TtC10ContactsUI23ContactHeaderAppearance
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_CNOOPContactContentViewController
+ __OBJC_$_PROP_LIST_CNContactListAction.9884
+ __OBJC_$_PROP_LIST_CNContactPickerContentViewController.480
+ __OBJC_CLASS_RO_$_CNOOPContactContentViewController
+ __OBJC_METACLASS_RO_$_CNOOPContactContentViewController
+ ___39+[CNUIFavoritesEntryPicker actionTypes]_block_invoke
+ ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke.90
+ ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke.95
+ ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke_2.96
+ ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke_3.98
+ ___49-[CNContactContentEditViewController setContact:]_block_invoke.416
+ ___49-[CNContactViewController _prepareViewController]_block_invoke.103
+ ___52-[CNContactContentDisplayViewController setContact:]_block_invoke.416
+ ___56-[CNHealthStoreManager notifyHandlersWithMedicalIDData:]_block_invoke.369
+ ___58-[CNContactListViewController contactDataSourceDidChange:]_block_invoke.634
+ ___60-[CNContactNavigationController addContact:animated:sender:]_block_invoke
+ ___60-[CNContactNavigationController addContact:animated:sender:]_block_invoke_2
+ ___64+[CNUIDraggingContacts itemProviderForContact:withContactStore:]_block_invoke_2
+ ___65-[CNContactContentUnitaryViewController ensureContactStoreExists]_block_invoke
+ ___65-[CNContactListViewController refreshForCurrentlySelectedContact]_block_invoke
+ ___67-[CNContactContentUnitaryViewController performSaveToSharedProfile]_block_invoke.558
+ ___67-[CNContactNavigationController presentAddToGroupPickerWithSender:]_block_invoke
+ ___67-[CNContactNavigationController presentAddToGroupPickerWithSender:]_block_invoke_2
+ ___69-[CNContactContentDisplayViewController reloadDataPreservingChanges:]_block_invoke.428
+ ___70-[CNContactContentUnitaryViewController setContact:shouldScrollToTop:]_block_invoke.475
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.346
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.368
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.375
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_2.370
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_3.372
+ ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_4.374
+ ___AssistantServicesLibraryCore_block_invoke.49002
+ ___AssistantServicesLibraryCore_block_invoke.54933
+ ___AvatarKitLibraryCore_block_invoke.30395
+ ___AvatarKitLibraryCore_block_invoke.32836
+ ___AvatarKitLibraryCore_block_invoke.50969
+ ___AvatarKitLibraryCore_block_invoke.55496
+ ___AvatarUILibraryCore_block_invoke.13212
+ ___AvatarUILibraryCore_block_invoke.16227
+ ___AvatarUILibraryCore_block_invoke.19957
+ ___AvatarUILibraryCore_block_invoke.30411
+ ___AvatarUILibraryCore_block_invoke.32824
+ ___AvatarUILibraryCore_block_invoke.33668
+ ___AvatarUILibraryCore_block_invoke.34338
+ ___AvatarUILibraryCore_block_invoke.36527
+ ___AvatarUILibraryCore_block_invoke.37802
+ ___AvatarUILibraryCore_block_invoke.41908
+ ___AvatarUILibraryCore_block_invoke.53403
+ ___AvatarUILibraryCore_block_invoke.55472
+ ___AvatarUILibraryCore_block_invoke.6097
+ ___Block_byref_object_copy_.13630
+ ___Block_byref_object_copy_.14843
+ ___Block_byref_object_copy_.16507
+ ___Block_byref_object_copy_.16926
+ ___Block_byref_object_copy_.19347
+ ___Block_byref_object_copy_.21879
+ ___Block_byref_object_copy_.22611
+ ___Block_byref_object_copy_.23564
+ ___Block_byref_object_copy_.24015
+ ___Block_byref_object_copy_.2404
+ ___Block_byref_object_copy_.26945
+ ___Block_byref_object_copy_.2857
+ ___Block_byref_object_copy_.29256
+ ___Block_byref_object_copy_.30663
+ ___Block_byref_object_copy_.31907
+ ___Block_byref_object_copy_.31988
+ ___Block_byref_object_copy_.32831
+ ___Block_byref_object_copy_.33063
+ ___Block_byref_object_copy_.34332
+ ___Block_byref_object_copy_.36501
+ ___Block_byref_object_copy_.38285
+ ___Block_byref_object_copy_.3968
+ ___Block_byref_object_copy_.4210
+ ___Block_byref_object_copy_.44463
+ ___Block_byref_object_copy_.47868
+ ___Block_byref_object_copy_.48748
+ ___Block_byref_object_copy_.50962
+ ___Block_byref_object_copy_.51979
+ ___Block_byref_object_copy_.53012
+ ___Block_byref_object_copy_.54661
+ ___Block_byref_object_copy_.55822
+ ___Block_byref_object_copy_.56846
+ ___Block_byref_object_copy_.59507
+ ___Block_byref_object_copy_.62434
+ ___Block_byref_object_copy_.64171
+ ___Block_byref_object_copy_.64612
+ ___Block_byref_object_dispose_.13631
+ ___Block_byref_object_dispose_.14844
+ ___Block_byref_object_dispose_.16508
+ ___Block_byref_object_dispose_.16927
+ ___Block_byref_object_dispose_.19348
+ ___Block_byref_object_dispose_.21880
+ ___Block_byref_object_dispose_.22612
+ ___Block_byref_object_dispose_.23565
+ ___Block_byref_object_dispose_.24016
+ ___Block_byref_object_dispose_.2405
+ ___Block_byref_object_dispose_.26946
+ ___Block_byref_object_dispose_.2858
+ ___Block_byref_object_dispose_.29257
+ ___Block_byref_object_dispose_.30664
+ ___Block_byref_object_dispose_.31908
+ ___Block_byref_object_dispose_.31989
+ ___Block_byref_object_dispose_.32832
+ ___Block_byref_object_dispose_.33064
+ ___Block_byref_object_dispose_.34333
+ ___Block_byref_object_dispose_.36502
+ ___Block_byref_object_dispose_.38286
+ ___Block_byref_object_dispose_.3969
+ ___Block_byref_object_dispose_.4211
+ ___Block_byref_object_dispose_.44464
+ ___Block_byref_object_dispose_.47869
+ ___Block_byref_object_dispose_.48749
+ ___Block_byref_object_dispose_.50963
+ ___Block_byref_object_dispose_.51980
+ ___Block_byref_object_dispose_.53013
+ ___Block_byref_object_dispose_.54662
+ ___Block_byref_object_dispose_.55823
+ ___Block_byref_object_dispose_.56847
+ ___Block_byref_object_dispose_.59508
+ ___Block_byref_object_dispose_.62435
+ ___Block_byref_object_dispose_.64172
+ ___Block_byref_object_dispose_.64613
+ ___GameCenterFoundationLibraryCore_block_invoke.42196
+ ___GameCenterFoundationLibraryCore_block_invoke.49583
+ ___GameCenterUICoreLibraryCore_block_invoke.42179
+ ___GameCenterUILibraryCore_block_invoke.49551
+ ___HealthKitLibraryCore_block_invoke.41716
+ ___IDSLibraryCore_block_invoke.23012
+ ___IDSLibraryCore_block_invoke.30942
+ ___IDSLibraryCore_block_invoke.42719
+ ___IDSLibraryCore_block_invoke.46342
+ ___IDSLibraryCore_block_invoke.50568
+ ___IDSLibraryCore_block_invoke.52195
+ ___IMCoreLibraryCore_block_invoke.10768
+ ___IMCoreLibraryCore_block_invoke.47424
+ ___IMCoreLibraryCore_block_invoke.64559
+ ___IntlPreferencesUILibraryCore_block_invoke.13961
+ ___IntlPreferencesUILibraryCore_block_invoke.58478
+ ___LoadAppleAccount_block_invoke.51348
+ ___LoadAssistantServices_block_invoke.46248
+ ___LoadCarPlayServices_block_invoke.50206
+ ___LoadCarPlayServices_block_invoke.51597
+ ___LoadCoreRecents_block_invoke.50585
+ ___LoadCoreSuggestions_block_invoke.50561
+ ___LoadMapKit_block_invoke.22272
+ ___LoadMapKit_block_invoke.24442
+ ___LoadMedicalIDUI_block_invoke.41695
+ ___LoadPhotosUI_block_invoke.44791
+ ___LoadPhotos_block_invoke.38293
+ ___LoadPhotos_block_invoke.44751
+ ___LoadPhotos_block_invoke.47858
+ ___MobileCoreServicesLibraryCore_block_invoke.47263
+ ___MobileCoreServicesLibraryCore_block_invoke.57935
+ ___PosterBoardServicesLibraryCore_block_invoke.65490
+ ___PosterBoardUIServicesLibraryCore_block_invoke.65538
+ ___PosterKitLibraryCore_block_invoke.65674
+ ___SharingLibraryCore_block_invoke.64605
+ ___SiriActivationLibraryCore_block_invoke.54921
+ ___SocialLibraryCore_block_invoke.22630
+ ___SocialLibraryCore_block_invoke.59578
+ ___SocialLibraryCore_block_invoke.64688
+ ___ToneKitLibraryCore_block_invoke.57695
+ ___block_descriptor_40_e8_32s_e42_"UICellAccessory"16?0"UICellAccessory"8ls32l8
+ ___block_descriptor_40_e8_32s_e45_"NSProgress"16?0?<v?"NSData""NSError">8ls32l8
+ ___block_descriptor_40_e8_32s_e59_"UIView"16?0"UIZoomTransitionSourceViewProviderContext"8ls32l8
+ ___block_descriptor_40_e8_32s_e68_"UIBarButtonItem"16?0"UIZoomTransitionSourceViewProviderContext"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e70_v24?0"CNContactListCollectionViewCell"8"UICellConfigurationState"16ls32l8s40l8
+ ___block_literal_global.10.64201
+ ___block_literal_global.10129
+ ___block_literal_global.1027
+ ___block_literal_global.10349
+ ___block_literal_global.105
+ ___block_literal_global.1051
+ ___block_literal_global.1053
+ ___block_literal_global.10796
+ ___block_literal_global.10918
+ ___block_literal_global.11.63847
+ ___block_literal_global.1131
+ ___block_literal_global.11387
+ ___block_literal_global.11492
+ ___block_literal_global.11583
+ ___block_literal_global.11743
+ ___block_literal_global.11957
+ ___block_literal_global.12413
+ ___block_literal_global.127.52673
+ ___block_literal_global.131.13956
+ ___block_literal_global.13202
+ ___block_literal_global.135.43341
+ ___block_literal_global.13565
+ ___block_literal_global.139.15766
+ ___block_literal_global.139.31088
+ ___block_literal_global.13974
+ ___block_literal_global.14.31131
+ ___block_literal_global.14.31352
+ ___block_literal_global.14.45136
+ ___block_literal_global.14.57598
+ ___block_literal_global.141.15764
+ ___block_literal_global.14836
+ ___block_literal_global.15824
+ ___block_literal_global.16573
+ ___block_literal_global.16754
+ ___block_literal_global.16922
+ ___block_literal_global.17929
+ ___block_literal_global.18.5501
+ ___block_literal_global.18540
+ ___block_literal_global.19.31126
+ ___block_literal_global.19.40239
+ ___block_literal_global.19.42154
+ ___block_literal_global.19133
+ ___block_literal_global.19237
+ ___block_literal_global.19396
+ ___block_literal_global.19751
+ ___block_literal_global.2.49465
+ ___block_literal_global.2.62988
+ ___block_literal_global.20.35061
+ ___block_literal_global.20487
+ ___block_literal_global.20706
+ ___block_literal_global.20993
+ ___block_literal_global.21.17955
+ ___block_literal_global.21.32026
+ ___block_literal_global.21259
+ ___block_literal_global.21512
+ ___block_literal_global.21795
+ ___block_literal_global.21896
+ ___block_literal_global.22236
+ ___block_literal_global.22268
+ ___block_literal_global.22670
+ ___block_literal_global.23.45122
+ ___block_literal_global.23.63147
+ ___block_literal_global.23024
+ ___block_literal_global.23489
+ ___block_literal_global.23923
+ ___block_literal_global.24030
+ ___block_literal_global.24490
+ ___block_literal_global.24819
+ ___block_literal_global.25.40247
+ ___block_literal_global.25.63148
+ ___block_literal_global.25.64191
+ ___block_literal_global.25677
+ ___block_literal_global.26.57594
+ ___block_literal_global.26190
+ ___block_literal_global.26271
+ ___block_literal_global.26445
+ ___block_literal_global.27.40790
+ ___block_literal_global.27299
+ ___block_literal_global.28.40250
+ ___block_literal_global.28.49237
+ ___block_literal_global.28244
+ ___block_literal_global.28321
+ ___block_literal_global.28468
+ ___block_literal_global.2867
+ ___block_literal_global.29.28466
+ ___block_literal_global.29.31118
+ ___block_literal_global.29.45113
+ ___block_literal_global.29.48350
+ ___block_literal_global.29.63667
+ ___block_literal_global.29005
+ ___block_literal_global.29066
+ ___block_literal_global.29285
+ ___block_literal_global.29848
+ ___block_literal_global.3.16749
+ ___block_literal_global.3.28326
+ ___block_literal_global.3.37245
+ ___block_literal_global.3.57633
+ ___block_literal_global.3.58659
+ ___block_literal_global.3.58892
+ ___block_literal_global.30717
+ ___block_literal_global.30954
+ ___block_literal_global.31.28449
+ ___block_literal_global.31.40253
+ ___block_literal_global.31141
+ ___block_literal_global.31312
+ ___block_literal_global.31356
+ ___block_literal_global.31609
+ ___block_literal_global.31652
+ ___block_literal_global.31933
+ ___block_literal_global.32058
+ ___block_literal_global.32116
+ ___block_literal_global.32391
+ ___block_literal_global.32845
+ ___block_literal_global.32874
+ ___block_literal_global.33110
+ ___block_literal_global.33719
+ ___block_literal_global.3390
+ ___block_literal_global.34.31113
+ ___block_literal_global.34.40258
+ ___block_literal_global.34210
+ ___block_literal_global.34356
+ ___block_literal_global.347
+ ___block_literal_global.34804
+ ___block_literal_global.35029
+ ___block_literal_global.35149
+ ___block_literal_global.354.26446
+ ___block_literal_global.35509
+ ___block_literal_global.3567
+ ___block_literal_global.357
+ ___block_literal_global.36.33105
+ ___block_literal_global.360
+ ___block_literal_global.36054
+ ___block_literal_global.3626
+ ___block_literal_global.363
+ ___block_literal_global.36494
+ ___block_literal_global.366
+ ___block_literal_global.369.26447
+ ___block_literal_global.3692
+ ___block_literal_global.37.40261
+ ___block_literal_global.37007
+ ___block_literal_global.37063
+ ___block_literal_global.37250
+ ___block_literal_global.37418
+ ___block_literal_global.37637
+ ___block_literal_global.37831
+ ___block_literal_global.37950
+ ___block_literal_global.38.38813
+ ___block_literal_global.38.64179
+ ___block_literal_global.38090
+ ___block_literal_global.38297
+ ___block_literal_global.38729
+ ___block_literal_global.38816
+ ___block_literal_global.39.31111
+ ___block_literal_global.3987
+ ___block_literal_global.39963
+ ___block_literal_global.4.31605
+ ___block_literal_global.4.37419
+ ___block_literal_global.4.46729
+ ___block_literal_global.4.5104
+ ___block_literal_global.40.40266
+ ___block_literal_global.40219
+ ___block_literal_global.40292
+ ___block_literal_global.40657
+ ___block_literal_global.40817
+ ___block_literal_global.41.19371
+ ___block_literal_global.41.23582
+ ___block_literal_global.41.29830
+ ___block_literal_global.41568
+ ___block_literal_global.41741
+ ___block_literal_global.41862
+ ___block_literal_global.41895
+ ___block_literal_global.42.66793
+ ___block_literal_global.42164
+ ___block_literal_global.4245
+ ___block_literal_global.42469
+ ___block_literal_global.425
+ ___block_literal_global.43.19373
+ ___block_literal_global.43.40271
+ ___block_literal_global.43253
+ ___block_literal_global.43626
+ ___block_literal_global.4369
+ ___block_literal_global.43724
+ ___block_literal_global.43821
+ ___block_literal_global.44240
+ ___block_literal_global.443
+ ___block_literal_global.44450
+ ___block_literal_global.44629
+ ___block_literal_global.44802
+ ___block_literal_global.45143
+ ___block_literal_global.454
+ ___block_literal_global.46.40276
+ ___block_literal_global.46068
+ ___block_literal_global.46254
+ ___block_literal_global.463
+ ___block_literal_global.467
+ ___block_literal_global.46731
+ ___block_literal_global.47.60473
+ ___block_literal_global.47026
+ ___block_literal_global.47279
+ ___block_literal_global.47355
+ ___block_literal_global.477
+ ___block_literal_global.47883
+ ___block_literal_global.48157
+ ___block_literal_global.48383
+ ___block_literal_global.48914
+ ___block_literal_global.49.56545
+ ___block_literal_global.49239
+ ___block_literal_global.49296
+ ___block_literal_global.49383
+ ___block_literal_global.49464
+ ___block_literal_global.495
+ ___block_literal_global.49838
+ ___block_literal_global.5.46058
+ ___block_literal_global.501
+ ___block_literal_global.50199
+ ___block_literal_global.50579
+ ___block_literal_global.51.31103
+ ___block_literal_global.51011
+ ___block_literal_global.5103
+ ___block_literal_global.51161
+ ___block_literal_global.51339
+ ___block_literal_global.51442
+ ___block_literal_global.51457
+ ___block_literal_global.51590
+ ___block_literal_global.51885
+ ___block_literal_global.52068
+ ___block_literal_global.522
+ ___block_literal_global.525
+ ___block_literal_global.52782
+ ___block_literal_global.53022
+ ___block_literal_global.53134
+ ___block_literal_global.53449
+ ___block_literal_global.53721
+ ___block_literal_global.53801
+ ___block_literal_global.539
+ ___block_literal_global.54.61054
+ ___block_literal_global.54160
+ ___block_literal_global.546
+ ___block_literal_global.54660
+ ___block_literal_global.5506
+ ___block_literal_global.55146
+ ___block_literal_global.55513
+ ___block_literal_global.56.66783
+ ___block_literal_global.56075
+ ___block_literal_global.56589
+ ___block_literal_global.57.51344
+ ___block_literal_global.57643
+ ___block_literal_global.58393
+ ___block_literal_global.584
+ ___block_literal_global.58652
+ ___block_literal_global.58887
+ ___block_literal_global.59605
+ ___block_literal_global.598
+ ___block_literal_global.6.10415
+ ___block_literal_global.60.61042
+ ___block_literal_global.60478
+ ___block_literal_global.61108
+ ___block_literal_global.6112
+ ___block_literal_global.616
+ ___block_literal_global.62.40640
+ ___block_literal_global.62385
+ ___block_literal_global.626
+ ___block_literal_global.62995
+ ___block_literal_global.63.31100
+ ___block_literal_global.63.46241
+ ___block_literal_global.63161
+ ___block_literal_global.634
+ ___block_literal_global.63696
+ ___block_literal_global.63853
+ ___block_literal_global.64215
+ ___block_literal_global.64822
+ ___block_literal_global.6509
+ ___block_literal_global.65140
+ ___block_literal_global.654
+ ___block_literal_global.65739
+ ___block_literal_global.65938
+ ___block_literal_global.66182
+ ___block_literal_global.66399
+ ___block_literal_global.664
+ ___block_literal_global.66576
+ ___block_literal_global.670
+ ___block_literal_global.678
+ ___block_literal_global.6783
+ ___block_literal_global.696
+ ___block_literal_global.700
+ ___block_literal_global.718
+ ___block_literal_global.721
+ ___block_literal_global.7225
+ ___block_literal_global.730
+ ___block_literal_global.743
+ ___block_literal_global.749
+ ___block_literal_global.75.27287
+ ___block_literal_global.7527
+ ___block_literal_global.767
+ ___block_literal_global.772
+ ___block_literal_global.78.44445
+ ___block_literal_global.7813
+ ___block_literal_global.8.16747
+ ___block_literal_global.8.40814
+ ___block_literal_global.8.46727
+ ___block_literal_global.8.5098
+ ___block_literal_global.8482
+ ___block_literal_global.87.24839
+ ___block_literal_global.9.31136
+ ___block_literal_global.9.31601
+ ___block_literal_global.9.41887
+ ___block_literal_global.9.46049
+ ___block_literal_global.90.58385
+ ___block_literal_global.9300
+ ___block_literal_global.940
+ ___block_literal_global.9473
+ ___block_literal_global.967
+ ___block_literal_global.970
+ ___block_literal_global.973
+ ___block_literal_global.9806
+ ___getAVTAvatarFetchRequestClass_block_invoke.37793
+ ___getAVTAvatarRecordImageProviderClass_block_invoke.19942
+ ___getAVTAvatarRecordImageProviderClass_block_invoke.32813
+ ___getAVTAvatarRecordImageProviderClass_block_invoke.53388
+ ___getAVTAvatarRecordRenderingClass_block_invoke.30393
+ ___getAVTAvatarRecordRenderingClass_block_invoke.55470
+ ___getAVTAvatarStoreClass_block_invoke.16240
+ ___getAVTAvatarStoreClass_block_invoke.37786
+ ___getAVTAvatarStoreClass_block_invoke.41918
+ ___getAVTRenderingScopeClass_block_invoke.19944
+ ___getAVTRenderingScopeClass_block_invoke.32815
+ ___getAVTRenderingScopeClass_block_invoke.53390
+ ___getAVTStickerGeneratorOptionsClass_block_invoke.50965
+ ___getAVTViewClass_block_invoke.55492
+ ___getGKDaemonProxyClass_block_invoke.42175
+ ___getGKLocalPlayerClass_block_invoke.42177
+ ___getIDSIDQueryControllerClass_block_invoke.22989
+ ___getIDSIDQueryControllerClass_block_invoke.50566
+ ___getIDSServiceNameFaceTimeSymbolLoc_block_invoke.30931
+ ___getIDSServiceNameFaceTimeSymbolLoc_block_invoke.46324
+ ___getIDSServiceNameiMessageSymbolLoc_block_invoke.42708
+ ___getIDSServiceNameiMessageSymbolLoc_block_invoke.46334
+ ___getIDSServiceNameiMessageSymbolLoc_block_invoke.52184
+ ___getIMNicknameControllerClass_block_invoke.10766
+ ___getIMNicknameControllerClass_block_invoke.47422
+ ___getIMNicknameControllerClass_block_invoke.64557
+ ___getIPPronounPickerViewControllerClass_block_invoke.13959
+ ___getIPPronounPickerViewControllerClass_block_invoke.58476
+ ___getPRSPosterConfigurationAttributesClass_block_invoke.65510
+ ___getPRSPosterRoleIncomingCallSymbolLoc_block_invoke.65484
+ ___getSFCreatePairedContactManagerSymbolLoc_block_invoke.64601
+ ___getSLComposeViewControllerClass_block_invoke.22627
+ ___getSLComposeViewControllerClass_block_invoke.59573
+ ___getSLComposeViewControllerClass_block_invoke.64685
+ ___getSiriDirectActionContextClass_block_invoke.54911
+ ___getSiriDirectActionSourceClass_block_invoke.54913
+ ___getkAssistantDirectActionEventKeySymbolLoc_block_invoke.54903
+ ___getkUTTypeJPEGSymbolLoc_block_invoke.57928
+ ___getkUTTypePNGSymbolLoc_block_invoke.57920
+ ___isPlatformVersionAtLeast
+ ___isPlatformVersionAtLeast.cold.1
+ ___isPlatformVersionAtLeast.cold.2
+ ___swift_memcpy113_8
+ ___unnamed_8
+ __availability_version_check
+ __extensionAuxiliaryHostProtocol.__interface.24833
+ __extensionAuxiliaryHostProtocol.onceToken.24832
+ __extensionAuxiliaryVendorProtocol.__interface.24840
+ __extensionAuxiliaryVendorProtocol.onceToken.24838
+ __initializeAvailabilityCheck
+ _actionTypes._actionTypes
+ _actionTypes.onceToken
+ _associated conformance 10ContactsUI22CNUIVisualIdentityTypeOSHAASQ
+ _associated conformance 10ContactsUI32ContactCardSwiftUIViewControllerC8RootViewV0eB00I0AA4BodyAfGP_AfG
+ _audit_stringAssistantServices.49016
+ _audit_stringAssistantServices.54937
+ _audit_stringAvatarKit.30409
+ _audit_stringAvatarKit.32840
+ _audit_stringAvatarKit.50985
+ _audit_stringAvatarKit.55501
+ _audit_stringAvatarUI.13220
+ _audit_stringAvatarUI.16233
+ _audit_stringAvatarUI.19963
+ _audit_stringAvatarUI.30416
+ _audit_stringAvatarUI.32826
+ _audit_stringAvatarUI.33674
+ _audit_stringAvatarUI.34349
+ _audit_stringAvatarUI.36532
+ _audit_stringAvatarUI.37806
+ _audit_stringAvatarUI.41911
+ _audit_stringAvatarUI.53406
+ _audit_stringAvatarUI.55487
+ _audit_stringAvatarUI.6109
+ _audit_stringGameCenterFoundation.42201
+ _audit_stringGameCenterFoundation.49586
+ _audit_stringGameCenterUI.49566
+ _audit_stringGameCenterUICore.42194
+ _audit_stringHealthKit.41729
+ _audit_stringIDS.23015
+ _audit_stringIDS.30946
+ _audit_stringIDS.42722
+ _audit_stringIDS.46345
+ _audit_stringIDS.50572
+ _audit_stringIDS.52199
+ _audit_stringIMCore.10773
+ _audit_stringIMCore.47437
+ _audit_stringIMCore.64564
+ _audit_stringIntlPreferencesUI.13966
+ _audit_stringIntlPreferencesUI.58494
+ _audit_stringMobileCoreServices.47267
+ _audit_stringMobileCoreServices.57938
+ _audit_stringPosterBoardServices.65493
+ _audit_stringPosterBoardUIServices.65540
+ _audit_stringPosterKit.65677
+ _audit_stringSharing.64607
+ _audit_stringSiriActivation.54924
+ _audit_stringSocial.22634
+ _audit_stringSocial.59582
+ _audit_stringSocial.64692
+ _audit_stringToneKit.57709
+ _block_copy_helper.117
+ _block_copy_helper.131
+ _block_copy_helper.138
+ _block_copy_helper.14
+ _block_copy_helper.17
+ _block_copy_helper.199
+ _block_copy_helper.206
+ _block_copy_helper.68
+ _block_copy_helper.88
+ _block_descriptor.119
+ _block_descriptor.133
+ _block_descriptor.140
+ _block_descriptor.16
+ _block_descriptor.19
+ _block_descriptor.201
+ _block_descriptor.208
+ _block_descriptor.70
+ _block_descriptor.90
+ _block_destroy_helper.118
+ _block_destroy_helper.132
+ _block_destroy_helper.139
+ _block_destroy_helper.15
+ _block_destroy_helper.18
+ _block_destroy_helper.200
+ _block_destroy_helper.207
+ _block_destroy_helper.69
+ _block_destroy_helper.89
+ _bundleCanManageDuplicates.cn_once_object_24
+ _bundleCanManageDuplicates.cn_once_token_24
+ _classAFPreferences.46243
+ _classCRRecentContactsLibrary.50580
+ _classFBSOpenApplicationService.50201
+ _classFBSOpenApplicationService.51592
+ _classMIUIDisplayConfiguration.41702
+ _classMIUIMedicalIDViewController.41691
+ _classPHPhotoLibrary.47873
+ _classPHPickerViewController.44787
+ _compatibilityInitializeAvailabilityCheck
+ _defaultServices._services.49297
+ _defaultServices.onceToken.49295
+ _descriptorForRequiredKeys.cn_once_object_1.18541
+ _descriptorForRequiredKeys.cn_once_object_1.32846
+ _descriptorForRequiredKeys.cn_once_object_1.35510
+ _descriptorForRequiredKeys.cn_once_object_1.42470
+ _descriptorForRequiredKeys.cn_once_object_1.43627
+ _descriptorForRequiredKeys.cn_once_object_1.47027
+ _descriptorForRequiredKeys.cn_once_object_1.48158
+ _descriptorForRequiredKeys.cn_once_object_1.48915
+ _descriptorForRequiredKeys.cn_once_object_1.49839
+ _descriptorForRequiredKeys.cn_once_object_1.53450
+ _descriptorForRequiredKeys.cn_once_object_2.16570
+ _descriptorForRequiredKeys.cn_once_object_2.31606
+ _descriptorForRequiredKeys.cn_once_object_2.31929
+ _descriptorForRequiredKeys.cn_once_object_2.45137
+ _descriptorForRequiredKeys.cn_once_object_2.5502
+ _descriptorForRequiredKeys.cn_once_object_2.6510
+ _descriptorForRequiredKeys.cn_once_token_1.18539
+ _descriptorForRequiredKeys.cn_once_token_1.32844
+ _descriptorForRequiredKeys.cn_once_token_1.35508
+ _descriptorForRequiredKeys.cn_once_token_1.42468
+ _descriptorForRequiredKeys.cn_once_token_1.43625
+ _descriptorForRequiredKeys.cn_once_token_1.47025
+ _descriptorForRequiredKeys.cn_once_token_1.48156
+ _descriptorForRequiredKeys.cn_once_token_1.48913
+ _descriptorForRequiredKeys.cn_once_token_1.49837
+ _descriptorForRequiredKeys.cn_once_token_1.53448
+ _descriptorForRequiredKeys.cn_once_token_2.16569
+ _descriptorForRequiredKeys.cn_once_token_2.31604
+ _descriptorForRequiredKeys.cn_once_token_2.31928
+ _descriptorForRequiredKeys.cn_once_token_2.45135
+ _descriptorForRequiredKeys.cn_once_token_2.5500
+ _descriptorForRequiredKeys.cn_once_token_2.6508
+ _descriptorForRequiredKeysForPreferredForNameMeContact.cn_once_object_11
+ _descriptorForRequiredKeysForPreferredForNameMeContact.cn_once_token_11
+ _descriptorForRequiredKeysWithDescription:.cn_once_object_13.59669
+ _descriptorForRequiredKeysWithDescription:.cn_once_object_13.64852
+ _descriptorForRequiredKeysWithDescription:.cn_once_token_13.59668
+ _descriptorForRequiredKeysWithDescription:.cn_once_token_13.64851
+ _dispatch_once_f
+ _emptyContact.cn_once_object_15
+ _emptyContact.cn_once_token_15
+ _enablesTransportButtons.s_enableTransportButtons.64849
+ _enablesTransportButtons.s_onceToken.64848
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _fullFormatter.44243
+ _getAFPreferencesClass.46237
+ _getAVTAvatarFetchRequestClass.37787
+ _getAVTAvatarFetchRequestClass.softClass.37792
+ _getAVTAvatarRecordImageProviderClass.softClass.19941
+ _getAVTAvatarRecordImageProviderClass.softClass.32812
+ _getAVTAvatarRecordImageProviderClass.softClass.53387
+ _getAVTAvatarRecordRenderingClass.softClass.30392
+ _getAVTAvatarRecordRenderingClass.softClass.55469
+ _getAVTAvatarStoreClass.softClass.16239
+ _getAVTAvatarStoreClass.softClass.37785
+ _getAVTAvatarStoreClass.softClass.41917
+ _getAVTRenderingScopeClass.softClass.19943
+ _getAVTRenderingScopeClass.softClass.32814
+ _getAVTRenderingScopeClass.softClass.53389
+ _getAVTStickerGeneratorOptionsClass.softClass.50964
+ _getAVTViewClass.softClass.55491
+ _getCRRecentContactsLibraryClass.50575
+ _getFBSOpenApplicationServiceClass.50195
+ _getFBSOpenApplicationServiceClass.51586
+ _getGKDaemonProxyClass.softClass.42174
+ _getGKLocalPlayerClass.softClass.42176
+ _getIDSIDQueryControllerClass.22984
+ _getIDSIDQueryControllerClass.softClass.22988
+ _getIDSIDQueryControllerClass.softClass.50565
+ _getIDSServiceNameFaceTimeSymbolLoc.ptr.30930
+ _getIDSServiceNameFaceTimeSymbolLoc.ptr.46323
+ _getIDSServiceNameiMessageSymbolLoc.ptr.42707
+ _getIDSServiceNameiMessageSymbolLoc.ptr.46333
+ _getIDSServiceNameiMessageSymbolLoc.ptr.52183
+ _getIMNicknameControllerClass.softClass.10765
+ _getIMNicknameControllerClass.softClass.47421
+ _getIMNicknameControllerClass.softClass.64556
+ _getIPPronounPickerViewControllerClass.softClass.13958
+ _getIPPronounPickerViewControllerClass.softClass.58475
+ _getMIUIDisplayConfigurationClass.41684
+ _getMIUIMedicalIDViewControllerClass.41685
+ _getPHPhotoLibraryClass.47867
+ _getPHPickerViewControllerClass.44782
+ _getPRSPosterConfigurationAttributesClass.softClass.65509
+ _getPRSPosterRoleIncomingCallSymbolLoc.ptr.65483
+ _getSFCreatePairedContactManagerSymbolLoc.ptr.64600
+ _getSLComposeViewControllerClass.softClass.22626
+ _getSLComposeViewControllerClass.softClass.59572
+ _getSLComposeViewControllerClass.softClass.64684
+ _getSiriDirectActionContextClass.softClass.54910
+ _getSiriDirectActionSourceClass.softClass.54912
+ _get_enum_tag_for_layout_string 7SwiftUI10ShapeStyle_pSg
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQOQr.3
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.5
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQOqd0__AaBHC.4
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.6
+ _get_witness_table 10ContactsUI36CNWallpaperSuggestionsGallerySectionVy05SwiftB015ModifiedContentVyAFyAD6ZStackVyAD9TupleViewVyAFyAFyAFyAD6VStackVyAD012_ConditionalI0VyAJyAD0L0PADE8onSubmit2of_QrAD0P8TriggersV_yyctFQOyAFyAFyAFyAD9TextFieldVyAD0S0VGAD30_EnvironmentKeyWritingModifierVyAD5ColorVSgGGAD14_PaddingLayoutVGA6_G_Qo__ApDEAqR_QrAT_yyctFQOyA7__Qo_tGAJyA10__A9_tGGGA6_GA6_GA6_G_ApDE05sceneZ0yQrAD4EdgeO3SetVFQOyAD7DividerV_Qo_tGGAD011_BackgroundX0VyAD06_ShapeL0VyAD16RoundedRectangleVA1_GGGA3_GGAdOHPyHC.29
+ _get_witness_table 7SwiftUI14GeometryReaderVyAA6ButtonVyAA15ModifiedContentVyAA13_VariadicViewO4TreeVy_AA11_LayoutRootVyAA03AnyK0VGAA05TupleI0VyAGyAGyAA6ZStackVyARyAA012_ConditionalG0VyAGyAGyAA16RoundedRectangleVAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGGAA08_OverlayV0VyAGyA0_AA11_ClipEffectVyAXGGSgGGAGyAGyAA6CircleVA2_GA5_yAGyA0_A7_yA14_GGSgGGG_AVyAA4TextVAGyAGyAA5ImageVAZyAA4FontVSgGGA2_GGtGGA5_yAGyAA08ProgressI0VyAA05EmptyI0VA38_GA2_GSgGGAA010_FlexFrameK0VG_A23_tGGA45_GGGAA0I0HPyHC.154
+ _get_witness_table 7SwiftUI15ModifiedContentVy14ContactsUICore10HeaderViewVAA30_EnvironmentKeyWritingModifierVyAD23ContactCardDetailsStyleVGGAA0H0HPAfaMHPyHC_AkA0hL0HPyHCHC.2
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6VStackVyAA9TupleViewVyAA6SpacerV_AA0G0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyAkAE15fullScreenCover11isPresented0I7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaJRd__lFQOyAEyAA06ScrollG0VyAA6HStackVyACyACyACyACy08ContactsB0021CNPosterSnapshotImageG0VAA12_FrameLayoutVGAA18_AnimationModifierVySo7UIImageCSgGGAA14_PaddingLayoutVGA13_GGGG_AkAE9statusBar6hiddenQrSb_tFQOyACyA_025CNExistingWallpaperEditorG0VAA23_SafeAreaIgnoringLayoutVG_Qo_Qo_AA25_AppearanceActionModifierVG_So24CNPRSPosterConfigurationCSgQo_AikAE12scenePaddingyQrAA4EdgeO3SetVFQOyAEyAGyACyAkAE11buttonStyleyQrqd__AA20PrimitiveButtonStyleRd__lFQOyAA6ButtonVyACyACyAA4TextVA3_GAA16_FlexFrameLayoutVGG_AA28BorderedProminentButtonStyleVQo_AA32_EnvironmentKeyTransformModifierVySbGG_ACyA43_yA45_GAA14_OpacityEffectVGtGG_Qo_tGGA13_GAaJHPA66_AaJHPyHC_A13_AA0G8ModifierHPyHCHC.83
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACyACy08ContactsB0013ContactAvatarG033_87FAEC429F5A2E07500F09EBFC13C74CLLVAA12_FrameLayoutVGAA11_BlurEffectVGAA07_OffsetU0VGSg_ACyAnA08_PaddingS0VGtGGAMGAA0G0HPAzAA0_HPyHC_AmA0G8ModifierHPyHCHC.52
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA9LazyVGridVyAA7ForEachVys10ArraySliceVySo9CNContactCGAK08ContactsB016HelperAvatarView33_87FAEC429F5A2E07500F09EBFC13C74CLLVGSgGAA14_PaddingLayoutVGAA0O0HPAsaWHPyHC_AuA0O8ModifierHPyHCHC.45
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA9LazyVGridVyAA9TupleViewVyAA7ForEachVys10ArraySliceVySo9CNContactCGAM08ContactsB0012HelperAvatarH033_87FAEC429F5A2E07500F09EBFC13C74CLLVG_ACyACyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAWyAA0X9AlignmentOGGAWySbGGAWy12CoreGraphics7CGFloatVGGSgtGSgGAA14_PaddingLayoutVGAA0H0HPA13_AAA17_HPyHC_A15_AA0H8ModifierHPyHCHC.46
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA6ButtonVyACy08ContactsB008CNAvatare10ControllerE0VAA21_TraitWritingModifierVyAA010TransitionO3KeyVGGSgG_Qo_AA14_PaddingLayoutVGAA17_FlipForRTLEffectVGAaDHPA0_AaDHPqd__AaDHD2_AYHO_A_AA0eQ0HPyHCHC_A2_AAA4_HPyHCHC.153
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE010navigationE5StyleyQrqd__AA010NavigationeG0Rd__lFQOyAA0hE0VyAeAE7toolbar7contentQrqd__yXE_tAA07ToolbarD0Rd__lFQOyAeAE0F8BarTitle_11displayModeQrqd___AA0hL4ItemV0m7DisplayO0OtSyRd__lFQOyAeAE06scrollD10BackgroundyQrAA10VisibilityOFQOy08ContactsB021DuplicatesUIContainerVyAA05TupleE0VyACyACyAeAE04listG0yQrqd__AA04ListG0Rd__lFQOyAA0Z0Vys5NeverOAA012_ConditionalD0VyAA7ForEachVySay0U014CNDuplicateSetCGSOAV09DuplicateZ4CellVGAZyAA7SectionVyAA05EmptyE0VA15_A19_GSg_A17_yA19_AV30DuplicatePreviouslyIgnoredCellVA19_GSgtGGG_AA012InsetGroupedzG0VQo_AA14_PaddingLayoutVGAV0v7UIInsetE0VG_AA6SpacerVAV22ActionButtonsContainerVyAZyAeAE18confirmationDialog_11isPresented05titleT07actionsQrqd___AA7BindingVySbGAUqd_0_yXEtSyRd__AaDRd_0_r0_lFQOyACyAeAE06buttonG0yQrqd__AA015PrimitiveButtonG0Rd__lFQOyAA6ButtonVyACyAA4TextVAA16_FlexFrameLayoutVGG_AA023BorderedProminentButtonG0VQo_AA32_EnvironmentKeyTransformModifierVySbGG_SSA52_yA54_GQo__ACyACyA66_AV0v12IgnoreButtonE8ModifierVGA64_GtGGSgtGG_Qo__SSQo__AA0kD7BuilderV10buildBlockyQrxAaLRzlFZQOy_AA0kP0VyytA66_GQo_Qo_G_AA05StackheG0VQo_AA01_sG8ModifierVyAA5ColorVGGAA25_AppearanceActionModifierVGA98_GAaDHPA99_AaDHPA96_AaDHPqd0__AaDHD3_A90_HO_A95_AA0E8ModifierHPyHCHC_A98_AAA101_HPyHCHC_A98_AAA101_HPyHCHC.62
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6VStackVyAA9TupleViewVyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVyAA0H9AlignmentOGGAKyAA4FontVSgGGSg_AA6SpacerVAA6HStackVyAGyAEyAGyAI_ACyACyAiKy12CoreGraphics7CGFloatVGGAKySiSgGGtGG_AWtGGtGGAKyAA5ColorVSgGGAA14_PaddingLayoutVGA18_GSgAA0G0HpA20_AAA22_HPA19_AAA22_HPA16_AAA22_HPA11_AAA22_HPyHC_A15_AA0gL0HPyHCHC_A18_AAA23_HPyHCHC_A18_AAA23_HPyHCHC_HC.174
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAA7ForEachVySnySiGSi08ContactsB020ContactDetailRowViewVGAA25_AppearanceActionModifierVGALGAA0L0HPAoaQHPAlaQHPAkaQHPyHC_HC_AnA0lO0HPyHCHC_AlaQHPAkaQHPyHC_HCHC.52
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA15NavigationStackVyAA0E4PathVAA08ModifiedD0VyAIyAIyAA4ViewPAAE22onScrollGeometryChange3for2of6actionQrqd__m_qd__AA0kL0Vcyqd___qd__tctSQRd__lFQOyAIyAkAE14scrollPosition2id6anchorQrAA7BindingVyqd__SgG_AA9UnitPointVSgtSHRd__lFQOyAK012_AppIntents_aB0E19appEntityIdentifieryQr0xY016EntityIdentifierVSgFQOyAA0kI0VyAkAE0Q12TargetLayout9isEnabledQrSb_tFQOyAA10LazyVStackVyAA05TupleI0Vy08ContactsB0021ContactCardHeaderNameI0V_A14_016CardQuickActionsI0VA14_018ContactCardDetailsI0VtGG_Qo_G_Qo__SiQo_AA23SafeAreaPaddingModifierVG_12CoreGraphics7CGFloatVQo_AA30_EnvironmentKeyWritingModifierVyAA11ColorSchemeOGGAA14_PaddingLayoutVGAA20_BackdropGroupEffectVGGA45_GAaJHPA46_AaJHPyHC_A45_AaJHPA42_AaJHPA39_AaJHPqd0__AaJHD3_A33_HO_A38_AA0I8ModifierHPyHCHC_A41_AAA48_HPyHCHC_A44_AAA48_HPyHCHCHC.175
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewPAAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQOyAA08ModifiedD0Vy08ContactsB014AnswerTemplateVAA25_AppearanceActionModifierVG_So9CNContactCQo_AeAEAfghijK_Qrqd___ALScPSSSiyyYaYAcntSQRd__lFQOyANyAO011ContactCardeaB0VASG_AVQo_GAaDHPqd0__AaDHD3_AWHO_qd0__AaDHD3_A_HOHC.92
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedD0Vy08ContactsB0021CNPosterSnapshotImageE0VAA25_AppearanceActionModifierVG_So16CNMutableContactCQo__12CoreGraphics7CGFloatVQo_AA6ZStackVyAA05TupleE0VyAJyAK08CNAvatare10ControllerE0VAK0L13VibrantShadowVG_A1_tGGGAaDHPqd0__AaDHD3_AWHO_A6_AaDHPyHCHC.210
+ _get_witness_table 7SwiftUI19_ConditionalContentVyACyAA6VStackVyAA9TupleViewVyAA08ModifiedD0Vy08ContactsB029CNContactGroupArrangedAvatars33_87FAEC429F5A2E07500F09EBFC13C74CLLVAA14_PaddingLayoutVG_AIyAA0K0VyAIyAA4TextVAOGGAA010_FlexFrameV0VGtGGAEyAIyAIyAJ0j16FullAccessPromptK10VisualizerALLLVAOGAXGGGAIyAIyAEyAGyAIyApA01_yV0VG_AIyAIyAIyAIyAA0G0PAAE9lineLimit_13reservesSpaceQrSi_SbtFQOyAIyARyATGAA30_EnvironmentKeyWritingModifierVyAA0W9AlignmentOGG_Qo_A15_yAA4FontVSgGGA15_ySbGGA15_y12CoreGraphics7CGFloatVGGAOGtGGAOGAA24_BackgroundStyleModifierVyAA8MaterialVGGGAAA9_HPA5_AAA9_HPA_AAA9_HPyHC_A4_AAA9_HPyHCHC_A42_AAA9_HPA36_AAA9_HPA35_AAA9_HPyHC_AoA0G8ModifierHPyHCHC_A41_AAA44_HPyHCHCHC.26
+ _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyAA6VStackVyAA05TupleC0VyAaBPAAE12scenePaddingyQrAA4EdgeO3SetVFQOyADy08ContactsB036CNWallpaperSuggestionsGallerySectionV05TitleC0027_C3DE73CB51D4E9D5CF00243C32R4FD8ALLVyx_GAA01_I6LayoutVG_Qo__xtGGAA16_FlexFrameLayoutVGAaBHPA_AaBHPyHC_A1_AA0C8ModifierHPyHCHC.12
+ _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyADyAaBPAAE10fontWeightyQrAA4FontV0G0VSgFQOyADyADyAA4TextVAA30_EnvironmentKeyWritingModifierVyAM4CaseOSgGGAOyAHSgGG_Qo_AOyAA5ColorVSgGGAA16_FixedSizeLayoutVGAaBHPA1_AaBHPqd__AaBHD2_AXHO_A0_AA0cM0HPyHCHC_A3_AAA5_HPyHCHC.28
+ _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyxAA30_EnvironmentKeyWritingModifierVy14ContactsUICore23ContactHeaderAppearanceCGGAaBHPxAaBHD1__AjA0cI0HPyHCHC.19
+ _get_witness_table 7SwiftUI6IDViewVy14ContactsUICore11ContactCardVyAA19_ConditionalContentVy0dB013InlineActionsVSgAI07WrappedjK0VGGSo9CNContactCGAA4ViewHPyHC.3
+ _get_witness_table 7SwiftUI9EmptyViewVAA0D0HPyHC.53
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAE12scenePaddingyQrAA4EdgeO3SetVFQOyAA14GeometryReaderVyAA012SubscriptionC0Vy7Combine10PublishersO5MergeVy_AR3MapVy_So20NSNotificationCenterC10FoundationE9PublisherVSbGA0_GAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAcAE23scrollDismissesKeyboardyQrAA06ScrollZ12KeyboardModeVFQOyAA06ScrollC0VyA3_yAA09_VariadicC0O4TreeVy_AA11_LayoutRootVy08ContactsB035CNWallpaperSuggestionsGalleryLayoutVGAA05TupleC0VyA3_yA15_29CNWallpaperSuggestionsGalleryV011PlaceholderC033_81619BC199BAC997F7A0ACA40B51B6D6LLVAA30_EnvironmentKeyWritingModifierVySo13UIWindowSceneCSgGG_A15_042CNWallpaperSuggestionsGalleryNameTextFieldC0VSgA22_013SourceButtonsC0A24_LLVtGGAA16_FlexFrameLayoutVGG_Qo_AA25_AppearanceActionModifierVG_12CoreGraphics7CGFloatVQo_GG_Qo__A15_35CNWallpaperSuggestionsGallerySourceVSgQo__SbQo__So24CNPRSPosterConfigurationCSgQo__A15_029CNWallpaperSuggestionsGalleryC5ModelC15SuggestedAvatarVSgQo__SSQo__SSQo__SbQo_HO.155
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOy08ContactsB036CNWallpaperSuggestionsGallerySectionVyAA09_VariadicC0O4TreeVy_AA11_LayoutRootVyAJ0jk12SourceButtoncP0VGAA05TupleC0VyAA7ForEachVySayAJ0jklR0VG10Foundation4UUIDVAJ0jkL0V0rS033_81619BC199BAC997F7A0ACA40B51B6D6LLVG_AA15ModifiedContentVyAYySayAJ0jklC5ModelC15SuggestedAvatarVGSSA11_yA5_016AvatarSuggestionS0A7_LLVAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGGA23_GSgtGGG_Qo_HO.209
+ _getkAssistantDirectActionEventKeySymbolLoc.ptr.54902
+ _getkUTTypeJPEGSymbolLoc.ptr.57927
+ _getkUTTypePNGSymbolLoc.ptr.57919
+ _initAFPreferences.46239
+ _initCRRecentContactsLibrary.50577
+ _initFBSOpenApplicationService.50197
+ _initFBSOpenApplicationService.51588
+ _initMIUIDisplayConfiguration.41700
+ _initMIUIMedicalIDViewController.41689
+ _initPHPhotoLibrary.47872
+ _initPHPickerViewController.44784
+ _initializeAvailabilityCheck
+ _keypath_get.8Tm
+ _log.cn_once_object_0.54161
+ _log.cn_once_object_1.15825
+ _log.cn_once_object_1.16574
+ _log.cn_once_object_1.19397
+ _log.cn_once_object_1.19752
+ _log.cn_once_object_1.21796
+ _log.cn_once_object_1.22237
+ _log.cn_once_object_1.24031
+ _log.cn_once_object_1.25678
+ _log.cn_once_object_1.31610
+ _log.cn_once_object_1.31934
+ _log.cn_once_object_1.32059
+ _log.cn_once_object_1.34357
+ _log.cn_once_object_1.35030
+ _log.cn_once_object_1.37638
+ _log.cn_once_object_1.37832
+ _log.cn_once_object_1.40818
+ _log.cn_once_object_1.45144
+ _log.cn_once_object_1.46069
+ _log.cn_once_object_1.48384
+ _log.cn_once_object_1.49384
+ _log.cn_once_object_1.51012
+ _log.cn_once_object_1.51443
+ _log.cn_once_object_1.52783
+ _log.cn_once_object_1.55514
+ _log.cn_once_object_1.58394
+ _log.cn_once_object_1.61109
+ _log.cn_once_object_1.9807
+ _log.cn_once_object_2.38730
+ _log.cn_once_object_2.41742
+ _log.cn_once_object_2.51162
+ _log.cn_once_object_20.44803
+ _log.cn_once_object_20.47884
+ _log.cn_once_object_6.13566
+ _log.cn_once_object_6.23490
+ _log.cn_once_object_6.36055
+ _log.cn_once_object_6.51886
+ _log.cn_once_object_6.66577
+ _log.cn_once_object_9.23583
+ _log.cn_once_token_0.54159
+ _log.cn_once_token_1.15823
+ _log.cn_once_token_1.16572
+ _log.cn_once_token_1.19395
+ _log.cn_once_token_1.19750
+ _log.cn_once_token_1.21794
+ _log.cn_once_token_1.22235
+ _log.cn_once_token_1.24029
+ _log.cn_once_token_1.25676
+ _log.cn_once_token_1.31608
+ _log.cn_once_token_1.31932
+ _log.cn_once_token_1.32057
+ _log.cn_once_token_1.34355
+ _log.cn_once_token_1.35028
+ _log.cn_once_token_1.37636
+ _log.cn_once_token_1.37830
+ _log.cn_once_token_1.40816
+ _log.cn_once_token_1.45142
+ _log.cn_once_token_1.46067
+ _log.cn_once_token_1.48382
+ _log.cn_once_token_1.49382
+ _log.cn_once_token_1.51010
+ _log.cn_once_token_1.51441
+ _log.cn_once_token_1.52781
+ _log.cn_once_token_1.55512
+ _log.cn_once_token_1.58392
+ _log.cn_once_token_1.61107
+ _log.cn_once_token_1.9805
+ _log.cn_once_token_2.38728
+ _log.cn_once_token_2.41740
+ _log.cn_once_token_2.51160
+ _log.cn_once_token_20.44801
+ _log.cn_once_token_20.47882
+ _log.cn_once_token_6.13564
+ _log.cn_once_token_6.23488
+ _log.cn_once_token_6.36053
+ _log.cn_once_token_6.51884
+ _log.cn_once_token_6.66575
+ _log.cn_once_token_9.23581
+ _objc_msgSend$HEICRepresentation
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_addScrollViewScrollObserver:
+ _objc_msgSend$_authenticationMessage
+ _objc_msgSend$_cn_appleAccountAppleID
+ _objc_msgSend$_contentOrObservableScrollViewForEdge:
+ _objc_msgSend$_hasFixedMaximumHeight
+ _objc_msgSend$_hasInProcessContactsDatabaseEntitlement
+ _objc_msgSend$_invalidationContextForRefreshingVisibleElementAttributes
+ _objc_msgSend$_isAnimatingScroll
+ _objc_msgSend$_removeScrollViewScrollObserver:
+ _objc_msgSend$_resolvedLargeTitleMargins
+ _objc_msgSend$_scrollToRevealNavigationBarPart:animated:
+ _objc_msgSend$_setContentOffsetWithDecelerationAnimation:
+ _objc_msgSend$_setCustomVerticalPadding:
+ _objc_msgSend$_setOverrideInlineActiveWidth:
+ _objc_msgSend$_setPreferredNumberOfVisibleIndicators:
+ _objc_msgSend$_setSlotAnyContentProvider:
+ _objc_msgSend$_viewControllerForAncestor
+ _objc_msgSend$addContact:animated:sender:
+ _objc_msgSend$addContactButton
+ _objc_msgSend$addContactsToListTappedWithSender:
+ _objc_msgSend$applyContactListStyleToContact:usingFormatter:ofCell:
+ _objc_msgSend$applyContentConfigurationUsingState:forCell:
+ _objc_msgSend$attributedStringFromContact:defaultAttributes:
+ _objc_msgSend$attributedSubstringFromRange:
+ _objc_msgSend$attributedTextForContact:usingFormatter:isBlocked:hasSubtitle:
+ _objc_msgSend$avatarPosterPairCollectionDidConfirmSelection
+ _objc_msgSend$avatarPosterPairCollectionDidDeleteCurrentPosterPair
+ _objc_msgSend$avatarPosterPairCollectionDidDeletePosterPair
+ _objc_msgSend$avatarPosterPairCollectionDidEditPoster:
+ _objc_msgSend$avatarPosterPairCollectionDidLoadCurrentPairWithAvatar:poster:backedByRecents:
+ _objc_msgSend$avatarPosterPairCollectionDidSelectAvatar:poster:selectionDidChange:isShared:
+ _objc_msgSend$avatarPosterPairCollectionDidSelectCreateNew
+ _objc_msgSend$avatarPosterPairCollectionDidSelectEditAvatar:
+ _objc_msgSend$avatarPosterPairCollectionDidTapDismiss
+ _objc_msgSend$avatarPreviewViewDidFinishWithImageData:cropRect:
+ _objc_msgSend$avatarPreviewViewDidSelectChangeScale
+ _objc_msgSend$avatarPreviewViewDidSelectCustomizePhoto
+ _objc_msgSend$avatarSizeForWidth:
+ _objc_msgSend$avatarViewDidFinishRendering
+ _objc_msgSend$blockedIcon
+ _objc_msgSend$bundleURL
+ _objc_msgSend$callCount
+ _objc_msgSend$canModifySharingLocations
+ _objc_msgSend$cohorts
+ _objc_msgSend$colorsForImageRef:
+ _objc_msgSend$comparatorForNameSortOrder:
+ _objc_msgSend$configureWithQueryString:caption:showMultiSelectContactsPicker:completion:
+ _objc_msgSend$configuredAsBlocked
+ _objc_msgSend$contactListAddContactButtonTapped:sender:
+ _objc_msgSend$contactListViewControllerSelectedAddContactToList:sender:
+ _objc_msgSend$contactListViewControllerSelectedCreateNewContact:sender:
+ _objc_msgSend$contactNameViewWidthContraint
+ _objc_msgSend$contactRelations
+ _objc_msgSend$contentsAndOverlayContentSnapshotDefinitionWithContext:attachmentIdentifiers:
+ _objc_msgSend$convertTime:fromLayer:
+ _objc_msgSend$createNewBlockedIconIfNecessary
+ _objc_msgSend$createNewContactTapped:
+ _objc_msgSend$currentPage
+ _objc_msgSend$currentPreferredSymbolConfiguration
+ _objc_msgSend$currentTraitCollection
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$defaultSettingsWithCacheSize:threeDTouchEnabled:
+ _objc_msgSend$devices
+ _objc_msgSend$didPhotoChangeFromContact:toContact:
+ _objc_msgSend$didSelectCancelMergeDuplicates:
+ _objc_msgSend$didSelectIgnoreAllDuplicates:signaturesIgnored:
+ _objc_msgSend$didSelectMergeAllDuplicates:signaturesToMerge:
+ _objc_msgSend$didSelectUnignoreDuplicate:
+ _objc_msgSend$disambiguationMenuForActionType:
+ _objc_msgSend$displayCornerRadius
+ _objc_msgSend$donateUpdatedContact:
+ _objc_msgSend$editInAppAction
+ _objc_msgSend$editingToolbar
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$ensureContactStoreExists
+ _objc_msgSend$executeAddContact:
+ _objc_msgSend$executeFetchRequest:error:
+ _objc_msgSend$executeTapBehaviorWithoutDisambiguationForActionType:
+ _objc_msgSend$fetchColorsForImage:ciContext:withCompletionHandler:
+ _objc_msgSend$fetchColorsForImage:withCompletionHandler:
+ _objc_msgSend$fetchTintedAvatarColorsFor:completionHandler:
+ _objc_msgSend$fileNameForContactName:
+ _objc_msgSend$finalizedConfiguration:forExtensionIdentifier:
+ _objc_msgSend$formattedHandle
+ _objc_msgSend$getRecentCallCountAndSpeakableName
+ _objc_msgSend$getRemoteContentForStyle:layerContext:queryString:currentFrame:ignoredEmails:ignoredPhones:traitData:sbExtension:with:
+ _objc_msgSend$imageDataFromMetadata:
+ _objc_msgSend$imageFromMetadata:size:completionHandler:
+ _objc_msgSend$incomingCallAvatarSnapshotForAvatarImageData:contact:windowScene:completionBlock:
+ _objc_msgSend$incomingCallSnapshotForConfiguration:nameString:includingCallButtons:windowScene:completionBlock:
+ _objc_msgSend$indexPathForItemAtPoint:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initForAppName:bundleId:
+ _objc_msgSend$initForInlineContactCardWithContact:
+ _objc_msgSend$initPickerWithContactsAvailableToAddForAppName:bundleId:searchText:caption:
+ _objc_msgSend$initWithActionTypes:contactQuickActionViewContainer:
+ _objc_msgSend$initWithAssetUUID:
+ _objc_msgSend$initWithCGColor:
+ _objc_msgSend$initWithCGImage:
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$initWithConfiguration:view:
+ _objc_msgSend$initWithConfigurationType:
+ _objc_msgSend$initWithContact:contactStore:actionsProvider:customViewConfiguration:propertyViewConfiguration:isInlineContactCard:geminiManager:isOutOfProcess:
+ _objc_msgSend$initWithContact:propertyItems:actionsDataSource:
+ _objc_msgSend$initWithContact:propertyItems:favorites:actionsDataSource:
+ _objc_msgSend$initWithContacts:listener:contactStore:
+ _objc_msgSend$initWithContext:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithHandle:handleType:createDate:expiry:origin:originatedFromTheSameClient:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:imageData:cropRect:lastUsedDate:
+ _objc_msgSend$initWithIdentifier:posterData:lastUsedDate:itemDetails:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithPosterArchiveData:metadata:contentIsSensitive:sharedToMe:
+ _objc_msgSend$initWithRed:green:blue:alpha:
+ _objc_msgSend$initWithService:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$insertNewItemIntoSuggestions:
+ _objc_msgSend$invalidateLayoutWithContext:
+ _objc_msgSend$isScrollEnabled
+ _objc_msgSend$isShowingGroups
+ _objc_msgSend$isTracking
+ _objc_msgSend$italicSystemFontOfSize:
+ _objc_msgSend$keyPath
+ _objc_msgSend$layoutAttributesForCellWithIndexPath:
+ _objc_msgSend$layoutAttributesForSupplementaryViewOfKind:atIndexPath:
+ _objc_msgSend$layoutAttributesForSupplementaryViewOfKind:withIndexPath:
+ _objc_msgSend$locationSharingModificationCheck
+ _objc_msgSend$locationSharingModificationState
+ _objc_msgSend$lock
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$makeXPCConnectionWithError:
+ _objc_msgSend$maximumWidthForNameView
+ _objc_msgSend$nextResponder
+ _objc_msgSend$notificationOccurred:
+ _objc_msgSend$numberOfPages
+ _objc_msgSend$onPrimaryTouchUpEvent:with:
+ _objc_msgSend$onboardingPrivacyViewDidTapCancel
+ _objc_msgSend$onboardingPrivacyViewDidTapContinue
+ _objc_msgSend$onboardingWelcomeViewDidTapCancel
+ _objc_msgSend$onboardingWelcomeViewDidTapContinue
+ _objc_msgSend$orientation
+ _objc_msgSend$overestimatedCount
+ _objc_msgSend$packageWithContentsOfURL:type:options:error:
+ _objc_msgSend$pairedPoster
+ _objc_msgSend$poseHasBody
+ _objc_msgSend$presentAddToGroupPickerWithSender:
+ _objc_msgSend$previewViewDidCreateWithPosterConfiguration:
+ _objc_msgSend$previewViewDidFinishWithPosterConfiguration:
+ _objc_msgSend$previewViewDidSelectUseDifferentPoster
+ _objc_msgSend$primaryID
+ _objc_msgSend$privateConfigurationForTypes:
+ _objc_msgSend$processName
+ _objc_msgSend$publishedObjectWithName:
+ _objc_msgSend$rawImageSource
+ _objc_msgSend$recentImagesRequestForContactIdentifiers:
+ _objc_msgSend$recentPostersForContactWithIdentifier:
+ _objc_msgSend$refreshForCurrentlySelectedContact
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$requestForConfiguration:definition:interfaceOrientation:windowScene:attachments:
+ _objc_msgSend$requestToDeleteImageForIdentifiers:
+ _objc_msgSend$requestToDeletePosterForIdentifiers:
+ _objc_msgSend$rootLayer
+ _objc_msgSend$save:
+ _objc_msgSend$saveToURL:error:
+ _objc_msgSend$serviceIdentifier
+ _objc_msgSend$setAllowsContinuousInteraction:
+ _objc_msgSend$setAlwaysBounceHorizontal:
+ _objc_msgSend$setBackgroundColors:
+ _objc_msgSend$setBlockedIcon:
+ _objc_msgSend$setConfiguredAsBlocked:
+ _objc_msgSend$setContactNameViewWidthContraint:
+ _objc_msgSend$setContentSize:
+ _objc_msgSend$setCropRectString:
+ _objc_msgSend$setCurrentPage:
+ _objc_msgSend$setCurrentPageIndicatorTintColor:
+ _objc_msgSend$setDecelerationRate:
+ _objc_msgSend$setEditInAppAction:
+ _objc_msgSend$setHidesForSinglePage:
+ _objc_msgSend$setHidesSharedBackground:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsAvailable:
+ _objc_msgSend$setMedia:
+ _objc_msgSend$setModelTrackingDelegate:
+ _objc_msgSend$setNamePrefix:
+ _objc_msgSend$setNameSuffix:
+ _objc_msgSend$setNickname:
+ _objc_msgSend$setOverrideUserInterfaceStyle:
+ _objc_msgSend$setPageIndicatorTintColor:
+ _objc_msgSend$setPosterData:
+ _objc_msgSend$setPreferredPresentationStyle:
+ _objc_msgSend$setPreferredTransition:
+ _objc_msgSend$setPrefersGrabberVisible:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setScrollsToTop:
+ _objc_msgSend$setSectionHeaderTopPadding:
+ _objc_msgSend$setSelectedContactImage:
+ _objc_msgSend$setSelectedContactPoster:
+ _objc_msgSend$setSpeed:
+ _objc_msgSend$setTimeOffset:
+ _objc_msgSend$setTintAdjustmentMode:
+ _objc_msgSend$setZIndex:
+ _objc_msgSend$sharedToMe
+ _objc_msgSend$showContactPhotos
+ _objc_msgSend$signature
+ _objc_msgSend$sizeForNumberOfPages:
+ _objc_msgSend$sizeThatFitsWithProposalWidth:proposalHeight:with:
+ _objc_msgSend$speakableName
+ _objc_msgSend$startOnboardingOrEditForMode:fromViewController:
+ _objc_msgSend$suggestionsGalleryDidFinishWithPosterConfiguration:posterType:withGivenName:familyName:
+ _objc_msgSend$suggestionsGalleryDidRequestPresentationOfImagePickerController:
+ _objc_msgSend$suggestionsGalleryDidRequestPresentationOfPosterEditingViewController:
+ _objc_msgSend$suggestionsGalleryDidSelectAvatarSourceType:withGivenName:familyName:
+ _objc_msgSend$suggestionsGalleryDidSelectSuggestedAvatar:withGivenName:familyName:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$systemGray2Color
+ _objc_msgSend$targetProfileForActionType:context:
+ _objc_msgSend$timeOffset
+ _objc_msgSend$toolbarButtonItemsForTraitCollection:
+ _objc_msgSend$transform
+ _objc_msgSend$uniqueID
+ _objc_msgSend$unlock
+ _objc_msgSend$updateSearchBarMaxSizeWithSize:
+ _objc_msgSend$urlAddresses
+ _objc_msgSend$useVerticalLayoutForWidth:
+ _objc_msgSend$validateSiriEnabled
+ _objc_msgSend$validateSiriLanguage
+ _objc_msgSend$viewContext
+ _objc_msgSend$visibleSize
+ _objc_msgSend$visualIdentityEditorViewControllerDidFinishEditing:
+ _objc_msgSend$wallpaperMetadata
+ _objc_msgSend$zoomWithOptions:sourceBarButtonItemProvider:
+ _objc_msgSend$zoomWithOptions:sourceViewProvider:
+ _objectdestroy.157Tm
+ _objectdestroy.184Tm
+ _objectdestroy.53Tm
+ _objectdestroy.85Tm
+ _os_log.cn_once_object_1.10350
+ _os_log.cn_once_object_1.63697
+ _os_log.cn_once_object_1.64216
+ _os_log.cn_once_object_1.9474
+ _os_log.cn_once_object_6.53722
+ _os_log.cn_once_object_6.66183
+ _os_log.cn_once_token_1.10348
+ _os_log.cn_once_token_1.63695
+ _os_log.cn_once_token_1.64214
+ _os_log.cn_once_token_1.9472
+ _os_log.cn_once_token_6.53720
+ _os_log.cn_once_token_6.66181
+ _pathToContentUnavailableRow.cn_once_object_30
+ _pathToContentUnavailableRow.cn_once_token_30
+ _pathToCreateNewContactRow.cn_once_object_29
+ _pathToCreateNewContactRow.cn_once_token_29
+ _pathToDuplicatesBanner.cn_once_object_28
+ _pathToDuplicatesBanner.cn_once_token_28
+ _pathToLimitedAccessTipRow.cn_once_object_17
+ _pathToLimitedAccessTipRow.cn_once_token_17
+ _rewind
+ _sscanf
+ _supportedPasteboardTypes.cn_once_object_1.51458
+ _supportedPasteboardTypes.cn_once_token_1.51456
+ _symbolic SaySSGSg
+ _symbolic SdSg
+ _symbolic So14CNContactStoreCSg
+ _symbolic So31CNContactQuickActionsControllerCSg
+ _symbolic _____ 10ContactsUI22CNUIVisualIdentityTypeO
+ _symbolic _____ 10ContactsUI23ContactHeaderAppearanceC
+ _symbolic _____ 10ContactsUI32ContactCardSwiftUIViewControllerC8RootViewV
+ _symbolic _____ 14ContactsUICore23ContactHeaderAppearanceC
+ _symbolic _____Sg 10ContactsUI13InlineActionsV
+ _symbolic _____Sg 10ContactsUI45CNContactHeaderQuickActionsControllerObserver33_3062C0EB640D5F51DAD6AB600DEB05B6LLC
+ _symbolic _____Sg 14ContactsUICore18VisualIdentityTypeO
+ _symbolic _____Sg_ABt 10ContactsUI35CNWallpaperSuggestionsGallerySourceV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____yAAyAAyAAy__________G_____ySo7UIImageCSgGG_____GAKG 7SwiftUI15ModifiedContentV 08ContactsB025CNPosterSnapshotImageViewV AA12_FrameLayoutV AA18_AnimationModifierV AA08_PaddingK0V
+ _symbolic _____yAAyAAyAAy__________G_____y_____GGAEy_____GG_____G 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO 12CoreGraphics7CGFloatV AA08_PaddingH0V
+ _symbolic _____yAAyAAyAAy__________ySiSgGGACy_____GGACySbGGACy_____GG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO 12CoreGraphics7CGFloatV
+ _symbolic _____yAAyAAy__________G_____G_____G 7SwiftUI15ModifiedContentV 08ContactsB017ContactAvatarView33_87FAEC429F5A2E07500F09EBFC13C74CLLV AA12_FrameLayoutV AA11_BlurEffectV AA07_OffsetS0V
+ _symbolic _____yAAyAAy__________G_____ySo7UIImageCSgGG_____G 7SwiftUI15ModifiedContentV 08ContactsB025CNPosterSnapshotImageViewV AA12_FrameLayoutV AA18_AnimationModifierV AA08_PaddingK0V
+ _symbolic _____yAAyAAy__________G_____y_____GGAEy_____GG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO 12CoreGraphics7CGFloatV
+ _symbolic _____yAAyAAy__________G_____y_____GG_____G 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO AA08_PaddingH0V
+ _symbolic _____yAAyAAy__________ySiSgGGACy_____GGACySbGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08ContactsB017ContactAvatarView33_87FAEC429F5A2E07500F09EBFC13C74CLLV AA12_FrameLayoutV AA11_BlurEffectV
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08ContactsB039CNPosterOnboardingSettingsAnimationViewV AA18_AspectRatioLayoutV AA010_FlexFrameM0V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08ContactsB040CNContactFullAccessPromptGroupVisualizer33_87FAEC429F5A2E07500F09EBFC13C74CLLV AA14_PaddingLayoutV AA010_FlexFrameT0V
+ _symbolic _____yAAy__________G_____ySo7UIImageCSgGG 7SwiftUI15ModifiedContentV 08ContactsB025CNPosterSnapshotImageViewV AA12_FrameLayoutV AA18_AnimationModifierV
+ _symbolic _____yAAy__________G_____ySo9CNContactCGG 7SwiftUI15ModifiedContentV 08ContactsB0015ContactCardViewaB0V AA25_AppearanceActionModifierV AA19_TaskValueModifier2V
+ _symbolic _____yAAy__________G_____ySo9CNContactCGG 7SwiftUI15ModifiedContentV 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AA19_TaskValueModifier2V
+ _symbolic _____yAAy__________G_____y_____GG 7SwiftUI15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO
+ _symbolic _____yAAy__________ySiSgGGACy_____GG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO
+ _symbolic _____yAAy__________y_____GGACy_____SgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO AA4FontV
+ _symbolic _____yAAy_____y__________G_____G_____G 7SwiftUI15ModifiedContentV AA10_ShapeViewV AA9RectangleV AA5ColorV AA18_AspectRatioLayoutV AA010_FlexFrameK0V
+ _symbolic _____yAAy_____y_____yAAy__________y_____GGSgG_Qo______G_____G 7SwiftUI15ModifiedContentV AA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA6ButtonV 08ContactsB008CNAvatare10ControllerE0V AA21_TraitWritingModifierV AA010TransitionO3KeyV AA14_PaddingLayoutV AA17_FlipForRTLEffectV
+ _symbolic _____ySo9CNContactCG 7SwiftUI19_TaskValueModifier2V
+ _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 08ContactsB0011ContactCarda6UIViewD0C8RootViewV
+ _symbolic _____y_____G 7SwiftUI30_EnvironmentKeyWritingModifierV 14ContactsUICore23ContactHeaderAppearanceC
+ _symbolic _____y_____GSg 7SwiftUI19UIHostingControllerC 08ContactsB0011ContactCarda6UIViewD0C8RootViewV
+ _symbolic _____y_____Sg_____G 7SwiftUI19_ConditionalContentV 08ContactsB013InlineActionsV AD07WrappedfG0V
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 08ContactsB025CNPosterSnapshotImageViewV AA12_FrameLayoutV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 08ContactsB039CNPosterOnboardingSettingsAnimationViewV AA18_AspectRatioLayoutV
+ _symbolic _____y__________y_____GG 7SwiftUI15ModifiedContentV 14ContactsUICore10HeaderViewV AA30_EnvironmentKeyWritingModifierV AD23ContactCardDetailsStyleV
+ _symbolic _____y_____yAAy__________y_____GGSgG_____G 7SwiftUI15ModifiedContentV AA6ButtonV 08ContactsB0022CNAvatarViewControllerH0V AA21_TraitWritingModifierV AA010TransitionJ3KeyV AA14_TaskModifier2V
+ _symbolic _____y_____y__________GG 7SwiftUI5GroupV AA15ModifiedContentV AA4TextV AA14_PaddingLayoutV
+ _symbolic _____y_____y__________G_So9CNContactCQo_ 7SwiftUI4ViewPAAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQO AA15ModifiedContentV 08ContactsB0011ContactCardcaB0V AA25_AppearanceActionModifierV
+ _symbolic _____y_____y__________G_So9CNContactCQo_ 7SwiftUI4ViewPAAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQO AA15ModifiedContentV 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV
+ _symbolic _____y_____y________________yAC_____GtGG 7SwiftUI6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA15ModifiedContentV AA16_FlexFrameLayoutV
+ _symbolic _____y_____y_____yAAy__________y_____GGSgG_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA6ButtonV 08ContactsB008CNAvatare10ControllerE0V AA21_TraitWritingModifierV AA010TransitionO3KeyV AA14_PaddingLayoutV
+ _symbolic _____y_____y_____y_____Sg_____GGSo9CNContactCG 7SwiftUI6IDViewV 14ContactsUICore11ContactCardV AA19_ConditionalContentV 0dB013InlineActionsV AI07WrappedjK0V
+ _symbolic _____y_____y_____y__________G_So9CNContactCQo______yABy_____ADG_AGQo_G 7SwiftUI19_ConditionalContentV AA4ViewPAAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQO AA08ModifiedD0V 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AeAEAfghijK_Qrqd___ALScPSSSiyyYaYAcntSQRd__lFQO AO011ContactCardeaB0V
+ _symbolic _____y_____y_____y__________G_So9CNContactCQo______yABy_____ADG_AGQo__G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE4task2id4name8priority4file4line_Qrqd___SSSgScPSSSiyyYaYAcntSQRd__lFQO AA08ModifiedD0V 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AgAEAhijklM_Qrqd___ANScPSSSiyyYaYAcntSQRd__lFQO AQ011ContactCardfaB0V
+ _symbolic _____y_____y_____y______y_____G_____y_____ySay_____G__________G_AAyAHySay_____GSSAAy__________y_____GGGASGSgtGGG_____G 7SwiftUI15ModifiedContentV 08ContactsB036CNWallpaperSuggestionsGallerySectionV AA13_VariadicViewO4TreeV AA11_LayoutRootV AD0fg12SourceButtonkM0V AA05TupleK0V AA7ForEachV AD0fghO0V 10Foundation4UUIDV AD0fgH0V0oP033_81619BC199BAC997F7A0ACA40B51B6D6LLV AD0fghK5ModelC15SuggestedAvatarV AY016AvatarSuggestionP0A_LLV AA21_TraitWritingModifierV AA18TransitionTraitKeyV AA14_TaskModifier2V
+ _symbolic _____y_____y_____y______y_____G_____y_____ySay_____G__________G______yAGySay_____GSSAMy__________y_____GGGASGSgtGGG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO 08ContactsB036CNWallpaperSuggestionsGallerySectionV AA09_VariadicC0O4TreeV AA11_LayoutRootV AJ0jk12SourceButtoncP0V AA05TupleC0V AA7ForEachV AJ0jklR0V 10Foundation4UUIDV AJ0jkL0V0rS033_81619BC199BAC997F7A0ACA40B51B6D6LLV AA15ModifiedContentV AJ0jklC5ModelC15SuggestedAvatarV A3_016AvatarSuggestionS0A5_LLV AA21_TraitWritingModifierV AA18TransitionTraitKeyV
+ _symbolic _____yx_____y_____GG 7SwiftUI15ModifiedContentV AA30_EnvironmentKeyWritingModifierV 14ContactsUICore23ContactHeaderAppearanceC
+ _symbolic qd0__
+ _yearlessFormatter.44242
- -[CNContactAddFavoriteAction initWithContact:propertyItems:favorites:]
- -[CNContactListStyleApplier applyContactListStyleToBlockedIcon:ofCell:]
- -[CNContactListStyleApplier applyContactListStyleToContact:usingFormatter:ofCell:wantsInlineBlockIcon:]
- -[CNContactListStyleApplier applyContactListStyleToContentConfiguration:usingState:forCell:]
- -[CNContactListStyleApplier createNewBlockedIcon]
- -[CNContactListViewController addContactsToListTappedWithSourceView:]
- -[CNContactListViewController createNewContactTapped]
- -[CNContactNavigationController contactListAddContactButtonTapped:]
- -[CNContactNavigationController contactListViewControllerSelectedAddContactToList:withSourceView:]
- -[CNContactNavigationController contactListViewControllerSelectedCreateNewContact:]
- -[CNContactNavigationController executeAddContact]
- -[CNContactNavigationController presentAddToGroupPickerWithSourceView:]
- -[CNPropertySendMessageAction initWithContact:propertyItems:actionDataSource:]
- -[CNSharedProfileBannerView avatarSize]
- -[CNSharedProfileBannerView layoutSubviews]
- -[CNStarkContactViewController viewWillLayoutSubviews]
- GCC_except_table10032
- GCC_except_table10038
- GCC_except_table10260
- GCC_except_table10461
- GCC_except_table10475
- GCC_except_table10489
- GCC_except_table10744
- GCC_except_table10746
- GCC_except_table10815
- GCC_except_table10816
- GCC_except_table10817
- GCC_except_table11112
- GCC_except_table11118
- GCC_except_table11169
- GCC_except_table11173
- GCC_except_table11377
- GCC_except_table11562
- GCC_except_table11567
- GCC_except_table11570
- GCC_except_table11580
- GCC_except_table11583
- GCC_except_table11593
- GCC_except_table11607
- GCC_except_table11632
- GCC_except_table11690
- GCC_except_table11800
- GCC_except_table11893
- GCC_except_table11919
- GCC_except_table12038
- GCC_except_table12100
- GCC_except_table12162
- GCC_except_table12163
- GCC_except_table12173
- GCC_except_table12174
- GCC_except_table12601
- GCC_except_table12618
- GCC_except_table12639
- GCC_except_table12937
- GCC_except_table12971
- GCC_except_table13074
- GCC_except_table13271
- GCC_except_table13339
- GCC_except_table13345
- GCC_except_table13419
- GCC_except_table13420
- GCC_except_table13428
- GCC_except_table13508
- GCC_except_table13513
- GCC_except_table13686
- GCC_except_table13705
- GCC_except_table13854
- GCC_except_table13883
- GCC_except_table13884
- GCC_except_table14018
- GCC_except_table14104
- GCC_except_table14111
- GCC_except_table14148
- GCC_except_table14406
- GCC_except_table14409
- GCC_except_table14515
- GCC_except_table14534
- GCC_except_table14801
- GCC_except_table14873
- GCC_except_table14994
- GCC_except_table14998
- GCC_except_table15072
- GCC_except_table15138
- GCC_except_table15146
- GCC_except_table15148
- GCC_except_table15152
- GCC_except_table15342
- GCC_except_table15443
- GCC_except_table15523
- GCC_except_table15527
- GCC_except_table15545
- GCC_except_table15595
- GCC_except_table15718
- GCC_except_table16023
- GCC_except_table16038
- GCC_except_table16054
- GCC_except_table16067
- GCC_except_table16068
- GCC_except_table16072
- GCC_except_table16073
- GCC_except_table16169
- GCC_except_table16555
- GCC_except_table16557
- GCC_except_table16566
- GCC_except_table16660
- GCC_except_table16723
- GCC_except_table16763
- GCC_except_table16893
- GCC_except_table17170
- GCC_except_table17174
- GCC_except_table17636
- GCC_except_table17653
- GCC_except_table17705
- GCC_except_table17715
- GCC_except_table17758
- GCC_except_table17778
- GCC_except_table17810
- GCC_except_table17811
- GCC_except_table17818
- GCC_except_table17819
- GCC_except_table17844
- GCC_except_table17971
- GCC_except_table17981
- GCC_except_table17997
- GCC_except_table18001
- GCC_except_table18005
- GCC_except_table18007
- GCC_except_table18053
- GCC_except_table18255
- GCC_except_table18312
- GCC_except_table18313
- GCC_except_table18320
- GCC_except_table18325
- GCC_except_table18330
- GCC_except_table18339
- GCC_except_table18342
- GCC_except_table18367
- GCC_except_table18389
- GCC_except_table18407
- GCC_except_table18419
- GCC_except_table18426
- GCC_except_table18427
- GCC_except_table18430
- GCC_except_table18432
- GCC_except_table18434
- GCC_except_table18447
- GCC_except_table18588
- GCC_except_table2100
- GCC_except_table2183
- GCC_except_table2881
- GCC_except_table2947
- GCC_except_table3021
- GCC_except_table3022
- GCC_except_table3023
- GCC_except_table3138
- GCC_except_table3268
- GCC_except_table3440
- GCC_except_table3442
- GCC_except_table3575
- GCC_except_table3577
- GCC_except_table3655
- GCC_except_table3770
- GCC_except_table3975
- GCC_except_table3976
- GCC_except_table4146
- GCC_except_table4188
- GCC_except_table4222
- GCC_except_table4339
- GCC_except_table4429
- GCC_except_table4701
- GCC_except_table4743
- GCC_except_table4753
- GCC_except_table4914
- GCC_except_table4955
- GCC_except_table5029
- GCC_except_table5030
- GCC_except_table5036
- GCC_except_table5038
- GCC_except_table5093
- GCC_except_table5113
- GCC_except_table5154
- GCC_except_table5161
- GCC_except_table5162
- GCC_except_table5226
- GCC_except_table5372
- GCC_except_table5739
- GCC_except_table5748
- GCC_except_table5839
- GCC_except_table5867
- GCC_except_table5875
- GCC_except_table5990
- GCC_except_table6163
- GCC_except_table6309
- GCC_except_table6325
- GCC_except_table6624
- GCC_except_table6663
- GCC_except_table6736
- GCC_except_table6914
- GCC_except_table6919
- GCC_except_table7050
- GCC_except_table7126
- GCC_except_table7268
- GCC_except_table7520
- GCC_except_table7618
- GCC_except_table8015
- GCC_except_table8072
- GCC_except_table8106
- GCC_except_table8222
- GCC_except_table8266
- GCC_except_table8645
- GCC_except_table8688
- GCC_except_table8753
- GCC_except_table8759
- GCC_except_table8927
- GCC_except_table8961
- GCC_except_table9001
- GCC_except_table9025
- GCC_except_table9090
- GCC_except_table9217
- GCC_except_table9221
- GCC_except_table9347
- GCC_except_table9348
- GCC_except_table9354
- GCC_except_table9360
- GCC_except_table9367
- GCC_except_table9372
- GCC_except_table9382
- GCC_except_table9385
- GCC_except_table9399
- GCC_except_table9405
- GCC_except_table9408
- GCC_except_table9411
- GCC_except_table9413
- GCC_except_table9619
- GCC_except_table9627
- GCC_except_table9702
- GCC_except_table9705
- GCC_except_table9800
- GCC_except_table9838
- GCC_except_table9853
- GCC_except_table9858
- _AFPreferencesFunction.46302
- _AssistantServicesLibraryCore.frameworkLibrary.49061
- _AssistantServicesLibraryCore.frameworkLibrary.54978
- _AvatarKitLibraryCore.frameworkLibrary.30486
- _AvatarKitLibraryCore.frameworkLibrary.32935
- _AvatarKitLibraryCore.frameworkLibrary.51028
- _AvatarKitLibraryCore.frameworkLibrary.55541
- _AvatarUILibrary.19913
- _AvatarUILibrary.32916
- _AvatarUILibrary.37873
- _AvatarUILibrary.41976
- _AvatarUILibrary.53442
- _AvatarUILibraryCore.frameworkLibrary.13180
- _AvatarUILibraryCore.frameworkLibrary.16196
- _AvatarUILibraryCore.frameworkLibrary.19924
- _AvatarUILibraryCore.frameworkLibrary.30502
- _AvatarUILibraryCore.frameworkLibrary.32923
- _AvatarUILibraryCore.frameworkLibrary.33739
- _AvatarUILibraryCore.frameworkLibrary.34419
- _AvatarUILibraryCore.frameworkLibrary.36609
- _AvatarUILibraryCore.frameworkLibrary.37882
- _AvatarUILibraryCore.frameworkLibrary.41986
- _AvatarUILibraryCore.frameworkLibrary.53449
- _AvatarUILibraryCore.frameworkLibrary.55517
- _AvatarUILibraryCore.frameworkLibrary.6080
- _CGSizeMake
- _CRRecentContactsLibraryFunction.50640
- _FBSOpenApplicationServiceFunction.50261
- _FBSOpenApplicationServiceFunction.51654
- _GameCenterFoundationLibraryCore.frameworkLibrary.42274
- _GameCenterFoundationLibraryCore.frameworkLibrary.49641
- _GameCenterUICoreLibraryCore.frameworkLibrary.42257
- _GameCenterUILibraryCore.frameworkLibrary.49610
- _HealthKitLibraryCore.frameworkLibrary.41793
- _IDSLibrary.23049
- _IDSLibrary.46382
- _IDSLibraryCore.frameworkLibrary.23085
- _IDSLibraryCore.frameworkLibrary.31033
- _IDSLibraryCore.frameworkLibrary.42789
- _IDSLibraryCore.frameworkLibrary.46398
- _IDSLibraryCore.frameworkLibrary.50626
- _IDSLibraryCore.frameworkLibrary.52252
- _IMCoreLibraryCore.frameworkLibrary.10734
- _IMCoreLibraryCore.frameworkLibrary.47479
- _IMCoreLibraryCore.frameworkLibrary.64591
- _IntlPreferencesUILibraryCore.frameworkLibrary.13931
- _IntlPreferencesUILibraryCore.frameworkLibrary.58518
- _LoadAppleAccount.frameworkLibrary.51410
- _LoadAppleAccount.loadPredicate.51403
- _LoadAssistantServices.frameworkLibrary.46307
- _LoadAssistantServices.loadPredicate.46297
- _LoadCarPlayServices.frameworkLibrary.50266
- _LoadCarPlayServices.frameworkLibrary.51659
- _LoadCarPlayServices.loadPredicate.50256
- _LoadCarPlayServices.loadPredicate.51649
- _LoadCoreRecents.frameworkLibrary.50644
- _LoadCoreRecents.loadPredicate.50636
- _LoadCoreSuggestions.frameworkLibrary.50622
- _LoadCoreSuggestions.loadPredicate.50618
- _LoadMapKit.frameworkLibrary.22240
- _LoadMapKit.frameworkLibrary.24518
- _LoadMapKit.loadPredicate.22233
- _LoadMapKit.loadPredicate.24515
- _LoadMedicalIDUI.frameworkLibrary.41776
- _LoadMedicalIDUI.loadPredicate.41769
- _LoadPhotos.frameworkLibrary.38377
- _LoadPhotos.frameworkLibrary.44809
- _LoadPhotos.frameworkLibrary.47921
- _LoadPhotos.loadPredicate.38373
- _LoadPhotos.loadPredicate.44806
- _LoadPhotos.loadPredicate.47916
- _LoadPhotosUI.frameworkLibrary.44849
- _LoadPhotosUI.loadPredicate.44841
- _MIUIDisplayConfigurationFunction.41783
- _MIUIMedicalIDViewControllerFunction.41772
- _MobileCoreServicesLibrary.57968
- _MobileCoreServicesLibraryCore.frameworkLibrary.47319
- _MobileCoreServicesLibraryCore.frameworkLibrary.57978
- _PHPhotoLibraryFunction.47937
- _PHPickerViewControllerFunction.44845
- _PosterBoardServicesLibrary.65505
- _PosterBoardServicesLibraryCore.frameworkLibrary.65512
- _PosterBoardUIServicesLibraryCore.frameworkLibrary.65563
- _PosterKitLibraryCore.frameworkLibrary.65702
- _SharingLibraryCore.frameworkLibrary.64630
- _SiriActivationLibrary.54960
- _SiriActivationLibraryCore.frameworkLibrary.54966
- _SocialLibraryCore.frameworkLibrary.22625
- _SocialLibraryCore.frameworkLibrary.59621
- _SocialLibraryCore.frameworkLibrary.64733
- _ToneKitLibraryCore.frameworkLibrary.57741
- _UIMenuApplication
- __OBJC_$_PROP_LIST_CNContactListAction.9853
- __OBJC_$_PROP_LIST_CNContactPickerContentViewController.479
- ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke.87
- ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke.92
- ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke_2.93
- ___48-[CNAccountsAndGroupsDataSource _reloadSections]_block_invoke_3.95
- ___49-[CNContactContentEditViewController setContact:]_block_invoke.368
- ___49-[CNContactViewController _prepareViewController]_block_invoke.93
- ___52-[CNContactContentDisplayViewController setContact:]_block_invoke.368
- ___56-[CNHealthStoreManager notifyHandlersWithMedicalIDData:]_block_invoke.321
- ___58-[CNContactListViewController contactDataSourceDidChange:]_block_invoke.584
- ___67-[CNContactContentUnitaryViewController performSaveToSharedProfile]_block_invoke.508
- ___69-[CNContactContentDisplayViewController reloadDataPreservingChanges:]_block_invoke.380
- ___69-[CNContactContentUnitaryViewController reloadDataPreservingChanges:]_block_invoke.456
- ___70-[CNContactContentUnitaryViewController setContact:shouldScrollToTop:]_block_invoke.426
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.298
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.320
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke.327
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_2.322
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_3.324
- ___74-[CNEmergencyContactAction performActionWithContactProperty:relationship:]_block_invoke_4.326
- ___AssistantServicesLibraryCore_block_invoke.49062
- ___AssistantServicesLibraryCore_block_invoke.54979
- ___AvatarKitLibraryCore_block_invoke.30487
- ___AvatarKitLibraryCore_block_invoke.32936
- ___AvatarKitLibraryCore_block_invoke.51029
- ___AvatarKitLibraryCore_block_invoke.55542
- ___AvatarUILibraryCore_block_invoke.13181
- ___AvatarUILibraryCore_block_invoke.16197
- ___AvatarUILibraryCore_block_invoke.19925
- ___AvatarUILibraryCore_block_invoke.30503
- ___AvatarUILibraryCore_block_invoke.32924
- ___AvatarUILibraryCore_block_invoke.33740
- ___AvatarUILibraryCore_block_invoke.34420
- ___AvatarUILibraryCore_block_invoke.36610
- ___AvatarUILibraryCore_block_invoke.37883
- ___AvatarUILibraryCore_block_invoke.41987
- ___AvatarUILibraryCore_block_invoke.53450
- ___AvatarUILibraryCore_block_invoke.55518
- ___AvatarUILibraryCore_block_invoke.6081
- ___Block_byref_object_copy_.13598
- ___Block_byref_object_copy_.14816
- ___Block_byref_object_copy_.16477
- ___Block_byref_object_copy_.16896
- ___Block_byref_object_copy_.19315
- ___Block_byref_object_copy_.21845
- ___Block_byref_object_copy_.22608
- ___Block_byref_object_copy_.23640
- ___Block_byref_object_copy_.2407
- ___Block_byref_object_copy_.24091
- ___Block_byref_object_copy_.27031
- ___Block_byref_object_copy_.2847
- ___Block_byref_object_copy_.29345
- ___Block_byref_object_copy_.30755
- ___Block_byref_object_copy_.32001
- ___Block_byref_object_copy_.32088
- ___Block_byref_object_copy_.32931
- ___Block_byref_object_copy_.33164
- ___Block_byref_object_copy_.34414
- ___Block_byref_object_copy_.36584
- ___Block_byref_object_copy_.38368
- ___Block_byref_object_copy_.3956
- ___Block_byref_object_copy_.4198
- ___Block_byref_object_copy_.44520
- ___Block_byref_object_copy_.47930
- ___Block_byref_object_copy_.48808
- ___Block_byref_object_copy_.51022
- ___Block_byref_object_copy_.52039
- ___Block_byref_object_copy_.53071
- ___Block_byref_object_copy_.54713
- ___Block_byref_object_copy_.55867
- ___Block_byref_object_copy_.56891
- ___Block_byref_object_copy_.59544
- ___Block_byref_object_copy_.62465
- ___Block_byref_object_copy_.64202
- ___Block_byref_object_copy_.64639
- ___Block_byref_object_dispose_.13599
- ___Block_byref_object_dispose_.14817
- ___Block_byref_object_dispose_.16478
- ___Block_byref_object_dispose_.16897
- ___Block_byref_object_dispose_.19316
- ___Block_byref_object_dispose_.21846
- ___Block_byref_object_dispose_.22609
- ___Block_byref_object_dispose_.23641
- ___Block_byref_object_dispose_.2408
- ___Block_byref_object_dispose_.24092
- ___Block_byref_object_dispose_.27032
- ___Block_byref_object_dispose_.2848
- ___Block_byref_object_dispose_.29346
- ___Block_byref_object_dispose_.30756
- ___Block_byref_object_dispose_.32002
- ___Block_byref_object_dispose_.32089
- ___Block_byref_object_dispose_.32932
- ___Block_byref_object_dispose_.33165
- ___Block_byref_object_dispose_.34415
- ___Block_byref_object_dispose_.36585
- ___Block_byref_object_dispose_.38369
- ___Block_byref_object_dispose_.3957
- ___Block_byref_object_dispose_.4199
- ___Block_byref_object_dispose_.44521
- ___Block_byref_object_dispose_.47931
- ___Block_byref_object_dispose_.48809
- ___Block_byref_object_dispose_.51023
- ___Block_byref_object_dispose_.52040
- ___Block_byref_object_dispose_.53072
- ___Block_byref_object_dispose_.54714
- ___Block_byref_object_dispose_.55868
- ___Block_byref_object_dispose_.56892
- ___Block_byref_object_dispose_.59545
- ___Block_byref_object_dispose_.62466
- ___Block_byref_object_dispose_.64203
- ___Block_byref_object_dispose_.64640
- ___GameCenterFoundationLibraryCore_block_invoke.42275
- ___GameCenterFoundationLibraryCore_block_invoke.49642
- ___GameCenterUICoreLibraryCore_block_invoke.42258
- ___GameCenterUILibraryCore_block_invoke.49611
- ___HealthKitLibraryCore_block_invoke.41794
- ___IDSLibraryCore_block_invoke.23086
- ___IDSLibraryCore_block_invoke.31034
- ___IDSLibraryCore_block_invoke.42790
- ___IDSLibraryCore_block_invoke.46399
- ___IDSLibraryCore_block_invoke.50627
- ___IDSLibraryCore_block_invoke.52253
- ___IMCoreLibraryCore_block_invoke.10735
- ___IMCoreLibraryCore_block_invoke.47480
- ___IMCoreLibraryCore_block_invoke.64592
- ___IntlPreferencesUILibraryCore_block_invoke.13932
- ___IntlPreferencesUILibraryCore_block_invoke.58519
- ___LoadAppleAccount_block_invoke.51408
- ___LoadAssistantServices_block_invoke.46305
- ___LoadCarPlayServices_block_invoke.50264
- ___LoadCarPlayServices_block_invoke.51657
- ___LoadCoreRecents_block_invoke.50643
- ___LoadCoreSuggestions_block_invoke.50620
- ___LoadMapKit_block_invoke.22238
- ___LoadMapKit_block_invoke.24517
- ___LoadMedicalIDUI_block_invoke.41774
- ___LoadPhotosUI_block_invoke.44847
- ___LoadPhotos_block_invoke.38376
- ___LoadPhotos_block_invoke.44808
- ___LoadPhotos_block_invoke.47919
- ___MobileCoreServicesLibraryCore_block_invoke.47320
- ___MobileCoreServicesLibraryCore_block_invoke.57979
- ___PosterBoardServicesLibraryCore_block_invoke.65513
- ___PosterBoardUIServicesLibraryCore_block_invoke.65564
- ___PosterKitLibraryCore_block_invoke.65703
- ___SharingLibraryCore_block_invoke.64631
- ___SiriActivationLibraryCore_block_invoke.54967
- ___SocialLibraryCore_block_invoke.22626
- ___SocialLibraryCore_block_invoke.59622
- ___SocialLibraryCore_block_invoke.64734
- ___ToneKitLibraryCore_block_invoke.57742
- ___block_descriptor_32_e42_"UICellAccessory"16?0"UICellAccessory"8l
- ___block_descriptor_56_e8_32s40s48s_e70_v24?0"CNContactListCollectionViewCell"8"UICellConfigurationState"16ls32l8s40l8s48l8
- ___block_literal_global.10.64232
- ___block_literal_global.1000
- ___block_literal_global.1002
- ___block_literal_global.10098
- ___block_literal_global.10318
- ___block_literal_global.10763
- ___block_literal_global.1080
- ___block_literal_global.10893
- ___block_literal_global.11.63878
- ___block_literal_global.11361
- ___block_literal_global.11466
- ___block_literal_global.11557
- ___block_literal_global.11717
- ___block_literal_global.11932
- ___block_literal_global.12382
- ___block_literal_global.127.52731
- ___block_literal_global.131.13927
- ___block_literal_global.13171
- ___block_literal_global.135.43397
- ___block_literal_global.13533
- ___block_literal_global.139.15740
- ___block_literal_global.139.31180
- ___block_literal_global.13952
- ___block_literal_global.14.31226
- ___block_literal_global.14.31446
- ___block_literal_global.14.45192
- ___block_literal_global.14.57645
- ___block_literal_global.141.15738
- ___block_literal_global.14809
- ___block_literal_global.15796
- ___block_literal_global.16543
- ___block_literal_global.16724
- ___block_literal_global.16892
- ___block_literal_global.17896
- ___block_literal_global.18.5492
- ___block_literal_global.18508
- ___block_literal_global.19.31221
- ___block_literal_global.19.40320
- ___block_literal_global.19.42233
- ___block_literal_global.19101
- ___block_literal_global.19205
- ___block_literal_global.19364
- ___block_literal_global.19719
- ___block_literal_global.2.49525
- ___block_literal_global.2.63019
- ___block_literal_global.20.35144
- ___block_literal_global.20455
- ___block_literal_global.20674
- ___block_literal_global.20959
- ___block_literal_global.21.17924
- ___block_literal_global.21.32126
- ___block_literal_global.21225
- ___block_literal_global.21478
- ___block_literal_global.21761
- ___block_literal_global.21862
- ___block_literal_global.22202
- ___block_literal_global.22234
- ___block_literal_global.22691
- ___block_literal_global.23.45178
- ___block_literal_global.23.63178
- ___block_literal_global.23098
- ___block_literal_global.23563
- ___block_literal_global.23999
- ___block_literal_global.24106
- ___block_literal_global.24566
- ___block_literal_global.24893
- ___block_literal_global.25.40328
- ___block_literal_global.25.40869
- ___block_literal_global.25.63179
- ___block_literal_global.25.64222
- ___block_literal_global.25748
- ___block_literal_global.26.57641
- ___block_literal_global.26261
- ___block_literal_global.26342
- ___block_literal_global.26525
- ___block_literal_global.27386
- ___block_literal_global.28.40331
- ___block_literal_global.28.49297
- ___block_literal_global.28333
- ___block_literal_global.28410
- ___block_literal_global.28557
- ___block_literal_global.2857
- ___block_literal_global.29.28555
- ___block_literal_global.29.31213
- ___block_literal_global.29.45169
- ___block_literal_global.29.48410
- ___block_literal_global.29.63698
- ___block_literal_global.29094
- ___block_literal_global.29155
- ___block_literal_global.29376
- ___block_literal_global.299
- ___block_literal_global.29939
- ___block_literal_global.3.16719
- ___block_literal_global.3.28415
- ___block_literal_global.3.37328
- ___block_literal_global.3.57680
- ___block_literal_global.3.58700
- ___block_literal_global.3.58933
- ___block_literal_global.306
- ___block_literal_global.30809
- ___block_literal_global.309
- ___block_literal_global.31.28538
- ___block_literal_global.31.40334
- ___block_literal_global.31046
- ___block_literal_global.312
- ___block_literal_global.31236
- ___block_literal_global.31407
- ___block_literal_global.31450
- ___block_literal_global.315
- ___block_literal_global.31703
- ___block_literal_global.31746
- ___block_literal_global.318
- ___block_literal_global.32034
- ___block_literal_global.321
- ___block_literal_global.32158
- ___block_literal_global.32216
- ___block_literal_global.32491
- ___block_literal_global.32945
- ___block_literal_global.32974
- ___block_literal_global.33211
- ___block_literal_global.33792
- ___block_literal_global.3380
- ___block_literal_global.34.31208
- ___block_literal_global.34.40339
- ___block_literal_global.34292
- ___block_literal_global.34438
- ___block_literal_global.34887
- ___block_literal_global.35112
- ___block_literal_global.35232
- ___block_literal_global.3557
- ___block_literal_global.35592
- ___block_literal_global.358
- ___block_literal_global.36.33206
- ___block_literal_global.36137
- ___block_literal_global.3616
- ___block_literal_global.36577
- ___block_literal_global.3682
- ___block_literal_global.37.40342
- ___block_literal_global.37089
- ___block_literal_global.37146
- ___block_literal_global.37333
- ___block_literal_global.37501
- ___block_literal_global.377
- ___block_literal_global.37716
- ___block_literal_global.37914
- ___block_literal_global.38.17912
- ___block_literal_global.38.38894
- ___block_literal_global.38.64210
- ___block_literal_global.38033
- ___block_literal_global.38173
- ___block_literal_global.38379
- ___block_literal_global.38810
- ___block_literal_global.38897
- ___block_literal_global.39.31206
- ___block_literal_global.395
- ___block_literal_global.3975
- ___block_literal_global.4.31699
- ___block_literal_global.4.37502
- ___block_literal_global.4.46786
- ___block_literal_global.4.5096
- ___block_literal_global.40.40347
- ___block_literal_global.40044
- ___block_literal_global.40300
- ___block_literal_global.40373
- ___block_literal_global.40738
- ___block_literal_global.40892
- ___block_literal_global.41.19339
- ___block_literal_global.41.23658
- ___block_literal_global.41.29921
- ___block_literal_global.415
- ___block_literal_global.41643
- ___block_literal_global.417
- ___block_literal_global.41819
- ___block_literal_global.41941
- ___block_literal_global.41974
- ___block_literal_global.42.66823
- ___block_literal_global.42243
- ___block_literal_global.4239
- ___block_literal_global.42548
- ___block_literal_global.429
- ___block_literal_global.43.19341
- ___block_literal_global.43.40352
- ___block_literal_global.43315
- ___block_literal_global.4363
- ___block_literal_global.43682
- ___block_literal_global.43780
- ___block_literal_global.43877
- ___block_literal_global.44297
- ___block_literal_global.44507
- ___block_literal_global.44686
- ___block_literal_global.447
- ___block_literal_global.44858
- ___block_literal_global.45199
- ___block_literal_global.452
- ___block_literal_global.46.40357
- ___block_literal_global.46125
- ___block_literal_global.46311
- ___block_literal_global.46788
- ___block_literal_global.47.60505
- ___block_literal_global.47083
- ___block_literal_global.473
- ___block_literal_global.47336
- ___block_literal_global.47412
- ___block_literal_global.476
- ___block_literal_global.47945
- ___block_literal_global.48218
- ___block_literal_global.48443
- ___block_literal_global.48974
- ___block_literal_global.49.56590
- ___block_literal_global.490
- ___block_literal_global.49299
- ___block_literal_global.49356
- ___block_literal_global.49443
- ___block_literal_global.49524
- ___block_literal_global.498
- ___block_literal_global.49896
- ___block_literal_global.5.46115
- ___block_literal_global.50257
- ___block_literal_global.50637
- ___block_literal_global.5095
- ___block_literal_global.51.31198
- ___block_literal_global.51071
- ___block_literal_global.51221
- ___block_literal_global.51399
- ___block_literal_global.51502
- ___block_literal_global.51517
- ___block_literal_global.51650
- ___block_literal_global.51945
- ___block_literal_global.52128
- ___block_literal_global.52840
- ___block_literal_global.53080
- ___block_literal_global.53185
- ___block_literal_global.533
- ___block_literal_global.53498
- ___block_literal_global.53770
- ___block_literal_global.53850
- ___block_literal_global.54.61084
- ___block_literal_global.54209
- ___block_literal_global.547
- ___block_literal_global.54712
- ___block_literal_global.5497
- ___block_literal_global.55192
- ___block_literal_global.55559
- ___block_literal_global.56.66813
- ___block_literal_global.56120
- ___block_literal_global.56634
- ___block_literal_global.568
- ___block_literal_global.57.51404
- ___block_literal_global.575
- ___block_literal_global.57690
- ___block_literal_global.583
- ___block_literal_global.58434
- ___block_literal_global.58693
- ___block_literal_global.58928
- ___block_literal_global.59650
- ___block_literal_global.6.10384
- ___block_literal_global.60.61072
- ___block_literal_global.604
- ___block_literal_global.60510
- ___block_literal_global.6095
- ___block_literal_global.61138
- ___block_literal_global.614
- ___block_literal_global.62.40721
- ___block_literal_global.620
- ___block_literal_global.62416
- ___block_literal_global.63.31195
- ___block_literal_global.63.46298
- ___block_literal_global.630
- ___block_literal_global.63026
- ___block_literal_global.63192
- ___block_literal_global.63727
- ___block_literal_global.63884
- ___block_literal_global.64246
- ___block_literal_global.646
- ___block_literal_global.6482
- ___block_literal_global.64837
- ___block_literal_global.65160
- ___block_literal_global.652
- ___block_literal_global.65767
- ___block_literal_global.65967
- ___block_literal_global.66212
- ___block_literal_global.66429
- ___block_literal_global.66606
- ___block_literal_global.668
- ___block_literal_global.673
- ___block_literal_global.6757
- ___block_literal_global.680
- ___block_literal_global.693
- ___block_literal_global.699
- ___block_literal_global.7199
- ___block_literal_global.745
- ___block_literal_global.7495
- ___block_literal_global.75.27374
- ___block_literal_global.750
- ___block_literal_global.7781
- ___block_literal_global.78.44502
- ___block_literal_global.8.16717
- ___block_literal_global.8.46784
- ___block_literal_global.8.5090
- ___block_literal_global.8450
- ___block_literal_global.87.24913
- ___block_literal_global.889
- ___block_literal_global.89
- ___block_literal_global.9.31231
- ___block_literal_global.9.31695
- ___block_literal_global.9.41966
- ___block_literal_global.9.46106
- ___block_literal_global.916
- ___block_literal_global.919
- ___block_literal_global.922
- ___block_literal_global.9268
- ___block_literal_global.9441
- ___block_literal_global.976
- ___block_literal_global.9775
- ___block_literal_global.99
- ___getAVTAvatarFetchRequestClass_block_invoke.37872
- ___getAVTAvatarRecordImageProviderClass_block_invoke.19910
- ___getAVTAvatarRecordImageProviderClass_block_invoke.32913
- ___getAVTAvatarRecordImageProviderClass_block_invoke.53438
- ___getAVTAvatarRecordRenderingClass_block_invoke.30485
- ___getAVTAvatarRecordRenderingClass_block_invoke.55516
- ___getAVTAvatarStoreClass_block_invoke.16210
- ___getAVTAvatarStoreClass_block_invoke.37865
- ___getAVTAvatarStoreClass_block_invoke.41997
- ___getAVTRenderingScopeClass_block_invoke.19912
- ___getAVTRenderingScopeClass_block_invoke.32915
- ___getAVTRenderingScopeClass_block_invoke.53440
- ___getAVTStickerGeneratorOptionsClass_block_invoke.51025
- ___getAVTViewClass_block_invoke.55538
- ___getGKDaemonProxyClass_block_invoke.42254
- ___getGKLocalPlayerClass_block_invoke.42256
- ___getIDSIDQueryControllerClass_block_invoke.23063
- ___getIDSIDQueryControllerClass_block_invoke.50625
- ___getIDSServiceNameFaceTimeSymbolLoc_block_invoke.31023
- ___getIDSServiceNameFaceTimeSymbolLoc_block_invoke.46381
- ___getIDSServiceNameiMessageSymbolLoc_block_invoke.42779
- ___getIDSServiceNameiMessageSymbolLoc_block_invoke.46391
- ___getIDSServiceNameiMessageSymbolLoc_block_invoke.52244
- ___getIMNicknameControllerClass_block_invoke.10733
- ___getIMNicknameControllerClass_block_invoke.47478
- ___getIMNicknameControllerClass_block_invoke.64590
- ___getIPPronounPickerViewControllerClass_block_invoke.13930
- ___getIPPronounPickerViewControllerClass_block_invoke.58517
- ___getPRSPosterConfigurationAttributesClass_block_invoke.65533
- ___getPRSPosterRoleIncomingCallSymbolLoc_block_invoke.65504
- ___getSFCreatePairedContactManagerSymbolLoc_block_invoke.64627
- ___getSLComposeViewControllerClass_block_invoke.22624
- ___getSLComposeViewControllerClass_block_invoke.59617
- ___getSLComposeViewControllerClass_block_invoke.64727
- ___getSiriDirectActionContextClass_block_invoke.54957
- ___getSiriDirectActionSourceClass_block_invoke.54959
- ___getkAssistantDirectActionEventKeySymbolLoc_block_invoke.54949
- ___getkUTTypeJPEGSymbolLoc_block_invoke.57974
- ___getkUTTypePNGSymbolLoc_block_invoke.57967
- ___swift_memcpy264_8
- ___unnamed_12
- ___unnamed_9
- __extensionAuxiliaryHostProtocol.__interface.24907
- __extensionAuxiliaryHostProtocol.onceToken.24906
- __extensionAuxiliaryVendorProtocol.__interface.24914
- __extensionAuxiliaryVendorProtocol.onceToken.24912
- _audit_stringAssistantServices.49076
- _audit_stringAssistantServices.54983
- _audit_stringAvatarKit.30501
- _audit_stringAvatarKit.32940
- _audit_stringAvatarKit.51045
- _audit_stringAvatarKit.55547
- _audit_stringAvatarUI.13189
- _audit_stringAvatarUI.16203
- _audit_stringAvatarUI.19931
- _audit_stringAvatarUI.30508
- _audit_stringAvatarUI.32926
- _audit_stringAvatarUI.33745
- _audit_stringAvatarUI.34431
- _audit_stringAvatarUI.36614
- _audit_stringAvatarUI.37889
- _audit_stringAvatarUI.41990
- _audit_stringAvatarUI.53456
- _audit_stringAvatarUI.55533
- _audit_stringAvatarUI.6092
- _audit_stringGameCenterFoundation.42280
- _audit_stringGameCenterFoundation.49645
- _audit_stringGameCenterUI.49625
- _audit_stringGameCenterUICore.42273
- _audit_stringHealthKit.41807
- _audit_stringIDS.23089
- _audit_stringIDS.31038
- _audit_stringIDS.42794
- _audit_stringIDS.46402
- _audit_stringIDS.50631
- _audit_stringIDS.52257
- _audit_stringIMCore.10740
- _audit_stringIMCore.47496
- _audit_stringIMCore.64597
- _audit_stringIntlPreferencesUI.13937
- _audit_stringIntlPreferencesUI.58535
- _audit_stringMobileCoreServices.47324
- _audit_stringMobileCoreServices.57982
- _audit_stringPosterBoardServices.65516
- _audit_stringPosterBoardUIServices.65566
- _audit_stringPosterKit.65705
- _audit_stringSharing.64633
- _audit_stringSiriActivation.54970
- _audit_stringSocial.22630
- _audit_stringSocial.59626
- _audit_stringSocial.64738
- _audit_stringToneKit.57756
- _block_copy_helper.116
- _block_copy_helper.13
- _block_copy_helper.130
- _block_copy_helper.137
- _block_copy_helper.141
- _block_copy_helper.148
- _block_copy_helper.16
- _block_descriptor.118
- _block_descriptor.132
- _block_descriptor.139
- _block_descriptor.143
- _block_descriptor.15
- _block_descriptor.150
- _block_descriptor.18
- _block_destroy_helper.117
- _block_destroy_helper.131
- _block_destroy_helper.138
- _block_destroy_helper.14
- _block_destroy_helper.142
- _block_destroy_helper.149
- _block_destroy_helper.17
- _bundleCanManageDuplicates.cn_once_object_22
- _bundleCanManageDuplicates.cn_once_token_22
- _classAFPreferences.46300
- _classCRRecentContactsLibrary.50638
- _classFBSOpenApplicationService.50259
- _classFBSOpenApplicationService.51652
- _classMIUIDisplayConfiguration.41781
- _classMIUIMedicalIDViewController.41770
- _classPHPhotoLibrary.47935
- _classPHPickerViewController.44843
- _defaultServices._services.49357
- _defaultServices.onceToken.49355
- _descriptorForRequiredKeys.cn_once_object_1.18509
- _descriptorForRequiredKeys.cn_once_object_1.32946
- _descriptorForRequiredKeys.cn_once_object_1.35593
- _descriptorForRequiredKeys.cn_once_object_1.42549
- _descriptorForRequiredKeys.cn_once_object_1.43683
- _descriptorForRequiredKeys.cn_once_object_1.47084
- _descriptorForRequiredKeys.cn_once_object_1.48219
- _descriptorForRequiredKeys.cn_once_object_1.48975
- _descriptorForRequiredKeys.cn_once_object_1.49897
- _descriptorForRequiredKeys.cn_once_object_1.53499
- _descriptorForRequiredKeys.cn_once_object_2.16540
- _descriptorForRequiredKeys.cn_once_object_2.31700
- _descriptorForRequiredKeys.cn_once_object_2.32030
- _descriptorForRequiredKeys.cn_once_object_2.45193
- _descriptorForRequiredKeys.cn_once_object_2.5493
- _descriptorForRequiredKeys.cn_once_object_2.6483
- _descriptorForRequiredKeys.cn_once_token_1.18507
- _descriptorForRequiredKeys.cn_once_token_1.32944
- _descriptorForRequiredKeys.cn_once_token_1.35591
- _descriptorForRequiredKeys.cn_once_token_1.42547
- _descriptorForRequiredKeys.cn_once_token_1.43681
- _descriptorForRequiredKeys.cn_once_token_1.47082
- _descriptorForRequiredKeys.cn_once_token_1.48217
- _descriptorForRequiredKeys.cn_once_token_1.48973
- _descriptorForRequiredKeys.cn_once_token_1.49895
- _descriptorForRequiredKeys.cn_once_token_1.53497
- _descriptorForRequiredKeys.cn_once_token_2.16539
- _descriptorForRequiredKeys.cn_once_token_2.31698
- _descriptorForRequiredKeys.cn_once_token_2.32029
- _descriptorForRequiredKeys.cn_once_token_2.45191
- _descriptorForRequiredKeys.cn_once_token_2.5491
- _descriptorForRequiredKeys.cn_once_token_2.6481
- _descriptorForRequiredKeysForPreferredForNameMeContact.cn_once_object_9
- _descriptorForRequiredKeysForPreferredForNameMeContact.cn_once_token_9
- _descriptorForRequiredKeysWithDescription:.cn_once_object_13.59707
- _descriptorForRequiredKeysWithDescription:.cn_once_object_13.64873
- _descriptorForRequiredKeysWithDescription:.cn_once_token_13.59706
- _descriptorForRequiredKeysWithDescription:.cn_once_token_13.64872
- _emptyContact.cn_once_object_13
- _emptyContact.cn_once_token_13
- _enablesTransportButtons.s_enableTransportButtons.64870
- _enablesTransportButtons.s_onceToken.64869
- _fullFormatter.44300
- _getAFPreferencesClass.46294
- _getAVTAvatarFetchRequestClass.37866
- _getAVTAvatarFetchRequestClass.softClass.37871
- _getAVTAvatarRecordImageProviderClass.softClass.19909
- _getAVTAvatarRecordImageProviderClass.softClass.32912
- _getAVTAvatarRecordImageProviderClass.softClass.53437
- _getAVTAvatarRecordRenderingClass.softClass.30484
- _getAVTAvatarRecordRenderingClass.softClass.55515
- _getAVTAvatarStoreClass.softClass.16209
- _getAVTAvatarStoreClass.softClass.37864
- _getAVTAvatarStoreClass.softClass.41996
- _getAVTRenderingScopeClass.softClass.19911
- _getAVTRenderingScopeClass.softClass.32914
- _getAVTRenderingScopeClass.softClass.53439
- _getAVTStickerGeneratorOptionsClass.softClass.51024
- _getAVTViewClass.softClass.55537
- _getCRRecentContactsLibraryClass.50633
- _getFBSOpenApplicationServiceClass.50253
- _getFBSOpenApplicationServiceClass.51646
- _getGKDaemonProxyClass.softClass.42253
- _getGKLocalPlayerClass.softClass.42255
- _getIDSIDQueryControllerClass.23058
- _getIDSIDQueryControllerClass.softClass.23062
- _getIDSIDQueryControllerClass.softClass.50624
- _getIDSServiceNameFaceTimeSymbolLoc.ptr.31022
- _getIDSServiceNameFaceTimeSymbolLoc.ptr.46380
- _getIDSServiceNameiMessageSymbolLoc.ptr.42778
- _getIDSServiceNameiMessageSymbolLoc.ptr.46390
- _getIDSServiceNameiMessageSymbolLoc.ptr.52243
- _getIMNicknameControllerClass.softClass.10732
- _getIMNicknameControllerClass.softClass.47477
- _getIMNicknameControllerClass.softClass.64589
- _getIPPronounPickerViewControllerClass.softClass.13929
- _getIPPronounPickerViewControllerClass.softClass.58516
- _getMIUIDisplayConfigurationClass.41763
- _getMIUIMedicalIDViewControllerClass.41764
- _getPHPhotoLibraryClass.47929
- _getPHPickerViewControllerClass.44838
- _getPRSPosterConfigurationAttributesClass.softClass.65532
- _getPRSPosterRoleIncomingCallSymbolLoc.ptr.65503
- _getSFCreatePairedContactManagerSymbolLoc.ptr.64626
- _getSLComposeViewControllerClass.softClass.22623
- _getSLComposeViewControllerClass.softClass.59616
- _getSLComposeViewControllerClass.softClass.64726
- _getSiriDirectActionContextClass.softClass.54956
- _getSiriDirectActionSourceClass.softClass.54958
- _get_witness_table 10ContactsUI36CNWallpaperSuggestionsGallerySectionVy05SwiftB015ModifiedContentVyAFyAD6ZStackVyAD9TupleViewVyAFyAFyAFyAD6VStackVyAD012_ConditionalI0VyAJyAD0L0PADE8onSubmit2of_QrAD0P8TriggersV_yyctFQOyAFyAFyAFyAD9TextFieldVyAD0S0VGAD30_EnvironmentKeyWritingModifierVyAD5ColorVSgGGAD14_PaddingLayoutVGA6_G_Qo__ApDEAqR_QrAT_yyctFQOyA7__Qo_tGAJyA10__A9_tGGGA6_GA6_GA6_G_ApDE05sceneZ0yQrAD4EdgeO3SetVFQOyAD7DividerV_Qo_tGGAD011_BackgroundX0VyAD06_ShapeL0VyAD16RoundedRectangleVA1_GGGA3_GGAdOHPyHC.12
- _get_witness_table 7SwiftUI14GeometryReaderVyAA6ButtonVyAA15ModifiedContentVyAA13_VariadicViewO4TreeVy_AA11_LayoutRootVyAA03AnyK0VGAA05TupleI0VyAGyAGyAA6ZStackVyARyAA012_ConditionalG0VyAGyAGyAA16RoundedRectangleVAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGGAA08_OverlayV0VyAGyA0_AA11_ClipEffectVyAXGGSgGGAGyAGyAA6CircleVA2_GA5_yAGyA0_A7_yA14_GGSgGGG_AVyAA4TextVAGyAGyAA5ImageVAZyAA4FontVSgGGA2_GGtGGA5_yAGyAA08ProgressI0VyAA05EmptyI0VA38_GA2_GSgGGAA010_FlexFrameK0VG_A23_tGGA45_GGGAA0I0HPyHC.208
- _get_witness_table 7SwiftUI15ModifiedContentVy08ContactsB036CNWallpaperSuggestionsGallerySectionVyAA13_VariadicViewO4TreeVy_AA11_LayoutRootVyAD0fg12SourceButtonkM0VGAA05TupleK0VyAA7ForEachVySayAD0fghO0VG10Foundation4UUIDVAD0fgH0V0oP033_81619BC199BAC997F7A0ACA40B51B6D6LLVG_ACyASySayAD0fghK5ModelC15SuggestedAvatarVGSSACyA_016AvatarSuggestionP0A1_LLVAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGGA15_GSgtGGGAA13_TaskModifierVGAA0K0HPA22_AAA26_HPyHC_A24_AA0K8ModifierHPyHCHC.169
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewP14ContactsUICoreE24asClearBackgroundSectionQryFQOyAF06HeaderE0V_Qo_AA30_EnvironmentKeyWritingModifierVyAF23ContactCardDetailsStyleVGGAaDHPqd__AaDHD2_AJHO_AoA0eP0HPyHCHC.3
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6VStackVyAA9TupleViewVyAA6SpacerV_AA0G0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyAkAE15fullScreenCover11isPresented0I7Dismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaJRd__lFQOyAEyAA06ScrollG0VyAA6HStackVyACyACyACyACy08ContactsB0021CNPosterSnapshotImageG0VAA12_FrameLayoutVGAA18_AnimationModifierVySo7UIImageCSgGGAA14_PaddingLayoutVGA13_GGGG_AkAE9statusBar6hiddenQrSb_tFQOyACyA_025CNExistingWallpaperEditorG0VAA23_SafeAreaIgnoringLayoutVG_Qo_Qo_AA25_AppearanceActionModifierVG_So24CNPRSPosterConfigurationCSgQo_AikAE12scenePaddingyQrAA4EdgeO3SetVFQOyAEyAGyACyAkAE11buttonStyleyQrqd__AA20PrimitiveButtonStyleRd__lFQOyAA6ButtonVyACyACyAA4TextVA3_GAA16_FlexFrameLayoutVGG_AA28BorderedProminentButtonStyleVQo_AA32_EnvironmentKeyTransformModifierVySbGG_ACyA43_yA45_GAA14_OpacityEffectVGtGG_Qo_tGGA13_GAaJHPA66_AaJHPyHC_A13_AA0G8ModifierHPyHCHC.76
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACyACy08ContactsB0013ContactAvatarG033_87FAEC429F5A2E07500F09EBFC13C74CLLVAA12_FrameLayoutVGAA11_BlurEffectVGAA07_OffsetU0VGSg_ACyAnA08_PaddingS0VGtGGAMGAA0G0HPAzAA0_HPyHC_AmA0G8ModifierHPyHCHC.51
- _get_witness_table 7SwiftUI15ModifiedContentVyAA9LazyVGridVyAA7ForEachVys10ArraySliceVySo9CNContactCGAK08ContactsB016HelperAvatarView33_87FAEC429F5A2E07500F09EBFC13C74CLLVGSgGAA14_PaddingLayoutVGAA0O0HPAsaWHPyHC_AuA0O8ModifierHPyHCHC.44
- _get_witness_table 7SwiftUI15ModifiedContentVyAA9LazyVGridVyAA9TupleViewVyAA7ForEachVys10ArraySliceVySo9CNContactCGAM08ContactsB0012HelperAvatarH033_87FAEC429F5A2E07500F09EBFC13C74CLLVG_ACyACyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAWyAA0X9AlignmentOGGAWySbGGAWy12CoreGraphics7CGFloatVGGSgtGSgGAA14_PaddingLayoutVGAA0H0HPA13_AAA17_HPyHC_A15_AA0H8ModifierHPyHCHC.45
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE010navigationE5StyleyQrqd__AA010NavigationeG0Rd__lFQOyAA0hE0VyAeAE7toolbar7contentQrqd__yXE_tAA07ToolbarD0Rd__lFQOyAeAE0F8BarTitle_11displayModeQrqd___AA0hL4ItemV0m7DisplayO0OtSyRd__lFQOyAeAE06scrollD10BackgroundyQrAA10VisibilityOFQOy08ContactsB021DuplicatesUIContainerVyAA05TupleE0VyACyACyAeAE04listG0yQrqd__AA04ListG0Rd__lFQOyAA0Z0Vys5NeverOAA012_ConditionalD0VyAA7ForEachVySay0U014CNDuplicateSetCGSOAV09DuplicateZ4CellVGAZyAA7SectionVyAA05EmptyE0VA15_A19_GSg_A17_yA19_AV30DuplicatePreviouslyIgnoredCellVA19_GSgtGGG_AA012InsetGroupedzG0VQo_AA14_PaddingLayoutVGAV0v7UIInsetE0VG_AA6SpacerVAV22ActionButtonsContainerVyAZyAeAE18confirmationDialog_11isPresented05titleT07actionsQrqd___AA7BindingVySbGAUqd_0_yXEtSyRd__AaDRd_0_r0_lFQOyACyAeAE06buttonG0yQrqd__AA015PrimitiveButtonG0Rd__lFQOyAA6ButtonVyACyAA4TextVAA16_FlexFrameLayoutVGG_AA023BorderedProminentButtonG0VQo_AA32_EnvironmentKeyTransformModifierVySbGG_SSA52_yA54_GQo__ACyACyA66_AV0v12IgnoreButtonE8ModifierVGA64_GtGGSgtGG_Qo__SSQo__AA0kD7BuilderV10buildBlockyQrxAaLRzlFZQOy_AA0kP0VyytA66_GQo_Qo_G_AA05StackheG0VQo_AA01_sG8ModifierVyAA5ColorVGGAA25_AppearanceActionModifierVGA98_GAaDHPA99_AaDHPA96_AaDHPqd0__AaDHD3_A90_HO_A95_AA0E8ModifierHPyHCHC_A98_AAA101_HPyHCHC_A98_AAA101_HPyHCHC.69
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6ButtonVyACy08ContactsB0022CNAvatarViewControllerH0VAA21_TraitWritingModifierVyAA010TransitionJ3KeyVGGSgGAA05_TaskL0VGAA14_PaddingLayoutVGAA17_FlipForRTLEffectVGAA0H0HPAvaZHPAsaZHPApaZHPyHC_ArA0hL0HPyHCHC_AuAA_HPyHCHC_AxAA_HPyHCHC.209
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6VStackVyAA9TupleViewVyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVyAA0H9AlignmentOGGAKyAA4FontVSgGGSg_AA6SpacerVAA6HStackVyAGyAEyAGyAI_ACyACyAiKy12CoreGraphics7CGFloatVGGAKySiSgGGtGG_AWtGGtGGAKyAA5ColorVSgGGAA14_PaddingLayoutVGA18_GSgAA0G0HpA20_AAA22_HPA19_AAA22_HPA16_AAA22_HPA11_AAA22_HPyHC_A15_AA0gL0HPyHCHC_A18_AAA23_HPyHCHC_A18_AAA23_HPyHCHC_HC.164
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAA7ForEachVySnySiGSi08ContactsB020ContactDetailRowViewVGAA25_AppearanceActionModifierVGALGAA0L0HPAoaQHPAlaQHPAkaQHPyHC_HC_AnA0lO0HPyHCHC_AlaQHPAkaQHPyHC_HCHC.53
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEy08ContactsB014AnswerTemplateVAA25_AppearanceActionModifierVGAA010_TaskValueK0VySo9CNContactCGGAEyAEyAF015ContactCardViewaB0VAJGAPGGAA0Q0HPAqaWHPAkaWHPAhaWHPyHC_AjA0qK0HPyHCHC_ApaXHPyHCHC_AuaWHPAtaWHPAsaWHPyHC_AjaXHPyHCHC_ApaXHPyHCHCHC.83
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA15NavigationStackVyAA0E4PathVAA08ModifiedD0VyAIyAIyAA4ViewPAAE22onScrollGeometryChange3for2of6actionQrqd__m_qd__AA0kL0Vcyqd___qd__tctSQRd__lFQOyAIyAkAE14scrollPosition2id6anchorQrAA7BindingVyqd__SgG_AA9UnitPointVSgtSHRd__lFQOyAK012_AppIntents_aB0E19appEntityIdentifieryQr0xY016EntityIdentifierVSgFQOyAA0kI0VyAkAE0Q12TargetLayout9isEnabledQrSb_tFQOyAA10LazyVStackVyAA05TupleI0Vy08ContactsB0021ContactCardHeaderNameI0V_A14_016CardQuickActionsI0VA14_018ContactCardDetailsI0VtGG_Qo_G_Qo__SiQo_AA23SafeAreaPaddingModifierVG_12CoreGraphics7CGFloatVQo_AA30_EnvironmentKeyWritingModifierVyAA11ColorSchemeOGGAA14_PaddingLayoutVGAA20_BackdropGroupEffectVGGA45_GAaJHPA46_AaJHPyHC_A45_AaJHPA42_AaJHPA39_AaJHPqd0__AaJHD3_A33_HO_A38_AA0I8ModifierHPyHCHC_A41_AAA48_HPyHCHC_A44_AAA48_HPyHCHCHC.165
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedD0Vy08ContactsB0021CNPosterSnapshotImageE0VAA25_AppearanceActionModifierVG_So16CNMutableContactCQo__12CoreGraphics7CGFloatVQo_AA6ZStackVyAA05TupleE0VyAJyAK08CNAvatare10ControllerE0VAK0L13VibrantShadowVG_A1_tGGGAaDHPqd0__AaDHD3_AWHO_A6_AaDHPyHCHC.170
- _get_witness_table 7SwiftUI19_ConditionalContentVyACyAA6VStackVyAA9TupleViewVyAA08ModifiedD0Vy08ContactsB029CNContactGroupArrangedAvatars33_87FAEC429F5A2E07500F09EBFC13C74CLLVAA14_PaddingLayoutVG_AIyAA0K0VyAIyAA4TextVAOGGAA010_FlexFrameV0VGtGGAEyAIyAIyAJ0j16FullAccessPromptK10VisualizerALLLVAOGAXGGGAIyAIyAEyAGyAIyApA01_yV0VG_AIyAIyAIyAIyAA0G0PAAE9lineLimit_13reservesSpaceQrSi_SbtFQOyAIyARyATGAA30_EnvironmentKeyWritingModifierVyAA0W9AlignmentOGG_Qo_A15_yAA4FontVSgGGA15_ySbGGA15_y12CoreGraphics7CGFloatVGGAOGtGGAOGAA24_BackgroundStyleModifierVyAA8MaterialVGGGAAA9_HPA5_AAA9_HPA_AAA9_HPyHC_A4_AAA9_HPyHCHC_A42_AAA9_HPA36_AAA9_HPA35_AAA9_HPyHC_AoA0G8ModifierHPyHCHC_A41_AAA44_HPyHCHCHC.25
- _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyAA6VStackVyAA05TupleC0VyAaBPAAE12scenePaddingyQrAA4EdgeO3SetVFQOyADy08ContactsB036CNWallpaperSuggestionsGallerySectionV05TitleC0027_C3DE73CB51D4E9D5CF00243C32R4FD8ALLVyx_GAA01_I6LayoutVG_Qo__xtGGAA16_FlexFrameLayoutVGAaBHPA_AaBHPyHC_A1_AA0C8ModifierHPyHCHC.19
- _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyADyAaBPAAE10fontWeightyQrAA4FontV0G0VSgFQOyADyADyAA4TextVAA30_EnvironmentKeyWritingModifierVyAM4CaseOSgGGAOyAHSgGG_Qo_AOyAA5ColorVSgGGAA16_FixedSizeLayoutVGAaBHPA1_AaBHPqd__AaBHD2_AXHO_A0_AA0cM0HPyHCHC_A3_AAA5_HPyHCHC.29
- _get_witness_table 7SwiftUI9EmptyViewVAA0D0HPyHC.54
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAcAE12scenePaddingyQrAA4EdgeO3SetVFQOyAA14GeometryReaderVyAA012SubscriptionC0Vy7Combine10PublishersO5MergeVy_AR3MapVy_So20NSNotificationCenterC10FoundationE9PublisherVSbGA0_GAcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAcAE23scrollDismissesKeyboardyQrAA06ScrollZ12KeyboardModeVFQOyAA06ScrollC0VyA3_yAA09_VariadicC0O4TreeVy_AA11_LayoutRootVy08ContactsB035CNWallpaperSuggestionsGalleryLayoutVGAA05TupleC0VyA3_yA15_29CNWallpaperSuggestionsGalleryV011PlaceholderC033_81619BC199BAC997F7A0ACA40B51B6D6LLVAA30_EnvironmentKeyWritingModifierVySo13UIWindowSceneCSgGG_A15_042CNWallpaperSuggestionsGalleryNameTextFieldC0VSgA22_013SourceButtonsC0A24_LLVtGGAA16_FlexFrameLayoutVGG_Qo_AA25_AppearanceActionModifierVG_12CoreGraphics7CGFloatVQo_GG_Qo__A15_35CNWallpaperSuggestionsGallerySourceVSgQo__SbQo__So24CNPRSPosterConfigurationCSgQo__A15_029CNWallpaperSuggestionsGalleryC5ModelC15SuggestedAvatarVSgQo__SSQo__SSQo__SbQo_HO.97
- _getkAssistantDirectActionEventKeySymbolLoc.ptr.54948
- _getkUTTypeJPEGSymbolLoc.ptr.57973
- _getkUTTypePNGSymbolLoc.ptr.57966
- _initAFPreferences.46296
- _initCRRecentContactsLibrary.50635
- _initFBSOpenApplicationService.50255
- _initFBSOpenApplicationService.51648
- _initMIUIDisplayConfiguration.41779
- _initMIUIMedicalIDViewController.41768
- _initPHPhotoLibrary.47934
- _initPHPickerViewController.44840
- _log.cn_once_object_0.54210
- _log.cn_once_object_1.15797
- _log.cn_once_object_1.16544
- _log.cn_once_object_1.19365
- _log.cn_once_object_1.19720
- _log.cn_once_object_1.21762
- _log.cn_once_object_1.22203
- _log.cn_once_object_1.24107
- _log.cn_once_object_1.25749
- _log.cn_once_object_1.31704
- _log.cn_once_object_1.32035
- _log.cn_once_object_1.32159
- _log.cn_once_object_1.34439
- _log.cn_once_object_1.35113
- _log.cn_once_object_1.37717
- _log.cn_once_object_1.37915
- _log.cn_once_object_1.40893
- _log.cn_once_object_1.45200
- _log.cn_once_object_1.46126
- _log.cn_once_object_1.48444
- _log.cn_once_object_1.49444
- _log.cn_once_object_1.51072
- _log.cn_once_object_1.51503
- _log.cn_once_object_1.52841
- _log.cn_once_object_1.55560
- _log.cn_once_object_1.58435
- _log.cn_once_object_1.61139
- _log.cn_once_object_1.9776
- _log.cn_once_object_2.38811
- _log.cn_once_object_2.41820
- _log.cn_once_object_2.51222
- _log.cn_once_object_20.44859
- _log.cn_once_object_20.47946
- _log.cn_once_object_6.13534
- _log.cn_once_object_6.23564
- _log.cn_once_object_6.36138
- _log.cn_once_object_6.51946
- _log.cn_once_object_6.66607
- _log.cn_once_object_9.23659
- _log.cn_once_token_0.54208
- _log.cn_once_token_1.15795
- _log.cn_once_token_1.16542
- _log.cn_once_token_1.19363
- _log.cn_once_token_1.19718
- _log.cn_once_token_1.21760
- _log.cn_once_token_1.22201
- _log.cn_once_token_1.24105
- _log.cn_once_token_1.25747
- _log.cn_once_token_1.31702
- _log.cn_once_token_1.32033
- _log.cn_once_token_1.32157
- _log.cn_once_token_1.34437
- _log.cn_once_token_1.35111
- _log.cn_once_token_1.37715
- _log.cn_once_token_1.37913
- _log.cn_once_token_1.40891
- _log.cn_once_token_1.45198
- _log.cn_once_token_1.46124
- _log.cn_once_token_1.48442
- _log.cn_once_token_1.49442
- _log.cn_once_token_1.51070
- _log.cn_once_token_1.51501
- _log.cn_once_token_1.52839
- _log.cn_once_token_1.55558
- _log.cn_once_token_1.58433
- _log.cn_once_token_1.61137
- _log.cn_once_token_1.9774
- _log.cn_once_token_2.38809
- _log.cn_once_token_2.41818
- _log.cn_once_token_2.51220
- _log.cn_once_token_20.44857
- _log.cn_once_token_20.47944
- _log.cn_once_token_6.13532
- _log.cn_once_token_6.23562
- _log.cn_once_token_6.36136
- _log.cn_once_token_6.51944
- _log.cn_once_token_6.66605
- _log.cn_once_token_9.23657
- _objc_msgSend$addContact:animated:
- _objc_msgSend$addContactsToListTappedWithSourceView:
- _objc_msgSend$applyContactListStyleToBlockedIcon:ofCell:
- _objc_msgSend$applyContactListStyleToContact:usingFormatter:ofCell:wantsInlineBlockIcon:
- _objc_msgSend$applyContactListStyleToContentConfiguration:usingState:forCell:
- _objc_msgSend$constraintGreaterThanOrEqualToSystemSpacingAfterAnchor:multiplier:
- _objc_msgSend$contactListAddContactButtonTapped:
- _objc_msgSend$contactListViewControllerSelectedAddContactToList:withSourceView:
- _objc_msgSend$contactListViewControllerSelectedCreateNewContact:
- _objc_msgSend$createNewBlockedIcon
- _objc_msgSend$createNewContactTapped
- _objc_msgSend$executeAddContact
- _objc_msgSend$initWithConfiguration:coordinateSpace:
- _objc_msgSend$initWithContact:contactStore:actionsProvider:customViewConfiguration:propertyViewConfiguration:isInlineContactCard:geminiManager:
- _objc_msgSend$initWithContact:propertyItems:actionDataSource:
- _objc_msgSend$initWithContact:propertyItems:favorites:
- _objc_msgSend$initWithContacts:listener:
- _objc_msgSend$initWithIdentifier:posterData:lastUsedDate:
- _objc_msgSend$initWithPosterArchiveData:metadata:contentIsSensitive:
- _objc_msgSend$presentAddToGroupPickerWithSourceView:
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objectdestroy.126Tm
- _objectdestroy.202Tm
- _objectdestroy.52Tm
- _objectdestroy.99Tm
- _os_log.cn_once_object_1.10319
- _os_log.cn_once_object_1.63728
- _os_log.cn_once_object_1.64247
- _os_log.cn_once_object_1.9442
- _os_log.cn_once_object_6.53771
- _os_log.cn_once_object_6.66213
- _os_log.cn_once_token_1.10317
- _os_log.cn_once_token_1.63726
- _os_log.cn_once_token_1.64245
- _os_log.cn_once_token_1.9440
- _os_log.cn_once_token_6.53769
- _os_log.cn_once_token_6.66211
- _pathToContentUnavailableRow.cn_once_object_28
- _pathToContentUnavailableRow.cn_once_token_28
- _pathToCreateNewContactRow.cn_once_object_27
- _pathToCreateNewContactRow.cn_once_token_27
- _pathToDuplicatesBanner.cn_once_object_26
- _pathToDuplicatesBanner.cn_once_token_26
- _pathToLimitedAccessTipRow.cn_once_object_15
- _pathToLimitedAccessTipRow.cn_once_token_15
- _supportedPasteboardTypes.cn_once_object_1.51518
- _supportedPasteboardTypes.cn_once_token_1.51516
- _symbolic Si6offset______7elementtSg 14ContactsUICore26ContactCardGroupHeaderItemV
- _symbolic ______p 7SwiftUI10ShapeStyleP
- _symbolic _____yAAyAAy_____yAAy__________y_____GGSgG_____G_____G_____G 7SwiftUI15ModifiedContentV AA6ButtonV 08ContactsB0022CNAvatarViewControllerH0V AA21_TraitWritingModifierV AA010TransitionJ3KeyV AA05_TaskL0V AA14_PaddingLayoutV AA17_FlipForRTLEffectV
- _symbolic _____yAAy__________GACG 7SwiftUI15ModifiedContentV 08ContactsB023CNOnboardingButtonsViewV AA14_PaddingLayoutV
- _symbolic _____yAAy__________G_____ySo9CNContactCGG 7SwiftUI15ModifiedContentV 08ContactsB0015ContactCardViewaB0V AA25_AppearanceActionModifierV AA010_TaskValueK0V
- _symbolic _____yAAy__________G_____ySo9CNContactCGG 7SwiftUI15ModifiedContentV 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AA010_TaskValueJ0V
- _symbolic _____yAAy_____yAAy__________y_____GGSgG_____G_____G 7SwiftUI15ModifiedContentV AA6ButtonV 08ContactsB0022CNAvatarViewControllerH0V AA21_TraitWritingModifierV AA010TransitionJ3KeyV AA05_TaskL0V AA14_PaddingLayoutV
- _symbolic _____yAAy_____y_____y_____yACy_____y__________G______y_____AJGSgtGG______tGG_____G_____G 7SwiftUI15ModifiedContentV AA5GroupV AA9TupleViewV AA6ZStackV AA06_ShapeG0V AA9RectangleV AA14LinearGradientV AA08ProgressG0V AA05EmptyG0V AA03AnyG0V 08ContactsB020CNPosterSnapshotMaskV AV0Q13VibrantShadowV
- _symbolic _____ySay_____GSS_____y__________y_____GGG 7SwiftUI7ForEachV 08ContactsB038CNWallpaperSuggestionsGalleryViewModelC15SuggestedAvatarV AA15ModifiedContentV AD0fgH0V0L16SuggestionButton33_81619BC199BAC997F7A0ACA40B51B6D6LLV AA21_TraitWritingModifierV AA010TransitionY3KeyV
- _symbolic _____ySo9CNContactCG 7SwiftUI18_TaskValueModifierV
- _symbolic _____y_____G 7SwiftUI19UIHostingControllerC AA7AnyViewV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 7SwiftUI4EdgeO3SetV
- _symbolic _____y_____GSg 7SwiftUI19UIHostingControllerC AA7AnyViewV
- _symbolic _____y__________G 7SwiftUI15ModifiedContentV 08ContactsB023CNOnboardingButtonsViewV AA14_PaddingLayoutV
- _symbolic _____y__________G 7SwiftUI19_ConditionalContentV 08ContactsB013InlineActionsV AD07WrappedfG0V
- _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
- _symbolic _____y_____yAAyAAy__________y_____GGACy_____SgGGACy_____SgGG_Qo_ 7SwiftUI4ViewPAAE15dynamicTypeSizeyQrAA07DynamiceF0OFQO AA15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AJ5ScaleO AA4FontV AA19SymbolRenderingModeV
- _symbolic _____y_____yAAy__________y_____GGSgG_____G 7SwiftUI15ModifiedContentV AA6ButtonV 08ContactsB0022CNAvatarViewControllerH0V AA21_TraitWritingModifierV AA010TransitionJ3KeyV AA05_TaskL0V
- _symbolic _____y_____yABy__________G_____ySo9CNContactCGGAByABy_____ADGAIGG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AA010_TaskValueK0V AF015ContactCardViewaB0V
- _symbolic _____y_____yABy__________G_____ySo9CNContactCGGAByABy_____ADGAIG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V 08ContactsB014AnswerTemplateV AA25_AppearanceActionModifierV AA010_TaskValueL0V AH015ContactCardViewaB0V
- _symbolic _____y_____y_____ACG_____y_____SgGGSg 7SwiftUI15ModifiedContentV AA12ProgressViewV AA05EmptyF0V AA30_EnvironmentKeyWritingModifierV AA5ColorV
- _symbolic _____y_____y______Qo______y_____GG 7SwiftUI15ModifiedContentV AA4ViewP14ContactsUICoreE24asClearBackgroundSectionQryFQO AF06HeaderE0V AA30_EnvironmentKeyWritingModifierV AF23ContactCardDetailsStyleV
- _symbolic _____y_____y___________Qo_______Qo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AcAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO 14ContactsUICore023ContactPosterBackgroundC0V AK0mN22ScrollGeometryObserverC 0kB00mnpQ0V
- _symbolic _____y_____y_____yABy_____y__________G______y_____AIGSgtGG___________SgtGG 7SwiftUI5GroupV AA9TupleViewV AA6ZStackV AA06_ShapeE0V AA9RectangleV AA14LinearGradientV AA08ProgressE0V AA05EmptyE0V AA03AnyE0V 08ContactsB0020SensitiveContentBlurE0V
- _symbolic _____y_____y_____yABy_____y__________G______y_____AIGSgtGG______tGG 7SwiftUI5GroupV AA9TupleViewV AA6ZStackV AA06_ShapeE0V AA9RectangleV AA14LinearGradientV AA08ProgressE0V AA05EmptyE0V AA03AnyE0V
- _symbolic _____y_____y_____y_____G______y_____yAFy__________y_____SgGGG_____GSgtGG 7SwiftUI6HStackV AA9TupleViewV AA9TextFieldV AA0F0V AA15ModifiedContentV AA6ButtonV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA14_PaddingLayoutV
- _symbolic _____y_____y_____y__________GG_____G 7SwiftUI15ModifiedContentV 14ContactsUICore11ContactCardV AA012_ConditionalD0V 0eB013InlineActionsV AI07WrappedjK0V AA30_SafeAreaRegionsIgnoringLayoutV
- _symbolic _____y_____y_____y__________G______yAGy_____yAByACyACyACy__________G_____G_____G______y_____y_____yAByAD_AAyAByAD_ACyACy_____yACyACyACy__________y_____GGATy_____SgGGATy_____SgGG_Qo_ANGANGtGGtGGGGSgtGGAHyABy_____y_____A17_G_ACyACyACyACy_____y__________GAJGALG_____y_____GGANGtGGGACyACy_____ALGANGGAfCyACyACyACy_____ALGATy_____GGANG_____y_____GGAfCyACyACyA41_ATy_____GGANGA45_GACyACyAdLGA45_GACyACyACy_____ANGANGA45_GtGG 7SwiftUI6VStackV AA9TupleViewV AA15ModifiedContentV AA6SpacerV AA12_FrameLayoutV AA012_ConditionalG0V AA6ZStackV 08ContactsB0035CNPosterOnboardingSettingsAnimationE0V AA012_AspectRatioJ0V AA05_FlexiJ0V AA08_PaddingJ0V AA6ButtonV AA14GeometryReaderV AA6HStackV AA0E0PAAE15dynamicTypeSizeyQrAA15DynamicTypeSizeOFQO AA5ImageV AA30_EnvironmentKeyWritingModifierV A9_5ScaleO AA4FontV AA19SymbolRenderingModeV AA08ProgressE0V AA05EmptyE0V AA06_ShapeE0V AA9RectangleV AA5ColorV AA11_ClipEffectV AA16RoundedRectangleV AP013CNPhotoCircleE0V AA4TextV AA13TextAlignmentO AA21_TraitWritingModifierV AA0J16PriorityTraitKeyV 12CoreGraphics7CGFloatV AP019CNOnboardingButtonsE0V
- _symbolic _____y_____y_____y______y_____G_____y_____ySay_____G__________G_AAyAHySay_____GSSAAy__________y_____GGGASGSgtGGG_____G 7SwiftUI15ModifiedContentV 08ContactsB036CNWallpaperSuggestionsGallerySectionV AA13_VariadicViewO4TreeV AA11_LayoutRootV AD0fg12SourceButtonkM0V AA05TupleK0V AA7ForEachV AD0fghO0V 10Foundation4UUIDV AD0fgH0V0oP033_81619BC199BAC997F7A0ACA40B51B6D6LLV AD0fghK5ModelC15SuggestedAvatarV AY016AvatarSuggestionP0A_LLV AA21_TraitWritingModifierV AA18TransitionTraitKeyV AA13_TaskModifierV
- _symbolic _____y_____y_____y_____y__________GG_____GSo9CNContactCG 7SwiftUI6IDViewV AA15ModifiedContentV 14ContactsUICore11ContactCardV AA012_ConditionalE0V 0fB013InlineActionsV AK07WrappedkL0V AA30_SafeAreaRegionsIgnoringLayoutV
- _symbolic _____y_____y_____y_____y_____y_____y________________tGG_Qo_G_Qo__SiQo_ 7SwiftUI4ViewPAAE14scrollPosition2id6anchorQrAA7BindingVyqd__SgG_AA9UnitPointVSgtSHRd__lFQO AC012_AppIntents_aB0E19appEntityIdentifieryQr0kL00nO0VSgFQO AA06ScrollC0V AcAE0D12TargetLayout9isEnabledQrSb_tFQO AA10LazyVStackV AA05TupleC0V 08ContactsB0021ContactCardHeaderNameC0V A0_0z12QuickActionsC0V A0_0yz7DetailsC0V
- _symbolic _____y_____y_____y_____y_____y_____y___________tGG_____y_____SgGG_Qo_GG 7SwiftUI6ButtonV AA6HStackV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA15ModifiedContentV AA5GroupV AA05TupleE0V AA5ImageV AA4TextV AA30_EnvironmentKeyWritingModifierV AJ
- _symbolic _____y_____y_____y_____y_____y_____y_____y_____y________________tGG_Qo_G_Qo__SiQo______G______Qo_ 7SwiftUI4ViewPAAE22onScrollGeometryChange3for2of6actionQrqd__m_qd__AA0eF0Vcyqd___qd__tctSQRd__lFQO AA15ModifiedContentV AcAE14scrollPosition2id6anchorQrAA7BindingVyqd__SgG_AA9UnitPointVSgtSHRd__lFQO AC012_AppIntents_aB0E19appEntityIdentifieryQr0tU00wX0VSgFQO AA0eC0V AcAE0M12TargetLayout9isEnabledQrSb_tFQO AA10LazyVStackV AA05TupleC0V 08ContactsB0021ContactCardHeaderNameC0V A8_016CardQuickActionsC0V A8_018ContactCardDetailsC0V AA23SafeAreaPaddingModifierV 12CoreGraphics7CGFloatV
- _yearlessFormatter.44299
CStrings:
+ "%d.%d.%d"
+ "("
+ "+contactsAuthStatusIsDenied"
+ "+contactsAuthStatusIsFullAccess"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNAccount+UIAdditions.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNActionView.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNActionsView.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNAvatarCardController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactAsyncDataSource.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactDeleteContactAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactIgnoreDonatedInformationAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactOrbActionsController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactPhotoView.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactPickerHostViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactPickerServiceViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactPickerViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactSuggestionAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNContactViewHostViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNMonogrammer.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPhotoPickerCapabilities.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPhotoPickerHeaderView.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPropertyAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPropertyIDSRequest.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPropertyLinkedCardsAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNPropertySuggestionAction.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNQuickActionsUsageManager.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNQuickActionsView.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNShareLocationController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNUIFamilyMemberDowntimeContactDataSource.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNUIMapTileGenerator.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/CNVCardViewController.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/Framework/LimitedAccess/CNLimitedAccessPickerSupport.m"
+ "/Library/Caches/com.apple.xbs/98AF9E63-8517-4A3A-A4AC-F850D0C435C8/TemporaryDirectory.gADbnd/Sources/ContactsUI/OldFramework/Sources/ContactsUI_Internal.m"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "@\"<CNUICoreLocationSharingModificationCheck>\""
+ "@\"CNEditInAppAction\""
+ "@\"CNUIUserActionListDataSource\"16@0:8"
+ "@\"UIBarButtonItem\"16@?0@\"UIZoomTransitionSourceViewProviderContext\"8"
+ "@\"UIToolbar\""
+ "@\"UIView\"16@?0@\"UIZoomTransitionSourceViewProviderContext\"8"
+ "@40@0:8@16B24B28q32"
+ "@72@0:8@16@24@32@40@48B56@60B68"
+ "B24@0:8d16"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "CNOOPContactContentViewController"
+ "ContactsButtonSlotTraits"
+ "Missing database entitlement"
+ "ProductVersion"
+ "T@\"CNEditInAppAction\",&,N,V_editInAppAction"
+ "T@\"NSLayoutConstraint\",&,N,V_contactNameViewWidthContraint"
+ "T@\"UIImage\",&,N,V_blockedIcon"
+ "T@\"UIToolbar\",&,N,V_editingToolbar"
+ "TB,N,R,VisOutOfProcess"
+ "TB,N,V_configuredAsBlocked"
+ "Unable to copy contact %@"
+ "Unknown Account"
+ "View.task @ ContactsUI/CNWallpaperSuggestionsGallery.swift:"
+ "View.task @ ContactsUI/ContactCardViewSwift.swift:"
+ "[CNAccountsAndGroupsDataSource] %ld contacts found for %{public}@ (%{public}@)"
+ "[CNAccountsAndGroupsDataSource] %ld contacts found for 'All Contacts'"
+ "[CNAccountsAndGroupsDataSource] %ld contacts found in group '%{public}@' for %{public}@"
+ "[CNAccountsAndGroupsDataSource] %ld total contacts found for account %{public}@"
+ "_TtC10ContactsUI23ContactHeaderAppearance"
+ "_blockedIcon"
+ "_cn_appleAccountAppleID"
+ "_configuredAsBlocked"
+ "_contactNameViewWidthContraint"
+ "_editInAppAction"
+ "_editingToolbar"
+ "_hasInProcessContactsDatabaseEntitlement"
+ "_locationSharingModificationCheck"
+ "_setOverrideInlineActiveWidth:"
+ "addContact:animated:sender:"
+ "addContactsToListTappedWithSender:"
+ "applyContactListStyleToContact:usingFormatter:ofCell:"
+ "applyContentConfigurationUsingState:forCell:"
+ "arrow.backward"
+ "arrow.forward"
+ "arrow.trianglehead.merge"
+ "attributedTextForContact:usingFormatter:isBlocked:hasSubtitle:"
+ "avatarSizeForWidth:"
+ "blockedIcon"
+ "canModifySharingLocations"
+ "configuredAsBlocked"
+ "contactListAddContactButtonTapped:sender:"
+ "contactListViewControllerSelectedAddContactToList:sender:"
+ "contactListViewControllerSelectedCreateNewContact:sender:"
+ "contactNameViewWidthContraint"
+ "core"
+ "createNewBlockedIconIfNecessary"
+ "createNewContactTapped:"
+ "dataUsingEncoding:"
+ "didBlockContactForInterventionViewController:"
+ "didPhotoChangeFromContact:toContact:"
+ "donateUpdatedContact:"
+ "editInAppAction"
+ "editingToolbar"
+ "ensureContactStoreExists"
+ "executeAddContact:"
+ "fileNameForContactName:"
+ "formattedHandle"
+ "initWithConfiguration:view:"
+ "initWithContact:contactStore:actionsProvider:customViewConfiguration:propertyViewConfiguration:isInlineContactCard:geminiManager:isOutOfProcess:"
+ "initWithContact:contactStore:isOutOfProcess:"
+ "initWithContact:isMeContact:saveChangesToContactStore:preferredDefaultIdentityType:"
+ "initWithContact:propertyItems:actionsDataSource:"
+ "initWithContact:propertyItems:favorites:actionsDataSource:"
+ "initWithContacts:listener:contactStore:"
+ "initWithIdentifier:posterData:lastUsedDate:itemDetails:"
+ "initWithPosterArchiveData:metadata:contentIsSensitive:sharedToMe:"
+ "isShowingGroups"
+ "kCFAllocatorNull"
+ "locationSharingModificationCheck"
+ "locationSharingModificationState"
+ "maximumWidthForNameView"
+ "onBlockContactForInterventionViewController:"
+ "preferredDefaultIdentityType"
+ "presentAddToGroupPickerWithSender:"
+ "r"
+ "refreshForCurrentlySelectedContact"
+ "setBlockedIcon:"
+ "setConfiguredAsBlocked:"
+ "setContactNameViewWidthContraint:"
+ "setEditInAppAction:"
+ "setEditingToolbar:"
+ "setHidesSharedBackground:"
+ "setPreferredPresentationStyle:"
+ "setPreferredTransition:"
+ "setPrefersGrabberVisible:"
+ "sharedToMe"
+ "showContactPhotos"
+ "targetProfileForActionType:context:"
+ "toolbarButtonItemsForTraitCollection:"
+ "updateSearchBarMaxSizeWithSize:"
+ "useVerticalLayoutForWidth:"
+ "v32@0:8@\"CNContactListViewController\"16@24"
+ "zoomWithOptions:sourceBarButtonItemProvider:"
+ "zoomWithOptions:sourceViewProvider:"
+ "{CGSize=dd}24@0:8d16"
+ "\xd1\xe1"
+ "\xf0S\xf0!\x81\xf0\xf0\xf0\xf0\xf0\xf0\xf0!"
- "+contactsAuthStatusIsDenied "
- "+contactsAuthStatusIsFullAccess "
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNAccount+UIAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNActionView.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNActionsView.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNAvatarCardController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactAsyncDataSource.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactDeleteContactAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactIgnoreDonatedInformationAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactOrbActionsController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactPhotoView.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactPickerHostViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactPickerServiceViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactPickerViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactSuggestionAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNContactViewHostViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNMonogrammer.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPhotoPickerCapabilities.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPhotoPickerHeaderView.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPropertyAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPropertyIDSRequest.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPropertyLinkedCardsAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNPropertySuggestionAction.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNQuickActionsUsageManager.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNQuickActionsView.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNShareLocationController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNUIFamilyMemberDowntimeContactDataSource.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNUIMapTileGenerator.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/CNVCardViewController.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/Framework/LimitedAccess/CNLimitedAccessPickerSupport.m"
- "/Library/Caches/com.apple.xbs/Sources/ContactsUI/OldFramework/Sources/ContactsUI_Internal.m"
- "@68@0:8@16@24@32@40@48B56@60"
- "addContactsToListTappedWithSourceView:"
- "applyContactListStyleToBlockedIcon:ofCell:"
- "applyContactListStyleToContact:usingFormatter:ofCell:wantsInlineBlockIcon:"
- "applyContactListStyleToContentConfiguration:usingState:forCell:"
- "constraintGreaterThanOrEqualToSystemSpacingAfterAnchor:multiplier:"
- "contactListAddContactButtonTapped:"
- "contactListViewControllerSelectedAddContactToList:withSourceView:"
- "contactListViewControllerSelectedCreateNewContact:"
- "createNewBlockedIcon"
- "createNewContactTapped"
- "executeAddContact"
- "initWithConfiguration:coordinateSpace:"
- "initWithContact:contactStore:actionsProvider:customViewConfiguration:propertyViewConfiguration:isInlineContactCard:geminiManager:"
- "initWithContact:propertyItems:actionDataSource:"
- "initWithContact:propertyItems:favorites:"
- "initWithContacts:listener:"
- "initWithIdentifier:posterData:lastUsedDate:"
- "initWithPosterArchiveData:metadata:contentIsSensitive:"
- "presentAddToGroupPickerWithSourceView:"
- "v32@0:8@\"CNContactListViewController\"16@\"UIView\"24"

```
