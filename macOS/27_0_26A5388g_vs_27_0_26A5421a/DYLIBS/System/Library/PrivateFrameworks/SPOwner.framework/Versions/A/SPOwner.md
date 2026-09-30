## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-449.20.6.14.15
-  __TEXT.__text: 0x7d8f0
-  __TEXT.__objc_methlist: 0xbd54
+449.20.6.14.21
+  __TEXT.__text: 0x7de28
+  __TEXT.__objc_methlist: 0xbe34
   __TEXT.__const: 0x5e8
   __TEXT.__gcc_except_tab: 0x1514
-  __TEXT.__cstring: 0x69c9
+  __TEXT.__cstring: 0x6a49
   __TEXT.__oslogstring: 0x8378
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x24e0
+  __TEXT.__unwind_info: 0x24f8
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x878
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e40
+  __DATA_CONST.__objc_selrefs: 0x3ea0
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x21d8
-  __AUTH_CONST.__cfstring: 0x6000
-  __AUTH_CONST.__objc_const: 0x14740
+  __DATA_CONST.__got: 0x610
+  __AUTH_CONST.__const: 0x2208
+  __AUTH_CONST.__cfstring: 0x6080
+  __AUTH_CONST.__objc_const: 0x14938
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH.__objc_data: 0x138
-  __DATA.__objc_ivar: 0xf54
+  __AUTH.__objc_data: 0x188
+  __DATA.__objc_ivar: 0xf6c
   __DATA.__data: 0x15f8
   __DATA.__bss: 0x660
   __DATA_DIRTY.__objc_data: 0x2a48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4407
-  Symbols:   8937
-  CStrings:  1586
+  Functions: 4426
+  Symbols:   8982
+  CStrings:  1591
 
Symbols:
+ +[SPCommand playSoundWithBeaconUUID:withContext:options:]
+ +[SPPlaySoundOptions supportsSecureCoding]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface collectionDifferenceSerialQueue]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setCollectionDifferenceSerialQueue:]
+ -[SPCommand initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:]
+ -[SPCommand playSoundOptions]
+ -[SPCommand setPlaySoundOptions:]
+ -[SPInternalSimpleBeacon isPairingIncomplete]
+ -[SPInternalSimpleBeacon setIsPairingIncomplete:]
+ -[SPPlaySoundOptions classicTimeout]
+ -[SPPlaySoundOptions copyWithZone:]
+ -[SPPlaySoundOptions encodeWithCoder:]
+ -[SPPlaySoundOptions initWithCoder:]
+ -[SPPlaySoundOptions setClassicTimeout:]
+ -[SPPlaySoundOptions setUseClassicIndividual:]
+ -[SPPlaySoundOptions useClassicIndividual]
+ -[SPUnifiedBeacon isPairingIncomplete]
+ -[SPUnifiedBeacon setIsPairingIncomplete:]
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._collectionDifferenceSerialQueue
+ OBJC_IVAR_$_SPCommand._playSoundOptions
+ OBJC_IVAR_$_SPInternalSimpleBeacon._isPairingIncomplete
+ OBJC_IVAR_$_SPPlaySoundOptions._classicTimeout
+ OBJC_IVAR_$_SPPlaySoundOptions._useClassicIndividual
+ OBJC_IVAR_$_SPUnifiedBeacon._isPairingIncomplete
+ _OBJC_CLASS_$_SPPlaySoundOptions
+ _OBJC_METACLASS_$_SPPlaySoundOptions
+ __OBJC_$_CLASS_METHODS_SPPlaySoundOptions
+ __OBJC_$_CLASS_PROP_LIST_SPPlaySoundOptions
+ __OBJC_$_INSTANCE_METHODS_SPPlaySoundOptions
+ __OBJC_$_INSTANCE_VARIABLES_SPPlaySoundOptions
+ __OBJC_$_PROP_LIST_SPPlaySoundOptions
+ __OBJC_CLASS_PROTOCOLS_$_SPPlaySoundOptions
+ __OBJC_CLASS_RO_$_SPPlaySoundOptions
+ __OBJC_METACLASS_RO_$_SPPlaySoundOptions
+ ___77-[SPBeaconManagerSimpleBeaconUpdateInterface setSimpleBeaconDifferenceBlock:]_block_invoke
+ ___77-[SPBeaconManagerSimpleBeaconUpdateInterface setSimpleBeaconDifferenceBlock:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs40w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16l
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$classicTimeout
+ _objc_msgSend$collectionDifferenceSerialQueue
+ _objc_msgSend$initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:
+ _objc_msgSend$isPairingIncomplete
+ _objc_msgSend$playSoundOptions
+ _objc_msgSend$playSoundWithBeaconUUID:withContext:options:
+ _objc_msgSend$setClassicTimeout:
+ _objc_msgSend$setIsPairingIncomplete:
+ _objc_msgSend$setUseClassicIndividual:
+ _objc_msgSend$useClassicIndividual
- -[SPCommand initWithBeaconUUID:type:expiration:duration:playSoundContext:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:]
- GCC_except_table58
- _objc_msgSend$initWithBeaconUUID:type:expiration:duration:playSoundContext:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:
CStrings:
+ "classicTimeout"
+ "com.apple.icloud.searchpartyd.simpleBeaconUpdate.collection"
+ "isPairingIncomplete"
+ "playSoundOptions"
+ "useClassicIndividual"
```
