## ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x10d08
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0xe8
-  __TEXT.__const: 0x2b2
-  __TEXT.__cstring: 0xe00
-  __TEXT.__swift5_typeref: 0x30c
-  __TEXT.__objc_methname: 0x95d
+560.4.11.0.0
+  __TEXT.__text: 0x16808
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_methlist: 0x360
+  __TEXT.__const: 0x5b2
+  __TEXT.__cstring: 0xbc3
+  __TEXT.__swift5_typeref: 0x3fa
+  __TEXT.__objc_methname: 0xad6
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x184
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xe6
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_fieldmd: 0xac
+  __TEXT.__constg_swiftt: 0x298
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x156
+  __TEXT.__swift5_fieldmd: 0x10c
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x7c
+  __TEXT.__oslogstring: 0x52d
   __TEXT.__swift5_capture: 0x18c
-  __TEXT.__oslogstring: 0x44d
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x42d
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__eh_frame: 0xa70
-  __DATA_CONST.__auth_got: 0x6f8
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x480
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0xe98
+  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x798
-  __DATA.__objc_selrefs: 0x1f8
-  __DATA.__objc_data: 0x2a0
-  __DATA.__data: 0x4f8
-  __DATA.__bss: 0x280
+  __DATA.__objc_const: 0x438
+  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_data: 0x2f8
+  __DATA.__data: 0x690
+  __DATA.__bss: 0x580
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
+  - /System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 225
-  Symbols:   151
-  CStrings:  254
+  Functions: 296
+  Symbols:   175
+  CStrings:  267
 
Symbols:
+ _OBJC_CLASS_$_DMCComposedIdentifier
+ _OBJC_CLASS_$_DMCDefaults
+ _OBJC_CLASS_$_RMErSSOStore
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_AppConfigDictionary
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_CredentialConfig
+ _OBJC_CLASS_$_RMModelAssetBase
+ _OBJC_CLASS_$_RMModelAssetCredentialACMEDeclaration
+ _OBJC_CLASS_$_RMModelAssetCredentialCertificateDeclaration
+ _OBJC_CLASS_$_RMModelAssetCredentialIdentityDeclaration
+ _OBJC_CLASS_$_RMModelAssetCredentialSCEPDeclaration
+ _OBJC_CLASS_$_RMModelAssetCredentialUserNameAndPasswordDeclaration
+ _OBJC_CLASS_$_RMModelAssetDataDeclaration
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfiguration
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfigurationState
+ _OBJC_CLASS_$_RMStoreAssetKey
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _RMUIConfigurationUIHiddenDetailAppBundleID
+ _objc_retain_x27
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
- _OBJC_CLASS_$_RMModelAppManagedDeclaration_AppCredentialConfig
- _objc_retain_x9
- _swift_arrayDestroy
CStrings:
+ "$__lazy_storage_$_systemClient"
+ "$__lazy_storage_$_userClient"
+ "Applying app config: %{public}s"
+ "ESSOTestModeEnabled"
+ "Error.IsSystemApp"
+ "Failed to apply app config with error: %{public}@"
+ "Failed to remove app config with error: %{public}@"
+ "Invalid composed identifier: "
+ "Removing app config: %{public}s"
+ "_TtC21ManagedAppsSubscriber10MACAPIImpl"
+ "assetWithIdentifier:"
+ "build"
+ "buildWithAppConfigState:extensionConfigState:"
+ "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:configState:reasons:"
+ "buildWithState:"
+ "bundleID"
+ "configurationUIWithTitle:description:details:hiddenDetails:"
+ "isPreEnrollmentErSSOStore:"
+ "keyWithoutServerToken"
+ "loading extension config: %s"
+ "macapi"
+ "newAssetKeyWithAsset:"
+ "newComposedIdentifier:"
+ "payloadAppConfig"
+ "payloadAssetReference"
+ "payloadCertificates"
+ "payloadDataAssetReference"
+ "payloadDictionary"
+ "payloadExtensionConfigs"
+ "payloadIdentifier"
+ "payloadIdentities"
+ "payloadLegacyAppConfigAssetReference"
+ "payloadPasswords"
+ "scope"
+ "setStatusDictionary:"
+ "teamID"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:"
- "configurationUIWithTitle:description:details:"
- "invalid Collection: less than 'count' elements in collection"
- "payloadAppConfigAssetReference"
- "payloadCertificateAppConfigs"
- "payloadIdentityAppConfigs"
- "payloadPasswordAppConfigs"

```
