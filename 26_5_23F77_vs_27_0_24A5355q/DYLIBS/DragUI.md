## DragUI

> `/System/Library/PrivateFrameworks/DragUI.framework/DragUI`

```diff

-9126.2.1.0.0
-  __TEXT.__text: 0x1024
-  __TEXT.__auth_stubs: 0x1b0
+9127.0.66.1.101
+  __TEXT.__text: 0xf10
   __TEXT.__objc_methlist: 0x1f0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x306
+  __TEXT.__cstring: 0x30d
   __TEXT.__oslogstring: 0x76
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x4b7
-  __TEXT.__objc_methtype: 0xfa
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x58
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x488
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A8C579C-FE68-318A-917F-A2397478C6C8
+  UUID: 207D0483-E003-3541-983A-ED9CE0153BC4
   Functions: 39
   Symbols:   211
-  CStrings:  137
+  CStrings:  59
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ _DRLogTarget : 84 -> 68
~ -[DRPasteAnnouncementEndpoint initWithCoder:] : 124 -> 120
~ -[DRPasteAnnouncementEndpoint localizedName] : 56 -> 8
~ +[DRPasteAnnouncementApplicationEndpoint homeScreenEndpoint] : 176 -> 160
~ ___60+[DRPasteAnnouncementApplicationEndpoint homeScreenEndpoint]_block_invoke : 268 -> 252
~ -[DRPasteAnnouncementApplicationEndpoint initWithCoder:] : 180 -> 176
~ -[DRPasteAnnouncementApplicationEndpoint isSimilarToApplicationEndpoint:] : 184 -> 172
~ -[DRPasteAnnouncementContinuityEndpoint deviceName] : 56 -> 8
~ -[DRPasteAnnouncementContinuityEndpoint isSimilarToContinuityEndpoint:] : 192 -> 176
~ -[DRPasteAnnouncement initWithSource:destination:pasteboardUUID:timeout:] : 188 -> 204
~ -[DRPasteAnnouncement initWithCoder:] : 264 -> 252
~ -[DRPasteAnnouncement encodeWithCoder:] : 156 -> 148
~ -[DRPasteAnnouncement _localizedTextRequiringAuthorization:] : 740 -> 708
~ ___60-[DRPasteAnnouncement _localizedTextRequiringAuthorization:]_block_invoke : 96 -> 92
~ -[DRPasteAnnouncement canCoalesceWithAnnouncement:] : 224 -> 208
~ +[DRPasteAnnouncement _canCoalesceEndpoint:withEndpoint:] : 204 -> 208
~ -[DRPasteAnnouncement _localizedTextRequiringAuthorization:].cold.3 : 120 -> 76
CStrings:
- ".cxx_destruct"
- "@\"DRPasteAnnouncementEndpoint\""
- "@\"NSData\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@48@0:8@16@24@32d40"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "DRPasteAnnouncement"
- "DRPasteAnnouncementApplicationEndpoint"
- "DRPasteAnnouncementContinuityEndpoint"
- "DRPasteAnnouncementEndpoint"
- "NSCoding"
- "NSSecureCoding"
- "T@\"DRPasteAnnouncementEndpoint\",R,N,V_destination"
- "T@\"DRPasteAnnouncementEndpoint\",R,N,V_source"
- "T@\"NSData\",R,N,V_persistentIdentifier"
- "T@\"NSString\",R,D,N"
- "T@\"NSString\",R,N"
- "T@\"NSUUID\",R,N,V_pasteboardUUID"
- "TB,R"
- "Td,R,N,V_timeout"
- "_canCoalesceEndpoint:withEndpoint:"
- "_destination"
- "_flags"
- "_initWithLocalizedName:"
- "_localizedName"
- "_localizedTextRequiringAuthorization:"
- "_pasteboardUUID"
- "_persistentIdentifier"
- "_source"
- "_timeout"
- "bundleForClass:"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "canCoalesceWithAnnouncement:"
- "copy"
- "d"
- "d16@0:8"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeObjectOfClass:forKey:"
- "deviceName"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "homeScreenEndpoint"
- "init"
- "initWithCoder:"
- "initWithDeviceName:"
- "initWithLocalizedName:persistentIdentifier:"
- "initWithPersistentIdentifier:"
- "initWithSource:destination:pasteboardUUID:timeout:"
- "isEqual:"
- "isEqualToData:"
- "isSimilarToApplicationEndpoint:"
- "isSimilarToContinuityEndpoint:"
- "localizedAnnouncementText"
- "localizedAuthorizationText"
- "localizedStringForKey:value:table:"
- "localizedStringWithValidatedFormat:validFormatSpecifiers:error:"
- "supportsSecureCoding"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "{?=\"isHomeScreen\"b1}"

```
