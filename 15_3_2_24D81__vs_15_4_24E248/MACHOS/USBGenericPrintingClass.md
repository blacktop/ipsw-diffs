## USBGenericPrintingClass

> `/System/Library/Printers/Libraries/USBGenericPrintingClass.plugin/Contents/MacOS/USBGenericPrintingClass`

```diff

-711.3.0.0.0
-  __TEXT.__text: 0x2ae0
+711.5.0.0.0
+  __TEXT.__text: 0x2ab8
   __TEXT.__auth_stubs: 0x340
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x11f

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 6F61937E-E49D-32C9-8432-248B7D0BB738
+  UUID: A4D6B794-836F-3ED5-BA10-CDFC0DF51060
   Functions: 36
   Symbols:   83
   CStrings:  53
Functions:
~ sub_1800 -> sub_ee8 : 112 -> 116
~ sub_1974 -> sub_1060 : 1428 -> 1416
~ sub_202c -> sub_170c : 588 -> 592
~ sub_2308 -> sub_19ec : 764 -> 760
~ _UsbLoadClassDriver : 560 -> 544
~ _UsbSupportedPrinter : 180 -> 188
~ _CreateSerial : 168 -> 180
~ _UsbGetAllPrinters : 1072 -> 1056
~ _UsbRegistryOpen : 528 -> 508

```
