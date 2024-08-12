## IntentsUI

> `/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI`

```diff

-2909.100.11.0.0
-  __TEXT.__text: 0x59edc
-  __TEXT.__auth_stubs: 0x17a0
-  __TEXT.__objc_stubs: 0x9020
-  __TEXT.__objc_methlist: 0x374c
-  __TEXT.__cstring: 0x24eb
-  __TEXT.__objc_classname: 0x57d
-  __TEXT.__objc_methname: 0xe6de
-  __TEXT.__objc_methtype: 0x20b9
-  __TEXT.__oslogstring: 0x21e8
-  __TEXT.__const: 0x9de
-  __TEXT.__gcc_except_tab: 0x2f8
-  __TEXT.__constg_swiftt: 0x684
-  __TEXT.__swift5_typeref: 0x6c8
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_capture: 0x550
-  __TEXT.__swift5_reflstr: 0x322
-  __TEXT.__swift5_fieldmd: 0x330
+2975.200.2.0.0
+  __TEXT.__text: 0x5b7f8
+  __TEXT.__auth_stubs: 0x17e0
+  __TEXT.__objc_stubs: 0x8f00
+  __TEXT.__objc_methlist: 0x369c
+  __TEXT.__cstring: 0x251b
+  __TEXT.__objc_classname: 0x57f
+  __TEXT.__objc_methname: 0xe4f1
+  __TEXT.__objc_methtype: 0x2099
+  __TEXT.__oslogstring: 0x2176
+  __TEXT.__const: 0xab0
+  __TEXT.__gcc_except_tab: 0x2bc
+  __TEXT.__constg_swiftt: 0x72c
+  __TEXT.__swift5_typeref: 0x768
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_capture: 0x874
+  __TEXT.__swift5_reflstr: 0x3a2
+  __TEXT.__swift5_fieldmd: 0x3c4
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x58
-  __TEXT.__swift5_types: 0x54
-  __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x18d0
-  __TEXT.__eh_frame: 0x26a8
-  __DATA_CONST.__auth_got: 0xbe0
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__auth_ptr: 0x280
-  __DATA_CONST.__const: 0x1610
+  __TEXT.__swift5_proto: 0x70
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_mpenum: 0x1c
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__eh_frame: 0x27e8
+  __DATA_CONST.__auth_got: 0xc00
+  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__auth_ptr: 0x2e0
+  __DATA_CONST.__const: 0x1cb8
   __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x58

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x7f80
-  __DATA.__objc_selrefs: 0x2d00
-  __DATA.__objc_ivar: 0x414
+  __DATA.__objc_const: 0x7ef0
+  __DATA.__objc_selrefs: 0x2cb0
+  __DATA.__objc_ivar: 0x400
   __DATA.__objc_data: 0x1620
-  __DATA.__data: 0x1998
+  __DATA.__data: 0x1af8
   __DATA.__bss: 0xc80
   __DATA.__common: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1968
-  Symbols:   476
-  CStrings:  2943
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1997
+  Symbols:   484
+  CStrings:  2929
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_deletedAsyncMethodErrorTu
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_TUCaption
CStrings:
+ "\n    transcriptData: "
+ "\x16"
+ "$__lazy_storage_$_transcriptData"
+ ",\x16"
+ "callDirectoryIdentityType"
+ "configureWithRecentsItem:recentCall:"
+ "isCallVoicemailSupportedForAccountUUID:"
+ "messagesChangedPublisher"
+ "transcriptData"
+ "v32@0:8@\"PHRecentsItem\"16@\"CHRecentCall\"24"
- "$__lazy_storage_$_captions"
- ".\x17"
- "@\"<MPVoicemailManagerProtocol>\"8@?0"
- "@\"VMVoicemailManager\"8@?0"
- "Captions at url %!s(MISSING) failed to unarchive."
- "Could not find captions for voicemail at %!s(MISSING) with error %!@(MISSING)"
- "T@\"<MPVoicemailManagerProtocol>\",&,N,V_voicemailManager"
- "T@\"MPVoicemailController\",R,N,V_voicemailController"
- "T@\"NSDictionary\",C,N,V_messageCache"
- "_messageCache"
- "addOperationWithBlock:"
- "combinedStringFromCaptions:"
- "configureWithRecentsItem:recentCall:messageIndicatorViewModel:"
- "initWithCallHistoryController:callProviderManager:contactStore:suggestedContactStore:metadataCache:voicemailController:"
- "mainQueue"
- "messageCache"
- "messageCacheForMessages:recentCalls:"
- "messageForRecentCall:"
- "phoneRecentsEnabled"
- "populateMessageCache"
- "populateMessageCacheForMessages:recentCalls:"
- "setAccountManager:"
- "setMessageCache:"
- "url"
- "v40@0:8@\"PHRecentsItem\"16@\"CHRecentCall\"24@\"TPMessageIndicatorViewModel\"32"

```
