## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-17.3.4.0.0
-  __TEXT.__text: 0x365cc
+17.4.19.0.0
+  __TEXT.__text: 0x366a0
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x2f88
+  __TEXT.__objc_methlist: 0x2fa0
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0xb2ec
+  __TEXT.__cstring: 0xb34e
   __TEXT.__gcc_except_tab: 0xcc4
-  __TEXT.__unwind_info: 0xcec
+  __TEXT.__unwind_info: 0xce8
   __TEXT.__objc_classname: 0x56d
-  __TEXT.__objc_methname: 0x888f
-  __TEXT.__objc_methtype: 0x17ea
-  __TEXT.__objc_stubs: 0x7920
+  __TEXT.__objc_methname: 0x88db
+  __TEXT.__objc_methtype: 0x17fa
+  __TEXT.__objc_stubs: 0x7960
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x11e0
+  __DATA_CONST.__const: 0x1230
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f28
-  __DATA_CONST.__objc_selrefs: 0x2070
+  __DATA_CONST.__objc_const: 0x3f58
+  __DATA_CONST.__objc_selrefs: 0x2080
+  __DATA_CONST.__objc_classrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x18e8
-  __AUTH_CONST.__cfstring: 0x6dc0
+  __AUTH_CONST.__cfstring: 0x6de0
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_classrefs: 0x3d8
-  __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x344
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x370
   __DATA.__bss: 0x138
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1160
-  Symbols:   4573
-  CStrings:  2744
+  Functions: 1162
+  Symbols:   4582
+  CStrings:  2753
 
Symbols:
+ -[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:]
+ -[WLWiFiNetwork channel]
+ -[WLWiFiNetwork setChannel:]
+ _OBJC_IVAR_$_WLWiFiNetwork._channel
+ ___130-[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:]_block_invoke
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs96w_e5_v8?0lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_48_e8_32s40bs_e23_v28?0B8q12"NSError"20ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e23_v28?0B8q12"NSError"20ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e23_v28?0B8q12"NSError"20lw88l8s32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_literal_global.66
+ _objc_msgSend$_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:
+ _objc_msgSend$channel
+ _objc_msgSend$setChannel:
- -[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:]
- ___115-[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:]_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs96w_e5_v8?0lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e20_v20?0B8"NSError"12lw88l8s32l8s40l8s48l8s56l8s64l8s80l8s72l8
- ___block_literal_global.62
- _objc_msgSend$_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:
CStrings:
+ "%@: Received the channel used for the new network. channel=%ld"
+ "T@\"NSString\",?,R,C"
+ "Tq,N,V_channel"
+ "WiFi _startNetworkCallback error %@ response %@ network=%@"
+ "_channel"
+ "_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:"
+ "channel"
+ "setChannel:"
+ "v24@0:8q16"
+ "v28@?0B8q12@\"NSError\"20"
+ "v92@0:8@16@24@32@40@48@?56B64@68@76q84"
- "WiFi _startNetworkCallback error %@ response %@"
- "_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:"
- "v84@0:8@16@24@32@40@48@?56B64@68@76"

```
