## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

 520.480.0.0.0
-  __TEXT.__text: 0x19181c
+  __TEXT.__text: 0x192020
   __TEXT.__auth_stubs: 0x3070
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xa0dc
+  __TEXT.__objc_methlist: 0xa0f4
   __TEXT.__const: 0x6b34
-  __TEXT.__gcc_except_tab: 0x1534
-  __TEXT.__cstring: 0x79be
-  __TEXT.__oslogstring: 0xbfac
+  __TEXT.__gcc_except_tab: 0x1564
+  __TEXT.__cstring: 0x79ee
+  __TEXT.__oslogstring: 0xc12c
   __TEXT.__dlopen_cstrs: 0x435
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xb184

   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4090
+  __TEXT.__unwind_info: 0x40a8
   __TEXT.__eh_frame: 0x808
   __TEXT.__objc_classname: 0x1fca
-  __TEXT.__objc_methname: 0x19778
-  __TEXT.__objc_methtype: 0x4a9d
-  __TEXT.__objc_stubs: 0x12a60
-  __DATA_CONST.__got: 0x18d0
-  __DATA_CONST.__const: 0x2c20
+  __TEXT.__objc_methname: 0x19848
+  __TEXT.__objc_methtype: 0x4ab1
+  __TEXT.__objc_stubs: 0x12ae0
+  __DATA_CONST.__got: 0x18f0
+  __DATA_CONST.__const: 0x2c70
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60d8
+  __DATA_CONST.__objc_selrefs: 0x60f0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0xc8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8177
-  Symbols:   15752
-  CStrings:  6734
+  Functions: 8189
+  Symbols:   15791
+  CStrings:  6746
 
Symbols:
+ -[AAUITheftAndLossStore createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:]
+ GCC_except_table33
+ _FindMyTheftAndLossDisclaimerUseCaseTurnOffFindMy
+ _OBJC_CLASS_$_FindMyTheftAndLossDisclaimerContext
+ _OBJC_CLASS_$_FindMyTheftAndLossDisclaimerViewController
+ __OBJC_$_INSTANCE_METHODS_AAUITheftAndLossStore
+ ___114-[AAUITheftAndLossStore createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:]_block_invoke
+ ___114-[AAUITheftAndLossStore createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:]_block_invoke.cold.1
+ ___114-[AAUITheftAndLossStore createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:]_block_invoke.cold.2
+ ___114-[AAUITheftAndLossStore createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:]_block_invoke.cold.3
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_4
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_5
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_6
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_6.cold.1
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_6.cold.2
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_6.cold.3
+ ___84+[AAUIDeviceLocatorConfirmationUtilities showDisableAlertForContext:withCompletion:]_block_invoke_6.cold.4
+ ___block_descriptor_40_e8_32bs_e38_v24?0"UIViewController"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e38_v24?0"UIViewController"8"NSError"16ls48l8r56l8s32l8s40l8
+ _objc_msgSend$_getDeviceType
+ _objc_msgSend$createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:
+ _objc_msgSend$disclaimerViewControllerForContext:confirmActionHandler:cancelActionHandler:completion:
+ _objc_msgSend$initWithUseCase:serialNumber:
CStrings:
+ "Failed to get tnl view controller with error: %@"
+ "Presenting view controller is a nav controller. Pushing TnL view controller with it."
+ "Presenting view controller is nil. Continue disabling FindMy."
+ "Setting TnL view controller with navigation controller and presenting."
+ "Successfully received TnL viewController."
+ "TnL view controller is nil."
+ "TnL view controller is nil. Continue disabling FindMy."
+ "createTnLDisclaimerViewControllerWithConfirmActionHandler:cancelActionHandler:completion:"
+ "disclaimerViewControllerForContext:confirmActionHandler:cancelActionHandler:completion:"
+ "initWithUseCase:serialNumber:"
+ "v24@?0@\"UIViewController\"8@\"NSError\"16"
+ "v40@0:8@?16@?24@?32"

```
