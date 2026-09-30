## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2175.13.1.0.0
-  __TEXT.__text: 0xae454
+2175.14.1.1.0
+  __TEXT.__text: 0xae648
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8dd8
+  __TEXT.__objc_methlist: 0x8e40
   __TEXT.__const: 0x24e8
-  __TEXT.__cstring: 0xeac8
+  __TEXT.__cstring: 0xead2
   __TEXT.__oslogstring: 0xc712
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0xa0
   __TEXT.__unwind_info: 0x16e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1bfcb
+  __TEXT.__objc_methname: 0x1c0f3
   __TEXT.__objc_methtype: 0x2478
-  __TEXT.__objc_stubs: 0xef20
+  __TEXT.__objc_stubs: 0xef80
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xda0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4340
+  __DATA_CONST.__objc_selrefs: 0x4368
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdf20
-  __AUTH_CONST.__objc_const: 0x169f8
+  __AUTH_CONST.__cfstring: 0xdf60
+  __AUTH_CONST.__objc_const: 0x16ab8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2044
+  __DATA.__objc_ivar: 0x2054
   __DATA.__data: 0x738
   __DATA.__bss: 0x78
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3D55B076-11EF-3F66-B8E3-39D761E6E322
-  Functions: 3978
-  Symbols:   13101
-  CStrings:  9307
+  UUID: D06CDF9C-E53C-39CF-A1A9-34EFDB48A533
+  Functions: 3987
+  Symbols:   13126
+  CStrings:  9320
 
Symbols:
+ -[MultiwayCall currentLocalSatelliteStatus]
+ -[MultiwayCall currentRemoteSatelliteStatus]
+ -[MultiwayCall setCurrentLocalSatelliteStatus:]
+ -[MultiwayCall setCurrentRemoteSatelliteStatus:]
+ -[MultiwaySegment currentLocalSatelliteStatus]
+ -[MultiwaySegment currentRemoteSatelliteStatus]
+ -[MultiwaySegment setCurrentLocalSatelliteStatus:]
+ -[MultiwaySegment setCurrentRemoteSatelliteStatus:]
+ -[VCAggregatorMultiway updateCurrentSatelliteNetworkStatusWithPayload:]
+ _OBJC_IVAR_$_MultiwayCall._currentLocalSatelliteStatus
+ _OBJC_IVAR_$_MultiwayCall._currentRemoteSatelliteStatus
+ _OBJC_IVAR_$_MultiwaySegment._currentLocalSatelliteStatus
+ _OBJC_IVAR_$_MultiwaySegment._currentRemoteSatelliteStatus
+ _objc_msgSend$setCurrentLocalSatelliteStatus:
+ _objc_msgSend$setCurrentRemoteSatelliteStatus:
+ _objc_msgSend$updateCurrentSatelliteNetworkStatusWithPayload:
CStrings:
+ "LSAT"
+ "RSAT"
+ "TC,V_currentLocalSatelliteStatus"
+ "TC,V_currentRemoteSatelliteStatus"
+ "[81B]"
+ "_currentLocalSatelliteStatus"
+ "_currentRemoteSatelliteStatus"
+ "currentLocalSatelliteStatus"
+ "currentRemoteSatelliteStatus"
+ "setCurrentLocalSatelliteStatus:"
+ "setCurrentRemoteSatelliteStatus:"
+ "updateCurrentSatelliteNetworkStatusWithPayload:"
- "[80B]"

```
