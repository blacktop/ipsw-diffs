## com.apple.AppleSunriseWLAN

> `/System/Library/DriverExtensions/com.apple.AppleSunriseWLAN.dext/com.apple.AppleSunriseWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-340.71.0.0.0
-  __TEXT.__text: 0x397fe8
+342.8.0.0.0
+  __TEXT.__text: 0x398b8c
   __TEXT.__auth_stubs: 0x1410
-  __TEXT.__cstring: 0xe78ca
+  __TEXT.__cstring: 0xe7bea
   __TEXT.__const: 0xd380
-  __TEXT.__unwind_info: 0x6b10
+  __TEXT.__unwind_info: 0x6b20
   __TEXT.__oslogstring: 0x18f
-  __DATA_CONST.__const: 0xe740
+  __DATA_CONST.__const: 0xe7d8
   __DATA_CONST.__osclassinfo: 0xd8
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0xf0
   __DATA.__data: 0xd7c8
-  __DATA.__common: 0x1f6420
+  __DATA.__common: 0x1f6428
   __DATA.__bss: 0xf000
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/IO80211DriverKit
   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 8054
-  Symbols:   10154
-  CStrings:  20357
+  Functions: 8057
+  Symbols:   10160
+  CStrings:  20371
 
Symbols:
+ __ZN23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ __ZN29AppleSunriseWLANAWDLInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZThn112_N29AppleSunriseWLANAWDLInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZThn128_N29AppleSunriseWLANAWDLInterface18setAGGRESSIVE_EDCAEP26apple80211_aggressive_edca
+ __ZThn80_N23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ _g_ucSkdaAttrTag
+ nicTxDirectStartXmit.count7439
+ nicTxDirectStartXmit.time7439
- nicTxDirectStartXmit.count7436
- nicTxDirectStartXmit.time7436
CStrings:
+ "\"AppleSunriseWLAN_driverkit-342.8\""
+ "%llu-%u-[%d]%s:(NAN ERROR) prNANSpecInfo[%u] is NULL\n"
+ "%llu-%u-[%d]%s:(NAN ERROR) prnanBssInfo is NULL\n"
+ "%llu-%u-[%d]%s:(NAN ERROR) prnanBssInfo[%u] is NULL\n"
+ "%llu-%u-[%d]%s:(NAN INFO) skdaAttrTag=%hhu\n"
+ "%llu-%u-[%d]%s:(NAN STATE) custom_attribute_length:%u,tag:%hhu\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/sta_info.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/utils/wpabuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7433"
+ "AppleSunrise-user: [NAN][%s]: Error: NAN net device not ready"
+ "AppleSunrise-user: [NAN][%s]: dev: %p"
+ "AppleSunriseWLAN_driverkit-342.8"
+ "MATSU/MATSU_"
+ "MATSU2/MATSU2_"
+ "Oct  3 2026 15:00:53"
+ "matsu"
+ "matsu2"
+ "nanDevUpdateBss"
+ "setAGGRESSIVE_EDCA"
- "\"AppleSunriseWLAN_driverkit-340.71\""
- "%llu-%u-[%d]%s:(NAN STATE) custom_attribute_length:%u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7430"
- "AppleSunriseWLAN_driverkit-340.71"
- "Sep 18 2026 22:11:02"
```
