## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.200.15.0.0
-  __TEXT.__text: 0x306624
-  __TEXT.__objc_methlist: 0x2c890
+4026.200.23.0.0
+  __TEXT.__text: 0x306b30
+  __TEXT.__objc_methlist: 0x2c8c8
   __TEXT.__const: 0x650
-  __TEXT.__cstring: 0x2de57
+  __TEXT.__cstring: 0x2deda
   __TEXT.__oslogstring: 0xebb9
-  __TEXT.__gcc_except_tab: 0x6364
+  __TEXT.__gcc_except_tab: 0x63b4
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xee28
+  __TEXT.__unwind_info: 0xee20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbb98
+  __DATA_CONST.__const: 0xbbe0
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf9b0
+  __DATA_CONST.__objc_selrefs: 0xf9d0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14d8
-  __AUTH_CONST.__const: 0x3460
-  __AUTH_CONST.__cfstring: 0x24a40
-  __AUTH_CONST.__objc_const: 0x47fa8
-  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__const: 0x3480
+  __AUTH_CONST.__cfstring: 0x24b40
+  __AUTH_CONST.__objc_const: 0x48050
+  __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x5f00
-  __DATA.__objc_ivar: 0x33f0
+  __DATA.__objc_ivar: 0x33fc
   __DATA.__data: 0x1ca8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x55a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21039
-  Symbols:   30278
-  CStrings:  6776
+  Functions: 21044
+  Symbols:   30285
+  CStrings:  6784
 
Symbols:
+ -[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]
+ -[MRGroupComposition setSpeakerGroupCount:]
+ -[MRGroupComposition setTvAndSpeakerCount:]
+ -[MRGroupComposition speakerGroupCount]
+ -[MRGroupComposition tvAndSpeakerCount]
+ -[_MRCommandOptionsProtobuf hasRequestDetails]
+ -[_MRCommandOptionsProtobuf requestDetails]
+ -[_MRCommandOptionsProtobuf setRequestDetails:]
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._requestDetails
+ _OBJC_IVAR_$_MRGroupComposition._speakerGroupCount
+ _OBJC_IVAR_$_MRGroupComposition._tvAndSpeakerCount
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_2
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_3
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_4
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_5
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_6
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_7
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_8
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke_4
+ ___block_descriptor_176_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8
- -[MRAVRoutingDiscoverySessionWrapper _currentVisibleEndpointsForSession:]
- -[MRAVRoutingDiscoverySessionWrapper _currentVisibleOutputDevicesForSession:]
- -[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]
- -[MRAVRoutingDiscoverySessionWrapper _shouldNotify]
- ___50-[MRRapportTransportConnection _registerCallbacks]_block_invoke_3
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_2
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_3
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_4
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_5
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_6
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_7
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_8
- ___block_descriptor_160_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8
CStrings:
+ "GracePeriod"
+ "OA"
+ "SpeakerGroup"
+ "TVAndSpeaker"
+ "hifispeaker.2"
+ "requestDetails"
+ "speakerGroup: %lu;"
+ "tv.and.hifispeaker.fill"
+ "tvAndSpeaker: %lu;"
- "O"
```
