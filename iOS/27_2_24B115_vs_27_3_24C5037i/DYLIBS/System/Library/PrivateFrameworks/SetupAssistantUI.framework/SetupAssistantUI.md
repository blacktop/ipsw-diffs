## SetupAssistantUI

> `/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI`

```diff

-5411.2.5.0.0
-  __TEXT.__text: 0x22970
-  __TEXT.__objc_methlist: 0x36c8
+5412.2.3.101.0
+  __TEXT.__text: 0x22df8
+  __TEXT.__objc_methlist: 0x3728
   __TEXT.__const: 0x334
-  __TEXT.__cstring: 0x8f7
+  __TEXT.__cstring: 0x907
   __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__oslogstring: 0x1248
+  __TEXT.__oslogstring: 0x12c8
   __TEXT.__dlopen_cstrs: 0x37f
   __TEXT.__constg_swiftt: 0xc8
   __TEXT.__swift5_typeref: 0x138

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xce0
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__eh_frame: 0x168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x768
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2448
+  __DATA_CONST.__objc_selrefs: 0x24b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x118
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x498
   __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__cfstring: 0x800
-  __AUTH_CONST.__objc_const: 0x59d8
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0x5bc8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x640
-  __AUTH.__objc_data: 0xea8
+  __AUTH.__objc_data: 0xf48
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0xd68
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 931
-  Symbols:   1981
-  CStrings:  211
+  Functions: 937
+  Symbols:   2003
+  CStrings:  213
 
Symbols:
+ +[BFFPasscodeNextButton configureNextButtonForNavigationItem:visible:title:target:action:animated:]
+ -[BFFFinishSetupAdaptiveModalPresentationControllerDelegate adaptivePresentationStyleForPresentationController:traitCollection:]
+ -[BFFFinishSetupModalNavigationController presentation]
+ -[BFFFinishSetupModalNavigationController setPresentation:]
+ -[BFFFinishSetupModalNavigationController viewDidLayoutSubviews]
+ -[BFFFinishSetupViewController _presentationMode]
+ -[BFFFinishSetupViewController adaptiveModalPresentationControllerDelegate]
+ -[BFFFinishSetupViewController setAdaptiveModalPresentationControllerDelegate:]
+ GCC_except_table30
+ _OBJC_CLASS_$_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ _OBJC_CLASS_$_BFFPasscodeNextButton
+ _OBJC_CLASS_$_UIBarButtonItemGroup
+ _OBJC_IVAR_$_BFFFinishSetupModalNavigationController._presentation
+ _OBJC_IVAR_$_BFFFinishSetupViewController._adaptiveModalPresentationControllerDelegate
+ _OBJC_IVAR_$_BFFNavBarSpinnerManager._savedPinnedTrailingGroups
+ _OBJC_IVAR_$_BFFPasscodeViewController._nextButton
+ _OBJC_METACLASS_$_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ _OBJC_METACLASS_$_BFFPasscodeNextButton
+ __OBJC_$_CLASS_METHODS_BFFPasscodeNextButton
+ __OBJC_$_INSTANCE_METHODS_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ __OBJC_$_PROP_LIST_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ __OBJC_CLASS_RO_$_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ __OBJC_CLASS_RO_$_BFFPasscodeNextButton
+ __OBJC_METACLASS_RO_$_BFFFinishSetupAdaptiveModalPresentationControllerDelegate
+ __OBJC_METACLASS_RO_$_BFFPasscodeNextButton
- -[BFFFinishSetupModalNavigationController isPad]
- -[BFFFinishSetupModalNavigationController setIsPad:]
- GCC_except_table29
- _OBJC_IVAR_$_BFFFinishSetupModalNavigationController._isPad
CStrings:
+ "Finish setup adaptive presentation style for horizontal size class %@ vertical size class %@ => %@"
+ "chevron.forward"
+ "did create _navigationController: %@ presentation: %lu"
- "did create _navigationController: %@"
```
