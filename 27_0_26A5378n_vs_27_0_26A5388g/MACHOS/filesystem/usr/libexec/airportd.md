## airportd

> `/usr/libexec/airportd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-19175.55.0.0.0
-  __TEXT.__text: 0xdef70
+19175.62.0.0.0
+  __TEXT.__text: 0xdf944
   __TEXT.__auth_stubs: 0x1fe0
-  __TEXT.__objc_stubs: 0x102a0
-  __TEXT.__objc_methlist: 0x5648
-  __TEXT.__const: 0xab8
-  __TEXT.__objc_methname: 0x149da
+  __TEXT.__objc_stubs: 0x10320
+  __TEXT.__objc_methlist: 0x5680
+  __TEXT.__const: 0xb28
+  __TEXT.__objc_methname: 0x14aac
   __TEXT.__objc_classname: 0x3be
   __TEXT.__objc_methtype: 0x3400
   __TEXT.__gcc_except_tab: 0x2114
-  __TEXT.__cstring: 0x2dcc7
+  __TEXT.__cstring: 0x2dfba
   __TEXT.__oslogstring: 0x14c4
-  __TEXT.__unwind_info: 0x2798
-  __DATA_CONST.__const: 0x3250
-  __DATA_CONST.__cfstring: 0x9ac0
+  __TEXT.__unwind_info: 0x27b0
+  __DATA_CONST.__const: 0x3270
+  __DATA_CONST.__cfstring: 0x9b00
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__auth_got: 0x1008
-  __DATA_CONST.__got: 0x938
+  __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x68c8
-  __DATA.__objc_selrefs: 0x4930
-  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_const: 0x6938
+  __DATA.__objc_selrefs: 0x4950
+  __DATA.__objc_ivar: 0x728
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x424
   __DATA.__common: 0x140
-  __DATA.__bss: 0x358
+  __DATA.__bss: 0x360
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2814
-  Symbols:   830
-  CStrings:  7540
+  Functions: 2825
+  Symbols:   831
+  CStrings:  7561
 
Symbols:
+ _OBJC_CLASS_$_WiFiAwareStateMonitor
CStrings:
+ "%s: Failed to allocate WiFiAwareStateMonitor — NAN RT awareness unavailable\n"
+ "%s: NAN RT handler: parent interface name is nil, cannot update context\n"
+ "-[CWXPCInterfaceContext __setNanRealTimeInProgress:]"
+ "-[CWXPCSubsystem activateXPC]"
+ "-[CWXPCSubsystem initWithScheduler:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/CWXPCSubsystem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/configdIODriverInterface.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MRnlo/Sources/AirPort_executables/Tools/airportd/configdSCInterface.m"
+ "<%s[%d]> %s: Failed to allocate WiFiAwareStateMonitor — NAN RT awareness unavailable\n"
+ "<%s[%d]> %s: Late-bound CWFAutoJoinManager in -activateXPC: %p\n"
+ "<%s[%d]> %s: NAN RT handler: parent interface name is nil, cannot update context\n"
+ "<%s[%d]> %s: NAN real-time is %s\n"
+ "<%s[%d]> %s: Pre-fetched CWFAutoJoinManager: %p\n"
+ "Late-bound CWFAutoJoinManager in -activateXPC: %p"
+ "Pre-fetched CWFAutoJoinManager: %p"
+ "T@\"CWFAutoJoinManager\",R,N,V_autoJoinManager"
+ "__forceResetNanRealTimeModeState"
+ "__setNanRealTimeInProgress:"
+ "_bestConnectedScanDeferredForNAN"
+ "_init_nan_realtime_monitor"
+ "_init_nan_realtime_monitor_block_invoke_2"
+ "_nanRealTimeInProgress"
+ "nanRealTimeInProgress"
+ "remotedevicekitwifid"
+ "setNanRealTimeInProgress:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/CWXPCSubsystem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/configdIODriverInterface.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/configdSCInterface.m"
- "hrmwifid"
```
