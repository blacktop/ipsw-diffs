## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1555.1.0.0.0
-  __TEXT.__text: 0x284370
+  __TEXT.__text: 0x284340
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80ba8
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
-  UUID: B1300391-C88E-3E09-9362-0EDF1B61BD08
+  UUID: 0B8D7CC3-DCF2-3A07-8E7B-BD0268A5D1E1
   Functions: 13966
   Symbols:   17217
   CStrings:  12934
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 80 -> 84
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 80 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 84
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNpdugDAy8mjzK7XvqrPe1lx3lO71Tu783XRdrM/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Apr 18 2026 16:13:04"
- "/AppleInternal/Library/BuildRoots/4~CNmaugASrue6i7_XqIqAiKK277dr-jTlhUShCfE/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Apr 18 2026 00:34:33"

```
