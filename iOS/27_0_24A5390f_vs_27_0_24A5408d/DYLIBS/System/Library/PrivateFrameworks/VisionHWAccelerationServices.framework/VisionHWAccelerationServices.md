## VisionHWAccelerationServices

> `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices`

```diff

-4.4.10.0.0
-  __TEXT.__text: 0x2049c
+4.4.12.0.0
+  __TEXT.__text: 0x209c4
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x1118
-  __TEXT.__gcc_except_tab: 0x1570
-  __TEXT.__oslogstring: 0x1859
-  __TEXT.__cstring: 0x12db
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__const: 0x1120
+  __TEXT.__gcc_except_tab: 0x157c
+  __TEXT.__oslogstring: 0x1a15
+  __TEXT.__cstring: 0x12dd
+  __TEXT.__unwind_info: 0x958
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xcf8
+  __AUTH_CONST.__const: 0xd38
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x358
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0xc0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x3d8
+  __DATA.__bss: 0x410
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 457
-  Symbols:   266
-  CStrings:  312
+  Functions: 460
+  Symbols:   272
+  CStrings:  320
 
Symbols:
+ _VisionHWServerStop
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ __ZNSt3__19to_stringEj
+ _dispatch_source_cancel
+ _dispatch_sync
+ _pthread_main_np
+ _xpc_retain
- _VisionHWAccelerationServicesStart
CStrings:
+ "**************** Launching VisionHWAccelerationServices framework version %{public}s *****************"
+ "."
+ "Empty connections list for PID %d"
+ "Listing all connections for PID %d:"
+ "Releasing os_transaction during Shutdown()"
+ "Unexpected entries in pidToConnections map, should be empty. Check code for inconsistent connection clean-up."
+ "VisionHWAServer: Shutdown begin"
+ "VisionHWAServer: Shutdown complete"
+ "VisionHWAServer: Shutdown() called off the main thread -- ignoring to avoid dispatch_sync self-deadlock"
+ "VisionHWAServer: calling VisionHWServerStart()"
+ "VisionHWAServer: calling VisionHWServerStop()"
+ "VisionHWAServer: destructor reached with %zu live client(s) and no Shutdown() -- exit path did not quiesce the service"
+ "XPC connection %p was not removed properly"
- "**************** VisionHWAServer has been disabled in mediaserverd"
- "**************** VisionHWAServer has been disabled in visionserverd"
- "Cancelling all connections for PID %d:"
- "Releasing os_transaction inside DTOR -- visionhwserverd is TERMINATING"
- "VisionHWAServer: VisionHWAccelerationServicesStart is invoked."
```
