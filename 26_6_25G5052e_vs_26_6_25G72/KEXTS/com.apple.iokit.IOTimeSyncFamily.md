## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-1450.2.0.0.0
-  __TEXT.__cstring: 0x42d6
-  __TEXT.__os_log: 0x8a38
+1460.2.0.0.0
+  __TEXT.__cstring: 0x4303
+  __TEXT.__os_log: 0x8b10
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x33128
+  __TEXT_EXEC.__text: 0x331c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x688

   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1773
-  Symbols:   3008
-  CStrings:  718
+  Symbols:   3010
+  CStrings:  721
 
Symbols:
+ __ZZN20IOTimeSyncUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_1
+ __ZZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt__15_
Functions:
~ __ZN20IOTimeSyncUserClient12initWithTaskEP4taskPvjP12OSDictionary : 276 -> 356
~ __ZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionary : 1204 -> 1284
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RbMC9e/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
+ "IOTimeSyncClockManagerUserClient::initWithTask: missing entitlement com.apple.private.timesync.direct-userclient\n"
+ "IOTimeSyncUserClient::initWithTask: missing entitlement com.apple.private.timesync.direct-userclient\n"
+ "com.apple.private.timesync.direct-userclient"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LHA4af/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
```
