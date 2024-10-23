## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.1.0.0.0
-  __TEXT.__text: 0xf5668
+989.4.2.0.0
+  __TEXT.__text: 0xf5a40
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x106a0
-  __TEXT.__objc_methlist: 0xbc30
+  __TEXT.__objc_stubs: 0x106c0
+  __TEXT.__objc_methlist: 0xbc38
   __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x24d8
-  __TEXT.__objc_methname: 0x1b3a9
-  __TEXT.__cstring: 0xd055
-  __TEXT.__oslogstring: 0x13211
+  __TEXT.__gcc_except_tab: 0x24d4
+  __TEXT.__objc_methname: 0x1b3e0
+  __TEXT.__cstring: 0xd100
+  __TEXT.__oslogstring: 0x1331c
   __TEXT.__objc_classname: 0x214f
   __TEXT.__objc_methtype: 0x490b
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x3848
+  __TEXT.__unwind_info: 0x3858
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xc20
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4928
-  __DATA_CONST.__cfstring: 0xb9c0
+  __DATA_CONST.__const: 0x4920
+  __DATA_CONST.__cfstring: 0xb9e0
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA.__objc_const: 0x1bdd0
-  __DATA.__objc_selrefs: 0x5888
+  __DATA.__objc_selrefs: 0x5890
   __DATA.__objc_ivar: 0x1130
   __DATA.__objc_data: 0x4bf0
   __DATA.__data: 0x19d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5551
+  Functions: 5553
   Symbols:   678
-  CStrings:  8412
+  CStrings:  8420
 
CStrings:
+ "%!s(MISSING) called with nil Bluetooth identifier!"
+ "+[NetworkRelayAgent networkRelayIdentifierForBluetoothIdentifier:]"
+ "-[NRPairingDaemon _updateNetworkRelayIdentifierForDevice:]"
+ "-[NRPairingDaemon _updateNetworkRelayIdentifierForDevicesInCollection:]"
+ "202"
+ "80E387E5-4BC3-421D-873B-080D09375241"
+ "NanoRegistry-989.4.2"
+ "Not updating NetworkRelayIdentifier for %!@(MISSING)"
+ "Unable to update NetworkRelayIdentifier for device with no Bluetooth identifier: %!@(MISSING)"
+ "_requiresNetworkRelayPairingIdentifierUpdateForDevice:"
+ "_updateNetworkRelayIdentifierForDevice:"
+ "_updateNetworkRelayIdentifierForDevicesInCollection:"
+ "createUnpairTransactionsWithCompletion: Updating NetworkRelay Identifier for devices in %!{(MISSING)public}@"
- "-[NRPairingDaemon _upgradePairingToNetworkRelayPairingForDevice:]"
- "761"
- "NanoRegistry-989.1"
- "_requiresNetworkRelayPairingUpgrageForDevice:"
- "_upgradePairingToNetworkRelayPairingForDevice:"

```
