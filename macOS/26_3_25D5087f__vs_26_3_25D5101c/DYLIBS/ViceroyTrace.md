## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/Versions/A/ViceroyTrace`

```diff

-2190.1.1.0.0
-  __TEXT.__text: 0xadcc0
+2190.3.1.0.0
+  __TEXT.__text: 0xae008
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x8e38
+  __TEXT.__objc_methlist: 0x8e68
   __TEXT.__const: 0x2420
-  __TEXT.__cstring: 0xe919
+  __TEXT.__cstring: 0xe938
   __TEXT.__oslogstring: 0xd1dd
   __TEXT.__gcc_except_tab: 0x388
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__unwind_info: 0x16b0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1c0cc
+  __TEXT.__objc_methname: 0x1c171
   __TEXT.__objc_methtype: 0x245b
-  __TEXT.__objc_stubs: 0xefa0
+  __TEXT.__objc_stubs: 0xf020
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4368
+  __DATA_CONST.__objc_selrefs: 0x4388
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0xb80
-  __AUTH_CONST.__cfstring: 0xdde0
-  __AUTH_CONST.__objc_const: 0x16a78
+  __AUTH_CONST.__cfstring: 0xde20
+  __AUTH_CONST.__objc_const: 0x16aa8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x204c
+  __DATA.__objc_ivar: 0x2050
   __DATA.__data: 0x730
   __DATA.__bss: 0x40
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F242915C-BD07-307E-88A3-102F8BC70FAF
-  Functions: 3992
-  Symbols:   9100
-  CStrings:  9282
+  UUID: 2766B5F0-3283-3F88-AD85-89AD483BCC98
+  Functions: 3997
+  Symbols:   9110
+  CStrings:  9292
 
Symbols:
+ -[StreamGroupStats fecMaxNumPacketsInFrame]
+ -[StreamGroupStats setFecMaxNumPacketsInFrame:]
+ -[VCAggregatorMultiway addFECMaxNumPacketsInFrame:]
+ -[VCAggregatorMultiway updateFECMaxNumPacketsInFrame:]
+ OBJC_IVAR_$_StreamGroupStats._fecMaxNumPacketsInFrame
+ _OUTLINED_FUNCTION_76
+ __64-[VCAggregatorMultiway processSessionInitWithPayload:timestamp:]_block_invoke.5680
+ _objc_msgSend$addFECMaxNumPacketsInFrame:
+ _objc_msgSend$fecMaxNumPacketsInFrame
+ _objc_msgSend$setFecMaxNumPacketsInFrame:
+ _objc_msgSend$updateFECMaxNumPacketsInFrame:
- __64-[VCAggregatorMultiway processSessionInitWithPayload:timestamp:]_block_invoke.5669
CStrings:
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
+ "FECMNPIF"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CGC4ugA0khtwGnZy80CsxxG0RXzAFwmtkY8mAdQ/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."
+ "TI,V_fecMaxNumPacketsInFrame"
+ "VCFECGenMaxNumPackets"
+ "_fecMaxNumPacketsInFrame"
+ "addFECMaxNumPacketsInFrame:"
+ "fecMaxNumPacketsInFrame"
+ "setFecMaxNumPacketsInFrame:"
+ "updateFECMaxNumPacketsInFrame:"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/4~CDzUugBNuyNAxAtEpy0W7WmejyVv_pUvBYdtqaY/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."

```
