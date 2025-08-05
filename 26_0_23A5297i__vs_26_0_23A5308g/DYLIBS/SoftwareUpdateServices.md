## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.0.24.0.0
-  __TEXT.__text: 0xaf8ac
+950.0.28.0.2
+  __TEXT.__text: 0xaefd8
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xac0c
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x20c51
-  __TEXT.__gcc_except_tab: 0x1014
-  __TEXT.__oslogstring: 0xd81
+  __TEXT.__objc_methlist: 0xac24
+  __TEXT.__const: 0x308
+  __TEXT.__cstring: 0x212cc
+  __TEXT.__gcc_except_tab: 0xff0
+  __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3160
+  __TEXT.__unwind_info: 0x3150
   __TEXT.__objc_classname: 0xf05
-  __TEXT.__objc_methname: 0x18b72
+  __TEXT.__objc_methname: 0x18bfa
   __TEXT.__objc_methtype: 0x344d
-  __TEXT.__objc_stubs: 0x141a0
+  __TEXT.__objc_stubs: 0x141e0
   __DATA_CONST.__got: 0xd98
   __DATA_CONST.__const: 0x2900
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5be0
+  __DATA_CONST.__objc_selrefs: 0x5bf0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x12b80
-  __AUTH_CONST.__objc_const: 0x157b0
+  __AUTH_CONST.__cfstring: 0x12f80
+  __AUTH_CONST.__objc_const: 0x157e0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x94c
+  __DATA.__objc_ivar: 0x950
   __DATA.__data: 0xe98
-  __DATA.__bss: 0xe8
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x1658
-  __DATA_DIRTY.__bss: 0x1e8
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A4D3AA0A-A082-36BA-A51A-E9872D8F8AB7
-  Functions: 4471
-  Symbols:   14830
-  CStrings:  10076
+  UUID: D1B1EC7E-78DC-31DC-B4E4-EE97F3A18047
+  Functions: 4463
+  Symbols:   14817
+  CStrings:  10116
 
Symbols:
+ -[SUDescriptor setTotalSnapshotRequiredFreeSpace:]
+ -[SUDescriptor totalSnapshotRequiredFreeSpace]
+ _OBJC_IVAR_$_SUDescriptor._totalSnapshotRequiredFreeSpace
+ ___32-[SUInstaller installCompleted:]_block_invoke.384
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.385
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.391
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.532
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.536
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.494
+ ___block_literal_global.293
+ ___block_literal_global.304
+ ___block_literal_global.309
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.324
+ ___block_literal_global.329
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.360
+ ___block_literal_global.396
+ ___block_literal_global.398
+ ___block_literal_global.404
+ ___block_literal_global.410
+ ___block_literal_global.432
+ ___block_literal_global.463
+ ___block_literal_global.510
+ ___block_literal_global.535
+ ___block_literal_global.540
+ ___block_literal_global.567
+ ___block_literal_global.583
+ ___block_literal_global.593
+ ___block_literal_global.615
+ ___block_literal_global.625
+ _objc_msgSend$setTotalSnapshotRequiredFreeSpace:
+ _objc_msgSend$totalSnapshotRequiredFreeSpace
+ _totalSnapshotRequiredFreeSpace
- -[SUInstallationConstraintMonitorForBatteryDiskAndKeybag dealloc].cold.1
- -[SUInstallationConstraintMonitorForBatteryDiskAndKeybag initOnQueue:withDownload:installOptions:pollDuration:keybag:].cold.1
- -[SUInstallationConstraintMonitorForBatteryDiskAndKeybag initOnQueue:withDownload:installOptions:pollDuration:keybag:].cold.2
- -[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:].cold.1
- -[SUInstallationConstraintMonitorWombat _wombatEnabledDidChange:].cold.2
- -[_SUInstallationConstraintBlockObserverToken dealloc].cold.1
- -[_SUInstallationConstraintBlockObserverToken initWithObserver:].cold.1
- -[_SUInstallationConstraintBlockObserverToken invalidate].cold.1
- ___118-[SUInstallationConstraintMonitorForBatteryDiskAndKeybag initOnQueue:withDownload:installOptions:pollDuration:keybag:]_block_invoke.cold.1
- ___32-[SUInstaller installCompleted:]_block_invoke.381
- ___32-[SUInstaller installCompleted:]_block_invoke_2.382
- ___32-[SUInstaller installCompleted:]_block_invoke_3.388
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.529
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.533
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.491
- ___block_literal_global.287
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.311
- ___block_literal_global.316
- ___block_literal_global.321
- ___block_literal_global.326
- ___block_literal_global.331
- ___block_literal_global.336
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.357
- ___block_literal_global.393
- ___block_literal_global.401
- ___block_literal_global.407
- ___block_literal_global.429
- ___block_literal_global.460
- ___block_literal_global.507
- ___block_literal_global.532
- ___block_literal_global.537
- ___block_literal_global.564
- ___block_literal_global.580
- ___block_literal_global.590
- ___block_literal_global.612
- ___block_literal_global.622
CStrings:
+ "-[SUNetworkMonitor displayStatusChanged:status:]_block_invoke"
+ "Ignoring status change notification for context %@ which is NOT the current context for cellular data. The cellular data context is %@"
+ "Received status change for context: %@ which is the current preferred context for cellular data. New isRoaming: %d"
+ "TQ,N,V_totalSnapshotRequiredFreeSpace"
+ "_totalSnapshotRequiredFreeSpace"
+ "setTotalSnapshotRequiredFreeSpace:"
+ "totalSnapshotRequiredFreeSpace"

```
