## SoftwareUpdateUIKit

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIKit.framework/SoftwareUpdateUIKit`

```diff

-508.40.50.0.0
-  __TEXT.__text: 0x1e4860
-  __TEXT.__auth_stubs: 0x3410
-  __TEXT.__objc_methlist: 0xa70
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x6e28
-  __TEXT.__oslogstring: 0x2e11
-  __TEXT.__const: 0xb744
-  __TEXT.__swift5_typeref: 0xb2d8
+508.40.54.0.0
+  __TEXT.__text: 0x1e5d48
+  __TEXT.__auth_stubs: 0x3420
+  __TEXT.__objc_methlist: 0xa88
+  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__cstring: 0x6f58
+  __TEXT.__oslogstring: 0x30c1
+  __TEXT.__const: 0xb7e4
+  __TEXT.__swift5_typeref: 0xb2e0
   __TEXT.__swift5_reflstr: 0x1b4a
   __TEXT.__swift5_assocty: 0xa60
-  __TEXT.__constg_swiftt: 0x34c8
+  __TEXT.__constg_swiftt: 0x34e8
   __TEXT.__swift5_fieldmd: 0x1890
-  __TEXT.__swift5_builtin: 0x21c
+  __TEXT.__swift5_builtin: 0x230
   __TEXT.__swift5_capture: 0x5f54
   __TEXT.__swift5_proto: 0x318
-  __TEXT.__swift5_types: 0x3a8
+  __TEXT.__swift5_types: 0x3ac
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x184
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5548
+  __TEXT.__unwind_info: 0x5558
   __TEXT.__eh_frame: 0x20b8
   __TEXT.__objc_classname: 0x18a
-  __TEXT.__objc_methname: 0x2e38
+  __TEXT.__objc_methname: 0x2f24
   __TEXT.__objc_methtype: 0x15c0
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0xc00
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0xc18
   __DATA_CONST.__const: 0x478
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xc80
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1a18
-  __AUTH_CONST.__const: 0x113a0
+  __AUTH_CONST.__auth_got: 0x1a20
+  __AUTH_CONST.__const: 0x113c0
   __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0xc780
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x5d8
   __AUTH.__data: 0x14a8
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x3de0
-  __DATA.__bss: 0x65f8
+  __DATA.__data: 0x3df0
+  __DATA.__bss: 0x6608
   __DATA.__common: 0x1c8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 60FACB74-9E99-3474-9D77-08EC8EC97617
-  Functions: 9165
-  Symbols:   2566
-  CStrings:  1399
+  UUID: 3206A167-B8C2-3FAE-9D83-9A82BF9E541D
+  Functions: 9176
+  Symbols:   2587
+  CStrings:  1422
 
Symbols:
+ -[SUUITermsConditionsInterop currentPresentedSceneViewController]
+ -[SUUITermsConditionsInterop getTopViewControllerFrom:]
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_CLASS_$_UITabBarController
+ _OBJC_CLASS_$_UIWindowScene
+ ___69-[SUUITermsConditionsInterop completePresentationWithResponse:error:]_block_invoke.189
+ _block_copy_helper.1668
+ _block_descriptor.1670
+ _block_destroy_helper.1669
+ _keypath_get_selector_currentUpdateOperationType
+ _objc_msgSend$activationState
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$currentPresentedSceneViewController
+ _objc_msgSend$getTopViewControllerFrom:
+ _objc_msgSend$isKeyWindow
+ _objc_msgSend$rootViewController
+ _objc_msgSend$selectedViewController
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$visibleViewController
+ _objc_msgSend$windows
+ _objc_opt_isKindOfClass
+ _symbolic _____ So33SUUIUpdateContinuousOperationTypeV
- ___69-[SUUITermsConditionsInterop completePresentationWithResponse:error:]_block_invoke.188
- _block_copy_helper.1661
- _block_descriptor.1663
- _block_destroy_helper.1662
CStrings:
+ "%s: Apple Account Terms and Conditions - Presenting the T&C dialog."
+ "%s: Apple Account Terms and Conditions - RemoteUI reported \"Agree\"."
+ "%s: Apple Account Terms and Conditions - RemoteUI reported \"Disagree\"."
+ "%s: Apple Account Terms and Conditions - _hostViewController is nil.Falling back to UIApplication's top view controller."
+ "%s: Apple Account Terms and Conditions - couldn't find the active keyWindow."
+ "%s: Apple Account Terms and Conditions - couldn't find the active windowScene."
+ "%s: Apple Account Terms and Conditions - dismissing the RemoteUI controller."
+ "%s: Apple Account Terms and Conditions - there's no RemoteUI controller available. Skipping on the dismissal request."
+ "-[SUUITermsConditionsInterop completePresentationWithResponse:error:]_block_invoke"
+ "-[SUUITermsConditionsInterop currentPresentedSceneViewController]"
+ "-[SUUITermsConditionsInterop handleAgreeResponseFromRemoteUIObjectModel:]"
+ "-[SUUITermsConditionsInterop handleDisagreeResponseFromRemoteUIObjectModel:]"
+ "activationState"
+ "connectedScenes"
+ "currentPresentedSceneViewController"
+ "currentUpdateOperationType"
+ "getTopViewControllerFrom:"
+ "isKeyWindow"
+ "rootViewController"
+ "selectedViewController"
+ "setCurrentUpdateOperationType:"
+ "visibleViewController"
+ "windows"

```
