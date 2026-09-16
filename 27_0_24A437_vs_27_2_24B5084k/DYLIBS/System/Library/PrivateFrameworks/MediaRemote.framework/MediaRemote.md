## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.110.4.0.0
-  __TEXT.__text: 0x306394
-  __TEXT.__objc_methlist: 0x2c818
-  __TEXT.__const: 0x6b0
-  __TEXT.__cstring: 0x2df00
-  __TEXT.__oslogstring: 0xeaed
-  __TEXT.__gcc_except_tab: 0x6368
+4026.200.11.0.0
+  __TEXT.__text: 0x30660c
+  __TEXT.__objc_methlist: 0x2c888
+  __TEXT.__const: 0x650
+  __TEXT.__cstring: 0x2de64
+  __TEXT.__oslogstring: 0xeb44
+  __TEXT.__gcc_except_tab: 0x6364
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xee08
+  __TEXT.__unwind_info: 0xee18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbb58
+  __DATA_CONST.__const: 0xbb98
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf978
+  __DATA_CONST.__objc_selrefs: 0xf9a0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x14d0
+  __DATA_CONST.__got: 0x14d8
   __AUTH_CONST.__const: 0x3440
-  __AUTH_CONST.__cfstring: 0x24a80
-  __AUTH_CONST.__objc_const: 0x47f48
+  __AUTH_CONST.__cfstring: 0x24a40
+  __AUTH_CONST.__objc_const: 0x47fa8
+  __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x8700
-  __DATA.__objc_ivar: 0x33ec
+  __DATA.__objc_ivar: 0x33f0
   __DATA.__data: 0x1ca8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2da0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21029
-  Symbols:   35599
-  CStrings:  6776
+  Functions: 21036
+  Symbols:   35612
+  CStrings:  6775
 
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
+ GCC_except_table222
+ GCC_except_table252
+ GCC_except_table321
+ _MRAVVolumeClientEndpointVolumeCategoryDidChangeNotification
+ _MRRequestDetailsInitiatorCorianderLockScreen
+ _MRRequestDetailsInitiatorNowPlayingPlatter
+ _OBJC_IVAR_$_MRCompanionLinkClientEvent._statusFlags
+ _RPOptionStatusFlags
+ ___50-[MRAVConcreteRoutingDiscoverySession detailsList]_block_invoke
+ _objc_msgSend$hasDeviceIsPlaying
+ _objc_msgSend$isWXDeviceWithModelID:
+ _objc_msgSend$supportsDiscoveredIsPlaying
- GCC_except_table102
- GCC_except_table221
- GCC_except_table250
- GCC_except_table320
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
