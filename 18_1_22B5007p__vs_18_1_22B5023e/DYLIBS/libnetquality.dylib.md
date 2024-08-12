## libnetquality.dylib

> `/usr/lib/libnetquality.dylib`

```diff

-140.0.0.0.0
-  __TEXT.__text: 0x18750
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x1388
-  __TEXT.__const: 0x176
-  __TEXT.__gcc_except_tab: 0x530
-  __TEXT.__cstring: 0x2425
+146.0.0.0.0
+  __TEXT.__text: 0x1841c
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x1418
+  __TEXT.__const: 0x188
+  __TEXT.__gcc_except_tab: 0x53c
+  __TEXT.__cstring: 0x231d
   __TEXT.__oslogstring: 0x1625
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x3b5b
-  __TEXT.__objc_methtype: 0xc44
-  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__objc_classname: 0x315
+  __TEXT.__objc_methname: 0x3e46
+  __TEXT.__objc_methtype: 0xc57
+  __TEXT.__objc_stubs: 0x3280
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x5a8
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde8
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_selrefs: 0xe28
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0x3970
+  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__objc_const: 0x3b18
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x7a0
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x388
-  __DATA.__data: 0x330
-  __DATA.__bss: 0x28
+  __AUTH.__objc_data: 0x780
+  __DATA.__objc_ivar: 0x3c0
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x20
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 550
-  Symbols:   805
-  CStrings:  1373
+  Functions: 548
+  Symbols:   825
+  CStrings:  1400
 
Symbols:
+ _nw_parameters_set_traffic_class
+ _nw_quic_connection_set_enable_l4s
- __swift_FORCE_LOAD_$_swiftCoreFoundation
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDispatch
- __swift_FORCE_LOAD_$_swiftFoundation
- __swift_FORCE_LOAD_$_swiftObjectiveC
- __swift_FORCE_LOAD_$_swiftXPC
- _objc_opt_self
- _swift_beginAccess
- _swift_getObjCClassMetadata
CStrings:
+ "\x11\x1f\x0f\x02"
+ "AV"
+ "BE"
+ "BK"
+ "BK_SYS"
+ "CTL"
+ "OAM"
+ "RD"
+ "RV"
+ "SIG"
+ "T@\"NSString\",C,V_latencyMeasurementServiceType"
+ "T@\"NSString\",C,V_loadGeneratingNetworkServiceType"
+ "TB,N,V_bonjourEnabled"
+ "TB,N,V_l4sEnabled"
+ "TB,N,V_mirrorServerIP"
+ "TB,N,V_tlsEnabled"
+ "TI,N,V_httpProtocol"
+ "TI,N,V_idleTimeoutSeconds"
+ "TQ,V_latencyMeasurementServiceType"
+ "TQ,V_loadGeneratingNetworkServiceType"
+ "TQ,V_networkServiceType"
+ "Ti,N,V_listenPort"
+ "VI"
+ "VO"
+ "_bonjourEnabled"
+ "_httpProtocol"
+ "_idleTimeoutSeconds"
+ "_l4sEnabled"
+ "_latencyMeasurementServiceType"
+ "_listenPort"
+ "_loadGeneratingNetworkServiceType"
+ "_mirrorServerIP"
+ "_networkServiceType"
+ "_tlsEnabled"
+ "accurate_ecn"
+ "l4sEnabled"
+ "latencyMeasurementServiceType"
+ "latencyMeasurementServiceType"
+ "loadGeneratingNetworkServiceType"
+ "loadGeneratingNetworkServiceType"
+ "networkServiceType"
+ "networkTrafficClass"
+ "setL4sEnabled:"
+ "setLatencyMeasurementServiceType:"
+ "setLoadGeneratingNetworkServiceType:"
+ "setNetworkServiceType:"
- "\x11\x1f\x0f"
- "TB,N,VbonjourEnabled"
- "TB,N,VmirrorServerIP"
- "TB,N,VtlsEnabled"
- "TI,N,VhttpProtocol"
- "TI,N,VidleTimeoutSeconds"
- "Ti,N,VlistenPort"
- "l4s"

```
