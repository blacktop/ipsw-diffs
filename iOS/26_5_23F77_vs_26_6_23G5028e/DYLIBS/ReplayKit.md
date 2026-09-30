## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-710.1.1.0.0
-  __TEXT.__text: 0x30540
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x2bb8
+720.1.1.0.0
+  __TEXT.__text: 0x30954
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x2be8
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x4d92
-  __TEXT.__cstring: 0x5b21
-  __TEXT.__unwind_info: 0xb38
+  __TEXT.__oslogstring: 0x4d72
+  __TEXT.__cstring: 0x5b87
+  __TEXT.__unwind_info: 0xb40
   __TEXT.__objc_classname: 0x6db
-  __TEXT.__objc_methname: 0x7d92
-  __TEXT.__objc_methtype: 0x1adb
-  __TEXT.__objc_stubs: 0x5580
-  __DATA_CONST.__got: 0x480
+  __TEXT.__objc_methname: 0x7e89
+  __TEXT.__objc_methtype: 0x1af0
+  __TEXT.__objc_stubs: 0x5620
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d08
+  __DATA_CONST.__objc_selrefs: 0x1d30
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x9f8
-  __AUTH_CONST.__cfstring: 0x17a0
-  __AUTH_CONST.__objc_const: 0x5cf0
+  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__objc_const: 0x5d20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_ivar: 0x298
   __DATA.__data: 0xb48
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6489DB36-DDDD-3763-BD6D-750BCE0E15FB
-  Functions: 1164
-  Symbols:   4247
-  CStrings:  2565
+  UUID: FB568C54-E2B9-3313-805F-2F8765452203
+  Functions: 1171
+  Symbols:   4267
+  CStrings:  2576
 
Symbols:
+ -[RPControlCenterClient cacheImageIfNeededForBundleID:extensionInfo:]
+ -[RPControlCenterClient cameraRollImageData]
+ -[RPControlCenterClient loadImagesForAvailableExtensionsWithHandler:]
+ -[RPControlCenterClient setCameraRollImageData:]
+ _OBJC_CLASS_$_NSCache
+ _OBJC_IVAR_$_RPControlCenterClient._cameraRollImageData
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.108
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.111
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.122
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.123
+ ___42-[RPControlCenterClient updateClientState]_block_invoke.96
+ ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke.75
+ ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke.74
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke.54
+ ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke.52
+ ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke.51
+ ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke.77
+ ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke.81
+ ___60-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke.31
+ ___60-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke.34
+ ___69-[RPControlCenterClient loadImagesForAvailableExtensionsWithHandler:]_block_invoke
+ ___block_literal_global.110
+ ___block_literal_global.113
+ ___block_literal_global.127
+ ___block_literal_global.129
+ ___block_literal_global.83
+ _objc_msgSend$_applicationIconImageForBundleIdentifier:format:scale:
+ _objc_msgSend$cacheImageIfNeededForBundleID:extensionInfo:
+ _objc_msgSend$cameraRollImageData
+ _objc_msgSend$loadImagesForAvailableExtensionsWithHandler:
+ _objc_msgSend$setCameraRollImageData:
- ___38-[RPControlCenterClient setCountdown:]_block_invoke.104
- ___38-[RPControlCenterClient setCountdown:]_block_invoke.107
- ___42-[RPControlCenterClient updateCallActive:]_block_invoke.118
- ___42-[RPControlCenterClient updateCallActive:]_block_invoke.119
- ___42-[RPControlCenterClient updateClientState]_block_invoke.92
- ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke.71
- ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke.70
- ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke.51
- ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke.49
- ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke.48
- ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke.73
- ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke.77
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.75
- _objc_opt_new
CStrings:
+ " [INFO] %{public}s:%d %p get cached availableExtensions, pre-loading images"
+ "-[RPControlCenterClient loadAvailableExtensionsWithHandler:]_block_invoke_2"
+ "@\"NSCache\""
+ "@\"NSData\""
+ "T@\"NSData\",&,N,V_cameraRollImageData"
+ "_applicationIconImageForBundleIdentifier:format:scale:"
+ "_cameraRollImageData"
+ "cacheImageIfNeededForBundleID:extensionInfo:"
+ "cameraRollImageData"
+ "com.apple.mobileslideshow"
+ "loadImagesForAvailableExtensionsWithHandler:"
+ "setCameraRollImageData:"
- " [INFO] %{public}s:%d %p get cached availableExtensions"
- " [INFO] %{public}s:%d image not found for extension"

```
