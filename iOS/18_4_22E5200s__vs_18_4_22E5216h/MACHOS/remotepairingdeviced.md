## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-199.100.14.0.0
-  __TEXT.__text: 0x5f894
-  __TEXT.__auth_stubs: 0x3110
+199.100.18.0.0
+  __TEXT.__text: 0x63338
+  __TEXT.__auth_stubs: 0x3140
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x1ad2
-  __TEXT.__oslogstring: 0x2f49
-  __TEXT.__cstring: 0x548b
+  __TEXT.__const: 0x1cc2
+  __TEXT.__oslogstring: 0x31b9
+  __TEXT.__cstring: 0x599b
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0x5ab
+  __TEXT.__objc_methname: 0x5d1
   __TEXT.__objc_classname: 0xd8
   __TEXT.__objc_methtype: 0x11e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1710
-  __TEXT.__swift5_typeref: 0x13b8
+  __TEXT.__constg_swiftt: 0x1888
+  __TEXT.__swift5_typeref: 0x1496
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1399
-  __TEXT.__swift5_fieldmd: 0xd24
+  __TEXT.__swift5_reflstr: 0x1579
+  __TEXT.__swift5_fieldmd: 0xe58
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x94
-  __TEXT.__swift5_types: 0xa4
-  __TEXT.__swift5_capture: 0xe44
-  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x9c
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_capture: 0xef0
+  __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x11d0
-  __TEXT.__eh_frame: 0x1018
-  __DATA_CONST.__auth_got: 0x1898
-  __DATA_CONST.__got: 0x868
-  __DATA_CONST.__auth_ptr: 0x8a0
-  __DATA_CONST.__const: 0x2ec0
+  __TEXT.__unwind_info: 0x1260
+  __TEXT.__eh_frame: 0x10a0
+  __DATA_CONST.__auth_got: 0x18b0
+  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__auth_ptr: 0x6e0
+  __DATA_CONST.__const: 0x3188
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x42c8
-  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_const: 0x48a8
+  __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x3000
+  __DATA.__data: 0x3200
   __DATA.__bss: 0xd90
   __DATA.__common: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2018
-  Symbols:   1220
-  CStrings:  754
+  Functions: 2103
+  Symbols:   1226
+  CStrings:  783
 
Symbols:
+ _$s10Foundation22_convertNSErrorToErrorys0E0_pSo0C0CSgF
+ _$s19RemotePairingDevice0B19DataStorageProviderP44updateLastSeenWireProtocolVersionIfNecessary3for2toySo12CUPairedPeerC_AA024ControlChannelConnectionjkL0CtKFTq
+ _$s19RemotePairingDevice0B19DataStorageProviderPAAE44updateLastSeenWireProtocolVersionIfNecessary3for2toySo12CUPairedPeerC_AA024ControlChannelConnectionjkL0CtKF
+ _$s19RemotePairingDevice23ListenerStartedResponseV4port18deviceRawPublicKey11serviceNameACs6UInt16V_10Foundation4DataVSStcfC
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportC10connectionACSo12CBConnectionC_tcfc
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCAA0fgH0AAWP
+ _$s19RemotePairingDevice44BluetoothLEConnectionControlChannelTransportCMa
+ _OBJC_CLASS_$_CBConnection
+ _objc_retain_x9
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _$s19RemotePairingDevice23ListenerStartedResponseV4port18deviceRawPublicKeyACs6UInt16V_10Foundation4DataVtcfC
- _NSClassFromString
- _objc_retain_x12
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "$__lazy_storage_$_bluetoothControlChannelService"
+ "$__lazy_storage_$_lockdownStateService"
+ "BT Peers updated. Total count: %ld"
+ "BluetoothControlChannelConnectionService control channel connection: %{public}s"
+ "BluetoothControlChannelConnectionService state: connection count = %ld"
+ "BluetoothControlChannelConnectionService: Ignoring shutdown request as service is already shutting down"
+ "EnableWifiConnections"
+ "EnableWifiDebugging"
+ "Failed to construct CBConnection instance from XPC event: %{public}s"
+ "LockdownControlChannelService: Ignoring shutdown request as service is already shutting down"
+ "Not initializing real LockdownControlChannelService as liblockdown is not available"
+ "Not starting %s as CoreBluetooth is not available at runtime"
+ "Received CBConnection XPC event %s"
+ "Received new CBConnection from peer: %@"
+ "Received notification that lockdown wireless connections did change. Invalidating previously computed metadata"
+ "Received updated wireless configuration from lockdown: %{public}s"
+ "Refreshing wireless configuration from lockdown"
+ "Rejecting bluetooth control channel connection"
+ "Rejecting incoming BT connection as RemotePairing support is disabled"
+ "Rejecting incoming BT connection as service is shutting down"
+ "Rejecting incoming BT connection as we already have %ld BT peers"
+ "Rejecting incoming BT connection due to 'deviceAllowBluetoothDeviceDiscovery' not being set to true"
+ "Rejecting incoming BT connection due to no hosts being paired"
+ "State dump: LockdownControlChannelService control channel connection: %{public}s"
+ "_TtC20remotepairingdeviced20LockdownStateService"
+ "_TtC20remotepairingdeviced29LockdownControlChannelService"
+ "_TtC20remotepairingdeviced34DummyLockdownControlChannelService"
+ "_TtC20remotepairingdeviced40BluetoothControlChannelConnectionService"
+ "_lockdownStateService"
+ "com.apple.bluetooth.connections"
+ "com.apple.dt.remotepairing.remotepairingdeviced.LockdownStateService.lockdown"
+ "com.apple.dt.remotepairing.remotepairingdeviced.btcontrolchannel"
+ "initWithXPCEventRepresentation:error:"
+ "lockdownstateservice"
- "LockdownService: Ignoring shutdown request as service is already shutting down"
- "Not initializing real LockdownService as liblockdown is not available"
- "State dump: LockdownService control channel connection: %{public}s"
- "_TtC20remotepairingdeviced15LockdownService"
- "_TtC20remotepairingdeviced20DummyLockdownService"

```
