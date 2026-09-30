## SystemStatusUI

> `/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI`

```diff

-2963.3.5.0.0
-  __TEXT.__text: 0x715c
+2963.3.6.0.0
+  __TEXT.__text: 0x72e8
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0xa58
-  __TEXT.__cstring: 0x2c2c
+  __TEXT.__cstring: 0x233d
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__unwind_info: 0x300
   __TEXT.__objc_classname: 0x924
-  __TEXT.__objc_methname: 0xd04
+  __TEXT.__objc_methname: 0xd33
   __TEXT.__objc_methtype: 0x103
-  __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x340
+  __TEXT.__objc_stubs: 0xd80
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x2d20
+  __AUTH_CONST.__cfstring: 0x2860
   __AUTH_CONST.__objc_const: 0x1dd0
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__bss: 0x9

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 203
-  Symbols:   429
-  CStrings:  579
+  Functions: 204
+  Symbols:   469
+  CStrings:  544
 
Symbols:
+ _STBackgroundActivityIdentifierActivePushToTalkCall
+ _STBackgroundActivityIdentifierAirPrint
+ _STBackgroundActivityIdentifierAssistantEyesFree
+ _STBackgroundActivityIdentifierAutoAirPlayPlaying
+ _STBackgroundActivityIdentifierAutoAirPlayReady
+ _STBackgroundActivityIdentifierBackgroundLocation
+ _STBackgroundActivityIdentifierCallHandoff
+ _STBackgroundActivityIdentifierCallRinging
+ _STBackgroundActivityIdentifierCallScreening
+ _STBackgroundActivityIdentifierCarPlay
+ _STBackgroundActivityIdentifierCellularSOS
+ _STBackgroundActivityIdentifierDeveloperTools
+ _STBackgroundActivityIdentifierDiagnostics
+ _STBackgroundActivityIdentifierFullScreenWebRTCAudioCapture
+ _STBackgroundActivityIdentifierFullScreenWebRTCCapture
+ _STBackgroundActivityIdentifierHearingAidRecording
+ _STBackgroundActivityIdentifierIdlePushToTalkCall
+ _STBackgroundActivityIdentifierInCall
+ _STBackgroundActivityIdentifierInVideoConference
+ _STBackgroundActivityIdentifierLoggingCapture
+ _STBackgroundActivityIdentifierNavigation
+ _STBackgroundActivityIdentifierNearbyInteractions
+ _STBackgroundActivityIdentifierPlaygrounds
+ _STBackgroundActivityIdentifierRecording
+ _STBackgroundActivityIdentifierSatelliteSOS
+ _STBackgroundActivityIdentifierSatelliteSOSDisconnected
+ _STBackgroundActivityIdentifierScreenReplayRecording
+ _STBackgroundActivityIdentifierScreenSharing
+ _STBackgroundActivityIdentifierScreenSharingServer
+ _STBackgroundActivityIdentifierSharePlay
+ _STBackgroundActivityIdentifierSharePlayInactive
+ _STBackgroundActivityIdentifierSharePlayScreenSharing
+ _STBackgroundActivityIdentifierSysdiagnose
+ _STBackgroundActivityIdentifierTethering
+ _STBackgroundActivityIdentifierVideoConferenceHandoff
+ _STBackgroundActivityIdentifierVideoConferenceRinging
+ _STBackgroundActivityIdentifierVideoOut
+ _STBackgroundActivityIdentifierWebRTCAudioCapture
+ _STBackgroundActivityIdentifierWebRTCCapture
CStrings:
+ "setAccessibilityValueBlock:"
+ "status.satellite"
- "com.apple.systemstatus.background-activity.ActivePushToTalkCall"
- "com.apple.systemstatus.background-activity.AirPrint"
- "com.apple.systemstatus.background-activity.AssistantEyesFree"
- "com.apple.systemstatus.background-activity.AutoAirPlayPlaying"
- "com.apple.systemstatus.background-activity.AutoAirPlayReady"
- "com.apple.systemstatus.background-activity.BackgroundLocation"
- "com.apple.systemstatus.background-activity.CallHandoff"
- "com.apple.systemstatus.background-activity.CallRinging"
- "com.apple.systemstatus.background-activity.CallScreening"
- "com.apple.systemstatus.background-activity.CarPlay"
- "com.apple.systemstatus.background-activity.CellularSOS"
- "com.apple.systemstatus.background-activity.DeveloperTools"
- "com.apple.systemstatus.background-activity.Diagnostics"
- "com.apple.systemstatus.background-activity.FullScreenWebRTCAudioCapture"
- "com.apple.systemstatus.background-activity.FullScreenWebRTCCapture"
- "com.apple.systemstatus.background-activity.HearingAidRecording"
- "com.apple.systemstatus.background-activity.IdlePushToTalkCall"
- "com.apple.systemstatus.background-activity.InCall"
- "com.apple.systemstatus.background-activity.InVideoConference"
- "com.apple.systemstatus.background-activity.LoggingCapture"
- "com.apple.systemstatus.background-activity.Navigation"
- "com.apple.systemstatus.background-activity.NearbyInteractions"
- "com.apple.systemstatus.background-activity.Playgrounds"
- "com.apple.systemstatus.background-activity.Recording"
- "com.apple.systemstatus.background-activity.SatelliteSOS"
- "com.apple.systemstatus.background-activity.SatelliteSOSDisconnected"
- "com.apple.systemstatus.background-activity.ScreenReplayRecording"
- "com.apple.systemstatus.background-activity.ScreenSharing"
- "com.apple.systemstatus.background-activity.ScreenSharingServer"
- "com.apple.systemstatus.background-activity.SharePlay"
- "com.apple.systemstatus.background-activity.SharePlayInactive"
- "com.apple.systemstatus.background-activity.SharePlayScreenSharing"
- "com.apple.systemstatus.background-activity.Sysdiagnose"
- "com.apple.systemstatus.background-activity.Tethering"
- "com.apple.systemstatus.background-activity.VideoConferenceHandoff"
- "com.apple.systemstatus.background-activity.VideoConferenceRinging"
- "com.apple.systemstatus.background-activity.VideoOut"
- "com.apple.systemstatus.background-activity.WebRTCAudioCapture"
- "com.apple.systemstatus.background-activity.WebRTCCapture"

```
