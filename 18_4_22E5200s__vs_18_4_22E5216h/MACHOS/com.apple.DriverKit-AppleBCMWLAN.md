## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1475.42.0.0.0
-  __TEXT.__text: 0x2af3c8
+1475.46.0.0.0
+  __TEXT.__text: 0x2af618
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e09a
-  __TEXT.__const: 0x7e190
+  __TEXT.__cstring: 0x7e0e6
+  __TEXT.__const: 0x7e1d0
   __TEXT.__oslogstring: 0x1f52
   __TEXT.__unwind_info: 0x5d08
   __TEXT.__eh_frame: 0x38

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 13036
-  Symbols:   16248
-  CStrings:  12659
+  Functions: 13038
+  Symbols:   16250
+  CStrings:  12661
 
Symbols:
+ __ZN16AppleBCMWLANCore23waitForGasAbortIfNeededEv
+ __ZN22AppleBCMWLANGASAdapter19getLastGasAbortTimeEv
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1475.46\""
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1475.46"
+ "Feb 22 2025 03:38:45"
+ "[dk] %s@%d:TIME to wait due to GAS abort is %llu  \n"
+ "waitForGasAbortIfNeeded"
- "\"AppleBCMWLANV3_driverkit-1475.42\""
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1475.42"
- "Feb 16 2025 03:04:30"

```
