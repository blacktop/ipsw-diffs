## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3816.100.2.0.0
-  __TEXT.__text: 0x551c4c
-  __TEXT.__auth_stubs: 0x43a0
+3818.100.11.2.3
+  __TEXT.__text: 0x55da80
+  __TEXT.__auth_stubs: 0x43c0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
-  __TEXT.__cstring: 0x8cf9
+  __TEXT.__cstring: 0x8dc9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x42570
-  __TEXT.__swift5_typeref: 0xd4ed
-  __TEXT.__swift5_capture: 0x6d28
-  __TEXT.__constg_swiftt: 0xb2d8
-  __TEXT.__swift5_reflstr: 0xcf99
-  __TEXT.__swift5_fieldmd: 0x11944
-  __TEXT.__swift5_proto: 0x2328
-  __TEXT.__swift5_types: 0x13d0
-  __TEXT.__swift5_assocty: 0x18d0
-  __TEXT.__oslogstring: 0xe360
-  __TEXT.__swift5_builtin: 0xcd0
+  __TEXT.__const: 0x42790
+  __TEXT.__swift5_typeref: 0xd501
+  __TEXT.__swift5_capture: 0x80b8
+  __TEXT.__constg_swiftt: 0xb3a4
+  __TEXT.__swift5_reflstr: 0xd029
+  __TEXT.__swift5_fieldmd: 0x11a68
+  __TEXT.__swift5_proto: 0x234c
+  __TEXT.__swift5_types: 0x13dc
+  __TEXT.__swift5_assocty: 0x18e8
+  __TEXT.__oslogstring: 0xe060
+  __TEXT.__swift5_builtin: 0xcf8
   __TEXT.__swift5_mpenum: 0xc88
-  __TEXT.__swift5_protos: 0x6c
+  __TEXT.__swift5_protos: 0x70
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x12e88
-  __TEXT.__eh_frame: 0x194b8
-  __DATA_CONST.__auth_got: 0x21e0
+  __TEXT.__unwind_info: 0x12f90
+  __TEXT.__eh_frame: 0x19350
+  __DATA_CONST.__auth_got: 0x21f0
   __DATA_CONST.__got: 0xb08
-  __DATA_CONST.__auth_ptr: 0x2db8
-  __DATA_CONST.__const: 0x47e60
+  __DATA_CONST.__auth_ptr: 0x2dc0
+  __DATA_CONST.__const: 0x4afb8
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4b30
+  __DATA.__objc_const: 0x4c08
   __DATA.__objc_selrefs: 0x798
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0xe648
-  __DATA.__bss: 0x450b0
+  __DATA.__data: 0xe700
+  __DATA.__bss: 0x454b0
   __DATA.__common: 0xcb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 28726
+  Functions: 29135
   Symbols:   444
-  CStrings:  2949
+  CStrings:  2955
 
CStrings:
+ " in body structure"
+ " inside quoted in body structure"
+ "%!s(MISSING): received %!{(MISSING)iec-bytes}ld, sent %!{(MISSING)iec-bytes}ld, messages indexed %!l(MISSING)d, updated flags %!l(MISSING)d, deleted messages %!l(MISSING)d, complete re-index %!l(MISSING)d, message re-index requests %!l(MISSING)d, over quota count %!l(MISSING)d, was unavailable: %!{(MISSING)BOOL}d"
+ "Extended search response has no UIDs."
+ "Managed object (message) was unregistered, probably deleted. Not marking as “indexing complete” for #%!l(MISSING)lu."
+ "Received unknown extended search response with tag '%!{(MISSING)public}s'."
+ "Start B {%!l(MISSING)d} for %!l(MISSING)d account(s)"
+ "Unexpected byte "
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Server temporarily unavailable."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication failed: %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID batch(es): %!{(MISSING)public}s, fetching highest-mod-seq: %!{(MISSING)BOOL}d"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d missing UIDs, adding %!l(MISSING)d UIDs as missing: ... %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d missing UIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d UIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d UIDs: ... %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d pending expunge, %!l(MISSING)d remaining."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed all %!l(MISSING)d changes without UID."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed for range #%!l(MISSING)d, but server never sent a response. rdar://127003347"
+ "[%!(BADPREC)%!h(MISSING)hx] [MailboxesToSelect] None."
+ "[%!l(MISSING)lu] {%!l(MISSING)d} Download & index is currently unavailable."
+ "[%!{(MISSING)public}s] Received server-unavailable for unknown account."
+ "[%!{(MISSING)public}s] Received server-unavailable, but the account has no active sync."
+ "[%!{(MISSING)public}s] Received server-unavailable. Completing sync #%!u(MISSING)."
+ "[%!{(MISSING)public}s] Server was recently unavailable."
+ "[{%!(BADPREC)%!h(MISSING)x}%!{(MISSING)sensitive,mask.mailbox}s] [MailboxesToSelect] %!h(MISSING)hu/%!h(MISSING)hu: %!{(MISSING)public}s - %!{(MISSING)public}s"
+ "_TtCV13IMAP2Behavior14StateWithTasks30MailboxesToSelectLoggingHelper"
+ "currentlyUnavailable"
+ "ed"
+ "previous"
+ "serverDidNotifyUnavailable"
+ "userInitiatedDownload("
+ "userInitiatedSearch("
+ "{%!l(MISSING)d} No account are currently available."
- "%!s(MISSING): received %!{(MISSING)iec-bytes}ld, sent %!{(MISSING)iec-bytes}ld, messages indexed %!l(MISSING)d, updated flags %!l(MISSING)d, deleted messages %!l(MISSING)d, complete re-index %!l(MISSING)d, message re-index requests %!l(MISSING)d"
- "Start B {%!l(MISSING)d}"
- "Unexpected byte in body structure"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Authentication failed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetched window: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges, %!l(MISSING)d UIDs total."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, no ranges to request."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Extended search completed, but server never sent a response. rdar://127003347"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in UID range #%!l(MISSING)d %!s(MISSING) from server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in fetched window %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox is empty. DetectChangesToMessages will not do any updates."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Not removing any messages in fetched window %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d messages in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d pending expunge, %!l(MISSING)d left."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed UIDs %!{(MISSING)public}s in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed all changes without UID."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed no messages in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing  %!l(MISSING)d messages in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping %!l(MISSING)d number of UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping UIDs %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!s(MISSING) in range #%!l(MISSING)d %!s(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!{(MISSING)public}s in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing unknown messages in range #%!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed without any UIDs"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed. Found %!l(MISSING)d UIDs locally, %!l(MISSING)d on server in range %!{(MISSING)public}s."
- "userInitiatedDownload"
- "userInitiatedSearch"

```
