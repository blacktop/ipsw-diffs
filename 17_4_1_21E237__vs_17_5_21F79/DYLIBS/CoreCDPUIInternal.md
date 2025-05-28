## CoreCDPUIInternal

> `/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal`

```diff

-359.13.0.0.0
-  __TEXT.__text: 0x5180
+359.21.0.0.0
+  __TEXT.__text: 0x5598
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x3c8
+  __TEXT.__objc_methlist: 0x41c
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x763
+  __TEXT.__cstring: 0x7fd
   __TEXT.__oslogstring: 0x1af
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__objc_classname: 0x10a
-  __TEXT.__objc_methname: 0x14f0
-  __TEXT.__objc_methtype: 0x322
-  __TEXT.__objc_stubs: 0x1260
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_classname: 0x157
+  __TEXT.__objc_methname: 0x171a
+  __TEXT.__objc_methtype: 0x381
+  __TEXT.__objc_stubs: 0x1300
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbd0
-  __DATA_CONST.__objc_selrefs: 0x5e8
-  __DATA_CONST.__objc_classrefs: 0x120
+  __DATA_CONST.__objc_const: 0xce0
+  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_classrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_const: 0x168
-  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__cfstring: 0xb40
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x188
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x240
+  __DATA.__data: 0x300
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 116
-  Symbols:   603
-  CStrings:  390
+  Functions: 124
+  Symbols:   638
+  CStrings:  415
 
Symbols:
+ -[SettingsController beginEnablementFlow:]
+ -[SettingsController presentAccountRecoveryFlow]
+ -[SettingsController setDelegate:]
+ -[SettingsController simulateADPUpsell:]
+ -[SettingsController upsellViewModelDidRequestBeginEnablementFlow]
+ -[SettingsController upsellViewModelDidRequestCFUDismissal]
+ -[SettingsController upsellViewModelDidRequestFlowCancellation]
+ _OBJC_CLASS_$_AKNetworkObserver
+ _OBJC_CLASS_$_AKURLBag
+ _OBJC_CLASS_$_CDPUIWalrusSwiftUIFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPUIADPUpsellViewModelDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPUIAdvancedDataProtectionViewModelDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CDPUIADPUpsellViewModelDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CDPUIAdvancedDataProtectionViewModelDelegate
+ __OBJC_$_PROTOCOL_REFS_CDPUIADPUpsellViewModelDelegate
+ __OBJC_$_PROTOCOL_REFS_CDPUIAdvancedDataProtectionViewModelDelegate
+ __OBJC_LABEL_PROTOCOL_$_CDPUIADPUpsellViewModelDelegate
+ __OBJC_LABEL_PROTOCOL_$_CDPUIAdvancedDataProtectionViewModelDelegate
+ __OBJC_PROTOCOL_$_CDPUIADPUpsellViewModelDelegate
+ __OBJC_PROTOCOL_$_CDPUIAdvancedDataProtectionViewModelDelegate
+ ___32-[SettingsController enableCDP:]_block_invoke.169
+ ___32-[SettingsController enableCDP:]_block_invoke.182
+ ___32-[SettingsController enableCDP:]_block_invoke.193
+ ___40-[SettingsController simulateADPUpsell:]_block_invoke
+ ___block_descriptor_40_e8_32s_e61_v24?0"UIViewController"8"<CDPUIADPUpsellErrorPresenter>"16ls32l8
+ ___block_literal_global.322
+ ___block_literal_global.339
+ ___block_literal_global.341
+ __unnamed_array_storage.293
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$makeSwiftUIUpsellViewWithCDPContext:urlBag:networkObserver:viewModelDelegate:completion:
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$sharedBag
+ _objc_msgSend$sharedNetworkObserver
- ___32-[SettingsController enableCDP:]_block_invoke.164
- ___32-[SettingsController enableCDP:]_block_invoke.177
- ___32-[SettingsController enableCDP:]_block_invoke.188
- ___block_literal_global.317
- ___block_literal_global.334
- ___block_literal_global.336
- __unnamed_array_storage.288
CStrings:
+ "Account Recovery Flow"
+ "Began Enablement Flow"
+ "CDPUIADPUpsellViewModelDelegate"
+ "CDPUIAdvancedDataProtectionViewModelDelegate"
+ "Requested CFU dismissal"
+ "Simulate ADP Upsell CFU"
+ "beginEnablementFlow:"
+ "dismissViewControllerAnimated:completion:"
+ "makeSwiftUIUpsellViewWithCDPContext:urlBag:networkObserver:viewModelDelegate:completion:"
+ "presentAccountRecoveryFlow"
+ "presentedViewController"
+ "setDelegate:"
+ "sharedBag"
+ "sharedNetworkObserver"
+ "simulateADPUpsell:"
+ "upsellViewModelDidRequestBeginEnablementFlow"
+ "upsellViewModelDidRequestBeginEnablementFlowWithContext:"
+ "upsellViewModelDidRequestCFUDismissal"
+ "upsellViewModelDidRequestCFUDismissalWithContext:"
+ "upsellViewModelDidRequestFlowCancellation"
+ "upsellViewModelDidRequestFlowCancellationWithContext:"
+ "v24@0:8@\"<CDPUIAdvancedDataProtectionStateManager>\"16"
+ "v24@0:8@\"CDPContext\"16"
+ "v24@0:8@\"NSURL\"16"
+ "v24@?0@\"UIViewController\"8@\"<CDPUIADPUpsellErrorPresenter>\"16"

```
