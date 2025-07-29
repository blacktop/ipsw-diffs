## ContextSync

> `/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync`

```diff

-123.2.8.0.0
+123.5.23.1.0
   __TEXT.__text: 0xec64
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x7b4

   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x390
   __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methname: 0x281a
+  __TEXT.__objc_methname: 0x282e
   __TEXT.__objc_methtype: 0xee7
   __TEXT.__objc_stubs: 0x1b60
   __DATA_CONST.__got: 0x38

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x12f0
   __DATA_CONST.__objc_selrefs: 0x7f0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0x470
   __AUTH_CONST.__const: 0x60

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x240
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x80

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2E64F69-60DD-3AB2-9482-24201FC341AD
+  UUID: D6B1D024-51B8-3CD0-BABE-8600117ABA2A
   Functions: 281
   Symbols:   1093
-  CStrings:  718
+  CStrings:  719
 
Symbols:
+ ___102-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:withError:]_block_invoke.63
+ ___83-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:]_block_invoke.70
+ ___83-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:]_block_invoke.70.cold.1
+ ___89-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDevices:withError:]_block_invoke.69
+ ___92-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:]_block_invoke.66
+ ___92-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:]_block_invoke.66.cold.1
+ ___93-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:withError:]_block_invoke.68
+ ___98-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDevices:withError:]_block_invoke.65
- ___102-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:withError:]_block_invoke.62
- ___83-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:]_block_invoke.69
- ___83-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:]_block_invoke.69.cold.1
- ___89-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDevices:withError:]_block_invoke.68
- ___92-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:]_block_invoke.65
- ___92-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDeviceTypes:]_block_invoke.65.cold.1
- ___93-[ContextSyncClient unregisterForUpdates:withIdentifier:forUseCase:forDeviceTypes:withError:]_block_invoke.67
- ___98-[ContextSyncClient registerForUpdates:withIdentifier:forUseCase:shouldWake:forDevices:withError:]_block_invoke.64
CStrings:
+ "T@\"NSString\",?,R,C"

```
