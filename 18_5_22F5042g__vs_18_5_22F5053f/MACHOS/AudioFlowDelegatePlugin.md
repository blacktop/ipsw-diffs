## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3405.17.1.0.0
-  __TEXT.__text: 0x276064
-  __TEXT.__auth_stubs: 0x6e60
+3405.22.1.0.0
+  __TEXT.__text: 0x2775d8
+  __TEXT.__auth_stubs: 0x6dd0
   __TEXT.__objc_methlist: 0x6e8
-  __TEXT.__const: 0x8732
+  __TEXT.__const: 0x89c2
   __TEXT.__cstring: 0x79ac
-  __TEXT.__swift5_typeref: 0x41b0
-  __TEXT.__oslogstring: 0x24347
-  __TEXT.__constg_swiftt: 0x55b0
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3eeb
-  __TEXT.__swift5_assocty: 0xa40
-  __TEXT.__swift5_proto: 0x464
-  __TEXT.__swift5_types: 0x31c
+  __TEXT.__swift5_typeref: 0x41d8
+  __TEXT.__oslogstring: 0x24537
+  __TEXT.__constg_swiftt: 0x5630
+  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_reflstr: 0x3f4b
+  __TEXT.__swift5_assocty: 0xaa0
+  __TEXT.__swift5_proto: 0x484
+  __TEXT.__swift5_types: 0x32c
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x29fc
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2fd4
+  __TEXT.__swift5_fieldmd: 0x2ff8
   __TEXT.__swift5_capture: 0x3904
   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x20c
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3438
-  __TEXT.__eh_frame: 0x32d0
-  __DATA_CONST.__auth_got: 0x3730
-  __DATA_CONST.__got: 0x1e00
-  __DATA_CONST.__auth_ptr: 0x2140
-  __DATA_CONST.__const: 0xa920
+  __TEXT.__unwind_info: 0x3430
+  __TEXT.__eh_frame: 0x3288
+  __DATA_CONST.__auth_got: 0x36e8
+  __DATA_CONST.__got: 0x1e20
+  __DATA_CONST.__auth_ptr: 0x1fe8
+  __DATA_CONST.__const: 0xa9a0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0xa4a8
+  __DATA.__objc_const: 0xa508
   __DATA.__objc_selrefs: 0xdd8
   __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xbc70
-  __DATA.__bss: 0x7a10
+  __DATA.__data: 0xbcc0
+  __DATA.__bss: 0x7e10
   __DATA.__common: 0x470
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5076
-  Symbols:   387
-  CStrings:  3017
+  Functions: 5080
+  Symbols:   386
+  CStrings:  3021
 
Symbols:
- _objc_retain_x13
CStrings:
+ "AddMediaDialogProvider#makeUnsupportedDialog, parameterName: %s"
+ "AddMediaDialogProvider#makeUnsupportedMediaItemsDialog, reasonCode: %s"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse App Resolution state found app: %s"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse App resolution resulted in a failure. Error: %s"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse Done, returning disambiguation response: %s"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse applying app to intent after disambiguation"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse error getting app: %@"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse for input: %s"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse success"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse success with app: %@"
+ "AppResolutionOnDeviceStrategy#parseDisambiguationResponse unexpected resopnse: %s"
+ "AppResolutionOnDeviceStrategy#resolveApp App resolution resulted in a failure. Error: %s"
+ "AppResolutionOnDeviceStrategy#resolveApp Unable to get SiriKit intent from parse"
+ "AppResolutionOnDeviceStrategy#resolveApp returning result %s"
+ "AppResolutionOnDeviceStrategy#resolveApp success"
+ "AppResolutionOnDeviceStrategy#resolveApp timed out waiting for resolveApp to return, continuing on with noAppFound"
+ "CommonIntentAppResolver#resolveSelectedApp app IS installed but doesn't support any SiriKit audio intents: %{public}s"
+ "DetermineSnippetProvider#handleIntent called for Intent: %s %{private}s"
+ "SearchForMediaDialogProvider#makeUnsupportedDialog, reason: %s, mediaType: %s"
+ "UpdateMediaAffinityDialogProvider#makeUnsupportedDialog, reason: %s, mediaType: %s"
- "AppResolutionStrategy#parseDisambiguationResponse App Resolution state found app: %s"
- "AppResolutionStrategy#parseDisambiguationResponse App resolution resulted in a failure. Error: %s"
- "AppResolutionStrategy#parseDisambiguationResponse Done, returning disambiguation response: %s"
- "AppResolutionStrategy#parseDisambiguationResponse applying app to intent after disambiguation"
- "AppResolutionStrategy#parseDisambiguationResponse error getting app: %@"
- "AppResolutionStrategy#parseDisambiguationResponse for input: %s"
- "AppResolutionStrategy#parseDisambiguationResponse success"
- "AppResolutionStrategy#parseDisambiguationResponse success with app: %@"
- "AppResolutionStrategy#parseDisambiguationResponse unexpected resopnse: %s"
- "AppResolutionStrategy#resolveApp App resolution resulted in a failure. Error: %s"
- "AppResolutionStrategy#resolveApp Unable to get SiriKit intent from parse"
- "AppResolutionStrategy#resolveApp returning result %s"
- "AppResolutionStrategy#resolveApp success"
- "CommonIntentAppResolver#resolveSelectedApp app IS installed but doesn't support any Sirikit audio intents: %{public}s"
- "DetermineSnippetProvider#handleIntent called for Intent: %s %{public}s"
- "_INPBWholeHouseAudioMetadata#init Resolved devices: %s"

```
