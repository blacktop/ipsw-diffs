## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-449.30.6.14.15
-  __TEXT.__text: 0x77470
-  __TEXT.__objc_methlist: 0xbb2c
+449.30.6.14.26
+  __TEXT.__text: 0x77954
+  __TEXT.__objc_methlist: 0xbc0c
   __TEXT.__const: 0x5b8
   __TEXT.__gcc_except_tab: 0x15a0
-  __TEXT.__cstring: 0x6a49
+  __TEXT.__cstring: 0x6ac9
   __TEXT.__oslogstring: 0x7fa8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x148

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2738
+  __TEXT.__unwind_info: 0x2760
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2168
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__const: 0x2190
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d98
+  __DATA_CONST.__objc_selrefs: 0x3df8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__got: 0x600
   __AUTH_CONST.__const: 0xbd8
-  __AUTH_CONST.__cfstring: 0x5e80
-  __AUTH_CONST.__objc_const: 0x14178
+  __AUTH_CONST.__cfstring: 0x5f00
+  __AUTH_CONST.__objc_const: 0x14370
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x698
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xefc
+  __AUTH.__objc_data: 0x98
+  __DATA.__objc_ivar: 0xf14
   __DATA.__data: 0x15c0
   __DATA.__bss: 0x800
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4392
-  Symbols:   8713
-  CStrings:  1572
+  Functions: 4411
+  Symbols:   8759
+  CStrings:  1577
 
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
+ GCC_except_table47
+ _OBJC_CLASS_$_SPPlaySoundOptions
+ _OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._collectionDifferenceSerialQueue
+ _OBJC_IVAR_$_SPCommand._playSoundOptions
+ _OBJC_IVAR_$_SPInternalSimpleBeacon._isPairingIncomplete
+ _OBJC_IVAR_$_SPPlaySoundOptions._classicTimeout
+ _OBJC_IVAR_$_SPPlaySoundOptions._useClassicIndividual
+ _OBJC_IVAR_$_SPUnifiedBeacon._isPairingIncomplete
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
+ ___block_descriptor_48_e8_32bs40w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw40l8s32l8
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
- GCC_except_table45
- _objc_msgSend$initWithBeaconUUID:type:expiration:duration:playSoundContext:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:
CStrings:
+ "classicTimeout"
+ "com.apple.icloud.searchpartyd.simpleBeaconUpdate.collection"
+ "isPairingIncomplete"
+ "playSoundOptions"
+ "useClassicIndividual"
```
