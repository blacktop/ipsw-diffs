## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-190.40.1.2.0
-  __TEXT.__text: 0xb3c90
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0xa044
-  __TEXT.__const: 0x2703
+190.43.0.0.0
+  __TEXT.__text: 0xb41a0
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_methlist: 0xa074
+  __TEXT.__const: 0x271b
   __TEXT.__oslogstring: 0x2b1b
-  __TEXT.__cstring: 0x14ecf
-  __TEXT.__gcc_except_tab: 0x2f30
+  __TEXT.__cstring: 0x14f22
+  __TEXT.__gcc_except_tab: 0x2f40
   __TEXT.__ustring: 0x82
   __TEXT.__unwind_info: 0x21d8
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x805
-  __TEXT.__objc_methname: 0x16b50
-  __TEXT.__objc_methtype: 0x24e8
-  __TEXT.__objc_stubs: 0xb600
+  __TEXT.__objc_methname: 0x16bb8
+  __TEXT.__objc_methtype: 0x251a
+  __TEXT.__objc_stubs: 0xb680
   __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0x5578
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fd8
+  __DATA_CONST.__objc_selrefs: 0x4ff8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x9b8
+  __AUTH_CONST.__auth_got: 0x9c8
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0xdba0
-  __AUTH_CONST.__objc_const: 0x11dc8
+  __AUTH_CONST.__objc_const: 0x11e68
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0xf64
+  __DATA.__objc_ivar: 0xf74
   __DATA.__data: 0xe68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1040

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9775BC6-948C-360F-BC28-403CDE608F19
-  Functions: 4234
-  Symbols:   13766
-  CStrings:  10423
+  UUID: EDB11C70-DF5F-31E4-9D5F-C7C5782675B5
+  Functions: 4237
+  Symbols:   13782
+  CStrings:  10438
 
Symbols:
+ -[CBHIDPerformanceSummary P75Max]
+ -[CBHIDPerformanceSummary P75]
+ -[CBHIDPerformanceSummary setP75:]
+ -[CBHIDPerformanceSummary setP75Max:]
+ _CFRetain
+ _OBJC_IVAR_$_CBCentralManager.peripheralsMutex
+ _OBJC_IVAR_$_CBHIDPerformanceMonitor._statsPacketP75Max
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P75
+ _OBJC_IVAR_$_CBHIDPerformanceSummary._P75Max
+ ___block_literal_global.184
+ ___block_literal_global.781
+ _objc_msgSend$P75
+ _objc_msgSend$P75Max
+ _objc_msgSend$setP75:
+ _objc_msgSend$setP75Max:
+ _pthread_mutex_init
- GCC_except_table34
- GCC_except_table49
- ___block_literal_global.174
- ___block_literal_global.777
CStrings:
+ "### Snapshot: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms, P50 %.2fms, P90 %.2fms, P95 %.2fms, P99 %.2fms"
+ "### Summary: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms(%.2fms), P75 %.2fms(%.2fms), P90 %.2fms(%.2fms), P95 %.2fms(%.2fms), P99 %.2fms(%.2fms)"
+ ", AcID <private> "
+ ", BDA <private>"
+ ", Nm <private> "
+ "MobileBluetooth-190.43"
+ "P75"
+ "P75Max"
+ "Td,N,V_P75"
+ "Td,N,V_P75Max"
+ "_P75"
+ "_P75Max"
+ "_statsPacketP75Max"
+ "dvIF"
+ "peripheralsMutex"
+ "setP75:"
+ "setP75Max:"
+ "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
+ "\xc1"
- "### Snapshot: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms, P90 %.2fms, P95 %.2fms, P99 %.2fms"
- "### Summary: Packet TS 0x%016llX, Actual %llu, Expected %llu, Delta %lld, ErrorRate %.2f%%, Interval %.3f ms, MaxInterval %.3f ms, RSSI %d, P50 %.2fms(%.2fms), P90 %.2fms(%.2fms), P95 %.2fms(%.2fms), P99 %.2fms(%.2fms)"
- "A"
- "MobileBluetooth-190.40.1.1"

```
