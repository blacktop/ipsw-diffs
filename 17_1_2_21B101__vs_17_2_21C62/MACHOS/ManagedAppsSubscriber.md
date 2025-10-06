## ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

-500.25.2.2.0
-  __TEXT.__text: 0x6900
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0x162
-  __TEXT.__swift5_typeref: 0x184
-  __TEXT.__objc_methname: 0x720
+500.25.3.7.0
+  __TEXT.__text: 0xd5d0
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0xe4
+  __TEXT.__const: 0x192
+  __TEXT.__swift5_typeref: 0x296
+  __TEXT.__objc_methname: 0x700
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x587
-  __TEXT.__constg_swiftt: 0x10c
-  __TEXT.__swift5_fieldmd: 0x4c
-  __TEXT.__swift5_reflstr: 0x15
+  __TEXT.__cstring: 0xb0d
+  __TEXT.__constg_swiftt: 0x134
+  __TEXT.__swift5_fieldmd: 0x7c
+  __TEXT.__swift5_capture: 0xa0
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_reflstr: 0x76
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x306
-  __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__eh_frame: 0x128
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2a0
+  __TEXT.__unwind_info: 0x2ac
+  __TEXT.__eh_frame: 0x640
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x690
-  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_data: 0x260
-  __DATA.__data: 0x330
+  __DATA.__objc_data: 0x288
+  __DATA.__data: 0x3f8
   __DATA.__common: 0x30
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
-  - /System/Library/PrivateFrameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7EC6DB32-3FA0-3C70-9420-EA0E261FDFCE
-  Functions: 105
-  Symbols:   122
-  CStrings:  160
+  UUID: D199F1D8-8501-3B0D-A626-8B217E12F7D9
+  Functions: 165
+  Symbols:   133
+  CStrings:  188
 
Symbols:
+ _OBJC_CLASS_$_DMFRemoveAppRequest
+ _OBJC_CLASS_$_RMConfigurationUIDetails
+ _OBJC_CLASS_$_RMModelStatusReason
+ _RMModelAppManagedDeclaration_InstallBehaviorLicense_VPPType_device
+ _RMModelAppManagedDeclaration_InstallBehaviorLicense_VPPType_user
+ _RMModelAppManagedDeclaration_InstallBehavior_Install_optional
+ _RMModelAppManagedDeclaration_InstallBehavior_Install_required
+ _RMModelStatusAppManagedList_State_downloading
+ _RMModelStatusAppManagedList_State_optional
+ _RMModelStatusAppManagedList_State_promptingForConsent
+ _RMModelStatusAppManagedList_UpdateState_available
+ _RMModelStatusAppManagedList_UpdateState_failed
+ _RMModelStatusAppManagedList_UpdateState_promptingForUpdate
+ _RMModelStatusAppManagedList_UpdateState_promptingForUpdateLogin
+ _RMModelStatusAppManagedList_UpdateState_updating
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x27
+ _swift_allocBox
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deletedAsyncMethodErrorTu
+ _swift_getErrorValue
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
- _OBJC_CLASS_$_DMFApp
- _OBJC_CLASS_$_DMFFetchAppsRequest
- _OBJC_CLASS_$_DMFFetchAppsResultObject
- _RMModelAppManagedDeclaration_InstallBehavior_Install_immediately
- _RMModelAppManagedDeclaration_InstallBehavior_Install_onDemand
- _RMModelStatusAppManagedList_State_managementRejected
- _RMModelStatusAppManagedList_State_needsRedemption
- _RMModelStatusAppManagedList_State_prompting
- _RMModelStatusAppManagedList_State_promptingForUpdate
- _RMModelStatusAppManagedList_State_promptingForUpdateLogin
- _RMModelStatusAppManagedList_State_redeeming
- _RMModelStatusAppManagedList_State_unknown
- _RMModelStatusAppManagedList_State_updateRejected
- _RMModelStatusAppManagedList_State_updating
- _RMModelStatusAppManagedList_State_userInstalledApp
- _RMModelStatusAppManagedList_State_userRejected
- _RMModelStatusAppManagedList_State_validatingPurchase
- _RMModelStatusAppManagedList_State_validatingUpdate
- _swift_beginAccess
- _swift_setDeallocating
CStrings:
+ "Apps cannot be used with enterprise persona"
+ "Configuration for App Store app has invalid VPP license type"
+ "Configuration for App Store app is missing the VPP license type"
+ "Could not query managed app status key: %{public}@"
+ "Declarative Device Management"
+ "Error.AppStoreDisabled"
+ "Error.DownloadFailed"
+ "Error.DuplicateConfiguredApp"
+ "Error.InstallFailed"
+ "Error.InvalidAppID"
+ "Error.LicenseNotFound"
+ "Error.UnmanagedAppAlreadyInstalled"
+ "Error.UpdateFailed"
+ "Error.UserRejected"
+ "Failed to get app status for configurationUI"
+ "Failed to get app status when removing"
+ "Failed to remove DMF app data: %@"
+ "Get configuration UI for: %{public}s"
+ "Ignoring unknown status key path: %s"
+ "Info.UpdateAvailable"
+ "Internal error: "
+ "Invalid VPP license type: "
+ "Invalid configuration type in configurationUI"
+ "Missing bundle ID when removing - will continue best effort"
+ "Removed DMF app data for: %{public}s"
+ "UI.ATTRIBUTES.CELLULAR-SLICE"
+ "UI.ATTRIBUTES.CONTENT-FILTER"
+ "UI.ATTRIBUTES.DNS-PROXY"
+ "UI.ATTRIBUTES.RELAY"
+ "UI.ATTRIBUTES.TAP-TO-PAY"
+ "UI.ATTRIBUTES.VPN"
+ "UI.ENTERPRISE-APP"
+ "UI.INCLUDE-IN-BACKUP"
+ "Unknown managed app state:%s"
+ "Unknown managed app update state: %s"
+ "Unknown scope"
+ "VPP license type is not specified for an App Store app"
+ "Wrong number of app status items for configuration UI: "
+ "buildRequiredOnlyWithCode:"
+ "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:"
+ "configurationUIWithTitle:description:details:"
+ "iOS user scope is not supported"
+ "identifier"
+ "payloadLicense"
+ "payloadVPPType"
+ "personaIdentifier"
+ "setBundleIdentifier:"
+ "setSourceIdentifier:"
+ "store"
+ "storeIdentifier"
- "    AccountPromptAllowed: "
- "  RemoveBehavior {\n"
- "Failed DMFFetchAppsRequest %@"
- "Failed to create DMFConnection"
- "Failed to create DMFFetchAppsRequest"
- "Invalid status keys %{public}s"
- "Unknown store type %ld"
- "Wrong DMFFetchAppsRequest result type"
- "appsByBundleIdentifier"
- "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:"
- "bundleIdentifier"
- "displayName"
- "externalVersionIdentifier"
- "managementInformation"
- "payloadAccountPromptAllowed"
- "payloadRemovable"
- "payloadRemoveBehavior"
- "setManagedAppsOnly:"
- "shortVersion"
- "state"
- "stringValue"
- "systemConnection"
- "type"
- "version"

```
