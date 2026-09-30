## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-645.1.100.0.0
-  __TEXT.__text: 0xf2d20
-  __TEXT.__objc_methlist: 0xa0f0
-  __TEXT.__const: 0x3288
-  __TEXT.__cstring: 0xa45c
-  __TEXT.__oslogstring: 0xba7a
+649.0.0.0.0
+  __TEXT.__text: 0xf3a7c
+  __TEXT.__objc_methlist: 0xa140
+  __TEXT.__const: 0x32a8
+  __TEXT.__cstring: 0xa52c
+  __TEXT.__oslogstring: 0xbafa
   __TEXT.__gcc_except_tab: 0x1b30
-  __TEXT.__swift5_typeref: 0x144e
+  __TEXT.__swift5_typeref: 0x14cc
   __TEXT.__constg_swiftt: 0xd0c
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x79e
-  __TEXT.__swift5_fieldmd: 0x9a8
+  __TEXT.__swift5_reflstr: 0x7be
+  __TEXT.__swift5_fieldmd: 0x9b4
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x210
   __TEXT.__swift5_types: 0xe8
-  __TEXT.__swift5_capture: 0xa58
+  __TEXT.__swift5_capture: 0xa84
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift_as_entry: 0x148
-  __TEXT.__swift_as_ret: 0x168
-  __TEXT.__swift_as_cont: 0x210
+  __TEXT.__swift_as_entry: 0x158
+  __TEXT.__swift_as_ret: 0x188
+  __TEXT.__swift_as_cont: 0x220
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3d78
-  __TEXT.__eh_frame: 0x3b40
+  __TEXT.__unwind_info: 0x3df8
+  __TEXT.__eh_frame: 0x3d90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c78
+  __DATA_CONST.__const: 0x1d48
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53a8
+  __DATA_CONST.__objc_selrefs: 0x53d8
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0xe98
-  __AUTH_CONST.__const: 0x32d8
-  __AUTH_CONST.__cfstring: 0x97c0
-  __AUTH_CONST.__objc_const: 0x13190
+  __DATA_CONST.__got: 0xe90
+  __AUTH_CONST.__const: 0x3308
+  __AUTH_CONST.__cfstring: 0x97e0
+  __AUTH_CONST.__objc_const: 0x13178
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1180
-  __AUTH.__objc_data: 0x31a0
-  __AUTH.__data: 0x4f8
+  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH.__objc_data: 0x31a8
+  __AUTH.__data: 0x500
   __DATA.__objc_ivar: 0x7bc
-  __DATA.__data: 0x2190
+  __DATA.__data: 0x21b0
   __DATA.__bss: 0x3f80
   __DATA.__common: 0xd0
   __DATA_DIRTY.__objc_data: 0x1f18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5821
-  Symbols:   8632
-  CStrings:  2231
+  Functions: 5840
+  Symbols:   8650
+  CStrings:  2237
 
Symbols:
+ -[STCommunicationClient _authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]
+ -[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]
+ -[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:]
+ -[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]
+ -[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]
+ -[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table209
+ _STRemoteAlertConfigurationContextKeyUserInterfaceStyle
+ ___100-[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]_block_invoke
+ ___100-[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]_block_invoke_2
+ ___116-[STCommunicationClient _authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]_block_invoke
+ ___138-[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:]_block_invoke
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_2
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_3
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_4
+ ___91-[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]_block_invoke
+ ___91-[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSUUID"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e74_v24?0"<STManagementStateServerInterface>"8?<v?"NSNumber""NSError">16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_v16?0?<v?"NSNumber""NSError">8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___swift_closure_destructor.27Tm
+ _objc_msgSend$_authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:
+ _objc_msgSend$_resolveOneMoreMinuteViaSettings:proxy:completionHandler:
+ _objc_msgSend$authenticatePasscodeForUserWithEndpoint:userInterfaceStyle:completionHandler:
+ _objc_msgSend$authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:
+ _objc_msgSend$familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:
+ _objc_msgSend$hasMigratedWithReplyHandler:
+ _objc_msgSend$isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:
+ _swift_retain_x8
+ _symbolic SbIegy_
+ _symbolic ScTy_____Sg_____GSg 26ScreenTimeSettingsServices0ab10WebBrowserC0C s5NeverO
+ _symbolic So6NSUUIDCSgSo7NSErrorCSgIeyByy_
+ _symbolic _____IeyBy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____SgIeAgHr_ 26ScreenTimeSettingsServices0ab10WebBrowserC0C
+ _symbolic _____SgXw So38STScreenTimeWebBrowserSettingsObserverC06ScreenB4CoreE0E033_C1D88EBD6D178F2084F8C827022CEF0ELLC
+ _symbolic _____SgXwz_Xx So38STScreenTimeWebBrowserSettingsObserverC06ScreenB4CoreE0E033_C1D88EBD6D178F2084F8C827022CEF0ELLC
+ _symbolic _____XDXMT So29STScreenTimeWebBrowserHistoryC06ScreenB4CoreE5Store33_C1361D6D4F858D96C532ECBA2F242AACLLC
- -[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]
- -[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]
- GCC_except_table189
- GCC_except_table192
- GCC_except_table201
- GCC_except_table204
- GCC_except_table210
- __OBJC_$_PROP_LIST_STScreenTimeSettingsWebBrowserHistoryStoring
- __PROPERTIES_STScreenTimeWebBrowserHistory
- __PROPERTIES__TtCE14ScreenTimeCoreCSo29STScreenTimeWebBrowserHistoryP33_C1361D6D4F858D96C532ECBA2F242AAC5Store
- ___119-[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:completionHandler:]_block_invoke
- ___73-[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]_block_invoke
- ___73-[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]_block_invoke_2
- ___76-[STManagementState shouldAllowOneMoreMinuteForWebDomain:completionHandler:]_block_invoke_3
- ___76-[STManagementState shouldAllowOneMoreMinuteForWebDomain:completionHandler:]_block_invoke_4
- ___83-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:]_block_invoke_3
- ___83-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:]_block_invoke_4
- ___85-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:]_block_invoke_3
- ___85-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:]_block_invoke_4
- ___90-[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]_block_invoke
- ___90-[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]_block_invoke_2
- ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke
- ___swift_closure_destructor.20Tm
- _objc_msgSend$authenticatePasscodeWithCommunicationServiceProxy:completionHandler:
- _objc_msgSend$deviceListForAltDSID:forceRefresh:completionHandler:
- _objc_msgSend$isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:
CStrings:
+ "Authenticating for communication configuration override (style: %ld)"
+ "Prompted for passcode authentication (style: %ld)"
+ "STRemoteAlertConfigurationContextKeyUserInterfaceStyle"
+ "v16@?0@?<v@?@\"NSNumber\"@\"NSError\">8"
+ "v24@?0@\"<STManagementStateServerInterface>\"8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
```
