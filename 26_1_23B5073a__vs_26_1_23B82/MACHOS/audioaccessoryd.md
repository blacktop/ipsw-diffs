## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-31.10.0.0.0
-  __TEXT.__text: 0x1fc01c
+31.10.1.1.0
+  __TEXT.__text: 0x1fc36c
   __TEXT.__auth_stubs: 0x2b00
   __TEXT.__objc_stubs: 0x183e0
-  __TEXT.__objc_methlist: 0xbc2c
+  __TEXT.__objc_methlist: 0xbc1c
   __TEXT.__const: 0x3f60
   __TEXT.__gcc_except_tab: 0x4dc8
-  __TEXT.__cstring: 0x435b3
+  __TEXT.__cstring: 0x43653
   __TEXT.__objc_classname: 0xa27
-  __TEXT.__objc_methname: 0x24553
+  __TEXT.__objc_methname: 0x2453e
   __TEXT.__objc_methtype: 0x32e2
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca

   __DATA_CONST.__auth_got: 0x1590
   __DATA_CONST.__got: 0xca8
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xab40
-  __DATA_CONST.__cfstring: 0x9c20
+  __DATA_CONST.__const: 0xab10
+  __DATA_CONST.__cfstring: 0x9ce0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x1a328
-  __DATA.__objc_selrefs: 0x7b60
+  __DATA.__objc_selrefs: 0x7b58
   __DATA.__objc_ivar: 0x14b4
   __DATA.__objc_data: 0x2a68
   __DATA.__data: 0x4268

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CC1B22CD-4CAC-3397-AB3A-0CC62BE7BEB9
-  Functions: 9342
+  UUID: 6DFBA8B8-C0B3-3EB2-9F4D-993EC3639279
+  Functions: 9346
   Symbols:   1242
-  CStrings:  14719
+  CStrings:  14732
 
CStrings:
+ "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
+ "-[BTServicesDaemon openRadarforAudioQuality]"
+ "1551854"
+ "815886"
+ "Bluetooth Audio Quality Feedback"
+ "CoreBluetooth - HFP Audio | iOS"
+ "Keywords"
+ "Performance"
+ "audioQuality - File Radar"
+ "audioQuality banner timeout"
+ "audioQuality user click, openradar"
+ "audioQuality user dismiss"
+ "audioQuality: banner action: %s, %{error}"
+ "audioQuality: banner error for device %@"
- "-[BTSmartRoutingDaemon triggerBtStateUpdate]_block_invoke"
- "-[SRSourceDevice setBluetoothState:]"
- "EvaluateNearbyDevicesForConnection: Invalid BT state %s, triggering update"
- "Setting bluetoothState %s -> %s"
- "TriggerBtStateUpdate: Failed. cbDiscovery is null"
- "TriggerBtStateUpdate: cbDiscoveryBT %s sourceBT %s"
- "triggerBtStateUpdate"

```
