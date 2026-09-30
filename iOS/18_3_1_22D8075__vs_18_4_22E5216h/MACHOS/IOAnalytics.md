## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0x15fc8
+1043.100.29.0.0
+  __TEXT.__text: 0x15864
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xd1c
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0xebc
   __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x129f
+  __TEXT.__objc_methname: 0x12a7
   __TEXT.__cstring: 0x1c77
   __TEXT.__oslogstring: 0x13ec
   __TEXT.__objc_classname: 0x13f

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x1df8
-  __DATA.__objc_selrefs: 0x4c8
+  __DATA.__objc_const: 0x1b00
+  __DATA.__objc_selrefs: 0x578
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x178

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 513
-  Symbols:   3919
-  CStrings:  842
+  Functions: 518
+  Symbols:   3890
+  CStrings:  843
 
Symbols:
+ -[IOAnalytics createMetadataFromIOThunderboltSwitch:properties:].cold.3
+ -[IOAnalytics createMetadataFromIOUSBHostInterface:properties:].cold.1
+ -[IOAnalytics removedService:withClassName:].cold.5
+ LogIOAnalytics.cold.1
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ __get_kCAEvent_ThunderboltCounters_block_invoke.cold.1
+ __get_kCAEvent_Thunderbolt_Daily_block_invoke.cold.1
+ _objc_msgSend$allKeys
+ get_USBFields.cold.1
+ get_kCAEvent_ThunderboltCounters.cold.1
+ get_kCAEvent_Thunderbolt_Daily.cold.1
+ get_kCAEvent_USBFW.cold.1
+ get_kCAEvent_USB_Device_Daily.cold.1
+ get_kCAEvent_USB_Interface_Daily.cold.1
- -[AUVDMAnalytics _handleServiceMatched:].cold.1
- -[AUVDMAnalytics _handleServiceMatched:].cold.10
- -[AUVDMAnalytics _handleServiceMatched:].cold.11
- -[AUVDMAnalytics _handleServiceMatched:].cold.2
- -[AUVDMAnalytics _handleServiceMatched:].cold.3
- -[AUVDMAnalytics _handleServiceMatched:].cold.4
- -[AUVDMAnalytics _handleServiceMatched:].cold.5
- -[AUVDMAnalytics _handleServiceMatched:].cold.6
- -[AUVDMAnalytics _handleServiceMatched:].cold.7
- -[AUVDMAnalytics _handleServiceMatched:].cold.8
- -[AUVDMAnalytics _handleServiceMatched:].cold.9
- -[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:].cold.1
- -[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:].cold.2
- -[CIOAnalytics _handleServiceMatched:].cold.1
- -[CIOAnalytics _handleServiceMatched:].cold.10
- -[CIOAnalytics _handleServiceMatched:].cold.11
- -[CIOAnalytics _handleServiceMatched:].cold.12
- -[CIOAnalytics _handleServiceMatched:].cold.13
- -[CIOAnalytics _handleServiceMatched:].cold.14
- -[CIOAnalytics _handleServiceMatched:].cold.15
- -[CIOAnalytics _handleServiceMatched:].cold.16
- -[CIOAnalytics _handleServiceMatched:].cold.2
- -[CIOAnalytics _handleServiceMatched:].cold.3
- -[CIOAnalytics _handleServiceMatched:].cold.4
- -[CIOAnalytics _handleServiceMatched:].cold.5
- -[CIOAnalytics _handleServiceMatched:].cold.6
- -[CIOAnalytics _handleServiceMatched:].cold.7
- -[CIOAnalytics _handleServiceMatched:].cold.8
- -[CIOAnalytics _handleServiceMatched:].cold.9
- -[DPAnalytics _handleServiceMatched:].cold.1
- -[DPAnalytics _handleServiceMatched:].cold.10
- -[DPAnalytics _handleServiceMatched:].cold.11
- -[DPAnalytics _handleServiceMatched:].cold.12
- -[DPAnalytics _handleServiceMatched:].cold.13
- -[DPAnalytics _handleServiceMatched:].cold.14
- -[DPAnalytics _handleServiceMatched:].cold.15
- -[DPAnalytics _handleServiceMatched:].cold.16
- -[DPAnalytics _handleServiceMatched:].cold.17
- -[DPAnalytics _handleServiceMatched:].cold.18
- -[DPAnalytics _handleServiceMatched:].cold.19
- -[DPAnalytics _handleServiceMatched:].cold.2
- -[DPAnalytics _handleServiceMatched:].cold.20
- -[DPAnalytics _handleServiceMatched:].cold.21
- -[DPAnalytics _handleServiceMatched:].cold.22
- -[DPAnalytics _handleServiceMatched:].cold.23
- -[DPAnalytics _handleServiceMatched:].cold.24
- -[DPAnalytics _handleServiceMatched:].cold.25
- -[DPAnalytics _handleServiceMatched:].cold.26
- -[DPAnalytics _handleServiceMatched:].cold.27
- -[DPAnalytics _handleServiceMatched:].cold.28
- -[DPAnalytics _handleServiceMatched:].cold.29
- -[DPAnalytics _handleServiceMatched:].cold.3
- -[DPAnalytics _handleServiceMatched:].cold.30
- -[DPAnalytics _handleServiceMatched:].cold.4
- -[DPAnalytics _handleServiceMatched:].cold.5
- -[DPAnalytics _handleServiceMatched:].cold.6
- -[DPAnalytics _handleServiceMatched:].cold.7
- -[DPAnalytics _handleServiceMatched:].cold.8
- -[DPAnalytics _handleServiceMatched:].cold.9
- -[PowerInAnalytics _handleServiceMatched:].cold.1
- -[PowerInAnalytics _handleServiceMatched:].cold.10
- -[PowerInAnalytics _handleServiceMatched:].cold.2
- -[PowerInAnalytics _handleServiceMatched:].cold.3
- -[PowerInAnalytics _handleServiceMatched:].cold.4
- -[PowerInAnalytics _handleServiceMatched:].cold.5
- -[PowerInAnalytics _handleServiceMatched:].cold.6
- -[PowerInAnalytics _handleServiceMatched:].cold.7
- -[PowerInAnalytics _handleServiceMatched:].cold.8
- -[PowerInAnalytics _handleServiceMatched:].cold.9
- -[USBAnalytics _handleServiceMatched:].cold.1
- -[USBAnalytics _handleServiceMatched:].cold.10
- -[USBAnalytics _handleServiceMatched:].cold.11
- -[USBAnalytics _handleServiceMatched:].cold.12
- -[USBAnalytics _handleServiceMatched:].cold.2
- -[USBAnalytics _handleServiceMatched:].cold.3
- -[USBAnalytics _handleServiceMatched:].cold.4
- -[USBAnalytics _handleServiceMatched:].cold.5
- -[USBAnalytics _handleServiceMatched:].cold.6
- -[USBAnalytics _handleServiceMatched:].cold.7
- -[USBAnalytics _handleServiceMatched:].cold.8
- -[USBAnalytics _handleServiceMatched:].cold.9
- -[USBPDAnalytics _handleServiceMatched:].cold.1
- -[USBPDAnalytics _handleServiceMatched:].cold.10
- -[USBPDAnalytics _handleServiceMatched:].cold.11
- -[USBPDAnalytics _handleServiceMatched:].cold.12
- -[USBPDAnalytics _handleServiceMatched:].cold.2
- -[USBPDAnalytics _handleServiceMatched:].cold.3
- -[USBPDAnalytics _handleServiceMatched:].cold.4
- -[USBPDAnalytics _handleServiceMatched:].cold.5
- -[USBPDAnalytics _handleServiceMatched:].cold.6
- -[USBPDAnalytics _handleServiceMatched:].cold.7
- -[USBPDAnalytics _handleServiceMatched:].cold.8
- -[USBPDAnalytics _handleServiceMatched:].cold.9
CStrings:
+ "allKeys"

```
