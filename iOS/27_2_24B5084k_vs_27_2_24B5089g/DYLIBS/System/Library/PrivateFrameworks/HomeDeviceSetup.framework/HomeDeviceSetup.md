## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-405.10.26.0.0
-  __TEXT.__text: 0x710fc
-  __TEXT.__objc_methlist: 0x3484
+405.10.29.0.0
+  __TEXT.__text: 0x70abc
+  __TEXT.__objc_methlist: 0x3474
   __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x1aae4
+  __TEXT.__cstring: 0x1a864
   __TEXT.__oslogstring: 0x81d
   __TEXT.__gcc_except_tab: 0x294
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x2580
+  __TEXT.__unwind_info: 0x2568
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1980
+  __DATA_CONST.__const: 0x1960
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dd0
+  __DATA_CONST.__objc_selrefs: 0x2dc0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
   __DATA_CONST.__got: 0x410
-  __AUTH_CONST.__const: 0xc38
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0x78d8
+  __AUTH_CONST.__const: 0xc18
+  __AUTH_CONST.__cfstring: 0x5580
+  __AUTH_CONST.__objc_const: 0x78a8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x850
   __AUTH.__objc_data: 0x778
   __AUTH.__data: 0x328
-  __DATA.__objc_ivar: 0xa50
+  __DATA.__objc_ivar: 0xa4c
   __DATA.__data: 0xb78
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3080
-  Symbols:   4381
-  CStrings:  3122
+  Functions: 3069
+  Symbols:   4377
+  CStrings:  3113
 
Symbols:
+ +[HDSDefaults getOptionalBoolForKey:]
+ -[HDSSetupSession _runFinishComplete]
+ -[HDSSetupSession _stereoCounterpartExpectedModelPrefix]
+ GCC_except_table311
+ GCC_except_table374
+ GCC_except_table426
+ ___37-[HDSSetupSession _runFinishComplete]_block_invoke
+ _objc_msgSend$_runFinishComplete
+ _objc_msgSend$_stereoCounterpartExpectedModelPrefix
+ _objc_msgSend$peerDevice
- -[HDSDeviceOperationHomeKitSetup _idsIdentifiersForAccessories:companionLinkClient:]
- -[HDSDeviceOperationHomeKitSetup companionLinkClient]
- -[HDSDeviceOperationHomeKitSetup modelForStereoPairVersion:]
- -[HDSDeviceOperationHomeKitSetup setCompanionLinkClient:]
- GCC_except_table310
- GCC_except_table372
- GCC_except_table424
- _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._companionLinkClient
- ___44-[HDSSetupSession _runFinishResponse:error:]_block_invoke
- ___84-[HDSDeviceOperationHomeKitSetup _idsIdentifiersForAccessories:companionLinkClient:]_block_invoke
- ___84-[HDSDeviceOperationHomeKitSetup _idsIdentifiersForAccessories:companionLinkClient:]_block_invoke_2
- ___block_descriptor_32_e38_B32?0"RPCompanionLinkDevice"8Q16^B24l
- _objc_msgSend$dictionary
- _objc_msgSend$setCompanionLinkClient:
CStrings:
+ "-[HDSSetupSession _runFinishComplete]"
+ "-[HDSSetupSession _runFinishComplete]_block_invoke"
+ "Ignoring color from %@ (model %@), setting up model code %d\n"
- "### _idsIdentifiersForAccessories: %@ has no IDS identifier\n"
- "### _idsIdentifiersForAccessories: %@ not found in Rapport\n"
- "### _idsIdentifiersForAccessories: nil accessories or client\n"
- "### _idsIdentifiersForAccessories: no active devices\n"
- "### _idsIdentifiersForAccessories: unregistered device has no IDS identifier\n"
- "-[HDSDeviceOperationHomeKitSetup _idsIdentifiersForAccessories:companionLinkClient:]"
- "-[HDSSetupSession _runFinishResponse:error:]_block_invoke"
- "AudioAccessory6,1"
- "_idsIdentifiersForAccessories: %@ -> IDS: %@ (matched as unregistered device, model: %@)\n"
- "_idsIdentifiersForAccessories: %@ -> IDS: %@ (matched by HomeKit UUID)\n"
- "_idsIdentifiersForAccessories: %@ not found by HomeKit UUID, checking for unregistered device\n"
- "_idsIdentifiersForAccessories: activeDevices count=%lu\n"
```
