## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3404.75.2.11.1
-  __TEXT.__text: 0x2348d0
-  __TEXT.__auth_stubs: 0x3bf0
+3405.17.1.0.0
+  __TEXT.__text: 0x23d718
+  __TEXT.__auth_stubs: 0x3c60
   __TEXT.__objc_methlist: 0xf6c
   __TEXT.__const: 0xbe78
-  __TEXT.__cstring: 0xb1c0
-  __TEXT.__swift5_typeref: 0x46a3
+  __TEXT.__cstring: 0xb240
+  __TEXT.__swift5_typeref: 0x46f7
   __TEXT.__swift5_fieldmd: 0x46a4
-  __TEXT.__constg_swiftt: 0x5f48
+  __TEXT.__constg_swiftt: 0x5f70
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x4a5c
+  __TEXT.__swift5_reflstr: 0x4a6c
   __TEXT.__swift5_assocty: 0x6c0
   __TEXT.__swift5_protos: 0x124
   __TEXT.__swift5_proto: 0x674
   __TEXT.__swift5_types: 0x45c
-  __TEXT.__swift5_capture: 0x55b8
-  __TEXT.__oslogstring: 0x20f5e
-  __TEXT.__swift_as_entry: 0xd0
-  __TEXT.__swift_as_ret: 0x128
+  __TEXT.__swift5_capture: 0x565c
+  __TEXT.__oslogstring: 0x2170e
+  __TEXT.__swift_as_entry: 0xcc
+  __TEXT.__swift_as_ret: 0x124
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4ad0
-  __TEXT.__eh_frame: 0x41ac
+  __TEXT.__unwind_info: 0x4aa0
+  __TEXT.__eh_frame: 0x3fcc
   __TEXT.__objc_classname: 0x19c
   __TEXT.__objc_methname: 0x630d
   __TEXT.__objc_methtype: 0x696
-  __DATA_CONST.__got: 0x1370
-  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__got: 0x1398
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2018
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1df8
-  __AUTH_CONST.__auth_ptr: 0x1980
-  __AUTH_CONST.__const: 0x15b98
+  __AUTH_CONST.__auth_got: 0x1e30
+  __AUTH_CONST.__auth_ptr: 0x1988
+  __AUTH_CONST.__const: 0x15d08
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xab48
+  __AUTH_CONST.__objc_const: 0xab68
   __AUTH.__objc_data: 0xd20
   __AUTH.__data: 0x47a0
-  __DATA.__data: 0x2720
+  __DATA.__data: 0x2750
   __DATA.__bss: 0x8970
   __DATA.__common: 0x110
   __DATA_DIRTY.__objc_data: 0x360
-  __DATA_DIRTY.__data: 0x2638
+  __DATA_DIRTY.__data: 0x2658
   __DATA_DIRTY.__bss: 0x980
   __DATA_DIRTY.__common: 0x140
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8796
-  Symbols:   1060
-  CStrings:  4194
+  Functions: 8835
+  Symbols:   1065
+  CStrings:  4220
 
Symbols:
+ _MRMediaRemoteIsMusicAppInstalled
CStrings:
+ "AppIntentInvoker#invokeSearchMusicIntent response: %s"
+ "AppleMediaServicesProvider#acknowledgementNeeded user %s GDPR acknowledgement for %s"
+ "CommonIntentSignals#onscreenMediaItemListPosition could not find intent returning nil"
+ "MediaPlaybackProvider#prepareForSetQueue MusicApp NOT installed, not issuing MRMediaRemoteCommandPrepareForSetQueue"
+ "MediaPlaybackProvider#prepareForSetQueue preventing re-send MRMediaRemoteCommandPrepareForSetQueue for same Siri request"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem intent is definite reference for onscreen entity. Fetching first onscreen media item..."
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem looking for onscreen entity matching search..."
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem no conditions met, returning nil"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem no matching onscreen mediaItem found."
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem no onscreen mediaItem found at: %ld"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem no onscreen mediaItem found."
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem onscreen media item list position was found: %ld"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem returning salient onscreen mediaItem for definite reference: %s"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem returning salient onscreen mediaItem matching request: %s"
+ "OnscreenAppProvider#resolveSalientOnscreenMediaItem returning salient onscreen mediaItem: %s at: %ld"
+ "ShimUtilities AudioResult %s"
+ "ShimUtilities AudioResult deserialization error: %@"
+ "ShimUtilities AudioResult uncast %s"
+ "ShimUtilities#getAppBundleId Not ifClientAction parse"
+ "ShimUtilities#getAppBundleId app parameter: %s"
+ "ShimUtilities#getAppBundleId app shimParameter not found"
+ "ShimUtilities#getAppBundleId app value: %s"
+ "ShimUtilities#getAppBundleId app: %s"
+ "ShimUtilities#getAppBundleId shim parameter: %s"
+ "ShimUtilities#getAppBundleId unable to extract appValue"
+ "ShimUtilities#getAppBundleId unable to extract appValue typed entity"
+ "com.apple.onboarding.podcasts"
+ "experience rankedResults "
+ "resolutionResultType"
- "AppIntentInvoker#invokeSearchMusicAppIntent response: %s"
- "AppleMediaServicesProvider#acknowledgementNeeded user %s GDPR acknowledgement"
- "MediaPlaybackProvider#play preventing re-send MRMediaRemoteCommandPrepareForSetQueue for same Siri request"

```
