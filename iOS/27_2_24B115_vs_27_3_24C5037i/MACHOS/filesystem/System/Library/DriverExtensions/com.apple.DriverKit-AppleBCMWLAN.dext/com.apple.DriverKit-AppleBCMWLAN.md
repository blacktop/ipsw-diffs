## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__osclassinfo`
- `__DATA.__data`

```diff

-1582.9.0.0.0
-  __TEXT.__text: 0x28b938
+1585.2.0.0.0
+  __TEXT.__text: 0x28bcc0
   __TEXT.__auth_stubs: 0x25c0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x83612
+  __TEXT.__cstring: 0x8364f
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0xa480
+  __TEXT.__unwind_info: 0xa490
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x211c0
+  __DATA_CONST.__const: 0x212e0
   __DATA_CONST.__osclassinfo: 0x388
   __DATA_CONST.__auth_got: 0x12e0
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14201
-  Symbols:   10284
-  CStrings:  13148
+  Functions: 14221
+  Symbols:   10302
+  CStrings:  13149
 
Symbols:
+ __ZN25AppleBCMWLANInfraProtocol15getSENSING_DATAEP25apple80211_sensing_data_t
+ __ZN25AppleBCMWLANInfraProtocol17getSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZN25AppleBCMWLANInfraProtocol17setSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZN25AppleBCMWLANInfraProtocol17setSENSING_ENABLEEP27apple80211_sensing_enable_t
+ __ZN25AppleBCMWLANInfraProtocol19getSENSING_GET_INFOEP25apple80211_sensing_info_t
+ __ZN25AppleBCMWLANInfraProtocol21getCSI_FIRMWARE_STATSEP31apple80211_firmware_csi_stats_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol15getSENSING_DATAEP25apple80211_sensing_data_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol17getSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol17setSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol17setSENSING_ENABLEEP27apple80211_sensing_enable_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol19getSENSING_GET_INFOEP25apple80211_sensing_info_t
+ __ZThn112_N25AppleBCMWLANInfraProtocol21getCSI_FIRMWARE_STATSEP31apple80211_firmware_csi_stats_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol15getSENSING_DATAEP25apple80211_sensing_data_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol17getSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol17setSENSING_CONFIGEP27apple80211_sensing_config_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol17setSENSING_ENABLEEP27apple80211_sensing_enable_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol19getSENSING_GET_INFOEP25apple80211_sensing_info_t
+ __ZThn128_N25AppleBCMWLANInfraProtocol21getCSI_FIRMWARE_STATSEP31apple80211_firmware_csi_stats_t
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1585.2\""
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS27.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1585.2"
+ "[dk] %s@%d:ERROR: Invalid advertisers count:%u, max count: %u\n"
+ "[dk] %s@%d:ERROR: Invalid servicelist count:%u, max count: %u\n"
- "\"AppleBCMWLANV3_driverkit-1582.9\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS27.2.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1582.9"
- "[dk] %s@%d:ERROR: Invalid servicelist length:%u, max length: %u\n"
```
