## SiriMessagesFlow

> `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow`

```diff

-3401.20.1.0.0
-  __TEXT.__text: 0x3b4b28
-  __TEXT.__auth_stubs: 0x78f0
+3401.23.2.0.0
+  __TEXT.__text: 0x3b5090
+  __TEXT.__auth_stubs: 0x7900
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0xf824
-  __TEXT.__cstring: 0xe0a7
-  __TEXT.__constg_swiftt: 0xd0f0
-  __TEXT.__swift5_typeref: 0x66d5
+  __TEXT.__const: 0xf854
+  __TEXT.__cstring: 0xe067
+  __TEXT.__constg_swiftt: 0xd118
+  __TEXT.__swift5_typeref: 0x66fb
   __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_reflstr: 0x7dbb
-  __TEXT.__swift5_fieldmd: 0x8f40
+  __TEXT.__swift5_reflstr: 0x7deb
+  __TEXT.__swift5_fieldmd: 0x8f5c
   __TEXT.__swift5_assocty: 0x1160
-  __TEXT.__swift5_proto: 0xb54
+  __TEXT.__swift5_proto: 0xb58
   __TEXT.__swift5_types: 0x690
-  __TEXT.__swift5_capture: 0x2998
-  __TEXT.__oslogstring: 0x2357f
-  __TEXT.__swift5_protos: 0x164
+  __TEXT.__swift5_capture: 0x2984
+  __TEXT.__oslogstring: 0x235cf
+  __TEXT.__swift5_protos: 0x168
   __TEXT.__swift5_mpenum: 0x84
-  __TEXT.__unwind_info: 0xd510
-  __TEXT.__eh_frame: 0x2436c
-  __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methname: 0x3c57
+  __TEXT.__unwind_info: 0xd128
+  __TEXT.__eh_frame: 0x24494
+  __TEXT.__objc_classname: 0x111
+  __TEXT.__objc_methname: 0x3b70
   __TEXT.__objc_methtype: 0x32c
-  __DATA_CONST.__got: 0x1f90
-  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__got: 0x1f70
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x5a0
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1548
-  __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x3c78
-  __AUTH_CONST.__auth_ptr: 0x2590
-  __AUTH_CONST.__const: 0x104b0
-  __AUTH_CONST.__objc_const: 0xcd08
+  __DATA_CONST.__objc_selrefs: 0x14e0
+  __DATA_CONST.__objc_protorefs: 0x78
+  __AUTH_CONST.__auth_got: 0x3c80
+  __AUTH_CONST.__auth_ptr: 0x23e8
+  __AUTH_CONST.__const: 0x104a0
+  __AUTH_CONST.__objc_const: 0xcd10
   __AUTH.__objc_data: 0x1f28
   __AUTH.__data: 0x11640
-  __DATA.__data: 0x6bf8
+  __DATA.__data: 0x6b78
   __DATA.__bss: 0x13300
-  __DATA.__common: 0xa18
+  __DATA.__common: 0xa20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16627
-  Symbols:   8421
-  CStrings:  4234
+  Functions: 16630
+  Symbols:   8423
+  CStrings:  4221
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _OBJC_CLASS_$_SASendCommands
- _OBJC_CLASS_$_SAStartRequest
- _OBJC_CLASS_$_SAUIConfirmationOption
- _OBJC_CLASS_$_SAUIConfirmationView
CStrings:
+ "#ConversationStateBuilder isSpoken=%!{(MISSING)bool}d, isCarPlay=%!{(MISSING)bool}d, referencedMessage is not from the device owner- Not converting this message to ReactionComponent."
+ "#SendMessageAppResolutionOnDeviceFlowStrategy returning SMART confirmation prompt"
+ "#SendMessageHandleIntentFlowStrategy adding SMART auto send settings button"
+ "parsePromptToSaveRelationshipResponse# Intent has no confirmation"
+ "unsetRelationshipResponses"
- "#ConversationStateBuilder Message isSpoken and referencedMessage is not from the device owner- Not converting this message to ReactionComponent."
- "#SendMessageAppResolutionOnDeviceFlowStrategy in car, returning disambiguation prompt without snippet"
- "SAServerBoundCommand"
- "parsePromptToSaveRelationshipResponse# Intent has no confirmation, check your 'onInput' func"
- "parsePromptToSaveRelationshipResponse# Unable contruct SMS intent"
- "setAllConfirmationOptions:"
- "setAutomaticConfirmationThreshold:"
- "setConfirmCommands:"
- "setConfirmText:"
- "setDelayExpiryCommands:"
- "setDenyCommands:"
- "setDenyText:"
- "setIconLabel:"
- "setIconType:"
- "setLabel:"
- "setSpeechDuration:"
- "setType:"
- "setUtterance:"

```
