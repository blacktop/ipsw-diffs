## AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

-864.60.3.0.0
-  __TEXT.__text: 0x14cb8
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x540
-  __TEXT.__objc_methlist: 0x134
-  __TEXT.__objc_methname: 0x42a
+864.100.42.0.0
+  __TEXT.__text: 0x148d8
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_methlist: 0x14c
+  __TEXT.__objc_methname: 0x447
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0x92
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x25f0
-  __TEXT.__oslogstring: 0x6fa
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__cstring: 0x2888
+  __TEXT.__oslogstring: 0x7cf
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x170
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x3
-  __DATA.__bss: 0x50
+  __DATA.__data: 0x12
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF63FA87-509D-3B07-8112-2F86572C3C0E
-  Functions: 426
-  Symbols:   103
-  CStrings:  401
+  UUID: 6874B8B0-7C9F-3EB9-B54E-204C1529A2E4
+  Functions: 502
+  Symbols:   102
+  CStrings:  421
 
Symbols:
+ _dlopen
+ _dlsym
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x8
CStrings:
+ "%s: %s: Buddy entered (buddyIsRunning=%s consoleUser=%s/%u).\n"
+ "%s: %s: Buddy exited (buddyIsRunning=%s consoleUser=%s/%u).\n"
+ "%s: %s: XPC Event: %@ (distnoted).\n"
+ "%s: %s: acmd started, handing control over to kext (consoleUser=%s/%u allowedByManagedConfiguration=%s/%u/%u disabledByAppleSetup=%s isInternalBuild=%s isUSBTypeCSupported=%s switchToAlwaysAllow=%s buddyIsRunning=%s).\n"
+ "%s: %s: called, eventName=%s consoleUser=%s/%u.\n"
+ "-[TransportRestrictedModeService onBuddyEntered]"
+ "-[TransportRestrictedModeService onBuddyExited]"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "ACMContextCredentialGetPropertyEx"
+ "BYSetupAssistantNeedsToRun"
+ "BuddyEntered"
+ "BuddyExited"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "MiniBuddyEntered"
+ "com.apple.distnoted.matching"
+ "n/a"
+ "onBuddyEntered"
+ "onBuddyExited"
+ "processing distnoted.matching"
- "%s: %s: acmd started, handing control over to kext (allowedByManagedConfiguration=%s/%u/%u disabledByAppleSetup=%s isInternalBuild=%s isUSBTypeCSupported=%s switchToAlwaysAllow=%s).\n"
- "%s: %s: called, eventName=%s.\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "ACMContextCredentialGetProperty"

```
