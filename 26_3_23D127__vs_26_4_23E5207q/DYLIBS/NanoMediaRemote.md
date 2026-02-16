## NanoMediaRemote

> `/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote`

```diff

-2023.300.2.0.0
-  __TEXT.__text: 0x990
-  __TEXT.__auth_stubs: 0x180
+2023.500.11.0.0
+  __TEXT.__text: 0xa4c
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__cstring: 0x13d
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x1f8

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18E24506-4C87-3CE1-85A1-164862B59DA3
+  UUID: 23F9EF77-3860-341B-B70A-0470ECF06A1A
   Functions: 16
-  Symbols:   123
+  Symbols:   120
   CStrings:  113
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x22
- _objc_retain_x3
Functions:
~ +[NSBundle(NanoMediaRemote) nanoMediaRemoteBundle] : 68 -> 84
~ ___50+[NSBundle(NanoMediaRemote) nanoMediaRemoteBundle]_block_invoke : 72 -> 76
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemPodcastsPath] : 56 -> 60
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemBooksPath] : 56 -> 60
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemWorkoutPath] : 64 -> 68
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemWorkoutGuidedWalkPath] : 80 -> 84
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemVoiceMemosPath] : 64 -> 68
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemRemotePath] : 64 -> 68
~ -[MPCPlayerPath(NanoMediaRemote) nmr_isSystemMindfulnessPath] : 64 -> 68
~ +[MPCPlayerPath(NanoMediaRemote) nmr_pathWithNowPlayingURL:] : 608 -> 656
~ -[NMRAppLaunchInfo initWithPlayerResponse:] : 776 -> 848
~ -[NMRAppLaunchInfo _launchURLForScheme:requestedPlayerPath:] : 372 -> 392

```
