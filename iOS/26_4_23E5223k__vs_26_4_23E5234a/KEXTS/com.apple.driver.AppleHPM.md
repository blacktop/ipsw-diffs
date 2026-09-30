## com.apple.driver.AppleHPM

> `com.apple.driver.AppleHPM`

```diff

 624.100.15.0.0
-  __TEXT.__cstring: 0x1db0a
+  __TEXT.__cstring: 0x1ddaa
   __TEXT.__const: 0xf0
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x61720
+  __TEXT_EXEC.__text: 0x61dd0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x630
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x130
   __DATA_CONST.__mod_term_func: 0x130
   __DATA_CONST.__const: 0x15db8
   __DATA_CONST.__kalloc_type: 0xcc0
-  UUID: 36020B81-704E-327F-9E24-15E222701608
+  UUID: B7EF8F57-A4BB-3CDB-8B36-44C344FB0A44
   Functions: 1654
   Symbols:   0
-  CStrings:  1684
+  CStrings:  1691
 
Functions:
~ __ZN17AppleHPMInterface20createUSB3PortObjectEPP24IOPortTransportStateUSB3j : 532 -> 556
~ sub_fffffe0008c36004 -> sub_fffffe0008c41fcc : 8 -> 920
~ __ZN17AppleTCController20createUSB3PortObjectEPP24IOPortTransportStateUSB3j : 484 -> 508
~ sub_fffffe0008c5cd40 -> sub_fffffe0008c690b0 : 8 -> 760
CStrings:
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x)\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x) - usb Type2 client ping, Handle(%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x) with non USB Type2 object... Quiting...\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) - dropping usb Type2 Handle(%d/%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) - usb Type2 client ping, Handle(%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) with non USB Type2 object... Quiting...\n\n"
+ "tunnelClientChangeWithParams"

```
