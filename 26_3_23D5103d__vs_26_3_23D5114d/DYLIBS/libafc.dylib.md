## libafc.dylib

> `/usr/lib/libafc.dylib`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0xef6c
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__const: 0x6c
-  __TEXT.__cstring: 0x273c
+283.0.0.0.1
+  __TEXT.__text: 0x16690
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__const: 0x100
+  __TEXT.__oslogstring: 0x1055
+  __TEXT.__cstring: 0x198d
+  __TEXT.__gcc_except_tab: 0x10
   __TEXT.__dof_afc: 0x88c
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xa00
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x370
+  __TEXT.__unwind_info: 0x490
+  __TEXT.__objc_methname: 0x1c
+  __TEXT.__objc_stubs: 0x40
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0xf00
-  __DATA.__data: 0x5c8
-  __DATA.__bss: 0x20
-  __DATA.__common: 0x10
+  __DATA.__data: 0x5cc
+  __DATA.__common: 0x18
+  __DATA.__bss: 0x49
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
-  UUID: 68DEE829-A961-3E61-BAEC-97300DF95D9A
-  Functions: 321
-  Symbols:   846
-  CStrings:  533
+  - /usr/lib/libobjc.A.dylib
+  UUID: F6C1171E-2507-30B0-8710-7BE250977570
+  Functions: 472
+  Symbols:   1291
+  CStrings:  561
 
Symbols:
+ GCC_except_table6
+ _AFCConnectionCreate.cold.2
+ _AFCConnectionInvalidate.cold.1
+ _AFCConnectionInvalidate.cold.2
+ _AFCConnectionProcessOperation.cold.2
+ _AFCConnectionProcessOperation.cold.3
+ _AFCConnectionProcessOperation.cold.4
+ _AFCConnectionProcessOperation.cold.5
+ _AFCConnectionSetFatalError.cold.1
+ _AFCConnectionSubmitOperation.cold.1
+ _AFCConnectionUnscheduleFromRunLoop.cold.1
+ _AFCConnectionUnscheduleFromRunLoop.cold.2
+ _AFCConnectionUnscheduleFromRunLoop.cold.3
+ _AFCConnectionUnscheduleFromRunLoop.cold.4
+ _AFCDiscardData.cold.1
+ _AFCFileDescriptorCreateCloseOperation.cold.1
+ _AFCFileDescriptorCreateCloseOperation.cold.2
+ _AFCFileDescriptorInvalidate.cold.1
+ _AFCInitServerConnection.cold.1
+ _AFCLogPacketInfo.cold.1
+ _AFCLogPacketInfo.cold.10
+ _AFCLogPacketInfo.cold.11
+ _AFCLogPacketInfo.cold.12
+ _AFCLogPacketInfo.cold.13
+ _AFCLogPacketInfo.cold.14
+ _AFCLogPacketInfo.cold.15
+ _AFCLogPacketInfo.cold.16
+ _AFCLogPacketInfo.cold.17
+ _AFCLogPacketInfo.cold.18
+ _AFCLogPacketInfo.cold.19
+ _AFCLogPacketInfo.cold.2
+ _AFCLogPacketInfo.cold.20
+ _AFCLogPacketInfo.cold.21
+ _AFCLogPacketInfo.cold.22
+ _AFCLogPacketInfo.cold.23
+ _AFCLogPacketInfo.cold.24
+ _AFCLogPacketInfo.cold.25
+ _AFCLogPacketInfo.cold.26
+ _AFCLogPacketInfo.cold.27
+ _AFCLogPacketInfo.cold.28
+ _AFCLogPacketInfo.cold.29
+ _AFCLogPacketInfo.cold.3
+ _AFCLogPacketInfo.cold.30
+ _AFCLogPacketInfo.cold.31
+ _AFCLogPacketInfo.cold.32
+ _AFCLogPacketInfo.cold.33
+ _AFCLogPacketInfo.cold.34
+ _AFCLogPacketInfo.cold.35
+ _AFCLogPacketInfo.cold.36
+ _AFCLogPacketInfo.cold.37
+ _AFCLogPacketInfo.cold.38
+ _AFCLogPacketInfo.cold.39
+ _AFCLogPacketInfo.cold.4
+ _AFCLogPacketInfo.cold.40
+ _AFCLogPacketInfo.cold.41
+ _AFCLogPacketInfo.cold.42
+ _AFCLogPacketInfo.cold.43
+ _AFCLogPacketInfo.cold.44
+ _AFCLogPacketInfo.cold.45
+ _AFCLogPacketInfo.cold.46
+ _AFCLogPacketInfo.cold.47
+ _AFCLogPacketInfo.cold.48
+ _AFCLogPacketInfo.cold.49
+ _AFCLogPacketInfo.cold.5
+ _AFCLogPacketInfo.cold.50
+ _AFCLogPacketInfo.cold.51
+ _AFCLogPacketInfo.cold.52
+ _AFCLogPacketInfo.cold.6
+ _AFCLogPacketInfo.cold.7
+ _AFCLogPacketInfo.cold.8
+ _AFCLogPacketInfo.cold.9
+ _AFCOperationCreate.cold.2
+ _AFCProcessFileRefWritePacket.cold.5
+ _AFCProcessServerPacket.cold.16
+ _AFCProcessServerPacket.cold.17
+ _AFCProcessServerPacket.cold.18
+ _AFCProcessServerPacket.cold.19
+ _AFCProcessServerPacket.cold.20
+ _AFCProcessServerPacket.cold.21
+ _AFCProcessServerPacket.cold.22
+ _AFCProcessServerPacket.cold.23
+ _AFCProcessServerPacket.cold.24
+ _AFCProcessServerPacket.cold.25
+ _AFCProcessServerPacket.cold.26
+ _AFCProcessServerPacket.cold.27
+ _AFCProcessServerPacket.cold.28
+ _AFCProcessServerPacket.cold.29
+ _AFCProcessServerPacket.cold.30
+ _AFCProcessServerPacket.cold.31
+ _AFCProcessServerPacket.cold.32
+ _AFCProcessServerPacket.cold.33
+ _AFCProcessServerPacket.cold.34
+ _AFCProcessServerPacket.cold.35
+ _AFCProcessServerPacket.cold.36
+ _AFCProcessServerPacket.cold.37
+ _AFCProcessServerPacket.cold.38
+ _AFCProcessServerPacket.cold.39
+ _AFCProcessServerPacket.cold.40
+ _AFCProcessServerPacket.cold.41
+ _AFCProcessServerPacket.cold.42
+ _AFCProcessServerPacket.cold.43
+ _AFCProcessServerPacket.cold.44
+ _AFCProcessServerPacket.cold.45
+ _AFCProcessServerPacket.cold.46
+ _AFCProcessServerPacket.cold.47
+ _AFCProcessServerPacket.cold.48
+ _AFCProcessServerPacket.cold.49
+ _AFCProcessServerPacket.cold.50
+ _AFCProcessServerPacket.cold.51
+ _AFCProcessServerPacket.cold.52
+ _AFCProcessServerPacket.cold.53
+ _AFCProcessServerPacket.cold.54
+ _AFCProcessServerPacket.cold.55
+ _AFCProcessServerPacket.cold.56
+ _AFCProcessServerPacket.cold.57
+ _AFCProcessServerPacket.cold.58
+ _AFCReadPacketHeader.cold.1
+ _AFCReadPacketHeader.cold.2
+ _AFCSendStatusExtended.cold.1
+ _AFCSendStatusExtended.cold.2
+ _AFCServeWithRoot.cold.1
+ _AFCServeWithRoot.cold.2
+ _AFCServeWithRoot.cold.3
+ _AFCSetSocketOptions.cold.1
+ _AFCSetSocketOptions.cold.2
+ _AFCValidateHeader.cold.1
+ _InitModelName.cold.1
+ _IsVirtualMachine.onceToken
+ _IsVirtualMachine.ret
+ _MAEGetActivationStateWithError
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _PlatformSupportsActivation
+ _PlatformSupportsActivation.cold.1
+ _UpdateCachedActivationState
+ _UpdateCachedActivationState.cold.1
+ _UpdateCachedActivationState.cold.2
+ _UpdateCachedActivationState.cold.3
+ __AFCSetFSBlockSize.cold.1
+ __Unwind_Resume
+ ___AFCActivationStateAllowsOperationOnPath
+ ___AFCActivationStateAllowsOperationOnPath.cold.1
+ ___AFCConnectionFinalize.cold.1
+ ___AFCConnectionFinalize.cold.2
+ ___AFCConnectionFinalize.cold.3
+ ___AFCConnectionInvalidate.cold.1
+ ___AFCConnectionNotifyOperationComplete.cold.1
+ ___AFCConnectionPerformOperationCallBack.cold.1
+ ___AFCConnectionProcessData.cold.1
+ ___AFCConnectionProcessData.cold.2
+ ___AFCConnectionProcessData.cold.3
+ ___AFCConnectionReceiveOperation.cold.1
+ ___AFCConnectionUnscheduleFromRunLoop.cold.1
+ ___AFCConnectionUnscheduleFromRunLoop.cold.2
+ ___AFCCoordinateFileActivity.cold.1
+ ___AFCCoordinateFileActivity.cold.2
+ ___AFCFileDescriptorFinalize.cold.1
+ ___AFCInitializeActivationMonitor
+ ___AFCInitializeActivationMonitor.cold.1
+ ___AFCInitializeActivationMonitor.initialized
+ ___AFCInitializeActivationMonitor.onceToken
+ ___AFCIsDeviceActivated
+ ___AFCLogPreferencesChanged.cold.1
+ ___AFCLogPreferencesChanged.cold.2
+ ___AFCLogPreferencesChanged.cold.3
+ ___AFCOperationFinalize.cold.1
+ ___AFCServerInit.cold.1
+ ___AFCServerInit.cold.2
+ ___AFCSetErrorResult.cold.1
+ ___IsVirtualMachine_block_invoke
+ ___IsVirtualMachine_block_invoke.cold.1
+ _____AFCInitializeActivationMonitor_block_invoke
+ _____AFCInitializeActivationMonitor_block_invoke.2
+ _____AFCInitializeActivationMonitor_block_invoke.6
+ _____AFCInitializeActivationMonitor_block_invoke.cold.1
+ _____AFCInitializeActivationMonitor_block_invoke.cold.2
+ _____AFCIsDeviceActivated_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.8
+ ___block_descriptor_tmp.82
+ ___block_descriptor_tmp.88
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.94
+ ___block_descriptor_tmp.97
+ ___block_descriptor_tmp.98
+ ___block_literal_global.11
+ ___block_literal_global.34
+ ___block_literal_global.5
+ ___block_literal_global.8
+ ___chkstk_darwin
+ ___gAFCOSLog
+ ___objc_personality_v0
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_fault_impl
+ __os_log_impl
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
+ _os_log_create
+ _os_log_type_enabled
+ _os_variant_is_darwinos
+ _realpath$DARWIN_EXTSN
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.142
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.77
- ___block_literal_global.53
CStrings:
+ "/%s"
+ "/private/var/mobile/Media/iTunes_Control"
+ "Device Activated"
+ "Device Deactivated"
+ "Device not activated"
+ "Evaluating %s(%s)"
+ "Failed to check activation state: %@"
+ "Failed to create activation dispatch queue"
+ "Failed to determine if device is virtual machine"
+ "Failed to register for activation notification: %u"
+ "Requested path (%s) is currently not allowed to be operated on: Device not activated"
+ "UTF8String"
+ "Unknown log level"
+ "__AFCActivationStateAllowsOperationOnPath"
+ "basename(%s)"
+ "com.apple.afc.activation"
+ "concat"
+ "dirname(%s)"
+ "isEqualToString:"
+ "kern.hv_vmm_present"
+ "realpath(%s) : %s"

```
