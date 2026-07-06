## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities`

```diff

-  __TEXT.__text: 0x1a2f58
-  __TEXT.__objc_methlist: 0x1b560
-  __TEXT.__cstring: 0x12456
+  __TEXT.__text: 0x1a3434
+  __TEXT.__objc_methlist: 0x1b5c8
+  __TEXT.__cstring: 0x124c6
   __TEXT.__const: 0x4098
-  __TEXT.__oslogstring: 0x12c17
+  __TEXT.__oslogstring: 0x12b77
   __TEXT.__gcc_except_tab: 0x13f8
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x535

   __TEXT.__swift5_capture: 0x1d0
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0xac
-  __TEXT.__swift_as_cont: 0x140
+  __TEXT.__swift_as_cont: 0x13c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6620
+  __TEXT.__unwind_info: 0x6630
   __TEXT.__eh_frame: 0x2040
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1928
+  __DATA_CONST.__const: 0x1920
   __DATA_CONST.__objc_classlist: 0x898
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x430
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb548
+  __DATA_CONST.__objc_selrefs: 0xb580
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0xa00
-  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__got: 0xf88
   __AUTH_CONST.__const: 0x5f00
-  __AUTH_CONST.__cfstring: 0x121e0
-  __AUTH_CONST.__objc_const: 0x2ae08
+  __AUTH_CONST.__cfstring: 0x12240
+  __AUTH_CONST.__objc_const: 0x2ae90
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x11f8
-  __AUTH.__objc_data: 0x2310
+  __AUTH.__objc_data: 0x26d0
   __AUTH.__data: 0xb30
-  __DATA.__objc_ivar: 0x18ec
+  __DATA.__objc_ivar: 0x18f4
   __DATA.__data: 0x3d48
   __DATA.__bss: 0x6b40
   __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x3438
+  __DATA_DIRTY.__objc_data: 0x3078
   __DATA_DIRTY.__data: 0x198
   __DATA_DIRTY.__bss: 0x7c0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11291
-  Symbols:   21179
-  CStrings:  6682
+  Functions: 11301
+  Symbols:   21196
+  CStrings:  6688
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[TUJoinContinuityConversationRequest requestForJoinWithUUID:isAudioEnabled:isVideoEnabled:isOutgoing:]
+ +[TUJoinConversationRequest isOutgoingFromURLComponents:]
+ -[TUFeatureFlags receiverSmartCropEnabled]
+ -[TUJoinContinuityConversationRequest initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:isOutgoing:]
+ -[TUJoinContinuityConversationRequest isOutgoing]
+ -[TUJoinConversationRequest isOutgoingQueryItem]
+ -[TUJoinConversationRequest isOutgoing]
+ -[TUJoinConversationRequest setIsOutgoing:]
+ -[TUSubtitleProvider localizedSubtitleForRecentCall:handle:contact:includeCallNotes:]
+ GCC_except_table116
+ GCC_except_table119
+ OBJC_IVAR_$_TUJoinContinuityConversationRequest._isOutgoing
+ OBJC_IVAR_$_TUJoinConversationRequest._isOutgoing
+ _TUNearbyInvitationTimeout
+ _TUShouldUseSuperboxForAllProviders
+ _objc_msgSend$dialWithRequest:
+ _objc_msgSend$initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:isOutgoing:
+ _objc_msgSend$isOutgoingFromURLComponents:
+ _objc_msgSend$isOutgoingQueryItem
+ _objc_msgSend$localizedSubtitleForRecentCall:handle:contact:includeCallNotes:
+ _objc_msgSend$setIsOutgoing:
- GCC_except_table115
- GCC_except_table118
- _TUShouldUseSuperBoxTelephonyProviderKey
- _objc_msgSend$initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:
CStrings:
+ " isOutgoing=%d"
+ "DefaultNearbyMemberTimeOutOverride"
+ "ReceiverSmartCrop"
+ "TUShouldUseSuperboxForAllProviders"
- "Because this is an internal install and the %@ default is set, com.apple.Superbox (aka Speakerbox)                     is acting as the telephony provider"

```
