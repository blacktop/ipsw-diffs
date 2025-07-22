## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-48.0.0.0.0
-  __TEXT.__text: 0x4c61c
+49.0.0.0.0
+  __TEXT.__text: 0x4c900
   __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x7080
+  __TEXT.__objc_methlist: 0x70d0
   __TEXT.__const: 0x2c4
-  __TEXT.__oslogstring: 0x1e21
-  __TEXT.__cstring: 0x2c15
+  __TEXT.__oslogstring: 0x1ea1
+  __TEXT.__cstring: 0x2c35
   __TEXT.__gcc_except_tab: 0x7a0
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8

   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x14f0
+  __TEXT.__unwind_info: 0x14f8
   __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x114e
-  __TEXT.__objc_methname: 0x142b0
-  __TEXT.__objc_methtype: 0x4955
-  __TEXT.__objc_stubs: 0xd160
+  __TEXT.__objc_classname: 0x117c
+  __TEXT.__objc_methname: 0x1436d
+  __TEXT.__objc_methtype: 0x498c
+  __TEXT.__objc_stubs: 0xd1c0
   __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0xfd8
+  __DATA_CONST.__const: 0x1028
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4898
+  __DATA_CONST.__objc_selrefs: 0x48b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x6f0
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x2ec0
-  __AUTH_CONST.__objc_const: 0x11340
+  __AUTH_CONST.__objc_const: 0x113b8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5e0
-  __DATA.__data: 0x1358
+  __DATA.__objc_ivar: 0x5e4
+  __DATA.__data: 0x13b8
   __DATA.__bss: 0x60
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 72315FE9-3C4A-3C04-87E3-8C648C23C1BC
-  Functions: 2121
-  Symbols:   8131
-  CStrings:  4598
+  UUID: DBA74A5E-9A4B-3D5C-91A6-E51EAD10C449
+  Functions: 2123
+  Symbols:   8147
+  CStrings:  4609
 
Symbols:
+ -[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequestNeedsExtractablePasscode:]
+ -[DMCProfileViewController isProvisionalMDMProfile]
+ GCC_except_table49
+ _OBJC_IVAR_$_DMCProfileViewController._isProvisionalMDMProfile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentFlowProfileInstallationPresenter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DMCEnrollmentFlowProfileInstallationPresenter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowProfileInstallationPresenter
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowProfileInstallationPresenter
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowProfileInstallationPresenter
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowProfileInstallationPresenter
+ ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.45
+ ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.46
+ ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.40
+ ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.66
+ ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.104
+ ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.97
+ ___94-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequestNeedsExtractablePasscode:]_block_invoke
+ ___94-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequestNeedsExtractablePasscode:]_block_invoke_2
+ ___94-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequestNeedsExtractablePasscode:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e22_v28?0"NSData"8Q16B24ls32l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.106
+ _objc_msgSend$_handlePasscodeRequestNeedsExtractablePasscode:
+ _objc_msgSend$requestDevicePasscodeDataWithCompletionHandler:
+ _objc_msgSend$setRightView:
+ _objc_msgSend$setRightViewMode:
- -[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]
- GCC_except_table48
- ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.42
- ___113-[DMCEnrollmentFlowManagedConfigurationHelper awaitPendingApplicationInstallationWithObserver:completionHandler:]_block_invoke.43
- ___202-[DMCEnrollmentFlowManagedConfigurationHelper manageApplicationWithBundleID:iTunesItemID:organization:personaID:associatedDomains:associatedDomainsEnableDirectDownloads:configuration:completionHandler:]_block_invoke.37
- ___69-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]_block_invoke
- ___69-[DMCEnrollmentFlowManagedConfigurationHelper _handlePasscodeRequest]_block_invoke_2
- ___84-[DMCEnrollmentFlowManagedConfigurationHelper _mdmV1AppsInstallationStateDidChange:]_block_invoke.61
- ___90-[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]_block_invoke.99
- ___93-[DMCEnrollmentFlowManagedConfigurationHelper _systemAppDeletableInstallationStateDidChange:]_block_invoke.92
- ___block_literal_global.101
- _objc_msgSend$_handlePasscodeRequest
CStrings:
+ "@\"<DMCEnrollmentFlowProfileInstallationPresenter>\""
+ "DMCEnrollmentFlowManagedConfigurationHelper: No presenter is provided."
+ "DMCEnrollmentFlowProfileInstallationPresenter"
+ "Fetched auth mode: %lu"
+ "T@\"<DMCEnrollmentFlowProfileInstallationPresenter>\",W,V_presenter"
+ "TB,R,N,V_isProvisionalMDMProfile"
+ "Will ask for passcode. needsExtractablePasscode: %d"
+ "_handlePasscodeRequestNeedsExtractablePasscode:"
+ "_isProvisionalMDMProfile"
+ "isProvisionalMDMProfile"
+ "isUpdateFromFactoryVersionRequired"
+ "setRightView:"
+ "setRightViewMode:"
+ "v28@?0@\"NSData\"8Q16B24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"B>24"
- "@\"DMCBYODEnrollmentFlowUIPresenter\""
- "T@\"DMCBYODEnrollmentFlowUIPresenter\",W,V_presenter"
- "Will ask for passcode"
- "_handlePasscodeRequest"

```
