## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-515.22.0.0.0
-  __TEXT.__text: 0x11bce4
+515.26.0.0.0
+  __TEXT.__text: 0x11c528
   __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0xa44c
+  __TEXT.__objc_methlist: 0xa474
   __TEXT.__const: 0xd64
-  __TEXT.__cstring: 0x1d1d
-  __TEXT.__oslogstring: 0x2b85
-  __TEXT.__gcc_except_tab: 0x245c
+  __TEXT.__cstring: 0x1d3d
+  __TEXT.__oslogstring: 0x2bb1
+  __TEXT.__gcc_except_tab: 0x2520
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x4fc
   __TEXT.__swift5_typeref: 0x111a

   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__unwind_info: 0x1d18
   __TEXT.__objc_classname: 0x17be
-  __TEXT.__objc_methname: 0x1d282
+  __TEXT.__objc_methname: 0x1d3ca
   __TEXT.__objc_methtype: 0x52a4
-  __TEXT.__objc_stubs: 0x13da0
+  __TEXT.__objc_stubs: 0x13e60
   __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x2d08
+  __DATA_CONST.__const: 0x2d30
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6560
+  __DATA_CONST.__objc_selrefs: 0x6588
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x9c0
   __AUTH_CONST.__const: 0x978
   __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x1ed98
+  __AUTH_CONST.__objc_const: 0x1edc8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2c60
   __AUTH.__data: 0x278
-  __DATA.__objc_ivar: 0xa2c
+  __DATA.__objc_ivar: 0xa30
   __DATA.__data: 0x2988
   __DATA.__bss: 0x600
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 357D0D3E-50B3-386B-8385-2E1A1CCEC104
-  Functions: 3694
-  Symbols:   14760
-  CStrings:  6056
+  UUID: B06137B1-891E-38B6-ACA0-671370D1B840
+  Functions: 3699
+  Symbols:   14779
+  CStrings:  6065
 
Symbols:
+ -[CPSAudioPlaybackManager setVideoPlaybackStateQueue:]
+ -[CPSAudioPlaybackManager videoPlaybackStateQueue]
+ -[CPSEmptyView _updateArrangedSubview:forTextVariants:]
+ GCC_except_table55
+ _OBJC_IVAR_$_CPSAudioPlaybackManager._videoPlaybackStateQueue
+ ___63-[CPSAudioPlaybackManager nowPlayingManager:didUpdateSnapshot:]_block_invoke
+ ___63-[CPSAudioPlaybackManager nowPlayingManager:didUpdateSnapshot:]_block_invoke.174
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ _objc_msgSend$_updateArrangedSubview:forTextVariants:
+ _objc_msgSend$accessorySymbolCustomSymbolImage
+ _objc_msgSend$initWithId:title:subtitle:image:imageShape:accessorySystemImage:accessorySymbolCustomSymbolImage:allowsTouches:disabledAppearance:action:
+ _objc_msgSend$instrumentClusterControllerConnection
+ _objc_msgSend$videoPlaybackState
+ _objc_msgSend$videoPlaybackStateQueue
CStrings:
+ "$&"
+ "New video playback state %ld, old state %ld"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_videoPlaybackStateQueue"
+ "_updateArrangedSubview:forTextVariants:"
+ "_videoPlaybackStateQueue"
+ "accessorySymbolCustomSymbolImage"
+ "com.apple.CarPlaySupport.videoPlaybackState"
+ "initWithId:title:subtitle:image:imageShape:accessorySystemImage:accessorySymbolCustomSymbolImage:allowsTouches:disabledAppearance:action:"
+ "setVideoPlaybackStateQueue:"
+ "videoPlaybackStateQueue"
- "$%"

```
