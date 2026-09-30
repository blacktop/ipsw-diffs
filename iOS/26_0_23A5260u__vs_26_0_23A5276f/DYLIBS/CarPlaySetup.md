## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-733.2.0.0.0
-  __TEXT.__text: 0xaf94
+738.1.0.0.0
+  __TEXT.__text: 0xb018
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x944
+  __TEXT.__objc_methlist: 0x954
   __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x472
-  __TEXT.__cstring: 0xc4f
+  __TEXT.__oslogstring: 0x4ab
+  __TEXT.__cstring: 0xda5
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x213c
+  __TEXT.__objc_methname: 0x2184
   __TEXT.__objc_methtype: 0x485
-  __TEXT.__objc_stubs: 0x1f00
+  __TEXT.__objc_stubs: 0x1f20
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x1420
   __AUTH_CONST.__objc_const: 0x1298
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3244F0C7-3888-388F-9BF0-FC1B34802CBF
-  Functions: 207
-  Symbols:   983
-  CStrings:  805
+  UUID: 9BCF88EB-D388-3427-90E6-83AD35209531
+  Functions: 208
+  Symbols:   988
+  CStrings:  830
 
Symbols:
+ +[CARSetupPrompts waitingOnMessagingPrompt]
+ +[CARSetupPrompts waitingOnStartSessionPrompt]
+ ___105+[CARSetupPrompts assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke.237
+ ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.214
+ ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.215
+ ___46+[CARSetupPrompts waitingOnStartSessionPrompt]_block_invoke
+ ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.156
+ ___block_descriptor_32_e19_v16?0"PRXAction"8l
+ _objc_msgSend$showActivityIndicatorWithStatus:
- +[CARSetupPrompts waitingPrompt]
- _NeedsLocalization
- ___105+[CARSetupPrompts assetSupportingUseWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:]_block_invoke.204
- ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.202
- ___106+[CARSetupPrompts assetSupportingConnectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.203
- ___91+[CARSetupPrompts connectPromptWithBluetoothOnlyOption:wirelessEnablement:responseHandler:]_block_invoke.158
CStrings:
+ "CONNECTING_MESSAGE"
+ "CONNECTING_TITLE"
+ "CONNECT_CARPLAY_ULTRA_CARD_DONTUSE"
+ "CONNECT_CARPLAY_ULTRA_CARD_ENABLE"
+ "CONNECT_CARPLAY_ULTRA_CARD_MESSAGE"
+ "CONNECT_CARPLAY_ULTRA_CARD_MESSAGE_BT"
+ "CONNECT_CARPLAY_ULTRA_CARD_MESSAGE_BT_WIFI"
+ "CONNECT_CARPLAY_ULTRA_CARD_MESSAGE_WIFI"
+ "CONNECT_CARPLAY_ULTRA_CARD_NOTNOW"
+ "CONNECT_TO_CARPLAY_ULTRA_CARD_TITLE"
+ "Connecting"
+ "received dismiss / decline for waiting on vehicle prompt"
+ "showActivityIndicatorWithStatus:"
+ "waitingOnMessagingPrompt"
+ "waitingOnStartSessionPrompt"
- "waitingPrompt"

```
