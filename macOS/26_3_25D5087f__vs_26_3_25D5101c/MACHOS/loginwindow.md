## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

-3085.3.1.0.0
-  __TEXT.__text: 0xd40c0
+3085.3.3.0.0
+  __TEXT.__text: 0xd4338
   __TEXT.__auth_stubs: 0x2c80
-  __TEXT.__objc_stubs: 0xf400
+  __TEXT.__objc_stubs: 0xf420
   __TEXT.__objc_methlist: 0x6654
   __TEXT.__const: 0x2c0
   __TEXT.__gcc_except_tab: 0x1240
-  __TEXT.__objc_methname: 0x11445
-  __TEXT.__oslogstring: 0x27d65
-  __TEXT.__cstring: 0x123aa
+  __TEXT.__objc_methname: 0x11466
+  __TEXT.__oslogstring: 0x27e6f
+  __TEXT.__cstring: 0x123c4
   __TEXT.__objc_classname: 0x827
   __TEXT.__objc_methtype: 0x2035
   __TEXT.__ustring: 0x1c
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__unwind_info: 0x1c40
+  __TEXT.__unwind_info: 0x1c48
   __DATA_CONST.__auth_got: 0x1650
-  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__got: 0x9b8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x2120
+  __DATA_CONST.__const: 0x2100
   __DATA_CONST.__cfstring: 0x6ea0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x8650
-  __DATA.__objc_selrefs: 0x4bf8
+  __DATA.__objc_selrefs: 0x4c00
   __DATA.__objc_ivar: 0x810
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0x888

   - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/Versions/A/IOMobileFramebuffer
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/Versions/A/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit
   - /System/Library/PrivateFrameworks/ManagedClient.framework/Versions/A/ManagedClient
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/Versions/A/MobileInBoxUpdate

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libquit.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 4E78EEE6-BEA5-3BD3-A41E-47B5C4F15B66
+  UUID: 1CC0EA3A-49AA-3F59-B550-1716CF41A7D4
   Functions: 2522
-  Symbols:   1043
-  CStrings:  9675
+  Symbols:   1045
+  CStrings:  9679
 
Symbols:
+ _OBJC_CLASS_$_LACSExtractablePassword
+ _UAUEnvUserPassword
Functions:
~ sub_10000e9cc -> sub_10000ea6c : 5732 -> 5784
~ sub_10002eb00 -> sub_10002ebd4 : 76 -> 160
~ sub_100035450 -> sub_100035578 : 4940 -> 5436
CStrings:
+ "%s | ERROR | Error creating LACSExtractablePassword for user account updater, but no error was returned"
+ "%s | ERROR | Error creating LACSExtractablePassword for user account updater: error: %@"
+ "%s | password is nil, UAUPlugins will not receive LACSExtractablePassword"
+ "-[UserAccountUpdater launchUserAccountUpdaterIfNecessaryWithPassword:]"
+ "-[UserAccountUpdater launchUserAccountUpdaterIfNecessaryWithPassword:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CGDDugB5wCJZxxgo5oVItD4LMcZHjuT7FzWG8A8/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
+ "/AppleInternal/Library/BuildRoots/4~CGDDugB5wCJZxxgo5oVItD4LMcZHjuT7FzWG8A8/Library/Caches/com.apple.xbs/Sources/loginwindow/Source/FirstLoginOptimizer.m"
+ "initWithData:error:"
+ "launchUserAccountUpdaterIfNecessaryWithPassword:"
- "-[UserAccountUpdater launchUserAccountUpdaterIfNecessary]"
- "-[UserAccountUpdater launchUserAccountUpdaterIfNecessary]_block_invoke"
- "/AppleInternal/Library/BuildRoots/4~CDziugAwSc9KAGT6RVU3DdiZhL92XeDOFme4JDE/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
- "/AppleInternal/Library/BuildRoots/4~CDziugAwSc9KAGT6RVU3DdiZhL92XeDOFme4JDE/Library/Caches/com.apple.xbs/Sources/loginwindow/Source/FirstLoginOptimizer.m"
- "launchUserAccountUpdaterIfNecessary"

```
