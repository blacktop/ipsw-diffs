## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-234.10.6.0.0
-  __TEXT.__text: 0x55040
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0x2ed4
-  __TEXT.__const: 0x41c
-  __TEXT.__cstring: 0x2802
+248.20.7.0.0
+  __TEXT.__text: 0x5a8a4
+  __TEXT.__auth_stubs: 0x1290
+  __TEXT.__objc_methlist: 0x2ee4
+  __TEXT.__const: 0x14b6
+  __TEXT.__cstring: 0x2ad7
   __TEXT.__oslogstring: 0x5b98
   __TEXT.__gcc_except_tab: 0x1074
-  __TEXT.__swift5_typeref: 0x3c5
+  __TEXT.__swift5_typeref: 0x91e
   __TEXT.__swift5_capture: 0xd0
-  __TEXT.__constg_swiftt: 0x1d8
-  __TEXT.__swift5_reflstr: 0x141
-  __TEXT.__swift5_fieldmd: 0x140
-  __TEXT.__swift5_types: 0x1c
+  __TEXT.__constg_swiftt: 0x280
+  __TEXT.__swift5_reflstr: 0x576
+  __TEXT.__swift5_fieldmd: 0x320
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_assocty: 0x210
+  __TEXT.__swift5_proto: 0x140
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__unwind_info: 0x1418
-  __TEXT.__eh_frame: 0x340
+  __TEXT.__unwind_info: 0x1838
+  __TEXT.__eh_frame: 0x338
   __TEXT.__objc_classname: 0x9ef
-  __TEXT.__objc_methname: 0xb811
+  __TEXT.__objc_methname: 0xb702
   __TEXT.__objc_methtype: 0x291c
-  __TEXT.__objc_stubs: 0x8960
-  __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0x16a8
+  __TEXT.__objc_stubs: 0x8980
+  __DATA_CONST.__got: 0x8e0
+  __DATA_CONST.__const: 0x16d0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2678
+  __DATA_CONST.__objc_selrefs: 0x2648
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x948
-  __AUTH_CONST.__auth_ptr: 0x118
-  __AUTH_CONST.__const: 0xa58
+  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_ptr: 0x290
+  __AUTH_CONST.__const: 0x1270
   __AUTH_CONST.__cfstring: 0x1360
   __AUTH_CONST.__objc_const: 0x7b20
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x650
   __AUTH.__data: 0x68
   __DATA.__objc_ivar: 0x294
-  __DATA.__data: 0x13b8
-  __DATA.__bss: 0x490
-  __DATA.__common: 0x20
+  __DATA.__data: 0x16e0
+  __DATA.__bss: 0x2910
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x948
   __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Announce.framework/Announce
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
-  - /System/Library/PrivateFrameworks/DropIn.framework/DropIn
-  - /System/Library/PrivateFrameworks/DropInCore.framework/DropInCore
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1587
+  Functions: 1903
   Symbols:   1930
-  CStrings:  3032
+  CStrings:  3049
 
Symbols:
+ __swiftImmortalRefCount
+ _swift_getOpaqueTypeConformance2
- _ANDefaultUserNotificationIncludeRecipients
- _OBJC_CLASS_$_INImage
- _OBJC_CLASS_$_INPerson
- _OBJC_CLASS_$_INPersonHandle
- _OBJC_CLASS_$_INSendMessageIntent
CStrings:
+ "INAnnouncementSoundType"
+ "INReadActionType"
+ "INReadAnnouncementIntentResponseCode"
+ "INSendAnnouncementIntentResponseCode"
+ "INStopAnnouncementIntentResponseCode"
+ "INUserNotificationType"
+ "_updateConnectionForReceivedAnnouncement:groupID:endpointID:"
+ "deliveryFailure"
+ "failureNoHomepod"
+ "failureNoOtherHomepodToReceiveAnnouncements"
+ "failureOnlyAnnouncersDeviceIsAvailable"
+ "failureRecipientCannotReceiveAnnouncements"
+ "failureRecipientHomepodsUpdateRequired"
+ "failureRecipientsAnnouncementsDisabled"
+ "failureRecipientsUnreachable"
+ "failureRemoteAccessNotAllowed"
+ "failureRequiringAppLaunch"
+ "failureSenderAnnouncementsDisabled"
+ "inProgress"
+ "read"
+ "ready"
+ "repeat"
+ "unspecified"
- "imageWithImageData:"
- "initWithPersonHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:"
- "initWithRecipients:outgoingMessageType:content:speakableGroupName:conversationIdentifier:serviceName:sender:attachments:"
- "initWithValue:type:"
- "isCommunicationUserNotificationsEnabled"
- "setAccessoryImageName:"
- "systemImageNamed:"

```
