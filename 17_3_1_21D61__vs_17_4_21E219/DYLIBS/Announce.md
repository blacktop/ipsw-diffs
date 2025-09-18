## Announce

> `/System/Library/PrivateFrameworks/Announce.framework/Announce`

```diff

-217.30.3.0.0
-  __TEXT.__text: 0x1c620
-  __TEXT.__auth_stubs: 0xac0
+217.40.9.0.0
+  __TEXT.__text: 0x1cb88
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0x1c50
   __TEXT.__const: 0x222
-  __TEXT.__cstring: 0x3be9
+  __TEXT.__cstring: 0x3f19
   __TEXT.__oslogstring: 0xa50
   __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__swift5_typeref: 0x1c3

   __TEXT.__swift5_reflstr: 0x112
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x888
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x54f
-  __TEXT.__objc_methname: 0x44dc
+  __TEXT.__objc_methname: 0x44ee
   __TEXT.__objc_methtype: 0xe24
   __TEXT.__objc_stubs: 0x3400
   __DATA_CONST.__got: 0xb0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x34f0
   __DATA_CONST.__objc_selrefs: 0x1180
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__cfstring: 0x2d00
   __AUTH_CONST.__objc_const: 0x11c8
   __AUTH_CONST.__const: 0x508
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x200
-  __DATA.__objc_superrefs: 0xa8
   __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0x78
   __DATA.__data: 0x870

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2CA7387F-AC7C-326A-A7A2-277C96FD8E68
-  Functions: 796
-  Symbols:   2893
-  CStrings:  1919
+  UUID: BA092409-F46E-380D-9CF1-31480683D970
+  Functions: 799
+  Symbols:   2894
+  CStrings:  1937
 
Symbols:
+ ___27-[ANTonePlayerService init]_block_invoke.47
+ ___30-[ANAnnounceReachability init]_block_invoke.81
+ ___32-[ANAnnounce announcementForID:]_block_invoke.99
+ ___32-[ANAnnounceReachability _start]_block_invoke.105
+ ___33-[ANAnnounce prewarmWithHandler:]_block_invoke.115
+ ___34-[ANAnnounce homeNamesForContext:]_block_invoke.109
+ ___34-[ANAnnounce isLocalDeviceInRoom:]_block_invoke.110
+ ___35-[ANAnnounce receivedAnnouncements]_block_invoke.101
+ ___35-[ANAnnounce unplayedAnnouncements]_block_invoke.102
+ ___37-[ANAnnounce receivedAnnouncementIDs]_block_invoke.97
+ ___37-[ANAnnounce sendRequest:completion:]_block_invoke.92
+ ___37-[ANRemotePlaybackSession endSession]_block_invoke.96
+ ___38-[ANAnnounce contextFromAnnouncement:]_block_invoke.107
+ ___39-[ANLocalPlaybackSession playbackState]_block_invoke.103
+ ___41-[ANAnnounce initWithEndpointIdentifier:]_block_invoke.87
+ ___44-[ANAnnounce _sendRequestLegacy:completion:]_block_invoke.116
+ ___48-[ANAnnounce isEndpointWithUUID:inRoomWithName:]_block_invoke.112
+ ___52-[ANLocalPlaybackSession lastPlayedAnnouncementInfo]_block_invoke.89
+ ___53-[ANAnnounce isAnnounceEnabledForAnyAccessoryInHome:]_block_invoke.113
+ ___58-[ANAnnounceReachability announceReachabilityForHomeName:]_block_invoke.85
+ ___58-[ANAnnounceReachability announceReachabilityForHomeUUID:]_block_invoke.88
+ ___59-[ANAnnounce isAnnounceEnabledForAnyAccessoryOrUserInHome:]_block_invoke.114
+ ___64-[ANLocalPlaybackSession sendPlaybackCommand:completionHandler:]_block_invoke.86
+ ___69-[ANAnnounceReachability announceReachabilityForRoomName:inHomeName:]_block_invoke.87
+ ___69-[ANAnnounceReachability announceReachabilityForRoomUUID:inHomeUUID:]_block_invoke.89
+ ___71-[ANRemotePlaybackSession startSessionForGroupID:announcementsHandler:]_block_invoke.94
+ ___75-[ANAnnounce mockAnnouncement:forHomeWithName:playbackDeadline:completion:]_block_invoke.103
+ ___78-[ANTonePlayerService playTone:audioSessionID:endpointUUID:completionHandler:]_block_invoke.53
+ ___block_literal_global.106
+ ___block_literal_global.158
+ ___block_literal_global.176
+ ___block_literal_global.340
+ ___block_literal_global.49
+ ___block_literal_global.66
+ ___block_literal_global.93
+ _block_copy_helper.29
+ _block_descriptor.31
+ _block_descriptor.39
+ _block_destroy_helper.30
+ _objc_retain_x27
- ___27-[ANTonePlayerService init]_block_invoke.46
- ___30-[ANAnnounceReachability init]_block_invoke.80
- ___32-[ANAnnounce announcementForID:]_block_invoke.98
- ___32-[ANAnnounceReachability _start]_block_invoke.104
- ___33-[ANAnnounce prewarmWithHandler:]_block_invoke.114
- ___34-[ANAnnounce homeNamesForContext:]_block_invoke.108
- ___34-[ANAnnounce isLocalDeviceInRoom:]_block_invoke.109
- ___35-[ANAnnounce receivedAnnouncements]_block_invoke.100
- ___35-[ANAnnounce unplayedAnnouncements]_block_invoke.101
- ___37-[ANAnnounce receivedAnnouncementIDs]_block_invoke.96
- ___37-[ANAnnounce sendRequest:completion:]_block_invoke.91
- ___37-[ANRemotePlaybackSession endSession]_block_invoke.95
- ___38-[ANAnnounce contextFromAnnouncement:]_block_invoke.106
- ___39-[ANLocalPlaybackSession playbackState]_block_invoke.102
- ___41-[ANAnnounce initWithEndpointIdentifier:]_block_invoke.86
- ___44-[ANAnnounce _sendRequestLegacy:completion:]_block_invoke.115
- ___48-[ANAnnounce isEndpointWithUUID:inRoomWithName:]_block_invoke.111
- ___52-[ANLocalPlaybackSession lastPlayedAnnouncementInfo]_block_invoke.88
- ___53-[ANAnnounce isAnnounceEnabledForAnyAccessoryInHome:]_block_invoke.112
- ___58-[ANAnnounceReachability announceReachabilityForHomeName:]_block_invoke.84
- ___58-[ANAnnounceReachability announceReachabilityForHomeUUID:]_block_invoke.87
- ___59-[ANAnnounce isAnnounceEnabledForAnyAccessoryOrUserInHome:]_block_invoke.113
- ___64-[ANLocalPlaybackSession sendPlaybackCommand:completionHandler:]_block_invoke.85
- ___69-[ANAnnounceReachability announceReachabilityForRoomName:inHomeName:]_block_invoke.86
- ___69-[ANAnnounceReachability announceReachabilityForRoomUUID:inHomeUUID:]_block_invoke.88
- ___71-[ANRemotePlaybackSession startSessionForGroupID:announcementsHandler:]_block_invoke.93
- ___75-[ANAnnounce mockAnnouncement:forHomeWithName:playbackDeadline:completion:]_block_invoke.102
- ___78-[ANTonePlayerService playTone:audioSessionID:endpointUUID:completionHandler:]_block_invoke.52
- ___block_literal_global.105
- ___block_literal_global.157
- ___block_literal_global.175
- ___block_literal_global.339
- ___block_literal_global.48
- ___block_literal_global.65
- ___block_literal_global.92
- _block_copy_helper.30
- _block_descriptor.32
- _block_descriptor.40
- _block_destroy_helper.31
CStrings:
+ "Index out of range"
+ "Insufficient space allocated to copy string contents"
+ "Range requires lowerBound <= upperBound"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
