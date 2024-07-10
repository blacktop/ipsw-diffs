## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi`

```diff

-802.57.0.0.0
-  __TEXT.__text: 0x21c320
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x9de8
+802.55.0.0.0
+  __TEXT.__text: 0x2189b0
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x9db8
   __TEXT.__const: 0x140
-  __TEXT.__oslogstring: 0xbb7e
-  __TEXT.__cstring: 0x10283
-  __TEXT.__gcc_except_tab: 0x9f94
-  __TEXT.__dlopen_cstrs: 0x3db
+  __TEXT.__oslogstring: 0xb7f0
+  __TEXT.__cstring: 0x101de
+  __TEXT.__gcc_except_tab: 0x9efc
+  __TEXT.__dlopen_cstrs: 0x435
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1fb0
+  __TEXT.__unwind_info: 0x1f88
   __TEXT.__objc_classname: 0x87f
-  __TEXT.__objc_methname: 0x162ed
+  __TEXT.__objc_methname: 0x16261
   __TEXT.__objc_methtype: 0x27ee
-  __TEXT.__objc_stubs: 0x11340
-  __DATA_CONST.__got: 0x5d8
-  __DATA_CONST.__const: 0xa18
+  __TEXT.__objc_stubs: 0x11280
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x248
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51d8
+  __DATA_CONST.__objc_selrefs: 0x51b0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0xe58
-  __AUTH_CONST.__auth_got: 0x728
+  __DATA_CONST.__objc_arraydata: 0xe68
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x35a0
-  __AUTH_CONST.__cfstring: 0x11000
-  __AUTH_CONST.__objc_const: 0xfc10
-  __AUTH_CONST.__objc_intobj: 0x3018
+  __AUTH_CONST.__const: 0x3530
+  __AUTH_CONST.__cfstring: 0x10fc0
+  __AUTH_CONST.__objc_const: 0xfbf0
+  __AUTH_CONST.__objc_intobj: 0x3030
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x16d0
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0x928
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4741
-  Symbols:   9688
-  CStrings:  2706
+  Functions: 4740
+  Symbols:   9681
+  CStrings:  2698
 
Symbols:
+ -[CWFInterface primaryRank]
+ -[CWFJoinStatus allowedToBecomePrimaryAt]
+ -[CWFJoinStatus durationUntilAllowedToBecomePrimary]
+ -[CWFJoinStatus setAllowedToBecomePrimaryAt:]
+ -[CWFLocalDeviceDiscovery _serviceRecordFromRecordName:]
+ -[CWFSCNetworkService primaryRank]
+ -[CWFXPCConnection queryPrimaryRankWithRequestParams:reply:]
+ -[CWFXPCRequestProxy __getPrimaryRank:]
+ -[CWFXPCRequestProxy __updateJoinStatusWithPrimaryRank:]
+ GCC_except_table103
+ GCC_except_table116
+ GCC_except_table133
+ GCC_except_table160
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table180
+ GCC_except_table192
+ GCC_except_table292
+ GCC_except_table359
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table489
+ GCC_except_table577
+ GCC_except_table589
+ GCC_except_table601
+ GCC_except_table613
+ GCC_except_table634
+ GCC_except_table652
+ GCC_except_table67
+ GCC_except_table83
+ GCC_except_table89
+ OBJC_IVAR_$_CWFJoinStatus._allowedToBecomePrimaryAt
+ _CWFLocalNetworkMapIconKey
+ __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.448
+ __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.72
+ __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.80
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.142
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.155
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.156
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.157
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.167
+ __45-[CWFLocalDeviceDiscovery _processMRCRecord:]_block_invoke.108
+ __53-[CWFXPCRequestProxy __stopHostAPMode:XPCConnection:]_block_invoke.296
+ __54-[CWFXPCRequestProxy __startHostAPMode:XPCConnection:]_block_invoke.289
+ __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.124
+ __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.126
+ __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.137
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.101
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.102
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.103
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.117
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.67
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.77
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.86
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.90
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke_2.118
+ __80-[CWFXPCRequestProxy __privateMACSettingChangedForNetworkProfile:interfaceName:]_block_invoke.270
+ __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.246
+ ___27-[CWFInterface primaryRank]_block_invoke
+ ___27-[CWFInterface primaryRank]_block_invoke_2
+ ___34-[CWFSCNetworkService primaryRank]_block_invoke
+ ___56-[CWFXPCRequestProxy __updateJoinStatusWithPrimaryRank:]_block_invoke
+ ___os_log_helper_16_2_8_8_0_8_0_8_34_8_34_4_0_8_66_4_0_4_0
+ __block_literal_global.107
+ __block_literal_global.13
+ __block_literal_global.15
+ __block_literal_global.180
+ __block_literal_global.190
+ __block_literal_global.21
+ __block_literal_global.330
+ __block_literal_global.386
+ __block_literal_global.396
+ __block_literal_global.401
+ __block_literal_global.410
+ __block_literal_global.433
+ __block_literal_global.434
+ __block_literal_global.437
+ __block_literal_global.440
+ __block_literal_global.443
+ __block_literal_global.450
+ __block_literal_global.455
+ __block_literal_global.457
+ __block_literal_global.464
+ __block_literal_global.467
+ __block_literal_global.475
+ __block_literal_global.480
+ __block_literal_global.487
+ _kSCPropNetServicePrimaryRank
+ _kSCValNetServicePrimaryRankFirst
+ _kSCValNetServicePrimaryRankLast
+ _kSCValNetServicePrimaryRankNever
+ _kSCValNetServicePrimaryRankScoped
+ _objc_msgSend$__getPrimaryRank:
+ _objc_msgSend$__isNonPinnedEAPTLSCandidate:
+ _objc_msgSend$__serviceStateConfig
+ _objc_msgSend$__updateJoinStatusWithPrimaryRank:
+ _objc_msgSend$allowedToBecomePrimaryAt
+ _objc_msgSend$durationUntilAllowedToBecomePrimary
+ _objc_msgSend$primaryRank
+ _objc_msgSend$queryPrimaryRankWithRequestParams:reply:
+ _objc_msgSend$setAllowedToBecomePrimaryAt:
- +[CWFBonjourServiceRecord serviceRecordFromRecordName:]
- -[CWFAutoJoinManager __isAnyKnownNetworkNearby]
- -[CWFKnownNetworkPreparer _presentationSortComparator]
- -[CWFKnownNetworkPreparer profilesContainsHomeProfile:]
- -[CWFNetworkProfile captiveWebsheetLoginDate]
- -[CWFNetworkProfile(Additions) _shouldDisplayDeviceNames]
- -[CWFPrivateMACManager setUpdatedPrivateMACAddressHandler:]
- -[CWFPrivateMACManager updatedPrivateMACAddressHandler]
- -[NSArray(Additions) _removeBackslashAndSpaceCharacter]
- -[NSArray(Additions) _shuffled]
- GCC_except_table120
- GCC_except_table124
- GCC_except_table170
- GCC_except_table177
- GCC_except_table181
- GCC_except_table193
- GCC_except_table204
- GCC_except_table204
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table289
- GCC_except_table298
- GCC_except_table34
- GCC_except_table361
- GCC_except_table479
- GCC_except_table493
- GCC_except_table580
- GCC_except_table592
- GCC_except_table604
- GCC_except_table616
- GCC_except_table637
- GCC_except_table84
- OBJC_IVAR_$_CWFPrivateMACManager._updatedPrivateMACAddressHandler
- _CWFXPCLocalNetworkDeviceDiscoveryKey
- __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.452
- __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.76
- __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.48
- __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.49
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.146
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.159
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.160
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.161
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.171
- __45-[CWFLocalDeviceDiscovery _processMRCRecord:]_block_invoke.110
- __53-[CWFXPCRequestProxy __stopHostAPMode:XPCConnection:]_block_invoke.299
- __54-[CWFXPCRequestProxy __startHostAPMode:XPCConnection:]_block_invoke.292
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.134
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.140
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.141
- __59-[CWFPrivateMACManager privateMACAddressForNetworkProfile:]_block_invoke.18
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.105
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.106
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.111
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.121
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.72
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.82
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.91
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke_2.122
- __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.183
- __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.184
- __79-[CWFXPCRequestProxy __getKnownNetworkInfoForLocalNetworkPrompt:XPCConnection:]_block_invoke.326
- __80-[CWFXPCRequestProxy __privateMACSettingChangedForNetworkProfile:interfaceName:]_block_invoke.276
- __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.258
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_Additions
- __OBJC_$_CATEGORY_NSArray_$_Additions
- __OBJC_$_CLASS_METHODS_CWFBonjourServiceRecord
- ___39-[CWFAutoJoinManager __performAutoJoin]_block_invoke_2
- ___41-[CWFXPCRequestProxy __privateMACManager]_block_invoke_2
- ___59-[CWFPrivateMACManager privateMACAddressForNetworkProfile:]_block_invoke
- ___79-[CWFXPCRequestProxy __getKnownNetworkInfoForLocalNetworkPrompt:XPCConnection:]_block_invoke
- ___block_descriptor_40_e8_32s_e25_v24?0"NSSet"8"NSSet"16l
- ___block_descriptor_48_e8_32s40w_e40_v24?0"CWFNetworkProfile"8"NSString"16l
- ___block_descriptor_64_e8_32s40s48s56s_e19_"NSDictionary"8?0l
- ___getkCNSCaptiveNetworkWebSheetLoginDatePropertySymbolLoc_block_invoke
- __block_literal_global.109
- __block_literal_global.14
- __block_literal_global.192
- __block_literal_global.194
- __block_literal_global.196
- __block_literal_global.332
- __block_literal_global.394
- __block_literal_global.399
- __block_literal_global.404
- __block_literal_global.413
- __block_literal_global.436
- __block_literal_global.441
- __block_literal_global.447
- __block_literal_global.454
- __block_literal_global.459
- __block_literal_global.461
- __block_literal_global.468
- __block_literal_global.471
- __block_literal_global.479
- __block_literal_global.484
- __block_literal_global.491
- __block_literal_global.57
- _arc4random_uniform
- _getkCNSCaptiveNetworkWebSheetLoginDateProperty
- _getkCNSCaptiveNetworkWebSheetLoginDatePropertySymbolLoc
- _objc_msgSend$__isAnyKnownNetworkNearby
- _objc_msgSend$_networkProfileUsageComparator
- _objc_msgSend$_presentationSortComparator
- _objc_msgSend$_removeBackslashAndSpaceCharacter
- _objc_msgSend$_shouldDisplayDeviceNames
- _objc_msgSend$_shuffled
- _objc_msgSend$captiveWebsheetLoginDate
- _objc_msgSend$differenceFromArray:
- _objc_msgSend$discover
- _objc_msgSend$exchangeObjectAtIndex:withObjectAtIndex:
- _objc_msgSend$object
- _objc_msgSend$profilesContainsHomeProfile:
- _objc_msgSend$setHandler:
- _objc_msgSend$setUpdatedPrivateMACAddressHandler:
- _objc_msgSend$updatedPrivateMACAddressHandler
- getkCNSCaptiveNetworkWebSheetLoginDatePropertySymbolLoc.ptr
CStrings:
+ "-[CWFXPCRequestProxy __updateJoinStatusWithPrimaryRank:]"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFApple80211.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFBSS.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFIO80211.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
+ "CWFPrivateMACManager.m"
+ "GET PRIMARY RANK"
+ "InterfaceFail"
+ "PRIMARY RANK CHANGED"
+ "PRIMARY RANK CHANGED EVENT"
+ "\\032"
+ "_allowedToBecomePrimaryAt"
+ "allowed_primary_at"
+ "com.apple.wifi.denyListing_event"
+ "duration_until_allowed_primary"
+ "mapLabelCalloutIconKey"
+ "primary_rank_timeout"
+ "uuid=%!@(MISSING), intf=%!@(MISSING), ssid='%!@(MISSING)' (%!@(MISSING)), error=%!l(MISSING)d, eap=[sup=%!d(MISSING) mode=%!d(MISSING) state=%!d(MISSING) client=%!d(MISSING)], start=%!@(MISSING), assoc=%!@(MISSING) (%!l(MISSING)ums), auth=%!@(MISSING) (%!l(MISSING)ums), linkup=%!@(MISSING) (%!l(MISSING)ums), end=%!@(MISSING) (%!l(MISSING)ums), ipv4=%!@(MISSING) (%!l(MISSING)ums), ipv4Primary=%!@(MISSING) (%!l(MISSING)ums), ipv6=%!@(MISSING) (%!l(MISSING)ums), ipv6Primary=%!@(MISSING) (%!l(MISSING)ums), primaryRank=%!@(MISSING) (%!l(MISSING)ums), auto=%!s(MISSING)"
+ "wifi"
- "![self __isAnyKnownNetworkNearby]"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFApple80211.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFBSS.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFIO80211.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCManager.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
- "CFStringRef getkCNSCaptiveNetworkWebSheetLoginDateProperty(void)"
- "CWFFilteredScanResults"
- "DeviceDiscovery"
- "Known network is nearby"
- "NetworkAtLocationOfInterestType"
- "SCAN_MIN_TIMESTAMP"
- "\\ "
- "addresses"
- "com.apple.wifi.blocklisting_event"
- "com.apple.wifi.local_network_prompt"
- "filtered"
- "hasTLS || hasTTLS"
- "kCNSCaptiveNetworkWebSheetLoginDateProperty"
- "network%!d(MISSING)DeviceCount"
- "network%!d(MISSING)DeviceName"
- "networkCount"
- "process"
- "services"
- "uuid=%!@(MISSING), intf=%!@(MISSING), ssid='%!@(MISSING)' (%!@(MISSING)), error=%!l(MISSING)d, eap=[sup=%!d(MISSING) mode=%!d(MISSING) state=%!d(MISSING) client=%!d(MISSING)], start=%!@(MISSING), assoc=%!@(MISSING) (%!l(MISSING)ums), auth=%!@(MISSING) (%!l(MISSING)ums), linkup=%!@(MISSING) (%!l(MISSING)ums), end=%!@(MISSING) (%!l(MISSING)ums), ipv4=%!@(MISSING) (%!l(MISSING)ums), ipv4Primary=%!@(MISSING) (%!l(MISSING)ums), ipv6=%!@(MISSING) (%!l(MISSING)ums), ipv6Primary=%!@(MISSING) (%!l(MISSING)ums), auto=%!s(MISSING)"
- "v24@?0@\"CWFNetworkProfile\"8@\"NSString\"16"
- "v24@?0@\"NSSet\"8@\"NSSet\"16"
- "valid"

```
