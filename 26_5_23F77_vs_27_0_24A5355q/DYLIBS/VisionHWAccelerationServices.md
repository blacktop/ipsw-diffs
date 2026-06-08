## VisionHWAccelerationServices

> `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices`

```diff

-4.3.7.0.0
-  __TEXT.__text: 0x1dd58
-  __TEXT.__auth_stubs: 0xc00
+4.4.9.0.0
+  __TEXT.__text: 0x205ec
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0xf81
-  __TEXT.__gcc_except_tab: 0x149c
-  __TEXT.__oslogstring: 0x128c
-  __TEXT.__cstring: 0x11c9
-  __TEXT.__unwind_info: 0x948
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0x3c1
-  __TEXT.__objc_methtype: 0x1bf
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1c8
+  __TEXT.__const: 0x1118
+  __TEXT.__gcc_except_tab: 0x158c
+  __TEXT.__oslogstring: 0x1859
+  __TEXT.__cstring: 0x12e8
+  __TEXT.__unwind_info: 0x950
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x610
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xcf8
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x358
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x20
+  __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0xc0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x448
+  __DATA.__bss: 0x3d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58FE063A-59D5-3C6B-8962-7803B10DB98D
-  Functions: 448
-  Symbols:   270
-  CStrings:  385
+  UUID: F1428C0D-6C30-33B4-BF80-EA5CB8C14285
+  Functions: 455
+  Symbols:   266
+  CStrings:  333
 
Symbols:
+ _audit_token_to_pid
+ _dispatch_async
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_release_x28
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _xpc_connection_cancel
- __ZNSt3__115recursive_mutex4lockEv
- __ZNSt3__115recursive_mutex6unlockEv
- __ZNSt3__115recursive_mutexC1Ev
- __ZNSt3__115recursive_mutexD1Ev
- __ZSt7nothrow
- __Znwm
- __ZnwmRKSt9nothrow_t
- _del_curterm
- _objc_release_x26
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _set_curterm
- _setupterm
- _tigetnum
CStrings:
+ "+++ Program loader destructor called +++"
+ "AppStateMonitor: notify_suspend called with app status = %d"
+ "Application PID=%d terminated, removed RunningBoardServices notification listener (OSStatus %d)"
+ "Cancelling all connections for PID %d:"
+ "Client ID %d not found in map"
+ "Client ID cannot be 0"
+ "End of status_callback."
+ "Error while starting the one-shot timer for tearing down ISP device -- was the timer active already?"
+ "Failed to remove the CMNotificationCenter listener for PID %d (OSStatus %d)"
+ "HasAppleNeuralEngine"
+ "HxISPDevice 0x%p: Removing device notification listener for device %p"
+ "HxISPDevice class instance at %p released"
+ "ISP Device no longer available, likely due to device sleep. Check the system logs to confirm"
+ "ISP Device unrecoverable error detected, this could indicate a Firmware crash -- check ISP FW logs for assertions"
+ "PID == 0 encountered during connection removal"
+ "PID == 0 encountered during connection update -- THIS SHOULDN'T HAPPEN"
+ "Removing connection %p from PID %d"
+ "SHT_AARCH64_AUTH_RELR"
+ "SHT_AARCH64_MEMTAG_GLOBALS_DYNAMIC"
+ "SHT_AARCH64_MEMTAG_GLOBALS_STATIC"
+ "SHT_CREL"
+ "SHT_HEXAGON_ATTRIBUTES"
+ "SHT_LLVM_BB_ADDR_MAP_V0"
+ "SHT_LLVM_LTO"
+ "SHT_LLVM_OFFLOADING"
+ "Section has been stripped from the object file"
+ "Unable to determine PID from XPC connection -- PID 0 is not supported"
+ "VisionHWAServer AppStateMonitor for process: %{private}@, pid: %d, notified of state transition: %d -> %d"
+ "VisionHWAServer: pid %d not found in connection map"
+ "VisionHWAServer: setting LACC mode to 0 for DesGen"
+ "VisionHWAServer: updatePidToConnections() tried to remove non-existing XPC connection for PID %d"
+ "XPC_ERROR_CONNECTION_INTERRUPTED"
+ "XPC_ERROR_CONNECTION_INVALID"
+ "XPC_ERROR_TERMINATION_IMMINENT"
+ "checking client ID %d for connections"
+ "client ID %d owns connection %p -- releasing buffers and destroying client info"
+ "cmd_client_id != 0"
+ "dispatching cancelAllClientConnections()"
+ "executing cancelAllClientConnections()"
+ "false"
+ "pid has %zu connections associated"
+ "retiring process monitor for PID %d"
+ "status_callback: Client with PID=%d was %s"
+ "suspended"
+ "terminated"
+ "updatePidToConnection(%p, %s)"
- "#16@0:8"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"RBSProcessHandle\""
- "@\"RBSProcessMonitor\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AppStateMonitor"
- "AppStateMonitorProtocol"
- "Application PID=%d terminated with status %d"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_monitoredProcessName"
- "TQ,R"
- "Ti,R"
- "Ti,R,V_monitoredPID"
- "VisionHWAServer: numClients is zero!!"
- "VisionHWAServer: pid not exist!!"
- "VisionHWAServer: previousState: %d, state: %d, name: %{private}@, pid: %d"
- "VisionHWAServer: received release command but numClients is already zero!!"
- "Vv16@0:8"
- "]"
- "^{_NSZone=}16@0:8"
- "_latestState"
- "_lock"
- "_monitoredPID"
- "_monitoredProcessName"
- "_process:didUpdateState:"
- "_processHandle"
- "_processMonitor"
- "_processNameInternal"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "colors"
- "conformsToProtocol:"
- "containsObject:"
- "currentAppState"
- "dealloc"
- "debugDescription"
- "description"
- "descriptor"
- "dictionaryWithObjects:forKeys:count:"
- "endowmentNamespaces"
- "handleForIdentifier:error:"
- "hash"
- "i16@0:8"
- "identifierWithPid:"
- "init"
- "initWithPID:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "monitorForDeath:"
- "monitorWithConfiguration:"
- "monitoredPID"
- "monitoredProcessName"
- "name"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "predicateMatchingIdentifier:"
- "previousState"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setPredicates:"
- "setStateDescriptor:"
- "setUpdateHandler:"
- "setValues:"
- "state"
- "superclass"
- "taskState"
- "v16@0:8"
- "v32@0:8@16@24"
- "zone"
- "{optional<UnifiedAppState>=\"\"(?=\"__null_state_\"c\"__val_\"{UnifiedAppState=\"processState\"@\"RBSProcessState\"\"appState\"i})\"__engaged_\"B}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
