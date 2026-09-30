## DragUI

> `/System/Library/PrivateFrameworks/DragUI.framework/DragUI`

```diff

 9126.2.1.0.0
-  __TEXT.__text: 0xf84
-  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__text: 0x1024
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_methlist: 0x1f0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x306
   __TEXT.__oslogstring: 0x76
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_classname: 0x9c
   __TEXT.__objc_methname: 0x4b7
   __TEXT.__objc_methtype: 0xfa

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x488

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 380AAC50-0ED5-3C58-A044-3FCCB7CDB6BD
+  UUID: C4EDD11A-3F9C-358B-B88F-B7E033635CBF
   Functions: 39
-  Symbols:   214
+  Symbols:   211
   CStrings:  137
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_release_x9
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ _DRLogTarget : 68 -> 84
~ -[DRPasteAnnouncementEndpoint initWithCoder:] : 120 -> 124
~ -[DRPasteAnnouncementEndpoint localizedName] : 8 -> 56
~ -[DRPasteAnnouncementApplicationEndpoint initWithLocalizedName:persistentIdentifier:] : 136 -> 128
~ +[DRPasteAnnouncementApplicationEndpoint homeScreenEndpoint] : 160 -> 176
~ ___60+[DRPasteAnnouncementApplicationEndpoint homeScreenEndpoint]_block_invoke : 260 -> 268
~ -[DRPasteAnnouncementApplicationEndpoint initWithCoder:] : 192 -> 180
~ -[DRPasteAnnouncementApplicationEndpoint encodeWithCoder:] : 148 -> 132
~ -[DRPasteAnnouncementApplicationEndpoint isSimilarToApplicationEndpoint:] : 180 -> 184
~ -[DRPasteAnnouncementApplicationEndpoint persistentIdentifier] : 16 -> 8
~ -[DRPasteAnnouncementApplicationEndpoint .cxx_destruct] : 20 -> 12
~ -[DRPasteAnnouncementContinuityEndpoint deviceName] : 8 -> 56
~ -[DRPasteAnnouncementContinuityEndpoint isSimilarToContinuityEndpoint:] : 176 -> 192
~ -[DRPasteAnnouncement initWithSource:destination:pasteboardUUID:timeout:] : 204 -> 188
~ -[DRPasteAnnouncement initWithCoder:] : 252 -> 264
~ -[DRPasteAnnouncement encodeWithCoder:] : 148 -> 156
~ -[DRPasteAnnouncement _localizedTextRequiringAuthorization:] : 708 -> 740
~ ___60-[DRPasteAnnouncement _localizedTextRequiringAuthorization:]_block_invoke : 92 -> 96
~ -[DRPasteAnnouncement canCoalesceWithAnnouncement:] : 208 -> 224
~ +[DRPasteAnnouncement _canCoalesceEndpoint:withEndpoint:] : 208 -> 204

```
