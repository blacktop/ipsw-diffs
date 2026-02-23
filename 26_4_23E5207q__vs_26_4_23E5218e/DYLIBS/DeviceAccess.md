## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-324.20.1.1.1
-  __TEXT.__text: 0x484dc
+324.23.0.0.0
+  __TEXT.__text: 0x4a718
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x3b44
+  __TEXT.__objc_methlist: 0x3c34
   __TEXT.__const: 0x608
-  __TEXT.__cstring: 0x7be3
-  __TEXT.__gcc_except_tab: 0xaf8
+  __TEXT.__cstring: 0x8493
+  __TEXT.__gcc_except_tab: 0xd30
   __TEXT.__constg_swiftt: 0x3d0
   __TEXT.__swift5_typeref: 0x258
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1168
+  __TEXT.__unwind_info: 0x1238
   __TEXT.__eh_frame: 0x570
   __TEXT.__objc_classname: 0x5c4
-  __TEXT.__objc_methname: 0x7821
-  __TEXT.__objc_methtype: 0xac6
-  __TEXT.__objc_stubs: 0x3ce0
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0xc08
+  __TEXT.__objc_methname: 0x7a1e
+  __TEXT.__objc_methtype: 0xaf6
+  __TEXT.__objc_stubs: 0x3f40
+  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b08
+  __DATA_CONST.__objc_selrefs: 0x1bb8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x690
-  __AUTH_CONST.__cfstring: 0x2fe0
-  __AUTH_CONST.__objc_const: 0x6bc0
+  __AUTH_CONST.__cfstring: 0x30e0
+  __AUTH_CONST.__objc_const: 0x6c70
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x8e0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x5ec
+  __DATA.__objc_ivar: 0x5fc
   __DATA.__data: 0xc30
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1F823DA7-0460-3C8C-9822-5C545AFA2096
-  Functions: 1963
-  Symbols:   5527
-  CStrings:  3197
+  UUID: 253911B3-B1DA-31FD-8A62-44FE1C3B7963
+  Functions: 2004
+  Symbols:   5648
+  CStrings:  3298
 
Symbols:
+ -[DAExtension _capabilitiesEnsureStartedWithFlags:error:]
+ -[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]
+ -[DAExtension _extensionEnsureStartedWithError:]
+ -[DAExtension _handleProcessStateUpdate:process:]
+ -[DAExtension _invalidated].cold.2
+ -[DAExtension _invalidated].cold.3
+ -[DAExtension _removeCapabilityWithFlag:]
+ -[DAExtension _reportEvent:]
+ -[DAExtension _reportEvent:].cold.1
+ -[DAExtension _reportEvent:].cold.2
+ -[DAExtension _startProcessMonitor:]
+ -[DAExtension _suspend]
+ -[DAExtension _suspend].cold.1
+ -[DAExtension bluetoothRestorationID]
+ -[DAExtension launchCapabilitiesWithFlags:]
+ -[DAExtension launch]
+ -[DAExtension processState]
+ -[DAExtension resumeCapabilitiesWithFlags:]
+ -[DAExtension resume]
+ -[DAExtension setBluetoothRestorationID:]
+ -[DAExtension setProcessState:]
+ -[DAExtension suspendCapabilitiesWithFlags:]
+ -[DAExtension suspend]
+ -[DAExtensionCapability _reportEvent:]
+ -[DAExtensionCapability _reportEvent:].cold.1
+ -[DAExtensionCapability _reportEvent:].cold.2
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.1
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.2
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.3
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.4
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.5
+ -[DAExtensionEventLifecycle processState]
+ -[DAExtensionEventLifecycle setPreviousState:]
+ -[DAExtensionEventLifecycle setProcessState:]
+ -[DAExtensionSessionConfiguration bluetoothRestorationID]
+ -[DAExtensionSessionConfiguration eventFlags]
+ -[DAExtensionSessionConfiguration setBluetoothRestorationID:]
+ -[DAExtensionSessionConfiguration setEventFlags:]
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table31
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table80
+ _DAExtensionProcessStateToString
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _OBJC_IVAR_$_DAExtension._bluetoothRestorationID
+ _OBJC_IVAR_$_DAExtension._processMonitor
+ _OBJC_IVAR_$_DAExtension._processState
+ _OBJC_IVAR_$_DAExtensionEventLifecycle._processState
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._bluetoothRestorationID
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._eventFlags
+ ___21-[DAExtension launch]_block_invoke
+ ___21-[DAExtension launch]_block_invoke_2
+ ___21-[DAExtension resume]_block_invoke
+ ___21-[DAExtension resume]_block_invoke_2
+ ___22-[DAExtension suspend]_block_invoke
+ ___36-[DAExtension _startProcessMonitor:]_block_invoke
+ ___36-[DAExtension _startProcessMonitor:]_block_invoke_2
+ ___36-[DAExtension _startProcessMonitor:]_block_invoke_3
+ ___36-[DAExtension _startProcessMonitor:]_block_invoke_4
+ ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke
+ ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2
+ ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2.cold.1
+ ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke
+ ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2
+ ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2.cold.1
+ ___44-[DAExtension suspendCapabilitiesWithFlags:]_block_invoke
+ ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke
+ ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_2
+ ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_3
+ ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_4
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_2
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_3
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_3.cold.1
+ ___57-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]_block_invoke
+ ___57-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8
+ ___block_descriptor_44_e8_32bs_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8
+ ___block_descriptor_56_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.223
+ ___block_literal_global.229
+ ___block_literal_global.234
+ _objc_msgSend$_capabilitiesEnsureStartedWithFlags:error:
+ _objc_msgSend$_capabilitiesEnsureStoppedWithFlags:error:
+ _objc_msgSend$_extensionEnsureStartedWithError:
+ _objc_msgSend$_handleProcessStateUpdate:process:
+ _objc_msgSend$_removeCapabilityWithFlag:
+ _objc_msgSend$_startProcessMonitor:
+ _objc_msgSend$_suspend
+ _objc_msgSend$bluetoothRestorationID
+ _objc_msgSend$bundle
+ _objc_msgSend$capabilitiesForFlags:
+ _objc_msgSend$descriptor
+ _objc_msgSend$initWithDevice:eventType:extensionType:
+ _objc_msgSend$monitorWithConfiguration:
+ _objc_msgSend$setBluetoothRestorationID:
+ _objc_msgSend$setEvents:
+ _objc_msgSend$setPredicates:
+ _objc_msgSend$setPreviousState:
+ _objc_msgSend$setProcessState:
+ _objc_msgSend$setStateDescriptor:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setValues:
+ _objc_msgSend$startExtension:bundleID:type:
+ _objc_msgSend$taskState
- -[DAExtension _activateExtension:]
- -[DAExtension _capabilitiesEnsureStarted:]
- -[DAExtensionCapability _invalidated].cold.1
- -[DAExtensionCapability _invalidated].cold.2
- -[DAExtensionCapability _reportEventType:]
- -[DAExtensionCapability reportEvent:].cold.1
- -[DAExtensionCapability reportEvent:].cold.2
- -[DAExtensionEventLifecycle newState]
- -[DAExtensionSessionConfiguration bluetoothRestorationIdentifier]
- -[DAExtensionSessionConfiguration setBluetoothRestorationIdentifier:]
- GCC_except_table18
- GCC_except_table6
- _OBJC_IVAR_$_DAExtensionEventLifecycle._newState
- _OBJC_IVAR_$_DAExtensionSessionConfiguration._bluetoothRestorationIdentifier
- ___27-[DAExtension reportEvent:]_block_invoke.cold.1
- ___27-[DAExtension reportEvent:]_block_invoke.cold.2
- ___27-[DAExtension reportEvent:]_block_invoke.cold.3
- ___34-[DAExtension _activateExtension:]_block_invoke
- ___34-[DAExtension _activateExtension:]_block_invoke_2
- ___34-[DAExtension _activateExtension:]_block_invoke_3
- ___34-[DAExtension _activateExtension:]_block_invoke_4
- ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke
- ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_2
- ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3
- ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3.cold.1
- ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke.cold.1
- ___44-[DAExtension _handleCapabilityInvalidated:]_block_invoke.cold.1
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.220
- _objc_msgSend$_capabilitiesEnsureStarted:
- _objc_msgSend$bluetoothRestorationIdentifier
- _objc_msgSend$setBluetoothRestorationIdentifier:
- _objc_msgSend$startExtension:bundleID:
CStrings:
+ "### EnsureCapabilityStopped %@: %@"
+ "### Extension XPC failed for start capability: %@, %@"
+ "### Init failed to get capability flag from %@"
+ "### Init failed with multiple capability flags %@"
+ "### Init failed with nil capability identifier"
+ "### Init failed with nil device"
+ "### Init failed with nil extension identity"
+ "### Init with nil bundle identifier"
+ "### Init with nil device"
+ "### Init with nil extension identity"
+ "### Init with unknown extension type"
+ "### Launch: %@"
+ "### LaunchCapabilityWithFlag %@: %@"
+ "### Resume: %@"
+ "### ResumeCapabilityWithFlag %@: %@"
+ "### StartCapability failed with nil XPC connection"
+ "### StartProcessMonitor: %@"
+ "%@ <%p> %@"
+ "%@ <%p> '%@'"
+ "%@ releasing extension process assertion..."
+ "-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]"
+ "-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_3"
+ "-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]"
+ "-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]_block_invoke"
+ "-[DAExtension _extensionEnsureStartedWithError:]"
+ "-[DAExtension _handleProcessStateUpdate:process:]"
+ "-[DAExtension _removeCapabilityWithFlag:]"
+ "-[DAExtension _reportEvent:]"
+ "-[DAExtension _startProcessMonitor:]"
+ "-[DAExtension _startProcessMonitor:]_block_invoke"
+ "-[DAExtension _suspend]"
+ "-[DAExtension initWithDevice:identity:type:]"
+ "-[DAExtension launchCapabilitiesWithFlags:]_block_invoke"
+ "-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2"
+ "-[DAExtension launch]_block_invoke"
+ "-[DAExtension launch]_block_invoke_2"
+ "-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke"
+ "-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2"
+ "-[DAExtension resume]_block_invoke"
+ "-[DAExtension resume]_block_invoke_2"
+ "-[DAExtension suspendCapabilitiesWithFlags:]_block_invoke"
+ "-[DAExtensionCapability _reportEvent:]"
+ "-[DAExtensionCapability initWithIdentity:device:capabilityID:]"
+ "@\"RBSProcessMonitor\""
+ "ActivateExtension %@"
+ "Activating %@"
+ "Already monitoring PID: %d"
+ "Cleaning up existing process for PID: %d"
+ "Created: %@"
+ "Creating DAExtensionCapability..."
+ "EXCapabilities"
+ "EXExtensionCapabilities"
+ "Launching capability with flag: %@"
+ "Launching: %@"
+ "PrevState %@"
+ "ProcessState"
+ "Received event: %@, xpcConnection %@"
+ "Received process state update for %@, bundleID '%@', PID %d: %@ (%ld) -> %@ (%ld)"
+ "Removed %@ capability: %lu, %@"
+ "Reporting event: %@"
+ "Resume: %@"
+ "Resuming capability with flag: %@"
+ "Running"
+ "Started monitoring %@ process with PID: %d"
+ "Starting capability: %@"
+ "State %@"
+ "Stopping %@"
+ "Suspended"
+ "Suspending capability %@ on %@"
+ "T@\"NSString\",C,N,V_bluetoothRestorationID"
+ "TQ,N,V_eventFlags"
+ "TQ,N,V_previousState"
+ "TQ,N,V_processState"
+ "Verifying enrolledFlags %@, inFlags %@, capabilityFlag %@"
+ "_bluetoothRestorationID"
+ "_capabilitiesEnsureStartedWithFlags:error:"
+ "_capabilitiesEnsureStoppedWithFlags:error:"
+ "_eventFlags"
+ "_extensionEnsureStartedWithError:"
+ "_handleProcessStateUpdate:process:"
+ "_processMonitor"
+ "_processState"
+ "_removeCapabilityWithFlag:"
+ "_startProcessMonitor:"
+ "_suspend"
+ "bluetoothRestorationID"
+ "bundle"
+ "descriptor"
+ "eventFlags"
+ "exEvFl"
+ "exPS"
+ "exPSP"
+ "failed to create process monitor"
+ "invalid PID: %d"
+ "launchCapabilitiesWithFlags:"
+ "monitorWithConfiguration:"
+ "processState"
+ "resumeCapabilitiesWithFlags:"
+ "setBluetoothRestorationID:"
+ "setEventFlags:"
+ "setEvents:"
+ "setPredicates:"
+ "setPreviousState:"
+ "setProcessState:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "setValues:"
+ "startExtension:bundleID:type:"
+ "suspendCapabilitiesWithFlags:"
+ "taskState"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v32@0:8Q16^@24"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "v40@0:8@\"DADevice\"16@\"NSString\"24q32"
+ "v40@0:8@16@24q32"
- "%@ %@"
- "-[DAExtension _capabilitiesEnsureStarted:]"
- "-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3"
- "-[DAExtension _handleCapabilityInterrupted:]_block_invoke"
- "-[DAExtension _handleCapabilityInvalidated:]_block_invoke"
- "-[DAExtension reportEvent:]_block_invoke"
- "-[DAExtensionCapability _invalidated]"
- "-[DAExtensionCapability reportEvent:]"
- "Removed %@ capability (interrupted): %lu, %@"
- "Removed %@ capability (invalidated): %lu, %@"
- "T@\"NSString\",C,N,V_bluetoothRestorationIdentifier"
- "TQ,R,N,V_newState"
- "TQ,R,N,V_previousState"
- "Updated PID: %@"
- "_bluetoothRestorationIdentifier"
- "_capabilitiesEnsureStarted:"
- "_newState"
- "bluetoothRestorationIdentifier"
- "newState"
- "setBluetoothRestorationIdentifier:"
- "startExtension:bundleID:"
- "v32@0:8@\"DADevice\"16@\"NSString\"24"

```
