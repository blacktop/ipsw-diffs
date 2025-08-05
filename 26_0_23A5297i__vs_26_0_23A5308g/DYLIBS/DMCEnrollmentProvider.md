## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x4c900
-  __TEXT.__auth_stubs: 0xdc0
+50.0.0.0.0
+  __TEXT.__text: 0x4df88
+  __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x70d0
-  __TEXT.__const: 0x2c4
-  __TEXT.__oslogstring: 0x1ea1
-  __TEXT.__cstring: 0x2c35
+  __TEXT.__const: 0x4b4
+  __TEXT.__oslogstring: 0x1f0f
+  __TEXT.__cstring: 0x2cb5
   __TEXT.__gcc_except_tab: 0x7a0
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8
-  __TEXT.__swift5_typeref: 0x120
+  __TEXT.__swift5_typeref: 0x1b6
+  __TEXT.__swift5_reflstr: 0x47
+  __TEXT.__swift5_assocty: 0x38
+  __TEXT.__constg_swiftt: 0x88
+  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__constg_swiftt: 0x50
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__unwind_info: 0x1588
   __TEXT.__eh_frame: 0x480
   __TEXT.__objc_classname: 0x117c
-  __TEXT.__objc_methname: 0x1436d
+  __TEXT.__objc_methname: 0x14368
   __TEXT.__objc_methtype: 0x498c
-  __TEXT.__objc_stubs: 0xd1c0
-  __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0x1028
+  __TEXT.__objc_stubs: 0xd1a0
+  __DATA_CONST.__got: 0xeb0
+  __DATA_CONST.__const: 0x1038
   __DATA_CONST.__objc_classlist: 0x310
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x6f0
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x2ec0
-  __AUTH_CONST.__objc_const: 0x113b8
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x113f8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x13b8
-  __DATA.__bss: 0x60
+  __DATA.__data: 0x13f8
+  __DATA.__bss: 0x260
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit

   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCApps.framework/DMCApps
   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
+  - /System/Library/PrivateFrameworks/DMCTools.framework/DMCTools
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI
+  - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DBA74A5E-9A4B-3D5C-91A6-E51EAD10C449
-  Functions: 2123
-  Symbols:   8147
-  CStrings:  4609
+  UUID: 261A0E21-4A8E-3043-BA19-EEEAF78D44AC
+  Functions: 2177
+  Symbols:   8184
+  CStrings:  4618
 
Symbols:
+ -[DMCEnrollmentUIBarButtonItem buttonType]
+ -[UIBarButtonItem(DMC) DMCIsSpinner]
+ GCC_except_table32
+ _DMCNavigationItemKey
+ _DMCSendNavUIUpdatedNotification
+ _NSClassFromString
+ _OBJC_CLASS_$_PSBarButtonSpinnerView
+ _OBJC_IVAR_$_DMCEnrollmentUIBarButtonItem._buttonType
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIBarButtonItem_$_DMC
+ __OBJC_$_CATEGORY_UIBarButtonItem_$_DMC
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy16_8
+ ___swift_project_boxed_opaque_existential_1
+ __swift_stdlib_bridgeErrorToNSError
+ _associated conformance 21DMCEnrollmentProvider30DMCGenericViewControllerRecipeVSHAASQ
+ _associated conformance 21DMCEnrollmentProvider37DMCGenericViewControllerRepresentableV7SwiftUI06UIVieweF0AaD0D0
+ _associated conformance 21DMCEnrollmentProvider37DMCGenericViewControllerRepresentableV7SwiftUI0D0AA4BodyAdEP_AdE
+ _kDMCNavUIUpdatedNotification
+ _kMDMSettingsURLMDMMigrationComponent
+ _kMDMSettingsURLManagedAccountComponent
+ _kMDMSettingsURLProfilesUI
+ _kMDMSettingsURLResourceID
+ _objc_msgSend$buttonType
+ _swift_allocBox
+ _swift_arrayDestroy
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_errorRetain
+ _symbolic $s7SwiftUI29UIViewControllerRepresentableP
+ _symbolic $s7SwiftUI4ViewP
+ _symbolic SO
+ _symbolic So16UIViewControllerC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 21DMCEnrollmentProvider30DMCGenericViewControllerRecipeV
+ _symbolic _____ 21DMCEnrollmentProvider37DMCGenericViewControllerRepresentableV
+ _symbolic _____ s5NeverO
+ _symbolic yt
+ _type_layout_string 21DMCEnrollmentProvider30DMCGenericViewControllerRecipeV
+ _type_layout_string 21DMCEnrollmentProvider37DMCGenericViewControllerRepresentableV
- -[DMCEnrollmentUIBarButtonItem type]
- -[DMCInstallProfileQuestionViewController _hideProgressIndicator]
- -[DMCInstallProfileQuestionViewController _setRightButtonEnabled:]
- GCC_except_table34
- _OBJC_IVAR_$_DMCEnrollmentUIBarButtonItem._type
- _kMCSettingsURLManagedAppleID
- _kMCSettingsURLProfilesOverview
- _objc_msgSend$_hideProgressIndicator
- _objc_msgSend$_setRightButtonEnabled:
CStrings:
+ "%@?%@=%@"
+ "DMCIsSpinner"
+ "MCUITableViewController"
+ "MCUIViewController"
+ "MDMMigrationGroup"
+ "NavigationItem"
+ "TQ,R,N,V_buttonType"
+ "UIViewController+DMCNavigationController failed navigation proxy pop to vc '%@' with error: %@"
+ "_buttonType"
+ "buttonType"
+ "kDMCNavUIUpdatedNotification"
- "%@&username=%@"
- "MDMMigration"
- "TQ,R,N,V_type"
- "_hideProgressIndicator"
- "_setRightButtonEnabled:"

```
