## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.512.0.0.0
-  __TEXT.__text: 0x16fb34
+3.604.0.0.0
+  __TEXT.__text: 0x16f2cc
   __TEXT.__auth_stubs: 0x26a0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x2218f
-  __TEXT.__oslogstring: 0x175b2
+  __TEXT.__const: 0x2212f
+  __TEXT.__oslogstring: 0x173d3
   __TEXT.__cstring: 0x13dd2
   __TEXT.__gcc_except_tab: 0x45ec
-  __TEXT.__unwind_info: 0x2e08
+  __TEXT.__unwind_info: 0x2dd8
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_methname: 0x594
   __TEXT.__objc_stubs: 0x980
-  __DATA_CONST.__got: 0x2e98
+  __DATA_CONST.__got: 0x2ea0
   __DATA_CONST.__const: 0x9b40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x1360
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x1f50
+  __AUTH_CONST.__const: 0x1e60
   __AUTH_CONST.__cfstring: 0x6da0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4510
-  Symbols:   8496
-  CStrings:  5215
+  Functions: 4490
+  Symbols:   8468
+  CStrings:  5207
 
Symbols:
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_TrackingFailureFieldOfViewModifier
- _ZL19StartExclaveStreamsP19H16ISPCaptureDeviceP19H16ISPCaptureStream.cold.20
- _ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE.cold.1
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode10onActivateEv
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode12onDeactivateEv
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode22GetNodeProcessingStateEv
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD0Ev
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD1Ev
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeD2Ev
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode10onActivateEv
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode12onDeactivateEv
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNode22GetNodeProcessingStateEv
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD0Ev
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD1Ev
- __ZN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeD2Ev
- __ZTIN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
- __ZTIN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
- __ZTSN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
- __ZTSN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
- __ZTVN6H16ISP34H16ISPGraphExclaveFaceTrackingNodeE
- __ZTVN6H16ISP43H16ISPGraphExclaveFaceTrackingSecondaryNodeE
CStrings:
- "%s - Cannot set face kit settings! result=%u\n"
- "%s - [Exclaves]: face tracking secondary process failed! idl error=%u\n"
- "H16ISPGraphExclaveFaceTrackingSecondaryNode::onActivate\n"
- "H16ISPGraphExclaveFaceTrackingSecondaryNode::onDeactivate\n"
- "Sent FaceKit config! channel=%u, numtrackedfaces=%u\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onActivate\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onDeactivate\n"
- "[Exclaves]: channel=%u runSecondaryProcessing=%{bool}d requestID=0x%08x\n"

```
