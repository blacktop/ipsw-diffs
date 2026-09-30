## CoreAUC

> `/System/Library/PrivateFrameworks/CoreAUC.framework/Versions/A/CoreAUC`

```diff

 638.12.0.0.0
-  __TEXT.__text: 0xe260
-  __TEXT.__const: 0x156
-  __TEXT.__cstring: 0x1314
-  __TEXT.__oslogstring: 0x37fc
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__text: 0x99c4
+  __TEXT.__const: 0x10e
+  __TEXT.__cstring: 0xa19
+  __TEXT.__unwind_info: 0x458
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__auth_got: 0x448
-  __DATA.__common: 0x10
+  __AUTH_CONST.__auth_got: 0x400
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x38
-  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 301
-  Symbols:   183
-  CStrings:  250
+  Functions: 270
+  Symbols:   174
+  CStrings:  84
 
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
- _strlen
- _sysctl
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "***FAKED*** "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor.c %s: deprecated, use CFRelease instead"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor.c %s: deprecated, use Create instead of New"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: \t\"%s\",\t// %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: %@ status is %lu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: %d status is %lu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: AUCHDCPMonitorSetSRMData: Failed with err=%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: HDCP: Checking system board-id, '%.*s' hashes to '%s'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: HDCP: hash '%s' is blacklisted"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: HDCPLoadSRM: Attempting to initialize SRM from '%s'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: HDCPLoadSRM: SRM file does not appear to exist on disk"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: HDCPLoadSRM: Setting SRM to upstream library %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: Non-capable hardware:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: Received NULL Dictionary from CGSCopyDisplayInfoDictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitorCommon.m %s: status = %s, type = %s, isDetermined = %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Barney.c %s: AppleUpstreamInit: Failed with result == %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Barney.c %s: AppleUpstreamInit: Succeeded (%d video connection(s) found)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Fred.c %s: %d audio connection%s added."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Fred.c %s: %d audio connection%s removed."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Fred.c %s: AppleUpstreamInit: Failed with result == 0x%x"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCHDCPMonitor_Fred.c %s: AppleUpstreamInit: Succeeded (%d video %d audio connections found)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/AUCMetalDeviceUtilities.m %s: deviceName = %@, ID=%llu, %sremovable"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/SRM.c %s: SRMCopyDataFromURL: SRM file is currently locked by pid %d which does not appear to be running"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/SRM.c %s: SRMWriteDataToURL: SRM file is currently locked by pid %d which does not appear to be running"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Ignoring status change %d from '%s' to '%s'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Status is now '%s' (was '%s')"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] Status is still '%s'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x] protocolType: %d, status: %d, isRepeater %d, type: %d, isDetermined %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: [%x]: Error - Protocol version in message header (%d:%s) is invalid (expected %d:%s)."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: calling upstreamConnectionCommonSendMessage[%x]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Actual message length (%zu) does not match the expected size (%d + %ld header)."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Message does not start with requisite 'HDCP' header."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Message length (%zu) should be at least %ld bytes."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionCheckMessage[%x]: Error - Unrecognized protocol type: %d."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() Flags: 0x%x, DTT: %d, DownstreamEstablished: %d, HDCPCapable: %d, InternalDevice: %d, Revoked: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULNVStateMachineErr, resetting..."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULStatusUntrusted, setting state to 'unknown'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: AULRcvRspMsg() returned kAULVersionMismatchErr, aborting..."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: Failed with fpResult == %d and result == 0x%x"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionGetMessage[%x]: Succeeded"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: AULGetUpstreamVersion = %s %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: Failed with result == %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionInitAUL[%x]: Succeeded"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionNotificationCallBack[%x]: messageType = %u"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionReset[%x]: AUL context %s successfully reset."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Failed with err == %d (fpResult == %d, result == 0x%x)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Flushing upstream driver due to kIOReturnNoSpace"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Message already in flight, ignoring send message attempt %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnectionCommon.c %s: upstreamConnectionSendMessage[%x]: Succeeded"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UpstreamConnection_GetProtectionOptions.c %s: gpoUpstreamConnectionNotificationCallBack[%x]: Failed with result == %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_GetProtectionOptions.c %s: Failed to create a new user client with GPO!\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_IOService.c %s: UserClientCreateWithService[%x]: Protocol Message - SupportedProtocol = 0x%x, LinkCount = %u, HDCPenabled = %u"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_IOService.c %s: UserClientCreateWithService[%x]: linkID = 0x%08llu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_IOService.c %s: UserClientFlush[%x]: %s (result=0x%x)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_IOService.c %s: ioserviceNotificationCallBack: messageType = %u, linkID = 0x%08llu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreAUC/Sources/UserClient_IOService.c %s: private message available but for linkID 0x%x, not me (0x%x)"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay did not return any valid displays"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay returned a NULL device name for display ID %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: CADisplay was unable to locate properties of display %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: GetProtectionOptions returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOAVCopyFirstMatchingIOAVObjectOfType returned no valid service"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOAVServiceGetContentProtectionCapabilities returned error %d"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOMFB GetProtectionOptions returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: IOMFB OpenByName returned error %d for display %s"
- "<<<< AUCWirelessHDCPSessionManager >>>> %s: OpenByName returned error %d for display %s"
- "AUCHDCPMonitorConfigureEGPUListeners_block_invoke"
- "AUCWirelessHDCPSessionManagerGetAggregateProtectionBits"
- "AUCWirelessHDCPSessionManagerGetHDCPCapabilityOfDevice"
- "AUCWirelessHDCPSessionManagerGetProtectionBitsOfDisplay"
- "AUCWirelessHDCPSessionManager_trace"
- "CopyCADisplayNameForCGSDisplayID"
- "Down"
- "Failed"
- "Fatal HDCP Error: This version of QuickTime is not compatible with the installed driver."
- "Gnf6vZyAVLNQta0BwK"
- "HDCP type Unknown"
- "HDCPIsHDCPCapableHardware"
- "HDCPLoadSRM"
- "HDCPMonitorGetSecureStatusTypeAndIsDeterminedForDisplays"
- "HDCPSetSRMData"
- "HDCP_type0"
- "HDCP_type1"
- "Initializing"
- "Mac-F221BEC8"
- "Mac-F221DCC8"
- "Mac-F226BEC8"
- "Mac-F22788A9"
- "Mac-F22788C8"
- "Mac-F227BEC8"
- "Mac-F4208AC8"
- "Mac-F4208CA9"
- "Mac-F4208CAA"
- "Mac-F4208CC8"
- "Mac-F4208DA9"
- "Mac-F4208DC8"
- "Mac-F4208EAA"
- "Mac-F4208EC8"
- "Mac-F42187C8"
- "Mac-F42189C8"
- "Mac-F4218EC8"
- "Mac-F4218FC8"
- "Mac-F42289C8"
- "Mac-F4228EC8"
- "Mac-F42386C8"
- "Mac-F42388C8"
- "Mac-F4238BC8"
- "Mac-F4238CC8"
- "Mac-F425BEC8"
- "Mac-F42786A9"
- "Mac-F42786C8"
- "Mac-F42787C8"
- "Mac-F42C86C8"
- "Mac-F42C88C8"
- "Mac-F42C89C8"
- "Mac-F42C8CC8"
- "Mac-F42DBEC8"
- "NOT"
- "Not Capable"
- "SRMCopyDataFromURL"
- "SRMWriteDataToURL"
- "Succeeded"
- "UNRECOGNIZED PROTOCOL"
- "UNRECOGNIZED STATUS"
- "Unknown"
- "Unsupported Interface"
- "Up"
- "UpstreamConnectionCommon.c"
- "UpstreamConnectionCommonInitialize_block_invoke"
- "UpstreamConnectionCommonNotificationCallBack"
- "UserClientCreateWithGPO"
- "UserClientCreateWithService"
- "WAS"
- "WAS NOT"
- "barneyInitializeUpstreamConnections"
- "failed"
- "fredAudioConnectedNotification_block_invoke"
- "fredAudioTerminatedNotification_block_invoke"
- "fredInitializeUpstreamConnections"
- "gpoUpstreamConnectionNotificationCallBack"
- "ioserviceNotificationCallBack"
- "ioserviceUserClient_Flush"
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
- "s"
- "succeeded"
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
