## MicroLocationUtilities

> `/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/Versions/A/MicroLocationUtilities`

```diff

-27.0.28.0.4
-  __TEXT.__text: 0x60b0
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x624
+27.0.28.0.6
+  __TEXT.__text: 0x6074
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_methlist: 0x8f8
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x313
   __TEXT.__gcc_except_tab: 0x90
   __TEXT.__oslogstring: 0x3a4
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_classname: 0xfb
-  __TEXT.__objc_methname: 0xfb7
+  __TEXT.__objc_methname: 0xfd2
   __TEXT.__objc_methtype: 0x56d
   __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0xc8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x590
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x1300
+  __AUTH_CONST.__objc_const: 0xde8
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x34

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04AA8516-9568-389A-9191-D0432F5E3C8B
-  Functions: 200
-  Symbols:   616
-  CStrings:  376
+  UUID: 678A1002-6B09-3830-9A0E-540D6A0915CB
+  Functions: 209
+  Symbols:   635
+  CStrings:  377
 
Symbols:
+ +[ULPlatform isInternalInstall].cold.1
+ +[ULPlatform isLimitedMiloUsagePlatform]
+ +[ULPlatform isRunningInXCTestEnvironment].cold.1
+ +[ULScheduler globalAsyncScheduler].cold.1
+ +[ULScheduler immediateScheduler].cold.1
+ +[ULUserNotification _queue].cold.1
+ -[ULDarwinNotificationHelper _handleDarwinNotificationCallback:].cold.1
+ -[ULDarwinNotificationHelper _handleDarwinNotificationCallback:].cold.2
+ _MGGetProductType
+ __55-[ULDarwinNotificationHelper stateForNotificationName:]_block_invoke.cold.1
+ __64-[ULDarwinNotificationHelper removeObserverForNotificationName:]_block_invoke.cold.1
+ __64-[ULDarwinNotificationHelper removeObserverForNotificationName:]_block_invoke.cold.2
+ __64-[ULDarwinNotificationHelper removeObserverForNotificationName:]_block_invoke.cold.3
+ __69-[ULDarwinNotificationHelper addObserverForNotificationName:handler:]_block_invoke.cold.1
+ __69-[ULDarwinNotificationHelper addObserverForNotificationName:handler:]_block_invoke.cold.2
+ __69-[ULDarwinNotificationHelper addObserverForNotificationName:handler:]_block_invoke.cold.3
+ initRadarComponent.cold.1
+ initRadarDraft.cold.1
+ initTapToRadarService.cold.1
CStrings:
+ "isLimitedMiloUsagePlatform"

```
