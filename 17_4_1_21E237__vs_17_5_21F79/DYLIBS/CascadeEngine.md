## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-123.5.23.1.0
-  __TEXT.__text: 0x17ab0
-  __TEXT.__auth_stubs: 0x5d0
+123.9.0.1.0
+  __TEXT.__text: 0x17dac
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0xb74
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x63c
-  __TEXT.__oslogstring: 0x1f8e
+  __TEXT.__oslogstring: 0x20fc
   __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__unwind_info: 0x544
-  __TEXT.__objc_classname: 0x2f7
-  __TEXT.__objc_methname: 0x3466
-  __TEXT.__objc_methtype: 0xe5a
-  __TEXT.__objc_stubs: 0x2d60
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_classname: 0x2f9
+  __TEXT.__objc_methname: 0x34f6
+  __TEXT.__objc_methtype: 0xe77
+  __TEXT.__objc_stubs: 0x2e00
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x21d0
-  __DATA_CONST.__objc_selrefs: 0xc30
+  __DATA_CONST.__objc_const: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0xc58
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x210
+  __DATA_CONST.__objc_classrefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x204
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x14
+  __DATA_DIRTY.__const: 0x60
+  __DATA_DIRTY.__objc_const: 0x4c8
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47200775-E440-328D-91F4-2A4B0CFF28E2
-  Functions: 458
-  Symbols:   1869
-  CStrings:  976
+  UUID: A1F41E65-00F1-3013-9DA9-4A0F13404CD2
+  Functions: 460
+  Symbols:   1883
+  CStrings:  988
 
Symbols:
+ _OBJC_CLASS_$_BMDeviceMetadataUtils
+ _OBJC_CLASS_$__PASSimpleCoalescingTimer
+ _OBJC_IVAR_$_CCSetStoreUpdateService._eagerExitTimer
+ ___41-[CCSetStoreUpdateService initWithQueue:]_block_invoke
+ ___62-[CCSetStoreUpdateService listener:shouldAcceptNewConnection:]_block_invoke
+ _objc_msgSend$cancelPendingOperations
+ _objc_msgSend$initWithQueue:operation:
+ _objc_msgSend$platform
+ _objc_msgSend$runAfterDelaySeconds:coalescingBehavior:
+ _objc_msgSend$setInvalidationHandler:
+ _xpc_transaction_exit_clean
CStrings:
+ "\x05"
+ "@\"_PASSimpleCoalescingTimer\""
+ "CCSetStoreUpdateService is running on HomePod, will attempt to eager exit after handling each connection"
+ "Connection from %{public}@(%d) was invalidated, will attempt to eager exit in %lu seconds if there are no more connections"
+ "Eager-exit coalescing timer fired, will attempt to exit when clean"
+ "Resetting eager-exit timer for incoming connection from %{public}@(%d)"
+ "_eagerExitTimer"
+ "cancelPendingOperations"
+ "initWithQueue:operation:"
+ "platform"
+ "runAfterDelaySeconds:coalescingBehavior:"
+ "setInvalidationHandler:"

```
