## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia`

```diff

-3350.77.5.6.0
-  __TEXT.__text: 0x1ed03c
+3385.14.5.2.0
+  __TEXT.__text: 0x1ed6e0
   __TEXT.__lazy_helpers: 0x738
   __TEXT.__objc_methlist: 0x3f8
-  __TEXT.__cstring: 0x1f64f
-  __TEXT.__const: 0xb1d2
-  __TEXT.__oslogstring: 0x56bc
+  __TEXT.__cstring: 0x1f73f
+  __TEXT.__const: 0xb1b2
+  __TEXT.__oslogstring: 0x56dc
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__swift5_typeref: 0x1d52

   __TEXT.__swift5_mpenum: 0x190
   __TEXT.__swift5_capture: 0x3b8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x6d70
+  __TEXT.__unwind_info: 0x6d78
   __TEXT.__eh_frame: 0x2938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9eb0
+  __DATA_CONST.__const: 0x9f20
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0x870
-  __AUTH_CONST.__const: 0xcef8
-  __AUTH_CONST.__cfstring: 0x1afc0
+  __AUTH_CONST.__const: 0xcf08
+  __AUTH_CONST.__cfstring: 0x1b120
   __AUTH_CONST.__objc_const: 0xc18
   __AUTH_CONST.__lazy_load_got: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH.__data: 0x928
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x2c68
-  __DATA.__bss: 0xa0b0
+  __DATA.__bss: 0xa0a0
   __DATA.__common: 0x220
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x3f8
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x1870
+  __DATA_DIRTY.__bss: 0x1890
   __DATA_DIRTY.__common: 0x1d0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14162
-  Symbols:   12918
-  CStrings:  5568
+  Functions: 14167
+  Symbols:   12931
+  CStrings:  5580
 
Symbols:
+ _FigEndpointManagerRemoteXPC_CreateEndpoint
+ _FigEndpointManagerRemoteXPC_DestroyEndpoint
+ _FigReportingSessionStatsCreateWithAggregatedTier
+ _hevcbridgeParseVdrDmDataPayloadExMetadataBlocks
+ _kFigEndpointCarPlayVideoPlaybackButton_BackButton
+ _kFigEndpointCarPlayVideoPlaybackButton_HideVideoButton
+ _kFigEndpointCarPlayVideoPlaybackPlayerEvent_ButtonTapped
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_SurroundRole
+ _kFigEndpointInfoKey_DeviceName
+ _kFigEndpointInfoKey_NetworkAddress
+ _kFigEndpointInfoKey_NetworkPort
+ _kFigEndpointInfoKey_TXTRecord
+ _kFigEndpointManagerXPCMsgParam_EndpointInfo
+ _kFigEndpointManagerXPCMsgParam_EndpointObjectID
+ _kFigEndpointNotification_CarPlayVideoPlaybackPlayerEvent
+ _kFigEndpointProperty_CarPlayScreenFadeDurationInSeconds
+ _kFigEndpointProperty_SnoopCollectionPathPattern
+ _kFigEndpointSubType_HomeAccessory
+ _met_copySessionID
+ _met_copyTimebase
+ createITUT_T35IdentifierFromSetupData.kSMPTE2094_50IdentifierBytes
+ hevcbridgeParseVdrDmDataPayloadExMetadataBlocks
- FigMayAccessPersistentURLOnBehalfOfClientWithAuditToken
- _FigMayAccessPersistentURLOnBehalfOfClientWithAuditToken
- _NOOP_PUTGetCurrentAccessForURLAndToken
- _OUTLINED_FUNCTION_170
- _hevcbridgeParseVdrDmDataPayloadExMetadatatBlocks
- _kInt64ValueCallBacks
- _met_getSessionID
- _met_getTimebase
- hevcbridgeParseVdrDmDataPayloadExMetadatatBlocks
CStrings:
+ "<< FigXPC >> %s: Unexpected type '%{public}s' in server reply; connection %p %{public}s"
+ "<< FigXPC >> %s: xpc error in server reply; connection %p %{public}s: %{public}s"
+ "<unknown>"
+ "BackButton"
+ "CarPlayScreenFadeDurationInSeconds"
+ "EndpointSubType_HomeAccessory"
+ "HidVideoButton"
+ "NetworkAddress"
+ "NetworkPort"
+ "SnoopCollectionPath"
+ "SurroundRole"
+ "TXTRecord"
+ "VideoPlaybackPlayerEvent_ButtonTapped"
+ "VideoPlayback_PlayerEvent"
- "<< FigXPC >> %s: Unexpected type '%s' in server reply; connection %p %s"
- "<< FigXPC >> %s: xpc error in server reply; connection %p %s: %s"
```
