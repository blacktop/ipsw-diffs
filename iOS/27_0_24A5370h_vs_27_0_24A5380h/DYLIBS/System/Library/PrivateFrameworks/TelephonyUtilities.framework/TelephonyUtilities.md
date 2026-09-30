## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-  __TEXT.__text: 0x19d6a0
-  __TEXT.__objc_methlist: 0x1b5c8
-  __TEXT.__cstring: 0x141c6
+  __TEXT.__text: 0x19db34
+  __TEXT.__objc_methlist: 0x1b630
+  __TEXT.__cstring: 0x14236
   __TEXT.__const: 0x40a8
-  __TEXT.__oslogstring: 0x13c17
+  __TEXT.__oslogstring: 0x13b77
   __TEXT.__gcc_except_tab: 0x181c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__swift5_capture: 0x1d0
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0xac
-  __TEXT.__swift_as_cont: 0x140
+  __TEXT.__swift_as_cont: 0x13c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6d40
+  __TEXT.__unwind_info: 0x6d50
   __TEXT.__eh_frame: 0x2040
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x37e0
+  __DATA_CONST.__const: 0x37d8
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb788
+  __DATA_CONST.__objc_selrefs: 0xb7c0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0xa00
-  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__got: 0xff8
   __AUTH_CONST.__const: 0x46d8
-  __AUTH_CONST.__cfstring: 0x12540
-  __AUTH_CONST.__objc_const: 0x2aeb0
+  __AUTH_CONST.__cfstring: 0x125a0
+  __AUTH_CONST.__objc_const: 0x2af38
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x14f8
-  __AUTH.__objc_data: 0x2920
+  __AUTH.__objc_data: 0x2fd8
   __AUTH.__data: 0xc30
-  __DATA.__objc_ivar: 0x18f8
-  __DATA.__data: 0x3d38
-  __DATA.__bss: 0x7640
+  __DATA.__objc_ivar: 0x1900
+  __DATA.__data: 0x3d58
+  __DATA.__bss: 0x7650
   __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x2da8
+  __DATA_DIRTY.__objc_data: 0x26f0
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11534
-  Symbols:   31669
-  CStrings:  6940
+  Functions: 11544
+  Symbols:   31695
+  CStrings:  6946
 
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
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table163
+ _OBJC_IVAR_$_TUJoinContinuityConversationRequest._isOutgoing
+ _OBJC_IVAR_$_TUJoinConversationRequest._isOutgoing
+ _TUNearbyInvitationTimeout
+ _TUShouldUseSuperboxForAllProviders
+ _objc_msgSend$dialWithRequest:
+ _objc_msgSend$initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:isOutgoing:
+ _objc_msgSend$isOutgoingFromURLComponents:
+ _objc_msgSend$isOutgoingQueryItem
+ _objc_msgSend$localizedSubtitleForRecentCall:handle:contact:includeCallNotes:
+ _objc_msgSend$setIsOutgoing:
- GCC_except_table110
- GCC_except_table113
- _TUShouldUseSuperBoxTelephonyProviderKey
- _objc_msgSend$initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:
CStrings:
+ " isOutgoing=%d"
+ "DefaultNearbyMemberTimeOutOverride"
+ "ReceiverSmartCrop"
+ "TUShouldUseSuperboxForAllProviders"
- "Because this is an internal install and the %@ default is set, com.apple.Superbox (aka Speakerbox)                     is acting as the telephony provider"

```
