## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1526.83.0.0.0
-  __TEXT.__text: 0x2b6f2c
+  __TEXT.__text: 0x2b6efc
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80262
   __TEXT.__const: 0x7ee40
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e80
+  __TEXT.__unwind_info: 0x5e78
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: EFC25011-8C81-3CBD-8B52-EC6D3D29A0D8
+  UUID: 5EF6D90A-6EEA-35D0-9743-85541B1F6DE8
   Functions: 13165
   Symbols:   16389
   CStrings:  12899
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 100 -> 104
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 100 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B6_NugBy6q6w6JYr5eIJtFlgsbk67Pm-Ar6TmsA/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Aug  6 2025 21:38:10"
- "/AppleInternal/Library/BuildRoots/4~B6_cugC--LGoPyyYDTEqIYEBz3shWCwRpcctSzA/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Aug  6 2025 22:49:20"

```
