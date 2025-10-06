## otter

> `/usr/libexec/otter`

```diff

-146.0.0.0.0
-  __TEXT.__text: 0xb25c
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x5c0
+151.0.0.0.0
+  __TEXT.__text: 0xb420
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_stubs: 0x5e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x3c0
-  __TEXT.__cstring: 0x2ac3
+  __TEXT.__objc_methlist: 0x3d8
+  __TEXT.__cstring: 0x2b44
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x384
   __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0x6d2
+  __TEXT.__objc_methname: 0x702
   __TEXT.__objc_methtype: 0x28e
-  __TEXT.__unwind_info: 0x398
-  __DATA_CONST.__auth_got: 0x510
+  __TEXT.__unwind_info: 0x3a0
+  __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x408
-  __DATA_CONST.__cfstring: 0x580
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x6e8
-  __DATA.__objc_selrefs: 0x290
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x718
+  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x328
-  __DATA.__bss: 0x18da0
+  __DATA.__bss: 0x18ea0
   __DATA.__common: 0x3c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdpdk.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 73D97939-EFA7-30C5-A605-35802572531D
-  Functions: 254
-  Symbols:   1850
-  CStrings:  640
+  UUID: 07084AE8-6C3C-3608-ACDB-0EEF1569B58F
+  Functions: 257
+  Symbols:   1857
+  CStrings:  646
 
Symbols:
+ -[LatticeInterface offloads]
+ -[LatticeInterface setOffloads:]
+ OBJC_IVAR_$_LatticeInterface._offloads
+ _objc_msgSend$offloads
+ _passthrough_send_broadcast_from_downlink
+ _passthrough_send_broadcast_from_uplink
- /Library/Caches/com.apple.xbs/Binaries/AppleLatticeNetwork/install/TempContent/Objects/AppleLatticeNetwork.build/otter.build/Objects-normal/arm64e/PlainLogging.o
- /Library/Caches/com.apple.xbs/Sources/AppleLatticeNetwork/Tools/ringdpdktool/
- PlainLogging.cpp
- __ZN5AU4RN4vlogENS_8LogLevelEPKcPc
- _passthrough_send_broadcast
- _vprintf
CStrings:
+ "  offloads        = %u"
+ "--vdev=net_io_user_eth0,mac=%02X:%02X:%02X:%02X:%02X:%02X,mtu=4072,tso=1"
+ "-o|--checksum_offload Offload checksums to the uplink\n"
+ "BC:D:TU:bc:dfi:klptuvzo"
+ "Failed to configure driver (%s): %s\n"
+ "Failed to send on the uplink\n"
+ "Learnt mac: %02X:%02X:%02X:%02X:%02X:%02X id=%u\n"
+ "Neigh: Failed to send on the uplink\n"
+ "Requesting TCP offloads on %s\n"
+ "TC,N,V_offloads"
+ "_offloads"
+ "checksum-offload"
+ "offloads"
+ "setOffloads:"
- "--vdev=net_io_user_eth0,mac=%02X:%02X:%02X:%02X:%02X:%02X,mtu=4072"
- "BC:D:TU:bc:dfi:klptuvz"
- "Failed to configure driver\n"
- "Failed to send on the downlink"
- "Failed to send on the uplink"
- "Learnt mac: %02X:%02X:%02X:%02X:%02X:%02X\n"
- "[DEBUG] "
- "[ERROR] "
- "[INFO] "

```
