## com.apple.iokit.IOTimeSyncFamily

> `com.apple.iokit.IOTimeSyncFamily`

```diff

-  __TEXT.__cstring: 0x43ef
-  __TEXT.__os_log: 0x8cb9
+  __TEXT.__cstring: 0x4425
+  __TEXT.__os_log: 0x8ea3
   __TEXT.__const: 0x1e8
-  __TEXT_EXEC.__text: 0x33b78
+  __TEXT_EXEC.__text: 0x33d58
   __TEXT_EXEC.__auth_stubs: 0x820
   __DATA.__data: 0xd0
   __DATA.__common: 0x688

   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1776
-  Symbols:   3188
-  CStrings:  739
+  Functions: 1778
+  Symbols:   3198
+  CStrings:  748
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZN24IOTimeSyncSyncUserClient23retainedTimeSyncServiceEv
+ __ZN32IOTimeSyncClockManagerUserClient20addMappingForClockIDEP22IOTimeSyncClockManageryPj
+ __ZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEP22IOTimeSyncClockManageryyhbPy
+ __ZN32IOTimeSyncClockManagerUserClient20retainedClockManagerEv
+ __ZN32IOTimeSyncClockManagerUserClient21releaseDynamicClockIDEP22IOTimeSyncClockManagery
+ __ZN32IOTimeSyncClockManagerUserClient23cleanupClientReferencesEP22IOTimeSyncClockManager
+ __ZN32IOTimeSyncClockManagerUserClient23removeMappingForClockIDEP22IOTimeSyncClockManagery
+ __ZN32IOTimeSyncClockManagerUserClient23removeUserFilteredClockEP22IOTimeSyncClockManagery
+ __ZN32IOTimeSyncClockManagerUserClient27nextAvailableDynamicClockIDEP22IOTimeSyncClockManagerPy
+ __ZZN20IOTimeSyncUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_3
+ __ZZN20IOTimeSyncUserClient5startEP9IOServiceE11_os_log_fmt_1
+ __ZZN20IOTimeSyncUserClient5startEP9IOServiceE11_os_log_fmt_2
+ __ZZN24IOTimeSyncSyncUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_2
+ __ZZN24IOTimeSyncSyncUserClient5startEP9IOServiceE11_os_log_fmt_0
+ __ZZN29IOTimeSyncClockTestUserClient5startEP9IOServiceE11_os_log_fmt_0
+ __ZZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt__15_
+ __ZZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt__16_
+ __ZZN32IOTimeSyncClockManagerUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt__17_
+ __ZZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEP22IOTimeSyncClockManageryyhbPyE11_os_log_fmt
+ __ZZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEP22IOTimeSyncClockManageryyhbPyE11_os_log_fmt_0
+ __ZZN32IOTimeSyncClockManagerUserClient5startEP9IOServiceE11_os_log_fmt_1
+ __ZZN32IOTimeSyncClockManagerUserClient5startEP9IOServiceE11_os_log_fmt_2
- __ZN32IOTimeSyncClockManagerUserClient20addMappingForClockIDEyPj
- __ZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEyyhbPy
- __ZN32IOTimeSyncClockManagerUserClient21releaseDynamicClockIDEy
- __ZN32IOTimeSyncClockManagerUserClient23cleanupClientReferencesEv
- __ZN32IOTimeSyncClockManagerUserClient23removeMappingForClockIDEy
- __ZN32IOTimeSyncClockManagerUserClient23removeUserFilteredClockEy
- __ZN32IOTimeSyncClockManagerUserClient27nextAvailableDynamicClockIDEPy
- __ZZN29IOTimeSyncClockTestUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_1
- __ZZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEyyhbPyE11_os_log_fmt
- __ZZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEyyhbPyE11_os_log_fmt_0
- __ZZN35IOTimeSyncEdgeTimeCaptureUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_0
- __ZZN38IOTimeSyncTimedEdgeGeneratorUserClient12initWithTaskEP4taskPvjP12OSDictionaryE11_os_log_fmt_0
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UVTQML/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
+ "12111112122212121111111111111111111111211"
+ "1211111212221212111111111111111122111111"
+ "IOTimeSyncClockManagerUserClient: missing entitlement %s\n"
+ "IOTimeSyncClockTestUserClient: missing entitlement %s\n"
+ "IOTimeSyncEdgeTimeCaptureUserClient: missing entitlement %s\n"
+ "IOTimeSyncSyncUserClient: missing entitlement %s\n"
+ "IOTimeSyncTimedEdgeGeneratorUserClient: missing entitlement %s\n"
+ "IOTimeSyncUserClient: missing entitlement %s\n"
+ "NULL == fIOTimeSyncClockManagerLock"
+ "com.apple.private.timesync.direct-userclient"
+ "failed to allocate clock manager lock\n"
+ "failed to allocate service lock\n"
+ "super::start failed\n"
+ "superStarted"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDTestInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vm2ru8/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp"
- "1211111212221212111111111111111111111211"
- "121111121222121211111111111111122111111"
- "Not entitled\n"
- "entitlement"
- "entitlement == kOSBooleanTrue"

```
