## PodcastsKit

> `/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit`

```diff

-4025.110.94.1.0
-  __TEXT.__text: 0x2b31c
-  __TEXT.__auth_stubs: 0x11a0
+4025.100.100.0.0
+  __TEXT.__text: 0x2b36c
+  __TEXT.__auth_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x2644
   __TEXT.__const: 0x956
   __TEXT.__gcc_except_tab: 0x4c8
-  __TEXT.__cstring: 0x20fe
+  __TEXT.__cstring: 0x214e
   __TEXT.__oslogstring: 0x135a
   __TEXT.__ustring: 0x20
-  __TEXT.__swift5_typeref: 0x5e4
+  __TEXT.__swift5_typeref: 0x5e6
   __TEXT.__swift5_reflstr: 0x2fa
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x77c

   __TEXT.__swift5_protos: 0x10
   __TEXT.__unwind_info: 0xd50
   __TEXT.__objc_classname: 0x440
-  __TEXT.__objc_methname: 0x6e32
-  __TEXT.__objc_methtype: 0xdd0
+  __TEXT.__objc_methname: 0x6e40
+  __TEXT.__objc_methtype: 0xdd3
   __TEXT.__objc_stubs: 0x46c0
   __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__const: 0xac8
+  __DATA_CONST.__const: 0xad8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__auth_got: 0x8f0
   __AUTH_CONST.__const: 0xf18
-  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__cfstring: 0x1240
   __AUTH_CONST.__objc_const: 0x4630
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B6D03565-6CE3-387E-80AC-3C91162CE8D7
+  UUID: 87C45873-2F47-3A1D-96B9-DB4718F81698
   Functions: 1319
-  Symbols:   3288
-  CStrings:  1876
+  Symbols:   3292
+  CStrings:  1888
 
Symbols:
+ +[POUtilities createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:isSiriRequest:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:]
+ _MRSystemAppPlaybackQueueSetFeatureName
+ ___block_literal_global.105
+ _kSetPlaybackQueueControlCenterFeatureName
+ _kSetPlaybackQueueSiriFeatureName
+ _objc_msgSend$createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:isSiriRequest:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:
+ _objc_retain_x6
+ _symbolic Igh_
- +[POUtilities createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:]
- ___block_literal_global.99
- _objc_msgSend$createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:
- _symbolic Ig_
Functions:
~ +[POUtilities performPodcastsPlaybackRequestWithIdentifier:assetInfo:hashedRouteUIDs:decodedRouteUIDs:originatingOutputDeviceUID:startPlaying:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:context:allowsFallback:completion:] : 1264 -> 1276
~ ___237+[POUtilities performPodcastsPlaybackRequestWithIdentifier:assetInfo:hashedRouteUIDs:decodedRouteUIDs:originatingOutputDeviceUID:startPlaying:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:context:allowsFallback:completion:]_block_invoke.23 : 1364 -> 1372
~ +[POUtilities createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:] -> +[POUtilities createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:isSiriRequest:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:] : 300 -> 328
~ +[MTExtensionPlaybackController playbackQueueForIdentifier:startPlayback:assetInfo:] : 248 -> 280
CStrings:
+ "?"
+ "@\"PKEpisode\""
+ "@\"PKEpisodeStoreId\""
+ "@\"PKShow\""
+ "@\"PKShowStoreId\""
+ "^{_MRSystemAppPlaybackQueue=}56@0:8@16B24@28B36@40@48"
+ "createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:isSiriRequest:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:"
+ "d"
+ "f"
+ "iosControlCenter"
+ "siri"
- "^{_MRSystemAppPlaybackQueue=}52@0:8@16B24@28@36@44"
- "createPlaybackQueueFromRequestIdentifiers:startPlaying:assetInfo:requesterSharedUserId:sharedUserIdFromPlayableITunesAccount:"

```
