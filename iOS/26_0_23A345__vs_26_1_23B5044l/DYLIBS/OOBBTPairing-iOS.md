## OOBBTPairing-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS`

```diff

-1124.2.1.0.0
-  __TEXT.__text: 0x5868
+1139.40.1.0.0
+  __TEXT.__text: 0x58cc
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x59c
   __TEXT.__const: 0xa8

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FB72FD3-63F4-3999-9C76-ADC7E1B40E30
-  Functions: 118
-  Symbols:   619
+  UUID: 5D04E428-4183-3826-A941-EC5D3888CA7D
+  Functions: 119
+  Symbols:   621
   CStrings:  342
 
Symbols:
+ -[ACCOOBBTPairingShim accessoryPairingCompletion:oobBtPairingUID:accessoryMacAddr:sendStop:result:].cold.7
Functions:
~ -[ACCOOBBTPairingShim accessoryPairingCompletion:oobBtPairingUID:accessoryMacAddr:sendStop:result:] : 1208 -> 1192
+ -[ACCOOBBTPairingShim accessoryPairingCompletion:oobBtPairingUID:accessoryMacAddr:sendStop:result:].cold.4

```
