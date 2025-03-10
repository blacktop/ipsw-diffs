## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-199.100.18.0.0
-  __TEXT.__text: 0x63338
-  __TEXT.__auth_stubs: 0x3140
+199.100.20.0.0
+  __TEXT.__text: 0x64988
+  __TEXT.__auth_stubs: 0x31d0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x1cc2
-  __TEXT.__oslogstring: 0x31b9
+  __TEXT.__oslogstring: 0x32c9
   __TEXT.__cstring: 0x599b
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__objc_methname: 0x5d1
   __TEXT.__objc_classname: 0xd8
   __TEXT.__objc_methtype: 0x11e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1888
-  __TEXT.__swift5_typeref: 0x1496
+  __TEXT.__constg_swiftt: 0x18a8
+  __TEXT.__swift5_typeref: 0x14c6
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1579
-  __TEXT.__swift5_fieldmd: 0xe58
+  __TEXT.__swift5_reflstr: 0x1599
+  __TEXT.__swift5_fieldmd: 0xe64
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift5_capture: 0xef0
+  __TEXT.__swift5_capture: 0xf38
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1260
-  __TEXT.__eh_frame: 0x10a0
-  __DATA_CONST.__auth_got: 0x18b0
-  __DATA_CONST.__got: 0x918
-  __DATA_CONST.__auth_ptr: 0x6e0
-  __DATA_CONST.__const: 0x3188
+  __TEXT.__unwind_info: 0x1250
+  __TEXT.__eh_frame: 0x1040
+  __DATA_CONST.__auth_got: 0x18f8
+  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__auth_ptr: 0x700
+  __DATA_CONST.__const: 0x3200
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x48a8
+  __DATA.__objc_const: 0x48c8
   __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x3200
+  __DATA.__data: 0x3270
   __DATA.__bss: 0xd90
   __DATA.__common: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2103
-  Symbols:   1226
-  CStrings:  783
+  Functions: 2101
+  Symbols:   1243
+  CStrings:  786
 
Symbols:
+ _$s19RemotePairingDevice21ControlChannelMessageO5EventO18connectionRejectedyA2EmFWC
+ _$s19RemotePairingDevice21ControlChannelMessageO5EventOMa
+ _$s19RemotePairingDevice21ControlChannelMessageO5eventyA2C5EventOcACmFWC
+ _$s19RemotePairingDevice21ControlChannelMessageOMa
+ _$s19RemotePairingDevice24ControlChannelConnectionC8PeerTypeO4hostyA2EmFWC
+ _$s19RemotePairingDevice24ControlChannelConnectionC8PeerTypeOMa
+ _$s19RemotePairingDevice29ControlChannelMessageEnvelopeV0F0O5plainyAeA0deF0OcAEmFWC
+ _$s19RemotePairingDevice29ControlChannelMessageEnvelopeV0F0OMa
+ _$s19RemotePairingDevice29ControlChannelMessageEnvelopeV12originatedBy14sequenceNumber7messageAcA0dE10ConnectionC8PeerTypeO_s6UInt64VAC0F0OtcfC
+ _$s19RemotePairingDevice29ControlChannelMessageEnvelopeVMa
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportC10invalidateyyFTj
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportC2idSSvgTj
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportC5start15withTargetQueue12eventHandlerySo17OS_dispatch_queueC_yAA0fgH5EventOctFTj
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCAA013JSONDataBasedfgH0AAWP
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCMn
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCSHAAMc
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCSQAAMc
CStrings:
+ "Completed send of connection rejected message to rejected peer connection %{public}s. Invalidating"
+ "Rejected peer connection %{public}s started. Will send connection rejected message"
+ "Rejecting bluetooth control channel connection from peer: %@"
+ "rejectedConnectionsPendingTeardown"
- "Rejecting bluetooth control channel connection"

```
