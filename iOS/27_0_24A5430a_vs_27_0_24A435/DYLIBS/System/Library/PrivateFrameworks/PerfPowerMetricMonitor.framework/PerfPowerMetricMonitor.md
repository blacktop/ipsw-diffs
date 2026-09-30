## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

 3486.2.4.0.0
-  __TEXT.__text: 0x19d90
-  __TEXT.__objc_methlist: 0x187c
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x998
-  __TEXT.__cstring: 0x1308
-  __TEXT.__oslogstring: 0x1c3b
+  __TEXT.__text: 0x1a974
+  __TEXT.__objc_methlist: 0x1954
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0x9a8
+  __TEXT.__cstring: 0x1444
+  __TEXT.__oslogstring: 0x1e7f
   __TEXT.__ustring: 0x77e
   __TEXT.__unwind_info: 0x510
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_selrefs: 0xfd0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__objc_arraydata: 0x328
   __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x1640
-  __AUTH_CONST.__objc_const: 0x2898
+  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__objc_const: 0x2a48
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x310
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x280
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x300
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x68

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 674
-  Symbols:   1518
-  CStrings:  334
+  Functions: 693
+  Symbols:   1563
+  CStrings:  343
 
Symbols:
+ -[PPSMetricCollection brightnessX]
+ -[PPSMetricCollection displayAPLX]
+ -[PPSMetricCollection displayCostX]
+ -[PPSMetricCollection displayEnergyX]
+ -[PPSMetricCollection displayFPSX]
+ -[PPSMetricCollection displayPowerX]
+ -[PPSMetricCollection scanoutFPSX]
+ -[PPSMetricCollection setBrightnessX:]
+ -[PPSMetricCollection setDisplayAPLX:]
+ -[PPSMetricCollection setDisplayCostX:]
+ -[PPSMetricCollection setDisplayEnergyX:]
+ -[PPSMetricCollection setDisplayFPSX:]
+ -[PPSMetricCollection setDisplayPowerX:]
+ -[PPSMetricCollection setScanoutFPSX:]
+ -[PPSProcessMetricCollection displayPowerX]
+ -[PPSProcessMetricCollection setDisplayPowerX:]
+ -[PPSProcessMetricCollection setWeightOnScreenX:]
+ -[PPSProcessMetricCollection weightOnScreenX]
+ _OBJC_IVAR_$_PPSMetricCollection._brightnessX
+ _OBJC_IVAR_$_PPSMetricCollection._displayAPLX
+ _OBJC_IVAR_$_PPSMetricCollection._displayCostX
+ _OBJC_IVAR_$_PPSMetricCollection._displayEnergyX
+ _OBJC_IVAR_$_PPSMetricCollection._displayFPSX
+ _OBJC_IVAR_$_PPSMetricCollection._displayPowerX
+ _OBJC_IVAR_$_PPSMetricCollection._scanoutFPSX
+ _OBJC_IVAR_$_PPSProcessMetricCollection._displayPowerX
+ _OBJC_IVAR_$_PPSProcessMetricCollection._weightOnScreenX
+ _objc_msgSend$brightnessPercentX
+ _objc_msgSend$brightnessX
+ _objc_msgSend$displayAPLX
+ _objc_msgSend$displayCostX
+ _objc_msgSend$displayEnergyX
+ _objc_msgSend$displayFPSX
+ _objc_msgSend$displayPowerX
+ _objc_msgSend$isV68
+ _objc_msgSend$scanoutFPSX
+ _objc_msgSend$setBrightnessX:
+ _objc_msgSend$setDisplayAPLX:
+ _objc_msgSend$setDisplayCostX:
+ _objc_msgSend$setDisplayEnergyX:
+ _objc_msgSend$setDisplayFPSX:
+ _objc_msgSend$setDisplayPowerX:
+ _objc_msgSend$setScanoutFPSX:
+ _objc_msgSend$setWeightOnScreenX:
+ _objc_msgSend$weightOnScreenX
CStrings:
+ "\nDisplay X Power    %8.3f W   %@\nDisplay X APL      %8.3f     %@\nDisplay X Cost     %8.3f     %@\nDisplay X Avg FPS  %8.3f     %@\nScanout X Avg FPS  %8.3f     %@\nDisplay X Energy   %8.3f J   %@\nBrightness X       %8.3f nits %@"
+ "%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\nSystem Power Usage (sampled power) = %{public, name=System_Power_Usage, units=%/hr}.2f %%/hr\nThermal State = %{public, name=Thermal_State}ld \nCharging Status = %{public, name=Charging_State}d \nDisplay APL = %{public, name=Display_APL}.2f \nFrame Rate = %{public, name=Frame_Rate, units =fps}.2f FPS \nDisplay Brightness Percentage = %{public, name=Display_Brightness_Percentage, units=%}.2f %%\nDisplay Brightness Percentage X = %{public, name=Display_Brightness_Percentage_X, units=%}.2f %%\n"
+ "brightnessX"
+ "displayAPLX"
+ "displayCostX"
+ "displayEnergyX"
+ "displayFPSX"
+ "displayPowerX"
+ "scanoutFPSX"
```
