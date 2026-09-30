## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1555.1.0.0.0
-  __TEXT.__text: 0x284340
+  __TEXT.__text: 0x284370
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80ba8
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
-  UUID: 0B8D7CC3-DCF2-3A07-8E7B-BD0268A5D1E1
+  UUID: 66B7BCD1-F6B8-314C-B6D4-7CB48834D047
   Functions: 13966
   Symbols:   17217
   CStrings:  12934
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 4 -> 60
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 84 -> 80
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 80
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 84 -> 96
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CPcXugAEUvIwHm-GRli6Nw4KQLVOV2bs2rIPwpE/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.6.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "May 13 2026 04:32:20"
- "/AppleInternal/Library/BuildRoots/4~CNpdugDAy8mjzK7XvqrPe1lx3lO71Tu783XRdrM/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Apr 18 2026 16:13:04"

```
