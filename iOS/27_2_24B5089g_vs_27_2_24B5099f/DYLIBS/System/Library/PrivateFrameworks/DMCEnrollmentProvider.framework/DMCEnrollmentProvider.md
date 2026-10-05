## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-113.40.17.0.0
-  __TEXT.__text: 0x4e0d0
-  __TEXT.__objc_methlist: 0x7254
-  __TEXT.__const: 0x504
-  __TEXT.__oslogstring: 0x24cf
-  __TEXT.__cstring: 0x2f98
-  __TEXT.__gcc_except_tab: 0x7b4
+113.40.20.0.0
+  __TEXT.__text: 0x4f668
+  __TEXT.__objc_methlist: 0x73e4
+  __TEXT.__const: 0x514
+  __TEXT.__oslogstring: 0x25ef
+  __TEXT.__cstring: 0x3098
+  __TEXT.__gcc_except_tab: 0x83c
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__swift5_typeref: 0x1b6

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1b10
+  __TEXT.__unwind_info: 0x1b98
   __TEXT.__eh_frame: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1218
-  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__const: 0x1240
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x1a0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49c8
+  __DATA_CONST.__objc_selrefs: 0x4a98
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0xef8
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x30c0
-  __AUTH_CONST.__objc_const: 0x114a0
+  __DATA_CONST.__got: 0xf28
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__objc_const: 0x11fa0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH.__objc_data: 0x1b00
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5f8
-  __DATA.__data: 0x1458
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0x14b8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/DMCTools.framework/DMCTools
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2221
-  Symbols:   4256
-  CStrings:  634
+  Functions: 2258
+  Symbols:   4332
+  CStrings:  647
 
Symbols:
+ -[DMCBYODEnrollmentFlowUIPresenter _appNetworkAccessItemForBundleID:]
+ -[DMCBYODEnrollmentFlowUIPresenter _appNetworkAccessItemsForCapabilities:]
+ -[DMCBYODEnrollmentFlowUIPresenter _openApplicationWithBundleID:]
+ -[DMCBYODEnrollmentFlowUIPresenter appNetworkAccessCompletionHandler]
+ -[DMCBYODEnrollmentFlowUIPresenter appNetworkAccessViewController:didReceiveUserAction:]
+ -[DMCBYODEnrollmentFlowUIPresenter ensureAppNetworkAccessForCapabilities:completionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter setAppNetworkAccessCompletionHandler:]
+ -[DMCEnrollmentAppNetworkAccessItem .cxx_destruct]
+ -[DMCEnrollmentAppNetworkAccessItem actionTitle]
+ -[DMCEnrollmentAppNetworkAccessItem action]
+ -[DMCEnrollmentAppNetworkAccessItem icon]
+ -[DMCEnrollmentAppNetworkAccessItem initWithTitle:icon:actionTitle:action:]
+ -[DMCEnrollmentAppNetworkAccessItem title]
+ -[DMCEnrollmentAppNetworkAccessViewController .cxx_destruct]
+ -[DMCEnrollmentAppNetworkAccessViewController _setupUI]
+ -[DMCEnrollmentAppNetworkAccessViewController delegate]
+ -[DMCEnrollmentAppNetworkAccessViewController dmc_viewControllerHasBeenDismissed]
+ -[DMCEnrollmentAppNetworkAccessViewController initWithDelegate:items:]
+ -[DMCEnrollmentAppNetworkAccessViewController items]
+ -[DMCEnrollmentAppNetworkAccessViewController leftBarButtonTapped:]
+ -[DMCEnrollmentAppNetworkAccessViewController setDelegate:]
+ -[DMCEnrollmentAppNetworkAccessViewController setItems:]
+ -[DMCEnrollmentAppNetworkAccessViewController viewWillAppear:]
+ -[DMCEnrollmentTableViewActionCell _buttonWithTitle:action:]
+ -[DMCEnrollmentTableViewActionCell cellHeight]
+ -[DMCEnrollmentTableViewActionCell cell]
+ -[DMCEnrollmentTableViewActionCell estimatedCellHeight]
+ -[DMCEnrollmentTableViewActionCell initWithTitle:icon:actionTitle:action:]
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table89
+ _DMCAuthKitUIUnavailableError
+ _OBJC_CLASS_$_DMCAppNetworkAccessCheck
+ _OBJC_CLASS_$_DMCEnrollmentAppNetworkAccessItem
+ _OBJC_CLASS_$_DMCEnrollmentAppNetworkAccessViewController
+ _OBJC_CLASS_$_DMCEnrollmentTableViewActionCell
+ _OBJC_CLASS_$_FBSOpenApplicationService
+ _OBJC_CLASS_$_UIButtonConfiguration
+ _OBJC_IVAR_$_DMCBYODEnrollmentFlowUIPresenter._appNetworkAccessCompletionHandler
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessItem._action
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessItem._actionTitle
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessItem._icon
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessItem._title
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessViewController._delegate
+ _OBJC_IVAR_$_DMCEnrollmentAppNetworkAccessViewController._items
+ _OBJC_METACLASS_$_DMCEnrollmentAppNetworkAccessItem
+ _OBJC_METACLASS_$_DMCEnrollmentAppNetworkAccessViewController
+ _OBJC_METACLASS_$_DMCEnrollmentTableViewActionCell
+ __OBJC_$_INSTANCE_METHODS_DMCEnrollmentAppNetworkAccessItem
+ __OBJC_$_INSTANCE_METHODS_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_$_INSTANCE_METHODS_DMCEnrollmentTableViewActionCell
+ __OBJC_$_INSTANCE_VARIABLES_DMCEnrollmentAppNetworkAccessItem
+ __OBJC_$_INSTANCE_VARIABLES_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_$_PROP_LIST_DMCEnrollmentAppNetworkAccessItem
+ __OBJC_$_PROP_LIST_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_$_PROP_LIST_DMCEnrollmentTableViewActionCell
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentAppNetworkAccessViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentAppNetworkAccessViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentAppNetworkAccessViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_CLASS_PROTOCOLS_$_DMCEnrollmentTableViewActionCell
+ __OBJC_CLASS_RO_$_DMCEnrollmentAppNetworkAccessItem
+ __OBJC_CLASS_RO_$_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_CLASS_RO_$_DMCEnrollmentTableViewActionCell
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentAppNetworkAccessViewControllerDelegate
+ __OBJC_METACLASS_RO_$_DMCEnrollmentAppNetworkAccessItem
+ __OBJC_METACLASS_RO_$_DMCEnrollmentAppNetworkAccessViewController
+ __OBJC_METACLASS_RO_$_DMCEnrollmentTableViewActionCell
+ __OBJC_PROTOCOL_$_DMCEnrollmentAppNetworkAccessViewControllerDelegate
+ ___55-[DMCEnrollmentAppNetworkAccessViewController _setupUI]_block_invoke
+ ___55-[DMCEnrollmentAppNetworkAccessViewController _setupUI]_block_invoke_2
+ ___60-[DMCEnrollmentTableViewActionCell _buttonWithTitle:action:]_block_invoke
+ ___65-[DMCBYODEnrollmentFlowUIPresenter _openApplicationWithBundleID:]_block_invoke
+ ___69-[DMCBYODEnrollmentFlowUIPresenter _appNetworkAccessItemForBundleID:]_block_invoke
+ ___92-[DMCBYODEnrollmentFlowUIPresenter ensureAppNetworkAccessForCapabilities:completionHandler:]_block_invoke
+ ___92-[DMCBYODEnrollmentFlowUIPresenter ensureAppNetworkAccessForCapabilities:completionHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8w40l8
+ _kDMCTableViewCellHorizontalMargin
- GCC_except_table80
- _objc_retain_x7
CStrings:
+ "Advising the user about network access for %{public}@. State: %lu"
+ "All apps this enrollment needs already have network access."
+ "AuthKitUI is unavailable, cannot authenticate"
+ "Failed to open %{public}@ with error: %{public}@"
+ "Opening %{public}@ so the user can grant it network access."
+ "UI_APP_NETWORK_ACCESS"
+ "UI_APP_NETWORK_ACCESS_DESCRIPTION"
+ "UI_APP_NETWORK_ACCESS_OPEN"
+ "UI_APP_NETWORK_ACCESS_OPEN_FAILED_MESSAGE"
+ "UI_APP_NETWORK_ACCESS_OPEN_FAILED_TITLE_%@"
+ "UNSUPPORTED_FEATURE"
+ "antenna.radiowaves.left.and.right"
+ "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
```
