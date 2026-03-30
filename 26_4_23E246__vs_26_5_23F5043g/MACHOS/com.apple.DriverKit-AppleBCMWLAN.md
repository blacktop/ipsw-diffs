## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1550.21.0.0.0
-  __TEXT.__text: 0x284340
+1555.1.0.0.0
+  __TEXT.__text: 0x284370
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x80baa
+  __TEXT.__cstring: 0x80ba8
   __TEXT.__const: 0x7eb38
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e58
+  __TEXT.__unwind_info: 0x5e60
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 5530CCA2-41BC-32FA-9B4C-8264F38714B5
+  UUID: 4994E48D-EB1C-3E5E-9D54-CB00FDAF6450
   Functions: 13966
   Symbols:   17217
   CStrings:  12934
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 4 -> 60
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 84 -> 80
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 80
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 84 -> 96
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1555.1\""
+ "/AppleInternal/Library/BuildRoots/4~CLizugCGFoUmgWWL5styc6lQ0Jptj2SKV4yWF0Y/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1555.1"
+ "Mar 20 2026 22:46:50"
- "\"AppleBCMWLANV3_driverkit-1550.21\""
- "/AppleInternal/Library/BuildRoots/4~CKgmugDxYeJ4isiYZqomhookWS0Ud8eKo-5rOYc/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1550.21"
- "Mar  6 2026 18:45:41"

```
