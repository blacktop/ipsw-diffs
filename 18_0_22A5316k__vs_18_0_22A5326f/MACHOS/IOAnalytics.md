## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-1008.0.0.502.1
-  __TEXT.__text: 0x1608c
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0xee0
+1017.0.0.0.0
+  __TEXT.__text: 0x15fc8
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0xea0
   __TEXT.__objc_methlist: 0xd1c
   __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x12c2
-  __TEXT.__cstring: 0x1c6e
-  __TEXT.__oslogstring: 0x13df
+  __TEXT.__objc_methname: 0x129f
+  __TEXT.__cstring: 0x1c77
+  __TEXT.__oslogstring: 0x13ec
   __TEXT.__objc_classname: 0x13f
   __TEXT.__objc_methtype: 0x4dc
   __TEXT.__gcc_except_tab: 0xec
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0xa90
+  __DATA_CONST.__const: 0xa98
   __DATA_CONST.__cfstring: 0x2c00
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x1df8
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_selrefs: 0x4c8
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x178

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 525
-  Symbols:   3984
-  CStrings:  844
+  Functions: 513
+  Symbols:   3919
+  CStrings:  842
 
Symbols:
+ -[DPAnalytics _handleServiceMatched:].cold.30
+ -[USBPDAnalytics _handleServiceMatched:].cold.12
+ -[USBPDAnalytics _handleServiceMatched:].cold.12
+ __42-[PowerInAnalytics _handleServiceMatched:]_block_invoke.76
+ __42-[PowerInAnalytics _handleServiceMatched:]_block_invoke.76
+ _kACCCoreAnalytics_IOPort_Transport_DP_Field_ProductName
+ _kACCCoreAnalytics_IOPort_Transport_DP_Field_ProductName
- -[AUVDMAnalytics _handleServiceMatched:].cold.12
- -[AUVDMAnalytics _handleServiceMatched:].cold.13
- -[AUVDMAnalytics _handleServiceMatched:].cold.13
- -[AUVDMAnalytics _handleServiceMatched:].cold.14
- -[AUVDMAnalytics _handleServiceMatched:].cold.14
- -[AUVDMAnalytics _handleServiceMatched:].cold.15
- -[AUVDMAnalytics _handleServiceMatched:].cold.15
- -[AUVDMAnalytics _handleServiceMatched:].cold.16
- -[AUVDMAnalytics _handleServiceMatched:].cold.16
- -[AUVDMAnalytics _handleServiceMatched:].cold.17
- -[AUVDMAnalytics _handleServiceMatched:].cold.17
- -[AUVDMAnalytics _handleServiceMatched:].cold.18
- -[AUVDMAnalytics _handleServiceMatched:].cold.18
- -[AUVDMAnalytics _handleServiceMatched:].cold.19
- -[AUVDMAnalytics _handleServiceMatched:].cold.19
- -[AUVDMAnalytics _handleServiceMatched:].cold.20
- -[AUVDMAnalytics _handleServiceMatched:].cold.20
- -[AUVDMAnalytics _handleServiceMatched:].cold.21
- -[AUVDMAnalytics _handleServiceMatched:].cold.22
- -[AUVDMAnalytics _handleServiceMatched:].cold.22
- -[PowerInAnalytics _getMutualPowerSourceProperties:dict:].cold.11
- -[PowerInAnalytics _getMutualPowerSourceProperties:dict:].cold.12
- -[PowerInAnalytics _getMutualPowerSourceProperties:dict:].cold.13
- -[PowerInAnalytics _getMutualPowerSourceProperties:dict:].cold.14
- __42-[PowerInAnalytics _handleServiceMatched:]_block_invoke.82
- __42-[PowerInAnalytics _handleServiceMatched:]_block_invoke.82
- _objc_msgSend$isEqualToString:
- _objc_msgSend$substringToIndex:
- _objc_retain_x25
CStrings:
+ "Converted AUVDM Manufacturer to VID!"
+ "Converted AUVDM Model to PID!"
+ "Converted AUVDM User String to Accessory Name!"
+ "Incorrect data type for '%!@(MISSING)' key! (class: %!@(MISSING), expecting: %!@(MISSING) or %!@(MISSING))"
+ "Incorrect data type for '%!s(MISSING)' key! (class: %!@(MISSING), expecting: %!@(MISSING))"
+ "ProductName"
- "0x"
- "Could not find AUVDM %!s(MISSING) property!"
- "Could not find AUVDM manufacturer!"
- "Incorrect data type for '%!@(MISSING)' key! (class: %!@(MISSING), expecting: %!@(MISSING) or %!@(MISSING)"
- "Unknown value for AUVDM %!s(MISSING) property! (pid: %!@(MISSING))"
- "Unknown value for AUVDM %!s(MISSING) property! (vid: %!@(MISSING))"
- "isEqualToString:"
- "substringToIndex:"

```
