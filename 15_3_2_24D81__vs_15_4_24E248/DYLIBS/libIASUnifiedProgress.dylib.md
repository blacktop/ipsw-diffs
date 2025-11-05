## libIASUnifiedProgress.dylib

> `/usr/lib/libIASUnifiedProgress.dylib`

```diff

-15.0.0.1.0
-  __TEXT.__text: 0x4e20
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x660
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__cstring: 0x16e6
-  __TEXT.__unwind_info: 0x238
+15.5.1.0.0
+  __TEXT.__text: 0x5064
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0x8a4
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x140
+  __TEXT.__cstring: 0x1415
+  __TEXT.__oslogstring: 0x3
+  __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x115
-  __TEXT.__objc_methname: 0x1185
+  __TEXT.__objc_methname: 0x1195
   __TEXT.__objc_methtype: 0x2d8
-  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d0
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1260
+  __DATA_CONST.__objc_selrefs: 0x658
+  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0xd00
+  __AUTH_CONST.__objc_const: 0xe38
   __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x98
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x2b0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF350A27-79F0-3422-9492-0A7C4B625A25
-  Functions: 160
-  Symbols:   519
-  CStrings:  547
+  UUID: 5530D725-1882-3D36-BC02-C7418A0B1507
+  Functions: 167
+  Symbols:   532
+  CStrings:  545
 
Symbols:
+ +[IASPPhaseManager sharedPhaseManager].cold.1
+ +[IASUnifiedProgressConnection sharedConnection].cold.1
+ +[IASUnifiedProgressManager sharedManager].cold.1
+ _IASPLog.cold.1
+ _IASPLog.installerProgressLog
+ _IASPLog.token
+ __IASPLog
+ ____IASPLog_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e8_v12?0B8l
+ ___copy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48r
+ __os_log_impl
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$phaseName
+ _os_log_create
+ _os_log_type_enabled
+ _syslog$DARWIN_EXTSN
- _StartDebugLogging
- _StopDebugLogging
- _WriteDebugLog
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8l
- _syslog
CStrings:
+ "%@"
+ "%s: %@"
+ "-[IASUnifiedProgressClient isShowingUI]_block_invoke"
+ "-[IASUnifiedProgressClient setProgress:animate:]"
+ "-[IASUnifiedProgressConnection _startReleaseTimer]"
+ "Logging also using os_log, installerProgressLog = %p"
+ "Releasing the connection %p"
+ "Starting release timer"
+ "all"
+ "client %p: phaseName \"%@\": progress %f: animate %d"
+ "client %p: phaseName = \"%@\""
+ "client %p: phaseName = \"%@\", inIsShowingUI = %d"
+ "client %p: phaseName = \"%@\", isShowingUI semaphore timedout"
+ "client %p: phaseName = \"%@\": status = \"%@\""
+ "client %p: phaseName = \"%@\": status = \"%@\": _prevStatus = \"%@\""
+ "com.apple.Installer-Progress"
+ "initWithFormat:"
+ "status \"%@\" is same as previous status \"%@\""
- "+[IASPRegistryManager clear]"
- "+[IASPRegistryManager currentPhaseName]"
- "+[IASPRegistryManager phases]"
- "+[IASPRegistryManager setCurrentPhaseName:]"
- "+[IASPRegistryManager setPhases:]"
- "+[IASPRegistryManager startingPercentage]"
- "-[IASPPhaseManager _setDoneForPhaseWithName:]"
- "-[IASPPhaseManager _setProgress:forPhaseWithName:]"
- "-[IASPPhaseManager _totalPercentage]"
- "-[IASPPhaseManager addPhase:]"
- "-[IASPPhaseManager loadPhases]"
- "-[IASPPhaseManager logPhases]"
- "-[IASUnifiedProgressClient _registerConnection]"
- "-[IASUnifiedProgressClient _registerConnection]_block_invoke"
- "-[IASUnifiedProgressClient connectionInterrupted]"
- "-[IASUnifiedProgressClient dealloc]"
- "-[IASUnifiedProgressClient hideProgressUI]"
- "-[IASUnifiedProgressClient initWithPhaseName:]"
- "-[IASUnifiedProgressClient registerCompletionHandler:]"
- "-[IASUnifiedProgressClient setBatteryIsLow:]"
- "-[IASUnifiedProgressClient setDone]"
- "-[IASUnifiedProgressClient setProgressIndicatorHidden:]"
- "-[IASUnifiedProgressClient showProgressUI]"
- "-[IASUnifiedProgressConnection connectionForCaller:]"
- "-[IASUnifiedProgressConnection connectionForCaller:]_block_invoke"
- "-[IASUnifiedProgressConnection releaseConnectionForCaller:]"
- "-[IASUnifiedProgressManager _isModernOS]_block_invoke"
- "-[IASUnifiedProgressManager _isModernOS]_block_invoke_2"
- "-[IASUnifiedProgressManager addPhaseNamed:withProgress:exitDelay:]"
- "-[IASUnifiedProgressManager clear]"

```
