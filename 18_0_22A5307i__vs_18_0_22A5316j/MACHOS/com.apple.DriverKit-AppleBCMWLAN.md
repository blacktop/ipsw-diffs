## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1256.88.0.0.0
-  __TEXT.__text: 0x279f90
+1256.92.0.0.0
+  __TEXT.__text: 0x27a398
   __TEXT.__auth_stubs: 0x24a0
   __TEXT.__init_offsets: 0x1ac
-  __TEXT.__cstring: 0x7c047
+  __TEXT.__cstring: 0x7c261
   __TEXT.__const: 0x69a70
   __TEXT.__oslogstring: 0x1f59
   __TEXT.__unwind_info: 0x3770
   __DATA_CONST.__auth_got: 0x1250
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1f030
+  __DATA_CONST.__const: 0x1f040
   __DATA_CONST.__osclassinfo: 0x368
   __DATA.__data: 0x590
   __DATA.__bss: 0x940

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 6804
-  Symbols:   9479
-  CStrings:  12482
+  Symbols:   9481
+  CStrings:  12491
 
Symbols:
+ __ZNK16IO80211BSSBeacon12getTimestampEv
+ __ZNK28AppleBCMWLANBusInterfacePCIe15isAPBAccessibleEbb
+ __ZNK28AppleBCMWLANBusInterfacePCIe20setDeviceInDeepSleepEb
+ __ZThn40_NK16IO80211BSSBeacon12getTimestampEv
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1081
+ __block_descriptor_tmp.1077
+ __block_descriptor_tmp.1084
+ __block_descriptor_tmp.1087
+ __block_descriptor_tmp.3225
+ __block_descriptor_tmp.3241
+ __block_descriptor_tmp.3243
+ __block_descriptor_tmp.3246
+ __block_descriptor_tmp.3252
+ __block_descriptor_tmp.3290
- __ZN28AppleBCMWLANBusInterfacePCIe15isAPBAccessibleEbb
- __ZN28AppleBCMWLANBusInterfacePCIe20setDeviceInDeepSleepEb
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1080
- __block_descriptor_tmp.1076
- __block_descriptor_tmp.1083
- __block_descriptor_tmp.1085
- __block_descriptor_tmp.3219
- __block_descriptor_tmp.3233
- __block_descriptor_tmp.3235
- __block_descriptor_tmp.3238
- __block_descriptor_tmp.3244
- __block_descriptor_tmp.3282
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1256.92\""
+ "/AppleInternal/Library/BuildRoots/2bd63ead-4181-11ef-b2b1-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANCore::Start_Impl: Invalid provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
+ "AppleBCMWLANCore::Start_Impl: Unable to create debug logger\n"
+ "AppleBCMWLANCore::Start_Impl: begin: this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
+ "AppleBCMWLANCore::Start_Impl: done: failed: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
+ "AppleBCMWLANV3_driverkit-1256.92"
+ "Jul 13 2024 19:50:28"
+ "[dk] %!s(MISSING)@%!d(MISSING): APB is not accessible; skip peripheral access\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Started provider[%!p(MISSING)]\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):done: succcess: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):invalid dispatch queue\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):wlan core start failed\n"
- "\"AppleBCMWLANV3_driverkit-1256.88\""
- "/AppleInternal/Library/BuildRoots/2ad44f09-34cf-11ef-a603-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1256.88"
- "Jun 28 2024 22:30:36"

```
