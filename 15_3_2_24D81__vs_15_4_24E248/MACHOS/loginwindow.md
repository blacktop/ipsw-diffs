## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

-3037.3.4.1.0
-  __TEXT.__text: 0xcc970
+3037.5.5.0.0
+  __TEXT.__text: 0xcc4a0
   __TEXT.__auth_stubs: 0x2bc0
-  __TEXT.__objc_stubs: 0xeaa0
-  __TEXT.__objc_methlist: 0x5970
+  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_methlist: 0x61fc
   __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0x111c
-  __TEXT.__objc_methname: 0x105d3
-  __TEXT.__oslogstring: 0x26815
-  __TEXT.__cstring: 0x119d4
+  __TEXT.__gcc_except_tab: 0x1120
+  __TEXT.__objc_methname: 0x1061d
+  __TEXT.__oslogstring: 0x267f2
+  __TEXT.__cstring: 0x118aa
   __TEXT.__objc_classname: 0x82d
   __TEXT.__objc_methtype: 0x1f43
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__unwind_info: 0x1b58
+  __TEXT.__unwind_info: 0x1b80
   __DATA_CONST.__auth_got: 0x15f0
-  __DATA_CONST.__got: 0x958
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1e50
-  __DATA_CONST.__cfstring: 0x6900
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x1e88
+  __DATA_CONST.__cfstring: 0x67c0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_arrayobj: 0x498
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x9478
-  __DATA.__objc_selrefs: 0x45f0
+  __DATA.__objc_const: 0x84e0
+  __DATA.__objc_selrefs: 0x4828
   __DATA.__objc_ivar: 0x804
   __DATA.__objc_data: 0x1900
   __DATA.__data: 0x878
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x58
-  __DATA.__bss: 0x768
+  __DATA.__bss: 0x760
   __CGPreLoginApp.__cgpreloginapp: 0x0
   __RESTRICT.__restrict: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libquit.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 73F34DCF-6AB4-348F-85E4-9529092F776E
-  Functions: 2354
+  UUID: E6E482D2-F006-35F8-A1C8-A1AF4E216214
+  Functions: 2409
   Symbols:   1022
-  CStrings:  9283
+  CStrings:  9265
 
CStrings:
+ "%s |        dark install, do not lock"
+ "%s |        screen lock is not enabled, do not lock"
+ "%s | Calling delegate %p, responds to selector %d"
+ "%s | ERROR |    permitted front array =\n%@"
+ "%s | ERROR | MiniBuddy exit in user session with non-zero status: %ld, logging out."
+ "%s | ERROR | TestScreenLockTTR pref is enabled"
+ "%s | ERROR | loginwindow is not in the permitted frontmost array"
+ "%s | Setting clamshellState.clamshellIsClosed to %d"
+ "%s | clamshellState.clamshellIsClosed == clamshellIsClosed"
+ "%s | passwordDelay = %d"
+ "-[ScreenSaverDaemon resume]"
+ "-[UserInfo hasLocalUser]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/loginwindow/Source/FirstLoginOptimizer.m"
+ "_prepareUserController"
+ "hasLocalUser"
+ "isDirAdminUser"
+ "isMBSetupUser"
+ "isOtherUser"
+ "localUsers"
+ "repairMacBuddyCookieIfNeeded"
- "%s |      checking needsRootSAS: %d"
- "%s | !allowOriginalBehavior checking if the machine has additional accounts"
- "%s | Deferred Mandatory Update: allowOriginalBehavior"
- "%s | ERROR | loginwindow is not in the permitted frontmost array: %@"
- "%s | Enter, event type: %lu"
- "%s | Found local users ignore missing setup done"
- "%s | Internal build, allowOriginalBehavior: %d"
- "%s | No local users found"
- "%s | Setup Resume allowOriginalBehavior"
- "%s | askForPassword being set to YES (always), passwordDelay = %d"
- "%s | tracking init success, attempting to do account scan"
- "-DeferredMandatoryUpdate"
- "-EOSBuddyYes"
- "-MigrationBuddyYes"
- "-ShouldHealEOS"
- "-[LWDefaultScreenLockUI lockUIIsOnScreen]"
- "/AppleInternal"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/loginwindow/Source/FirstLoginOptimizer.m"
- "AllowMacBuddyWithExistingAccounts"
- "DeferredMandatoryUpdate"
- "LoginInstallNeedsEOSHelperOnly"
- "LoginInstallNeedsMigration"
- "LoginInstallNeedsSASAndEOSHelper"
- "createFileAtPath:contents:attributes:"
- "data"
- "localSearchNode"
- "missingSetupDoneIgnoreAndReplaceIfNeeded"
- "stopScreenSaver"

```
