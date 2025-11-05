## PMBrowser

> `/System/Library/CoreServices/AddPrinter.app/Contents/Frameworks/PMBrowser.framework/Versions/A/PMBrowser`

```diff

 2.3.1.0.0
-  __TEXT.__text: 0x133f4
+  __TEXT.__text: 0x1339c
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_stubs: 0x30e0
-  __TEXT.__objc_methlist: 0x116c
+  __TEXT.__objc_methlist: 0x1470
   __TEXT.__objc_methname: 0x2a36
   __TEXT.__objc_classname: 0x2b6
   __TEXT.__objc_methtype: 0x86d

   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x74
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__unwind_info: 0x490
   __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x10

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x2400
-  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_const: 0x1e78
+  __DATA.__objc_selrefs: 0xf38
   __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x2a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22679787-89B6-33AE-86E7-3E2993B7180D
-  Functions: 428
-  Symbols:   1393
+  UUID: A6A32C6B-8639-3F0A-9C83-CDA3F7D1A746
+  Functions: 427
+  Symbols:   1394
   CStrings:  1742
 
Symbols:
+ -[DNSSDConfigure setMainRef:].cold.1
Functions:
~ -[PPDManager matchPPDsByDeviceID:model:product:fromList:] : 1732 -> 1736
~ -[PPDManager genericPostscriptPPD] : 400 -> 396
~ +[PPDManager(ConvenienceMethods) parsePPD:] : 2244 -> 2224
~ -[PMPPDPopUpButton setDrivers:supportsAutoSelect:supportsPostscript:supportsPCL:supportsFax:selectStandardDefaults:] : 1492 -> 1460
~ -[PMPPDPopUpButton genericPCLPPD] : 176 -> 180
~ -[PrinterInspector initWithFrame:] : 344 -> 340
~ -[PrinterInspector driverChanged:] : 1556 -> 1572
- sub_9f24
~ -[PrinterInspector updateUI] : 1000 -> 980
~ -[PrinterInspector sendPrinterChangedNotification] : 336 -> 332
~ -[PrinterInspector panel:shouldEnableURL:] : 244 -> 248
~ _getPrinters : 988 -> 996
~ _driverMatches : 336 -> 324
~ -[PrinterConfigure ppds] : 88 -> 80
~ -[DNSSDConfigure setMainRef:] : 104 -> 68
~ ___42-[DNSSDConfigure startConfigureWithTypes:]_block_invoke : 800 -> 796
~ -[DNSSDConfigure updatePPDForPrinter:on:port:encryption:] : 1856 -> 1872
~ _cupsAppendAttribute : 1168 -> 1188
- sub_10e6c
~ -[DNSSDPrinter dictionaryWithDriverSpecification:] : 1100 -> 1116
~ -[DNSSDPrinter addRegistrationType:domain:] : 172 -> 176
~ -[IPPrinter configure] : 236 -> 232
~ _str_for_ioreturn : 120 -> 116
~ -[PPDPickerWindowController init] : 144 -> 140
+ -[DNSSDConfigure setMainRef:].cold.1
~ -[DNSSDConfigure updatePPDForPrinter:on:port:encryption:].cold.1 : 132 -> 128
~ -[DNSSDConfigure updatePPDForPrinter:on:port:encryption:].cold.2 : 128 -> 132

```
