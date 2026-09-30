## CaptiveNetwork

> `/System/Library/PrivateFrameworks/CaptiveNetwork.framework/Versions/A/CaptiveNetwork`

```diff

-480.60.4.0.0
-  __TEXT.__text: 0xae44
+491.100.3.0.0
+  __TEXT.__text: 0xae80
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x168
-  __TEXT.__cstring: 0x613
+  __TEXT.__cstring: 0x626
   __TEXT.__oslogstring: 0x70b
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methname: 0x2c
   __TEXT.__objc_methtype: 0x46
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
   __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x4b0
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x40
-  __DATA.__data: 0x140
+  __DATA.__data: 0x148
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0682250F-16E2-37FF-8B33-00C81B09CDCF
-  Functions: 216
-  Symbols:   480
-  CStrings:  230
+  UUID: A321DCBF-20B1-3881-AA75-9E41136F22D1
+  Functions: 222
+  Symbols:   491
+  CStrings:  232
 
Symbols:
+ CNNetworkGetTypeID.cold.1
+ CNPluginCommandCreate.cold.1
+ CNPluginCommandGetTypeID.cold.1
+ CNPluginMonitorStart.cold.1
+ CNPluginMonitorStop.cold.1
+ CNPluginResponseCreate.cold.1
+ CNPluginResponseGetTypeID.cold.1
+ CNScanListFilterStart.cold.1
+ CNScanListFilterStop.cold.1
+ __CNNetworkAllocate.cold.1
+ __block_descriptor_tmp.13
+ __block_descriptor_tmp.15
+ __block_descriptor_tmp.32
+ __block_descriptor_tmp.44
+ __block_descriptor_tmp.48
+ __block_literal_global.17
+ _kCNSWebsheetInfoPropertyCarPlayAndInternet
- __block_descriptor_tmp.12
- __block_descriptor_tmp.29
- __block_descriptor_tmp.41
- __block_descriptor_tmp.45
- __block_literal_global.14
Functions:
~ ___CNMonitorSetQueueAndHandler_block_invoke : 492 -> 496
~ _CNPluginMonitorStart : 124 -> 108
~ _CNPluginMonitorStop : 92 -> 76
~ _CNAccountsCopy : 156 -> 148
~ ___CNMarkPortalOnline : 208 -> 204
~ ___CNMarkPortalOffline : 208 -> 204
~ ___CNCopySupportedInterfaces : 156 -> 148
~ ___CNNetworkAllocate : 92 -> 76
~ _CNNetworkGetTypeID : 68 -> 56
~ _CNNetworkGetPluginBundleID : 88 -> 92
~ _CNNetworkGetSSIDString : 88 -> 92
~ _CNNetworkGetSSID : 88 -> 92
~ _CNNetworkGetBSSID : 88 -> 92
~ __CNNetworkWasAutoJoined : 88 -> 92
~ _CNNetworkGetPassword : 88 -> 92
~ _CNNetworkIsChosenPlugin : 104 -> 108
~ ___CNPluginHandleCommandInfo_block_invoke : 508 -> 504
~ _CNPluginCommandGetTypeID : 68 -> 56
~ _CNPluginCommandCreate : 268 -> 252
~ _CNPluginResponseGetTypeID : 68 -> 56
~ _CNPluginResponseCreate : 156 -> 140
~ _ServerConnectionConnect : 1440 -> 1416
~ _CNScanListFilterStart : 124 -> 108
~ _CNScanListFilterStop : 84 -> 68
~ _CNSClient_server : 152 -> 156
~ _ParsePost : 784 -> 800
~ _ForgetNetwork : 356 -> 352
~ _PurgeAccountRecord : 356 -> 352
~ _DebugLaunchWebsheet : 432 -> 436
~ _RegisterSSIDs : 432 -> 436
~ _CopySupportedInterfaces : 472 -> 476
~ _CopyAccountList : 472 -> 476
~ _AddAccount : 816 -> 848
~ _ConnectionEstablish : 504 -> 508
~ _ConnectionGetCommandInfo : 472 -> 476
~ _ConnectionProvideResponse : 432 -> 436
~ _ConnectionSendCmdAck : 432 -> 436
~ _CopyLandingPageURL : 488 -> 492
~ _ConnectionProcessControl : 468 -> 472
~ _UserInteractionIsRequired : 372 -> 376
CStrings:
+ "CarPlayAndInternet"

```
