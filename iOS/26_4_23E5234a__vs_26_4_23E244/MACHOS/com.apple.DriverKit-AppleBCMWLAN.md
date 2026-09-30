## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1550.21.0.0.0
-  __TEXT.__text: 0x284370
+  __TEXT.__text: 0x284340
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80baa
   __TEXT.__const: 0x7eb38
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e60
+  __TEXT.__unwind_info: 0x5e58
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 1F324F6E-AB71-34E4-A00E-2B3E6A8710B1
+  UUID: 5530CCA2-41BC-32FA-9B4C-8264F38714B5
   Functions: 13966
   Symbols:   17217
   CStrings:  12934
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 80 -> 84
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 80 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 84
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKgmugDxYeJ4isiYZqomhookWS0Ud8eKo-5rOYc/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Mar  6 2026 18:45:41"
- "/AppleInternal/Library/BuildRoots/4~CKX3ugCRYiCYEAbWrvBDGjm9VnOmUSFQl_Hj9hY/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Mar  4 2026 22:04:42"

```
