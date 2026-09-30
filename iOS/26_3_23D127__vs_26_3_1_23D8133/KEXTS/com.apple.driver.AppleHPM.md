## com.apple.driver.AppleHPM

> `com.apple.driver.AppleHPM`

```diff

 614.80.20.0.0
-  __TEXT.__cstring: 0x1db0a
+  __TEXT.__cstring: 0x1ddaa
   __TEXT.__const: 0x110
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x68db4
+  __TEXT_EXEC.__text: 0x694b4
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
-  UUID: 330E54F7-43D5-39B1-BF8C-87031D584C7C
+  UUID: 46A2FDDA-C89D-3DBA-BA01-30F0BDF96FBE
   Functions: 1654
   Symbols:   0
-  CStrings:  1684
+  CStrings:  1691
 
Functions:
~ __ZN17AppleHPMInterface20createUSB3PortObjectEPP24IOPortTransportStateUSB3 : 540 -> 564
~ sub_fffffe0009544454 -> sub_fffffe000954b75c : 8 -> 960
~ __ZN17AppleTCController20createUSB3PortObjectEPP24IOPortTransportStateUSB3j : 516 -> 540
~ sub_fffffe000956e484 -> sub_fffffe0009575b5c : 8 -> 800
CStrings:
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x)\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x) - usb Type2 client ping, Handle(%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChangeWithParams(@0x%x) with non USB Type2 object... Quiting...\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) - dropping usb Type2 Handle(%d/%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) - usb Type2 client ping, Handle(%d)\n\n"
+ "%s::%s(0x%x@0x%x): AppleTCController::tunnelClientChangeWithParams(@0x%x) with non USB Type2 object... Quiting...\n\n"
+ "tunnelClientChangeWithParams"

```
