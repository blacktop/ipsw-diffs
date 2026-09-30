## SiriMessagesFlow

> `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow`

```diff

-3404.53.2.0.0
-  __TEXT.__text: 0x36214c
-  __TEXT.__auth_stubs: 0x8000
-  __TEXT.__objc_methlist: 0x324
-  __TEXT.__const: 0xff14
-  __TEXT.__cstring: 0xdf37
-  __TEXT.__constg_swiftt: 0xd01c
-  __TEXT.__swift5_typeref: 0x6a81
+3405.17.1.0.0
+  __TEXT.__text: 0x3659e0
+  __TEXT.__auth_stubs: 0x8080
+  __TEXT.__objc_methlist: 0x33c
+  __TEXT.__const: 0xff44
+  __TEXT.__cstring: 0xdfe7
+  __TEXT.__constg_swiftt: 0xd054
+  __TEXT.__swift5_typeref: 0x6b75
   __TEXT.__swift5_builtin: 0x348
   __TEXT.__swift5_reflstr: 0x800b
   __TEXT.__swift5_fieldmd: 0x8f74
   __TEXT.__swift5_assocty: 0x1130
   __TEXT.__swift5_proto: 0xb10
-  __TEXT.__swift5_types: 0x684
-  __TEXT.__swift5_capture: 0x2a24
-  __TEXT.__oslogstring: 0x250df
+  __TEXT.__swift5_types: 0x688
+  __TEXT.__swift5_capture: 0x2a84
+  __TEXT.__oslogstring: 0x2544f
   __TEXT.__swift5_protos: 0x170
-  __TEXT.__swift_as_entry: 0x1054
-  __TEXT.__swift_as_ret: 0x1510
+  __TEXT.__swift_as_entry: 0x107c
+  __TEXT.__swift_as_ret: 0x154c
   __TEXT.__swift5_mpenum: 0xa0
-  __TEXT.__unwind_info: 0xbfc0
-  __TEXT.__eh_frame: 0x24428
-  __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x3c7a
-  __TEXT.__objc_methtype: 0x32c
-  __DATA_CONST.__got: 0x21b0
+  __TEXT.__unwind_info: 0xc128
+  __TEXT.__eh_frame: 0x249ec
+  __TEXT.__objc_classname: 0x11e
+  __TEXT.__objc_methname: 0x3d23
+  __TEXT.__objc_methtype: 0x35a
+  __DATA_CONST.__got: 0x21d8
   __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_classlist: 0x598
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1660
-  __DATA_CONST.__objc_protorefs: 0x78
-  __AUTH_CONST.__auth_got: 0x4000
-  __AUTH_CONST.__auth_ptr: 0x2750
-  __AUTH_CONST.__const: 0x10488
-  __AUTH_CONST.__objc_const: 0xc5b0
+  __DATA_CONST.__objc_selrefs: 0x1690
+  __DATA_CONST.__objc_protorefs: 0x80
+  __AUTH_CONST.__auth_got: 0x4040
+  __AUTH_CONST.__auth_ptr: 0x23d0
+  __AUTH_CONST.__const: 0x10618
+  __AUTH_CONST.__objc_const: 0xc5d0
   __AUTH.__objc_data: 0x1e38
-  __AUTH.__data: 0x11458
-  __DATA.__data: 0x6df0
+  __AUTH.__data: 0x11468
+  __DATA.__data: 0x6f10
   __DATA.__bss: 0x12990
   __DATA.__common: 0xa98
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
+  - /System/Library/Frameworks/CoreTransferable.framework/CoreTransferable
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MapKit.framework/MapKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16159
-  Symbols:   9400
-  CStrings:  4335
+  Functions: 16255
+  Symbols:   9479
+  CStrings:  4358
 
Symbols:
+ _INIssueSandboxExtensionsForFileURLEnumerable
+ __INSendMessageIntentResponseCodeFailureNotAMemberOfConversation
+ _swift_dynamicCastObjCProtocolConditional
CStrings:
+ "#ClientAction+Utilities INFile is not INEnumerable, this is unexpected"
+ "#ClientAction+Utilities converting file to attachment: typeIdentifier=%s, fileURL=%s"
+ "#ClientAction+Utilities data-only INFile, saving to temporary file"
+ "#ClientAction+Utilities failed to create temporary file: %@"
+ "#ClientAction+Utilities failed to extract URL from file: %@"
+ "#ClientAction+Utilities failed to load image representation for live photo bundle: %@"
+ "#ClientAction+Utilities image representation for live photo bundle not available"
+ "#ClientAction+Utilities issuing sandbox extension to path %s"
+ "#ClientAction+Utilities loading image representation for live photo bundle"
+ "#ClientAction+Utilities type identifier conforming to URL, extracting URL from file"
+ "#ClientAction+Utilities unexpected shim parameter for attachment: %s"
+ "#NowPlayingUtilities amsMediaResult is nil returning nil"
+ "#SendMessageConfirmIntentFlow starting dispatch"
+ "#SendMessageNeedsValueFlowStrategy shouldReturnSMARTOutput : %{bool}d because device supports smart : %{bool}d and isTextMessage : %{bool}d "
+ "B32@0:8#16@?24"
+ "B32@0:8#16@?<B@?@\"NSObject\">24"
+ "INEnumerable"
+ "ReadComponentAction#MultilingualContentCommand: No preferred voice found. Utilized voice asset will be compact."
+ "ReadComponentAction#MultilingualContentCommand: Preferred voice found. Voice asset is of high quality."
+ "_intents_enumerateObjectsOfClass:withBlock:"
+ "com.apple.live-photo-bundle"
+ "itemProvider"
+ "loadFileRepresentationWithType:completion:"
+ "notAMemberOfConversation"
+ "resultWithCompletion:"
+ "setIsDefaultApp:"
+ "setIsRequestByHandleType:"
+ "setIsRequestByLabel:"
+ "supportsFlexibleFollowups"
+ "v24@?0@\"AMSLookupResult\"8@\"NSError\"16"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "v28@?0@\"NSURL\"8B16@\"NSError\"20"
- "#SendMessageHandleIntentFlowStrategy can not support app intent responses"
- "#SendMessageShimFlow attaching file with type identifier: %s"
- "#SendMessageShimFlow failed to create temporary file from %@"
- "#SendMessageShimFlow unexpected attachment parameter: %s"
- "MessagesFlowDelegatePlugin HomeIntercom on SiriX is enabled"
- "MessagesFlowDelegatePlugin received an NLv4 parse for reply, announcement is salient, and HomeIntercomeOnSiriX is disabled, falling back to server"
- "NLv4Adoption"
- "SiriHomeCommunication"
- "resultWithError:"

```
