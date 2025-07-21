## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-531.140.7.0.0
-  __TEXT.__text: 0x3c9c8
+531.140.7.0.2
+  __TEXT.__text: 0x3d03c
   __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x4334
+  __TEXT.__objc_methlist: 0x439c
   __TEXT.__const: 0x380
   __TEXT.__gcc_except_tab: 0xef4
-  __TEXT.__cstring: 0x3e7f
-  __TEXT.__oslogstring: 0x2cc5
+  __TEXT.__cstring: 0x3e9f
+  __TEXT.__oslogstring: 0x2d10
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__unwind_info: 0x11f8
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methname: 0x9386
+  __TEXT.__objc_methname: 0x9461
   __TEXT.__objc_methtype: 0x325e
-  __TEXT.__objc_stubs: 0x5420
+  __TEXT.__objc_stubs: 0x5480
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22b0
+  __DATA_CONST.__objc_selrefs: 0x22d0
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0x1e80
-  __AUTH_CONST.__objc_const: 0x7018
+  __AUTH_CONST.__objc_const: 0x7038
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1158
   __AUTH.__data: 0x80

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 594665CF-3FA4-366B-9F8A-E7E275FAD01E
-  Functions: 1822
-  Symbols:   5850
-  CStrings:  3070
+  UUID: 02A19D5C-8AC2-3192-95CD-1A891064A031
+  Functions: 1833
+  Symbols:   5875
+  CStrings:  3075
 
Symbols:
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]
+ +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:].cold.1
+ -[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]
+ -[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]
+ -[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]
+ -[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]
+ -[FSClient(Project) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.1
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.2
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.3
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.4
+ GCC_except_table96
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.233
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.233.cold.1
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.228
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.228.cold.1
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.236
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.236.cold.1
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.236.cold.2
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.269
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.274
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.274.cold.1
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.274.cold.2
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.276
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.279
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.277
+ ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.283
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.285
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.288
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.288.cold.1
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.253
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.255
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.256
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.265
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.266
+ ___70-[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]_block_invoke
+ ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.244.cold.1
+ ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.245
+ ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke_2.246
+ ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.259
+ ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.259.cold.1
+ ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2.260
+ ___76-[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___78-[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___78-[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ ___87-[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]_block_invoke
+ ___87-[FSClient(Project) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]_block_invoke
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.24.cold.3
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.29.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.30.cold.2
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.32.cold.1
+ ___98+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke.cold.1
+ ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.235
+ ___block_literal_global.249
+ ___block_literal_global.258
+ ___block_literal_global.262
+ ___block_literal_global.268
+ ___block_literal_global.287
+ ___block_literal_global.321
+ _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:
+ _objc_msgSend$activateVolume:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$deactivateVolume:shortName:numericOptions:auditToken:replyHandler:
+ _objc_msgSend$loadResource:shortName:options:auditToken:replyHandler:
+ _objc_msgSend$sendConfigureUserClientWithReplyHandler:
+ _objc_msgSend$unloadResource:shortName:options:auditToken:replyHandler:
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]
- +[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:].cold.1
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.1
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.2
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.3
- GCC_except_table94
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.232
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.232.cold.1
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.227
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.227.cold.1
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235.cold.1
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.235.cold.2
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.268
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273.cold.1
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273.cold.2
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.275
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.278
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.276
- ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.282
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.284
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.287
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.287.cold.1
- ___67-[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]_block_invoke
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.252
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.254
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.255
- ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.264
- ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.265
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.243
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.243.cold.1
- ___74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke_2.245
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.258
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.258.cold.1
- ___75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2.259
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.24.cold.3
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.29.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.30.cold.2
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.32
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.32.cold.1
- ___87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.cold.1
- ___block_descriptor_116_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.234
- ___block_literal_global.248
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.267
- ___block_literal_global.286
- ___block_literal_global.316
- _objc_msgSend$DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:
- _objc_msgSend$fsMachPort
- _objc_msgSend$mountVolume:fileSystem:displayName:provider:domainError:on:how:options:
Functions (modified):
~ +[FSKitConstants(project) setArgumentsForFSClientXPC:] : 688 -> 768

Functions (added):
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.276
+ -[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]
+ ___78-[FSClient(Private) activateVolume:shortName:options:auditToken:replyHandler:]_block_invoke
+ -[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]
+ ___87-[FSClient(Private) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]_block_invoke
+ -[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]
+ ___76-[FSClient(Private) loadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ -[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]
+ ___78-[FSClient(Private) unloadResource:shortName:options:auditToken:replyHandler:]_block_invoke
+ -[FSClient(Project) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]
+ ___87-[FSClient(Project) deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]_block_invoke
+ _OUTLINED_FUNCTION_7
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.4

Functions (removed):
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.275
- _OUTLINED_FUNCTION_8
CStrings:
+ "%s: Created FSMachPort = %d"
+ "%s: Extension (%{public}@) doesn't have a mach port to configure user client"
+ "%s: Failed to create FSMachPort"
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]"
+ "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:]_block_invoke"
+ "-[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]"
+ "DAMountFSKitVolume:deviceName:mountPoint:volumeName:auditToken:mountOptions:"
+ "activateVolume:shortName:options:auditToken:replyHandler:"
+ "deactivateVolume:shortName:numericOptions:auditToken:replyHandler:"
+ "loadResource:shortName:options:auditToken:replyHandler:"
+ "sendConfigureUserClientWithReplyHandler:"
+ "unloadResource:shortName:options:auditToken:replyHandler:"
- "%s: Failed to create LiveFSMachPort"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]"
- "+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke"
- "-[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]"
- "DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:"
- "created fsFSMachPort = %d"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:options:"

```
