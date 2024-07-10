## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1253.58.0.0.0
-  __TEXT.__text: 0x2763b0
+1253.56.0.0.0
+  __TEXT.__text: 0x2756f4
   __TEXT.__auth_stubs: 0x2480
   __TEXT.__init_offsets: 0x1b0
-  __TEXT.__cstring: 0x7b986
+  __TEXT.__cstring: 0x7b6fe
   __TEXT.__const: 0x3be40
-  __TEXT.__unwind_info: 0x3780
+  __TEXT.__unwind_info: 0x3770
   __TEXT.__oslogstring: 0x1eac
   __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1f178
+  __DATA_CONST.__const: 0x1f0e8
   __DATA_CONST.__osclassinfo: 0x370
   __DATA.__data: 0x588
   __DATA.__bss: 0x948

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 6804
-  Symbols:   9484
-  CStrings:  12338
+  Functions: 6794
+  Symbols:   9472
+  CStrings:  12324
 
Symbols:
+ __ZN25AppleBCMWLANConfigManager11isNewDeviceEv
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2213
+ __block_descriptor_tmp.1617
+ __block_descriptor_tmp.1917
+ __block_descriptor_tmp.2211
+ __block_descriptor_tmp.2215
+ __block_descriptor_tmp.2233
+ __block_descriptor_tmp.2266
+ __block_descriptor_tmp.2598
+ __block_descriptor_tmp.2635
+ __block_descriptor_tmp.3115
+ __block_descriptor_tmp.3188
+ __block_descriptor_tmp.3200
+ __block_descriptor_tmp.3202
+ __block_descriptor_tmp.3205
+ __block_descriptor_tmp.3249
+ __block_descriptor_tmp.659
+ __block_descriptor_tmp.796
+ __block_descriptor_tmp.937
+ __block_literal_global.2235
+ __block_literal_global.2268
- __ZN16AppleBCMWLANCore19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZN16AppleBCMWLANCore21disableHtSisoOnlySafeEv
- __ZN16AppleBCMWLANCore26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZN25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZN25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZNK16IO80211BSSBeacon12getTimestampEv
- __ZThn112_N25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn112_N25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZThn128_N25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn128_N25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZThn40_NK16IO80211BSSBeacon12getTimestampEv
- __ZThn64_N16AppleBCMWLANCore19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn64_N16AppleBCMWLANCore26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2220
- __block_descriptor_tmp.1624
- __block_descriptor_tmp.1924
- __block_descriptor_tmp.2218
- __block_descriptor_tmp.2222
- __block_descriptor_tmp.2240
- __block_descriptor_tmp.2273
- __block_descriptor_tmp.2607
- __block_descriptor_tmp.2644
- __block_descriptor_tmp.3124
- __block_descriptor_tmp.3197
- __block_descriptor_tmp.3209
- __block_descriptor_tmp.3214
- __block_descriptor_tmp.3220
- __block_descriptor_tmp.3258
- __block_descriptor_tmp.666
- __block_descriptor_tmp.803
- __block_descriptor_tmp.944
- __block_literal_global.2242
- __block_literal_global.2275
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1253.56\""
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
+ "AppleBCMWLANV3_driverkit-1253.56"
+ "Jun 15 2024 00:21:03"
+ "[dk] %!s(MISSING)@%!d(MISSING): fw query for chanspecs SUCCEEDED during init : %!s(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): fw query for chanspecs failed after watchdog complete\n "
+ "wlan.debug.isNewDevice"
- "\"AppleBCMWLANV3_driverkit-1253.58\""
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
- "AppleBCMWLANV3_driverkit-1253.58"
- "Jul  2 2024 21:40:41"
- "[dk] %!s(MISSING)@%!d(MISSING): WiFiCC : fw query for chanspecs SUCCEEDED during init : %!s(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Not a german device but Siso enable, lets disable it cc<%!c(MISSING) %!c(MISSING)> siso=<%!d(MISSING)> isAssociated=<%!d(MISSING)>\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Old device=<%!d(MISSING)>  date<%!d(MISSING)/%!d(MISSING)/%!d(MISSING)> limit<%!d(MISSING)/%!d(MISSING)/%!d(MISSING)> siso=<%!d(MISSING)> isAssociated=<%!d(MISSING)>\n"
- "[dk] %!s(MISSING)@%!d(MISSING):WiFiCC : Current host country code [%!s(MISSING)] setup to FW is complete.\n"
- "[dk] %!s(MISSING)@%!d(MISSING):WiFiCC : Initializing FW with country code [%!s(MISSING)]. Probably a chip reset recovery\n"
- "[dk] %!s(MISSING)@%!d(MISSING):WiFiCC : host country code not present. Defaulting fHostCountryEnabled to false\n"
- "[dk] %!s(MISSING)@%!d(MISSING):WiFiCC : setup default countrycode to FW complete. rv : [%!s(MISSING)] \n"
- "[dk] %!s(MISSING)@%!d(MISSING):disable HT Siso \n"
- "[dk] %!s(MISSING)@%!d(MISSING):isAllowHtSiso false \n"
- "bluetooth-pcie"
- "disableHtSisoOnlySafe"
- "setFIRST_BOOT_COUNTRY_CODE"
- "setMANUFACTURE_DATE"
- "wlan.isAllowHtSiso"
- "wlan.mf.day"
- "wlan.mf.month"
- "wlan.mf.year"

```
