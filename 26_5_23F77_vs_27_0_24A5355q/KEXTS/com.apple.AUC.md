## com.apple.AUC

> `com.apple.AUC`

```diff

-620.1.0.0.0
-  __TEXT.__cstring: 0x933
+638.12.0.0.0
+  __TEXT.__cstring: 0xd62
+  __TEXT.__os_log: 0x184c
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x56e4
+  __TEXT_EXEC.__text: 0x7ac8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc5
+  __DATA.__data: 0xd1
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x60
+  __DATA.__bss: 0x4
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x10d8
+  __DATA_CONST.__const: 0x1118
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: B98EC11A-E57D-3A84-A015-4E85787ECBCA
-  Functions: 238
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x68
+  UUID: 6056EF71-9D22-3A7A-87C3-3AFA62D32F4E
+  Functions: 240
   Symbols:   0
-  CStrings:  42
+  CStrings:  187
 
CStrings:
+ "%s %s: AULInitContext failed, protocolType = %d, r = %X\n"
+ "%s %s: ConnectionWatchdog message timer waking up...\n"
+ "%s %s: Processed HDCP packet successfully\n"
+ "%s %s: dropped HDCP packet notification\n"
+ "%s %s: dropping callback for non pending notification\n"
+ "%s PL read_edt(%s) provider=%d\n"
+ "%s PL read_edt(%s) provider=%p\n"
+ "%s PL read_edt: buf=%p\n"
+ "%s PL read_edt: data=%d, len=%d\n"
+ "%s PL read_edt: data=%p, len=%d\n"
+ "%s PL read_edt: databytes=%d\n"
+ "%s PL read_edt: databytes=%p\n"
+ "%s PL read_edt: done\n"
+ "%s PL read_edt: values=%d\n"
+ "%s [%p] %s: ProcessStatusChange for userClient[%p] at index = %d.\n"
+ "%s [%p] %s: no hdcp reply available while not pending\n"
+ "%s [%p] AppleRGBOUT: DP cable attached.\n"
+ "%s [%p] Could not cast param0: %p to AUCOUT instance\n"
+ "%s [%p] DisplayCapable: returning true EARLY because ioSurface is not protected\n"
+ "%s [%p] DisplayProtectionOptions: prot = 0x%llx, error = %d. \n"
+ "%s [%p] In AUC::DisplayCapable\n"
+ "%s [%p] In AUC::InterfaceCapable\n"
+ "%s [%p] In AUC::InterfaceCapable: returning false EARLY because AVVideoInterface is inactive"
+ "%s [%p] In AUC::InterfaceCapable: returning true EARLY because ioSurface is not protected\n"
+ "%s [%p] In AUC::InterfaceForDisplayType(%u)\n"
+ "%s [%p] In DisplayProtectionOptions\n"
+ "%s [%p] InterfaceCapable: status = %u, type = %u, surfaceBits = 0x%llx, capable = %s. \n"
+ "%s [%p] InterfaceForDisplayType: Special case for internal display\n"
+ "%s [%p] InterfaceForDisplayType: displayType %u is not being tracked. \n"
+ "%s [%p] InterfaceStatusAndType: IOAVVideoInterface is not being tracked, interface:%p, location:%u, mDriver_DP:%p.\n"
+ "%s [%p] InterfaceStatusAndType: calling Watchdog\n"
+ "%s [%p] InterfaceStatusAndType: if=%p, dispLoc=%u, status=%u, type=%u"
+ "%s [%p] InterfaceStatusAndType: special case for internal display\n"
+ "%s [%p] Status = %d, Type = %d, protectionOptions = 0x%llx. \n"
+ "%s [%p] Status is now '%s%s:%d. mSendCallbackOnSetStatus = %d ' (was '%s%s:%d')."
+ "%s [%p] Status is still '%s%s:%d'."
+ "%s [%p] displayType = %u, status = %u, type = %u, ioSurfaceProtectionOption = 0x%llx, displayCapable = %s . \n"
+ "%s [%p] first protected surface in a while (%llu milliseconds)"
+ "%s [%p] interface == NULL; using kUpstreamConnection{Status,Type}_Unknown.\n"
+ "%s [%p] no Service received in call_DPPluggedNotificationGated \n"
+ "%s [%p] protectedIOSurfaceSeenRecentlyTimer to be run only on an external display"
+ "%s [%p] setting LastSeenAtTimeMS to %llu"
+ "%s [%p] topologyType=%d\n"
+ "%s [%p] upstreamConnectionGetMessage: hdcpFlags=0x%x"
+ "%s [%p] upstreamConnectionGetMessage: hhdcp_get_reply failed with return code %d"
+ "%s [%p] upstreamConnectionGetStatusFromAULFlags flags: 0x%08x; digitalTransmitting: %d; hdcpUp: %d; supportsHDCP: %d"
+ "%s [%p] upstreamConnectionGetStatusFromAULFlags_continue flags: 0x%08x; repeater: %s; statusVersion:%d"
+ "%s [%p]::%s Unable to get location of interface from CommonAVVideoInterface.\n"
+ "%s [%p]::%s but newService is NULL\n"
+ "%s [%p]::%s but no DP driver\n"
+ "%s [%p]::%s called"
+ "%s [%p]::%s called \n"
+ "%s [%p]::%s hot plug notification while we already have an interface available\n"
+ "%s [%p]::%s newService(%p) != mDriver_DP(%p)\n"
+ "%s [%p]::%s(%p)\n"
+ "%s [%p]::%s(%p, %p)\n"
+ "%s [%p]::%s(%p:%ld)\n"
+ "%s [%p]::%s,  release DP driver\n"
+ "%s [%p]::%s, Could not cast newService: %p to CommonAVVideoInterface\n"
+ "%s [%p]::%s, Could not cast param0: %p to AUCOUT instance\n"
+ "%s [%p]::%s, Releasing mStaleConnectionWatchdog_DP object\n"
+ "%s [%p]::%s, Storing mConnectionWatchdog_DP to mStaleConnectionWatchdog_DP object\n"
+ "%s [%p]::%s, created ConnectionWatchdog object \n"
+ "%s [%p]::%s: !DTT, returning UnsupportedInterface\n"
+ "%s [%p]::%s: Call to LocalAULGetReqMsg failed:  r = %X.\n"
+ "%s [%p]::%s: Call to LocalAULRcvRspMsg: protocolType=%d, hdcpFlags = 0x%X, err = %d. header->status = %d\n"
+ "%s [%p]::%s: Call to hdcp_send_request:  r = %X.\n"
+ "%s [%p]::%s: DTT & !hdcpUp, returning kUpstreamConnectionStatus_UnsupportedInterface\n"
+ "%s [%p]::%s: DTT & !supportsHDCP, returning DownNotCapable\n"
+ "%s [%p]::%s: DTT & supportsHDCP & hdcpUp"
+ "%s [%p]::%s: HDCP reply was never collected\n"
+ "%s [%p]::%s: INTERNAL, returning Up/Type1\n"
+ "%s [%p]::%s: Ignoring status change, numberOfTimes:%d, from '%s' to '%s'.\n"
+ "%s [%p]::%s: REVOKED, returning DownNotCapable\n"
+ "%s [%p]::%s: can't allocate ConnectionWatchdog\n"
+ "%s [%p]::%s: createAUPPacketAsync failed with: 0x%x\n"
+ "%s [%p]::%s: enabling SeenRecently timer\n"
+ "%s [%p]::%s: hdcp reply is not ready\n"
+ "%s [%p]::%s: mAULMessageBuffer(%p) = %d bytes.\n"
+ "%s [%p]::%s: no map or size passed\n"
+ "%s [%p]::%s: none of the above, returning Down\n"
+ "%s [%p]::%s: protected surface NOT seen recently: but re-arming message timer for %ull milliseconds from now to finish determining"
+ "%s [%p]::%s: protected surface NOT seen recently: message timer going to sleep : Status is '%s%s:%d.\n"
+ "%s [%p]::%s: protected surface seen recently: re-arming message timer for %ull milliseconds from now"
+ "%s [%p]::%s: upstreamConnectionSendMessage call is kIOReturnBusy.\n"
+ "%s [%p]::%s: upstreamConnectionSendMessage result r = %d,  mAUCDriver = %p, loopCount = %d.\n"
+ "%s [%p]::%s[%p] Received timer callback \n"
+ "%s [%p]::AppleRGBOUT: DP cable removed\n"
+ "%s create ConnectionWatchdog [%p]"
+ "%s seenRecentlyTimer_Handler: protected surface NOT seen recently, disabling SeenRecently timer"
+ "%s seenRecentlyTimer_Handler: timeSinceLastSeen = %llu ms (lastSeen = %llu, timeNow = %llu)"
+ "%s started coreauc [%p] %s"
+ "%s terminate coreauc [%p] with optionBits:%u"
+ "%s timeSinceLastSeen <= %llu ms: scheduling SeenRecently timer to check again in a bit"
+ "%s timeSinceLastSeen > %llu ms: setting SeenRecently to false and disabling SeenRecently timer"
+ "%s: [%p] %s:IOMobileFramebuffer not found.\n"
+ "%s: [%p] HDCPGetSecureStatusForDisplay: displayType = %u, status = %u, type = %u, isDetermined = %s\n"
+ "%s: [%p] In HDCPGetSecureStatusForDisplay"
+ "%s: [%p] Removing userClient[%p] at index = %d.\n"
+ "%s: [%p] Setting userClient[%p] at index = %d.\n"
+ "%s: [%p] Want to remove userClient[%p] at index = %d"
+ "%s: [%p] incoming userClient[%p]"
+ "%s: [%p]found userClient[%p] at index = %d.\n"
+ "%s: hdcp-hoover-protocol set!!!!!!!.\n"
+ "%s: tempIOMFB NOT set!!!!!!!.\n"
+ "%s: tempIOMFB set!!!!!!!.\n"
+ ":Unknown"
+ ":type0"
+ ":type1"
+ "<<<< AUC >>>>"
+ "<<<< AUC >>>> loggingLevel = %d"
+ "DPPluggedNotification"
+ "DPRemovedNotification"
+ "DPRemovedNotificationGated"
+ "Down"
+ "EnableMessageTimer"
+ "IOReturn AUC::DPPluggedNotificationGated(IOService *)"
+ "IOReturn AUC::DPRemovedNotificationGated(IOService *)"
+ "IOReturn AUC::hdcp_send_request_gated(const uint8_t *, size_t, ConnectionWatchdog *)"
+ "IOReturn auc_CreateAUPPacketCallback(OSObject *, OSData *, void *)"
+ "LocalAULRcvRspMsg"
+ "NO"
+ "Not Capable"
+ "Unknown"
+ "Unsupported Interface"
+ "Up"
+ "YES"
+ "auclog_level"
+ "bool AUC::DPRemovedNotification(void *, IOService *)"
+ "checkForHooverProtocolRequired"
+ "fail"
+ "hdcp_get_reply"
+ "init"
+ "protectedIOSurfaceSeenRecentlyTimer_Handler"
+ "success"
+ "timer_handler_gated"
+ "upstreamConnectionGetMessage"
+ "upstreamConnectionGetStatusFromAULFlags"
+ "upstreamConnectionSendMessage"
+ "upstreamConnectionSetStatus"
+ "virtual IOReturn AUC::hdcp_get_reply(uint8_t *, size_t *)"
+ "void AUC::DPRemovedNotificationAsync(void *, void *)"
+ "void AUC::InterfaceStatusAndType(IOAVVideoInterface *, UInt32 *, UInt32 *)"
+ "void AUC::aucUpstreamConnectionStatusChanged()"
+ "void AUC::protectedIOSurfaceSeen(IOAVVideoInterface *)"

```
