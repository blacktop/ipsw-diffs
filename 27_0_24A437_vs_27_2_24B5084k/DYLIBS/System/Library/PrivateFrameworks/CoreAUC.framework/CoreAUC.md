## CoreAUC

> `/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC`

```diff

 638.12.0.0.0
-  __TEXT.__text: 0x12bd0
-  __TEXT.__const: 0xcf0
-  __TEXT.__cstring: 0x9b7
-  __TEXT.__oslogstring: 0x2014
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__text: 0xfba4
+  __TEXT.__const: 0xcb0
+  __TEXT.__cstring: 0x3ed
+  __TEXT.__unwind_info: 0x300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x30
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x998
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x40
-  __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x60
-  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   124
-  CStrings:  133
+  Functions: 185
+  Symbols:   117
+  CStrings:  39
 
Symbols:
+ _FigSignalErrorAtGM
+ _fig_log_get_emitter
- _FigNote_AllowInternalDefaultLogs
- _FigSignalErrorAt3
- __Unwind_Resume
- ___objc_personality_v0
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work
- _os_log_type_enabled
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "***FAKED*** "
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor.c %s: deprecated, use CFRelease instead"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor.c %s: deprecated, use Create instead of New"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: %@ status is %lu"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: status = %s, type = %s, isDetermined = %s"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Barney.c %s: AppleUpstreamInit: Failed with result == %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Barney.c %s: AppleUpstreamInit: Succeeded (%d video connection(s) found)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Ignoring status change %d from '%s' to '%s'"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Status is now '%s' (was '%s')"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Status is still '%s'"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] protocolType: %d, status: %d, isRepeater %d, type: %d, isDetermined %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x]: Error - Protocol version in message header (%d:%s) is invalid (expected %d:%s)."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: calling upstreamConnectionCommonSendMessage[%x]"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Actual message length (%zu) does not match the expected size (%d + %ld header)."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Message does not start with requisite 'HDCP' header."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Message length (%zu) should be at least %ld bytes."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Unrecognized protocol type: %d."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() Flags: 0x%x, DTT: %d, DownstreamEstablished: %d, HDCPCapable: %d, InternalDevice: %d, Revoked: %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULNVStateMachineErr, resetting..."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULStatusUntrusted, setting state to 'unknown'"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULVersionMismatchErr, aborting..."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: Failed with fpResult == %d and result == 0x%x"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: Succeeded"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: AULGetUpstreamVersion = %s %s"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: Failed with result == %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: Succeeded"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionNotificationCallBack[%x]: messageType = %u"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionReset[%x]: AUL context %s successfully reset."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Failed with err == %d (fpResult == %d, result == 0x%x)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Flushing upstream driver due to kIOReturnNoSpace"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Message already in flight, ignoring send message attempt %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Succeeded"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnection_GetProtectionOptions.c %s: gpoUpstreamConnectionNotificationCallBack[%x]: Failed with result == %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_Framebuffer.c %s: UserClientCreateWithFrameBuffer[%x]: Protocol Message - SupportedProtocol = 0x%x"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_GetProtectionOptions.c %s: Failed to create a new user client with GPO!\n"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay did not return any valid displays"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay returned a NULL device name for display ID %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay was unable to locate properties of display %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: GetProtectionOptions returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOAVCopyFirstMatchingIOAVObjectOfType returned no valid service"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOAVServiceGetContentProtectionCapabilities returned error %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOMFB GetProtectionOptions returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOMFB OpenByName returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: OpenByName returned error %d for display %s"
- "AUCWirelessHDCPSessionManagerGetAggregateProtectionBits"
- "AUCWirelessHDCPSessionManagerGetHDCPCapabilityOfDevice"
- "AUCWirelessHDCPSessionManagerGetProtectionBitsOfDisplay"
- "AUCWirelessHDCPSessionManager_trace"
- "Down"
- "Fatal HDCP Error: This version of QuickTime is not compatible with the installed driver."
- "Gnf6vZyAVLNQta0BwK"
- "HDCP type Unknown"
- "HDCPMonitorGetSecureStatusTypeAndIsDeterminedForDisplays"
- "HDCP_type0"
- "HDCP_type1"
- "Initializing"
- "Not Capable"
- "UNRECOGNIZED PROTOCOL"
- "UNRECOGNIZED STATUS"
- "Unknown"
- "Unsupported Interface"
- "Up"
- "UpstreamConnectionCommon.c"
- "UpstreamConnectionCommonInitialize_block_invoke"
- "UpstreamConnectionCommonNotificationCallBack"
- "UserClientCreateWithFramebuffer"
- "UserClientCreateWithGPO"
- "WAS"
- "WAS NOT"
- "barneyInitializeUpstreamConnections"
- "gpoUpstreamConnectionNotificationCallBack"
- "kAULVersionMismatchErr"
- "kAppleUpstreamNotSupported"
- "kAppleUpstreamUnknownProtocol"
- "kAppleUpstreamUseAMDProtocol"
- "kAppleUpstreamUseAppleAudioProtocol"
- "kAppleUpstreamUseAppleProtocol"
- "kAppleUpstreamUseAppleProtocolSDVO"
- "kAppleUpstreamUseHooverProtocol"
- "kAppleUpstreamUseIntel2Protocol"
- "kAppleUpstreamUseIntelProtocol"
- "kAppleUpstreamUseNVIDIAProtocol"
- "monitor_trace"
- "no"
- "tQN5x9ksL4jeZ"
- "upstreamConnectionCommonGetMessage"
- "upstreamConnectionCommonInitAUL"
- "upstreamConnectionCommonReset"
- "upstreamConnectionCommonSendMessage"
- "upstreamConnectionCommonSetStatus"
- "upstreamConnectionCommonSetStatus_block_invoke"
- "upstreamConnectionUtilCheckMessage"
- "upstreamConnectionsGetCombinedSecureStatusForDisplays"
- "yes"
```
