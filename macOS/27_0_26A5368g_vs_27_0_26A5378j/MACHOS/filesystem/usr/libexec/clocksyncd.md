## clocksyncd

> `/usr/libexec/clocksyncd`

```diff

-  __TEXT.__text: 0x3db00
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_stubs: 0x59c0
-  __TEXT.__objc_methlist: 0x36b4
+  __TEXT.__text: 0x3de04
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_methlist: 0x36c4
   __TEXT.__const: 0x139
   __TEXT.__cstring: 0x2a11
-  __TEXT.__oslogstring: 0x5979
-  __TEXT.__gcc_except_tab: 0x1ad0
-  __TEXT.__objc_methname: 0x917d
+  __TEXT.__oslogstring: 0x5ab3
+  __TEXT.__gcc_except_tab: 0x1af8
+  __TEXT.__objc_methname: 0x91c9
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
   __TEXT.__unwind_info: 0xee0

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1d90
-  __DATA.__objc_ivar: 0x514
+  __DATA.__objc_const: 0x6a68
+  __DATA.__objc_selrefs: 0x1d98
+  __DATA.__objc_ivar: 0x51c
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x141

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1566
-  Symbols:   260
-  CStrings:  2726
+  Functions: 1564
+  Symbols:   259
+  CStrings:  2733
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- _mach_get_times
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/MSG/TSDMSGClockSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5jZenp/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
+ "1501.4"
+ "Dropping stale trigger timing for triggerId %u: GTB %llu < threshold %llu\n"
+ "GTB/MCT offset changed (%llu -> %llu) — clearing trigger timing buffer before read\n"
+ "GTB/MCT offset changed mid-fetch (%llu -> %llu) — buffer entries are mixed; resetting\n"
+ "Nominal sync period: (%llu/%llu), nominal syncs per poll: %llu, %@\n"
+ "Reset MSG trigger timings, cachedGtbMctOffset: %llu, postResetGtbThreshold: %llu\n"
+ "Reset trigger timings: re-register failed for triggerId %u: 0x%x\n"
+ "Reset trigger timings: unregister failed for triggerId %u: 0x%x\n"
+ "Trigger timestamp overflow: whole=%llu, offset=%llu\n"
+ "_cachedGtbMctOffset"
+ "_postResetGtbThreshold"
+ "_resetTriggerTimingBuffersLocked"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/MSG/TSDMSGClockSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8tLSBk/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
- "1501.1"
- "Failed to calculate MAT offset because MCT < MAT. MCT: %llu, MAT: %llu\n"
- "Failed to calculate MAT offset from MCT. Error: %i\n"
- "MAT/MCT offset greater than INT64_MAX. MCT: %llu, MAT: %llu\n"
- "Nominal sync period: (%llu/%llu), nominal syncs per poll: %llu, %@, matOffset: %lli\n"

```
