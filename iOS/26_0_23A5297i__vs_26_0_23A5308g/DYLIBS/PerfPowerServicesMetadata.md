## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata`

```diff

-2964.0.107.502.1
-  __TEXT.__text: 0x3c064
+2964.0.137.0.0
+  __TEXT.__text: 0x3a810
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x25dc
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x408f
-  __TEXT.__oslogstring: 0x13bf
+  __TEXT.__objc_methlist: 0x2594
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x3c72
+  __TEXT.__oslogstring: 0x13e8
   __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x840
-  __TEXT.__objc_classname: 0x466
-  __TEXT.__objc_methname: 0x328f
+  __TEXT.__objc_classname: 0x453
+  __TEXT.__objc_methname: 0x3283
   __TEXT.__objc_methtype: 0x527
-  __TEXT.__objc_stubs: 0x38e0
+  __TEXT.__objc_stubs: 0x3880
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1158
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x1f0
+  __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x8460
-  __AUTH_CONST.__objc_const: 0x44b8
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__cfstring: 0x7c60
+  __AUTH_CONST.__objc_const: 0x43c8
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH.__objc_data: 0x280
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x120
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3B69AC3C-94F9-395C-B33D-3C49A6241589
-  Functions: 980
-  Symbols:   3226
-  CStrings:  3085
+  UUID: 53F7B0C7-6F7E-3826-833F-C5DFBF5873FD
+  Functions: 979
+  Symbols:   3214
+  CStrings:  2955
 
Symbols:
+ +[PPSClientInterface getCategoriesForFilepath:subsystem:]
+ +[PPSClientInterface getCategoriesForFilepath:subsystem:].cold.1
+ +[PPSIOReportMetrics gpuStatsGpuPowerControllerStatesMetrics]
+ +[PPSSQLMetadataStore queryCategoriesForFilepath:subsystem:]
+ +[PPSUIKitMetrics UIKitMetrics]
+ +[PPSUIKitMetrics allDeclMetrics]
+ +[PPSUIKitMetrics subsystem]
+ _OBJC_CLASS_$_PPSUIKitMetrics
+ _OBJC_METACLASS_$_PPSUIKitMetrics
+ __OBJC_$_CLASS_METHODS_PPSUIKitMetrics
+ __OBJC_$_PROP_LIST_PPSUIKitMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSUIKitMetrics
+ __OBJC_CLASS_RO_$_PPSUIKitMetrics
+ __OBJC_METACLASS_RO_$_PPSUIKitMetrics
+ _objc_msgSend$UIKitMetrics
+ _objc_msgSend$gpuStatsGpuPowerControllerStatesMetrics
+ _objc_msgSend$queryCategoriesForFilepath:subsystem:
- +[HomeEnergyMetrics allDeclMetrics]
- +[HomeEnergyMetrics cleanEnergyForecastMetrics]
- +[HomeEnergyMetrics homeAppUIInteractionsMetrics]
- +[HomeEnergyMetrics subsystem]
- +[PPSBatteryMetrics smartChargingMetrics]
- +[PPSEnergyMetrics allDeclMetrics]
- +[PPSEnergyMetrics cleanEnergyChargingMetrics]
- +[PPSEnergyMetrics energyAccountingMetrics]
- +[PPSEnergyMetrics subsystem]
- +[PPSSMCMetrics smcMetrics]
- _OBJC_CLASS_$_HomeEnergyMetrics
- _OBJC_CLASS_$_PPSEnergyMetrics
- _OBJC_METACLASS_$_HomeEnergyMetrics
- _OBJC_METACLASS_$_PPSEnergyMetrics
- __OBJC_$_CLASS_METHODS_HomeEnergyMetrics
- __OBJC_$_CLASS_METHODS_PPSEnergyMetrics
- __OBJC_$_PROP_LIST_HomeEnergyMetrics
- __OBJC_$_PROP_LIST_PPSEnergyMetrics
- __OBJC_CLASS_PROTOCOLS_$_HomeEnergyMetrics
- __OBJC_CLASS_PROTOCOLS_$_PPSEnergyMetrics
- __OBJC_CLASS_RO_$_HomeEnergyMetrics
- __OBJC_CLASS_RO_$_PPSEnergyMetrics
- __OBJC_METACLASS_RO_$_HomeEnergyMetrics
- __OBJC_METACLASS_RO_$_PPSEnergyMetrics
- _objc_msgSend$cleanEnergyChargingMetrics
- _objc_msgSend$cleanEnergyForecastMetrics
- _objc_msgSend$energyAccountingMetrics
- _objc_msgSend$homeAppUIInteractionsMetrics
- _objc_msgSend$smartChargingMetrics
- _objc_msgSend$smcMetrics
CStrings:
+ "BackdropGroup"
+ "Dynamic"
+ "GPUStatsGPUPowerControllerStates"
+ "Hard"
+ "Invalid Input: filepath=%@, subsystem=%@"
+ "PPSUIKitMetrics"
+ "SELECT DISTINCT category FROM PLCoreStorage_Metadata where subsystem='%@';"
+ "ScrollPocket"
+ "Total"
+ "UIKit"
+ "UIKitMetrics"
+ "getCategoriesForFilepath:subsystem:"
+ "gpuStatsGpuPowerControllerStatesMetrics"
+ "queryCategoriesForFilepath:subsystem:"
- "Appear"
- "CleanEnergyCharging"
- "CleanEnergyForecast"
- "DashboardDualPaneView"
- "DashboardSinglePaneView"
- "Detected"
- "Disappear"
- "DisplayStateExtended"
- "EnabledChargingOverride"
- "EnergyAccounting"
- "EnergyCategoryStatusItemTapped"
- "EnergyCategoryStatusItemVisit"
- "EnergyCategoryViewAccessedFromURL"
- "EnergyCategoryViewDuration"
- "EnergyDashboardVisit"
- "EnergyEducationTipVisit"
- "EnergyIndicatorAccessoryViewTapped"
- "EnergyIndicatorAccessoryViewVisit"
- "EnergyMetrics"
- "EnergyModelInformationSheetViewDuration"
- "EnergyModelInformationSheetVisit"
- "EnergyWidgetAndComplicationSettings"
- "FailedEnergyWindows"
- "FailedGridID"
- "FullyCharged"
- "GettingEnergyWindows"
- "GettingGridID"
- "GettingLocation"
- "GridForecastOnboardingVisit"
- "HomeAppUIInteractions"
- "HomeEnergy"
- "HomeEnergyMetrics"
- "HomeNotFound"
- "IdlePeriodSocCeiling"
- "IdlePeriodSocFloor"
- "IdlePeriodStart"
- "InstantKeys"
- "Interrupted"
- "IpDst"
- "IpDstPort"
- "IpProto"
- "IpSrc"
- "IpSrcPort"
- "IpVer"
- "NoEnergyWindows"
- "NoGridID"
- "NoHomePermission"
- "NoLocation"
- "OtherError"
- "Override"
- "PPSEnergyMetrics"
- "SmartCharging"
- "TemporarilyDisabled"
- "TopOff"
- "TopOffWithoutIdle"
- "UserOverride"
- "ViewAccessedFromURL"
- "adapter_family"
- "avg_intensity"
- "balancing_authority_id"
- "carbon_footprint"
- "cecState"
- "checkpoint"
- "cleanEnergyChargingMetrics"
- "cleanEnergyForecastMetrics"
- "energyAccountingMetrics"
- "g/kWh"
- "gridID"
- "homeAppUIInteractionsMetrics"
- "isEngaged"
- "isPaused"
- "marginal_intensity"
- "slot_id"
- "smartChargingMetrics"
- "smcMetrics"
- "spi"
- "system_energy_consumed"
- "wall_energy_consumed"
- "windowEnd"
- "windowStart"

```
