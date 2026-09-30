## airportd

> `/usr/libexec/airportd`

```diff

-  __TEXT.__text: 0xdea34
-  __TEXT.__auth_stubs: 0x1fc0
+  __TEXT.__text: 0xdef70
+  __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__objc_stubs: 0x102a0
   __TEXT.__objc_methlist: 0x5648
   __TEXT.__const: 0xab8
-  __TEXT.__objc_methname: 0x149cd
+  __TEXT.__objc_methname: 0x149da
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methtype: 0x33d3
+  __TEXT.__objc_methtype: 0x3400
   __TEXT.__gcc_except_tab: 0x2114
-  __TEXT.__cstring: 0x2dbb0
+  __TEXT.__cstring: 0x2dcc7
   __TEXT.__oslogstring: 0x14c4
   __TEXT.__unwind_info: 0x2798
   __DATA_CONST.__const: 0x3250
-  __DATA_CONST.__cfstring: 0x9a80
+  __DATA_CONST.__cfstring: 0x9ac0
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__auth_got: 0xff8
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__auth_got: 0x1008
+  __DATA_CONST.__got: 0x938
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x68c8
   __DATA.__objc_selrefs: 0x4930
   __DATA.__objc_ivar: 0x71c
   __DATA.__objc_data: 0xb90
-  __DATA.__data: 0x414
+  __DATA.__data: 0x424
   __DATA.__common: 0x140
   __DATA.__bss: 0x358
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 2814
-  Symbols:   828
-  CStrings:  8808
+  Symbols:   830
+  CStrings:  8813
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetName
CStrings:
+ "-[CWXPCSubsystem associateToWiFiNetwork:password:is8021X:remember:addReason:possiblyHidden:tetherDevice:interfaceName:authorization:connection:isAutoJoin:error:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/CWXPCSubsystem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/configdIODriverInterface.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qaQnar/Sources/AirPort_executables/Tools/airportd/configdSCInterface.m"
+ "<%s[%d]> %s: TCPKA TKO was disabled, indicate TCPKA Timeout Mitigation Soft Error: WiFi(%@), tag['%s'] tagid[0x%016llx] type[0x%08x/%u], lastEnabled[%u] lastWakeCount[%llu], wakeCounterTimeout[%d] lastWakeCounter[%d], window[%llu mins] modulus[%llu] fireTTR[%u], recentMitigations[%ld] mitigationTimestampsLast5[%@]\n"
+ "B96@0:8@16@24B32B36q40B48@52@60@68@76B84^@88"
+ "TCPKA TKO was disabled, indicate TCPKA Timeout Mitigation Soft Error: WiFi(%@), tag['%s'] tagid[0x%016llx] type[0x%08x/%u], lastEnabled[%u] lastWakeCount[%llu], wakeCounterTimeout[%d] lastWakeCounter[%d], window[%llu mins] modulus[%llu] fireTTR[%u], recentMitigations[%ld] mitigationTimestampsLast5[%@]"
+ "associateToWiFiNetwork:password:is8021X:remember:addReason:possiblyHidden:tetherDevice:interfaceName:authorization:connection:isAutoJoin:error:"
+ "wifi_tcpka_ttr_modulus_override"
+ "wifi_tcpka_ttr_window_mins_override"
- "-[CWXPCSubsystem associateToWiFiNetwork:password:is8021X:remember:addReason:possiblyHidden:interfaceName:authorization:connection:isAutoJoin:error:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/CWXPCSubsystem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/configdIODriverInterface.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RR25vC/Sources/AirPort_executables/Tools/airportd/configdSCInterface.m"
- "<%s[%d]> %s: TCPKA TKO was disabled, indicate TCPKA Timeout Mitigation Soft Error: WiFi(%@), tag['%s'] tagid[0x%016llx] type[0x%08x/%u], lastEnabled[%u] lastWakeCount[%llu], wakeCounterTimeout[%d] lastWakeCounter[%d]\n"
- "TCPKA TKO was disabled, indicate TCPKA Timeout Mitigation Soft Error: WiFi(%@), tag['%s'] tagid[0x%016llx] type[0x%08x/%u], lastEnabled[%u] lastWakeCount[%llu], wakeCounterTimeout[%d] lastWakeCounter[%d]"
- "associateToWiFiNetwork:password:is8021X:remember:addReason:possiblyHidden:interfaceName:authorization:connection:isAutoJoin:error:"

```
