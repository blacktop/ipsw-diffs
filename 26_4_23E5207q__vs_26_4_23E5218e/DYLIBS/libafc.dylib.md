## libafc.dylib

> `/usr/lib/libafc.dylib`

```diff

-286.0.0.0.0
-  __TEXT.__text: 0x14fc4
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__const: 0xf4
-  __TEXT.__oslogstring: 0xf6b
-  __TEXT.__cstring: 0x19e7
+287.0.0.0.0
+  __TEXT.__text: 0x15d40
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__const: 0x110
+  __TEXT.__oslogstring: 0x10bd
+  __TEXT.__cstring: 0x1b40
+  __TEXT.__gcc_except_tab: 0x10
   __TEXT.__dof_afc: 0x88c
-  __TEXT.__unwind_info: 0x438
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xa00
-  __AUTH_CONST.__auth_got: 0x690
-  __AUTH_CONST.__const: 0x370
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__objc_methname: 0x1c
+  __TEXT.__objc_stubs: 0x40
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__const: 0x410
   __AUTH_CONST.__cfstring: 0xf00
-  __DATA.__data: 0x5c8
+  __DATA.__data: 0x5cc
   __DATA.__common: 0x18
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x59
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
-  UUID: 2D239D51-45AD-39D7-960E-C7633924B270
-  Functions: 455
-  Symbols:   1253
-  CStrings:  541
+  - /usr/lib/libobjc.A.dylib
+  UUID: CB4D81C2-F2AB-3935-9236-AE6579A62A05
+  Functions: 480
+  Symbols:   1342
+  CStrings:  566
 
Symbols:
+ GCC_except_table0
+ _AFCProcessServerPacket.cold.58
+ _InitializeActivationMonitor.initialized
+ _InitializeActivationMonitor.onceToken
+ _IsInternalDaemon.onceToken
+ _IsInternalDaemon.ret
+ _IsVirtualMachine.onceToken
+ _IsVirtualMachine.ret
+ _MAEGetActivationStateWithError
+ _PlatformSupportsActivation
+ _PlatformSupportsActivation.cold.1
+ _UpdateCachedActivationState
+ _UpdateCachedActivationState.cold.1
+ _UpdateCachedActivationState.cold.2
+ _UpdateCachedActivationState.cold.3
+ __NSGetExecutablePath
+ __Unwind_Resume
+ ___AFCActivationStateAllowsOperationOnPath
+ ___AFCActivationStateAllowsOperationOnPath.cold.1
+ ___AFCIsDeviceActivated
+ ___AFCIsDeviceActivated.cold.1
+ ___AFCIsDeviceActivated.cold.2
+ ___AFCIsDeviceActivated.cold.3
+ ___InitializeActivationMonitor_block_invoke
+ ___InitializeActivationMonitor_block_invoke.11
+ ___InitializeActivationMonitor_block_invoke.15
+ ___InitializeActivationMonitor_block_invoke.cold.1
+ ___InitializeActivationMonitor_block_invoke.cold.2
+ ___IsInternalDaemon_block_invoke
+ ___IsInternalDaemon_block_invoke.cold.1
+ ___IsInternalDaemon_block_invoke.cold.2
+ ___IsVirtualMachine_block_invoke
+ ___IsVirtualMachine_block_invoke.cold.1
+ _____AFCIsDeviceActivated_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.82
+ ___block_descriptor_tmp.94
+ ___block_descriptor_tmp.97
+ ___block_descriptor_tmp.98
+ ___block_literal_global.14
+ ___block_literal_global.17
+ ___block_literal_global.6
+ ___block_literal_global.9
+ ___chkstk_darwin
+ ___objc_personality_v0
+ __os_feature_enabled_impl
+ _basename_r
+ _dirname_r
+ _dispatch_async
+ _dispatch_once
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _gActivationNotifyToken
+ _gActivationQueue
+ _gCachedActivationState
+ _kMAActivationStateActivated
+ _kMAActivationStateFactoryActivated
+ _kNotificationActivationStateChanged
+ _objc_msgSend
+ _objc_msgSend$UTF8String
+ _objc_msgSend$isEqualToString:
+ _os_variant_allows_internal_security_policies
+ _os_variant_is_darwinos
+ _realpath$DARWIN_EXTSN
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.79
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.85
- ___block_descriptor_tmp.91
- ___block_descriptor_tmp.92
CStrings:
+ "/%s"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/afc.c"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/client-async.c"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/client-sync.c"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/connection.c"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/platform.c"
+ "/Library/Caches/com.apple.xbs/B8A0FBDE-8ECA-48E7-80FF-57426F31EA02/TemporaryDirectory.lEiSwy/Sources/AppleFileConduit/server.c"
+ "/private/var/mobile/Media/iTunes_Control"
+ "AppleFileConduit"
+ "Could not get executable path"
+ "Could not get executable realpath"
+ "Device Activated"
+ "Device Deactivated"
+ "Device not activated"
+ "EnableActivationChecksForInternalDaemon"
+ "Evaluating %s(%s)"
+ "Failed to check activation state: %@"
+ "Failed to create activation dispatch queue"
+ "Failed to determine if device is virtual machine"
+ "Failed to register for activation notification: %u"
+ "Requested path (%s) is currently not allowed to be operated on: Device not activated"
+ "UTF8String"
+ "__AFCActivationStateAllowsOperationOnPath"
+ "basename(%s)"
+ "com.apple.afc.activation"
+ "concat"
+ "dirname(%s)"
+ "failed to initialize activation monitor"
+ "isEqualToString:"
+ "kern.hv_vmm_present"
+ "realpath(%s) : %s"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/afc.c"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/client-async.c"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/client-sync.c"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/connection.c"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/platform.c"
- "/Library/Caches/com.apple.xbs/DE42B38B-61DC-4B56-8EEF-68B465B2594B/TemporaryDirectory.fapSDj/Sources/AppleFileConduit/server.c"

```
