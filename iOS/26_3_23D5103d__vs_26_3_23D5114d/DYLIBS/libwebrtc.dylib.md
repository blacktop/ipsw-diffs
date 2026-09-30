## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-623.2.4.0.0
-  __TEXT.__text: 0xad5c28
+623.2.7.0.0
+  __TEXT.__text: 0xad5d94
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xad558
   __TEXT.__cstring: 0x4e9ab
   __TEXT.__gcc_except_tab: 0x1890
-  __TEXT.__unwind_info: 0x28d8
+  __TEXT.__unwind_info: 0x28e0
   __TEXT.__eh_frame: 0xf70
   __TEXT.__objc_classname: 0x45a
   __TEXT.__objc_methname: 0x25aa

   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__bss: 0x2098
   __DATA_DIRTY.__common: 0x30
+  .note.gnu.proper."a": 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8332FC81-335D-377F-94D1-1D9234CD69F0
-  Functions: 18483
-  Symbols:   45280
+  UUID: F2D43B0F-ACC8-3D0B-A30D-5BCA143A6606
+  Functions: 18484
+  Symbols:   45282
   CStrings:  9808
 
Symbols:
+ _set_tile_limits
Functions:
~ _bn_mul_mont_words : 576 -> 608
~ __bn_mul4x_mont : 1600 -> 1616
~ _bn_sub_words : 80 -> 96
~ _ChaCha20_ctr32_nohw : 896 -> 928
~ ChaCha20_512_neon : 4416 -> 4448
~ _chacha20_poly1305_open : 5136 -> 5152
~ gcm_ghash_v8_4x : 944 -> 928
~ _vp9_change_config : 3708 -> 3516
~ _update_frame_size : 616 -> 432
+ _set_tile_limits
~ _create_enc_workers : 1224 -> 1388

```
