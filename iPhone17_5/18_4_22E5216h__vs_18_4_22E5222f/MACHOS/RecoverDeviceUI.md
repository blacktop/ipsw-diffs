## RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-2171.100.132.0.0
-  __TEXT.__text: 0xd8e0
+2171.100.143.0.0
+  __TEXT.__text: 0xda90
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x28a0
-  __TEXT.__objc_methlist: 0xfc8
+  __TEXT.__objc_stubs: 0x28e0
+  __TEXT.__objc_methlist: 0xfe0
   __TEXT.__gcc_except_tab: 0x3dc
   __TEXT.__cstring: 0xf8a
-  __TEXT.__objc_methname: 0x3d66
+  __TEXT.__objc_methname: 0x3db8
   __TEXT.__objc_classname: 0x146
   __TEXT.__objc_methtype: 0x15c1
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x11a4
+  __TEXT.__oslogstring: 0x1245
   __TEXT.__unwind_info: 0x260
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x1e8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x12a0
-  __DATA.__objc_selrefs: 0x1030
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_const: 0x12d0
+  __DATA.__objc_selrefs: 0x1040
+  __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 209
-  Symbols:   1765
-  CStrings:  1059
+  Functions: 211
+  Symbols:   1778
+  CStrings:  1065
 
Symbols:
+ -[RecoverDeviceUIExtensionRemoteViewController setShowingResultCard:]
+ -[RecoverDeviceUIExtensionRemoteViewController showingResultCard]
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._showingResultCard
+ __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.762
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.686
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.688
+ __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.767
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.678
+ __block_literal_global.764
+ _objc_msgSend$setShowingResultCard:
+ _objc_msgSend$showingResultCard
- __57-[RecoverDeviceUIExtensionRemoteViewController setupStop]_block_invoke.761
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.685
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.687
- __69-[RecoverDeviceUIExtensionRemoteViewController waitForServerResponse]_block_invoke.765
- ___94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke_2
- __block_literal_global.763
CStrings:
+ "Already showing result card, nothing to do"
+ "Got request to show code card, flags: %d, ThrottleSeconds: %d"
+ "Ignoring show code card because we have an overall result card present, attempt: %llu"
+ "TB,V_showingResultCard"
+ "_showingResultCard"
+ "setShowingResultCard:"
+ "showingResultCard"
- "Got request to show code card"

```
