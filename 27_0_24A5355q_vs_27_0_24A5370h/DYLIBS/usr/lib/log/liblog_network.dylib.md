## liblog_network.dylib

> `/usr/lib/log/liblog_network.dylib`

```diff

-6681.0.372.502.1
-  __TEXT.__text: 0x17c0 sha256:40f60a1025ccfc298f36861400b4c3a276dfac75ccf1ecd185691491220345d3
-  __TEXT.__const: 0x58 sha256:8ee69944b25c7ebfb7003a3bd61cf26b9a4922161d8532db2664886bbba0abb8
+6681.0.436.0.8
+  __TEXT.__text: 0x17a8 sha256:4c0f4e60354777c6b4dbe75b25f248f1ca49e56ec120757b08b98632251c2357
+  __TEXT.__const: 0x50 sha256:0fa624be5c028650b67a569559ae1e6195efd1d217a986236f0228317f58b821
   __TEXT.__cstring: 0x2f7 sha256:94ef7f4f90389e72e1cd2cdbaf9666e014bb851dbcf4f1cc30b77a173f9808df
   __TEXT.__gcc_except_tab: 0x54 sha256:cf4e6809f24068aaaf5429ed7b01275b36292e6074d8bc54633ff5d542033293
-  __TEXT.__unwind_info: 0xb0 sha256:a2d63bab3deb1d060a1acc15b130c233dc2c3ffb80db11498e745befc86a62a9
+  __TEXT.__unwind_info: 0xa8 sha256:baa24488c3d315a29b2e583797933dac0bc3444f7a2f5bf987b8b920f666bdaa
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0xe0 sha256:3ae0269214f301c076d6f4d9c0f44930348b80881eb6af5deec16a910763c413
+  __DATA_CONST.__const: 0xe0 sha256:a0a5fd2b53167b31b98103333150048d23c10520c9082a901ceac75b5177ae13
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x60 sha256:6f88f0089bdce4acd75bdb5685e3b04c4a3918e17dca6026e2288bcca84d538d
+  __DATA_CONST.__objc_selrefs: 0x60 sha256:24e075fdbdbe251150e8835de82d57dd60bdc7afcc2986894f5e443f48820a81
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x80 sha256:fe8dc466f837c02ef17c2ca231759f12904dbc270c17e310207ba447d38b54ba
-  __AUTH_CONST.__cfstring: 0x380 sha256:ef4ecade626dd879425767d12a820d86f8db67a283cd3713514a5fbebe22c3b0
+  __AUTH_CONST.__const: 0x80 sha256:852fe1d29f0aef50762fad9027b37014547c6335567d5d36585f8647c8717ea8
+  __AUTH_CONST.__cfstring: 0x380 sha256:a5a0ba8788ac793e4eab4ee53abe8340678a891bc3fc634b3878d26a36a93d8a
   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libquic.dylib
-  UUID: 3B0CFE84-08D3-35F0-8229-300506FE9138
+  UUID: 2078CCC8-F825-34A8-95E1-B2A7A8D61803
   Functions: 13
   Symbols:   85
   CStrings:  90
Functions:
~ _OSLogCopyFormattedString : sha256 464f77a7354c292601dc699fb160d71b385c463ba557d32de9afe4e8efd39ff2 -> c11074516ae2d0494d27a2a6ec47c2763eba9c3527bc1c4aab8c8dffdfeeffb5
~ _NWOLCopyFormattedStringIPv4Address -> _NWOLCopyFormattedStringSockaddr : 592 -> 1412
~ _NWOLCopyFormattedStringIPv6Address -> _NWOLCopyFormattedStringIPv4Address : 512 -> 592
~ _NWOLCopyFormattedStringSockaddr -> _NWOLCopyFormattedStringIPv6Address : 1416 -> 512
~ _NWOLCopyFormattedStringTCPFlags : sha256 2cd8b21822b012483f08b2b81cc2ea343220d53ff4ee35c593946e4c1c778264 -> 04cde1d6f0facb2f71b8412ab4ca44382f213b78b8d7aa352d1413bf70d9f8a8
~ _NWOLCopyFormattedStringTCPState : sha256 805d2b95002676f3984c98317e769ca04fd0f973b3b2b5a79a1c2670010a3ba6 -> 2e168ebafca248cf97fa119bcaaf42c2aee1e341c05d6c77aef0a6d4124eee1f
~ _NWOLCopyFormattedStringTCPPackets : sha256 9d23e74482167624fb8d43b13aa4e5f5b1c64b097cbb22294a4b5e047b0a0c40 -> 4159a271c3d2f1030d1d7fee0637684e68fea36a9041a855e6c4a3d80a91b3ac
~ _NWOLCopyFormattedStringQUICPackets : sha256 63565bbfa07dffce26c97b9a46ec93a3ba77d4c14d1c7fae90f3a8634c288c22 -> a3207f666416b45a7b9a182a48250bb17025c565ad221b79190b57c9406e1169
~ _NWOLCopyFormattedStringData : 700 -> 688
~ ___Block_byref_object_dispose_ : sha256 7aaa94e2dcd72aeebe18d071ca35f57ac5863e4a81f14ecab594b193bfa64c69 -> af05104621dd89ba6b6a1a033e1fd5b3411a8202df264b53bacb8db3d023bbd4
~ ___NWOLCopyFormattedStringTCPPackets_block_invoke : 612 -> 604
~ ___NWOLCopyFormattedStringQUICPackets_block_invoke : sha256 edba7aa39e3dd2da4a7212b255e45c35960ed8986642488ee48d31567d4ce45f -> 2a0ba14deda9a0670772a98e5694381be610cf31bfa1a3b25c217e3160d84858

```
