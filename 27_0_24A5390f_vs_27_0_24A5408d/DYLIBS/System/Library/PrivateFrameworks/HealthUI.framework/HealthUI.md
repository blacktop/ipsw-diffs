## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-7027.0.67.2.1
-  __TEXT.__text: 0x44e804
-  __TEXT.__objc_methlist: 0x3b41c
-  __TEXT.__const: 0x8d74
+7027.0.72.2.5
+  __TEXT.__text: 0x44cc58
+  __TEXT.__objc_methlist: 0x3b5dc
+  __TEXT.__const: 0x8d94
   __TEXT.__gcc_except_tab: 0x23d4
-  __TEXT.__cstring: 0x233af
-  __TEXT.__oslogstring: 0x74e5
+  __TEXT.__cstring: 0x2355f
+  __TEXT.__oslogstring: 0x7635
   __TEXT.__ustring: 0x56
   __TEXT.__dlopen_cstrs: 0x367
-  __TEXT.__constg_swiftt: 0x4eac
-  __TEXT.__swift5_typeref: 0x3542
+  __TEXT.__constg_swiftt: 0x4ee8
+  __TEXT.__swift5_typeref: 0x3544
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x31a6
-  __TEXT.__swift5_fieldmd: 0x30d8
+  __TEXT.__swift5_reflstr: 0x31f6
+  __TEXT.__swift5_fieldmd: 0x3118
   __TEXT.__swift5_assocty: 0x7e8
   __TEXT.__swift5_proto: 0x398
-  __TEXT.__swift5_types: 0x3f0
-  __TEXT.__swift5_capture: 0x1510
+  __TEXT.__swift5_types: 0x3f4
+  __TEXT.__swift5_capture: 0x14d4
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__swift_as_entry: 0x9c
-  __TEXT.__swift_as_ret: 0x8c
-  __TEXT.__swift_as_cont: 0x164
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0x80
+  __TEXT.__swift_as_cont: 0x144
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0xf420
-  __TEXT.__eh_frame: 0x34e8
+  __TEXT.__unwind_info: 0xf430
+  __TEXT.__eh_frame: 0x3340
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x79b8
-  __DATA_CONST.__objc_classlist: 0x21b0
+  __DATA_CONST.__const: 0x79e0
+  __DATA_CONST.__objc_classlist: 0x21c8
   __DATA_CONST.__objc_catlist: 0x2a8
-  __DATA_CONST.__objc_protolist: 0x6c8
+  __DATA_CONST.__objc_protolist: 0x6d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18ae0
-  __DATA_CONST.__objc_protorefs: 0x188
-  __DATA_CONST.__objc_superrefs: 0x1870
+  __DATA_CONST.__objc_selrefs: 0x18b90
+  __DATA_CONST.__objc_protorefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x1878
   __DATA_CONST.__objc_arraydata: 0x2080
-  __DATA_CONST.__got: 0x3858
-  __AUTH_CONST.__const: 0x8c58
-  __AUTH_CONST.__cfstring: 0x1e9c0
-  __AUTH_CONST.__objc_const: 0x662d0
+  __DATA_CONST.__got: 0x38b0
+  __AUTH_CONST.__const: 0x8c10
+  __AUTH_CONST.__cfstring: 0x1ea40
+  __AUTH_CONST.__objc_const: 0x66650
   __AUTH_CONST.__objc_intobj: 0x2a00
   __AUTH_CONST.__objc_doubleobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0xf60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x3120
-  __AUTH.__objc_data: 0x183e8
-  __AUTH.__data: 0x2640
-  __DATA.__objc_ivar: 0x4060
-  __DATA.__data: 0x8308
-  __DATA.__bss: 0x7030
+  __AUTH_CONST.__auth_got: 0x3158
+  __AUTH.__objc_data: 0x18548
+  __AUTH.__data: 0x2670
+  __DATA.__objc_ivar: 0x407c
+  __DATA.__data: 0x8378
+  __DATA.__bss: 0x7050
   __DATA.__common: 0x260
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__bss: 0x58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26382
-  Symbols:   45410
-  CStrings:  5320
+  Functions: 26414
+  Symbols:   45496
+  CStrings:  5334
 
Symbols:
+ +[HKExternalImageProvider _sharedProvider]
+ +[HKExternalImageProvider imageReferenceForKind:]
+ +[HKInteractiveChartViewController _heightDesignationForViewController:]
+ +[HKInteractiveChartViewController shouldUseNavigationBarLayoutForViewController:]
+ -[HKAuthorizationPresentationController presentationDidFailHandler]
+ -[HKAuthorizationPresentationController setPresentationDidFailHandler:]
+ -[HKAxis omitsOverlappingLabels]
+ -[HKAxisConfiguration omitsOverlappingLabels]
+ -[HKAxisConfiguration setOmitsOverlappingLabels:]
+ -[HKExternalImageReference .cxx_destruct]
+ -[HKExternalImageReference bundle]
+ -[HKExternalImageReference initWithName:bundle:]
+ -[HKExternalImageReference name]
+ -[HKNanoHostAuthorizationController beginSettingsReauthorizationForSource:readTypes:writeTypes:]
+ -[HKNanoHostAuthorizationController didFinish]
+ -[HKNanoHostAuthorizationController setDidFinish:]
+ -[HKOverlayRoomViewController overlayZeroHeightConstraint]
+ -[HKOverlayRoomViewController setOverlayZeroHeightConstraint:]
+ -[HKSourceAuthorizationController commonHistoryWindowForReadTypes:]
+ -[HKSourceAuthorizationController presentSettingsReauthorizationWithCompletion:]
+ GCC_except_table141
+ GCC_except_table62
+ GCC_except_table75
+ GCC_except_table78
+ _HKCategoryTypeIdentifierBleedingAfterMenopause
+ _HKCategoryTypeIdentifierBleedingAfterPregnancy
+ _HKCategoryTypeIdentifierBleedingDuringPregnancy
+ _HKCategoryTypeIdentifierLactation
+ _HKCategoryTypeIdentifierMenopausalState
+ _HKCategoryTypeIdentifierPregnancy
+ _HKErrorDomain
+ _HKQuantityTypeIdentifierAtrialFibrillationBurden
+ _OBJC_CLASS_$_HKExternalImageProvider
+ _OBJC_CLASS_$_HKExternalImageReference
+ _OBJC_IVAR_$_HKAuthorizationPresentationController._presentationDidFailHandler
+ _OBJC_IVAR_$_HKAxis._omitsOverlappingLabels
+ _OBJC_IVAR_$_HKAxisConfiguration._omitsOverlappingLabels
+ _OBJC_IVAR_$_HKExternalImageReference._bundle
+ _OBJC_IVAR_$_HKExternalImageReference._name
+ _OBJC_IVAR_$_HKNanoHostAuthorizationController._didFinish
+ _OBJC_IVAR_$_HKOverlayRoomViewController._overlayZeroHeightConstraint
+ _OBJC_METACLASS_$_HKExternalImageProvider
+ _OBJC_METACLASS_$_HKExternalImageReference
+ _OBJC_METACLASS_$__TtC8HealthUIP33_6437C8397BE458390DCCD81C27D63EDE27AuthorizationFooterTextView
+ __DATA__TtC8HealthUIP33_6437C8397BE458390DCCD81C27D63EDE27AuthorizationFooterTextView
+ __HKCategoryTypeIdentifierIsSensitiveForLogging.onceToken
+ __HKCategoryTypeIdentifierIsSensitiveForLogging.sensitiveIdentifiers
+ __HKQuantityTypeIdentifierIsSensitiveForLogging.onceToken
+ __HKQuantityTypeIdentifierIsSensitiveForLogging.sensitiveIdentifiers
+ __INSTANCE_METHODS__TtC8HealthUIP33_6437C8397BE458390DCCD81C27D63EDE27AuthorizationFooterTextView
+ __IVARS__TtC8HealthUIP33_6437C8397BE458390DCCD81C27D63EDE27AuthorizationFooterTextView
+ __METACLASS_DATA__TtC8HealthUIP33_6437C8397BE458390DCCD81C27D63EDE27AuthorizationFooterTextView
+ __OBJC_$_CLASS_METHODS_HKExternalImageProvider
+ __OBJC_$_INSTANCE_METHODS_HKExternalImageReference
+ __OBJC_$_INSTANCE_VARIABLES_HKExternalImageReference
+ __OBJC_$_PROP_LIST_HKExternalImageReference
+ __OBJC_$_PROP_LIST__HKAuthorizationPresentationController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HealthAssetBundleImageProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HKHealthPrivacyServiceRemoteAuthorizationViewController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HealthAssetBundleImageProviding
+ __OBJC_$_PROTOCOL_REFS_HealthAssetBundleImageProviding
+ __OBJC_CLASS_RO_$_HKExternalImageProvider
+ __OBJC_CLASS_RO_$_HKExternalImageReference
+ __OBJC_LABEL_PROTOCOL_$_HealthAssetBundleImageProviding
+ __OBJC_METACLASS_RO_$_HKExternalImageProvider
+ __OBJC_METACLASS_RO_$_HKExternalImageReference
+ __OBJC_PROTOCOL_$_HealthAssetBundleImageProviding
+ __OBJC_PROTOCOL_REFERENCE_$_HealthAssetBundleImageProviding
+ ___42+[HKExternalImageProvider _sharedProvider]_block_invoke
+ ___96-[HKNanoHostAuthorizationController beginSettingsReauthorizationForSource:readTypes:writeTypes:]_block_invoke
+ ____HKCategoryTypeIdentifierIsSensitiveForLogging_block_invoke
+ ____HKQuantityTypeIdentifierIsSensitiveForLogging_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e67_v16?0"<HKHealthPrivacyServiceRemoteAuthorizationViewController>"8ls32l8s40l8s48l8
+ __sharedProvider.onceToken
+ __sharedProvider.provider
+ _objc_msgSend$_heightDesignationForViewController:
+ _objc_msgSend$_sharedProvider
+ _objc_msgSend$beginSettingsReauthorizationForSource:readTypes:writeTypes:
+ _objc_msgSend$dateBySettingHour:minute:second:ofDate:options:
+ _objc_msgSend$didFinish
+ _objc_msgSend$imageNameForKind:
+ _objc_msgSend$initWithName:bundle:
+ _objc_msgSend$omitsOverlappingLabels
+ _objc_msgSend$presentationDidFailHandler
+ _objc_msgSend$principalClass
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDidFinish:
+ _objc_msgSend$setEstimatedSectionFooterHeight:
+ _objc_msgSend$setOmitsOverlappingLabels:
+ _objc_msgSend$setSelfSizingInvalidation:
+ _symbolic SDyS2SG
+ _symbolic _____ 10Foundation6LocaleV
+ _symbolic _____ 8HealthUI27AuthorizationFooterTextView33_6437C8397BE458390DCCD81C27D63EDELLC
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 10Foundation6LocaleV
- GCC_except_table139
- GCC_except_table60
- GCC_except_table73
- _objc_msgSend$removeTarget:action:forControlEvents:
- _objc_msgSend$setEnabled:forTypes:inSection:commit:
- _swift_release_x12
- _symbolic So11UIStackViewC
- _symbolic So8UIButtonC
CStrings:
+ "/System/Library/Health/ImageBundles/HealthAssetBundle.bundle"
+ "AUTHORIZATION_PROMPT_ACCESS_BODY_SHARE"
+ "AUTHORIZATION_PROMPT_ACCESS_BODY_WRITE_ONLY"
+ "AUTHORIZATION_PROMPT_ACCESS_TITLE_%@"
+ "AUTHORIZATION_READ_ACCESS_HEADER"
+ "AUTHORIZATION_WRITE_ACCESS_HEADER"
+ "AuthorizationFooterTextViewIdentifier"
+ "CLINICAL_DOCUMENTS_REQUEST_AUTH_DESCRIPTION_THIS_APP"
+ "DISABLE_ALL_%ld_CATEGORIES"
+ "HKExternalImageProvider: failed to load %{public}@: %{public}@"
+ "HKExternalImageProvider: principal class %{public}@ does not conform to HealthAssetBundleImageProviding"
+ "HKLevelCategory(<redacted>)"
+ "HKNanoHostAuthorizationController: Failed to begin settings reauthorization with error: %{public}@"
+ "HKNanoHostAuthorizationController: begin settings reauthorization for %{public}@"
+ "HKQuantityType(<redacted>)"
+ "MMMdjmm"
+ "TIME_BOUNDED_AUTH_SELECT_DATA_BODY"
+ "The authorization prompt could not be presented from this process."
- "MMMdjj"
- "TIME_BOUNDED_AUTH_TOPICS_SELECTED_%ld"
- "queryDayDatesWithData(for:since:healthStore:)"
- "queryEarliestSampleDate(for:healthStore:)"
```
