## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.300.31.0.0
-  __TEXT.__text: 0x16f0f8
+1576.400.4.0.0
+  __TEXT.__text: 0x16f660
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_methlist: 0x1a2f0
-  __TEXT.__cstring: 0x135a8
+  __TEXT.__objc_methlist: 0x1a328
+  __TEXT.__cstring: 0x13618
   __TEXT.__const: 0x1218
-  __TEXT.__oslogstring: 0x125d2
+  __TEXT.__oslogstring: 0x12642
   __TEXT.__gcc_except_tab: 0x197c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5df8
+  __TEXT.__unwind_info: 0x5e10
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x274f
-  __TEXT.__objc_methname: 0x3c5ec
+  __TEXT.__objc_methname: 0x3c66f
   __TEXT.__objc_methtype: 0x7f83
-  __TEXT.__objc_stubs: 0x20f60
+  __TEXT.__objc_stubs: 0x20fc0
   __DATA_CONST.__got: 0xe60
-  __DATA_CONST.__const: 0x3678
+  __DATA_CONST.__const: 0x3680
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xafd8
+  __DATA_CONST.__objc_selrefs: 0xaff8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11d8
   __AUTH_CONST.__const: 0x31a8
-  __AUTH_CONST.__cfstring: 0x11ce0
-  __AUTH_CONST.__objc_const: 0x28358
+  __AUTH_CONST.__cfstring: 0x11d60
+  __AUTH_CONST.__objc_const: 0x283b0
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x2648
   __AUTH.__data: 0x5e8
-  __DATA.__objc_ivar: 0x17f8
+  __DATA.__objc_ivar: 0x17fc
   __DATA.__data: 0x3368
   __DATA.__bss: 0x18b0
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FB2C27E9-F070-3E79-9EB8-D4D51411DB92
-  Functions: 10065
-  Symbols:   30079
-  CStrings:  16506
+  UUID: AF7BEB9D-8792-3498-8BC7-D016AEB8565F
+  Functions: 10073
+  Symbols:   30099
+  CStrings:  16524
 
Symbols:
+ -[TUCall canAnswerCall]
+ -[TUCall setCanAnswerCall:]
+ -[TUCallNotificationManager canAnswerCallChangedForCall:]
+ -[TUFeatureFlags isSameWiFiNetworkPingCheckEnabled]
+ -[TUProxyCall setCanAnswerCall:]
+ _OBJC_IVAR_$_TUCall._canAnswerCall
+ _TUCallCanAnswerCallChangedNotification
+ _TUIsSameWiFiNetworkPingCheckEnabled
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.664
+ __OBJC_$_PROP_LIST_TUFeatureFlags.668
+ ___32-[TUProxyCall setCanAnswerCall:]_block_invoke
+ ___32-[TUProxyCall setCanAnswerCall:]_block_invoke_2
+ ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.61
+ ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.60
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke.272
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_2.275
+ ___block_descriptor_786_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s272s280s288s296s304s312s320s328s336s344s352s360s368s376s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8s176l8s184l8s192l8s200l8s208l8s216l8s224l8s232l8s240l8s248l8s256l8s264l8s272l8s280l8s288l8s296l8s304l8s312l8s320l8s328l8s336l8s344l8s352l8s360l8s368l8s376l8
+ ___block_literal_global.2026
+ ___block_literal_global.2032
+ ___block_literal_global.280
+ ___block_literal_global.357
+ ___block_literal_global.385
+ ___block_literal_global.390
+ ___block_literal_global.395
+ _objc_msgSend$canAnswerCall
+ _objc_msgSend$canAnswerCallChangedForCall:
+ _objc_msgSend$isSameWiFiNetworkPingCheckEnabled
- GCC_except_table157
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.661
- __OBJC_$_PROP_LIST_TUFeatureFlags.665
- ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.56
- ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.55
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke.269
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_2.272
- ___block_descriptor_784_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s272s280s288s296s304s312s320s328s336s344s352s360s368s376s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8s176l8s184l8s192l8s200l8s208l8s216l8s224l8s232l8s240l8s248l8s256l8s264l8s272l8s280l8s288l8s296l8s304l8s312l8s320l8s328l8s336l8s344l8s352l8s360l8s368l8s376l8
- ___block_literal_global.2012
- ___block_literal_global.2018
- ___block_literal_global.271
- ___block_literal_global.348
- ___block_literal_global.382
- ___block_literal_global.387
- ___block_literal_global.392
CStrings:
+ " cAns=%d"
+ "TB,N,V_canAnswerCall"
+ "TUCallCanAnswerCallChangedNotification"
+ "_canAnswerCall"
+ "canAnswerCall"
+ "canAnswerCallChangedForCall"
+ "canAnswerCallChangedForCall %@"
+ "canAnswerCallChangedForCall:"
+ "isSameWiFiNetworkPingCheck"
+ "isSameWiFiNetworkPingCheckEnabled"
+ "isSameWiFiNetworkPingCheckEnabled ff: %@, server bag: %@"
+ "same-wifi-network-ping-disabled"
+ "setCanAnswerCall:"
+ "\xf0\xf0A"
- "\xf0\xf01"

```
