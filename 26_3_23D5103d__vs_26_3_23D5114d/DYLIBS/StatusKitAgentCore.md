## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-116.400.1.0.0
-  __TEXT.__text: 0x101d44
+116.400.11.0.0
+  __TEXT.__text: 0x101f04
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x804c
-  __TEXT.__const: 0x2288
-  __TEXT.__cstring: 0x4ea1
-  __TEXT.__oslogstring: 0x1301f
+  __TEXT.__objc_methlist: 0x8054
+  __TEXT.__const: 0x2298
+  __TEXT.__cstring: 0x4ec1
+  __TEXT.__oslogstring: 0x1309f
   __TEXT.__gcc_except_tab: 0x12e8
   __TEXT.__swift5_typeref: 0x163e
   __TEXT.__constg_swiftt: 0x6d0

   __TEXT.__unwind_info: 0x3750
   __TEXT.__eh_frame: 0x5500
   __TEXT.__objc_classname: 0xed1
-  __TEXT.__objc_methname: 0x11ce9
+  __TEXT.__objc_methname: 0x11cfc
   __TEXT.__objc_methtype: 0x4b44
-  __TEXT.__objc_stubs: 0x9c40
+  __TEXT.__objc_stubs: 0x9c60
   __DATA_CONST.__got: 0x910
   __DATA_CONST.__const: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3538
+  __DATA_CONST.__objc_selrefs: 0x3540
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0x24c0
+  __AUTH_CONST.__cfstring: 0x24e0
   __AUTH_CONST.__objc_const: 0xbcd8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 454C1C62-C4A2-390E-9688-0F445EAA7E7C
-  Functions: 4855
-  Symbols:   15765
-  CStrings:  4909
+  UUID: E73E64CD-074B-310F-9458-E95B50B2696E
+  Functions: 4856
+  Symbols:   15786
+  CStrings:  4914
 
Symbols:
+ +[SKAServerBag preferPhoneNumbers]
+ _objc_msgSend$preferPhoneNumbers
Functions:
+ +[SKAServerBag preferPhoneNumbers]
~ -[SKAInvitationManager _sendReverseInvitationIfNeededForPresenceIdentifier:incomingChannel:senderHandle:invitedHandle:dateInvitationCreated:databaseContext:] : 900 -> 984
~ -[SKAMessagingProvider resolveSenderHandleWithPreferredSenderHandle:] : 752 -> 764
~ -[SKAMessagingProvider tokenURIWithError:] : 684 -> 696
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92
CStrings:
+ "Attempting to send reverse invite: incoming channel %@, representative channel %@"
+ "Incoming channel is the same as our current channel - skipping reverse invite"
+ "Server bag indicates prefer phone numbers: %@"
+ "preferPhoneNumbers"
+ "shared-channels-prefer-phone-numbers"
- "incoming channel creation date: %@ current channel creation date: %@"

```
