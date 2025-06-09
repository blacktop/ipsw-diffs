## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-606.23.0.0.0
-  __TEXT.__text: 0xb1e8
+733.2.0.0.0
+  __TEXT.__text: 0xaf94
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0x944
   __TEXT.__const: 0xa0

   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 150B0EEE-E7C1-33E6-823F-1EE7805E4B34
+  UUID: 3244F0C7-3888-388F-9BF0-FC1B34802CBF
   Functions: 207
-  Symbols:   985
+  Symbols:   983
   CStrings:  805
 
Functions:
~ -[PRXCardContentViewController(CARSetupPrompts) carSetup_addMainContentCenteredView:size:] : 748 -> 664
~ +[CARSetupPrompts useWirelessPromptWithWirelessEnablement:declineVariant:responseHandler:] : 1724 -> 1240
~ -[CARSetupAssetUnavailableViewController viewDidLoad] : 880 -> 852

```
