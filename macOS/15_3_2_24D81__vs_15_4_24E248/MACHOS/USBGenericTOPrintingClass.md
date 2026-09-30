## USBGenericTOPrintingClass

> `/System/Library/Printers/Libraries/USBGenericTOPrintingClass.plugin/Contents/MacOS/USBGenericTOPrintingClass`

```diff

-711.3.0.0.0
-  __TEXT.__text: 0x2af0
+711.5.0.0.0
+  __TEXT.__text: 0x2ac8
   __TEXT.__auth_stubs: 0x340
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x121

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: E44E9722-45ED-38B9-97D7-5EB4179322FE
+  UUID: AD08F2B3-BA10-3416-9B0D-0C6A80C47985
   Functions: 36
   Symbols:   83
   CStrings:  53
Functions:
~ _UsbLoadClassDriver : 560 -> 544
~ _UsbSupportedPrinter : 180 -> 188
~ _CreateSerial : 168 -> 180
~ _UsbGetAllPrinters : 1072 -> 1056
~ _UsbRegistryOpen : 528 -> 508
~ sub_2c14 -> sub_22fc : 112 -> 116
~ sub_2d94 -> sub_2480 : 1428 -> 1416
~ sub_344c -> sub_2b2c : 588 -> 592
~ sub_3728 -> sub_2e0c : 764 -> 760

```
