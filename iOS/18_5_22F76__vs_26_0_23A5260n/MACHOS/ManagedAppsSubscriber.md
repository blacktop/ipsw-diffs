## ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

-560.4.11.0.0
-  __TEXT.__text: 0x16808
-  __TEXT.__auth_stubs: 0xf50
+578.0.1.0.0
+  __TEXT.__text: 0x14d14
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_methlist: 0x360
-  __TEXT.__const: 0x5b2
-  __TEXT.__cstring: 0xbc3
-  __TEXT.__swift5_typeref: 0x3fa
-  __TEXT.__objc_methname: 0xad6
+  __TEXT.__const: 0x6e8
+  __TEXT.__swift5_typeref: 0x3e4
+  __TEXT.__objc_methname: 0xad8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x298
+  __TEXT.__constg_swiftt: 0x288
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x156
-  __TEXT.__swift5_fieldmd: 0x10c
+  __TEXT.__swift5_reflstr: 0x176
+  __TEXT.__swift5_fieldmd: 0x118
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x1c
+  __TEXT.__cstring: 0xd93
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift_as_entry: 0x64
-  __TEXT.__swift_as_ret: 0x7c
-  __TEXT.__oslogstring: 0x52d
-  __TEXT.__swift5_capture: 0x18c
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x64
+  __TEXT.__oslogstring: 0x3dd
+  __TEXT.__swift5_capture: 0x164
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x42d
-  __TEXT.__unwind_info: 0x510
-  __TEXT.__eh_frame: 0xe98
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x338
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__eh_frame: 0xba8
+  __DATA_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA.__objc_const: 0x438
-  __DATA.__objc_selrefs: 0x388
-  __DATA.__objc_data: 0x2f8
-  __DATA.__data: 0x690
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_data: 0x2e8
+  __DATA.__data: 0x530
   __DATA.__bss: 0x580
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
-  - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9996B3B7-4848-32E5-94EB-9FF1CD4EE022
-  Functions: 296
-  Symbols:   175
-  CStrings:  267
+  UUID: 5757FEA9-B613-38BF-9F75-191F6FBB05DE
+  Functions: 273
+  Symbols:   167
+  CStrings:  264
 
Symbols:
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_alwaysOff
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_alwaysOn
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_storeSettings
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_alwaysOff
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_alwaysOn
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_storeSettings
+ _RMModelStatusAppManagedList_State_notPresent
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x22
+ _objc_retain_x9
- _OBJC_CLASS_$_DMFApp
- _OBJC_CLASS_$_DMFConnection
- _OBJC_CLASS_$_DMFFetchAppsRequest
- _OBJC_CLASS_$_DMFFetchAppsResultObject
- _OBJC_CLASS_$_DMFStopManagingAppRequest
- __NSConcreteStackBlock
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x24
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
- _swift_release_n
CStrings:
+ "    Allow Downloads Over Cellular: "
+ "    Automatic App Updates: "
+ "  ComposedIdentifier: "
+ "  UpdateBehavior {\n"
+ "Composed identifier not supported on this platform"
+ "Could not query managed app list status key: %{public}@"
+ "Error.InvalidCodeSignature"
+ "This option means \"Use the settings the user has selected in the App Store or the alternative Marketplace that provided the app.\" The other choices are AlwaysOn and AlwaysOff, which force the option on or off. The key the MDM admin uses to select this value is \"StoreSettings\"."
+ "UI.APP-COMPOSED-IDENTIFIER"
+ "UI.AUTOMATIC-APP-UPDATES"
+ "UI.COMPOSED-IDENTIFIER"
+ "UI.STORE-SETTINGS"
+ "newComposedIdentifierWithBundleID:"
+ "payloadAllowDownloadsOverCellular"
+ "payloadAppComposedIdentifier"
+ "payloadAutomaticAppUpdates"
+ "payloadUpdateBehavior"
+ "payloadVersion"
+ "unsignedLongLongValue"
- "Could not query managed app status key: %{public}@"
- "Declarative Device Management"
- "Failed to fetch DMF app data: %@"
- "Failed to get app status when removing"
- "Failed to stop DMF managing app: %@"
- "Fetched DMF app data for: %{public}s"
- "Missing bundle ID when removing - will continue best effort"
- "Stopped DMF managing app: %{public}s"
- "appsByBundleIdentifier"
- "bundleIdentifier"
- "currentUserConnection"
- "iOS user scope is not supported"
- "performRequest:completion:"
- "setBundleIdentifier:"
- "setBundleIdentifiers:"
- "setManagedAppsOnly:"
- "setPropertyKeys:"
- "setSourceIdentifier:"
- "setType:"
- "v24@?0@\"CATTaskResultObject\"8@\"NSError\"16"

```
