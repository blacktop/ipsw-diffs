## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.210.3.0.0
-  __TEXT.__text: 0x3078d0
-  __TEXT.__objc_methlist: 0x2c900
-  __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x2e02c
+4026.300.11.0.0
+  __TEXT.__text: 0x3081c8
+  __TEXT.__objc_methlist: 0x2c9b8
+  __TEXT.__const: 0x750
+  __TEXT.__cstring: 0x2dfeb
   __TEXT.__oslogstring: 0xebb9
-  __TEXT.__gcc_except_tab: 0x63d8
+  __TEXT.__gcc_except_tab: 0x63e4
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xee28
+  __TEXT.__unwind_info: 0xee70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbc18
+  __DATA_CONST.__const: 0xbc40
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa00
+  __DATA_CONST.__objc_selrefs: 0xfa48
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14e8
-  __AUTH_CONST.__const: 0x3480
-  __AUTH_CONST.__cfstring: 0x24cc0
-  __AUTH_CONST.__objc_const: 0x480b0
+  __AUTH_CONST.__const: 0x34a0
+  __AUTH_CONST.__cfstring: 0x24ca0
+  __AUTH_CONST.__objc_const: 0x481c8
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__auth_got: 0xbd8
   __AUTH.__objc_data: 0x5f00
-  __DATA.__objc_ivar: 0x3404
+  __DATA.__objc_ivar: 0x3418
   __DATA.__data: 0x1ca8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x55a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21053
-  Symbols:   30299
-  CStrings:  6796
+  Functions: 21071
+  Symbols:   30328
+  CStrings:  6797
 
Symbols:
+ -[MRDestinationResolver endpointChangesRegistration]
+ -[MRDestinationResolver setEndpointChangesRegistration:]
+ -[MRDeviceInfo airPlayBidirectionalAudioSessionID]
+ -[MRDeviceInfo airPlayServerConnectionInfo]
+ -[MRDeviceInfo hasAirPlayBidirectionalAudioSessionID]
+ -[MRDeviceInfo setAirPlayBidirectionalAudioSessionID:]
+ -[MRDeviceInfo setAirPlayServerConnectionInfo:]
+ -[MRDeviceInfo setHasAirPlayBidirectionalAudioSessionID:]
+ -[_MRDeviceInfoMessageProtobuf airPlayBidirectionalAudioSessionID]
+ -[_MRDeviceInfoMessageProtobuf airPlayServerConnectionInfo]
+ -[_MRDeviceInfoMessageProtobuf hasAirPlayBidirectionalAudioSessionID]
+ -[_MRDeviceInfoMessageProtobuf hasAirPlayServerConnectionInfo]
+ -[_MRDeviceInfoMessageProtobuf setAirPlayBidirectionalAudioSessionID:]
+ -[_MRDeviceInfoMessageProtobuf setAirPlayServerConnectionInfo:]
+ -[_MRDeviceInfoMessageProtobuf setHasAirPlayBidirectionalAudioSessionID:]
+ GCC_except_table147
+ _MGIsDeviceOneOfType
+ _MRMediaRemoteAirPlayReceiverCopyServerConnectionInfo
+ _MRMediaRemoteAirPlayReceiverGetBidirectionalAudioSessionID
+ _OBJC_IVAR_$_MRDestinationResolver._endpointChangesRegistration
+ _OBJC_IVAR_$_MRDeviceInfo._airPlayBidirectionalAudioSessionID
+ _OBJC_IVAR_$_MRDeviceInfo._airPlayServerConnectionInfo
+ _OBJC_IVAR_$_MRDeviceInfo._hasAirPlayBidirectionalAudioSessionID
+ _OBJC_IVAR_$_MRV1NowPlayingController._helper
+ _OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._airPlayBidirectionalAudioSessionID
+ _OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._airPlayServerConnectionInfo
+ ___46-[MRSharedSettings supportAgentLiveActivities]_block_invoke
+ ___70-[MRDestinationResolver registerForEndpointChangesForOutputDeviceUID:]_block_invoke_2
+ ___block_descriptor_48_e8_32w_e28_v16?0^{__MRAVEndpointRef=}8lw32l8
+ _objc_getProperty
+ _objc_setProperty_atomic_copy
+ _supportAgentLiveActivities.__supports
+ _supportAgentLiveActivities.onceToken
- GCC_except_table145
- _OBJC_IVAR_$_MRSharedSettings._supportAgentLiveActivities
- _OBJC_IVAR_$_MRV1NowPlayingController.helper
- __OBJC_$_INSTANCE_VARIABLES_MRSharedSettings
CStrings:
+ "LiveActivitiesQFA"
+ "MenuBar"
+ "airPlayBidirectionalAudioSessionID"
+ "airPlayServerConnectionInfo"
- "MRAudioDataBlock.m"
- "invalid buffer size for decoding voice input message (%lu > (%lu * %lu))"
- "packet descriptions exceed maximum packet capacity (%lu > %lu)"
```
