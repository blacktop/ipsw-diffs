## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.300.41.2.7
-  __TEXT.__text: 0x232b78
-  __TEXT.__auth_stubs: 0x46d0
-  __TEXT.__objc_methlist: 0x73b4
+1450.400.3.2.1
+  __TEXT.__text: 0x23353c
+  __TEXT.__auth_stubs: 0x4770
+  __TEXT.__objc_methlist: 0x73cc
   __TEXT.__const: 0xb648
-  __TEXT.__cstring: 0x4873b
-  __TEXT.__oslogstring: 0x1e0c6
-  __TEXT.__gcc_except_tab: 0xd0e4
+  __TEXT.__cstring: 0x4883b
+  __TEXT.__oslogstring: 0x1e1d6
+  __TEXT.__gcc_except_tab: 0xd0f0
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4ec4

   __TEXT.__swift5_fieldmd: 0x2ebc
   __TEXT.__swift5_assocty: 0x548
   __TEXT.__swift5_capture: 0x10e8
-  __TEXT.__swift5_proto: 0x6d0
+  __TEXT.__swift5_proto: 0x6d4
   __TEXT.__swift5_types: 0x340
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x8b30
+  __TEXT.__unwind_info: 0x8b18
   __TEXT.__eh_frame: 0x7348
   __TEXT.__objc_classname: 0x11e5
-  __TEXT.__objc_methname: 0x17c76
-  __TEXT.__objc_methtype: 0x381d
-  __TEXT.__objc_stubs: 0x11c60
-  __DATA_CONST.__got: 0x1770
+  __TEXT.__objc_methname: 0x17d57
+  __TEXT.__objc_methtype: 0x3823
+  __TEXT.__objc_stubs: 0x11d00
+  __DATA_CONST.__got: 0x1780
   __DATA_CONST.__const: 0x8470
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52e0
+  __DATA_CONST.__objc_selrefs: 0x5308
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x2378
-  __AUTH_CONST.__const: 0xa010
-  __AUTH_CONST.__cfstring: 0x12200
+  __AUTH_CONST.__auth_got: 0x23c8
+  __AUTH_CONST.__const: 0xa018
+  __AUTH_CONST.__cfstring: 0x122e0
   __AUTH_CONST.__objc_const: 0xf738
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH.__data: 0x40f0
   __DATA.__objc_ivar: 0x488
   __DATA.__data: 0x2ff8
-  __DATA.__bss: 0xac60
+  __DATA.__bss: 0xac70
   __DATA.__common: 0x198
   __DATA_DIRTY.__objc_data: 0x1620
   __DATA_DIRTY.__data: 0x3d30

   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD561606-5AF8-3C52-9F52-F96AADAE98DE
-  Functions: 10814
-  Symbols:   2580
-  CStrings:  12406
+  UUID: 1B7AAC03-707F-3C8B-BFFC-478B4AE0BC8E
+  Functions: 10815
+  Symbols:   2589
+  CStrings:  12431
 
Symbols:
+ _CGImageDestinationAddImageFromSource
+ _CGImageDestinationCreateWithURL
+ _CGImageDestinationFinalize
+ _CGImageSourceCreateWithData
+ _CGImageSourceCreateWithURL
+ _IMStringIsStewieEmergency
+ _IMStringIsStewieRoadside
+ _OBJC_CLASS_$_UNTextInputNotificationAction
+ _UTTypeJPEG
CStrings:
+ "Can't inspect directory for path: '%s' with error '%@'"
+ "Error transcoding preview image."
+ "Failed to create image destination at URL: %s"
+ "Failed to create image destination with %{private}@"
+ "Failed to create image source from first frame."
+ "Failed to create image source with %{private}@"
+ "Failed to generate a destination URL for first frame of %{private}@"
+ "Failed to read first frame: %@"
+ "MESSAGE_SEND_TO_EMERGENCY_SERVICES_FAILED_FORMAT"
+ "MESSAGE_SEND_TO_ROADSIDE_ASSISTANCE_FAILED_FORMAT"
+ "Send"
+ "Show More"
+ "StorageInspection.StorageInspectionAttachmentDirectory"
+ "Text Message"
+ "URLByAppendingPathExtensionForType:"
+ "URLByDeletingPathExtension"
+ "_includesNotificationReplyActionOnIOS"
+ "_transcodeImageAtURL:toJPEGAtURL:"
+ "actionWithIdentifier:title:options:textInputButtonTitle:textInputPlaceholder:"
+ "com.apple.messages.ReplyAction"
+ "notificationReplyActionOnIOS"
+ "populateUserInfoForNotificationContent:messageBalloonBundleID:payloadData:chatIdentifier:isUrgentMessageTrigger:shouldSuppressNotification:isKnownChat:"
+ "v68@0:8@\"UNMutableNotificationContent\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40^B48^B56B64"
+ "v68@0:8@16@24@32@40^B48^B56B64"
- "Error when copy preview image: [%@]"
- "Failed to copy first frame: %@"
- "Failed to generate a destination URL for a "
- "populateUserInfoForNotificationContent:messageBalloonBundleID:payloadData:chatIdentifier:isUrgentMessageTrigger:shouldSuppressNotification:"
- "v64@0:8@\"UNMutableNotificationContent\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40^B48^B56"
- "v64@0:8@16@24@32@40^B48^B56"

```
