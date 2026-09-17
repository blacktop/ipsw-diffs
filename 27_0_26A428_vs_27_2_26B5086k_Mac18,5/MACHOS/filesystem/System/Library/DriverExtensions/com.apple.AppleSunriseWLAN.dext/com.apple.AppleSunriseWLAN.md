## com.apple.AppleSunriseWLAN

> `/System/Library/DriverExtensions/com.apple.AppleSunriseWLAN.dext/com.apple.AppleSunriseWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-340.71.0.0.0
-  __TEXT.__text: 0x397fe8
+342.6.0.0.0
+  __TEXT.__text: 0x398880
   __TEXT.__auth_stubs: 0x1410
-  __TEXT.__cstring: 0xe78ca
+  __TEXT.__cstring: 0xe7b4a
   __TEXT.__const: 0xd380
   __TEXT.__unwind_info: 0x6b10
   __TEXT.__oslogstring: 0x18f
-  __DATA_CONST.__const: 0xe740
+  __DATA_CONST.__const: 0xe7a0
   __DATA_CONST.__osclassinfo: 0xd8
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0xf0
   __DATA.__data: 0xd7c8
-  __DATA.__common: 0x1f6420
+  __DATA.__common: 0x1f6428
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 8054
-  Symbols:   10154
-  CStrings:  20357
+  Symbols:   10157
+  CStrings:  20364
 
Symbols:
+ __ZN23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ __ZThn80_N23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ _g_ucSkdaAttrTag
+ nicTxDirectStartXmit.count7439
+ nicTxDirectStartXmit.time7439
- nicTxDirectStartXmit.count7436
- nicTxDirectStartXmit.time7436
Functions:
~ __ZN30AppleSunriseWLANInfraInterface16dequeueTxPacketsEP24IOUserNetworkPacketQueuePP19IOUserNetworkPacketjPv : 1324 -> 1348
~ _ap_sa_query_timer : 512 -> 596
~ _nl80211_get_hw_feature_data : 2372 -> 2368
~ _cnmInitDbdcSetting : 704 -> 724
~ _nanDevUpdateBss : 144 -> 400
~ _nanDevSetNmiAddress : 1104 -> 1304
~ _nanDevMasterIndEvtHandler : 316 -> 424
~ __ZN22AppleSunriseWLANSoftAP16dequeueTxPacketsEP24IOUserNetworkPacketQueuePP19IOUserNetworkPacketjPv : 744 -> 764
~ __ZN16AppleSunriseWLAN20getCARD_CAPABILITIESEP23IO80211SkywalkInterfaceP26apple80211_capability_data : 812 -> 836
~ _gl_io80211_get_rssi : 980 -> 1112
~ _gl_io80211_get_mcs_vht : 1404 -> 1528
~ _gl_io80211_get_rate : 816 -> 940
~ _gl_io80211_get_mcs : 1040 -> 1164
~ _gl_io80211_get_wf_trx_info : 1296 -> 1424
~ _gl_io80211_get_aggregate_stats : 1028 -> 1160
~ _gl_io80211_get_all_sta_stats : 1160 -> 1288
~ _nanSchedGetPeerOobAvailableBitmap : 1424 -> 1432
~ _netif_skywalk_dequeue_tx : 348 -> 408
~ _nicTxDirectStartXmit : 832 -> 876
~ __Z22kalIndicateFilsBssInfoP9GLUE_INFOPhjh9ENUM_BANDi : 964 -> 976
~ _kalIndicateBssInfo : 1668 -> 1680
~ _wpabuf_resize : 380 -> 572
~ _nanDiscCmdUpdateCustomAttrCache : 1112 -> 1260
~ _nanTransmitRequest : 1068 -> 1144
~ _nicCfgChipCapNAN : 252 -> 272
~ __ZN37AppleSunriseWLANNANInterfaceMetaClass3NewEP8OSObject : 268 -> 272
CStrings:
+ "\"AppleSunriseWLAN_driverkit-342.6\""
+ "%llu-%u-[%d]%s:(NAN ERROR) prNANSpecInfo[%u] is NULL\n"
+ "%llu-%u-[%d]%s:(NAN ERROR) prnanBssInfo is NULL\n"
+ "%llu-%u-[%d]%s:(NAN ERROR) prnanBssInfo[%u] is NULL\n"
+ "%llu-%u-[%d]%s:(NAN INFO) skdaAttrTag=%hhu\n"
+ "%llu-%u-[%d]%s:(NAN STATE) custom_attribute_length:%u,tag:%hhu\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/sta_info.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/utils/wpabuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7433"
+ "AppleSunriseWLAN_driverkit-342.6"
+ "nanDevUpdateBss"
- "\"AppleSunriseWLAN_driverkit-340.71\""
- "%llu-%u-[%d]%s:(NAN STATE) custom_attribute_length:%u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7430"
- "AppleSunriseWLAN_driverkit-340.71"
```
