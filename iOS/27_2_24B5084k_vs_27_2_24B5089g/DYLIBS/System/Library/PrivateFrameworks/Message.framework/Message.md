## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3901.200.34.0.0
-  __TEXT.__text: 0xae6a84
-  __TEXT.__objc_methlist: 0x144ac
-  __TEXT.__const: 0x6b7e8
-  __TEXT.__gcc_except_tab: 0x3701c
-  __TEXT.__cstring: 0x314c6
+3901.200.41.0.0
+  __TEXT.__text: 0xae8b68
+  __TEXT.__objc_methlist: 0x144bc
+  __TEXT.__const: 0x6b858
+  __TEXT.__gcc_except_tab: 0x370d4
+  __TEXT.__cstring: 0x314d6
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__oslogstring: 0x27eb0
+  __TEXT.__oslogstring: 0x27ed0
   __TEXT.__ustring: 0x23ca
-  __TEXT.__swift5_typeref: 0x10d0c
+  __TEXT.__swift5_typeref: 0x10d48
   __TEXT.__swift5_capture: 0x33968
   __TEXT.__constg_swiftt: 0xda74
-  __TEXT.__swift5_reflstr: 0xf370
+  __TEXT.__swift5_reflstr: 0xf380
   __TEXT.__swift5_fieldmd: 0x15508
   __TEXT.__swift5_builtin: 0xd70
   __TEXT.__swift5_assocty: 0x1d38
-  __TEXT.__swift5_proto: 0x2a38
+  __TEXT.__swift5_proto: 0x2a40
   __TEXT.__swift5_types: 0x1834
   __TEXT.__swift5_mpenum: 0x7f0
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x32488
-  __TEXT.__eh_frame: 0x1895c
+  __TEXT.__unwind_info: 0x32528
+  __TEXT.__eh_frame: 0x18a7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb8c0
+  __DATA_CONST.__objc_selrefs: 0xb8c8
   __DATA_CONST.__objc_protorefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0xeb8
   __DATA_CONST.__got: 0x2eb0
-  __AUTH_CONST.__const: 0xaccb8
-  __AUTH_CONST.__cfstring: 0x18700
+  __AUTH_CONST.__const: 0xacce0
+  __AUTH_CONST.__cfstring: 0x18740
   __AUTH_CONST.__objc_const: 0x23118
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x9a8

   __AUTH.__objc_data: 0x6418
   __AUTH.__data: 0xb5c8
   __DATA.__objc_ivar: 0x1388
-  __DATA.__data: 0xe948
+  __DATA.__data: 0xe978
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xec9
   __DATA_DIRTY.__objc_data: 0xa50

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 48698
-  Symbols:   26293
-  CStrings:  8545
+  Functions: 48719
+  Symbols:   26297
+  CStrings:  8548
 
Symbols:
+ +[MFMessageCriterion criterionForEmailAddresses:]
+ _associated conformance 15IMAP2Connection6EnableVSHAASQ
+ _symbolic _____7mailbox______7messaget 16IMAP2Persistence15OpaqueMailboxIDV AA0C26PersistedMessageIdentifierV
+ _symbolic ______Say_____G_____t 15IMAP2Connection6EnableV 12NIOIMAPCore210CapabilityV 0A8Protocol8ServerIDV
CStrings:
+ "EXISTS (  SELECT global_message_id     FROM message_attachments LEFT OUTER     JOIN searchable_attachments ON message_attachments.rowid = searchable_attachments.attachment_id     WHERE message_attachments.global_message_id = messages.global_message_id       AND searchable_attachments.attachment_id IS NULL       AND message_attachments.attachment IS NOT NULL )"
+ "[%.*hhx-%{public}s] Did enable capabilities: %{public}s"
+ "[%.*hhx-%{public}s] Received post-auth capabilities from server: %{public}s"
+ "enablingCapabilities"
+ "messages.searchable_message IS NULL"
+ "searchable_messages.message_body_indexed = 0"
+ "searchable_messages.transaction_id IN (%@, %@)"
+ "unauthenticated(enablingCapabilities)"
- "(  messages.searchable_message IS NULL OR   messages.global_message_id IN   (SELECT global_message_id    FROM message_attachments LEFT OUTER    JOIN searchable_attachments       ON ( message_attachments.rowid = searchable_attachments.attachment_id )    WHERE searchable_attachments.attachment_id IS NULL           AND message_attachments.attachment IS NOT NULL   ))"
- "(messages.searchable_message IS NULL OR   searchable_messages.message_body_indexed = 0 OR   searchable_messages.transaction_id IN (%@, %@))"
- "[%.*hhx-%{public}s] Did enable UIDONLY"
- "[%.*hhx-%{public}s] Received capabilities from server"
- "unauthenticated(enablingUIDOnly)"
```
