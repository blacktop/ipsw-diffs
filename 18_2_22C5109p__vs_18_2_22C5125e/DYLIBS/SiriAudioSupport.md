## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3402.51.1.1.2
-  __TEXT.__text: 0x224494
-  __TEXT.__auth_stubs: 0x38f0
+3402.60.1.1.1
+  __TEXT.__text: 0x2259f4
+  __TEXT.__auth_stubs: 0x3880
   __TEXT.__objc_methlist: 0x81c
-  __TEXT.__const: 0xa328
-  __TEXT.__cstring: 0xb330
-  __TEXT.__swift5_typeref: 0x4239
-  __TEXT.__swift5_fieldmd: 0x4494
-  __TEXT.__constg_swiftt: 0x5cb8
+  __TEXT.__const: 0xa3c8
+  __TEXT.__cstring: 0xb3c0
+  __TEXT.__swift5_typeref: 0x4279
+  __TEXT.__swift5_fieldmd: 0x44e8
+  __TEXT.__constg_swiftt: 0x5d60
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x483c
+  __TEXT.__swift5_reflstr: 0x489c
   __TEXT.__swift5_assocty: 0x648
-  __TEXT.__swift5_protos: 0x118
-  __TEXT.__swift5_proto: 0x630
-  __TEXT.__swift5_types: 0x43c
-  __TEXT.__swift5_capture: 0x5430
-  __TEXT.__oslogstring: 0x1f93e
+  __TEXT.__swift5_protos: 0x11c
+  __TEXT.__swift5_proto: 0x634
+  __TEXT.__swift5_types: 0x444
+  __TEXT.__swift5_capture: 0x54c4
+  __TEXT.__oslogstring: 0x1fabe
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4aa8
-  __TEXT.__eh_frame: 0x3424
+  __TEXT.__unwind_info: 0x4af0
+  __TEXT.__eh_frame: 0x33ec
   __TEXT.__objc_classname: 0x19c
-  __TEXT.__objc_methname: 0x6280
+  __TEXT.__objc_methname: 0x62e6
   __TEXT.__objc_methtype: 0x696
-  __DATA_CONST.__got: 0x1118
+  __DATA_CONST.__got: 0x1108
   __DATA_CONST.__const: 0x888
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1cf0
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1c78
-  __AUTH_CONST.__auth_ptr: 0x17f0
-  __AUTH_CONST.__const: 0x15388
+  __AUTH_CONST.__auth_got: 0x1c40
+  __AUTH_CONST.__auth_ptr: 0x1760
+  __AUTH_CONST.__const: 0x154e0
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xb518
+  __AUTH_CONST.__objc_const: 0xb660
   __AUTH.__objc_data: 0x1128
-  __AUTH.__data: 0x5d20
-  __DATA.__data: 0x2ff8
+  __AUTH.__data: 0x5e70
+  __DATA.__data: 0x3008
   __DATA.__bss: 0x8b90
   __DATA.__common: 0x2e8
   __DATA_DIRTY.__objc_data: 0xd0

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8760
-  Symbols:   998
-  CStrings:  4105
+  Functions: 8796
+  Symbols:   1003
+  CStrings:  4114
 
Symbols:
+ _MPCAssistantMediaRemoteSendCommandErrorDomain
+ _OBJC_CLASS_$_LNConnectionPolicy
+ _OBJC_CLASS_$_LNEntityIdentifier
+ _OBJC_CLASS_$_LNValue
- _OBJC_CLASS_$_NSPropertyListSerialization
CStrings:
+ "AudioMegamodelTriggeredLogger#emitTriggeredLogAsync: provided codepath [%!s(MISSING)] doesn't parse as a UUID; this trigger will never be emitted!  Skipping."
+ "LocalPlaybackHandler#handlePlaybackQueueLocation, routeCount: %!l(MISSING)d"
+ "LocalPlaybackHandler#preLoadQueue, routeCount: %!l(MISSING)d, targetsLocalDevice: %!{(MISSING)bool}d"
+ "LocalPlaybackHelper#makeCollectionQuery Unable to extract Query Items as fallback; returning original query"
+ "LocalPlaybackHelper#queryOnlyPlayableItems for %!{(MISSING)public}s with onlyPlayableItems: %!{(MISSING)bool,public}d, hasRoutes: %!{(MISSING)bool}d, and targetsLocalDevice: %!{(MISSING)bool,public}d"
+ "MediaPlaybackProvider#doesCurrentDevicePolicyAllowTimeoutErrorsForTailspin no Trial policy, returning false"
+ "MediaPlaybackProvider#doesCurrentDevicePolicyAllowTimeoutErrorsForTailspin no parseable policy, returning false"
+ "MediaPlaybackProvider#doesCurrentDevicePolicyAllowTimeoutErrorsForTailspin tailspin list is empty"
+ "MediaPlaybackProvider#doesCurrentDevicePolicyAllowTimeoutErrorsForTailspin tailspins supported: %!s(MISSING)"
+ "MediaPlaybackProvider#generateTailSpinIfPolicyAndErrorAllow collecting tailspin for list: %!s(MISSING) and errorDescription: %!s(MISSING)"
+ "MediaPlaybackProvider#generateTailSpinIfPolicyAndErrorAllow createTailSpinFile generated: %!s(MISSING)"
+ "MediaPlaybackProvider#generateTailSpinIfPolicyAndErrorAllow failed to create tailspin file"
+ "MediaPlaybackProvider#generateTailSpinIfPolicyAndErrorAllow no op, with tailspinList: %!s(MISSING) and errorDescription: '%!s(MISSING)'"
+ "MediaPlaybackProvider#logSignpost submitting error metrics for %!s(MISSING)"
+ "MediaPlaybackProvider#readStatus %!{(MISSING)public}s MPCAssistantCommand status for: '%!{(MISSING)public}s' - Error returned AppNotInstalledError"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem Checking for matching on-screen entities"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem No salient on screen entities found"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem Unknown/unsupported result type"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem failed to create entity from builder"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem found match: %!s(MISSING)"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem found multiple matches: %!s(MISSING)"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem media item not found."
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem no on screen entities found"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem reference resolution failed with error: %!s(MISSING)"
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem returning on-screen media item: %!s(MISSING)."
+ "OnscreenEntityProvider#retrieveSalientOnScreenMediaItem there is no media item title to match with."
+ "PlaybackService#warm, terminating flow due to PFSQ terminal error: %!{(MISSING)public}s"
+ "SiriAudioLinkServiceConnection#mediaItems fetchStructuredData failed with error: %!@(MISSING)"
+ "SiriAudioLinkServiceConnection#mediaItems fetching structured data for entities identifiers: %!s(MISSING)"
+ "SiriAudioLinkServiceConnection#mediaItems no app bundle id for connection policy."
+ "SiriAudioLinkServiceConnection#mediaItems returning mediaItems: %!s(MISSING)"
+ "_TtC16SiriAudioSupport11PFSQHandler"
+ "_TtC16SiriAudioSupport21SiriAudioLinkServices"
+ "appEntityTypeNameSpace"
+ "appNotInstalled"
+ "connectionWithError:"
+ "fetchStructuredDataWithTypeIdentifier:forEntityIdentifiers:completionHandler:"
+ "initWithTypeIdentifier:instanceIdentifier:"
+ "policyWithBundleIdentifier:"
- "AudioMegamodelTriggeredLogger#emitTriggeredLogAsync: provided codepath doesn't parse as a UUID; this trigger will never be emitted!  Skipping."
- "LocalPlaybackHelper#makeCollectionQuery Unable to extract Query Items as fallback"
- "LocalPlaybackHelper#queryOnlyPlayableItems for %!{(MISSING)public}s with onlyPlayableItems: %!{(MISSING)bool,public}d and targetsLocalDevice: %!{(MISSING)bool,public}d"
- "MediaPlaybackProvider#checkIsDenyListed count of results for '%!s(MISSING)': %!l(MISSING)d"
- "MediaPlaybackProvider#checkIsDenyListed no throttledErrors, not denied"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin denyAll, returning false"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin invalid policy, returning false"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no error denyList, returning true"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no policy for %!s(MISSING)"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no policy, returning false"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin not HomePod, returning false"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin returning %!{(MISSING)bool}d"
- "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin..."
- "MediaPlaybackProvider#generateTailSpinIfIsCommandDidNotProvideAStatusError createTailSpinFile generated: %!s(MISSING)"
- "MediaPlaybackProvider#generateTailSpinIfIsCommandDidNotProvideAStatusError failed to create tailspin file"
- "MediaPlaybackProvider#send, terminating flow due to PFSQ terminal error"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity Checking for matching on-screen entities"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity No salient on screen entities found"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity Unknown/unsupported result type"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity failed to convert task to AudioMediaItem"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity failed to create entity from builder"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity found match: %!s(MISSING)"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity found matching on screen entity for: %!s(MISSING)"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity found multiple matches: %!s(MISSING)"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity no on screen entities found"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity onscreen entity is not common_MediaItem"
- "OnscreenEntityProvider#retrieveSalientOnScreenEntity reference resolution failed with error: %!s(MISSING)"
- "UsoEntity_common_MediaItem#toINMediaItem creating AudioMediaItem with title: %!s(MISSING), artist: %!s(MISSING), mediaItemType: %!s(MISSING), and identifier: %!s(MISSING) from songEntityId: %!s(MISSING)"
- "objectForKeyedSubscript:"
- "propertyListWithData:options:format:error:"

```
