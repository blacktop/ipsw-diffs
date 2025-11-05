## Installer Progress

> `/System/Library/CoreServices/Installer Progress.app/Contents/MacOS/Installer Progress`

```diff

-15.0.0.1.0
-  __TEXT.__text: 0x11100
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x3060
-  __TEXT.__objc_methlist: 0xeb8
-  __TEXT.__cstring: 0x406a
+15.5.1.0.0
+  __TEXT.__text: 0x12290
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x1324
+  __TEXT.__cstring: 0x4a51
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__objc_methname: 0x370d
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__objc_methname: 0x371d
   __TEXT.__objc_classname: 0x1b7
   __TEXT.__objc_methtype: 0x89c
+  __TEXT.__oslogstring: 0x3
   __TEXT.__ustring: 0x64
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__auth_got: 0x4b8
+  __TEXT.__unwind_info: 0x508
+  __DATA_CONST.__auth_got: 0x4d0
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x720
-  __DATA_CONST.__cfstring: 0x2600
+  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__cfstring: 0x33c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x27f0
-  __DATA.__objc_selrefs: 0xf70
+  __DATA.__objc_const: 0x1f88
+  __DATA.__objc_selrefs: 0x1138
   __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x310
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0xd0
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libScreenReader.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEED4F26-CCAF-3C45-A0D7-59D74CB9A185
-  Functions: 417
-  Symbols:   230
-  CStrings:  1533
+  UUID: 1E96E066-6660-3A78-A43E-29146012A337
+  Functions: 426
+  Symbols:   233
+  CStrings:  1735
 
Symbols:
+ _NSStringFromPoint
+ __os_log_impl
+ _os_log_create
+ _os_log_type_enabled
- _syslog
CStrings:
+ "     NSPointInRect(dimensionsCenter, windowFrame) %@"
+ "     NSPointInRect(windowFrameCenter, dimensions) %@"
+ "     dimensions %@"
+ "     dimensionsCenter %@"
+ "     windowFrame %@"
+ "     windowFrameCenter %@"
+ "    self.shieldWindows = %@"
+ "%p"
+ "%p: handler = %p, _progressBar = %p"
+ "%s: %@"
+ "%s: %x: Adding windows %@ to Unmanaged Space %x"
+ "%s: %x: Created space %x"
+ "%s: %x: Removing Unmanaged Space %x"
+ "%s: %x: Removing windows %@"
+ "%s: %x: Setting space level %x"
+ "%s: Adding window %x"
+ "%s: The color is the same as the first color, this may be an Apple Logo boot image"
+ "%s: The middle color is not the same as the first color, this may be an Apple Logo boot image"
+ "%s: colorsEqual = %@"
+ "%s: enter"
+ "%s: enter: self = %@"
+ "%s: firstColor = sampleColor[%lld][%lld] (%f, %f) = %@"
+ "%s: sampleColor[%lld][%lld] (%f, %f) = %@"
+ "%s: testColor[%lld][%lld] = %@"
+ "-[IASPApplicationListener hideProgressUI]"
+ "-[IASPApplicationListener hideProgressUI]_block_invoke"
+ "-[IASPApplicationListener isShowingUI:]"
+ "-[IASPApplicationListener isShowingUI:]_block_invoke"
+ "-[IASPApplicationListener registerClient:]"
+ "-[IASPApplicationListener registerClient:completionHandler:]"
+ "-[IASPApplicationListener setBatteryInfo:]"
+ "-[IASPApplicationListener setBatteryInfo:]_block_invoke"
+ "-[IASPApplicationListener setPhaseAlternateStatus:]"
+ "-[IASPApplicationListener setPhaseDone:]"
+ "-[IASPApplicationListener setPhaseProgress:]"
+ "-[IASPApplicationListener setPhaseStatus:]"
+ "-[IASPApplicationListener setProgressIndicatorInfo:]"
+ "-[IASPApplicationListener setProgressIndicatorInfo:]_block_invoke"
+ "-[IASPApplicationListener showProgressUI:]"
+ "-[IASPApplicationListener unregisterClient:]"
+ "-[IASPShieldWindow _alternateStatuses:]"
+ "-[IASPShieldWindow _flashBattery:]"
+ "-[IASPShieldWindow _progressBarYConstant]"
+ "-[IASPShieldWindow _startAlternatingStatusTimer]"
+ "-[IASPShieldWindow _stopAlternatingStatusTimer]"
+ "-[IASPShieldWindow hasProgressBar]"
+ "-[IASPShieldWindow initWithScreenRect:andInitialProgressValue:]"
+ "-[IASPShieldWindow orderOut:]"
+ "-[IASPShieldWindow setDebugInfo:]"
+ "-[IASPShieldWindow setHasProgressBar:]"
+ "-[IASPShieldWindow setProgress:animate:]"
+ "-[IASPShieldWindow setProgressAnimationCompletionHandler:]"
+ "-[IASPShieldWindow setProgressAnimationCompletionHandler:]_block_invoke"
+ "-[IASPShieldWindow setProgressIndicatorHidden:]"
+ "-[IASPShieldWindowController _beginDisplayChange]"
+ "-[IASPShieldWindowController _displaysDidChange:]"
+ "-[IASPShieldWindowController _endDisplayChange:]"
+ "-[IASPShieldWindowController _fadeCGShieldWindow]_block_invoke"
+ "-[IASPShieldWindowController _finishHidingWindows]"
+ "-[IASPShieldWindowController _startOrUpdateDisplayReconfigurationTimer:]"
+ "-[IASPShieldWindowController setAlternateStatus:]"
+ "-[IASPShieldWindowController setDebugInfo:]"
+ "-[IASPShieldWindowController setStatus:]"
+ "-[IASPShieldWindowController setWindowLevels:]"
+ "-[IASUnifiedProgressConnection _startReleaseTimer]"
+ "================"
+ "Acquire the boot windows from the window server"
+ "Adding CG shield window %x to space"
+ "Adding window %x to space"
+ "Alternating Statuses"
+ "Battery timer is not running"
+ "Before level = %d, self.shieldWindows = %@"
+ "Client using Setup Assistant phase name was registered"
+ "Fading out shield window"
+ "Flashing the battery interior"
+ "Hide Progress UI"
+ "Initializing the window controller"
+ "Is Showing UI"
+ "Logging also using os_log, installerProgressLog = %p"
+ "Make sure status is visible and alternate status is not"
+ "NSHeight(self.frame) = %1.2f"
+ "No shield windows available on which to set the completion handler"
+ "Releasing boot window %x"
+ "Releasing the connection %p"
+ "Resume timer"
+ "Set Progress: currentPhase = \"%@\", progress = %3.1f, adjusted progress = %3.1f, animate = %@"
+ "Setting animation completion handler to %p"
+ "Shield window fade complete"
+ "Starting release timer"
+ "Status timer is not running"
+ "Stop using AppKit display change notification"
+ "Stop using CoreGraphics notification and callback"
+ "The first sampled color is %@"
+ "Window info %@"
+ "_AddWindowToUnmanagedSpace"
+ "_AddWindowsToUnmanagedSpace"
+ "_RemoveUnmanagedSpace"
+ "_RemoveWindowsFromUnmanagedSpace"
+ "_batteryOutlineView created"
+ "_hasProgressBar = %d"
+ "_lowBatteryView created"
+ "all"
+ "alternateStatus = \"%@\""
+ "attempting to activate %@"
+ "created window %@ for screen %ld"
+ "debugInfo = \"%@\""
+ "dstRect after: {{ %1.2f, %1.2f }, { %1.2f, %1.2f }}"
+ "dstRect before: {{ %1.2f, %1.2f }, { %1.2f, %1.2f }}"
+ "enter: alternateStatusInfo = %@"
+ "enter: batteryInfo = %@"
+ "enter: clientInfo = %@"
+ "enter: completion handler = %p, clientInfo = %@"
+ "enter: doneInfo = %@"
+ "enter: progressIndicatorInfo = %@"
+ "enter: progressInfo = %@"
+ "enter: statusInfo = %@"
+ "executing from serial queue"
+ "executing from serial queue %p: clientInfo = %@"
+ "executing from serial queue: alternateStatusInfo = %@"
+ "executing from serial queue: batteryInfo = %@"
+ "executing from serial queue: clientInfo = %@"
+ "executing from serial queue: completion handler = %p, clientInfo = %@"
+ "executing from serial queue: doneInfo = %@"
+ "executing from serial queue: progressIndicatorInfo = %@"
+ "executing from serial queue: progressInfo = %@"
+ "executing from serial queue: statusInfo = %@"
+ "finalImage = %@"
+ "flag = %@"
+ "handlesNotifications = %d"
+ "height = %1.2f"
+ "hidden = %d"
+ "imageArray = %@"
+ "inValue = %f, inAnimate = %d, self.shieldWindows = %@"
+ "info = %@"
+ "initWithFormat:"
+ "itr %d - windowID %d"
+ "itr %d, windowID %d is the best one to use"
+ "mutableClientInfo = %@"
+ "origin x: %f, y: %f"
+ "phaseName = \"%@\""
+ "progress = %f: animate = %d"
+ "progress back buffer data = %@"
+ "progress bar constant = %1.2f"
+ "progress complete calling handler"
+ "progressBarBackgroundImage = %@"
+ "screens = %@"
+ "self = %p"
+ "self.progressBarYPosition = %1.2f"
+ "self.shieldWindows = %@"
+ "shieldWindows = %@"
+ "shieldWindows = %@, onscreen = %d"
+ "start timer with fireDate = %@"
+ "status = \"%@\""
+ "update fireDate = %@"
+ "window %ld %@"
+ "window.progressBarYPosition set to %1.2f"
+ "windowID = %d"
- "+[IASPRegistryManager clear]"
- "+[IASPRegistryManager currentPhaseName]"
- "+[IASPRegistryManager phases]"
- "+[IASPRegistryManager setCurrentPhaseName:]"
- "+[IASPRegistryManager setPhases:]"
- "+[IASPRegistryManager startingPercentage]"
- "+[IASPShieldWindowController _preMacOSSourceHeight]_block_invoke"
- "+[IASPShieldWindowController scaleForSize:]"
- "-[IASPApplicationListener _logConnectedProcesses]"
- "-[IASPApplicationListener _quitTimerHandler:]_block_invoke"
- "-[IASPApplicationListener _removeConnection:]"
- "-[IASPApplicationListener _removeConnection:]_block_invoke_2"
- "-[IASPApplicationListener _startQuitTimer]"
- "-[IASPApplicationListener clearPhases]_block_invoke"
- "-[IASPApplicationListener getVersion:]"
- "-[IASPApplicationListener hideProgressUI]_block_invoke_2"
- "-[IASPApplicationListener init]_block_invoke"
- "-[IASPApplicationListener init]_block_invoke_2"
- "-[IASPApplicationListener isShowingUI:]_block_invoke_2"
- "-[IASPApplicationListener setPhaseDone:]_block_invoke_3"
- "-[IASPApplicationListener showProgressUI:]_block_invoke_2"
- "-[IASPApplicationProgressControllerListener _joinAuditSessionForConnection:]"
- "-[IASPApplicationProgressControllerListener listener:shouldAcceptNewConnection:]"
- "-[IASPApplicationProgressControllerListener listener:shouldAcceptNewConnection:]_block_invoke"
- "-[IASPApplicationProgressControllerListener listener:shouldAcceptNewConnection:]_block_invoke_2"
- "-[IASPPhaseManager _setDoneForPhaseWithName:]"
- "-[IASPPhaseManager _setProgress:forPhaseWithName:]"
- "-[IASPPhaseManager _totalPercentage]"
- "-[IASPPhaseManager addPhase:]"
- "-[IASPPhaseManager loadPhases]"
- "-[IASPPhaseManager logPhases]"
- "-[IASPShieldWindow _flashBattery:]_block_invoke"
- "-[IASPShieldWindow _startFlashingBattery]"
- "-[IASPShieldWindow keyDown:]"
- "-[IASPShieldWindow sendEvent:]"
- "-[IASPShieldWindow setBatteryIsLow:]"
- "-[IASPShieldWindowController _callAnimationCompletionHandler]"
- "-[IASPShieldWindowController _orderCGShieldWindowOut]"
- "-[IASPShieldWindowController _windowServerConnection]"
- "-[IASPShieldWindowController hideWindows]"
- "-[IASPShieldWindowController hideWindows]_block_invoke"
- "-[IASPShieldWindowController setBatteryIsLow:]"
- "-[IASPShieldWindowController setProgress:animate:]"
- "-[IASPShieldWindowController setProgressIndicatorHidden:]"
- "-[IASPShieldWindowController showWindows]"
- "-[IASPShieldWindowController showWindows]_block_invoke"
- "-[IASUnifiedProgressConnection connectionForCaller:]"
- "-[IASUnifiedProgressConnection connectionForCaller:]_block_invoke"
- "-[IASUnifiedProgressConnection releaseConnectionForCaller:]"
- "-[IASUnifiedProgressManager _isModernOS]_block_invoke"
- "-[IASUnifiedProgressManager _isModernOS]_block_invoke_2"
- "-[IASUnifiedProgressManager addPhaseNamed:withProgress:exitDelay:]"
- "-[IASUnifiedProgressManager clear]"
- "-[IPAppDelegate applicationDidFinishLaunching:]"
- "-[IPAppDelegate applicationDidFinishLaunching:]_block_invoke"
- "-[IPAppDelegate hideCursor]"
- "-[IPAppDelegate lowerProgressApp:]"
- "-[IPAppDelegate quitProgressApp:]"
- "-[IPAppDelegate quit]"
- "-[IPAppDelegate setBackgroundOnly:]"
- "-[IPAppDelegate setHotKeysEnabled:]"
- "-[IPAppDelegate showCursor]"
- "DisplaysWillChangeWhileHidingWindows"
- "IASPGetBootMode_block_invoke"
- "IASPIsUsingFileVault_block_invoke"
- "main"

```
