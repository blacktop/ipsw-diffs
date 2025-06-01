## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-17.2.5.0.0
-  __TEXT.__text: 0x354b0
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x2f44
+17.3.4.0.0
+  __TEXT.__text: 0x365cc
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x2f88
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0xb000
-  __TEXT.__gcc_except_tab: 0xc54
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__cstring: 0xb2ec
+  __TEXT.__gcc_except_tab: 0xcc4
+  __TEXT.__unwind_info: 0xcec
   __TEXT.__objc_classname: 0x56d
-  __TEXT.__objc_methname: 0x874d
-  __TEXT.__objc_methtype: 0x1762
-  __TEXT.__objc_stubs: 0x7800
+  __TEXT.__objc_methname: 0x888f
+  __TEXT.__objc_methtype: 0x17ea
+  __TEXT.__objc_stubs: 0x7920
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1148
+  __DATA_CONST.__const: 0x11e0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3f28
-  __DATA_CONST.__objc_selrefs: 0x2028
+  __DATA_CONST.__objc_selrefs: 0x2070
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x18e8
-  __AUTH_CONST.__cfstring: 0x6b60
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__cfstring: 0x6dc0
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_classrefs: 0x3d0
+  __DATA.__objc_classrefs: 0x3d8
   __DATA.__objc_superrefs: 0x118
   __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x370

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 72DB1135-DA6F-3492-AC5A-CF6D677E6D20
-  Functions: 1147
-  Symbols:   4523
-  CStrings:  3568
+  UUID: D7F289EE-195C-318C-AD23-3EC9BBACD68A
+  Functions: 1160
+  Symbols:   4573
+  CStrings:  3622
 
Symbols:
+ -[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:]
+ -[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:channel:error:completion:]
+ -[WLWiFiController preferredChannel:]
+ -[WLWiFiManager _preferredChannel:network:channels:completion:]
+ -[WLWiFiManager currentNetwork:channels:completion:]
+ -[WLWiFiManager preferredChannel:]
+ -[WLWiFiManager scanNetwork:]
+ GCC_except_table24
+ GCC_except_table35
+ GCC_except_table39
+ GCC_except_table40
+ _OBJC_CLASS_$_NSSortDescriptor
+ _WiFiDeviceClientCopyCurrentNetworkAsync
+ _WiFiDeviceClientCopyProperty
+ _WiFiDeviceClientScanAsync
+ _WiFiManagerClientGetDevice
+ _WiFiNetworkGetChannel
+ __WiFiDeviceClientCopyCurrentNetworkAsyncCallback
+ __WiFiDeviceClientScanAsyncCallback
+ ___115-[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:]_block_invoke
+ ___29-[WLWiFiManager scanNetwork:]_block_invoke
+ ___52-[WLWiFiManager currentNetwork:channels:completion:]_block_invoke
+ ___63-[WLWiFiManager _preferredChannel:network:channels:completion:]_block_invoke
+ ___63-[WLWiFiManager _preferredChannel:network:channels:completion:]_block_invoke_2
+ ___84-[WLDeviceDiscoveryController _queue_startDiscoveryWithPreGeneratedCode:completion:]_block_invoke
+ ___91-[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:channel:error:completion:]_block_invoke
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_40_e8_32bs_e62_v52?0B8"NSString"12"NSString"20"NSString"28q36"NSError"44ls32l8
+ ___block_descriptor_56_e8_32bs40w_e22_v16?0"NSDictionary"8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e24_v16?0^{__WiFiNetwork=}8lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e8_v16?0q8lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e20_v20?0B8"NSError"12lw88l8s32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_literal_global.76
+ _objc_msgSend$_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:
+ _objc_msgSend$_preferredChannel:network:channels:completion:
+ _objc_msgSend$currentNetwork:channels:completion:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$preferredChannel:
+ _objc_msgSend$scanNetwork:
+ _objc_msgSend$softAPDidStart:ssid:psk:secret:srp:channel:error:completion:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$sortedArrayUsingDescriptors:
- -[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:error:completion:]
- GCC_except_table22
- GCC_except_table33
- GCC_except_table37
- ___83-[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:error:completion:]_block_invoke
- ___92-[WLDeviceDiscoveryController enableSoftAPWithSSID:password:channels:secret:srp:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e59_v44?0B8"NSString"12"NSString"20"NSString"28"NSError"36ls32l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e20_v20?0B8"NSError"12lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- _objc_msgSend$softAPDidStart:ssid:psk:secret:srp:error:completion:
CStrings:
+ "CHANNELINFO_CH_NUM"
+ "CHANNELINFO_INDOOR_RESTRICTED"
+ "CHANNELINFO_PASSIVE"
+ "SCAN_BSS_TYPE"
+ "SCAN_DWELL_TIME"
+ "SCAN_NUM_SCANS"
+ "SCAN_PHY_MODE"
+ "SUP_CHANNEL"
+ "SUP_CHANNEL_FLAGS"
+ "_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:"
+ "_preferredChannel:network:channels:completion:"
+ "channel=%@, indoor_restricted=%@, passive=%@"
+ "could not find en0 interface and will return channel 1 for safety."
+ "could not get the current network from en0 and will return channel 1 for safety. error=%d"
+ "could not scan other networks and will return channel 1 for safety. error=%d"
+ "currentNetwork:channels:completion:"
+ "did determine the preferred channel. current_channel=%ld, preferred_channel=%ld"
+ "did receive the current network. network=%@"
+ "did scan networks. error=%d"
+ "en0"
+ "found a network. channel=%@"
+ "found available channel. channel=%@, flags=%@, skip=%d"
+ "keysSortedByValueUsingComparator:"
+ "numberWithInteger:"
+ "preferredChannel:"
+ "q24@?0@8@16"
+ "scanNetwork:"
+ "softAPDidStart:ssid:psk:secret:srp:channel:error:completion:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0^{__WiFiNetwork=}8"
+ "v16@?0q8"
+ "v40@0:8^{__WiFiDeviceClient=}16@24@?32"
+ "v48@0:8^{__WiFiDeviceClient=}16^{__WiFiNetwork=}24@32@?40"
+ "v52@?0B8@\"NSString\"12@\"NSString\"20@\"NSString\"28q36@\"NSError\"44"
+ "v76@0:8B16@20@28@36@44@52@60@?68"
+ "v84@0:8@16@24@32@40@48@?56B64@68@76"
- "softAPDidStart:ssid:psk:secret:srp:error:completion:"
- "v44@?0B8@\"NSString\"12@\"NSString\"20@\"NSString\"28@\"NSError\"36"
- "v68@0:8B16@20@28@36@44@52@?60"

```
