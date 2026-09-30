## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-  __TEXT.__text: 0xe6808
-  __TEXT.__objc_methlist: 0x96e0
+  __TEXT.__text: 0xe6d4c
+  __TEXT.__objc_methlist: 0x9728
   __TEXT.__const: 0x1b68
-  __TEXT.__cstring: 0x3f5fd
-  __TEXT.__oslogstring: 0x884a
+  __TEXT.__cstring: 0x3ff65
+  __TEXT.__oslogstring: 0x88f8
   __TEXT.__gcc_except_tab: 0x297c
-  __TEXT.__unwind_info: 0x3098
+  __TEXT.__unwind_info: 0x30a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2580
+  __DATA_CONST.__const: 0x25a0
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5920
+  __DATA_CONST.__objc_selrefs: 0x5950
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x41040
+  __DATA_CONST.__objc_arraydata: 0x41680
   __DATA_CONST.__got: 0x7e8
-  __AUTH_CONST.__const: 0x24a0
-  __AUTH_CONST.__cfstring: 0x666e0
-  __AUTH_CONST.__objc_const: 0xa9a0
+  __AUTH_CONST.__const: 0x24e0
+  __AUTH_CONST.__cfstring: 0x67280
+  __AUTH_CONST.__objc_const: 0xaa00
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x4a58
+  __AUTH_CONST.__objc_intobj: 0x4a70
   __AUTH_CONST.__objc_doubleobj: 0x13a0
   __AUTH_CONST.__objc_arrayobj: 0x1170
-  __AUTH_CONST.__objc_dictobj: 0xf618
+  __AUTH_CONST.__objc_dictobj: 0xf690
   __AUTH_CONST.__auth_got: 0xda8
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x7c4
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x7cc
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x1739
+  __DATA.__bss: 0x16b1
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1db0
+  __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x1138
+  __DATA_DIRTY.__bss: 0x11c0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4920
-  Symbols:   17016
-  CStrings:  27536
+  Functions: 4929
+  Symbols:   17041
+  CStrings:  27727
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[PLArchiveManager fireArchiveListener]
+ -[PLArchiveManager setFireArchiveListener:]
+ -[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:]
+ -[PowerlogCore fireSBCListener]
+ -[PowerlogCore fireSignificantBatteryChangeNotification]
+ -[PowerlogCore setFireSBCListener:]
+ _OBJC_IVAR_$_PLArchiveManager._fireArchiveListener
+ _OBJC_IVAR_$_PowerlogCore._fireSBCListener
+ ___116-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:]_block_invoke
+ ___20-[PowerlogCore init]_block_invoke_2
+ ___24-[PLArchiveManager init]_block_invoke_2
+ ___block_descriptor_32_e38_v32?0"NSDictionary"8"NSString"1624l
+ _objc_msgSend$fireSignificantBatteryChangeNotification
+ _objc_msgSend$initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:
- GCC_except_table42
- ___105-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:withMatchBlock:]_block_invoke
CStrings:
+ "1006035"
+ "ANE1"
+ "BatteryShippingChargeLimit"
+ "CPU_Energy"
+ "CSIDualAntennaDuration"
+ "CSIEnabledDuration"
+ "CSIMacActiveDuration"
+ "Dormancy"
+ "ECPU_CORE0_NRG"
+ "ECPU_CORE0_SRM_NRG"
+ "ECPU_CORE1_NRG"
+ "ECPU_CORE1_SRM_NRG"
+ "ECPU_CORE2_NRG"
+ "ECPU_CORE2_SRM_NRG"
+ "ECPU_CORE3_NRG"
+ "ECPU_CORE3_SRM_NRG"
+ "ECPU_CPM_NRG"
+ "ECPU_CPM_SRM_NRG"
+ "ECPU_NRG"
+ "Features"
+ "FirstPartyApps"
+ "Manually firing SBC"
+ "Manually firing archive activity"
+ "PCPU0_CORE0_NRG"
+ "PCPU0_CORE0_SRM_NRG"
+ "PCPU0_CORE1_NRG"
+ "PCPU0_CORE1_SRM_NRG"
+ "PCPU0_CPM_NRG"
+ "PCPU0_CPM_SRM_NRG"
+ "PCPU_NRG"
+ "PLBatteryAgent_EventBackward_Battery.filtered.Level_0_1.Level_7_1800.Level_8_300"
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "ShippingChargeLimitSystemStatus"
+ "Skipping manual archive: archive manager is not enabled"
+ "Skipping manual archive: storage is locked"
+ "SystemCapability100ms_Battery0"
+ "SystemCapability100ms_Battery0_0"
+ "SystemCapability100ms_Battery0_1"
+ "SystemCapability100ms_Battery0_2"
+ "SystemCapability100ms_Battery0_3"
+ "SystemCapability100ms_Battery0_4"
+ "SystemCapability100ms_Battery0_5"
+ "SystemCapability100ms_Battery0_6"
+ "SystemCapability100ms_Battery0_7"
+ "SystemCapability100ms_Battery1"
+ "SystemCapability100ms_Battery1_0"
+ "SystemCapability100ms_Battery1_1"
+ "SystemCapability100ms_Battery1_2"
+ "SystemCapability100ms_Battery1_3"
+ "SystemCapability100ms_Battery1_4"
+ "SystemCapability100ms_Battery1_5"
+ "SystemCapability100ms_Battery1_6"
+ "SystemCapability100ms_Battery1_7"
+ "SystemCapability1sec_Battery0"
+ "SystemCapability1sec_Battery0_0"
+ "SystemCapability1sec_Battery0_1"
+ "SystemCapability1sec_Battery0_2"
+ "SystemCapability1sec_Battery0_3"
+ "SystemCapability1sec_Battery0_4"
+ "SystemCapability1sec_Battery0_5"
+ "SystemCapability1sec_Battery0_6"
+ "SystemCapability1sec_Battery0_7"
+ "SystemCapability1sec_Battery1"
+ "SystemCapability1sec_Battery1_0"
+ "SystemCapability1sec_Battery1_1"
+ "SystemCapability1sec_Battery1_2"
+ "SystemCapability1sec_Battery1_3"
+ "SystemCapability1sec_Battery1_4"
+ "SystemCapability1sec_Battery1_5"
+ "SystemCapability1sec_Battery1_6"
+ "SystemCapability1sec_Battery1_7"
+ "SystemCapabilityInsta_Battery0"
+ "SystemCapabilityInsta_Battery0_0"
+ "SystemCapabilityInsta_Battery0_1"
+ "SystemCapabilityInsta_Battery0_2"
+ "SystemCapabilityInsta_Battery0_3"
+ "SystemCapabilityInsta_Battery0_4"
+ "SystemCapabilityInsta_Battery0_5"
+ "SystemCapabilityInsta_Battery0_6"
+ "SystemCapabilityInsta_Battery0_7"
+ "SystemCapabilityInsta_Battery1"
+ "SystemCapabilityInsta_Battery1_0"
+ "SystemCapabilityInsta_Battery1_1"
+ "SystemCapabilityInsta_Battery1_2"
+ "SystemCapabilityInsta_Battery1_3"
+ "SystemCapabilityInsta_Battery1_4"
+ "SystemCapabilityInsta_Battery1_5"
+ "SystemCapabilityInsta_Battery1_6"
+ "SystemCapabilityInsta_Battery1_7"
+ "UISoc"
+ "candidate"
+ "com.apple.powerlogd.archive"
+ "com.apple.powerlogd.fireSBC"
+ "effectiveIdleSeconds"
+ "eventTimestamp"
+ "excluded"
+ "inactive"
+ "\xa3"
- "\xa2"

```
