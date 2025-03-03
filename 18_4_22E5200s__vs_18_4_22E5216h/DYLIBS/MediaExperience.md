## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-230.12.1.11.2
-  __TEXT.__text: 0x2777a8
-  __TEXT.__auth_stubs: 0x1f60
-  __TEXT.__objc_methlist: 0x4d9c
-  __TEXT.__cstring: 0x3c909
+230.15.2.11.1
+  __TEXT.__text: 0x276ed0
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_methlist: 0x4d44
+  __TEXT.__cstring: 0x3c7e1
   __TEXT.__const: 0x1af8
   __TEXT.__gcc_except_tab: 0x24e0
-  __TEXT.__oslogstring: 0x5b8ed
+  __TEXT.__oslogstring: 0x5b772
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4720
-  __TEXT.__objc_classname: 0x51c
-  __TEXT.__objc_methname: 0x12a62
-  __TEXT.__objc_methtype: 0x1c97
-  __TEXT.__objc_stubs: 0xb740
+  __TEXT.__unwind_info: 0x46f0
+  __TEXT.__objc_classname: 0x506
+  __TEXT.__objc_methname: 0x12991
+  __TEXT.__objc_methtype: 0x1c88
+  __TEXT.__objc_stubs: 0xb6e0
   __DATA_CONST.__got: 0xa18
-  __DATA_CONST.__const: 0x6538
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3378
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x3368
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xfc8
+  __AUTH_CONST.__auth_got: 0xfc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3b58
-  __AUTH_CONST.__cfstring: 0x17b60
-  __AUTH_CONST.__objc_const: 0x75e8
+  __AUTH_CONST.__const: 0x3b18
+  __AUTH_CONST.__cfstring: 0x17b20
+  __AUTH_CONST.__objc_const: 0x74d8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x550
+  __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x760
+  __DATA.__objc_ivar: 0x754
   __DATA.__data: 0xf24
-  __DATA.__bss: 0x17d8
+  __DATA.__bss: 0x17c0
   __DATA.__common: 0x5a0
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x310
+  __DATA_DIRTY.__bss: 0x308
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6873
-  Symbols:   9893
-  CStrings:  14078
+  Functions: 6860
+  Symbols:   9879
+  CStrings:  14061
 
Symbols:
- _AudioServicesPlaySystemSoundWithCompletion
CStrings:
+ "-CMSM_IDSConnection- %s: Gizmo playing info has been received already!"
+ "-MXNowPlayingAppManager- %s: Pushing displayID='%{public}@' to NowPlayingAppStack, existing size = %lu, new size = %lu"
+ "-MXSessionManagerUtilities- %s: No DisplayID provided!"
+ "-MXSessionManagerUtilities- %s: We don't want to play a chime if session is not doing IO."
+ "-PVM- %s: Failed to save endpoint type"
+ "-[MXNowPlayingAppManager pushToNowPlayingAppStack:]"
+ "-[MXSessionManager(Utilities) copySessionWithDisplayID:]"
+ "-endpoint_central- %s: If no client is playing and initial mode is User-init/Anytime/Anytime, don't resume nowPlayingApp"
+ "-endpoint_central- %s: an active client is already playing, so don't resume nowPlayingApp"
+ "20:43:53"
+ "Feb 24 2025"
+ "copySessionWithDisplayID:"
+ "populateNowPlayingAppStack:"
+ "pushToNowPlayingAppStack:"
- "-MXNowPlayingAppManager- %s: \t-------------------------- NowPlayingAppHostProcessAttributionBundleID Dictionary --------------------------"
- "-MXNowPlayingAppManager- %s: Now Playing App HostProcessAttributionBundle on disk is NULL"
- "-MXNowPlayingAppManager- %s: Pushing displayID='%{public}@' hostProcessAttributionBundleID='%{public}@' to NowPlayingAppStack, existing size = %lu, new size = %lu"
- "-MXSessionManagerUtilities- %s: We dont want to play a chime if session is not doing IO."
- "-MXSystemSoundServices- %s: Completed request to play privacy pong sound... Resetting conditions to play privacy pong to false"
- "-MXSystemSoundServices- %s: Invalid system sound:%d"
- "-MX_FeatureFlags- %s: PrivacyPong feature is %{public}s"
- "-PVM- %s: Failed to save endoint type\n"
- "-[MXNowPlayingAppManager pushToNowPlayingAppStack:hostProcessAttributionBundleID:]"
- "-[MXSystemSoundServices playPrivacyPongSound]_block_invoke"
- "-[MXSystemSoundServices playSystemSound:completionBlock:]"
- "-endpoint_central- %s: If no client is playing and initial mode is User-init/Anytime/Anytime, dont resume nowPlayingApp"
- "-endpoint_central- %s: an active client is already playing, so dont resume nowPlayingApp"
- "04:51:03"
- "Feb 16 2025"
- "MXSystemSoundServices"
- "MX_FeatureFlags_IsPrivacyPongEnabled_block_invoke"
- "MX_SystemSoundServices.m"
- "PrivacyPong"
- "PrivacyPongAlwaysHeard"
- "TB,R,V_shouldPrivacyPongPlay"
- "_shouldPrivacyPongPlay"
- "com.apple.mediaexperience.SystemSoundServicesQueue"
- "i28@0:8I16@?20"
- "mNowPlayingAppHostProcessAttributionBundleID"
- "nowPlayingAppHostProcessAttributionBundleID"
- "playPrivacyPongSound"
- "playSystemSound:completionBlock:"
- "populateNowPlayingAppStack:hostProcessAttributionBundleID:"
- "pushToNowPlayingAppStack:hostProcessAttributionBundleID:"
- "shouldPrivacyPongPlay"

```
