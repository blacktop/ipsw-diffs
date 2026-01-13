## com.apple.AppleSunriseWLAN

> `/System/Library/DriverExtensions/com.apple.AppleSunriseWLAN.dext/com.apple.AppleSunriseWLAN`

```diff

-290.10.0.0.0
-  __TEXT.__text: 0x388bb8
+290.12.0.0.0
+  __TEXT.__text: 0x389578
   __TEXT.__auth_stubs: 0x13e0
-  __TEXT.__cstring: 0xe0f4d
-  __TEXT.__const: 0xcef0
-  __TEXT.__unwind_info: 0x4b88
+  __TEXT.__cstring: 0xe1100
+  __TEXT.__const: 0xc030
+  __TEXT.__unwind_info: 0x4b90
   __TEXT.__oslogstring: 0x18f
   __DATA_CONST.__auth_got: 0x9f0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0xe190
   __DATA_CONST.__osclassinfo: 0xd8
-  __DATA.__data: 0xd570
+  __DATA.__data: 0xd588
   __DATA.__common: 0x1f5810
-  __DATA.__bss: 0xe710
+  __DATA.__bss: 0xe7b0
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/IO80211DriverKit
   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: A66107A8-C712-38ED-AB98-4C01C5A0602E
-  Functions: 7881
-  Symbols:   10309
-  CStrings:  19978
+  UUID: 77F20D01-A285-3434-AFC0-3213DE86E1CD
+  Functions: 7883
+  Symbols:   10312
+  CStrings:  19988
 
Symbols:
+ __ZZ21kalArpFrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3531
+ __ZZ21kalArpFrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3531
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3372
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3379
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3400
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3372
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3379
+ __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3400
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3467
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3474
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3495
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3467
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3474
+ __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3495
+ _priv_driver_set_6g_force_roam_offset
+ _wlanStatsWlanInfoBackupRestore
+ wlanPktTxDone.count16209
+ wlanPktTxDone.count16241
+ wlanPktTxDone.count16250
+ wlanPktTxDone.count16257
+ wlanPktTxDone.time16209
+ wlanPktTxDone.time16241
+ wlanPktTxDone.time16250
+ wlanPktTxDone.time16257
+ wlanStatsWlanInfoBackupRestore.arWlanInfoBackup
- __ZZ21kalArpFrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3532
- __ZZ21kalArpFrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3532
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3373
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3380
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3401
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3373
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3380
- __ZZ22kalIPv4FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3401
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3468
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3475
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE8time3496
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3468
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3475
- __ZZ22kalIPv6FrameClassifierP9GLUE_INFOPvPhP14TX_PACKET_INFOE9count3496
- wlanPktTxDone.count16205
- wlanPktTxDone.count16237
- wlanPktTxDone.count16246
- wlanPktTxDone.count16253
- wlanPktTxDone.time16205
- wlanPktTxDone.time16237
- wlanPktTxDone.time16246
- wlanPktTxDone.time16253
Functions:
~ _p2pFuncValidateAuth : 1240 -> 1264
~ _gl_io80211_set_roam_profile_config : 904 -> 980
~ _wlanInitFeatureOption : 8388 -> 8436
+ _wlanStatsWlanInfoBackupRestore
~ _gl_io80211_get_stats_chip_counter : 4700 -> 4716
~ _gl_io80211_get_stats_wtd_avg_lqm : 3500 -> 3516
~ _gl_io80211_get_mcs_vht : 1372 -> 1388
~ _gl_io80211_get_mcs : 992 -> 1016
~ _priv_driver_set_chip_config : 884 -> 1184
~ _priv_driver_get_sta_stat : 3188 -> 3204
~ _priv_driver_get_wow_port : 1056 -> 1052
~ _priv_driver_get_sta_info : 1980 -> 1996
~ _priv_driver_get_wtbl_info : 984 -> 996
+ _priv_driver_set_6g_force_roam_offset
~ _kalIndicateStatusAndComplete : 2224 -> 2196
~ _kalIndicateScanSummary : 1976 -> 1984
~ _kalPerMonStop : 884 -> 892
~ _nicEventWPAStatus : 936 -> 1456
~ _nicTimesyncResetDrvInfo : 764 -> 756
~ _SetICapStart : 1156 -> 1160
~ _SaveIQDataTblToBuf : 1208 -> 1212
CStrings:
+ "\"AppleSunriseWLAN_driverkit-290.12\""
+ "%llu-%u-[%d]%s:(INIT ERROR) [STAT_OID] wlanoidQueryWlanInfo timeout, execute restore!!\n"
+ "%llu-%u-[%d]%s:(REQ INFO) %s 6g force roam\n"
+ "%llu-%u-[%d]%s:(REQ INFO) Reset 6g first roam bracket with offset:%d\n"
+ "%llu-%u-[%d]%s:(RSN INFO) Invalid BssInfo index[%u]\n"
+ "%llu-%u-[%d]%s:(RSN INFO) REPORT_EV_WPA3_AUTH_FAIL, isAp:%d\n"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLAN.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANAWDLInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANInfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANLQMData.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANLowLatencyInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANNANDataInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/AppleSunriseKext/AppleSunriseHALClient_user.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/awdl/awdl_data_engine.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/awdl/awdl_dev.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/cmm_asic_connac2x.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/dbg_connac2x.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/fw_dl.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/dbg_mt7922.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2343"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2361"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2391"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2408"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2539"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2628"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2735"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2813"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2911"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2944"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2978"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:3010"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/dbg_mt7961.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/hal_dmashdl_mt7961.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/hal_wfsys_reset_mt7961.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/mt7961.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/debug.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/dump.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c:16412"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c:3167"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_oid.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_p2p.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/csiphash/csiphash_key.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/hostapd/config_file.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/beacon.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/wpa_auth.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/utils/os_internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1-internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1-pbkdf2.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/ais_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/ais_fsm.c:6988"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/assoc.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/auth.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/bss.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/cnm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/cnm_mem.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/gas.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/he_rlm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/hem_mbox.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/hs20.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_assoc.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_dev_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_dev_state.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_func.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_ie.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_role_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_role_state.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/privacy.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rlm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rlm_domain.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/roaming_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rrm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rsn.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/saa_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/scan.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/scan_fsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/stats.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/tkip_mic.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/tm_stof.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nanDiscovery.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nanScheduler.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_data_engine.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_data_engine_util.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_dev.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_ranging.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_sec.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth_glue.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth_ie.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/common/wpa_common.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/aes-unwrap.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/aes-wrap.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1-internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1-prf.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256-internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256-prf.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384-internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384-prf.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha512-internal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/rsn_supp/wpa.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/utils/common.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/wpa_supplicant/wpas_glue.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_cmd_event.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:1699"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:5511"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:5562"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rxd_v2.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:2969"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6235"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6257"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6359"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6388"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6417"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7279"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7356"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_txd_v2.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_umac.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:1006"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:4956"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:5063"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:5899"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:917"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c:310"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c:399"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_device.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_firmware.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_init.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_awdl.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_connect.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_nan.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_roam.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_sap.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_scan.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_stats.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_wow.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:2280"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:3102"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4857"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4883"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4920"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4953"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4985"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5007"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5042"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5072"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5104"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5201"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5220"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5288"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5587"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6400"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6417"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6485"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:707"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:768"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:8453"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:8486"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c:430"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c:533"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_netdev.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c:863"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c:966"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_cfg80211.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_kal.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_kal.c:1180"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_qa_agent.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:634"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:646"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:877"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:916"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:980"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_sched.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_sk_buff.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_vendor_fw_supp.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_wext_priv.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/dbg_pdma.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/dbg_pdma.c:1351"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:1461"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:1591"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4238"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4246"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4347"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4355"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4535"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4676"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:664"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:832"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/kal_pdma.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/kal_pdma.c:1729"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:1055"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:1154"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:756"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/proto/bonjour_offload.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugC6iBmHMWf7o7CvzBPCTjC1co5LE_H542I/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/proto/keep_alive.c"
+ "6gFREnable"
+ "6gFROffset"
+ "AppleSunriseWLAN_driverkit-290.12"
+ "Invalid 6gForceRoam command\n"
+ "Jan  4 2026 19:26:40"
+ "priv_driver_set_6g_force_roam_offset"
+ "wlanStatsWlanInfoBackupRestore"
- "\"AppleSunriseWLAN_driverkit-290.10\""
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLAN.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANAWDLInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANInfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANLQMData.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANLowLatencyInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANNANDataInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/Apple/AppleSunriseWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/AppleSunriseKext/AppleSunriseHALClient_user.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/awdl/awdl_data_engine.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/awdl/awdl_dev.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/cmm_asic_connac2x.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/dbg_connac2x.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/common/fw_dl.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/dbg_mt7922.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2343"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2361"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2391"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2408"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2539"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2628"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2735"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2813"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2911"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2944"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:2978"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7922/mt7922.c:3010"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/dbg_mt7961.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/hal_dmashdl_mt7961.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/hal_wfsys_reset_mt7961.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/chips/mt7961/mt7961.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/debug.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/dump.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c:16408"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_lib.c:3167"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_oid.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/common/wlan_p2p.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/csiphash/csiphash_key.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/hostapd/config_file.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/beacon.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/ap/wpa_auth.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_hostapd/hostapd/src/utils/os_internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1-internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1-pbkdf2.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/drv_sme_sec/sha1.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/ais_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/ais_fsm.c:6988"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/assoc.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/auth.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/bss.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/cnm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/cnm_mem.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/gas.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/he_rlm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/hem_mbox.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/hs20.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_assoc.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_dev_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_dev_state.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_func.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_ie.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_role_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/p2p_role_state.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/privacy.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rlm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rlm_domain.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/roaming_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rrm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/rsn.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/saa_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/scan.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/scan_fsm.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/stats.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/tkip_mic.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/mgmt/tm_stof.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nanDiscovery.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nanScheduler.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_data_engine.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_data_engine_util.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_dev.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_ranging.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/nan_sec.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth_glue.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/ap/wpa_auth_ie.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/common/wpa_common.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/aes-unwrap.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/aes-wrap.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1-internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1-prf.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha1.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256-internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256-prf.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha256.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384-internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384-prf.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha384.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/crypto/sha512-internal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/rsn_supp/wpa.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/src/utils/common.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nan/wpa_supp/wpa_supplicant/wpas_glue.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_cmd_event.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:1699"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:5511"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rx.c:5562"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_rxd_v2.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:2969"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6235"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6257"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6359"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6388"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:6417"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7279"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_tx.c:7356"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_txd_v2.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/nic_umac.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:1006"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:4956"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:5063"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:5899"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/nic/que_mgt.c:917"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c:310"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_awdl.c:399"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_device.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_firmware.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_init.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_awdl.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_connect.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_nan.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_roam.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_sap.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_scan.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_stats.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_io80211_wow.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:2281"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:3103"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4855"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4881"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4918"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4951"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:4983"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5005"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5040"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5070"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5102"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5199"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5218"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5286"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:5585"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6398"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6415"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:6483"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:707"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:768"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:8451"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_kal.cpp:8484"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c:430"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_nan.c:533"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_netdev.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c:863"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p.c:966"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_cfg80211.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_kal.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_p2p_kal.c:1180"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_qa_agent.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:634"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:646"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:877"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:916"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_rst.c:980"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_sched.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_sk_buff.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_vendor_fw_supp.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/gl_wext_priv.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/dbg_pdma.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/dbg_pdma.c:1351"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:1461"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:1591"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4238"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4246"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4347"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4355"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4535"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:4676"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:664"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/hal_pdma.c:832"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/kal_pdma.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/common/kal_pdma.c:1729"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:1055"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:1154"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/os/dale/hif/pcie/pcie.c:756"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/proto/bonjour_offload.c"
- "/AppleInternal/Library/BuildRoots/4~CD26ugBCY54UZhcZmwvXYf9ikBcaBBISf6379VY/Library/Caches/com.apple.xbs/Sources/AppleSunriseWLAN_driverkit/MTK/proto/keep_alive.c"
- "AppleSunriseWLAN_driverkit-290.10"
- "Dec  5 2025 23:15:43"

```
