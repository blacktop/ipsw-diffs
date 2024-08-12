## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1303.100.13.0.0
-  __TEXT.__text: 0x11460c
-  __TEXT.__auth_stubs: 0x26a0
+1305.100.2.2.9
+  __TEXT.__text: 0x114754
+  __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_methlist: 0x3734
   __TEXT.__const: 0xb5a
-  __TEXT.__cstring: 0x381d1
-  __TEXT.__oslogstring: 0x19a45
-  __TEXT.__gcc_except_tab: 0xd2f4
+  __TEXT.__cstring: 0x38331
+  __TEXT.__oslogstring: 0x19a15
+  __TEXT.__gcc_except_tab: 0xd28c
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__unwind_info: 0x4c88
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xaac
-  __TEXT.__objc_methname: 0xfee4
+  __TEXT.__objc_methname: 0xff46
   __TEXT.__objc_methtype: 0x23e1
-  __TEXT.__objc_stubs: 0xd3a0
-  __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x10d10
+  __TEXT.__objc_stubs: 0xd400
+  __DATA_CONST.__got: 0xdd8
+  __DATA_CONST.__const: 0x10d40
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3960
+  __DATA_CONST.__objc_selrefs: 0x3978
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x1360
+  __AUTH_CONST.__auth_got: 0x1368
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x1a88
-  __AUTH_CONST.__cfstring: 0x10a80
+  __AUTH_CONST.__const: 0x1aa8
+  __AUTH_CONST.__cfstring: 0x10b40
   __AUTH_CONST.__objc_const: 0x68a0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __DATA.__bss: 0x3f8
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x17a0
-  __DATA_DIRTY.__data: 0xe58
+  __DATA_DIRTY.__data: 0xe88
   __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4452
+  Functions: 4455
   Symbols:   2307
-  CStrings:  7304
+  CStrings:  7310
 
Symbols:
+ _IMAttachmentEmojiImagePreviewFileURL
+ _IMDMigrateTo18014
+ _IMDMigrateTo18015
- _kUTTypeAudio
- _kUTTypeImage
- _kUTTypeVideo
CStrings:
+ "Failed to load contact plist at: %!@(MISSING) (error: %!@(MISSING))"
+ "SELECT count(rowid) FROM Attachment WHERE is_sticker = 1 AND filename LIKE ?;"
+ "Successfully loaded contact plist at: %!@(MISSING)"
+ "UPDATE message SET is_read = 1, date_read = %!l(MISSING)ld WHERE (is_read == 0 AND is_finished == 1 AND is_from_me == 0 AND item_type == 1 AND is_system_message == 0);"
+ "UPDATE message SET schedule_state = 4 WHERE (is_sent = 0 AND is_from_me = 1 AND error = 39)"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByAppendingPathExtension:"
+ "_notificationsSafePreviewFileURLForTransferURL:utiType:knownSender:"
+ "attachment(is_sticker)"
+ "attachment_idx_is_sticker"
+ "contactFormatterTitle"
+ "dictionaryWithContentsOfURL:error:"
+ "organizationNameTitle"
+ "plist"
- "      chatGroupIDKey: %!@(MISSING)"
- "      chatGroupNameKey: %!@(MISSING) }"
- "   FromChat: { chatChatGUIDKey: %!@(MISSING)"
- "Failed to deserialize contact for message %!@(MISSING), error %!@(MISSING)"
- "SELECT count(rowid) FROM Attachment WHERE filename LIKE ?;"
- "_previewFileURLForTransferURL:utiType:knownSender:"
- "caseInsensitiveCompare:"
- "public.vlocation"

```
