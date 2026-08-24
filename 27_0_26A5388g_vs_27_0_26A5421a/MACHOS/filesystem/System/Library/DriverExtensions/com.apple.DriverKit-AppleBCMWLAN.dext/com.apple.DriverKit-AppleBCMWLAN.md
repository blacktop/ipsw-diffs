## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-1570.62.0.0.0
-  __TEXT.__text: 0x28d6bc
+1570.66.0.0.0
+  __TEXT.__text: 0x28d804
   __TEXT.__auth_stubs: 0x25b0
   __TEXT.__init_offsets: 0x1c0
-  __TEXT.__cstring: 0x8289b
+  __TEXT.__cstring: 0x82985
   __TEXT.__const: 0x3d858
   __TEXT.__unwind_info: 0x6028
   __TEXT.__eh_frame: 0x38
   __TEXT.__oslogstring: 0x1e7a
-  __DATA_CONST.__const: 0x21248
+  __DATA_CONST.__const: 0x21270
   __DATA_CONST.__osclassinfo: 0x390
   __DATA_CONST.__auth_got: 0x12d8
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14167
-  Symbols:   12055
-  CStrings:  13079
+  Functions: 14179
+  Symbols:   12062
+  CStrings:  13082
 
Symbols:
+ _ZNK28AppleBCMWLANBusInterfacePCIe22checkPCIeMMIOReadinessEv
+ __ZN11AppleOLYHAL32reportInitFailureWithChipResetDKEP8OSStringb
+ __ZN17IO80211Controller34reportsPerInterfacePeerCacheLimitsEv
+ __ZN24AppleBCMWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZNK28AppleBCMWLANBusInterfacePCIe22checkPCIeMMIOReadinessEv
+ __ZThn112_N24AppleBCMWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZThn128_N24AppleBCMWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZThn48_N17IO80211Controller34reportsPerInterfacePeerCacheLimitsEv
- __ZN11AppleOLYHAL19reportInitFailureDKEP8OSString
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1570.66\""
+ "AppleBCMWLANV3_driverkit-1570.66"
+ "Aug  9 2026 22:30:03"
+ "[dk] %s@%d:APB CB not accessible before readOTP\n"
+ "[dk] %s@%d:Dext PCIe config not ready for MMIO.\n"
+ "[dk] %s@%d:Failed to read or parse OTP data. Failing start\n"
+ "[dk] %s@%d:PCI config not MMIO-ready before readOTP (cmd=0x%04x bar0=0x%08x)\n"
+ "[dk] %s@%d:Pre-OTP PCI cfg cmd=0x%04x bar0=0x%08x\n"
+ "[dk] %s@%d:Pre-OTP read checks failed! Failing start\n"
+ "[dk] %s@%d:PreOTP PCI config read failed"
+ "[dk] %s@%d:dext APB gate ENTER (checking APB before readOTP)\n"
+ "checkPCIeMMIOReadiness"
- "\"AppleBCMWLANV3_driverkit-1570.62\""
- "AppleBCMWLANV3_driverkit-1570.62"
- "Jul 10 2026 22:07:08"
- "[dk] %s@%d:APB CB error-log registers before readOTP:\n"
- "[dk] %s@%d:CB0[0x%x] = 0x%08x\n"
- "[dk] %s@%d:CB0[0x%x] read failed: 0x%x\n"
- "[dk] %s@%d:CB1[0x%x] = 0x%08x\n"
- "[dk] %s@%d:CB1[0x%x] read failed: 0x%x\n"
- "[dk] %s@%d:Failed to read OTP data\n"
```
