## ScreenTimeUI

> `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI`

```diff

-605.1.8.0.0
-  __TEXT.__text: 0x27404
+605.1.15.100.0
+  __TEXT.__text: 0x2804c
   __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0x16e0
+  __TEXT.__objc_methlist: 0x1700
   __TEXT.__const: 0x774
-  __TEXT.__cstring: 0x148c
+  __TEXT.__cstring: 0x14bc
   __TEXT.__gcc_except_tab: 0x460
-  __TEXT.__oslogstring: 0x28ed
+  __TEXT.__oslogstring: 0x29fd
   __TEXT.__swift5_typeref: 0x1650
   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift5_reflstr: 0x111

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0xa00
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0x1d2
-  __TEXT.__objc_methname: 0x5e5c
+  __TEXT.__objc_methname: 0x5f9c
   __TEXT.__objc_methtype: 0x888
-  __TEXT.__objc_stubs: 0x4b40
+  __TEXT.__objc_stubs: 0x4c00
   __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0xb58
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c8
+  __DATA_CONST.__objc_selrefs: 0x16f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x5e8
+  __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0xf40
   __AUTH_CONST.__objc_const: 0x22f8
   __AUTH.__objc_data: 0x750

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8C6FA79-3E45-39B2-8C1A-E5BE1DA35966
-  Functions: 924
-  Symbols:   2890
-  CStrings:  1553
+  UUID: 84ECDCE7-4320-36D1-BEAA-E9B689219562
+  Functions: 938
+  Symbols:   2935
+  CStrings:  1565
 
Symbols:
+ +[STBlockingViewController openAppWithBundleIdentifier:]
+ +[STBlockingViewController openParentAppHandler]
+ -[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]
+ -[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:].cold.1
+ GCC_except_table41
+ ___48+[STBlockingViewController openParentAppHandler]_block_invoke
+ ___49-[STBlockingViewController _customButtonPressed:]_block_invoke.256
+ ___49-[STBlockingViewController _customButtonPressed:]_block_invoke_2.257
+ ___49-[STBlockingViewController _customButtonPressed:]_block_invoke_2.257.cold.1
+ ___56+[STBlockingViewController openAppWithBundleIdentifier:]_block_invoke
+ ___56+[STBlockingViewController openAppWithBundleIdentifier:]_block_invoke.cold.1
+ ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.258
+ ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.259
+ ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.259.cold.1
+ ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.260
+ ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.261
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke.82
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke.82.cold.1
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke.83
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke.83.cold.1
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke.cold.1
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke_2
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke_2.84
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke_2.84.cold.1
+ ___78-[STBlockingViewController fetchAppResponsibleForShieldWithCompletionHandler:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e32_v24?0"CTCategory"8"NSError"16ls32l8s40l8
+ ___block_literal_global.236
+ _objc_msgSend$appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:
+ _objc_msgSend$appResponsibleForShieldingCategoryIdentifier:completionHandler:
+ _objc_msgSend$appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:
+ _objc_msgSend$fetchAppResponsibleForShieldWithCompletionHandler:
+ _objc_msgSend$openAppWithBundleIdentifier:
+ _objc_msgSend$openParentAppHandler
- GCC_except_table31
- GCC_except_table32
- _OUTLINED_FUNCTION_12
- ___49-[STBlockingViewController _customButtonPressed:]_block_invoke.253
- ___49-[STBlockingViewController _customButtonPressed:]_block_invoke_2.254
- ___49-[STBlockingViewController _customButtonPressed:]_block_invoke_2.254.cold.1
- ___51+[STBlockingViewController closeApplicationHandler]_block_invoke_2
- ___51+[STBlockingViewController closeApplicationHandler]_block_invoke_2.cold.1
- ___72-[STBlockingViewController _handleCustomButtonResponse:forAction:error:]_block_invoke.255
- ___block_literal_global.212
- ___block_literal_global.231
- ___block_literal_global.77
CStrings:
+ "Attempting to retrieve reponsible app with no bundle identifier, category identifier, or web domain."
+ "Failed to fetch responsible app for %{public}@: %{public}@."
+ "Failed to get parental controls app, closing current application instead."
+ "Failed to open %@: %@"
+ "Opening parental controls application %{public}@"
+ "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:"
+ "appResponsibleForShieldingCategoryIdentifier:completionHandler:"
+ "appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:"
+ "fetchAppResponsibleForShieldWithCompletionHandler:"
+ "openAppWithBundleIdentifier:"
+ "openParentAppHandler"
+ "v16@?0@\"NSString\"8"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
- "Failed to return to Home Screen: %@"

```
