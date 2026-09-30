## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-  __TEXT.__text: 0xe2c04
-  __TEXT.__objc_methlist: 0x13cf0
-  __TEXT.__const: 0x878
-  __TEXT.__cstring: 0x25c2b
+  __TEXT.__text: 0xe2b64
+  __TEXT.__objc_methlist: 0x13d18
+  __TEXT.__const: 0x868
+  __TEXT.__cstring: 0x25ceb
   __TEXT.__oslogstring: 0x54ee
   __TEXT.__gcc_except_tab: 0x190c
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__ustring: 0x82
-  __TEXT.__swift5_typeref: 0xb8
-  __TEXT.__swift5_capture: 0x34
-  __TEXT.__constg_swiftt: 0x188
+  __TEXT.__constg_swiftt: 0x180
+  __TEXT.__swift5_typeref: 0xa4
   __TEXT.__swift5_reflstr: 0x8f
-  __TEXT.__swift5_fieldmd: 0xc0
+  __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x29f0
-  __TEXT.__eh_frame: 0x98
+  __TEXT.__swift5_capture: 0x34
+  __TEXT.__unwind_info: 0x29e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2738
+  __DATA_CONST.__const: 0x2790
   __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf00
+  __DATA_CONST.__objc_selrefs: 0xaf18
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x1510
-  __DATA_CONST.__got: 0xbc8
+  __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x20d20
-  __AUTH_CONST.__objc_const: 0x25970
+  __AUTH_CONST.__cfstring: 0x20da0
+  __AUTH_CONST.__objc_const: 0x25980
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1aa0
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xf18
-  __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x2564
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH.__objc_data: 0x6b8
+  __DATA.__objc_ivar: 0x2568
   __DATA.__data: 0x1ca0
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x3468
-  __DATA_DIRTY.__data: 0x178
-  __DATA_DIRTY.__bss: 0x378
+  __DATA.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x3558
+  __DATA_DIRTY.__data: 0x160
+  __DATA_DIRTY.__bss: 0x390
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7203
-  Symbols:   23177
-  CStrings:  9571
+  Functions: 7205
+  Symbols:   23199
+  CStrings:  9579
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
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
+ _OBJC_IVAR_$_WiFiUsagePowerAnalytics._mloConnection
+ ___30-[WFLoggerFileWithTTL dealloc]_block_invoke
+ ___39-[WFLoggerFileWithTTL checkForRotation]_block_invoke
+ ___42-[WFLoggerFileWithTTL stopWatchingLogFile]_block_invoke
+ ___46-[WFLoggerFileWithTTL WFLog:privacy:cfStrMsg:]_block_invoke
+ ___52-[WFLoggerFileWithTTL WFLog:privacy:message:valist:]_block_invoke
+ ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o_e5_v8?0ls32l8
+ _objc_msgSend$_stopWatchingLogFileOnQueue
+ _objc_msgSend$collectCurrentNetworkInfo
+ _objc_msgSend$mloConnection
+ _objc_msgSend$setActivityType:
+ _objc_msgSend$setMloConnection:
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x24
+ _swift_retain_x21
+ _symbolic Ig_
- _objc_msgSend$addAccessPointsObject:
- _objc_msgSend$unsignedCharValue
- _swift_release_x26
- _swift_retain
- _swift_retain_x26
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
- _symbolic _____SgXw 10WiFiPolicy0aB19AONSenseBeaconCacheC
- _symbolic _____SgXwz_Xx 10WiFiPolicy0aB19AONSenseBeaconCacheC
CStrings:
+ "-[WFLoggerFileWithTTL _stopWatchingLogFileOnQueue]"
+ "25%"
+ "EMLSR_CONNECTION"
+ "MLO_CONNECTION"
+ "collectCurrentNetworkInfo - APPLE80211_IOC_CURRENT_NETWORK failed with error: %d"
+ "collectCurrentNetworkInfo - APPLE80211_IOC_CURRENT_NETWORK returned nil dict"
+ "collectCurrentNetworkInfo - No Apple80211 reference available"
+ "com.apple.WiFiPolicy.WFLoggerFileWithTTL"
- "-[WFLoggerFileWithTTL stopWatchingLogFile]"
- "LP_EMLSR_SUPPORTED"
- "WiFiUsagePowerAnalytics: extractMloLinkInfo - Processing %lu MLO links"
- "com.apple.wifi.aonsense.cache"

```
