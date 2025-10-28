## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1535.9.4.1.0
-  __TEXT.__text: 0x2b78c4
+  __TEXT.__text: 0x2b7894
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x8053b
   __TEXT.__const: 0x7ee90
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e98
+  __TEXT.__unwind_info: 0x5e90
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 52236D4B-455F-35C8-AE13-6EB6AD83E25E
+  UUID: 33D124AE-82A9-3FF7-AC07-CFB67E5AD5D6
   Functions: 13169
   Symbols:   16394
   CStrings:  12910
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 100 -> 104
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 100 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CAoHugCNRLZ38M6QC0gAwfKfDtdxLLiLxRq_W0E/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Oct 22 2025 21:27:26"
- "/AppleInternal/Library/BuildRoots/4~CAMWugDtCRi38K5WhWC0LsOen0kU0TbTjKiNvpo/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Oct 16 2025 23:20:53"

```
