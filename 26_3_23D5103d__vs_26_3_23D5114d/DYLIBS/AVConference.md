## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2190.3.1.0.0
-  __TEXT.__text: 0x79acc4
+2190.4.1.0.0
+  __TEXT.__text: 0x79b174
   __TEXT.__auth_stubs: 0x5640
-  __TEXT.__objc_methlist: 0x35d10
+  __TEXT.__objc_methlist: 0x35d60
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8fa6f
-  __TEXT.__oslogstring: 0x10fdba
+  __TEXT.__cstring: 0x8fac2
+  __TEXT.__oslogstring: 0x10fe34
   __TEXT.__gcc_except_tab: 0x2b44
   __TEXT.__ustring: 0x2d4
   __TEXT.__unwind_info: 0x10928
   __TEXT.__objc_classname: 0x4ed7
-  __TEXT.__objc_methname: 0x7e1fb
-  __TEXT.__objc_methtype: 0x283d7
-  __TEXT.__objc_stubs: 0x4f100
+  __TEXT.__objc_methname: 0x7e266
+  __TEXT.__objc_methtype: 0x283da
+  __TEXT.__objc_stubs: 0x4f180
   __DATA_CONST.__got: 0x1a60
-  __DATA_CONST.__const: 0x6b38
+  __DATA_CONST.__const: 0x6b40
   __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16aa0
+  __DATA_CONST.__objc_selrefs: 0x16ab8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b38
   __AUTH_CONST.__const: 0x3ca8
-  __AUTH_CONST.__cfstring: 0x26600
-  __AUTH_CONST.__objc_const: 0x63a70
+  __AUTH_CONST.__cfstring: 0x26620
+  __AUTH_CONST.__objc_const: 0x63af0
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_ivar: 0x6cd8
+  __DATA.__objc_ivar: 0x6ce4
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2ADE860A-ECAD-3626-B1FE-74FC4BC320AC
-  Functions: 31655
-  Symbols:   97615
-  CStrings:  57392
+  UUID: 39C187CF-3F58-3D86-9D5A-909AFA244121
+  Functions: 31661
+  Symbols:   97635
+  CStrings:  57402
 
Symbols:
+ +[VCHardwareSettings maxFrameRateForClipping]
+ +[VCPayloadUtils isAMRPayload:]
+ -[VCAudioPayloadConfig maxBundleFactor]
+ -[VCAudioStreamCodecConfig maxPtime]
+ -[VCAudioStreamCodecConfig setMaxPtime:]
+ -[VCHardwareSettingsMac maxFrameRateForClipping]
+ _OBJC_IVAR_$_VCAudioPayloadConfig._maxBundleFactor
+ _OBJC_IVAR_$_VCAudioStreamCodecConfig._maxPtime
+ _OBJC_IVAR_$_VCImageQueue._maxFrameRateForClipping
+ _kVCAudioPayloadConfigKeyMaxBundleFactor
+ _objc_msgSend$maxBundleFactor
+ _objc_msgSend$maxFrameRateForClipping
+ _objc_msgSend$maxPtime
+ _objc_msgSend$setMaxPtime:
CStrings:
+ " [%s] %s:%d %@(%p) frameRate updated from=%u to=%u"
+ " [%s] %s:%d @:@ VCImageQueue-init VCImageQueue=%p FigImageQueue=%p CAImageQueue=%p, slot=%u, layerHostMode=%d localVideo=%d externalCamera=%d maxFrameRateForClipping=%u"
+ " [%s] %s:%d frameRate updated from=%u to=%u"
+ "%@ payload=%d blockSize=%d codecSampleRate=%d codecSamplesPerFrame=%d inputSampleRate=%d inputSamplesPerFrame=%d isDTXEnabled=%d octedAligned=%d useSBR=%d, internalBundleFactor=%d initialBitrate=%d maxBundleFactor=%d"
+ "-[VCImageQueue setFrameRate:]"
+ "2190.4.1"
+ "TI,R,N,V_maxBundleFactor"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBBI}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B},R,VaudioReceiver"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBBI}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBBI}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}16@0:8"
+ "_maxBundleFactor"
+ "_maxFrameRateForClipping"
+ "isAMRPayload:"
+ "maxBundleFactor"
+ "maxFrameRateForClipping"
+ "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBBI}16"
+ "vcPayloadConfigKeyMaxBundleFactor"
- " [%s] %s:%d @:@ VCImageQueue-init VCImageQueue=%p FigImageQueue=%p CAImageQueue=%p, slot=%u, layerHostMode=%d localVideo=%d externalCamera=%d"
- "%@ payload=%d blockSize=%d codecSampleRate=%d codecSamplesPerFrame=%d inputSampleRate=%d inputSamplesPerFrame=%d isDTXEnabled=%d octedAligned=%d useSBR=%d, internalBundleFactor=%d initialBitrate=%d"
- "2190.3.1"
- "TI,V_frameRate"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B},R,VaudioReceiver"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}16@0:8"
- "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}16"

```
