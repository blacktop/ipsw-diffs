## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-548.10.21.0.0
-  __TEXT.__text: 0xcd4b8
+548.10.23.0.0
+  __TEXT.__text: 0xcd5a8
   __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xb3e0
+  __TEXT.__objc_methlist: 0xb3d0
   __TEXT.__const: 0x24a4
   __TEXT.__gcc_except_tab: 0x1ec4
   __TEXT.__cstring: 0x740a
-  __TEXT.__oslogstring: 0x59c2
+  __TEXT.__oslogstring: 0x5a02
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__constg_swiftt: 0x2dcc

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2ac0
+  __TEXT.__unwind_info: 0x2ac8
   __TEXT.__eh_frame: 0x878
   __TEXT.__objc_classname: 0x144f
-  __TEXT.__objc_methname: 0x1b1d9
+  __TEXT.__objc_methname: 0x1b1bc
   __TEXT.__objc_methtype: 0x44c7
-  __TEXT.__objc_stubs: 0x13000
+  __TEXT.__objc_stubs: 0x12fe0
   __DATA_CONST.__got: 0xd38
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67b8
+  __DATA_CONST.__objc_selrefs: 0x67b0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0x2eb8
   __AUTH_CONST.__cfstring: 0x3a00
-  __AUTH_CONST.__objc_const: 0x14a20
+  __AUTH_CONST.__objc_const: 0x14a10
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7F579B95-9C14-3293-91F6-585E393EEF17
+  UUID: D928A95B-1DDB-34D5-9F24-9AB523E4F4B0
   Functions: 4701
-  Symbols:   17463
-  CStrings:  7204
+  Symbols:   17462
+  CStrings:  7205
 
Symbols:
+ -[TVRUIButtonPanelView _disableButton:]
+ -[TVRUIButtonPanelView disableButtons]
+ -[TVRUIRemoteViewController _presentKeyboardWithAttributes:initialText:].cold.1
+ GCC_except_table23
+ GCC_except_table29
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.124
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.131
+ ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.203
+ ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.205
+ ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.176
+ ___block_literal_global.133
+ _objc_msgSend$_disableButton:
+ _objc_msgSend$disableButtons
+ _objc_msgSend$effectiveGeometry
- -[TVRUIButtonPanelView _disableButton:changeAlpha:]
- -[TVRUIButtonPanelView disableButtons:]
- -[TVRUINowPlayingController bottomSpacingRequired]
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.125
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.132
- ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.204
- ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.206
- ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.177
- ___block_literal_global.134
- _objc_msgSend$_disableButton:changeAlpha:
- _objc_msgSend$bottomSpacingRequired
- _objc_msgSend$disableButtons:
- _objc_msgSend$orientation
CStrings:
+ "%s text length: %lu"
+ "Attempting to dismiss presented content: %@"
+ "Disabled panel buttons"
+ "Found existing Keyboard view controller. This is an error."
+ "Keyboard attributes attributed"
+ "_disableButton:"
+ "disableButtons"
+ "effectiveGeometry"
- "Attempting to dismiss any presented content"
- "Disabled panel buttons. shouldChangeAlpha=%d"
- "Keyboard attributes attributed "
- "_disableButton:changeAlpha:"
- "bottomSpacingRequired"
- "disableButtons:"
- "orientation"

```
