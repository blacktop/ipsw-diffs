## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-4026.140.2.0.0
-  __TEXT.__text: 0x30ecfc
-  __TEXT.__objc_methlist: 0x2b8bc
+4026.200.11.0.0
+  __TEXT.__text: 0x30eeb4
+  __TEXT.__objc_methlist: 0x2b92c
   __TEXT.__const: 0x5d8
-  __TEXT.__cstring: 0x2c5ce
-  __TEXT.__oslogstring: 0xd361
-  __TEXT.__gcc_except_tab: 0x5898
+  __TEXT.__cstring: 0x2c532
+  __TEXT.__oslogstring: 0xd3b8
+  __TEXT.__gcc_except_tab: 0x58c0
   __TEXT.__dlopen_cstrs: 0x40b
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xe2e8
+  __TEXT.__unwind_info: 0xe2f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b80
+  __DATA_CONST.__const: 0x4b98
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf130
+  __DATA_CONST.__objc_selrefs: 0xf158
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xff0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x1420
+  __DATA_CONST.__got: 0x1428
   __AUTH_CONST.__const: 0xa420
-  __AUTH_CONST.__cfstring: 0x23e40
-  __AUTH_CONST.__objc_const: 0x46660
+  __AUTH_CONST.__cfstring: 0x23e00
+  __AUTH_CONST.__objc_const: 0x466c0
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x8430
-  __DATA.__objc_ivar: 0x32f0
+  __DATA.__objc_ivar: 0x32f4
   __DATA.__data: 0x1a08
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2d50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20600
-  Symbols:   35160
-  CStrings:  6512
+  Functions: 20607
+  Symbols:   35174
+  CStrings:  6511
 
Symbols:
+ +[MRCBProductInfo isWXDeviceWithModelID:]
+ -[MRAVConcreteOutputDevice supportsDiscoveredIsPlaying]
+ -[MRAVConcreteRoutingDiscoverySession detailsList]
+ -[MRAVDistantOutputDevice supportsDiscoveredIsPlaying]
+ -[MRAVEndpoint supportsDiscoveredIsPlaying]
+ -[MRAVOutputDevice isWXDevice]
+ -[MRAVOutputDevice supportsDiscoveredIsPlaying]
+ -[MRCompanionLinkClientEvent setStatusFlags:]
+ -[MRCompanionLinkClientEvent statusFlags]
+ GCC_except_table126
+ GCC_except_table255
+ GCC_except_table287
+ GCC_except_table356
+ OBJC_IVAR_$_MRCompanionLinkClientEvent._statusFlags
+ _MRAVVolumeClientEndpointVolumeCategoryDidChangeNotification
+ _MRRequestDetailsInitiatorCorianderLockScreen
+ _MRRequestDetailsInitiatorNowPlayingPlatter
+ _RPOptionStatusFlags
+ ___50-[MRAVConcreteRoutingDiscoverySession detailsList]_block_invoke
+ _objc_msgSend$hasDeviceIsPlaying
+ _objc_msgSend$isWXDeviceWithModelID:
+ _objc_msgSend$supportsDiscoveredIsPlaying
- GCC_except_table125
- GCC_except_table254
- GCC_except_table285
- GCC_except_table355
- _objc_msgSend$contents
- _objc_msgSend$dataByteSize
- _objc_msgSend$startOffset
- _objc_msgSend$variableFramesInPacket
CStrings:
+ "-[MRAVOutputDevice supportsDiscoveredIsPlaying]"
+ "CorianderLockScreen"
+ "MRAVVolumeClientEndpointVolumeCategoryDidChangeNotification"
+ "NowPlayingPlatter"
+ "Update: %{public}@<%{public}@> localGroupID detected. Substituting picked localDevice "
- "MRAudioDataBlock.m"
- "MRDeviceInfo *MRMediaRemoteServiceCopyDeviceInfo(MRMediaRemoteServiceRef, MRPlayerPath *__strong)"
- "Trying to call CopyDeviceInfo from Daemon"
- "invalid buffer size for decoding voice input message (%lu > (%lu * %lu))"
- "iphone"
- "packet descriptions exceed maximum packet capacity (%lu > %lu)"
```
