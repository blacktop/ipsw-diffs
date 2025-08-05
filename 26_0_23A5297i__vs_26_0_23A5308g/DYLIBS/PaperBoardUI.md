## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x80ee4
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0xa164
+289.103.0.0.0
+  __TEXT.__text: 0x817a8
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0xa1e4
   __TEXT.__const: 0x838
-  __TEXT.__cstring: 0x7b12
-  __TEXT.__oslogstring: 0x43e3
-  __TEXT.__gcc_except_tab: 0x1218
+  __TEXT.__cstring: 0x7b8b
+  __TEXT.__oslogstring: 0x454a
+  __TEXT.__gcc_except_tab: 0x120c
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x2c18
-  __TEXT.__objc_classname: 0x15f1
-  __TEXT.__objc_methname: 0x17fb5
-  __TEXT.__objc_methtype: 0x4133
-  __TEXT.__objc_stubs: 0x11f40
-  __DATA_CONST.__got: 0x940
-  __DATA_CONST.__const: 0x2898
-  __DATA_CONST.__objc_classlist: 0x3c8
+  __TEXT.__unwind_info: 0x2c40
+  __TEXT.__objc_classname: 0x1601
+  __TEXT.__objc_methname: 0x18072
+  __TEXT.__objc_methtype: 0x410f
+  __TEXT.__objc_stubs: 0x11fa0
+  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__const: 0x28c0
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5418
+  __DATA_CONST.__objc_selrefs: 0x5440
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x848
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0x6360
-  __AUTH_CONST.__objc_const: 0x1ca80
+  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__const: 0xbe0
+  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__objc_const: 0x1cbd8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x90
-  __AUTH.__objc_data: 0x2210
+  __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xa60
+  __DATA.__objc_ivar: 0xa6c
   __DATA.__data: 0x18e0
-  __DATA.__bss: 0x418
-  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA.__bss: 0x438
+  __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC9B04E9-93A8-3CF0-9F70-587FAEA6D8FF
-  Functions: 4000
-  Symbols:   13813
-  CStrings:  6565
+  UUID: F0C7B5F9-0A18-34A4-A2FE-F2113F961B1A
+  Functions: 4017
+  Symbols:   13866
+  CStrings:  6593
 
Symbols:
+ +[PBUIPowerLogger sendTelemetryForPosterForegroundChange:posterProviderID:posterPowerlogIdentifier:]
+ +[PBUIPowerLogger sendTelemetryForPosterForegroundChange:posterProviderID:posterPowerlogIdentifier:].cold.1
+ +[PBUIPowerLogger sendTelemetryForPosterForegroundChange:posterProviderID:posterPowerlogIdentifier:].cold.2
+ -[PBUIPosterHomeViewController _accessibilityReduceTransparencyChanged:]
+ -[PBUIPosterLockViewController _updateExtendedRenderSessionForScene:]
+ -[PBUIPosterViewController _updatePowerlogStatus]
+ -[PBUIPosterViewController isDeviceMotionEventGenerationActive]
+ -[PBUIPosterViewController posterComponent:didUpdateInExtendedRenderSession:]
+ -[PBUIPosterViewController posterIsActive]
+ -[PBUIPosterViewController setDeviceMotionEventGenerationActive:]
+ -[PBUIPosterViewController setPosterIsActive:]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateInExtendedRenderSession:]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdateInExtendedRenderSession:]
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table57
+ _OBJC_CLASS_$_PBUIPowerLogger
+ _OBJC_IVAR_$_PBUIPosterViewController._deviceMotionEventGenerationActive
+ _OBJC_IVAR_$_PBUIPosterViewController._posterIsActive
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._deviceMotionKeepActiveReason
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._extendedRenderSessionKeepActiveReason
+ _OBJC_METACLASS_$_PBUIPowerLogger
+ _PBUILogPower
+ _PBUILogPower.__logObj
+ _PBUILogPower.cold.1
+ _PBUILogPower.onceToken
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __OBJC_$_CLASS_METHODS_PBUIPowerLogger
+ __OBJC_CLASS_RO_$_PBUIPowerLogger
+ __OBJC_METACLASS_RO_$_PBUIPowerLogger
+ ___106-[PBUIPosterLockViewController scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke_2
+ ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.81
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.154
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.155
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.156
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.159
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.163
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.172
+ ___PBUILogPower_block_invoke
+ ____sharedWallpaperMetricsTelemetryIdentifier_block_invoke
+ ____sharedWallpaperMetricsTelemetryIdentifier_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e12_v24?0Q8^v16ls32l8s40l8
+ __sharedWallpaperMetricsTelemetryIdentifier.onceToken
+ __sharedWallpaperMetricsTelemetryIdentifier.telemetryIdentifier
+ _objc_msgSend$_updateExtendedRenderSessionForScene:
+ _objc_msgSend$_updatePowerlogStatus
+ _objc_msgSend$initWithScene:
+ _objc_msgSend$posterComponent:didUpdateInExtendedRenderSession:
+ _objc_msgSend$providerBundleIdentifier
+ _objc_msgSend$pui_powerlogIdentifier
+ _objc_msgSend$sendTelemetryForPosterForegroundChange:posterProviderID:posterPowerlogIdentifier:
- -[PBUIPosterViewController deviceMotionEventGenerationDidStop]
- -[PBUIPosterViewController deviceMotionEventGenerationWillStart]
- _OBJC_IVAR_$_PBUIPosterViewController._renderingServiceServerKeepAliveAssertionManager
- ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.75
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.151
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.152
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.153
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.156
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.160
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.169
- _objc_msgSend$deviceMotionEventGenerationDidStop
- _objc_msgSend$deviceMotionEventGenerationWillStart
- _objc_msgSend$initWithScene:renderingServiceServerKeepAliveAssertionManager:
- _objc_msgSend$renderingServiceServer
CStrings:
+ "\v"
+ "ApplicationMetrics"
+ "Failed to weak-link PPSCreateTelemetryIdentifier"
+ "Failed to weak-link PPSSendTelemetry"
+ "Jul 31 2025 21:24:23"
+ "PBUIPowerLogger"
+ "Poster Extant update DID change"
+ "Power"
+ "Sent Telemetry: foreground=%{BOOL}d, posterID=%{public}@, posterPowerlogIdentifier=%lu"
+ "TB,N,V_posterIsActive"
+ "Updating powerlog for %{public}@ (%lu): going background"
+ "Updating powerlog for %{public}@ (%lu): going foreground with %lu activelyRequiredReasons, %lu defaultModeAssertion reasons"
+ "WallpaperID"
+ "WallpaperSession"
+ "WallpaperType"
+ "[%{public}@] Poster Extant %lu did change content"
+ "[%{public}@] Poster Extant update COULD change %lu (%lu)"
+ "[%{public}@] Poster Extant update DID change"
+ "[%{public}@] Poster last extant update changed %lu"
+ "_deviceMotionKeepActiveReason"
+ "_extendedRenderSessionKeepActiveReason"
+ "_posterIsActive"
+ "_updateExtendedRenderSessionForScene:"
+ "_updatePowerlogStatus"
+ "background"
+ "device motion"
+ "event"
+ "in extended render session"
+ "initWithScene:"
+ "posterComponent:didUpdateInExtendedRenderSession:"
+ "posterIsActive"
+ "providerBundleIdentifier"
+ "pui_powerlogIdentifier"
+ "sendTelemetryForPosterForegroundChange:posterProviderID:posterPowerlogIdentifier:"
+ "setPosterIsActive:"
+ "v36@0:8B16@20Q28"
+ "\xf0\xe1"
- "@\"PRRenderingServiceServerKeepAliveAssertionManager\""
- "Jul 16 2025 21:39:12"
- "Poster Extact update DID change"
- "[%{public}@] Poster Extact %lu did change content"
- "[%{public}@] Poster Extact update COULD change %lu (%lu)"
- "[%{public}@] Poster Extact update DID change"
- "[%{public}@] Poster Extact update changed %lu"
- "_renderingServiceServerKeepAliveAssertionManager"
- "auto"
- "deviceMotionEventGenerationDidStop"
- "deviceMotionEventGenerationWillStart"
- "initWithScene:renderingServiceServerKeepAliveAssertionManager:"
- "renderingServiceServer"
- "\xf0\xc1"
- "\xf0\xf0!"

```
