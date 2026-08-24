## SiriVideoFlowTools

> `/System/Library/FlowTools/Tools/SiriVideoFlowTools.flowtool/Contents/MacOS/SiriVideoFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`

```diff

-3600.28.6.0.0
-  __TEXT.__text: 0x18d24
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x3a0
-  __TEXT.__const: 0x1fa8
-  __TEXT.__cstring: 0xe65
-  __TEXT.__swift5_typeref: 0x717
-  __TEXT.__constg_swiftt: 0x370
-  __TEXT.__swift5_reflstr: 0x6ae
-  __TEXT.__swift5_fieldmd: 0x7c4
-  __TEXT.__swift5_types: 0x60
+3600.28.7.0.0
+  __TEXT.__text: 0x19f94
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__const: 0x2168
+  __TEXT.__cstring: 0x15d5
+  __TEXT.__constg_swiftt: 0x3a8
+  __TEXT.__swift5_typeref: 0x769
+  __TEXT.__swift5_reflstr: 0x6de
+  __TEXT.__swift5_fieldmd: 0x7e0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_assocty: 0x180
+  __TEXT.__swift5_proto: 0x13c
+  __TEXT.__swift5_types: 0x64
   __TEXT.__objc_classname: 0x9f
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x124
-  __TEXT.__objc_methname: 0x301
+  __TEXT.__objc_methname: 0x30a
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__oslogstring: 0x540
+  __TEXT.__oslogstring: 0x590
   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x5c
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x6e8
-  __TEXT.__eh_frame: 0x948
-  __DATA_CONST.__const: 0xef1
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__eh_frame: 0x980
+  __DATA_CONST.__const: 0xf19
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__auth_ptr: 0xa00
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__auth_ptr: 0xab8
   __DATA.__objc_const: 0x320
-  __DATA.__objc_selrefs: 0xe8
-  __DATA.__data: 0x7a8
-  __DATA.__bss: 0x23a0
+  __DATA.__objc_selrefs: 0xf0
+  __DATA.__data: 0x7e8
+  __DATA.__bss: 0x26a0
   __DATA.__common: 0x128
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/FlowToolTypes.framework/Versions/A/FlowToolTypes
   - /System/Library/PrivateFrameworks/FlowToolsShared.framework/Versions/A/FlowToolsShared
   - /System/Library/PrivateFrameworks/FlowToolsSnippetService.framework/Versions/A/FlowToolsSnippetService
+  - /System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriVideoIntents.framework/Versions/A/SiriVideoIntents
   - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 651
-  Symbols:   120
-  CStrings:  124
+  Functions: 685
+  Symbols:   126
+  CStrings:  135
 
Symbols:
+ _LNPerformActionErrorKindInterventionRequired
+ _LNPerformActionErrorKindKey
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSError
+ _swift_dynamicCast
+ _swift_getForeignTypeMetadata
CStrings:
+ "Intents.Error.ContentRestricted"
+ "Intents.Error.PlayFailureContentUnavailable"
+ "Intents.Error.PlayFailureFederatedUnavailable"
+ "PlayVideoContentToolErrorProvider: received error from TV app — %s"
+ "Playback requires the user to take an action in the app. Stop and inform the user they need to take that action in the app before this content can play. Do not retry this or any other play request for this content."
+ "The app did not respond in time when launched for playback. Stop and inform the user the app didn't respond. Do not retry this or any other play request for this content."
+ "The app failed to open for playback. Stop and inform the user the app couldn't be launched. Do not retry this or any other play request for this content."
+ "The app has already shown the user a screen asking them to connect the app to the Apple TV app, which requires agreeing to share their viewing activity with Apple under their Apple Account. Stop and inform the user they need to tap Connect on that screen before this content can play. Do not retry this or any other play request for this content."
+ "The app required to play this content is not installed on this device. The app has already shown the user a prompt with the app icon, name, and a message that the content will play once it's installed. Stop and inform the user they need to install the app before this content can play. Do not retry this or any other play request for this content."
+ "The app requires the user to accept a GDPR consent agreement before playing content. Stop and inform the user they need to open the app and accept the agreement. Do not retry this or any other play request for this content."
+ "The app requires the user to sign in with their iCloud account before this content can play. Stop and inform the user they need to sign in to the app with their iCloud account before this content can play. Do not retry this or any other play request for this content."
+ "This content could not be automatically launched in the app. Stop and inform the user to open the app directly to continue. This is not a sign-in or subscription issue Do not suggest sign-in or purchase, and do not retry this or any other play request for this content."
+ "This content exceeds the content restrictions (parental controls) configured on this device. Stop and inform the user this content is blocked by their content restrictions settings. This is not a sign-in or subscription issue — do not suggest sign-in or purchase, and do not retry this or any other play request for this content."
+ "This content is unavailable, for example due to region or licensing restrictions. Stop and inform the user this content isn't available. This is not a sign-in or subscription issue Do not suggest sign-in or purchase, and do not retry this or any other play request for this content."
+ "This content requires a subscription or purchase the user doesn't have. The app has already shown the user a page with options to buy, rent, or subscribe for this content. Stop and inform the user they need to complete a purchase or subscription in the app before this content can play. Do not retry this or any other play request for this content."
+ "Video playback is not supported while CarPlay is in background mode. Stop and inform the user video can't play here while CarPlay is in the background. Do not retry this or any other play request for this content."
+ "playVideoContentTool.error.contentRestricted"
+ "playVideoContentTool.error.playFailureContentUnavailable"
+ "playVideoContentTool.error.playFailureFederatedUnavailable"
+ "userInfo"
- "No app on this device can play this content — the user likely needs to install a provider app first. This cannot be resolved by Siri. Do not retry searching or playing this content."
- "Playback requires the user to take an action in the provider app that Siri cannot complete. This cannot be resolved by Siri. Do not retry searching or playing this content."
- "The content requires a subscription or purchase the user doesn't have. Siri cannot subscribe or purchase content on their behalf. Do not retry searching or playing this content."
- "The provider app did not respond in time when Siri tried to launch it for playback. This cannot be resolved by Siri. Do not retry searching or playing this content."
- "The provider app failed to open when Siri tried to launch it for playback. This cannot be resolved by Siri. Do not retry searching or playing this content."
- "The provider app requires the user to accept a GDPR consent agreement before playing content. Siri cannot complete consent flows. Do not retry searching or playing this content."
- "The provider app requires the user to accept a video privacy agreement (VPPA) before playing content. Siri cannot complete consent flows. Do not retry searching or playing this content."
- "The provider app requires the user to be signed in, and they currently are not. Siri cannot sign in on their behalf. Do not retry searching or playing this content."
- "Video playback is not supported in CarPlay background mode. This is a platform limitation. This cannot be resolved by Siri. Do not retry searching or playing this content."
```
