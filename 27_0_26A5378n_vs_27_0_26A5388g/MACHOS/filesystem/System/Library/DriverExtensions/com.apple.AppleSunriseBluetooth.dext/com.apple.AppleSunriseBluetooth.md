## com.apple.AppleSunriseBluetooth

> `/System/Library/DriverExtensions/com.apple.AppleSunriseBluetooth.dext/com.apple.AppleSunriseBluetooth`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-110.0.0.0.0
-  __TEXT.__text: 0x2ed60
+112.0.0.0.0
+  __TEXT.__text: 0x2ef68
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__cstring: 0xb339
-  __TEXT.__const: 0x1580
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__cstring: 0xb3e9
+  __TEXT.__const: 0x15b0
+  __TEXT.__unwind_info: 0x870
   __TEXT.__oslogstring: 0x251d
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__osclassinfo: 0x60

   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit
   - /System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 940
-  Symbols:   1190
-  CStrings:  1654
+  Functions: 941
+  Symbols:   1191
+  CStrings:  1659
 
Symbols:
+ _btmtk_pcie_handle_dma_hang
Functions:
~ __ZN30AppleSunriseBluetoothIPCClient26ReadCompletionNotificationEPhm : 1824 -> 1828
~ _btmtk_pcie_patch_dl_timer_handler : 668 -> 716
~ _btmtk_pcie_ipc_check_dma_hang : 376 -> 716
+ _btmtk_pcie_handle_dma_hang
~ _btmtk_pcie_ipc_status_timer_cback : 228 -> 272
CStrings:
+ "%s: 5ms late, addr = %lx, value= %lu"
+ "%s: BTDMA hang detected, need whole chip reset"
+ "%s: BTDMA hang, triggering BT_DMA_Hang fault report"
+ "%s: addr = %lx, value= %lu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7BiDgn/Sources/AppleSunriseBluetooth_driverkit/Sunrise/dale/gl_device.cpp"
+ "8.0.2026052201"
+ "BT_DMA_Hang"
+ "btmtk_pcie_handle_dma_hang"
- "%s: need whole chip reset"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c5QNkE/Sources/AppleSunriseBluetooth_driverkit/Sunrise/dale/gl_device.cpp"
- "8.0.2024081401"
```
