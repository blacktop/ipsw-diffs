## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1487.2.0.0.0
-  __TEXT.__text: 0x2b17cc
+  __TEXT.__text: 0x2b179c
   __TEXT.__auth_stubs: 0x2500
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x7e8f2
   __TEXT.__const: 0x7e330
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d78
+  __TEXT.__unwind_info: 0x5d70
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1280
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 207CD41F-9127-3515-BA4C-5DEBB5028BF4
+  UUID: 27768FD0-6460-3FB4-9A18-F3CE03EDC953
   Functions: 13076
   Symbols:   16289
   CStrings:  12704
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 100 -> 104
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 100 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B5YJugATGjo-QH3MSX-nMU_91bjDm2EyQ07gddQ/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.6.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Jul 15 2025 21:55:44"
- "/AppleInternal/Library/BuildRoots/4~B4brugAFxtwTm3hrTnpzeoLON4nkArmGOr4Mk9M/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.6.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Jul  3 2025 00:21:08"

```
