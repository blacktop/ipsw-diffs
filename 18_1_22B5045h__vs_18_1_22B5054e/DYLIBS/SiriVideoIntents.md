## SiriVideoIntents

> `/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents`

```diff

-3401.6.1.0.0
-  __TEXT.__text: 0x1d9f78
-  __TEXT.__auth_stubs: 0x48b0
+3401.10.1.0.0
+  __TEXT.__text: 0x1dbcb4
+  __TEXT.__auth_stubs: 0x48d0
   __TEXT.__objc_methlist: 0xbf0
-  __TEXT.__const: 0xfc3e
-  __TEXT.__oslogstring: 0xcc39
-  __TEXT.__cstring: 0x8156
-  __TEXT.__swift5_typeref: 0x5a6a
-  __TEXT.__swift5_fieldmd: 0x5b68
-  __TEXT.__constg_swiftt: 0x636c
-  __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x524f
-  __TEXT.__swift5_assocty: 0xe08
+  __TEXT.__const: 0xfe5e
+  __TEXT.__oslogstring: 0xcb39
+  __TEXT.__cstring: 0x8576
+  __TEXT.__swift5_typeref: 0x5a60
+  __TEXT.__swift5_fieldmd: 0x5c54
+  __TEXT.__constg_swiftt: 0x637c
+  __TEXT.__swift5_builtin: 0x21c
+  __TEXT.__swift5_reflstr: 0x542f
+  __TEXT.__swift5_assocty: 0xe20
   __TEXT.__swift5_protos: 0xe0
-  __TEXT.__swift5_proto: 0xc28
-  __TEXT.__swift5_types: 0x61c
+  __TEXT.__swift5_proto: 0xc40
+  __TEXT.__swift5_types: 0x624
   __TEXT.__swift5_capture: 0x163c
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7700
-  __TEXT.__eh_frame: 0xf3bc
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x7798
+  __TEXT.__eh_frame: 0xf5b4
   __TEXT.__objc_classname: 0x112
-  __TEXT.__objc_methname: 0x387b
+  __TEXT.__objc_methname: 0x3884
   __TEXT.__objc_methtype: 0x2a8
   __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0xff0
+  __DATA_CONST.__got: 0x1000
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x1458
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x2460
-  __AUTH_CONST.__auth_ptr: 0x2330
-  __AUTH_CONST.__const: 0xd7d0
-  __AUTH_CONST.__objc_const: 0xe138
+  __AUTH_CONST.__auth_got: 0x2470
+  __AUTH_CONST.__auth_ptr: 0x23d8
+  __AUTH_CONST.__const: 0xd9c8
+  __AUTH_CONST.__objc_const: 0xe218
   __AUTH.__objc_data: 0x2818
-  __AUTH.__data: 0x6050
-  __DATA.__data: 0x4e98
-  __DATA.__bss: 0x15af0
-  __DATA.__common: 0x3c0
+  __AUTH.__data: 0x6080
+  __DATA.__data: 0x4ed8
+  __DATA.__bss: 0x15df0
+  __DATA.__common: 0x410
   __DATA_DIRTY.__data: 0x540
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10714
-  Symbols:   4275
-  CStrings:  2494
+  Functions: 10789
+  Symbols:   4288
+  CStrings:  2513
 
Symbols:
+ _INSearchForMediaIntentResponseCodeGetName
CStrings:
+ "intent.matchupId"
+ "sirikit.intents.custom.com.apple.siri.SiriVideoIntents.ThirdPartyFind"
+ "intentResponse.urlToLaunch"
+ "PlayLiveServiceDisambiguationStrategy.parseDisambiguationResult() received an unexpected parse"
+ "The SiriKit parse was missing data required to continue the request"
+ "When trying to resolve an item from the list, the provided identifier was not found"
+ "liveService.isInstalled"
+ "sirikit.intents.custom.com.apple.siri.SiriVideoIntents.ThirdPartyPlay"
+ "intentResponse.appName"
+ "The SiriKit parse contained unexpected data in the "
+ "A required method parameter is missing: "
+ "Attempting to run parameter resolution on an unsupported parameter"
+ "An error occurred while decoding a DirectInvocation parse"
+ "intentResponse.appName/intentResponse.appStorePunchoutUrl"
+ "intentResponse.appStorePunchoutUrl"
+ "templatingResult"
+ "INSearchForMedia.HandleIntentFlowStrategy.makeFailureHandlingIntentResponse() called with unexpected response code %!s(MISSING)"
+ "An error occurred when trying to localize a value"
+ "Error searching for live services: %!s(MISSING)"
+ "Error removing %!s(MISSING) from WatchList: %!s(MISSING)"
+ "intentResponse.playablePunchoutUrl"
+ "items"
+ "Received an unexpected response code for the "
+ "Unexpected exception when serializing dictionary to/from JSON for content conversion: %!s(MISSING), error: %!s(MISSING)"
+ "mediaRouteIdentifier"
+ "typeName"
+ "Received a parse type which is not supported"
+ "Error searching against WatchList: %!s(MISSING)"
+ "understanding.confirmationValue"
+ "nextToken"
- "Unexpected exception when serializing dictionary to/from JSON for content conversion: %!s(MISSING)"
- "WatchSportsEventHandleIntentFlowStrategy.makeIntentHandledResponse() did not receive code: .success"
- "createInstallAppViews error executing makeAceView"
- "Unexpected exception when serializing dictionary to/from JSON for response conversion: %!s(MISSING)"
- "PlayLiveServiceDisambiguationStrategy.parseDisambiguationResult() received an unecpected parse"
- "Timed out removing %!s(MISSING) from WatchList"
- "Unknown error while handling UTS operation"
- "Timed out searching against WatchList"
- "Failed to deserialize sportsTuneIn response: %!s(MISSING)"
- "PlayVideoHandleIntentFlowStrategy.makeFailureHandlingIntentResponse() called"
- "Timed out searching for live services"
- "An unknown error occurred while executing a request in the Video domain"

```
