## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

 2022.120.2.0.0
-  __TEXT.__text: 0x2599e4
+  __TEXT.__text: 0x259e48
   __TEXT.__auth_stubs: 0x2320
-  __TEXT.__objc_methlist: 0x17298
-  __TEXT.__cstring: 0x239b5
+  __TEXT.__objc_methlist: 0x172e8
+  __TEXT.__cstring: 0x239f5
   __TEXT.__const: 0xab8
-  __TEXT.__gcc_except_tab: 0x5288
-  __TEXT.__oslogstring: 0x40e8b
+  __TEXT.__gcc_except_tab: 0x52bc
+  __TEXT.__oslogstring: 0x40f09
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x6417
   __TEXT.default_clp: 0x2fe0

   __TEXT.bb_MAV_clp: 0xa690
   __TEXT.bb_INT_clp: 0x68e0
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6618
+  __TEXT.__unwind_info: 0x6630
   __TEXT.__objc_classname: 0x1d37
-  __TEXT.__objc_methname: 0x3ba58
+  __TEXT.__objc_methname: 0x3bb42
   __TEXT.__objc_methtype: 0x6a83
-  __TEXT.__objc_stubs: 0x25240
+  __TEXT.__objc_stubs: 0x252a0
   __DATA_CONST.__got: 0xdf0
   __DATA_CONST.__const: 0x6558
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc7d0
+  __DATA_CONST.__objc_selrefs: 0xc7f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x810
   __AUTH_CONST.__auth_got: 0x11a8
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__cfstring: 0x1ca00
-  __AUTH_CONST.__objc_const: 0x3b0c0
+  __AUTH_CONST.__cfstring: 0x1ca60
+  __AUTH_CONST.__objc_const: 0x3b198
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1568
-  __DATA.__objc_ivar: 0x2cd0
+  __DATA.__objc_ivar: 0x2cd4
   __DATA.__data: 0x1c60
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x358

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10916
-  Symbols:   35797
-  CStrings:  22396
+  Functions: 10922
+  Symbols:   35814
+  CStrings:  22408
 
Symbols:
+ -[CellularStateRelay isNonTerrestrialNetworkActive]
+ -[CellularStateRelay setIsNonTerrestrialNetworkActive:]
+ -[CoreTelephonyShim _deliverNonTerrestrialNetworkActiveChangedTo:]
+ -[CoreTelephonyShim displayStatusChanged:status:]
+ -[NetworkAnalyticsEngine nonTerrestrialNetworkActiveChangedTo:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table122
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table154
+ GCC_except_table199
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table266
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table325
+ GCC_except_table362
+ GCC_except_table376
+ GCC_except_table387
+ _OBJC_IVAR_$_CellularStateRelay._isNonTerrestrialNetworkActive
+ ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.285
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.278
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.279
+ ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.305
+ ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.306
+ ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.897
+ ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.894
+ ___63-[NetworkAnalyticsEngine nonTerrestrialNetworkActiveChangedTo:]_block_invoke
+ ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.290
+ ___block_literal_global.218
+ ___block_literal_global.299
+ ___block_literal_global.887
+ _objc_msgSend$_deliverNonTerrestrialNetworkActiveChangedTo:
+ _objc_msgSend$isNonTerrestrialNetworkActive
+ _objc_msgSend$isSatelliteSystem
+ _objc_msgSend$nonTerrestrialNetworkActiveChangedTo:
+ _objc_msgSend$setIsNonTerrestrialNetworkActive:
- GCC_except_table103
- GCC_except_table131
- GCC_except_table134
- GCC_except_table152
- GCC_except_table197
- GCC_except_table232
- GCC_except_table235
- GCC_except_table239
- GCC_except_table240
- GCC_except_table264
- GCC_except_table268
- GCC_except_table269
- GCC_except_table279
- GCC_except_table323
- GCC_except_table360
- GCC_except_table374
- GCC_except_table385
- GCC_except_table88
- GCC_except_table95
- GCC_except_table99
- ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.281
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.273
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.276
- ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.303
- ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.304
- ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.894
- ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.891
- ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.288
- ___block_literal_global.216
- ___block_literal_global.297
- ___block_literal_global.884
- _objc_msgSend$observeSetupAssistantFinished
- _objc_msgSend$requireUserNotification
CStrings:
+ "Delivering new GF active value to delegates. isActive: %{BOOL}d"
+ "GF"
+ "NW_L2_RADIO_TECHNOLOGY_TYPE_GF"
+ "Received GF active changed notification, new status: %{BOOL}d"
+ "TB,N,V_isNonTerrestrialNetworkActive"
+ "_deliverNonTerrestrialNetworkActiveChangedTo:"
+ "_isNonTerrestrialNetworkActive"
+ "isNonTerrestrialNetworkActive"
+ "isSatelliteSystem"
+ "nonTerrestrialNetworkActiveChangedTo:"
+ "setIsNonTerrestrialNetworkActive:"

```
