## CallsDialer

> `/System/Library/PrivateFrameworks/CallsDialer.framework/CallsDialer`

```diff

-3011.100.2.2.10
-  __TEXT.__text: 0x27108
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x296c
-  __TEXT.__const: 0x874
-  __TEXT.__cstring: 0x11fb
+3015.100.5.2.4
+  __TEXT.__text: 0x29e04
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0x2b44
+  __TEXT.__const: 0x974
+  __TEXT.__cstring: 0x13eb
   __TEXT.__gcc_except_tab: 0x220
   __TEXT.__oslogstring: 0x11da
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__swift5_typeref: 0x186
-  __TEXT.__constg_swiftt: 0x154
-  __TEXT.__swift5_reflstr: 0x15c
-  __TEXT.__swift5_fieldmd: 0x114
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__swift5_typeref: 0x1ec
+  __TEXT.__swift5_capture: 0x50
+  __TEXT.__swift5_reflstr: 0x1cc
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__constg_swiftt: 0x254
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_fieldmd: 0x16c
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__unwind_info: 0xab0
   __TEXT.__objc_classname: 0x43c
-  __TEXT.__objc_methname: 0x9170
-  __TEXT.__objc_methtype: 0x153d
-  __TEXT.__objc_stubs: 0x76e0
-  __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__objc_methname: 0x9723
+  __TEXT.__objc_methtype: 0x159d
+  __TEXT.__objc_stubs: 0x7a00
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2678
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH_CONST.__const: 0x308
+  __AUTH_CONST.__auth_got: 0x738
+  __AUTH_CONST.__const: 0x4b8
   __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__objc_const: 0x3730
+  __AUTH_CONST.__objc_const: 0x39f0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x270
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x258
-  __DATA.__data: 0x828
-  __DATA.__bss: 0x550
+  __AUTH.__objc_data: 0x400
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x270
+  __DATA.__data: 0x880
+  __DATA.__bss: 0x6d0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x5b0
   __DATA_DIRTY.__data: 0x68

   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E40674A6-A3E0-3A22-9F63-266FB02FAE31
-  Functions: 996
-  Symbols:   3626
-  CStrings:  2255
+  UUID: 38B9F04E-5951-3ABF-9EB3-C2F2D33A7F72
+  Functions: 1122
+  Symbols:   3743
+  CStrings:  2330
 
Symbols:
+ -[DialerController performCallActionForCallProvider:video:senderIdentity:ttyType:]
+ -[DialerController tabBarIconImage]
+ -[DialerController tabBarIconName]
+ -[MPKeypadViewController handleSelectedSenderIdentity:]
+ -[MPKeypadViewController senderIdentityClient]
+ -[MPKeypadViewController setSimLineSelectionAnalyticsReporter:]
+ -[MPKeypadViewController simLineSelectionAnalyticsReporter]
+ -[PHHandsetDialerLCDView dialerReporter]
+ -[PHHandsetDialerLCDView dialerResultButtonsGlassBackgroundView]
+ -[PHHandsetDialerLCDView logWithCall]
+ -[PHHandsetDialerLCDView logWithCancel]
+ -[PHHandsetDialerLCDView resultButtonsHorizontalPadding]
+ -[PHHandsetDialerLCDView secondaryHiddenConstraint]
+ -[PHHandsetDialerLCDView secondaryVisibleConstraint]
+ -[PHHandsetDialerLCDView setDialerReporter:]
+ -[PHHandsetDialerLCDView setDialerResultButtonsGlassBackgroundView:]
+ -[PHHandsetDialerLCDView setSecondaryHiddenConstraint:]
+ -[PHHandsetDialerLCDView setSecondaryVisibleConstraint:]
+ -[PHHandsetDialerLCDView updateDialerResultGlassBackgroundConstraintsForSecondaryButtonVisibility:]
+ GCC_except_table34
+ GCC_except_table62
+ GCC_except_table78
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_MPAnalyticsLogger
+ _OBJC_CLASS_$_MPDialerInterceptReporter
+ _OBJC_CLASS_$_TUSenderIdentityClient
+ _OBJC_IVAR_$_MPKeypadViewController._senderIdentityClient
+ _OBJC_IVAR_$_MPKeypadViewController._simLineSelectionAnalyticsReporter
+ _OBJC_IVAR_$_PHHandsetDialerLCDView._dialerReporter
+ _OBJC_IVAR_$_PHHandsetDialerLCDView._dialerResultButtonsGlassBackgroundView
+ _OBJC_IVAR_$_PHHandsetDialerLCDView._secondaryHiddenConstraint
+ _OBJC_IVAR_$_PHHandsetDialerLCDView._secondaryVisibleConstraint
+ _OBJC_METACLASS_$_MPDialerInterceptReporter
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_MPDialerInterceptReporter
+ __CLASS_PROPERTIES_MPDialerInterceptReporter
+ __DATA_MPDialerInterceptReporter
+ __INSTANCE_METHODS_MPDialerInterceptReporter
+ __IVARS_MPDialerInterceptReporter
+ __METACLASS_DATA_MPDialerInterceptReporter
+ __PROPERTIES_MPDialerInterceptReporter
+ __UISolariumEnabled
+ ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.133
+ ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.133.cold.1
+ ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.135
+ ___96-[PHHandsetDialerLCDView updateAddAndDeleteButtonForText:name:label:source:suggestion:animated:]_block_invoke.131
+ ___96-[PHHandsetDialerLCDView updateAddAndDeleteButtonForText:name:label:source:suggestion:animated:]_block_invoke_2.132
+ __swiftEmptyDictionarySingleton
+ _associated conformance 11CallsDialer0B23InterceptSelectedOptionOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.16
+ _block_copy_helper.23
+ _block_copy_helper.36
+ _block_copy_helper.9
+ _block_descriptor
+ _block_descriptor.11
+ _block_descriptor.18
+ _block_descriptor.25
+ _block_descriptor.38
+ _block_destroy_helper
+ _block_destroy_helper.10
+ _block_destroy_helper.17
+ _block_destroy_helper.24
+ _block_destroy_helper.37
+ _kCACornerCurveContinuous
+ _objc_msgSend$dialerResultButtonsGlassBackgroundView
+ _objc_msgSend$dialer_applyGlassBackground
+ _objc_msgSend$dismissModalViewControllerAnimated:
+ _objc_msgSend$handleSelectedSenderIdentity:
+ _objc_msgSend$horizontalPadding
+ _objc_msgSend$logSIMLineSelection:
+ _objc_msgSend$logWith:
+ _objc_msgSend$logWithCall
+ _objc_msgSend$logWithCancel
+ _objc_msgSend$performCallActionForCallProvider:video:senderIdentity:ttyType:
+ _objc_msgSend$resultButtonsHorizontalPadding
+ _objc_msgSend$secondaryHiddenConstraint
+ _objc_msgSend$secondaryVisibleConstraint
+ _objc_msgSend$setAutocomplete:
+ _objc_msgSend$setCornerCurve:
+ _objc_msgSend$setDialerResultButtonsGlassBackgroundView:
+ _objc_msgSend$setFirstShownOption:
+ _objc_msgSend$setSecondShownOption:
+ _objc_msgSend$setSecondaryHiddenConstraint:
+ _objc_msgSend$setSecondaryVisibleConstraint:
+ _objc_msgSend$setTtyType:
+ _objc_msgSend$simLineSelectionAnalyticsReporter
+ _objc_msgSend$updateDialerResultGlassBackgroundConstraintsForSecondaryButtonVisibility:
+ _objc_msgSend$updateForDialerResultPressed:savedContact:
+ _objc_msgSend$uplevelFTAEnabled
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_endAccess
+ _swift_initStackObject
+ _swift_isaMask
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _symbolic SS_So8NSObjectCt
+ _symbolic Sb
+ _symbolic So8NSObjectC
+ _symbolic _____ 11CallsDialer0B17InterceptReporterC
+ _symbolic _____ 11CallsDialer0B23InterceptSelectedOptionO
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
- +[DialerController tabBarIconImage]
- +[DialerController tabBarIconName]
- GCC_except_table32
- GCC_except_table60
- GCC_except_table74
- ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.132
- ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.132.cold.1
- ___89-[MPKeypadViewController searchAndUpdateResultsFor:shouldRefreshResult:showPastedString:]_block_invoke.134
- ___96-[PHHandsetDialerLCDView updateAddAndDeleteButtonForText:name:label:source:suggestion:animated:]_block_invoke.128
- ___96-[PHHandsetDialerLCDView updateAddAndDeleteButtonForText:name:label:source:suggestion:animated:]_block_invoke_2.131
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CallsDialer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CallsDialer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CallsDialer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CallsDialer
CStrings:
+ "@\"MPAnalyticsLogger\""
+ "@\"MPDialerInterceptReporter\""
+ "@\"NSDictionary\"8@?0"
+ "@\"TUSenderIdentityClient\""
+ "MPDialerInterceptReporter"
+ "T@\"MPAnalyticsLogger\",&,N,V_simLineSelectionAnalyticsReporter"
+ "T@\"MPDialerInterceptReporter\",&,N,V_dialerReporter"
+ "T@\"NSLayoutConstraint\",&,N,V_secondaryHiddenConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_secondaryVisibleConstraint"
+ "T@\"NSString\",N,R"
+ "T@\"TUSenderIdentityClient\",R,N,V_senderIdentityClient"
+ "T@\"UIView\",&,V_dialerResultButtonsGlassBackgroundView"
+ "TB,N,VappleSupport"
+ "TB,N,Vautocomplete"
+ "TB,N,VsavedContact"
+ "Tq,N,VfirstShownOption"
+ "Tq,N,VsecondShownOption"
+ "Tq,N,VselectedOption"
+ "_dialerReporter"
+ "_dialerResultButtonsGlassBackgroundView"
+ "_secondaryHiddenConstraint"
+ "_secondaryVisibleConstraint"
+ "_senderIdentityClient"
+ "_simLineSelectionAnalyticsReporter"
+ "appleSupport"
+ "autocomplete"
+ "com.apple.phone.dialer_intercept"
+ "constraintLessThanOrEqualToAnchor:"
+ "dialerReporter"
+ "dialerResultButtonsGlassBackgroundView"
+ "dismissModalViewControllerAnimated:"
+ "eventName"
+ "firstShownOption"
+ "handleSelectedSenderIdentity:"
+ "log"
+ "logSIMLineSelection:"
+ "logWith:"
+ "logWithCall"
+ "logWithCancel"
+ "performCallActionForCallProvider:video:senderIdentity:ttyType:"
+ "resultButtonsHorizontalPadding"
+ "savedContact"
+ "secondShownOption"
+ "secondaryHiddenConstraint"
+ "secondaryVisibleConstraint"
+ "selectedOption"
+ "senderIdentityClient"
+ "setAccessibilityLabel:"
+ "setAppleSupport:"
+ "setAutocomplete:"
+ "setCornerCurve:"
+ "setDialerReporter:"
+ "setDialerResultButtonsGlassBackgroundView:"
+ "setFirstShownOption:"
+ "setIsAccessibilityElement:"
+ "setSavedContact:"
+ "setSecondShownOption:"
+ "setSecondaryHiddenConstraint:"
+ "setSecondaryVisibleConstraint:"
+ "setSelectedOption:"
+ "setSimLineSelectionAnalyticsReporter:"
+ "setTtyType:"
+ "simLineSelectionAnalyticsReporter"
+ "updateDialerResultGlassBackgroundConstraintsForSecondaryButtonVisibility:"
+ "updateForDialerResultPressed:savedContact:"
+ "uplevelFTAEnabled"
+ "v44@0:8@16B24@28q36"
- "!"
- "constraintLessThanOrEqualToAnchor:constant:"

```
