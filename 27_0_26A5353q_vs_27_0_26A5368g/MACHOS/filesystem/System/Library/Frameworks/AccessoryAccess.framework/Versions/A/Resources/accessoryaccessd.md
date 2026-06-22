## accessoryaccessd

> `/System/Library/Frameworks/AccessoryAccess.framework/Versions/A/Resources/accessoryaccessd`

```diff

-301.0.4.0.0
-  __TEXT.__text: 0x36c08 sha256:745312719f16d16003ba13db5e9e7a1e8d4df8a96c33cc13606ddea477830147
-  __TEXT.__auth_stubs: 0xd90 sha256:2ab74265c42e2124d01068eae492956531b1b2e380a90b43c58c29e463a6adf3
-  __TEXT.__objc_stubs: 0x260 sha256:730c18caefeb342df3928eb83b36de2819a92d9a31745fbf9a5f124f5987b969
-  __TEXT.__const: 0x3f80 sha256:4a29b802c524b8ed2183148674de6ce919172b660e72431afcb097aa9fc591ad
-  __TEXT.__gcc_except_tab: 0x408c sha256:303fb5a1ade0e8dc95f989b9239e3ee3906305130967c76a55041de30570e644
+304.0.1.0.0
+  __TEXT.__text: 0x3636c sha256:1c1c2f8ec4b49171df6fb607704f2f6cac951b4cc7a9468ba4986dc35122888b
+  __TEXT.__auth_stubs: 0xdd0 sha256:d7d099092c003e2eed733cf8390c5dab866c119195b6c887d7c5b1913faa7527
+  __TEXT.__objc_stubs: 0x240 sha256:9dbbdfd5294a4c1d0b9319f11a03f348880201ce5df92e0474c085696eb29664
+  __TEXT.__const: 0x3fe0 sha256:11cdf6244db6acb2bf5587b3ef1ef13ac22dd17ada083d9e7c86f9d90282343a
+  __TEXT.__gcc_except_tab: 0x3fe0 sha256:9066ca32ddd1a4b771fc3f1838629ecc168f61706324103821859c5051ba73c1
   __TEXT.__cstring: 0xf5c sha256:f8bed4ca34543f9917eb4cdbe26275f31a615d8d12dd77194038ba24ba2cff47
-  __TEXT.__oslogstring: 0x98c sha256:607e36079e158e47fc1864843eb727cebed1b2ad157b775ed24b780cf790507c
-  __TEXT.__objc_methname: 0x176 sha256:54f8400d2170df2051451293e5caa1b7b071494c219586375df7faaed2b0c585
-  __TEXT.__unwind_info: 0x1488 sha256:c10bf9758445e5a6bbde76176f86fc378f5046b0d379653948f5fcb5f522b2cb
-  __DATA_CONST.__const: 0xeb0 sha256:d6ef84235970eb25a0a39c9417de73f8d4bcac4688e47b3fc4ab06d47531d0f7
-  __DATA_CONST.__cfstring: 0x120 sha256:39bd92da2c4ec359dc184b11fc12374a0b873f5afd9e9d3673f9fb94f7842997
+  __TEXT.__oslogstring: 0x98f sha256:ad4cad6fa853e4fea0f0369631536bf7f3bb4a222449f5188a32cea8287c195d
+  __TEXT.__objc_methname: 0x15c sha256:60597d0782bbc42a0acc8ed40da26e99eb66f67a3a1d1bf78d25b2246b5e6c9d
+  __TEXT.__unwind_info: 0x1468 sha256:d4900bfe5de49338baa92e2bbcf6c5cdccaea700f0e9b45d64813d32d4fe6d07
+  __DATA_CONST.__const: 0xec8 sha256:9554132fc131614999fb1707db3a6356d58c2458ddf79e65bac5fa36edbb6f5a
+  __DATA_CONST.__cfstring: 0x120 sha256:d9e33d2eb61bd26539376f46567acdc247f889a99d9b43bf79918f71faa32e35
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0x6d8 sha256:08bc30ea3a7b5d972f6c683349b443abf4c8bf17040995068b691d1fd0239ca9
-  __DATA_CONST.__got: 0x1e8 sha256:d6215f4eaaef701a8fac9c22e7df02f02d7c308a5f24f4f1953d6e559b4adc4a
-  __DATA.__objc_selrefs: 0x98 sha256:3b8c94969710d794f891a079f5536334b400c53390f6ec6974139fdfbe291a53
+  __DATA_CONST.__auth_got: 0x6f8 sha256:a5e4237daf35092d18f7287fda2ee2ccd7d8ed1f3acdb4049c07a7af4a438009
+  __DATA_CONST.__got: 0x1f0 sha256:21605efb5a78168bcdfd691c66872334e19e4747b188d5f22cf5f7fe73921974
+  __DATA.__objc_selrefs: 0x90 sha256:ca3ad254dc83126365fb8985550018d3885496c040e7f7ec57f0407625cd2cc7
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x54 sha256:4fea5e6a3ec5f5474a26d858bc77b6d7bd3ab864ea02d988683fdc648602b248
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC5B9BE5-0A0D-303A-BE11-9388687AC264
-  Functions: 611
-  Symbols:   292
-  CStrings:  210
+  UUID: 389A72AE-E9B3-38AD-AD3A-E4E8C5C35BDE
+  Functions: 613
+  Symbols:   297
+  CStrings:  209
 
Symbols:
+ _IOUSBGetNextAssociatedDescriptorWithType
+ __dispatch_source_type_signal
+ __exit
+ _dispatch_activate
+ _signal
CStrings:
+ "Configuration descriptor wTotalLength %u is invalid (descriptor data size: %zu)"
- "Failed to reset USB device configuration. Error code: %ld, Error message: %@"
- "configureWithValue:error:"

```
