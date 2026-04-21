## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-1147.100.17.0.0
-  __TEXT.__text: 0x9f58
+1147.120.2.0.0
+  __TEXT.__text: 0x9fc8
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x3c4
   __TEXT.__cstring: 0xd76
-  __TEXT.__const: 0x1864
+  __TEXT.__const: 0x18ec
   __TEXT.__oslogstring: 0x17a2
   __TEXT.__gcc_except_tab: 0x174
   __TEXT.__dlopen_cstrs: 0xc2

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85863D65-E4A3-36CB-94EC-3B1D6BCE0231
+  UUID: B29E3439-B25D-3E58-A8B2-07FA435A27BD
   Functions: 154
-  Symbols:   1036
+  Symbols:   1038
   CStrings:  623
 
Symbols:
+ _colorWashTable0x5F
+ _colorWashTable0x5FSize
Functions:
~ sub_23990d834 -> sub_239479834 : 96 -> 132
~ sub_23990d894 -> sub_2394798b8 : 180 -> 204
~ -[AccessoryTransportPluginNFC _getAccessoryFamily:] : 384 -> 380
~ -[AccessoryTransportPluginNFC _hasWalletOnClearCase2020:] : 340 -> 364
~ -[AccessoryTransportPluginNFC _animationDelayMs:] : 172 -> 196
~ -[AccessoryTransportPluginNFC _decodeTagIdentifier:] : 2340 -> 2348

```
