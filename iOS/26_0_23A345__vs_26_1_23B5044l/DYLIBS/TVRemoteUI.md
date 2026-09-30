## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-548.0.17.0.0
-  __TEXT.__text: 0xcd3ac
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0xb3e8
+548.10.16.0.0
+  __TEXT.__text: 0xcd520
+  __TEXT.__auth_stubs: 0x1b30
+  __TEXT.__objc_methlist: 0xb3e0
   __TEXT.__const: 0x24a4
-  __TEXT.__gcc_except_tab: 0x1ef0
+  __TEXT.__gcc_except_tab: 0x1ec4
   __TEXT.__cstring: 0x745a
   __TEXT.__oslogstring: 0x59c2
   __TEXT.__ustring: 0x4a

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2ad0
+  __TEXT.__unwind_info: 0x2ac8
   __TEXT.__eh_frame: 0x878
   __TEXT.__objc_classname: 0x144f
-  __TEXT.__objc_methname: 0x1b1a2
+  __TEXT.__objc_methname: 0x1b1ed
   __TEXT.__objc_methtype: 0x44c7
-  __TEXT.__objc_stubs: 0x13020
-  __DATA_CONST.__got: 0xd28
+  __TEXT.__objc_stubs: 0x12fe0
+  __DATA_CONST.__got: 0xd38
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67b0
+  __DATA_CONST.__objc_selrefs: 0x67b8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xd90
+  __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0x2eb8
   __AUTH_CONST.__cfstring: 0x3a20
-  __AUTH_CONST.__objc_const: 0x14a10
+  __AUTH_CONST.__objc_const: 0x14a08
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 85F9EF19-C4BA-3270-A5FA-48BE647A16A4
-  Functions: 4700
-  Symbols:   17458
+  UUID: F9DE9F88-3FD9-3A45-BE2D-4B846222C04F
+  Functions: 4702
+  Symbols:   17462
   CStrings:  7205
 
Symbols:
+ GCC_except_table94
+ _$s5UIKit11_GlassGroupV10foregroundACSb_tcfC
+ _$s5UIKit11_GlassGroupVMa
+ _$s5UIKit11_GlassGroupVSo6UIViewCAAE8MaterialAAWP
+ _$s5UIKit6_GlassV8flexibleyACSbF
+ _$sSo6UIViewC10TVRemoteUIE13setGlassGroupyyF
+ _$sSo6UIViewC10TVRemoteUIE13setGlassGroupyyFTo
+ _$sSo6UIViewC10TVRemoteUIE26setFlexibleGlassBackgroundyyF
+ _$sSo6UIViewC10TVRemoteUIE26setFlexibleGlassBackgroundyyFTo
+ _UIFontWeightMedium
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.125
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.132
+ ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.204
+ ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.206
+ ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.177
+ ___59-[TVRUIRemoteViewController _startFindingSessionForDevice:]_block_invoke.248
+ ___block_literal_global.134
+ _objc_msgSend$_preferredFontForTextStyle:weight:
+ _objc_msgSend$_setEnableMonochromaticTreatment:
+ _objc_msgSend$_setMonochromaticTreatment:
+ _objc_msgSend$tvrui_setFlexibleGlassBackground
+ _objc_msgSend$tvrui_setGlassGroup
- -[TVRUICoreDevice isLegacyAppleTV]
- GCC_except_table95
- ___41-[TVRKeyboardView initWithStyleProvider:]_block_invoke
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.126
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.133
- ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.205
- ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.207
- ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.178
- ___59-[TVRUIRemoteViewController _startFindingSessionForDevice:]_block_invoke.249
- _objc_msgSend$_createLegacyButtonPanel
- _objc_msgSend$_createLegacyPanelWithkeyboard
- _objc_msgSend$_glassButtonConfiguration
- _objc_msgSend$capellaEnabled
- _objc_msgSend$deviceTitleHeight
- _objc_msgSend$greymatterEnabled
- _objc_msgSend$isLegacyAppleTV
CStrings:
+ "Adding connected device: %{public}@"
+ "Adding suggested device: %{public}@"
+ "User picked device: %{public}@"
+ "User tapped on already connected device: %{public}@"
+ "[Autoconnect] Updated active device to: %{public}@"
+ "_preferredFontForTextStyle:weight:"
+ "_setEnableMonochromaticTreatment:"
+ "_setMonochromaticTreatment:"
+ "devices: %{public}@"
+ "tvrui_setFlexibleGlassBackground"
+ "tvrui_setGlassGroup"
- "Adding connected device: %@"
- "Adding suggested device: %@"
- "Device is legacy apple tv. transitioning to legacy buttonpanel"
- "User picked device %@"
- "User tapped on already connected device"
- "_glassButtonConfiguration"
- "capellaEnabled"
- "devices: %@"
- "greymatterEnabled"
- "isLegacyAppleTV"
- "suggested devices: %@"

```
