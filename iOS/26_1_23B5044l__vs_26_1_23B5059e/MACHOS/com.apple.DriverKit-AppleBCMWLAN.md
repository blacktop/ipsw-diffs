## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1535.5.0.0.0
-  __TEXT.__text: 0x2b73d0
+1535.9.0.0.0
+  __TEXT.__text: 0x2b77b8
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x8031f
-  __TEXT.__const: 0x7ee40
+  __TEXT.__cstring: 0x8035f
+  __TEXT.__const: 0x7ee50
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e98
+  __TEXT.__unwind_info: 0x5ea0
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 3A339EE5-9068-34CA-8A28-1766C48023A5
-  Functions: 13167
-  Symbols:   16392
-  CStrings:  12903
+  UUID: B9BFF1F7-828D-36B3-9B51-5EDABA19FF01
+  Functions: 13170
+  Symbols:   16395
+  CStrings:  12905
 
Symbols:
+ _ZN24AppleBCMWLANNANInterface19setNAN_PAIRING_KEYSEP30apple80211_nan_encryption_keys.cold.4
+ _ZN24AppleBCMWLANNANInterface19setNAN_PAIRING_KEYSEP30apple80211_nan_encryption_keys.cold.5
+ _ZN24AppleBCMWLANNANInterface19setNAN_PAIRING_KEYSEP30apple80211_nan_encryption_keys.cold.6
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1535.9\""
+ "/AppleInternal/Library/BuildRoots/4~B-8KugCQ-oSuhq_E770F0TL8quyL7wDlVrfwKVY/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1535.9"
+ "Sep 29 2025 20:43:28"
+ "[dk] %s@%d:%s adding key\n"
+ "[dk] %s@%d:%s deleting pairing keys\n"
+ "[dk] %s@%d:ERROR: Unable to set NAN Custom Attribute, ret = %d\n"
- "\"AppleBCMWLANV3_driverkit-1535.5\""
- "/AppleInternal/Library/BuildRoots/4~B9nwugBULgfjvgbKioRFtBGCu9lWEjGfK4x07x8/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1535.5"
- "Sep 11 2025 20:35:19"
- "[dk] %s@%d:ERROR: Unable to set NAN Custom Attribut, ret = %d\n"

```
