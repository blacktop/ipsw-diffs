## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

 1124.2.1.0.0
-  __TEXT.__text: 0xa1b4
+  __TEXT.__text: 0xa224
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0x3c4
   __TEXT.__cstring: 0xd49
-  __TEXT.__const: 0x1534
+  __TEXT.__const: 0x1764
   __TEXT.__oslogstring: 0x17a2
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__dlopen_cstrs: 0xc2

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E4CD790-B938-391A-B7C7-16948C56D6FF
+  UUID: 46EA85F2-9799-3177-9344-E93A6CA00096
   Functions: 141
-  Symbols:   1006
+  Symbols:   1010
   CStrings:  619
 
Symbols:
+ _colorWashTable0x60
+ _colorWashTable0x60Size
+ _colorWashTable0x61
+ _colorWashTable0x61Size
Functions:
~ -[AccessoryTransportPluginNFC _getAccessoryType:] : 204 -> 208
~ -[AccessoryTransportPluginNFC _getAccessoryFamily:] : 428 -> 508
~ -[AccessoryTransportPluginNFC _checkProductTypeCompatibility:] : 372 -> 376
~ -[AccessoryTransportPluginNFC _animationDelayMs:] : 156 -> 176
~ -[AccessoryTransportPluginNFC _decodeTagIdentifier:] : 2496 -> 2500

```
