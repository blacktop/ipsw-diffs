## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-30.54.2.1.1
-  __TEXT.__text: 0x3d4b0
+30.58.1.0.0
+  __TEXT.__text: 0x3de40
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x4f94
+  __TEXT.__objc_methlist: 0x4fcc
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0xef0
-  __TEXT.__cstring: 0xb228
-  __TEXT.__unwind_info: 0xfe0
+  __TEXT.__gcc_except_tab: 0x14e4
+  __TEXT.__cstring: 0xb253
+  __TEXT.__unwind_info: 0x1078
   __TEXT.__objc_classname: 0x63b
-  __TEXT.__objc_methname: 0xaa67
+  __TEXT.__objc_methname: 0xab06
   __TEXT.__objc_methtype: 0x13eb
-  __TEXT.__objc_stubs: 0x56a0
+  __TEXT.__objc_stubs: 0x56c0
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xe38
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22b0
+  __DATA_CONST.__objc_selrefs: 0x22c8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x128
   __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2180
-  __AUTH_CONST.__objc_const: 0x9100
+  __AUTH_CONST.__cfstring: 0x2160
+  __AUTH_CONST.__objc_const: 0x9110
   __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x884
+  __DATA.__objc_ivar: 0x888
   __DATA.__data: 0xc58
   __DATA.__common: 0x8
   __DATA.__bss: 0x38

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 476D8F53-6377-34C7-9066-376A6B79F824
-  Functions: 2100
-  Symbols:   6355
-  CStrings:  3902
+  UUID: 60FFA0D0-1F12-3F50-A92F-18FA44C2D158
+  Functions: 2103
+  Symbols:   6378
+  CStrings:  3903
 
Symbols:
+ -[AADeviceBatteryInfo optimizedBatteryChargingCapability]
+ -[AADeviceBatteryInfo setOptimizedBatteryChargingCapability:]
+ -[AADeviceBatteryInfo updateWithPairedDevice:]
+ -[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]
+ -[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table4
+ GCC_except_table44
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table61
+ _OBJC_IVAR_$_AADeviceBatteryInfo._optimizedBatteryChargingCapability
+ ___62-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]_block_invoke
+ ___62-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]_block_invoke_2
+ ___62-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]_block_invoke_2.cold.1
+ ___65-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]_block_invoke
+ ___65-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2
+ ___65-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2.cold.1
+ _objc_msgSend$_syncXPCFetchAADeviceBatteryInfoForAddress:
+ _objc_msgSend$_syncXPCFetchAADeviceBatteryInfoForIdentifier:
+ _objc_msgSend$enableHeartRateMonitor
- -[AADeviceManager _activateXPC:reactivate:].cold.1
- -[AASystemStateMonitor activeHRMDeviceChanged:]
- GCC_except_table48
- GCC_except_table52
- GCC_except_table56
- ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke
- ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2
- ___54-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2.cold.1
- ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke
- ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2
- ___57-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2.cold.1
- _objc_msgSend$setChargingReminderCapability:
- _objc_msgSend$setCoreBluetoothDevice:
CStrings:
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]"
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]_block_invoke"
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:]_block_invoke_2"
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]"
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]_block_invoke"
+ "-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2"
+ "TB,N,V_connected"
+ "TB,N,V_paired"
+ "_syncXPCFetchAADeviceBatteryInfoForAddress:"
+ "_syncXPCFetchAADeviceBatteryInfoForIdentifier:"
+ "assetManagerShowDownloadNotificationForBTAddress:completionHandler:"
+ "obcc"
+ "updateWithPairedDevice:"
- "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]"
- "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke"
- "-[AADeviceManager fetchAADeviceBatteryInfoForAddress:]_block_invoke_2"
- "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]"
- "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke"
- "-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:]_block_invoke_2"
- "OBCc"
- "Tc,N,V_connected"
- "Tc,N,V_paired"
- "activeHRMDeviceChanged:"
- "cRcp"

```
