## Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

-376.0.3.0.0
-  __TEXT.__text: 0x104c
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__cstring: 0x1d5
-  __TEXT.__oslogstring: 0xd5
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x39d
-  __TEXT.__objc_methtype: 0x18d
-  __TEXT.__unwind_info: 0x84
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x1c0
+376.40.6.0.0
+  __TEXT.__text: 0x5fc
+  __TEXT.__auth_stubs: 0x170
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__objc_methlist: 0x74
+  __TEXT.__oslogstring: 0x4f
+  __TEXT.__cstring: 0xf0
+  __TEXT.__objc_classname: 0x4e
+  __TEXT.__objc_methname: 0x2b7
+  __TEXT.__objc_methtype: 0x10c
+  __TEXT.__unwind_info: 0x60
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x560
-  __DATA.__objc_selrefs: 0xe0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x518
+  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_classrefs: 0x28
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D80F6C7C-16B3-3FA7-AE57-332A9B361349
-  Functions: 20
-  Symbols:   64
-  CStrings:  127
+  UUID: 7ECB3023-7B03-3649-B287-23655FA8B521
+  Functions: 8
+  Symbols:   45
+  CStrings:  87
 
Symbols:
+ _SavageCamInterfaceColdBootPowerCycle
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _SavageCamInterfaceForgetISPFirmware
- __Block_object_dispose
- __NSConcreteStackBlock
- __Unwind_Resume
- ___objc_personality_v0
- __os_log_debug_impl
- __os_log_error_impl
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_alloc
- _objc_release
- _objc_release_x8
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x20
- _objc_retain_x22
CStrings:
+ "%s: SavageCamInterfaceColdBootPowerCycle"
+ "-[CameradReloaderController powerCycleSensor:]"
+ "SavageCamInterfaceColdBootPowerCycle failed: %d"
+ "powerCycleSensor:"
- "%s: SavageCamInterfaceForgetISPFirmware"
- "-[CameradReloaderController forgetISPFirmware:]"
- "-[CameradReloaderController reopenSavageCamInterface:]"
- "B32@0:8@16^@24"
- "CoreRepairHelperProtocol"
- "Daemon control operation failed."
- "Daemon control timed out."
- "Error:%@"
- "Forget ISP Firmware"
- "Reload Camera Daemon"
- "Reopen SavageCamInterface"
- "SavageCamInterfaceForgetISPFirmware failed: %d"
- "Unload Camera Daemon"
- "action"
- "com.apple.appleh16camerad"
- "com.apple.corerepair"
- "daemonControl returns %d. Results: %@"
- "daemonControl:withReply:"
- "doDaemonControl:error:"
- "forgetISPFirmware:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "load"
- "name"
- "remoteObjectProxyWithErrorHandler:"
- "reopenSavageCamInterface:"
- "resume"
- "seal:withReply:"
- "setRemoteObjectInterface:"
- "unload"
- "v16@?0@\"NSError\"8"
- "v20@?0B8@\"NSDictionary\"12"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSDictionary\">24"
- "v32@0:8@16@?24"

```
