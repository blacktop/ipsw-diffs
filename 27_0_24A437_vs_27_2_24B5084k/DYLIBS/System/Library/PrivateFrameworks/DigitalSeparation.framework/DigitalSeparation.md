## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-653.0.1.0.0
-  __TEXT.__text: 0x38994
-  __TEXT.__objc_methlist: 0x1fac
-  __TEXT.__cstring: 0x1887
-  __TEXT.__const: 0xaf8
-  __TEXT.__gcc_except_tab: 0xb78
-  __TEXT.__oslogstring: 0x26c4
+653.0.7.0.0
+  __TEXT.__text: 0x3a0f0
+  __TEXT.__objc_methlist: 0x202c
+  __TEXT.__cstring: 0x1927
+  __TEXT.__const: 0xbc8
+  __TEXT.__gcc_except_tab: 0xb8c
+  __TEXT.__oslogstring: 0x2844
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__swift5_typeref: 0x50e
+  __TEXT.__swift5_typeref: 0x51c
   __TEXT.__swift5_capture: 0x1c8
-  __TEXT.__constg_swiftt: 0x280
-  __TEXT.__swift5_reflstr: 0x213
-  __TEXT.__swift5_fieldmd: 0x2c4
+  __TEXT.__constg_swiftt: 0x29c
+  __TEXT.__swift5_reflstr: 0x263
+  __TEXT.__swift5_fieldmd: 0x31c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x54
-  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_types: 0x3c
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x90
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x10f8
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__unwind_info: 0x1170
   __TEXT.__eh_frame: 0xd10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1548
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__got: 0x530
-  __AUTH_CONST.__const: 0xe88
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x4e88
+  __DATA_CONST.__got: 0x550
+  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x4ed8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x908
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x7a8
+  __DATA.__objc_ivar: 0x194
+  __DATA.__data: 0x7b0
   __DATA_DIRTY.__objc_data: 0x938
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0xb8

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
+  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1242
-  Symbols:   2370
-  CStrings:  464
+  Functions: 1275
+  Symbols:   2412
+  CStrings:  477
 
Symbols:
+ -[DSAppSharing addFileAccessPermissionsToAppMap:handler:]
+ -[DSAppSharing resetFileAccessPermissionsForApp:withCompletionHandler:]
+ -[DSSourceDescriptor ignoreDisplayNames]
+ -[DSTCCStorePassThrough allAppsWithFileAccess:handler:]
+ -[DSTCCStorePassThrough resetFilePermissionForApp:completionHandler:]
+ -[DSXPCSharingPermissions _consumePendingCompletion:]
+ -[DSXPCSharingPermissions _failAllPendingOperationsWithError:]
+ -[DSXPCSharingPermissions _registerPendingCompletion:]
+ -[DSXPCSharingPermissions dealloc]
+ -[DSXPCSharingPermissions remoteProxyForCompletionToken:]
+ -[DSXPCSharingPermissions safetycheckdConnectionWithFailureHandlers:]
+ -[DSXPCSharingPermissions setFailureHandlersForConnection:]
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table5
+ GCC_except_table51
+ GCC_except_table9
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_FPAccessControlManager
+ _OBJC_CLASS_$_ICAccessManager
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_DSXPCSharingPermissions._connectionLock
+ _OBJC_IVAR_$_DSXPCSharingPermissions._pendingCompletions
+ _OUTLINED_FUNCTION_48
+ ___55-[DSTCCStorePassThrough allAppsWithFileAccess:handler:]_block_invoke
+ ___55-[DSTCCStorePassThrough allAppsWithFileAccess:handler:]_block_invoke_2
+ ___56-[DSAppSharing collectPermissionsForApps:queue:handler:]_block_invoke_6
+ ___57-[DSAppSharing addFileAccessPermissionsToAppMap:handler:]_block_invoke
+ ___57-[DSXPCSharingPermissions remoteProxyForCompletionToken:]_block_invoke
+ ___59-[DSXPCSharingPermissions setFailureHandlersForConnection:]_block_invoke
+ ___71-[DSAppSharing resetFileAccessPermissionsForApp:withCompletionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ _associated conformance 17DigitalSeparation21SafetyCheckEntrypointOSHAASQ
+ _objc_msgSend$UUID
+ _objc_msgSend$_consumePendingCompletion:
+ _objc_msgSend$_failAllPendingOperationsWithError:
+ _objc_msgSend$_registerPendingCompletion:
+ _objc_msgSend$addFileAccessPermissionsToAppMap:handler:
+ _objc_msgSend$allAppsWithFileAccess:handler:
+ _objc_msgSend$bundleIdentifiersAccessingExternalMediaDevices
+ _objc_msgSend$bundleIdentifiersWithAccessToAnyItemCompletionHandler:
+ _objc_msgSend$remoteProxyForCompletionToken:
+ _objc_msgSend$resetFileAccessPermissionsForApp:withCompletionHandler:
+ _objc_msgSend$resetFilePermissionForApp:completionHandler:
+ _objc_msgSend$revokeAccessToAllItemsForBundle:completionHandler:
+ _objc_msgSend$safetycheckdConnectionWithFailureHandlers:
+ _objc_msgSend$setFailureHandlersForConnection:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$updateBundleIdentifierAccessingExternalMediaDevices:withStatus:
+ _symbolic _____ 17DigitalSeparation21SafetyCheckEntrypointO
- -[DSXPCSharingPermissions connectXPC]
- -[DSXPCSharingPermissions disconnect]
- GCC_except_table30
- GCC_except_table31
- GCC_except_table36
- GCC_except_table41
- GCC_except_table46
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke
- ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_56_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- _objc_msgSend$connectXPC
- _objc_msgSend$xpcConnection
CStrings:
+ "Apple Intelligence"
+ "Attempting to reconnect to safetycheckd"
+ "Cannot connect to safetycheckd with error: %{public}@"
+ "DSFiles"
+ "Error resetting file access permissions %@"
+ "FILES"
+ "Failing pending operation %{public}@ due to connection failure"
+ "Sharing Reminder"
+ "XPC connection failure"
+ "XPC connection unavailable, consuming pending completion"
+ "com.apple.MobileSlideShow"
+ "fetchSharedResourcesWithCompletion: completion already consumed by connection failure handler"
+ "ignoreResourceDisplayName"
+ "stopSharingSources: strongSelf is nil"
+ "stopSharingWithParticipants: completion already consumed by connection failure handler"
+ "strongSelf is nil, cannot make sharing people"
- "Cannot connect to remote service with error: %{public}@"
- "Disconnecting xpc"
- "XPC connection failed, completion should be called in proxy error handler"
```
