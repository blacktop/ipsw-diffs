## SetupAssistantUI

> `/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI`

```diff

-5380.0.0.0.0
-  __TEXT.__text: 0x21270
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x34cc
-  __TEXT.__const: 0x254
-  __TEXT.__cstring: 0x9a0
-  __TEXT.__gcc_except_tab: 0x2d8
-  __TEXT.__oslogstring: 0x117f
-  __TEXT.__dlopen_cstrs: 0x325
-  __TEXT.__swift5_typeref: 0xa6
-  __TEXT.__swift5_capture: 0x2c
-  __TEXT.__constg_swiftt: 0x50
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x9a0
-  __TEXT.__objc_classname: 0x88b
-  __TEXT.__objc_methname: 0x8a7d
-  __TEXT.__objc_methtype: 0x2d31
-  __TEXT.__objc_stubs: 0x5ae0
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0x6c0
-  __DATA_CONST.__objc_classlist: 0x170
+5381.1.2.0.0
+  __TEXT.__text: 0x2300c
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x3600
+  __TEXT.__const: 0x2f4
+  __TEXT.__cstring: 0xa80
+  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__oslogstring: 0x11c8
+  __TEXT.__dlopen_cstrs: 0x37f
+  __TEXT.__swift5_typeref: 0x132
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__swift5_fieldmd: 0x30
+  __TEXT.__constg_swiftt: 0x9c
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0xa58
+  __TEXT.__eh_frame: 0x160
+  __TEXT.__objc_classname: 0x8d7
+  __TEXT.__objc_methname: 0x8bb2
+  __TEXT.__objc_methtype: 0x2d82
+  __TEXT.__objc_stubs: 0x5b60
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2370
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x23b0
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x1e8
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x2b0
   __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x5600
+  __AUTH_CONST.__objc_const: 0x58c8
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xd90
-  __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x29c
-  __DATA.__data: 0xcf0
-  __DATA.__bss: 0x130
+  __AUTH.__objc_data: 0xea8
+  __AUTH.__data: 0xf0
+  __DATA.__objc_ivar: 0x2a8
+  __DATA.__data: 0xd58
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B1A27B5B-FD1F-3091-9D95-2E63F53B2B7C
-  Functions: 873
-  Symbols:   3489
-  CStrings:  2163
+  UUID: 55D23A56-BAF6-37B3-A888-7FDA5785BB69
+  Functions: 927
+  Symbols:   3576
+  CStrings:  2184
 
Symbols:
+ -[BFFFinishSetupIntelligenceController .cxx_destruct]
+ -[BFFFinishSetupIntelligenceController completion]
+ -[BFFFinishSetupIntelligenceController flowSkipController]
+ -[BFFFinishSetupIntelligenceController paneFeatureAnalyticsManager]
+ -[BFFFinishSetupIntelligenceController performExtendedInitializationWithCompletion:]
+ -[BFFFinishSetupIntelligenceController setCompletion:]
+ -[BFFFinishSetupIntelligenceController setFlowSkipController:]
+ -[BFFFinishSetupIntelligenceController setPaneFeatureAnalyticsManager:]
+ -[BFFFinishSetupIntelligenceController siriGMIntroViewControllerContinuePressed:]
+ -[BFFFinishSetupIntelligenceController siriGMIntroViewControllerNotNowPressed:]
+ -[BFFFinishSetupIntelligenceController viewControllerWithCompletion:]
+ _BYFlowSkipIdentifierAppleIntelligence
+ _OBJC_CLASS_$_BFFFinishSetupIntelligenceController
+ _OBJC_CLASS_$__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ _OBJC_IVAR_$_BFFFinishSetupIntelligenceController._completion
+ _OBJC_IVAR_$_BFFFinishSetupIntelligenceController._flowSkipController
+ _OBJC_IVAR_$_BFFFinishSetupIntelligenceController._paneFeatureAnalyticsManager
+ _OBJC_METACLASS_$_BFFFinishSetupIntelligenceController
+ _OBJC_METACLASS_$__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ __DATA__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ __INSTANCE_METHODS__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ __METACLASS_DATA__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ __OBJC_$_INSTANCE_METHODS_BFFFinishSetupIntelligenceController
+ __OBJC_$_INSTANCE_VARIABLES_BFFFinishSetupIntelligenceController
+ __OBJC_$_PROP_LIST_BFFFinishSetupIntelligenceController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VTUIGMEnrollmentViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VTUIGMEnrollmentViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VTUIGMEnrollmentViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_VTUIGMEnrollmentViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BFFFinishSetupIntelligenceController
+ __OBJC_CLASS_RO_$_BFFFinishSetupIntelligenceController
+ __OBJC_LABEL_PROTOCOL_$_VTUIGMEnrollmentViewControllerDelegate
+ __OBJC_METACLASS_RO_$_BFFFinishSetupIntelligenceController
+ __OBJC_PROTOCOL_$_VTUIGMEnrollmentViewControllerDelegate
+ __PROTOCOLS__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider
+ __PROTOCOLS__TtC16SetupAssistantUI27BuddyGMAvailabilityProvider.4
+ __PROTOCOL_INSTANCE_METHODS__TtP16SetupAssistantUI36ProvidesGenerativeModelsAvailability_
+ __PROTOCOL_METHOD_TYPES__TtP16SetupAssistantUI36ProvidesGenerativeModelsAvailability_
+ __PROTOCOL__TtP16SetupAssistantUI36ProvidesGenerativeModelsAvailability_
+ ___41-[BFFFinishSetupViewController _complete]_block_invoke.71
+ ___84-[BFFFinishSetupIntelligenceController performExtendedInitializationWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___getVTUIGMEnrollmentViewControllerClass_block_invoke
+ ___getVTUIGMEnrollmentViewControllerClass_block_invoke.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _getVTUIGMEnrollmentViewControllerClass.softClass
+ _objc_msgSend$completion
+ _objc_msgSend$fetchLatestAvailabilityStatusWithCompletionHandler:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$isAvailable
+ _objectdestroy.9Tm
+ _swift_errorRelease
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic $s16SetupAssistantUI36ProvidesGenerativeModelsAvailabilityP
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectC
+ _symbolic _____ 16SetupAssistantUI27BuddyGMAvailabilityProviderC
+ _symbolic ytIeAgHr_
- ___41-[BFFFinishSetupViewController _complete]_block_invoke.70
CStrings:
+ "@\"<BuddyAgeAssuranceUIProvider>\"16@0:8"
+ "BFFFinishSetupIntelligenceController"
+ "GM on device status: shouldShow: %{bool}d, with availability state: %ld"
+ "T@\"<BuddyAgeAssuranceUIProvider>\",?,&,N"
+ "VTUIGMEnrollmentViewController"
+ "VTUIGMEnrollmentViewControllerDelegate"
+ "_TtC16SetupAssistantUI27BuddyGMAvailabilityProvider"
+ "_TtP16SetupAssistantUI36ProvidesGenerativeModelsAvailability_"
+ "ageAssuranceUIProvider"
+ "fetchLatestAvailabilityStatusWithCompletionHandler:"
+ "initWithDelegate:"
+ "isAvailable"
+ "setAgeAssuranceUIProvider:"
+ "siriGMIntroViewControllerContinuePressed:"
+ "siriGMIntroViewControllerNotNowPressed:"
+ "siriGMIntroViewControllerPresented:withEnrollmentType:"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"<BuddyAgeAssuranceUIProvider>\"16"
+ "v24@0:8@?<v@?@\"NSError\">16"

```
