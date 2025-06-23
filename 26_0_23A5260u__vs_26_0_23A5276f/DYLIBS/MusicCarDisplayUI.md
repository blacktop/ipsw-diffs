## MusicCarDisplayUI

> `/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`

```diff

-4025.110.116.2.0
-  __TEXT.__text: 0x1a240
+4025.100.129.0.0
+  __TEXT.__text: 0x1a2c0
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x2248
+  __TEXT.__objc_methlist: 0x2270
   __TEXT.__cstring: 0xcbb
   __TEXT.__oslogstring: 0x260b
   __TEXT.__const: 0xaa

   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x6e0
-  __TEXT.__objc_classname: 0x3ec
-  __TEXT.__objc_methname: 0x6fa4
-  __TEXT.__objc_methtype: 0x1c13
+  __TEXT.__objc_classname: 0x40e
+  __TEXT.__objc_methname: 0x7012
+  __TEXT.__objc_methtype: 0x1c62
   __TEXT.__objc_stubs: 0x4d60
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__const: 0x970
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc8
+  __DATA_CONST.__objc_selrefs: 0x1bd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x4fa0
+  __AUTH_CONST.__objc_const: 0x4fe8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x6b8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x688
+  __DATA.__objc_ivar: 0x218
+  __DATA.__data: 0x6e8
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30DAE2AA-665E-3DF6-BF56-A22460FEF7D3
-  Functions: 646
-  Symbols:   2732
-  CStrings:  1800
+  UUID: E06E6DB6-44CC-36E0-AAB2-A561186F0832
+  Functions: 648
+  Symbols:   2734
+  CStrings:  1805
 
Symbols:
+ -[MCDNowPlayingViewController playerResponse]
+ -[MCDNowPlayingViewController setPlayerResponse:]
+ _OBJC_IVAR_$_MCDNowPlayingViewController._playerResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PlaybackQueueViewControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PlaybackQueueViewControllerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MCDPlayableContentQueueTableViewController
+ __OBJC_LABEL_PROTOCOL_$_PlaybackQueueViewControllerProtocol
+ __OBJC_PROTOCOL_$_PlaybackQueueViewControllerProtocol
+ _objc_msgSend$initWithImage:style:target:action:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MusicCarDisplayUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MusicCarDisplayUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MusicCarDisplayUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MusicCarDisplayUI
- _objc_msgSend$setImage:forState:
Functions:
~ -[MCDNowPlayingViewController viewDidLoad] : 1944 -> 1932
~ -[MCDNowPlayingViewController contentManager:processResponse:error:] : 504 -> 588
+ -[MCDNowPlayingViewController setActivityIndicatorBarButtonItem:]
+ -[MCDNowPlayingViewController appName]
~ -[MCDNowPlayingViewController .cxx_destruct] : 264 -> 284
CStrings:
+ "@\"UITableViewController<PlaybackQueueViewControllerProtocol>\""
+ "PlaybackQueueViewControllerProtocol"
+ "T@\"MPCPlayerResponse\",&,N,V_playerResponse"
+ "T@\"UITableViewController<PlaybackQueueViewControllerProtocol>\",&,N,V_playbackQueueViewController"
+ "_playerResponse"
+ "initWithImage:style:target:action:"
+ "playerResponse"
+ "setPlayerResponse:"
+ "v32@0:8@\"MPCPlayerResponse\"16@\"NSError\"24"
- "@\"UITableViewController\""
- "T@\"UITableViewController\",&,N,V_playbackQueueViewController"
- "nowPlayingViewControllerWillAppear:"
- "setImage:forState:"

```
