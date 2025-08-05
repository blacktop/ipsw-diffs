## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

-719.1.0.0.0
-  __TEXT.__text: 0x3bbc
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x324
+728.0.0.0.0
+  __TEXT.__text: 0x4124
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0x6c9
-  __TEXT.__cstring: 0x26b
+  __TEXT.__oslogstring: 0x722
+  __TEXT.__cstring: 0x2b1
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__objc_methname: 0xe58
-  __TEXT.__objc_classname: 0x8a
-  __TEXT.__objc_methtype: 0x387
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x178
-  __DATA_CONST.__cfstring: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__objc_methname: 0x1036
+  __TEXT.__objc_classname: 0x9b
+  __TEXT.__objc_methtype: 0x3ae
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6a8
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_const: 0x818
+  __DATA.__objc_selrefs: 0x540
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
+  - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F6554AF-7062-3E6F-B7A6-E53DD020B1F3
-  Functions: 71
-  Symbols:   133
-  CStrings:  318
+  UUID: 38AD4E22-9F7B-3F81-AB8F-70B06D76FD33
+  Functions: 88
+  Symbols:   137
+  CStrings:  353
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_RBDevice
+ _dispatch_source_cancel
+ _dispatch_time
CStrings:
+ "#ISGPUIDleTimer create transaction"
+ "#ISGPUIDleTimer purge"
+ "#ISGPUIDleTimer tickle"
+ "@\"ISGPUIdleTimer\""
+ "ISGPUIdleTimer"
+ "ISGPUIdleTimer.m"
+ "Stating IconServices agent service with name: %s safe: %d"
+ "T@\"ISGPUIdleTimer\",R,V_gpuIdleTimer"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_cleanupQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "TQ,N,V_generation"
+ "T{os_unfair_lock_s=I},N,V_transactionLock"
+ "_cleanupQueue"
+ "_generation"
+ "_gpuIdleTimer"
+ "_timer"
+ "_timerFiredForGeneration:"
+ "_transactionLock"
+ "armTimer"
+ "cleanupQueue"
+ "com.apple.iconservices.cleanup"
+ "com.apple.iconservicesagent.gpu-idle-timer"
+ "currentHandler"
+ "dealloc"
+ "generation"
+ "gpuIdleTimer"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithQueue:"
+ "need a queue"
+ "purgeResources"
+ "safeBoot"
+ "setGeneration:"
+ "setTimer:"
+ "setTransaction:"
+ "setTransactionLock:"
+ "timer"
+ "transactionLock"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8@16"
- "@\"NSOperationQueue\""
- "Stating IconServices agent service with name: %s"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_cuiCleanupQueue"
- "_cuiCleanupQueue"
- "_operationQueue"
- "com.apple.iconservices.cuicleanup"
- "cuiCleanupQueue"

```
