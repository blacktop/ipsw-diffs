## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-  __TEXT.__text: 0x2dd758
+  __TEXT.__text: 0x2dd884
   __TEXT.__lazy_helpers: 0x498
   __TEXT.__objc_methlist: 0x564
-  __TEXT.__const: 0xa798
-  __TEXT.__oslogstring: 0x32d67
-  __TEXT.__cstring: 0x5ff2a
+  __TEXT.__const: 0xa7b8
+  __TEXT.__oslogstring: 0x32e68
+  __TEXT.__cstring: 0x5fdfa
   __TEXT.__gcc_except_tab: 0x1e0
   __TEXT.__dlopen_cstrs: 0x190
   __TEXT.__swift5_typeref: 0x1cd0

   __TEXT.__swift5_capture: 0x3b8
   __TEXT.__swift5_mpenum: 0x190
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x78e8
-  __TEXT.__eh_frame: 0x26a8
+  __TEXT.__unwind_info: 0x7898
+  __TEXT.__eh_frame: 0x2760
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbc70
+  __DATA_CONST.__const: 0xbc20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__got: 0x8c0
-  __AUTH_CONST.__const: 0xce80
-  __AUTH_CONST.__cfstring: 0x1d360
+  __AUTH_CONST.__const: 0xce00
+  __AUTH_CONST.__cfstring: 0x1d1c0
   __AUTH_CONST.__objc_const: 0xdd8
   __AUTH_CONST.__lazy_load_got: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x2460
+  __AUTH_CONST.__auth_got: 0x2470
   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x8f8
   __DATA.__objc_ivar: 0x94
-  __DATA.__data: 0x2d00
+  __DATA.__data: 0x2ca8
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x8c0
-  __DATA.__bss: 0xa1b8
-  __DATA_DIRTY.__data: 0x2ec
-  __DATA_DIRTY.__common: 0x2c8
-  __DATA_DIRTY.__bss: 0x1b00
+  __DATA.__common: 0x7e0
+  __DATA.__bss: 0xa158
+  __DATA_DIRTY.__data: 0x35c
+  __DATA_DIRTY.__common: 0x3a8
+  __DATA_DIRTY.__bss: 0x1b20
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17263
-  Symbols:   33915
-  CStrings:  19011
+  Functions: 17243
+  Symbols:   33839
+  CStrings:  18984
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
Symbols:
+ _swift_willThrowTypedImpl
- _FigTransportGetCMBaseObject
- _FigTransportGetClassID
- _FigTransportGetTypeID
- _FigTransportServiceGetCMBaseObject
- _FigTransportServiceGetClassID
- _FigTransportServiceGetTypeID
- _FigTransportSessionGetCMBaseObject
- _FigTransportSessionGetClassID
- _FigTransportSessionGetTypeID
- _FigTransportStreamGetCMBaseObject
- _FigTransportStreamGetClassID
- _FigTransportStreamGetTypeID
- _FigTransportStreamSendBatchSlow
- _kFigTransportSessionNotification_Disconnected
- _kFigTransportSessionNotification_KeepAliveResponseReceived
- _kFigTransportSessionProperty_KeepAliveInterval
- _kFigTransportSessionProperty_KeepAliveType
- _kFigTransportSessionProperty_UUID
- _kFigTransportSessionStreamOption_DelegatedID
- _kFigTransportSessionStreamOption_GroupID
- _kFigTransportSessionStreamOption_StreamPriority
- _kFigTransportSessionStreamOption_Type
- _kFigTransportStreamProperty_ID
- _service_copyFormattingDesc
- _service_getClassID
- _service_getClassID.sClassDesc
- _session_copyFormattingDesc
- _session_getClassID
- _session_getClassID.sClassDesc
- _stream_getClassID.sClassDesc
- _transport_copyFormattingDesc
- _transport_getClassID
- _transport_getClassID.sClassDesc
CStrings:
+ "<< FigEndpointManagerXPCRemote >> %s: Created aggregate endpoint proxy (type %d): <FigEndpointRemote %{private}p>{ endpointID : %{public}@ }"
+ "<<<< AudioFormatDescription >>>> %s: (%p) Creation layout channel count %d doesn't match the ASBD channel count %d."
+ "alternateIndex > 3"
+ "hevcbridgeParseSMPTE_ST2094_50AdaptiveToneMap"
- "DelegatedID"
- "FigTransport"
- "FigTransportService"
- "FigTransportSession"
- "FigTransportStream"
- "KeepAliveInterval"
- "KeepAliveType"
- "StreamGroupID"
- "StreamPriority"
- "StreamType"
- "TransportSession_Disconnected"
- "TransportSession_KeepAliveResponseReceived"
- "TransportStreamProperty_ID"
- "[FigTransport %p]"
- "[FigTransportService %p]"
- "[FigTransportSession %p]"
- "[FigTransportStream %p]"
- "alternateIndex > 4"

```
