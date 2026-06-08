## NanoMediaRemote

> `/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote`

```diff

-2023.600.2.0.0
-  __TEXT.__text: 0xa4c
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__cstring: 0x13d
-  __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x23
-  __TEXT.__objc_methname: 0x51c
-  __TEXT.__objc_methtype: 0x46
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x20
+2024.100.38.0.0
+  __TEXT.__text: 0x874
+  __TEXT.__objc_methlist: 0xa4
+  __TEXT.__cstring: 0xf5
+  __TEXT.__unwind_info: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x1f8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x198
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
-  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69EDAD7D-454E-3A61-B084-C71547699642
-  Functions: 16
-  Symbols:   120
-  CStrings:  113
+  UUID: 2C515487-F6A9-34FA-90D6-10F3394DD253
+  Functions: 11
+  Symbols:   101
+  CStrings:  36
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x22
+ _objc_retain_x3
- +[NSBundle(NanoMediaRemote) nanoMediaRemoteBundle]
- +[NSBundle(NanoMediaRemote) nanoMediaRemoteBundle].cold.1
- -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemRemotePath]
- -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemVoiceMemosPath]
- _OBJC_CLASS_$_NSBundle
- __NSConcreteGlobalBlock
- __OBJC_$_CATEGORY_CLASS_METHODS_NSBundle_$_NanoMediaRemote
- __OBJC_$_CATEGORY_NSBundle_$_NanoMediaRemote
- ___50+[NSBundle(NanoMediaRemote) nanoMediaRemoteBundle]_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_literal_global
- _dispatch_once
- _nanoMediaRemoteBundle.nanoMediaRemoteBundle
- _nanoMediaRemoteBundle.onceToken
- _objc_msgSend$bundleWithIdentifier:
- _objc_release_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
CStrings:
- ".cxx_destruct"
- "@\"NSString\""
- "@\"NSURL\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "B16@0:8"
- "NMRAppLaunchInfo"
- "NanoMediaRemote"
- "T@\"NSString\",R,N,V_bundleID"
- "T@\"NSURL\",R,N,V_URL"
- "TB,R,N,Gnmr_isSystemBooksPath"
- "TB,R,N,Gnmr_isSystemMindfulnessPath"
- "TB,R,N,Gnmr_isSystemPodcastsPath"
- "TB,R,N,Gnmr_isSystemRemotePath"
- "TB,R,N,Gnmr_isSystemVoiceMemosPath"
- "TB,R,N,Gnmr_isSystemWorkoutGuidedWalkPath"
- "TB,R,N,Gnmr_isSystemWorkoutPath"
- "URL"
- "_URL"
- "_bundleID"
- "_launchURLForScheme:requestedPlayerPath:"
- "arrayWithObjects:count:"
- "bundleWithIdentifier:"
- "com.apple.NanoMediaRemote"
- "com.apple.NanoRemote"
- "com.apple.VoiceMemos"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "designatedGroupLeaderRouteUID"
- "dictionaryWithCapacity:"
- "init"
- "initWithPlayerResponse:"
- "isDeviceRoute"
- "isEqualToString:"
- "isNativeBooksPath"
- "isNativeMusicPath"
- "isNativePodcastsPath"
- "isPhoneRoute"
- "name"
- "nanoMediaRemoteBundle"
- "nmr_isSystemBooksPath"
- "nmr_isSystemMindfulnessPath"
- "nmr_isSystemPodcastsPath"
- "nmr_isSystemRemotePath"
- "nmr_isSystemVoiceMemosPath"
- "nmr_isSystemWorkoutGuidedWalkPath"
- "nmr_isSystemWorkoutPath"
- "nmr_pathWithNowPlayingURL:"
- "nmr_systemBooksPath"
- "nmr_systemPodcastsPath"
- "nmr_systemRemotePath"
- "nmr_systemVoiceMemosPath"
- "nmr_systemWorkoutGuidedWalkPath"
- "nmr_systemWorkoutPath"
- "objectForKeyedSubscript:"
- "pathWithDeviceUID:bundleID:pid:playerID:"
- "playerPath"
- "queryItemWithName:value:"
- "queryItems"
- "representedBundleID"
- "request"
- "route"
- "setHost:"
- "setObject:forKeyedSubscript:"
- "setQueryItems:"
- "setScheme:"
- "v16@0:8"
- "v8@?0"
- "value"

```
