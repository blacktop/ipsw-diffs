## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.4.16.0.0
-  __TEXT.__text: 0x133fb4
+605.4.17.0.0
+  __TEXT.__text: 0x13418c
   __TEXT.__auth_stubs: 0x2ed0
-  __TEXT.__objc_methlist: 0xc4ac
+  __TEXT.__objc_methlist: 0xc4bc
   __TEXT.__const: 0x3de4
   __TEXT.__cstring: 0xd145
-  __TEXT.__oslogstring: 0x5d03
+  __TEXT.__oslogstring: 0x5d93
   __TEXT.__gcc_except_tab: 0x126c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0x44ea

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x88
-  __TEXT.__unwind_info: 0x4028
+  __TEXT.__unwind_info: 0x4030
   __TEXT.__eh_frame: 0x20c0
   __TEXT.__objc_classname: 0x2854
-  __TEXT.__objc_methname: 0x238bd
+  __TEXT.__objc_methname: 0x2391d
   __TEXT.__objc_methtype: 0x42c3
-  __TEXT.__objc_stubs: 0x164c0
+  __TEXT.__objc_stubs: 0x164e0
   __DATA_CONST.__got: 0x1420
   __DATA_CONST.__const: 0x2660
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6da8
+  __DATA_CONST.__objc_selrefs: 0x6db0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x1778
-  __AUTH_CONST.__const: 0x3240
+  __AUTH_CONST.__const: 0x3260
   __AUTH_CONST.__cfstring: 0xb060
   __AUTH_CONST.__objc_const: 0x25de0
   __AUTH_CONST.__objc_intobj: 0x8d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ACB26EE7-5D52-306D-8D78-4773AACAE26F
-  Functions: 6241
-  Symbols:   16727
-  CStrings:  9295
+  UUID: 882953E8-C543-3D57-B2DF-4F34831CF60B
+  Functions: 6244
+  Symbols:   16735
+  CStrings:  9298
 
Symbols:
+ -[STContentPrivacyViewModelCoordinator _repairTopLevelContentPrivacyEnablementToMatchRegulatoryRequirementsWithCompletionHandler:]
+ GCC_except_table110
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1015
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke.326
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke.326.cold.1
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.823
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.823.cold.1
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.824
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.832
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.831
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.843
+ ___block_literal_global.1018
+ ___block_literal_global.791
+ ___block_literal_global.848
+ _objc_msgSend$_repairTopLevelContentPrivacyEnablementToMatchRegulatoryRequirementsWithCompletionHandler:
- GCC_except_table109
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1011
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820.cold.1
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.821
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.829
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.828
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.840
- ___block_literal_global.1014
- ___block_literal_global.845
Functions:
~ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke : 308 -> 332
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke.326
+ -[STContentPrivacyViewModelCoordinator _repairTopLevelContentPrivacyEnablementToMatchRegulatoryRequirementsWithCompletionHandler:]
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke.326.cold.1
CStrings:
+ "Failed to repair Content & Privacy state after load: %{public}@"
+ "Repairing Content & Privacy state: enabling restrictions due to regulatory policy requirement"
+ "_repairTopLevelContentPrivacyEnablementToMatchRegulatoryRequirementsWithCompletionHandler:"

```
