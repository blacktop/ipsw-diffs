## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-110.40.15.0.0
-  __TEXT.__text: 0x484d0
-  __TEXT.__auth_stubs: 0x2a20
+110.60.5.0.0
+  __TEXT.__text: 0x47c74
+  __TEXT.__auth_stubs: 0x29f0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0xa4
   __TEXT.__const: 0x10d8
   __TEXT.__oslogstring: 0x1b0
-  __TEXT.__cstring: 0x5fab
+  __TEXT.__cstring: 0x5fdb
   __TEXT.__gcc_except_tab: 0x3c
   __TEXT.__objc_methname: 0x603
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methtype: 0x11e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xf58
+  __TEXT.__constg_swiftt: 0xf60
   __TEXT.__swift5_typeref: 0xe02
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0xc79

   __TEXT.__swift5_capture: 0xae8
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1bbc
-  __TEXT.__eh_frame: 0xcb8
-  __DATA_CONST.__auth_got: 0x1520
-  __DATA_CONST.__got: 0x660
+  __TEXT.__unwind_info: 0x1c74
+  __TEXT.__eh_frame: 0xd50
+  __DATA_CONST.__auth_got: 0x1508
+  __DATA_CONST.__got: 0x658
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x2cf8
+  __DATA_CONST.__const: 0x2d00
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x90

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1F71D3B3-AC68-3921-A6A8-9B99237CDA55
+  UUID: 470481D6-8F10-39C2-BBF2-92F7343AB1BC
   Functions: 1757
-  Symbols:   1011
+  Symbols:   1008
   CStrings:  604
 
Symbols:
+ _$s19RemotePairingDevice0B19DataStorageProviderP14numPairedPeersSiyKFTq
+ _$s7Network14NWProtocolQUICC7OptionsC17initialPacketSizeSivsTj
+ _$sSo17OS_dispatch_queueC19RemotePairingDeviceE10childQueue5label3qos10attributes20autoreleaseFrequencyABSS_8Dispatch0N3QoSVAbIE10AttributesVAbIE011AutoreleaseM0OtF
+ _$sSo17OS_dispatch_queueC19RemotePairingDeviceE22assertOnQueueHierarchyyyF
- _$s19RemotePairingDevice8DefaultsV25deviceTunnelKeepWiFiAliveSbvgZ
- _$s19RemotePairingDevice8DefaultsV43wirelessTunnelStartupPowerAssertionDurationSdvgZ
- _$s8Dispatch0A3QoSV7utilityACvgZ
- _$s8Dispatch0A9PredicateO7onQueueyACSo17OS_dispatch_queueCcACmFWC
- _$s8Dispatch0A9PredicateOMa
- _$s8Dispatch25_dispatchPreconditionTestySbAA0A9PredicateOF
- _sec_protocol_options_set_max_tls_protocol_version
CStrings:
+ "com.apple.dt.remotepairing.remotepairingdeviced.lockdownservice"
+ "com.apple.dt.remotepairing.remotepairingdeviced.networkcontrolchannel"
+ "com.apple.dt.remotepairing.remotepairingdeviced.networkpairing"
+ "com.apple.dt.remotepairing.remotepairingdeviced.remotexpc"
- "%{public}s: Failed to create power assertion for tunnel connection %{public}s: %d"
- "com.apple.remotepairing.tunnel."
- "remotepairingdeviced Tunnel connection"
- "remotepairingdeviced tunnel connection "

```
