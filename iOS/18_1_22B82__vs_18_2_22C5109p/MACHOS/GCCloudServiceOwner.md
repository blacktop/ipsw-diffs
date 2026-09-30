## GCCloudServiceOwner

> `/System/Library/Accounts/ServiceOwners/GCCloudServiceOwner.bundle/GCCloudServiceOwner`

```diff

-819.1.22.2.3
-  __TEXT.__text: 0x11d4
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x640
-  __TEXT.__objc_methlist: 0xb0
+819.2.1.0.0
+  __TEXT.__text: 0x152c
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x197
-  __TEXT.__objc_methname: 0x70c
-  __TEXT.__oslogstring: 0x1f5
-  __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methtype: 0x1ff
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0xe0
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0x18b
+  __TEXT.__objc_methname: 0x6cc
+  __TEXT.__oslogstring: 0x235
+  __TEXT.__objc_classname: 0x39
+  __TEXT.__objc_methtype: 0x20e
+  __TEXT.__dlopen_cstrs: 0x5e
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x558
-  __DATA.__objc_selrefs: 0x1e0
+  __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation
-  - /System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI
-  - /System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 24
-  Symbols:   65
-  CStrings:  140
+  Functions: 30
+  Symbols:   72
+  CStrings:  146
 
Symbols:
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_error_impl
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_getClass
+ _objc_retainAutorelease
+ _os_log_GKError
- _OBJC_CLASS_$_GKLocalPlayerAuthenticator
- _OBJC_CLASS_$_NSNumber
- _objc_retain_x9
CStrings:
+ "%!s(MISSING)"
+ "@24@?0@\"ACAccount\"8Q16"
+ "Cannot proceed with sign in since UI is not permitted."
+ "GKLocalPlayerAuthenticator"
+ "Proceeding with sign in since UI is permitted."
+ "Unable to find class %!s(MISSING)"
+ "Unexpectedly found more than one account matching username during sign in. Proceeding with first account."
+ "_gkFilterWithBlock:"
+ "accountMatchingUsername:serviceType:"
+ "accountsForService:"
+ "authenticateWithContext:completion:"
+ "count"
+ "operationUIPermissions"
+ "softlink:r:path:/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore"
+ "v32@0:8@16@?24"
- "Attempted to sign in to Game Center with a different GameCenter account already existing"
- "GameCenter sign in completed with result %!@(MISSING), error: %!@(MISSING)"
- "authenticationDidCompleteWithError:"
- "authenticationPersonality"
- "authenticationShowGreenBuddyUIForLocalPlayer:withCompletionHandler:"
- "authenticationShowSignInUIForLocalPlayer:origin:dismiss:"
- "com.apple.appleaccount"
- "numberWithInteger:"
- "v40@?0q8@\"GKLocalPlayer\"16@\"NSError\"24@\"GKAuthenticateResponse\"32"

```
