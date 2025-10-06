## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-680.3.1.0.0
-  __TEXT.__text: 0x2f0ac
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x2b58
+680.5.1.0.0
+  __TEXT.__text: 0x2f4b4
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x2b68
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x46e9
-  __TEXT.__cstring: 0x58c7
-  __TEXT.__unwind_info: 0x980
+  __TEXT.__oslogstring: 0x483b
+  __TEXT.__cstring: 0x5960
+  __TEXT.__unwind_info: 0x988
   __TEXT.__objc_classname: 0x6d9
-  __TEXT.__objc_methname: 0x7cb5
+  __TEXT.__objc_methname: 0x7cc6
   __TEXT.__objc_methtype: 0x1adb
-  __TEXT.__objc_stubs: 0x54c0
-  __DATA_CONST.__got: 0x478
+  __TEXT.__objc_stubs: 0x54e0
+  __DATA_CONST.__got: 0x480
   __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1ce8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x550
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x9f8
-  __AUTH_CONST.__cfstring: 0x1740
+  __AUTH_CONST.__cfstring: 0x1780
   __AUTH_CONST.__objc_const: 0x5c90
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27F2DCC6-7544-32D4-A556-781A90BD6946
-  Functions: 1130
-  Symbols:   4117
-  CStrings:  2515
+  UUID: 4A66AB80-5E81-360F-AC83-00AE0FECB8D2
+  Functions: 1131
+  Symbols:   4125
+  CStrings:  2528
 
Symbols:
+ -[RPControlCenterClient getHqlrAudioOnly]
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _CFPreferencesAppSynchronize
+ _CFPreferencesSetAppValue
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.104
+ ___38-[RPControlCenterClient setCountdown:]_block_invoke.107
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.118
+ ___42-[RPControlCenterClient updateCallActive:]_block_invoke.119
+ ___42-[RPControlCenterClient updateClientState]_block_invoke.92
+ ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke.71
+ ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke.70
+ ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke.51
+ ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke.49
+ ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke.48
+ ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke.73
+ ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke.77
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.125
+ ___block_literal_global.75
+ ___block_literal_global.79
+ _kCFBooleanTrue
+ _objc_msgSend$getHqlrAudioOnly
- ___38-[RPControlCenterClient setCountdown:]_block_invoke.95
- ___38-[RPControlCenterClient setCountdown:]_block_invoke.98
- ___42-[RPControlCenterClient updateCallActive:]_block_invoke.109
- ___42-[RPControlCenterClient updateCallActive:]_block_invoke.110
- ___42-[RPControlCenterClient updateClientState]_block_invoke.83
- ___44-[RPControlCenterClient stopCurrentSession:]_block_invoke.62
- ___46-[RPControlCenterClient startHQLRWithHandler:]_block_invoke.61
- ___51-[RPControlCenterClient startBroadcastWithHandler:]_block_invoke.42
- ___51-[RPControlCenterClient startRecordingWithHandler:]_block_invoke.40
- ___52-[RPControlCenterClient notifyClientDelegatesStart:]_block_invoke.39
- ___54-[RPControlCenterClient stopHQLRRecordingWithHandler:]_block_invoke.64
- ___56-[RPControlCenterClient stopSystemRecordingWithHandler:]_block_invoke.68
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.116
- ___block_literal_global.66
- ___block_literal_global.70
- ___block_literal_global.97
CStrings:
+ " [INFO] %{public}s:%d Found audio only location: %d"
+ " [INFO] %{public}s:%d Getting audio only value"
+ " [INFO] %{public}s:%d Posted Darwin notification for audio only change"
+ " [INFO] %{public}s:%d Removed RPHQLRAudioOnly key from preferences"
+ " [INFO] %{public}s:%d Set RPHQLRAudioOnly to true"
+ " [INFO] %{public}s:%d Setting audio only value: %d"
+ "-[RPControlCenterClient getHqlrAudioOnly]"
+ "-[RPControlCenterClient setHqlrAudioOnly:]"
+ "RPAudioOnlySelection"
+ "com.apple.replaykit.audioOnlyPreferenceChanged"
+ "getHqlrAudioOnly"

```
