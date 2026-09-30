## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy`

```diff

-  __TEXT.__text: 0xe04c0
-  __TEXT.__objc_methlist: 0x13630
-  __TEXT.__const: 0x7b8
-  __TEXT.__cstring: 0x2382b
+  __TEXT.__text: 0xe043c
+  __TEXT.__objc_methlist: 0x13658
+  __TEXT.__const: 0x7a0
+  __TEXT.__cstring: 0x238db
   __TEXT.__oslogstring: 0x3f0a
   __TEXT.__gcc_except_tab: 0x1728
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__swift5_typeref: 0x7e
-  __TEXT.__swift5_capture: 0x24
-  __TEXT.__constg_swiftt: 0x160
-  __TEXT.__swift5_reflstr: 0x70
-  __TEXT.__swift5_fieldmd: 0xb4
+  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__swift5_typeref: 0x6a
+  __TEXT.__swift5_reflstr: 0x6a
+  __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x2758
-  __TEXT.__eh_frame: 0x98
+  __TEXT.__swift5_capture: 0x24
+  __TEXT.__unwind_info: 0x2748
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__const: 0xd08
   __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa50
+  __DATA_CONST.__objc_selrefs: 0xaa68
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x1508
-  __DATA_CONST.__got: 0xb40
-  __AUTH_CONST.__const: 0x2058
-  __AUTH_CONST.__cfstring: 0x1fb60
-  __AUTH_CONST.__objc_const: 0x24fc8
+  __DATA_CONST.__got: 0xb30
+  __AUTH_CONST.__const: 0x20b8
+  __AUTH_CONST.__cfstring: 0x1fbe0
+  __AUTH_CONST.__objc_const: 0x24fd8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1a58
   __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xc78
-  __AUTH.__objc_data: 0x708
-  __DATA.__objc_ivar: 0x24d8
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH.__objc_data: 0x618
+  __DATA.__objc_ivar: 0x24dc
   __DATA.__data: 0x1c38
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x3398
-  __DATA_DIRTY.__data: 0x168
-  __DATA_DIRTY.__bss: 0x320
+  __DATA.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x3488
+  __DATA_DIRTY.__data: 0x150
+  __DATA_DIRTY.__bss: 0x338
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7028
-  Symbols:   15554
-  CStrings:  9105
+  Functions: 7030
+  Symbols:   15566
+  CStrings:  9113
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[WFLoggerFileWithTTL _stopWatchingLogFileOnQueue]
+ -[WiFiUsagePowerAnalytics collectCurrentNetworkInfo]
+ -[WiFiUsagePowerAnalytics mloConnection]
+ -[WiFiUsagePowerAnalytics setMloConnection:]
+ OBJC_IVAR_$_WiFiUsagePowerAnalytics._mloConnection
+ ___30-[WFLoggerFileWithTTL dealloc]_block_invoke
+ ___39-[WFLoggerFileWithTTL checkForRotation]_block_invoke
+ ___42-[WFLoggerFileWithTTL stopWatchingLogFile]_block_invoke
+ ___46-[WFLoggerFileWithTTL WFLog:privacy:cfStrMsg:]_block_invoke
+ ___52-[WFLoggerFileWithTTL WFLog:privacy:message:valist:]_block_invoke
+ ___block_descriptor_56_e8_32o40o_e5_v8?0l
+ ___block_descriptor_56_e8_32o_e5_v8?0l
+ __swift_closure_destructor
+ _objc_msgSend$_stopWatchingLogFileOnQueue
+ _objc_msgSend$collectCurrentNetworkInfo
+ _objc_msgSend$mloConnection
+ _objc_msgSend$setActivityType:
+ _objc_msgSend$setMloConnection:
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
- ___swift__destructor
- _objc_msgSend$addAccessPointsObject:
- _objc_msgSend$unsignedCharValue
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
- _symbolic _____SgXw 10WiFiPolicy0aB19AONSenseBeaconCacheC
- _symbolic _____SgXwz_Xx 10WiFiPolicy0aB19AONSenseBeaconCacheC
CStrings:
+ "-[WFLoggerFileWithTTL _stopWatchingLogFileOnQueue]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.D7h4ep/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
+ "25%"
+ "EMLSR_CONNECTION"
+ "MLO_CONNECTION"
+ "collectCurrentNetworkInfo - APPLE80211_IOC_CURRENT_NETWORK failed with error: %d"
+ "collectCurrentNetworkInfo - APPLE80211_IOC_CURRENT_NETWORK returned nil dict"
+ "collectCurrentNetworkInfo - No Apple80211 reference available"
+ "com.apple.WiFiPolicy.WFLoggerFileWithTTL"
- "-[WFLoggerFileWithTTL stopWatchingLogFile]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pQHeCZ/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "LP_EMLSR_SUPPORTED"
- "WiFiUsagePowerAnalytics: extractMloLinkInfo - Processing %lu MLO links"
- "com.apple.wifi.aonsense.cache"

```
