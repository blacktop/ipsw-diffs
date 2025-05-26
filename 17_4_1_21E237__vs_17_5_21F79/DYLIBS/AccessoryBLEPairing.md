## AccessoryBLEPairing

> `/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`

```diff

-919.100.33.0.0
-  __TEXT.__text: 0x8f5c
+919.120.14.0.1
+  __TEXT.__text: 0x9558
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x374
+  __TEXT.__objc_methlist: 0x380
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__oslogstring: 0x16dc
+  __TEXT.__oslogstring: 0x17c2
   __TEXT.__cstring: 0x709
   __TEXT.__unwind_info: 0x134
   __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methname: 0xde7
+  __TEXT.__objc_methname: 0xe21
   __TEXT.__objc_methtype: 0x3e3
-  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_stubs: 0x7a0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x920
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_const: 0x940
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 167
-  Symbols:   592
-  CStrings:  350
+  Functions: 171
+  Symbols:   601
+  CStrings:  356
 
Symbols:
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingNoAccessories]
+ -[ACCBLEPairingProviderInternal accessoryBLEPairingNoAccessories].cold.1
+ -[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:].cold.2
+ -[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:].cold.3
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.153
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.153.cold.1
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154.cold.1
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.154.cold.2
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.158
+ ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.158.cold.1
+ ___block_literal_global.157
+ _objc_msgSend$blePairingNoAccessories:
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.150
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.150.cold.1
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.151
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.151.cold.1
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.151.cold.2
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.155
- ___48-[ACCBLEPairingProviderInternal connectToServer]_block_invoke.155.cold.1
- ___block_literal_global.154
CStrings:
+ "%s:%d NOT accessoryServer_isServerAvailable(), delegate=%@, provider=%@"
+ "%s:%d call blePairingNoAccessories, delegate=%@, provider=%@"
+ "accessoryBLEPairingNoAccessories"
+ "accessoryBLEPairingNoAccessories, call delegate=%@, provider=%@"
+ "blePairingNoAccessories:"

```
