## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3109.0.0.0.0
-  __TEXT.__text: 0xc8fb0
-  __TEXT.__auth_stubs: 0x2ce0
-  __TEXT.__objc_stubs: 0xff60
-  __TEXT.__objc_methlist: 0x6b64
+3109.2.3.0.0
+  __TEXT.__text: 0xcaf78
+  __TEXT.__auth_stubs: 0x2d10
+  __TEXT.__objc_stubs: 0x101a0
+  __TEXT.__objc_methlist: 0x6c74
   __TEXT.__const: 0x2e8
-  __TEXT.__gcc_except_tab: 0x1064
-  __TEXT.__objc_methname: 0x1232d
-  __TEXT.__oslogstring: 0x29a9c
-  __TEXT.__cstring: 0x12c88
-  __TEXT.__objc_classname: 0x87a
-  __TEXT.__objc_methtype: 0x21af
+  __TEXT.__gcc_except_tab: 0x106c
+  __TEXT.__objc_methname: 0x1270e
+  __TEXT.__oslogstring: 0x2a5ac
+  __TEXT.__cstring: 0x12eb8
+  __TEXT.__objc_classname: 0x88a
+  __TEXT.__objc_methtype: 0x2228
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x36
   __TEXT.__constg_swiftt: 0x44

   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0x53
-  __TEXT.__unwind_info: 0x2610
-  __DATA_CONST.__const: 0x2188
-  __DATA_CONST.__cfstring: 0x6e60
+  __TEXT.__unwind_info: 0x2660
+  __DATA_CONST.__const: 0x21a8
+  __DATA_CONST.__cfstring: 0x6e40
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_intobj: 0x240

   __DATA_CONST.__objc_arrayobj: 0x498
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1680
+  __DATA_CONST.__auth_got: 0x1698
   __DATA_CONST.__got: 0xac8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x8d58
-  __DATA.__objc_selrefs: 0x4f18
-  __DATA.__objc_ivar: 0x868
+  __DATA.__objc_const: 0x8e60
+  __DATA.__objc_selrefs: 0x4fe0
+  __DATA.__objc_ivar: 0x880
   __DATA.__objc_data: 0x1a70
-  __DATA.__data: 0x990
+  __DATA.__data: 0x9f0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x88
   __CGPreLoginApp.__cgpreloginapp: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2613
-  Symbols:   1065
-  CStrings:  9051
+  Functions: 2639
+  Symbols:   1068
+  CStrings:  9137
 
Symbols:
+ _DisableSecureEventInput
+ _EnableSecureEventInput
+ _IsSecureEventInputEnabled
+ _NSPointInRect
+ _NSStringFromPoint
- _CGSSetSecureEventInput
- _IOPMCopyAssertionsByType
CStrings:
+ "!\x81a"
+ "%s | \t secure input dropped; system-wide secure input still enabled (any holder): %d"
+ "%s |                App has already exited but LaunchServices is still listing it, do not add it"
+ "%s |      adopting software update subType %@ for the in flight logout"
+ "%s |      already in progress UI is already showing, leaving it"
+ "%s |      app death for %@ in logout phase %d, no handler for this phase, ignoring"
+ "%s |      app death for %@ while waiting on the Finder (%@), ignoring"
+ "%s |      applying options from the incoming request to the in flight logout"
+ "%s |      no longer waiting on the Finder, phase: %d, nothing to do"
+ "%s |      no pid captured for the Finder, the watchdog will fall back to a LaunchServices liveness check when it fires"
+ "%s |      no valid pid for app: %@, cannot verify - treating it as still running"
+ "%s |      pid %d no longer exists"
+ "%s |      reconciled the request with the in flight logout, not showing UI"
+ "%s |      sending SU notification for the newly-software-update logout"
+ "%s |      subType is software update, setting default update flags"
+ "%s |      upgrading the in flight end action from %@ to %@"
+ "%s |     loginwindow UI handoff, Installer Progress owns this transition, no snapshot needed"
+ "%s |     repositioning spinner from %@ to origin %@ (old frame %@, new frame %@)"
+ "%s | %sSecureEventInput"
+ "%s | ERROR |      already in flight: type:%d - %@, subType:%d - %@"
+ "%s | ERROR |      dropping the logoutOptions from the rejected request: %@"
+ "%s | ERROR |      logout phase: %d, interrupted: %d"
+ "%s | ERROR |      no start time recorded for the in flight logout"
+ "%s | ERROR |      not waiting on any single app right now"
+ "%s | ERROR |      rejected request:  type:%d - %@, subType:%d - %@"
+ "%s | ERROR |      still waiting on: %@ (%@)"
+ "%s | ERROR |      the in flight logout has been running for %.1f seconds"
+ "%s | ERROR | %sSecureEventInput returned error: %d"
+ "%s | ERROR | beginGUIAppQuit called while a GUI app quit cycle is already running, ignoring"
+ "%s | ERROR | cannot upgrade in flight %@ to %@: already past the point of no return, the request must be re-issued at loginwindow"
+ "%s | ERROR | termination timer fired but %@ is no longer running, its app death notification was missed.  Treating it as quit and continuing the logout"
+ "%s | ERROR | the Finder accepted the quit but failed to terminate, killing it and continuing the logout"
+ "%s | ERROR | the Finder is already gone but its death notification never arrived, continuing the logout"
+ "%s | Enter, reconciling in flight %@ (subType %@) with incoming %@ (subType %@), phase: %d"
+ "%s | PMDisplaySleepIsBlocked IS blocked"
+ "%s | PlatformSSO is enabled, cleaning up before continuing"
+ "%s | PlatformSSO is not enabled, cleaning up on a background queue"
+ "%s | clearing the Finder quit watchdog"
+ "%s | exit, accommodated: %d"
+ "%s | exit, upgrade blocked past the point of no return, nothing merged"
+ "%s | secure event input already %d, nothing to do"
+ "%s | starting the Finder quit watchdog, delay: %f, pid: %d"
+ "-[LWDefaultScreenLockUI notifyPlatformSSOUIVisibilityChanged]"
+ "-[LoginTransition _repositionProgressIndicatorWindowIfOnScreenFrame:toScreenFrame:]"
+ "-[LogoutUtilities appProcessIsAlive:]"
+ "-[LogoutUtilities processExistsForPID:]"
+ "-[SessionLogoutManager _checkFinderQuitStatus:]"
+ "-[SessionLogoutManager logRejectedLogoutRequest:logoutSubType:logoutOptions:]"
+ "-[SessionLogoutManager reconcileInFlightLogoutWithType:logoutSubType:logoutOptions:]"
+ "-[SessionLogoutManager startFinderQuitWatchdog:]"
+ "-[SessionLogoutManager stopFinderQuitWatchdog]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
+ "B32@0:8i16i20@24"
+ "Disable"
+ "Enable"
+ "Finder"
+ "LUI2UIControllerDelegate"
+ "TB,R,V_holdingSecureInput"
+ "TB,V_windowControllerActionInProgress"
+ "_RemovePlatformSSOTemporaryUserHomeDirectories"
+ "_RemovePlatformSSOTemporaryUserHomeDirectories_block_invoke"
+ "_checkFinderQuitStatus:"
+ "_disableSecureEventInput"
+ "_enableSecureEventInput"
+ "_finderQuitPid"
+ "_finderQuitTimer"
+ "_guiAppQuitCycleRunning"
+ "_holdingSecureInput"
+ "_loginTransitionPendingBehindProgress"
+ "_logoutStartTime"
+ "_progressCompletedForLoginWindowUIHandoff"
+ "_repositionProgressIndicatorWindowIfOnScreenFrame:toScreenFrame:"
+ "_specialTransitionInProgress"
+ "appProcessIsAlive:"
+ "holdingSecureInput"
+ "i20@0:8i16"
+ "logRejectedLogoutRequest:logoutSubType:logoutOptions:"
+ "logoutTypeRank:"
+ "notifyPlatformSSOUIVisibilityChanged"
+ "platformSSOEnabled"
+ "platformSSOUIVisibilityDidChange"
+ "platformSSOUIVisible"
+ "processExistsForPID:"
+ "reconcileInFlightLogoutWithType:logoutSubType:logoutOptions:"
+ "removeObserver:forKeyPath:context:"
+ "setFrameOrigin:"
+ "setMiniBuddyInProgress_forTesting:"
+ "setProgressIndicatorWindow_forTesting:"
+ "setTransitionToLoginWindowUIComplete_forTesting:"
+ "setWindowControllerActionInProgress:"
+ "startFinderQuitWatchdog:"
+ "stopFinderQuitWatchdog"
+ "v32@0:8i16i20@24"
+ "v80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "windowControllerActionInProgress"
- "%s | CGSSetSecureEventInput: %d"
- "%s | ERROR | CGSSetSecureEventInput returned error: %d"
- "%s | PMDisplaySleepIsBlocked IS blocked, by %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
- "Assert Name: %@ pid: %d,   "
- "AssertPID"
- "CleanupPlatformSSOTemporaryUserHomeDirectories_block_invoke"
- "assertionType: %@, "
- "\x81a"
```
