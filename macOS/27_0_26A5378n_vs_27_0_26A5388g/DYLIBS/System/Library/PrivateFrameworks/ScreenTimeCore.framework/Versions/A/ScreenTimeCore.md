## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
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

```diff

-645.1.401.0.0
-  __TEXT.__text: 0xfd87c
-  __TEXT.__objc_methlist: 0xa0c0
-  __TEXT.__const: 0x3278
-  __TEXT.__cstring: 0xa39c
-  __TEXT.__oslogstring: 0xb99a
-  __TEXT.__gcc_except_tab: 0x1b60
-  __TEXT.__swift5_typeref: 0x149e
-  __TEXT.__constg_swiftt: 0xcf0
+649.0.0.0.0
+  __TEXT.__text: 0xff3b8
+  __TEXT.__objc_methlist: 0xa110
+  __TEXT.__const: 0x3308
+  __TEXT.__cstring: 0xa41c
+  __TEXT.__oslogstring: 0xba4a
+  __TEXT.__gcc_except_tab: 0x1ac4
+  __TEXT.__swift5_typeref: 0x153a
+  __TEXT.__constg_swiftt: 0xd0c
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x79e
-  __TEXT.__swift5_fieldmd: 0x998
+  __TEXT.__swift5_reflstr: 0x7be
+  __TEXT.__swift5_fieldmd: 0x9b4
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x210
-  __TEXT.__swift5_types: 0xe4
-  __TEXT.__swift5_capture: 0xa18
+  __TEXT.__swift5_types: 0xe8
+  __TEXT.__swift5_capture: 0xb04
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift_as_entry: 0x144
-  __TEXT.__swift_as_ret: 0x164
-  __TEXT.__swift_as_cont: 0x200
+  __TEXT.__swift_as_entry: 0x168
+  __TEXT.__swift_as_ret: 0x198
+  __TEXT.__swift_as_cont: 0x238
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3e30
-  __TEXT.__eh_frame: 0x3ab0
+  __TEXT.__unwind_info: 0x3f18
+  __TEXT.__eh_frame: 0x3f90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52e0
+  __DATA_CONST.__objc_selrefs: 0x5310
   __DATA_CONST.__objc_protorefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x250
-  __DATA_CONST.__got: 0xe10
-  __AUTH_CONST.__const: 0x4738
-  __AUTH_CONST.__cfstring: 0x96a0
-  __AUTH_CONST.__objc_const: 0x13090
+  __DATA_CONST.__got: 0xe08
+  __AUTH_CONST.__const: 0x4a50
+  __AUTH_CONST.__cfstring: 0x96e0
+  __AUTH_CONST.__objc_const: 0x13078
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0xfc8
-  __AUTH.__objc_data: 0x31a0
-  __AUTH.__data: 0x508
+  __AUTH_CONST.__auth_got: 0xfb0
+  __AUTH.__objc_data: 0x31a8
+  __AUTH.__data: 0x518
   __DATA.__objc_ivar: 0x7a0
-  __DATA.__data: 0x2160
+  __DATA.__data: 0x2180
   __DATA.__bss: 0x3ed0
   __DATA.__common: 0xd0
   __DATA_DIRTY.__objc_data: 0x1f18
-  __DATA_DIRTY.__data: 0x2a8
+  __DATA_DIRTY.__data: 0x298
   __DATA_DIRTY.__bss: 0x250
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5862
-  Symbols:   8704
-  CStrings:  2217
+  Functions: 5917
+  Symbols:   8729
+  CStrings:  2224
 
Symbols:
+ -[STCommunicationClient _authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]
+ -[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]
+ -[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:]
+ -[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]
+ -[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]
+ -[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]
+ -[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:]
+ -[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:]
+ -[STManagementState shouldAllowOneMoreMinuteForWebDomain:completionHandler:]
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table216
+ GCC_except_table222
+ _STRemoteAlertConfigurationContextKeyUserInterfaceStyle
+ __116-[STCommunicationClient _authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]_block_invoke
+ __83-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:]_block_invoke
+ ___100-[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]_block_invoke
+ ___100-[STManagementState isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:]_block_invoke_2
+ ___116-[STCommunicationClient _authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:]_block_invoke
+ ___138-[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:]_block_invoke
+ ___76-[STManagementState shouldAllowOneMoreMinuteForWebDomain:completionHandler:]_block_invoke
+ ___76-[STManagementState shouldAllowOneMoreMinuteForWebDomain:completionHandler:]_block_invoke_2
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_2
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_3
+ ___78-[STManagementState _resolveOneMoreMinuteViaSettings:proxy:completionHandler:]_block_invoke_4
+ ___83-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:completionHandler:]_block_invoke
+ ___85-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:]_block_invoke
+ ___85-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:]_block_invoke_2
+ ___91-[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]_block_invoke
+ ___91-[STManagementState familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSUUID"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e74_v24?0"<STManagementStateServerInterface>"8?<v?"NSNumber""NSError">16l
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e35_v16?0?<v?"NSNumber""NSError">8l
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48b56b
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_ScreenTimeCore
+ __swift__destructor
+ __swift_closure_destructor.26Tm
+ __swift_closure_destructor.27Tm
+ __swift_closure_destructor.30Tm
+ _objc_msgSend$_authenticateForCommunicationConfigurationOverrideWithUserInterfaceStyle:completionHandler:
+ _objc_msgSend$_resolveOneMoreMinuteViaSettings:proxy:completionHandler:
+ _objc_msgSend$authenticatePasscodeForUserWithEndpoint:userInterfaceStyle:completionHandler:
+ _objc_msgSend$authenticatePasscodeWithCommunicationServiceProxy:userInterfaceStyle:completionHandler:
+ _objc_msgSend$familyDevicesForAltDSID:forceRefresh:ineligibleOnly:completionHandler:
+ _objc_msgSend$hasMigratedWithReplyHandler:
+ _objc_msgSend$isFamilyMemberEligibleForMigrationUIWithAltDSID:forceRefresh:completionHandler:
+ _objc_msgSend$shouldAllowOneMoreMinuteForCategoryIdentifier:completionHandler:
+ _objc_msgSend$shouldAllowOneMoreMinuteForWebDomain:completionHandler:
+ _symbolic SbIegy_
+ _symbolic ScTy_____Sg_____GSg 26ScreenTimeSettingsServices0ab10WebBrowserC0C s5NeverO
+ _symbolic So6NSUUIDCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8NSNumberCSgSo7NSErrorCSgIeyByy_Sg
+ _symbolic _____ 14ScreenTimeCore17OneMoreMinuteGateO
+ _symbolic _____IeyBy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____SgIeAgHr_ 26ScreenTimeSettingsServices0ab10WebBrowserC0C
+ _symbolic _____SgXw So38STScreenTimeWebBrowserSettingsObserverC06ScreenB4CoreE0E033_C1D88EBD6D178F2084F8C827022CEF0ELLC
+ _symbolic _____SgXwz_Xx So38STScreenTimeWebBrowserSettingsObserverC06ScreenB4CoreE0E033_C1D88EBD6D178F2084F8C827022CEF0ELLC
+ _symbolic _____XDXMT So29STScreenTimeWebBrowserHistoryC06ScreenB4CoreE5Store33_C1361D6D4F858D96C532ECBA2F242AACLLC
- -[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]
- -[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]
- -[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:error:]
- -[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:error:]
- -[STManagementState shouldAllowOneMoreMinuteForWebDomain:error:]
- GCC_except_table164
- GCC_except_table167
- GCC_except_table170
- GCC_except_table199
- GCC_except_table202
- GCC_except_table208
- GCC_except_table214
- __96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke
- __OBJC_$_PROP_LIST_STScreenTimeSettingsWebBrowserHistoryStoring
- __PROPERTIES_STScreenTimeWebBrowserHistory
- __PROPERTIES__TtCE14ScreenTimeCoreCSo29STScreenTimeWebBrowserHistoryP33_C1361D6D4F858D96C532ECBA2F242AAC5Store
- ___119-[STConcretePasscodeAuthenticationProviderService authenticatePasscodeWithCommunicationServiceProxy:completionHandler:]_block_invoke
- ___64-[STManagementState shouldAllowOneMoreMinuteForWebDomain:error:]_block_invoke
- ___64-[STManagementState shouldAllowOneMoreMinuteForWebDomain:error:]_block_invoke_2
- ___71-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:error:]_block_invoke
- ___71-[STManagementState shouldAllowOneMoreMinuteForBundleIdentifier:error:]_block_invoke_2
- ___73-[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]_block_invoke
- ___73-[STManagementState deviceListForAltDSID:forceRefresh:completionHandler:]_block_invoke_2
- ___73-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:error:]_block_invoke
- ___73-[STManagementState shouldAllowOneMoreMinuteForCategoryIdentifier:error:]_block_invoke_2
- ___90-[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]_block_invoke
- ___90-[STManagementState isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:]_block_invoke_2
- ___96-[STCommunicationClient authenticateForCommunicationConfigurationOverrideWithCompletionHandler:]_block_invoke
- __swift_closure_destructor.20Tm
- __swift_closure_destructor.21Tm
- _objc_msgSend$authenticatePasscodeWithCommunicationServiceProxy:completionHandler:
- _objc_msgSend$deviceListForAltDSID:forceRefresh:completionHandler:
- _objc_msgSend$isFamilyEligibleForUpgradeWithAltDSID:forceRefresh:completionHandler:
- _objc_msgSend$shouldAllowOneMoreMinuteForBundleIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForCategoryIdentifier:error:
- _objc_msgSend$shouldAllowOneMoreMinuteForWebDomain:error:
- _symbolic _____y______G 26ScreenTimeSettingsServices0abC0C0C10CollectionV AC0B10AllowancesV5GroupV5EntryV
CStrings:
+ "%s: could not form URL for web domain, failing open"
+ "Authenticating for communication configuration override (style: %ld)"
+ "Prompted for passcode authentication (style: %ld)"
+ "STAskForTimeClient"
+ "STRemoteAlertConfigurationContextKeyUserInterfaceStyle"
+ "shouldAllowOneMoreMinute(for:)"
+ "v16@?0@?<v@?@\"NSNumber\"@\"NSError\">8"
+ "v24@?0@\"<STManagementStateServerInterface>\"8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "shouldAllowOneMoreMinute(forBundleIdentifier:)"
- "shouldAllowOneMoreMinute(forCategoryIdentifier:)"
```
