## BLEPairing-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS`

```diff

-1139.82.1.0.0
-  __TEXT.__text: 0x5be8
-  __TEXT.__auth_stubs: 0x470
+1147.100.12.0.0
+  __TEXT.__text: 0x5c08
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x270
   __TEXT.__cstring: 0x241
   __TEXT.__oslogstring: 0xfa1
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methname: 0xe25
   __TEXT.__objc_methtype: 0x5cd

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x6c0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE0B711A-3F90-31D7-BE22-C2E0077B1ABE
-  Functions: 96
-  Symbols:   565
+  UUID: F5B8ADB1-4804-3AF3-B71B-5B70705C63D7
+  Functions: 97
+  Symbols:   564
   CStrings:  305
 
Symbols:
+ _OUTLINED_FUNCTION_4
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[ACCBLEPairingFeaturePlugin description] : 168 -> 176
~ -[ACCBLEPairingFeaturePlugin startPlugin] : 816 -> 768
~ -[ACCBLEPairingFeaturePlugin stopPlugin] : 460 -> 432
~ -[ACCBLEPairingFeaturePlugin blePairing:accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:] : 816 -> 780
~ -[ACCBLEPairingFeaturePlugin blePairing:accessoryDetached:blePairingUUID:] : 484 -> 460
~ ___74-[ACCBLEPairingFeaturePlugin blePairing:accessoryDetached:blePairingUUID:]_block_invoke : 508 -> 516
~ -[ACCBLEPairingFeaturePlugin blePairingStateUpdate:validMask:btRadioOn:pairingState:pairingModeOn:accessory:blePairingUUID:] : 560 -> 532
~ ___124-[ACCBLEPairingFeaturePlugin blePairingStateUpdate:validMask:btRadioOn:pairingState:pairingModeOn:accessory:blePairingUUID:]_block_invoke : 444 -> 448
~ -[ACCBLEPairingFeaturePlugin blePairingInfoUpdate:pairType:pairInfoList:accessory:blePairingUUID:] : 544 -> 512
~ ___98-[ACCBLEPairingFeaturePlugin blePairingInfoUpdate:pairType:pairInfoList:accessory:blePairingUUID:]_block_invoke : 436 -> 440
~ -[ACCBLEPairingFeaturePlugin blePairingDataUpdate:pairType:pairData:accessory:blePairingUUID:] : 544 -> 512
~ ___94-[ACCBLEPairingFeaturePlugin blePairingDataUpdate:pairType:pairData:accessory:blePairingUUID:]_block_invoke : 436 -> 440
~ -[ACCBLEPairingFeaturePlugin bleAccessoryForConnectionID:] : 244 -> 240
~ ___58-[ACCBLEPairingFeaturePlugin bleAccessoryForConnectionID:]_block_invoke : 128 -> 136
~ -[ACCBLEPairingFeaturePlugin deviceStartBLEUpdates:pairType:btRadio:pairInfo:] : 468 -> 448
~ ___78-[ACCBLEPairingFeaturePlugin deviceStartBLEUpdates:pairType:btRadio:pairInfo:]_block_invoke : 468 -> 472
~ -[ACCBLEPairingFeaturePlugin deviceStateUpdate:btRadio:pairStatus:pairModeOn:forceUpdates:] : 480 -> 468
~ ___91-[ACCBLEPairingFeaturePlugin deviceStateUpdate:btRadio:pairStatus:pairModeOn:forceUpdates:]_block_invoke : 476 -> 480
~ -[ACCBLEPairingFeaturePlugin deviceSend:pairType:pairingData:] : 472 -> 452
~ ___62-[ACCBLEPairingFeaturePlugin deviceSend:pairType:pairingData:]_block_invoke : 464 -> 468
~ -[ACCBLEPairingFeaturePlugin deviceUpdate:pairType:pairInfo:] : 472 -> 452
~ ___61-[ACCBLEPairingFeaturePlugin deviceUpdate:pairType:pairInfo:]_block_invoke : 464 -> 468
~ -[ACCBLEPairingFeaturePlugin deviceStopBLEUpdates:] : 400 -> 388
~ ___51-[ACCBLEPairingFeaturePlugin deviceStopBLEUpdates:]_block_invoke : 456 -> 460
~ -[ACCBLEPairingFeaturePlugin setIap2server:] : 12 -> 64
~ -[ACCBLEPairingFeaturePlugin setBlePairingProvider:] : 12 -> 64
~ -[ACCBLEPairingFeaturePlugin setBlePairingQueue:] : 12 -> 64
~ -[ACCBLEPairingFeaturePlugin setBlePairingShim:] : 12 -> 64
~ -[ACCBLEPairingFeaturePlugin setBlePairingAccessoryList:] : 12 -> 64
~ _OUTLINED_FUNCTION_0 : 24 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 24
+ _OUTLINED_FUNCTION_2
~ -[ACCBLEPairingAccessory setIap2ShimAccessory:] : 12 -> 64
~ -[ACCBLEPairingAccessory setBlePairingUUID:] : 12 -> 64
~ -[ACCBLEPairingAccessory setSupportedPairTypes:] : 12 -> 64
~ -[ACCBLEPairingShim initWithDelegate:] : 156 -> 164
~ -[ACCBLEPairingShim description] : 120 -> 124
~ -[ACCBLEPairingShim accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:] : 1044 -> 1052
~ _logObjectForModule : 132 -> 116
~ -[ACCBLEPairingShim accessoryDetached:blePairingUUID:] : 628 -> 616
~ -[ACCBLEPairingShim stateUpdate:blePairingUUID:validMask:btRadioOn:pairingState:pairingModeOn:] : 912 -> 908
~ -[ACCBLEPairingShim stateUpdate:blePairingUUID:pairType:pairInfoList:] : 528 -> 524
~ -[ACCBLEPairingShim dataUpdate:blePairingUUID:pairType:pairData:] : 528 -> 524
~ -[ACCBLEPairingShim getUID] : 8 -> 56
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:] : 2620 -> 2572
+ _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_3
~ ___98-[ACCBLEPairingFeaturePlugin blePairingInfoUpdate:pairType:pairInfoList:accessory:blePairingUUID:]_block_invoke.cold.1 : 112 -> 56
~ ___105-[ACCBLEPairingFeaturePlugin blePairing:accessoryAttached:blePairingUUID:accInfoDict:supportedPairTypes:]_block_invoke.cold.2 : 176 -> 180
~ _logObjectForModule.cold.1 : 144 -> 124
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.3 : 120 -> 92
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.4 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.6 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.8 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.10 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.12 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.14 : 60 -> 52
~ -[ACCBLEPairingShim tryProcessXPCMessage:connection:server:].cold.16 : 140 -> 112

```
