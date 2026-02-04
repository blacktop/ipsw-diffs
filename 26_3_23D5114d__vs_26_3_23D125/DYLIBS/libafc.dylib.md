## libafc.dylib

> `/usr/lib/libafc.dylib`

```diff

-283.0.0.0.1
-  __TEXT.__text: 0x16690
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x1055
-  __TEXT.__cstring: 0x198d
-  __TEXT.__gcc_except_tab: 0x10
+284.82.1.0.0
+  __TEXT.__text: 0x15ac4
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__const: 0xdc
+  __TEXT.__oslogstring: 0xf6b
+  __TEXT.__cstring: 0x186d
   __TEXT.__dof_afc: 0x88c
-  __TEXT.__unwind_info: 0x490
-  __TEXT.__objc_methname: 0x1c
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xa68
-  __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH_CONST.__const: 0x3f0
+  __TEXT.__unwind_info: 0x440
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0xa00
+  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__const: 0x370
   __AUTH_CONST.__cfstring: 0xf00
-  __DATA.__data: 0x5cc
+  __DATA.__data: 0x5c8
   __DATA.__common: 0x18
-  __DATA.__bss: 0x49
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libobjc.A.dylib
-  UUID: F6C1171E-2507-30B0-8710-7BE250977570
-  Functions: 472
-  Symbols:   1291
-  CStrings:  561
+  UUID: B5D75FFC-B76F-38F8-968B-1D4DB1851C33
+  Functions: 451
+  Symbols:   1217
+  CStrings:  541
 
Symbols:
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.91
+ ___block_descriptor_tmp.92
- GCC_except_table6
- _AFCProcessServerPacket.cold.58
- _IsVirtualMachine.onceToken
- _IsVirtualMachine.ret
- _MAEGetActivationStateWithError
- _PlatformSupportsActivation
- _PlatformSupportsActivation.cold.1
- _UpdateCachedActivationState
- _UpdateCachedActivationState.cold.1
- _UpdateCachedActivationState.cold.2
- _UpdateCachedActivationState.cold.3
- __Unwind_Resume
- ___AFCActivationStateAllowsOperationOnPath
- ___AFCActivationStateAllowsOperationOnPath.cold.1
- ___AFCInitializeActivationMonitor
- ___AFCInitializeActivationMonitor.cold.1
- ___AFCInitializeActivationMonitor.initialized
- ___AFCInitializeActivationMonitor.onceToken
- ___AFCIsDeviceActivated
- ___IsVirtualMachine_block_invoke
- ___IsVirtualMachine_block_invoke.cold.1
- _____AFCInitializeActivationMonitor_block_invoke
- _____AFCInitializeActivationMonitor_block_invoke.2
- _____AFCInitializeActivationMonitor_block_invoke.6
- _____AFCInitializeActivationMonitor_block_invoke.cold.1
- _____AFCInitializeActivationMonitor_block_invoke.cold.2
- _____AFCIsDeviceActivated_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_32_e8_v12?0i8l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.82
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.97
- ___block_descriptor_tmp.98
- ___block_literal_global.11
- ___block_literal_global.5
- ___block_literal_global.8
- ___chkstk_darwin
- ___objc_personality_v0
- _basename_r
- _dirname_r
- _dispatch_async
- _dispatch_once
- _dispatch_queue_attr_make_with_autorelease_frequency
- _gActivationNotifyToken
- _gActivationQueue
- _gCachedActivationState
- _kMAActivationStateActivated
- _kMAActivationStateFactoryActivated
- _kNotificationActivationStateChanged
- _objc_msgSend
- _objc_msgSend$UTF8String
- _objc_msgSend$isEqualToString:
- _os_variant_is_darwinos
- _realpath$DARWIN_EXTSN
CStrings:
- "/%s"
- "/private/var/mobile/Media/iTunes_Control"
- "Device Activated"
- "Device Deactivated"
- "Device not activated"
- "Evaluating %s(%s)"
- "Failed to check activation state: %@"
- "Failed to create activation dispatch queue"
- "Failed to determine if device is virtual machine"
- "Failed to register for activation notification: %u"
- "Requested path (%s) is currently not allowed to be operated on: Device not activated"
- "UTF8String"
- "__AFCActivationStateAllowsOperationOnPath"
- "basename(%s)"
- "com.apple.afc.activation"
- "concat"
- "dirname(%s)"
- "isEqualToString:"
- "kern.hv_vmm_present"
- "realpath(%s) : %s"

```
