## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-1440.23.0.0.0
-  __TEXT.__cstring: 0x3de4
-  __TEXT.__os_log: 0x8568
+1440.24.0.0.0
+  __TEXT.__cstring: 0x3e62
+  __TEXT.__os_log: 0x89ce
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x3075c
+  __TEXT_EXEC.__text: 0x30c24
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd0
+  __DATA.__data: 0xd4
   __DATA.__common: 0x688
-  __DATA.__bss: 0x39
+  __DATA.__bss: 0x41
   __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
   __DATA_CONST.__const: 0xc550
-  __DATA_CONST.__kalloc_type: 0xd00
+  __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 68BB0288-FF0E-3ED9-9ED1-976C0F2062FB
-  Functions: 1482
+  UUID: 4DA54C74-2B61-3110-A74C-1CB6C832BCBB
+  Functions: 1483
   Symbols:   0
-  CStrings:  699
+  CStrings:  721
 
CStrings:
+ "  %s(%s): *** DISCARDING STALE LINK %s EVENT *** (sequence %lld < last processed %lld)"
+ "  %s(%s): Failed to allocate link state context"
+ "  %s(%s): STALE EVENT DETECTED but fix disabled: %s (seq=%lld < last=%lld)"
+ "  %s(%s): STALE messageClients DETECTED but fix disabled: %s (seq=%lld < last=%lld)"
+ "  %s(%s): Skipping stale messageClients for link %s (sequence %lld < last processed %lld)"
+ "  %s(%s): TimeSync: [Scenario A] DOWN event (seq=%lld) delay complete"
+ "  %s(%s): TimeSync: [Scenario A] DOWN event (seq=%lld) delaying %d ms before lock"
+ "  %s(%s): TimeSync: [Scenario B] DOWN event (seq=%lld) delay complete"
+ "  %s(%s): TimeSync: [Scenario B] DOWN event (seq=%lld) delaying %d ms after stopTimeSyncCallbackThread"
+ "  %s(%s): setLinkActiveAsync: %s event (seq=%lld) starting, lastProcessed=%lld"
+ "  %s(%s): setLinkActiveAsync: DOWN event (seq=%lld) completed, sent messageClients(DOWN)"
+ "  %s(%s): setLinkActiveAsync: UP event (seq=%lld) completed, sent messageClients(UP)"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
+ "/Library/Caches/com.apple.xbs/2DB8C0AB-1B8F-41E6-8103-5D1F92CE1080/TemporaryDirectory.xTfKto/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
+ "12"
+ "12111112122212121211221211222221211112111121111222222211"
+ "121111121222121212112212112222212111121111211112222222111"
+ "1211111212221212121122121122222121111211112111122222221111111212222"
+ "121111121222121212112212112222212111121111211112222222111111121222211"
+ "121111121222121212112212112222212111121111211112222222111111121222222221"
+ "DOWN"
+ "TimeSync: Invalid delay1 value %d, using 0\n"
+ "TimeSync: Invalid delay2 value %d, using 0\n"
+ "TimeSync: Link state fix initialized: enabled=%d, delay1=%dms, delay2=%dms\n"
+ "UP"
+ "site.TSNLinkStateContext"
+ "timesync_linkstate_delay1"
+ "timesync_linkstate_delay2"
+ "timesync_linkstate_fix"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
- "/Library/Caches/com.apple.xbs/500B18AD-A649-4904-A1FF-C4B0BF23B2ED/TemporaryDirectory.zOJvzr/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
- "12111112122212121211221211221211112111121111222222211"
- "121111121222121212112212112212111121111211112222222111"
- "1211111212221212121122121122121111211112111122222221111111212222"
- "121111121222121212112212112212111121111211112222222111111121222211"
- "121111121222121212112212112212111121111211112222222111111121222222221"

```
