## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-496.50.7.0.0
-  __TEXT.__text: 0xc56e0
+496.60.3.0.0
+  __TEXT.__text: 0xc58fc
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0xa760
-  __TEXT.__const: 0x2444
-  __TEXT.__gcc_except_tab: 0x1a1c
-  __TEXT.__cstring: 0x68ea
+  __TEXT.__objc_methlist: 0xa79c
+  __TEXT.__const: 0x2464
+  __TEXT.__gcc_except_tab: 0x1a3c
+  __TEXT.__cstring: 0x68da
   __TEXT.__oslogstring: 0x5712
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x4e

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x28d8
+  __TEXT.__unwind_info: 0x28f0
   __TEXT.__eh_frame: 0x8b8
   __TEXT.__objc_classname: 0x133f
-  __TEXT.__objc_methname: 0x196c1
-  __TEXT.__objc_methtype: 0x42e7
-  __TEXT.__objc_stubs: 0x11e60
+  __TEXT.__objc_methname: 0x197af
+  __TEXT.__objc_methtype: 0x4323
+  __TEXT.__objc_stubs: 0x11ee0
   __DATA_CONST.__got: 0xd00
-  __DATA_CONST.__const: 0x1620
+  __DATA_CONST.__const: 0x1648
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61f8
+  __DATA_CONST.__objc_selrefs: 0x6228
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0xd10
-  __AUTH_CONST.__const: 0x2ea8
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x13660
+  __AUTH_CONST.__const: 0x2e88
+  __AUTH_CONST.__cfstring: 0x3540
+  __AUTH_CONST.__objc_const: 0x136a0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x6538
   __AUTH.__data: 0x578
-  __DATA.__objc_ivar: 0xa4c
-  __DATA.__data: 0x24b8
+  __DATA.__objc_ivar: 0xa50
+  __DATA.__data: 0x2498
   __DATA.__bss: 0x2658
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x7d0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D16DC36E-CEEA-3807-BA6A-5EDBD4BE7579
-  Functions: 4449
-  Symbols:   16634
-  CStrings:  6795
+  UUID: 0B30E2E7-4392-3DBD-AF9B-B5D5CE283590
+  Functions: 4453
+  Symbols:   16648
+  CStrings:  6801
 
Symbols:
+ -[TVRUIUpNextViewController _confirmOkToPlayUpNextInfo:withHandler:]
+ -[TVRUIUpNextViewController isCurrentlyPlayingMedia]
+ -[TVRUIUpNextViewController nowPlayingProvider]
+ -[TVRUIUpNextViewController playItem:animated:]
+ -[TVRUIUpNextViewController setNowPlayingProvider:]
+ -[_TVRUIUpNextHorizontalCell actionButtonTapped]
+ GCC_except_table107
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table92
+ _OBJC_IVAR_$_TVRUIUpNextViewController._nowPlayingProvider
+ ___31-[_TVRUIUpNextCell _actionMenu]_block_invoke.409
+ ___31-[_TVRUIUpNextCell _actionMenu]_block_invoke_2.411
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke.68
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke_2
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke_2.69
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke_2.cold.1
+ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke_3
+ ___block_descriptor_41_e8_32w_e18_v16?0"UIAction"8lw32l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e24_v16?0?<v?"NSArray">8ls32l8s40l8w64l8s48l8s56l8
+ ___block_literal_global.360
+ _objc_msgSend$_confirmOkToPlayUpNextInfo:withHandler:
+ _objc_msgSend$indexPathForItemIdentifier:
+ _objc_msgSend$nowPlayingProvider
+ _objc_msgSend$playItem:animated:
+ _objc_msgSend$setNowPlayingProvider:
- -[TVRUIUpNextViewController playItem:]
- -[_TVRUIUpNextHorizontalCell actionButtonTapped:]
- GCC_except_table102
- GCC_except_table151
- GCC_except_table152
- GCC_except_table175
- GCC_except_table87
- ___31-[_TVRUIUpNextCell _actionMenu]_block_invoke.398
- ___31-[_TVRUIUpNextCell _actionMenu]_block_invoke_2.400
- ___38-[TVRUIUpNextViewController playItem:]_block_invoke
- ___38-[TVRUIUpNextViewController playItem:]_block_invoke.cold.1
- ___41-[_TVRUIUpNextHorizontalCell _actionMenu]_block_invoke_14
- ___69-[TVRUIUpNextViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_2
- ___69-[TVRUIUpNextViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_3
- ___69-[TVRUIUpNextViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_4
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e24_v16?0?<v?"NSArray">8ls32l8s40l8w72l8s48l8s56l8s64l8
- ___block_literal_global.349
- ___block_literal_global.570
- _objc_msgSend$playItem:
CStrings:
+ "@\"<TVRUINowPlayingProviding>\""
+ "T@\"<TVRUINowPlayingProviding>\",W,N,V_nowPlayingProvider"
+ "_confirmOkToPlayUpNextInfo:withHandler:"
+ "_nowPlayingProvider"
+ "actionButtonTapped"
+ "indexPathForItemIdentifier:"
+ "isCurrentlyPlayingMedia"
+ "nowPlayingProvider"
+ "playItem:animated:"
+ "setNowPlayingProvider:"
+ "v28@0:8@\"TVRCUpNextInfo\"16B24"
- "TVRUIPlay"
- "play.tv"
- "playItem:"

```
