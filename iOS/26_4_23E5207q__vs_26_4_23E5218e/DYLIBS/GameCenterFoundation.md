## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.4.13.0.0
-  __TEXT.__text: 0x17f494
-  __TEXT.__auth_stubs: 0x28d0
-  __TEXT.__objc_methlist: 0x123fc
-  __TEXT.__cstring: 0x18900
-  __TEXT.__const: 0x6588
+820.4.16.0.0
+  __TEXT.__text: 0x17f364
+  __TEXT.__auth_stubs: 0x2890
+  __TEXT.__objc_methlist: 0x1242c
+  __TEXT.__cstring: 0x18960
+  __TEXT.__const: 0x65c8
   __TEXT.__gcc_except_tab: 0x1410
-  __TEXT.__oslogstring: 0xdb3b
+  __TEXT.__oslogstring: 0xdb1b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__swift5_typeref: 0x1f96
+  __TEXT.__swift5_typeref: 0x1f88
   __TEXT.__swift5_capture: 0x8c0
-  __TEXT.__swift5_fieldmd: 0x171c
-  __TEXT.__constg_swiftt: 0x18b4
-  __TEXT.__swift5_reflstr: 0x1113
+  __TEXT.__swift5_fieldmd: 0x1750
+  __TEXT.__constg_swiftt: 0x18d8
+  __TEXT.__swift5_reflstr: 0x1123
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_proto: 0x444
-  __TEXT.__swift5_types: 0x1b0
+  __TEXT.__swift5_types: 0x1b4
   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__unwind_info: 0x7398
-  __TEXT.__eh_frame: 0x59f8
-  __TEXT.__objc_classname: 0x259d
-  __TEXT.__objc_methname: 0x286f5
-  __TEXT.__objc_methtype: 0x6b62
-  __TEXT.__objc_stubs: 0x15820
-  __DATA_CONST.__got: 0x1130
-  __DATA_CONST.__const: 0x6090
-  __DATA_CONST.__objc_classlist: 0x820
+  __TEXT.__eh_frame: 0x5a40
+  __TEXT.__objc_classname: 0x25ad
+  __TEXT.__objc_methname: 0x287e5
+  __TEXT.__objc_methtype: 0x6b72
+  __TEXT.__objc_stubs: 0x15840
+  __DATA_CONST.__got: 0x1138
+  __DATA_CONST.__const: 0x60c0
+  __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85d8
+  __DATA_CONST.__objc_selrefs: 0x85f0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x1478
-  __AUTH_CONST.__const: 0x59a0
-  __AUTH_CONST.__cfstring: 0x11520
-  __AUTH_CONST.__objc_const: 0x24e38
+  __AUTH_CONST.__auth_got: 0x1458
+  __AUTH_CONST.__const: 0x5a28
+  __AUTH_CONST.__cfstring: 0x115c0
+  __AUTH_CONST.__objc_const: 0x24f28
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x2c80
+  __AUTH.__objc_data: 0x2cd0
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0x105c
-  __DATA.__data: 0x3a80
+  __DATA.__objc_ivar: 0x1064
+  __DATA.__data: 0x3a98
   __DATA.__bss: 0x8510
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2ba0
-  __DATA_DIRTY.__data: 0x5f8
+  __DATA_DIRTY.__data: 0x5e8
   __DATA_DIRTY.__bss: 0xbf0
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 39837C50-3D7D-33A8-AF89-0ED5CA197CEA
-  Functions: 11011
-  Symbols:   25418
-  CStrings:  13652
+  UUID: 06333350-829B-36BE-AF56-946A4225582A
+  Functions: 11014
+  Symbols:   25430
+  CStrings:  13670
 
Symbols:
+ +[GKDaemonProxyTelemetry sendEvent:duration:]
+ -[GKInstallMetadata appStoreInstallDate]
+ -[GKInstallMetadata appStoreLastLaunchedDate]
+ -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:appStoreInstallDate:appStoreLastLaunchedDate:persistentRecordID:]
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_GKDaemonProxyTelemetry
+ _OBJC_IVAR_$_GKInstallMetadata._appStoreInstallDate
+ _OBJC_IVAR_$_GKInstallMetadata._appStoreLastLaunchedDate
+ _OBJC_METACLASS_$_GKDaemonProxyTelemetry
+ __OBJC_$_CLASS_METHODS_GKDaemonProxyTelemetry
+ __OBJC_CLASS_RO_$_GKDaemonProxyTelemetry
+ __OBJC_METACLASS_RO_$_GKDaemonProxyTelemetry
+ ___45+[GKDaemonProxyTelemetry sendEvent:duration:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ _objc_msgSend$sendEvent:duration:
+ _symbolic _____ 20GameCenterFoundation23GKDaemonProxySignposterC7RPCData33_FDBD14FCC60716D0D1151526AC440726LLV
+ _symbolic _____ 2os23OSSignpostIntervalStateC
+ _symbolic _____ySo8NSObjectC_____G s17_NativeDictionaryV 20GameCenterFoundation23GKDaemonProxySignposterC7RPCData33_FDBD14FCC60716D0D1151526AC440726LLV
+ _type_layout_string 20GameCenterFoundation23GKDaemonProxySignposterC7RPCData33_FDBD14FCC60716D0D1151526AC440726LLV
- -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:persistentRecordID:]
- _symbolic _____ySo8NSObjectC_____G s17_NativeDictionaryV 2os23OSSignpostIntervalStateC
- _symbolic _____ySo8NSObjectC_____G s18_DictionaryStorageC 2os23OSSignpostIntervalStateC
CStrings:
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKLocalPlayer.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatch.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchRequest.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchmaker.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKPlayer.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKSavedGameManager.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKTurnBasedMatch.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKCollectionUtils.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKDaemonProxy.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKInternalRepresentation.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKMatchmaker+Nearby.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUpdateGroup+NoARC.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils+FriendRequest.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/NSDictionary+GKImageAdditions.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/NSInvocation+GKAdditions+NoARC.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKCompositeTransport.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKTransportContext.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKMultiplayerServiceInterface.m"
+ "/Library/Caches/com.apple.xbs/A4B2FA77-D566-41CC-A82D-85E66A9DA49A/TemporaryDirectory.AqAAve/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKServiceInterface.m"
+ "@\"NSDictionary\"8@?0"
+ "@140@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104B112@116@124@132"
+ "GKDaemonProxyTelemetry"
+ "GKRefreshDataTypeCrossUseConsent"
+ "RPCMethod=%{public, name=RPCMethod,public}@"
+ "T@\"GKDispatchGroup\",&,V_matchingGroup"
+ "T@\"NSDate\",R,N,V_appStoreInstallDate"
+ "T@\"NSDate\",R,N,V_appStoreLastLaunchedDate"
+ "_appStoreInstallDate"
+ "_appStoreLastLaunchedDate"
+ "appStoreInstallDate"
+ "appStoreLastLaunchedDate"
+ "com.apple.GameKit.GKDaemonProxy"
+ "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:appStoreInstallDate:appStoreLastLaunchedDate:persistentRecordID:"
+ "rpc"
+ "sendEvent:duration:"
- "%s RPCMethod=%{public, signpost.telemetry:string1, name=RPCMethod,public}@"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKLocalPlayer.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatch.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchRequest.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchmaker.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKPlayer.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKSavedGameManager.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKTurnBasedMatch.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKCollectionUtils.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKDaemonProxy.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKInternalRepresentation.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKMatchmaker+Nearby.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUpdateGroup+NoARC.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils+FriendRequest.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/NSDictionary+GKImageAdditions.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/NSInvocation+GKAdditions+NoARC.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKCompositeTransport.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKTransportContext.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKMultiplayerServiceInterface.m"
- "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKServiceInterface.m"
- "@124@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104B112@116"
- "T@\"GKDispatchGroup\",V_matchingGroup"
- "enableTelemetry=YES"
- "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:persistentRecordID:"

```
