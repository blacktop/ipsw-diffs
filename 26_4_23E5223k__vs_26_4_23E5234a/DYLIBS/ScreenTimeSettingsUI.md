## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.4.17.0.0
-  __TEXT.__text: 0x13418c
+605.4.18.1.0
+  __TEXT.__text: 0x13401c
   __TEXT.__auth_stubs: 0x2ed0
-  __TEXT.__objc_methlist: 0xc4bc
-  __TEXT.__const: 0x3de4
-  __TEXT.__cstring: 0xd145
-  __TEXT.__oslogstring: 0x5d93
+  __TEXT.__objc_methlist: 0xc49c
+  __TEXT.__const: 0x3e04
+  __TEXT.__cstring: 0xd165
+  __TEXT.__oslogstring: 0x5e43
   __TEXT.__gcc_except_tab: 0x126c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0x44ea

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x88
-  __TEXT.__unwind_info: 0x4030
+  __TEXT.__unwind_info: 0x4010
   __TEXT.__eh_frame: 0x20c0
   __TEXT.__objc_classname: 0x2854
-  __TEXT.__objc_methname: 0x2391d
+  __TEXT.__objc_methname: 0x2396d
   __TEXT.__objc_methtype: 0x42c3
   __TEXT.__objc_stubs: 0x164e0
   __DATA_CONST.__got: 0x1420
-  __DATA_CONST.__const: 0x2660
+  __DATA_CONST.__const: 0x2688
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210

   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x1778
   __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0xb060
+  __AUTH_CONST.__cfstring: 0xb0c0
   __AUTH_CONST.__objc_const: 0x25de0
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 882953E8-C543-3D57-B2DF-4F34831CF60B
-  Functions: 6244
-  Symbols:   16735
-  CStrings:  9298
+  UUID: 283C71D2-0234-31A7-884C-6C158046EB24
+  Functions: 6236
+  Symbols:   16718
+  CStrings:  9306
 
Symbols:
+ -[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:authorizationRecord:]
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table35
+ GCC_except_table39
+ ___113-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:authorizationRecord:]_block_invoke
+ ___113-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:authorizationRecord:]_block_invoke.45
+ ___113-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:authorizationRecord:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48s56s_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_performFamilyControlsChange:forSpecifier:authorizationRecord:
+ _objc_msgSend$silentlyResetAuthorizationForRecordIdentifier:completionHandler:
- -[STCommunicationSafetyListController _createAdditionalFooterIfNeeded]
- -[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]
- -[STWebFilterDetailController _createAdditionalFooterIfNeeded]
- GCC_except_table20
- GCC_except_table24
- GCC_except_table30
- GCC_except_table36
- GCC_except_table40
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.40
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.40.cold.1
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.42
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.42.cold.1
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.cold.1
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2.41
- ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2.43
- _objc_msgSend$_createAdditionalFooterIfNeeded
- _objc_msgSend$_performFamilyControlsChange:forSpecifier:
CStrings:
+ "%@\n\n%@"
+ "FOAuthorizationCenter failed with error: %{public}@"
+ "FOAuthorizationCenter finished successfully"
+ "Not performing family controls change since application is already %@"
+ "Requesting authorization for FOAuthorizationRecord:%{private}@"
+ "Reseting authorization for FOAuthorizationRecord:%{private}@ silent revocation:%@"
+ "_performFamilyControlsChange:forSpecifier:authorizationRecord:"
+ "approved"
+ "not approved"
+ "silentlyResetAuthorizationForRecordIdentifier:completionHandler:"
- "Authorization's reset failed: %{public}@"
- "Request for authorization failed: %{public}@"
- "Request for data access authorization failed: %{public}@"
- "_createAdditionalFooterIfNeeded"
- "_performFamilyControlsChange:forSpecifier:"

```
