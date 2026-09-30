## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1535.9.0.0.0
-  __TEXT.__text: 0x2b776c
+  __TEXT.__text: 0x2b773c
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x8035f
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
-  UUID: 97D44201-6BAA-38D9-9FC0-DCFF6FAD536C
+  UUID: A123C100-0765-3004-BABF-E5DD7781DDA0
   Functions: 13171
   Symbols:   16397
   CStrings:  12905
Functions:
~ __ZN27AppleBCMWLANChipManagerPCIe21isSafeToCaptureSoCRAMEv : 60 -> 4
~ __Z41AppleBCMWLAN_isVerboseDebugLoggingAllowedv : 100 -> 104
~ __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv -> __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv : 100 -> 96
~ __Z36AppleBCMWLAN_isDevFusedOrCSRInternalv -> __Z35AppleBCMWLAN_isSoCRAMCaptureAllowedv : 96 -> 104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CCKqugDexe7JGaH8qxhljH2zCEGRc9aD0IoOxSk/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "Nov 12 2025 20:59:53"
- "/AppleInternal/Library/BuildRoots/4~CCK0ugBYcjmjShlatkNqSEKRi3N1UydPT-VzZVI/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Nov 12 2025 21:50:31"

```
