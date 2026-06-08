## sensorkitd

> `/usr/libexec/sensorkitd`

```diff

-972.0.21.0.0
-  __TEXT.__text: 0x42d4c
+1025.0.0.0.0
+  __TEXT.__text: 0x41d94
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x3860
-  __TEXT.__objc_methlist: 0x2594
+  __TEXT.__objc_stubs: 0x3880
+  __TEXT.__objc_methlist: 0x25e4
   __TEXT.__const: 0x158
-  __TEXT.__objc_methname: 0x5c6b
-  __TEXT.__objc_classname: 0x8ed
-  __TEXT.__objc_methtype: 0x2785
-  __TEXT.__cstring: 0x2fc4
-  __TEXT.__oslogstring: 0x703d
-  __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__unwind_info: 0xa18
-  __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x1010
-  __DATA_CONST.__cfstring: 0x32a0
-  __DATA_CONST.__objc_classlist: 0x1c8
-  __DATA_CONST.__objc_catlist: 0x38
+  __TEXT.__objc_methname: 0x5d22
+  __TEXT.__objc_classname: 0x8f5
+  __TEXT.__objc_methtype: 0x27e7
+  __TEXT.__cstring: 0x2f96
+  __TEXT.__oslogstring: 0x7098
+  __TEXT.__gcc_except_tab: 0x648
+  __TEXT.__unwind_info: 0xa20
+  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__cfstring: 0x3280
+  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0x498
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x5e08
-  __DATA.__objc_selrefs: 0x1428
-  __DATA.__objc_ivar: 0x438
-  __DATA.__objc_data: 0x11d0
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x378
+  __DATA.__objc_const: 0x5fd0
+  __DATA.__objc_selrefs: 0x1440
+  __DATA.__objc_ivar: 0x454
+  __DATA.__objc_data: 0x1220
   __DATA.__data: 0x11a8
   __DATA.__bss: 0x1e0
   __DATA.__common: 0x30

   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 636A0DBE-85B8-3495-AEED-E4BC94C09FB4
-  Functions: 816
-  Symbols:   325
-  CStrings:  2680
+  UUID: C4F3D08E-3481-3E44-A811-CA8F82288AE7
+  Functions: 821
+  Symbols:   324
+  CStrings:  2689
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyEnclosureMaterial
+ _PDRDevicePropertyKeyLocalizedModel
+ _PDRDevicePropertyKeyName
+ _PDRDevicePropertyKeyProductType
+ _PDRDevicePropertyKeySystemBuildVersion
+ _PDRDevicePropertyKeySystemName
+ _PDRDevicePropertyKeySystemVersion
- _NRDevicePropertyEnclosureMaterial
- _NRDevicePropertyLocalizedModel
- _NRDevicePropertyName
- _NRDevicePropertyPairingID
- _NRDevicePropertyProductType
- _NRDevicePropertySystemBuildVersion
- _NRDevicePropertySystemName
- _NRDevicePropertySystemVersion
- _OBJC_CLASS_$_NRPairedDeviceRegistry
CStrings:
+ "@\"RDReadableDatastore\""
+ "Converting auto-enable recording request for legacy name %{public}@ to new name %{public}@"
+ "RDSampleEnumerator"
+ "_datastore"
+ "_end"
+ "_error"
+ "_exhausted"
+ "_latestSampleTime"
+ "deviceForBluetoothID:"
+ "deviceForPairingID:"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "sk_deviceForIDSDevice:"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
- "9b084186-2b81-4526-9a7d-ad719ec81c83"
- "B16@?0@\"NRDevice\"8"
- "deviceForIDSDevice:"
- "getDevicesMatching:"

```
