## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1538.3.0.0.0
-  __TEXT.__text: 0x2b76e0
+  __TEXT.__text: 0x2b76b0
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80490
   __TEXT.__const: 0x7ea10
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5ea0
+  __TEXT.__unwind_info: 0x5e98
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: A2461071-C9AA-3551-884A-1B712016DF63
+  UUID: 13EF20EB-88AC-3F71-8FE9-1ED8ACEB91B7
   Functions: 13173
   Symbols:   16400
   CStrings:  12911
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 100 -> 104
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 100 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHu8ugDxknxO4z4PBm7F-Kd7Uivh3TzeyCz-CCk/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Jan 27 2026 21:13:30"
- "/AppleInternal/Library/BuildRoots/4~CHO4ugBWeaSHKlNNpZWIWW3UpiVbpp0GPWqRUGI/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Jan 21 2026 01:04:33"

```
