## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1260.8.0.0.0
-  __TEXT.__text: 0x280ef0
+1260.10.0.0.0
+  __TEXT.__text: 0x280bd8
   __TEXT.__auth_stubs: 0x2480
   __TEXT.__init_offsets: 0x1b8
-  __TEXT.__cstring: 0x7d882
+  __TEXT.__cstring: 0x7d5ca
   __TEXT.__const: 0x7cff0
   __TEXT.__oslogstring: 0x1e6a
-  __TEXT.__unwind_info: 0x37e0
+  __TEXT.__unwind_info: 0x37d8
   __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1f7b8
+  __DATA_CONST.__const: 0x1f9d8
   __DATA_CONST.__osclassinfo: 0x378
   __DATA.__data: 0x590
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 6885
-  Symbols:   9583
-  CStrings:  12629
+  Symbols:   9584
+  CStrings:  12620
 
Symbols:
+ __ZZNK28AppleBCMWLANBusInterfacePCIe17dumpPMNIRegistersEvE10dmpMNIRegs
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1156
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.689
+ __block_descriptor_tmp.1152
+ __block_descriptor_tmp.1159
+ __block_descriptor_tmp.1161
+ __block_descriptor_tmp.1162
+ __block_descriptor_tmp.210
+ __block_descriptor_tmp.261
+ __block_descriptor_tmp.335
+ __block_descriptor_tmp.389
+ __block_descriptor_tmp.534
+ __block_descriptor_tmp.577
+ __block_descriptor_tmp.584
+ __block_descriptor_tmp.687
+ __block_descriptor_tmp.692
+ __block_descriptor_tmp.706
+ __block_descriptor_tmp.711
+ __block_descriptor_tmp.718
+ __block_descriptor_tmp.721
+ __block_descriptor_tmp.722
+ __block_descriptor_tmp.732
+ __block_descriptor_tmp.840
+ __block_descriptor_tmp.841
+ __block_descriptor_tmp.850
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1131
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.687
- __block_descriptor_tmp.1127
- __block_descriptor_tmp.1134
- __block_descriptor_tmp.1136
- __block_descriptor_tmp.1137
- __block_descriptor_tmp.208
- __block_descriptor_tmp.259
- __block_descriptor_tmp.333
- __block_descriptor_tmp.385
- __block_descriptor_tmp.532
- __block_descriptor_tmp.575
- __block_descriptor_tmp.582
- __block_descriptor_tmp.685
- __block_descriptor_tmp.690
- __block_descriptor_tmp.704
- __block_descriptor_tmp.709
- __block_descriptor_tmp.716
- __block_descriptor_tmp.719
- __block_descriptor_tmp.720
- __block_descriptor_tmp.728
- __block_descriptor_tmp.838
- __block_descriptor_tmp.839
- __block_descriptor_tmp.848
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1260.10\""
+ "/AppleInternal/Library/BuildRoots/f67a58a9-8709-11ef-bfc4-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1260.10"
+ "Oct 10 2024 22:20:43"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper offset : 0x%!x(MISSING) data : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper offset : 0x%!x(MISSING) data : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper offset : 0x%!x(MISSING) data : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Enable log collection of WLAN APB registers : %!u(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper offset : 0x%!x(MISSING) ret : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper offset : 0x%!x(MISSING) ret : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapperoffset : 0x%!x(MISSING) ret : 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Start dumping WLAN APB registers\n"
+ "wlan.pcie.logCollectWLAPB"
- "\"AppleBCMWLANV3_driverkit-1260.8\""
- "/AppleInternal/Library/BuildRoots/79c11500-77ed-11ef-b745-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1260.8"
- "Sep 22 2024 22:19:45"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper SILDBG: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper SILDBG: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper SILDBG: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"

```
