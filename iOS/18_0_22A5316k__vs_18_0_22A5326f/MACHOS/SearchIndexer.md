## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3814.100.5.2.3
-  __TEXT.__text: 0x5420f4
-  __TEXT.__auth_stubs: 0x4380
+3816.100.2.0.0
+  __TEXT.__text: 0x551c4c
+  __TEXT.__auth_stubs: 0x43a0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
-  __TEXT.__cstring: 0x8cfa
+  __TEXT.__cstring: 0x8cf9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x42390
-  __TEXT.__swift5_typeref: 0xd393
-  __TEXT.__swift5_capture: 0x6ab8
-  __TEXT.__constg_swiftt: 0xb260
-  __TEXT.__swift5_reflstr: 0xd00d
-  __TEXT.__swift5_fieldmd: 0x118fc
-  __TEXT.__swift5_proto: 0x230c
-  __TEXT.__swift5_types: 0x13b8
+  __TEXT.__const: 0x42570
+  __TEXT.__swift5_typeref: 0xd4ed
+  __TEXT.__swift5_capture: 0x6d28
+  __TEXT.__constg_swiftt: 0xb2d8
+  __TEXT.__swift5_reflstr: 0xcf99
+  __TEXT.__swift5_fieldmd: 0x11944
+  __TEXT.__swift5_proto: 0x2328
+  __TEXT.__swift5_types: 0x13d0
   __TEXT.__swift5_assocty: 0x18d0
-  __TEXT.__oslogstring: 0xda50
-  __TEXT.__swift5_builtin: 0xcbc
-  __TEXT.__swift5_mpenum: 0xc5c
+  __TEXT.__oslogstring: 0xe360
+  __TEXT.__swift5_builtin: 0xcd0
+  __TEXT.__swift5_mpenum: 0xc88
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0x171f
+  __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x12d08
-  __TEXT.__eh_frame: 0x193b8
-  __DATA_CONST.__auth_got: 0x21d0
-  __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__auth_ptr: 0x2d70
-  __DATA_CONST.__const: 0x47288
+  __TEXT.__unwind_info: 0x12e88
+  __TEXT.__eh_frame: 0x194b8
+  __DATA_CONST.__auth_got: 0x21e0
+  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__auth_ptr: 0x2db8
+  __DATA_CONST.__const: 0x47e60
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4bb0
-  __DATA.__objc_selrefs: 0x788
-  __DATA.__objc_data: 0x980
-  __DATA.__data: 0xe6e8
-  __DATA.__bss: 0x44d30
-  __DATA.__common: 0xcc0
+  __DATA.__objc_const: 0x4b30
+  __DATA.__objc_selrefs: 0x798
+  __DATA.__objc_data: 0x930
+  __DATA.__data: 0xe648
+  __DATA.__bss: 0x450b0
+  __DATA.__common: 0xcb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 28535
-  Symbols:   436
-  CStrings:  2936
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 28726
+  Symbols:   444
+  CStrings:  2949
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Account message count %!l(MISSING)d -> %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!(BADPREC)%!X(MISSING)] Account message count unchanged at %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!{(MISSING)public}s IDLE completed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!{(MISSING)public}s IDLE is %!l(MISSING)d seconds old (< %!l(MISSING)d). Not refreshing."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!{(MISSING)public}s NOOP completed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Command %!{(MISSING)public}s completed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Command with unknown tag %!{(MISSING)public}s completed."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld (of total %!{(MISSING)iec-bytes}ld) from output buffer to network (tag %!{(MISSING)public}s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld (of total %!{(MISSING)iec-bytes}ld) from output buffer to network (tags %!{(MISSING)public}s - %!{(MISSING)public}s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld from output buffer to network (tag %!{(MISSING)public}s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld from output buffer to network (tags %!{(MISSING)public}s - %!{(MISSING)public}s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Path did change. Constrained: %!{(MISSING)BOOL}d"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Received 'S: %!{(MISSING)public}s %!{(MISSING)public}s %!s(MISSING)' from network."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Received 'S: %!{(MISSING)public}s %!{(MISSING)public}s %!s(MISSING)' from network. Server is temporarily unavailable."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending IDLE as %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending NOOP as %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sent '%!{(MISSING)public}s' command as %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Server is temporarily unavailable."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d messages have flag changes after copy"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d new message(s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d remaining known-to-be-missing. Requesting FindMissingMessages to re-run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] APPEND failed with “No, try create”."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] APPEND failed: %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] APPEND succeeded with UID %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] APPEND succeeded without UIDValidity."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d messages (out of %!l(MISSING)d) to download."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d new UID(s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d sections for message %!u(MISSING). Downloading message headers: %!{(MISSING)BOOL}d"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Adding %!{(MISSING)public}s (%!l(MISSING)d out of %!l(MISSING)d) to download."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Attempting to store HIGHESTMODSEQ, but PendingServerResponses does not support CONDSTORE."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Clearing local HIGHESTMODSEQ."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Clearing window of interest"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed '%!{(MISSING)public}s' (%!{(MISSING)public}s, #%!u(MISSING))"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed action '%!{(MISSING)public}s' (#%!u(MISSING))"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed download for message %!u(MISSING), but we don’t have a body structure for this message."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed download of %!l(MISSING)d sections for message %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed fetching Body Structure for messages %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created %!l(MISSING)d message batches: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task for %!{(MISSING)public}s %!s(MISSING) '%!{(MISSING)public}s'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task for %!{(MISSING)public}s %!s(MISSING) '%!{(MISSING)public}s' -- full message download for %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task for search #%!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task purging UIDs %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task querying in UIDs %!{(MISSING)public}s. Server unread count %!l(MISSING)d"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task with fetched-window %!s(MISSING) (persisted) -> %!u(MISSING) (new)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task with fetched-window-update %!s(MISSING), ranges %!s(MISSING), UID limit: %!l(MISSING)d, grow: %!u(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task with missing %!l(MISSING)d, batch %!l(MISSING)d UIDs %!{(MISSING)public}s, fetched-window %!s(MISSING) (persisted) -> %!u(MISSING) (new)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID batch(es): %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID(s) vanished in range %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID(s) vanished: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UIDs total, %!l(MISSING)d UIDs to fetch."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UIDs total, no UIDs to fetch."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d identifier(s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Excluding %!l(MISSING)d, UIDs %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Excluding UIDs %!{(MISSING)public}s, %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetched window: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges, %!l(MISSING)d UIDs total."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, no ranges to request."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Local UID validity: 0x%!x(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. No messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Not purging any messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Not querying server."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Server supports move: %!{(MISSING)BOOL}d"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Using fixed range(s): %!{(MISSING)public}s (batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query local persistence (message count: %!l(MISSING)d, batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query server. (batch size: %!l(MISSING)d)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. highest-mod-seq local: %!l(MISSING)lu, changes without UID: %!l(MISSING)d, server: %!l(MISSING)lu"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Creating UID ranges from UIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Creating UID ranges from UIDs: %!{(MISSING)public}s (window of interest: %!{(MISSING)public}s)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Data length %!l(MISSING)d > %!u(MISSING) (segment length)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did delete all existing local messages due to validity change: 0x%!x(MISSING) → 0x%!x(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did mark as sync complete."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did not get any UIDs"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did not remove any pending expunge."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did not search for unread messages. Server unread count %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Did upload flags for %!l(MISSING)d messages"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Done. Still %!l(MISSING)d vanished UID(s) remaining in range %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Done. Still %!l(MISSING)d vanished UID(s) remaining: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Expunging deleted messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Extended search completed, but server never sent a response. rdar://127003347"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Failed to delete %!l(MISSING)d messages after uploading flag changes"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Failed to delete %!l(MISSING)d messages with UIDs %!{(MISSING)public}s after uploading flag changes"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Failed to determine message batches"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Failed to find unread messages (UIDs %!{(MISSING)public}s). Server unread count %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in UID range #%!l(MISSING)d %!s(MISSING) from server."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in fetched window %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Fetching headers for message %!u(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs %!{(MISSING)public}s to be missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs locally in window %!{(MISSING)public}s, %!l(MISSING)d on server."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs locally, %!l(MISSING)d on server."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d new UIDs missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d new UIDs on server. Querying server.."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d unread messages in UIDs %!{(MISSING)public}s. Server unread count %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d unread messages. Server unread count %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found no UIDs to be missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Found window of interest: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Got %!l(MISSING)d flag/label changes."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Grouped the local flag changes into %!l(MISSING)d message sets. Expecting %!l(MISSING)d commands."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Ignoring UID %!u(MISSING) outside of range-of-interest %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Ignoring message data."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Limiting server UIDs to %!l(MISSING)d UIDs in range %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Limiting server UIDs to %!l(MISSING)d UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Local mailbox is empty. Removed %!l(MISSING)d pending expunge."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox is empty. DetectChangesToMessages will not do any updates."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking flag changes upload as “has dependencies”."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking mailbox '%!{(MISSING)sensitive,mask.mailbox}s' as needing to run find-missing-messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking mailbox as needing to run upload-messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking no more flag changes pending upload."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking no more messages needing move or copy."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking source messages %!{(MISSING)public}s as deleted."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking step %!s(MISSING) as complete."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Marking task as complete."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Missing: %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No Message UID found."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No change to local HIGHESTMODSEQ."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No flag changes for messages %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No header data in response for '%!{(MISSING)public}s'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No missing message; fetched window upper bound: %!u(MISSING), queriedUIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] No missing message; fetched-window upper bound: nil, queriedUIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Not removing any messages in fetched window %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Number of changes to-be-sent to the persistence: %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Only found %!l(MISSING)d UIDs locally but %!l(MISSING)d on server. Querying server for message batches."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more flag changes to upload. Will mark as needing to re-run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more messages to move/copy. Will mark as needing to re-run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more messages to upload. Will mark as needing to re-run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d (min:  %!u(MISSING), max: %!u(MISSING)) messages to download."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d UIDs in range %!{(MISSING)public}s as newest UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d moves / copies."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned UIDs %!{(MISSING)public}s to download."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned empty list as newest UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned no messages to download."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Pruning. No mailbox affinity, not targeting mailboxes-to-be-selected."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received %!l(MISSING)d UIDs for temporarily growing window-of-interest: %!{(MISSING)public}s (did query %!{(MISSING)public}s)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received 'BAD %!s(MISSING)'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received 'NO %!s(MISSING)'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received body structure for message %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received bytes in range %!s(MISSING) -- some of which have previously been received: %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received local flag changes for %!l(MISSING)d messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d EXPUNGE messages, still %!l(MISSING)d remaining."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d changes without UID, still %!l(MISSING)d remaining."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d messages in %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d pending expunge, %!l(MISSING)d left."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed UIDs %!{(MISSING)public}s in %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed all %!l(MISSING)d EXPUNGE messages."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed all changes without UID."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removed no messages in %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing  %!l(MISSING)d messages in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d deleted messages after uploading flag changes"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d deleted messages with UIDs %!{(MISSING)public}s after uploading flag changes"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping %!l(MISSING)d number of UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping UIDs %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing all messages pending upload."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!s(MISSING) in range #%!l(MISSING)d %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!{(MISSING)public}s in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Removing unknown messages in range #%!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING) -- but sections for this message have already been added."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING), but we don’t have a body structure for this message."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requesting re-run after initial run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requesting re-run."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Requesting sections to download for message %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed for range #%!l(MISSING)d %!{(MISSING)public}s. Got %!l(MISSING)d UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed for range #%!l(MISSING)d. Got %!l(MISSING)d UIDs."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed without any UIDs"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search completed. Found %!l(MISSING)d UIDs locally, %!l(MISSING)d on server in range %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Search returned %!l(MISSING)d UIDs for search #%!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Sent %!l(MISSING)d changes to the persistence."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Sent '%!{(MISSING)public}s' %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Sent '%!{(MISSING)public}s' command as %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server completed %!{(MISSING)public}s of messages %!{(MISSING)public}s with destination UIDs %!{(MISSING)public}s and UIDValidity 0x%!x(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server completed %!{(MISSING)public}s of messages %!{(MISSING)public}s without destination UIDs"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server completed move of messages %!{(MISSING)public}s with destination UIDs"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server did not return any data for message %!u(MISSING), part '[%!{(MISSING)public}s]', ranges %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server did not return header data for message %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server failed to %!{(MISSING)public}s messages %!{(MISSING)public}s: %!{(MISSING)public}s %!s(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Server moved messages %!{(MISSING)public}s with destination UIDs %!{(MISSING)public}s and UIDValidity 0x%!x(MISSING)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Setting mailbox HIGHESTMODSEQ to %!l(MISSING)lu."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Setting window of interest: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Still missing %!l(MISSING)d messages (%!l(MISSING)d completed). Will run again."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Task is completing, but not done."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Total missing message count: %!l(MISSING)d; %!l(MISSING)d done; fetched-window upper bound: %!u(MISSING), queriedUIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Total missing message count: %!l(MISSING)d; %!l(MISSING)d done; fetched-window upper bound: nil, queriedUIDs: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Trying to add message-to-skip, but mailbox has no UID validity."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING), size %!{(MISSING)iec-bytes}ld"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING), unknown size"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Adding '%!{(MISSING)public}s/%!{(MISSING)public}s' section '[%!{(MISSING)public}s]' (%!{(MISSING)iec-bytes}ld)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Adding multi-part '%!s(MISSING)' section '[%!{(MISSING)public}s]' (approx. %!{(MISSING)iec-bytes}ld)"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): All data for section '%!{(MISSING)public}s' has been received."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Forwarding %!l(MISSING)d bytes for section '[%!{(MISSING)public}s]' to the persistence."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received %!l(MISSING)d bytes (offset %!u(MISSING)) for section '%!{(MISSING)public}s'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received %!l(MISSING)d bytes for section '%!{(MISSING)public}s'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received BodySection with NIL data for section '%!{(MISSING)public}s', but we already have all data. Ignoring."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received BodySection with NIL data for section '%!{(MISSING)public}s'. Message may have been deleted."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received body section data for section '%!{(MISSING)public}s'"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Section '[%!{(MISSING)public}s]' not found in complete body structure."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Unable to append body section data for UID %!u(MISSING). Marking as failed. (%!@(MISSING))"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Unexpectedly received multiple .uploadMessages"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating fetched-window to %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating local HIGHESTMODSEQ to %!l(MISSING)lu."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating server next UID to %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating sync state next UID to %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] User search did fail."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] User search failed with BAD %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] User search failed with NO %!s(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] [%!{(MISSING)sensitive,mask.mailbox}s] Copying messages %!{(MISSING)public}s."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Flag change has no UID and no sequence number."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Flag/label change without UID and without sequence number."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Inserting flag/label change for UID %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Inserting flag/label change without UID. Sequence number %!u(MISSING)."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox has pending updates while being deselected."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox supports CONDSTORE, but flag change has no MODSEQ."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received expunge %!u(MISSING), but mMessage is already zero."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received expunge %!u(MISSING). Message count is now %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received vanished (earlier) for %!l(MISSING)d UID(s)."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Received vanished for %!l(MISSING)d UID(s). Message count is now %!l(MISSING)d."
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating highest mod-seq to %!l(MISSING)lu"
+ "[%!(BADPREC)%!h(MISSING)hx-{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Updating message count to %!u(MISSING)"
+ "messagesInLargestAccount"
+ "primitiveMessageCount"
+ "primitiveMessageCount"
+ "setPrimitiveMessageCount:"
+ "tag: %!{(MISSING)public}s response: %!h(MISSING)hu"
+ "tag: %!{(MISSING)public}s, name: %!s(MISSING) %!u(MISSING) %!u(MISSING) %!u(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!s(MISSING) IDLE completed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!s(MISSING) IDLE is %!l(MISSING)d seconds old (< %!l(MISSING)d). Not refreshing."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!s(MISSING) NOOP completed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] '%!{(MISSING)sensitive,mask.mailbox}s' Did mark as sync complete."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Command %!s(MISSING) completed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Command with unknown tag %!s(MISSING) completed."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld (of total %!{(MISSING)iec-bytes}ld) from output buffer to network (tag %!s(MISSING))."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld (of total %!{(MISSING)iec-bytes}ld) from output buffer to network (tags %!s(MISSING) - %!s(MISSING))."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld from output buffer to network (tag %!s(MISSING))."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Flushing %!{(MISSING)iec-bytes}ld from output buffer to network (tags %!s(MISSING) - %!s(MISSING))."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Received 'S: %!s(MISSING) %!{(MISSING)public}s %!s(MISSING)' from network."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending IDLE as %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sending NOOP as %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] Sent '%!{(MISSING)public}s' command as %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d messages have flag changes after copy"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d new message(s)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] %!l(MISSING)d remaining known-to-be-missing. Requesting FindMissingMessages to re-run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] APPEND failed with “No, try create”."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] APPEND failed: %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] APPEND succeeded with UID %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] APPEND succeeded without UIDValidity."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d messages (out of %!l(MISSING)d) to download."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d new UID(s)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Adding %!l(MISSING)d sections for message %!u(MISSING). Downloading message headers: %!{(MISSING)BOOL}d"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Adding %!{(MISSING)public}s (%!l(MISSING)d out of %!l(MISSING)d) to download."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Attempting to store HIGHESTMODSEQ, but PendingServerResponses does not support CONDSTORE."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Clearing local HIGHESTMODSEQ."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Clearing window of interest"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Completed download for message %!u(MISSING), but we don’t have a body structure for this message."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Completed download of %!l(MISSING)d sections for message %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Completed fetching Body Structure for messages %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created %!l(MISSING)d message batches: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task for %!{(MISSING)public}s %!s(MISSING) '%!{(MISSING)public}s'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task for %!{(MISSING)public}s %!s(MISSING) '%!{(MISSING)public}s' -- full message download for %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task for search #%!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task purging UIDs %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task querying in UIDs %!{(MISSING)public}s. Server unread count %!l(MISSING)d"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task with fetched-window %!s(MISSING) (persisted) -> %!u(MISSING) (new)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task with fetched-window-update %!s(MISSING), ranges %!s(MISSING), UID limit: %!l(MISSING)d, grow: %!u(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task with missing %!l(MISSING)d, batch %!l(MISSING)d UIDs %!{(MISSING)public}s, fetched-window %!s(MISSING) (persisted) -> %!u(MISSING) (new)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID batche(s): %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID(s) vanished in range %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UID(s) vanished: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UIDs total, %!l(MISSING)d UIDs to fetch."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d UIDs total, no UIDs to fetch."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. %!l(MISSING)d identifier(s)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Excluding %!l(MISSING)d, UIDs %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Excluding UIDs %!{(MISSING)public}s, %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetched window: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges, %!l(MISSING)d UIDs total."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, %!l(MISSING)d UID ranges: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Fetching highest-mod-seq: %!{(MISSING)BOOL}d, no ranges to request."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Local UID validity: 0x%!x(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. No messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Not purging any messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Not querying server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Server supports move: %!{(MISSING)BOOL}d"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Using fixed range(s): %!{(MISSING)public}s (batch size: %!l(MISSING)d)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query local persistence (message count: %!l(MISSING)d, batch size: %!l(MISSING)d)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. Will query server. (batch size: %!l(MISSING)d)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Created task. highest-mod-seq local: %!l(MISSING)lu, changes without UID: %!l(MISSING)d, server: %!l(MISSING)lu"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Creating UID ranges from UIDs: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Creating UID ranges from UIDs: %!{(MISSING)public}s (window of interest: %!{(MISSING)public}s)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Data length %!l(MISSING)d > %!u(MISSING) (segment length)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Did delete all existing local messages due to validity change: 0x%!x(MISSING) → 0x%!x(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Did not get any UIDs"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Did not remove any pending expunge."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Did not search for unread messages. Server unread count %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Did upload flags for %!l(MISSING)d messages"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Done. Still %!l(MISSING)d vanished UID(s) remaining in range %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Done. Still %!l(MISSING)d vanished UID(s) remaining: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Expunging deleted messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Extended search completed, but server never sent a response. rdar://127003347"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Failed to delete %!l(MISSING)d messages after uploading flag changes"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Failed to delete %!l(MISSING)d messages with UIDs %!{(MISSING)public}s after uploading flag changes"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Failed to determine message batches"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Failed to find unread messages (UIDs %!{(MISSING)public}s). Server unread count %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in UID range #%!l(MISSING)d %!s(MISSING) from server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Fetch completed. Got %!l(MISSING)d messages in fetched window %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Fetching headers for message %!u(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs %!{(MISSING)public}s to be missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs locally in window %!{(MISSING)public}s, %!l(MISSING)d on server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d UIDs locally, %!l(MISSING)d on server."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d new UIDs missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d new UIDs on server. Querying server.."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d unread messages in UIDs %!{(MISSING)public}s. Server unread count %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found %!l(MISSING)d unread messages. Server unread count %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found no UIDs to be missing locally. (%!l(MISSING)d locally, %!l(MISSING)d on server)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Found window of interest: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Got %!l(MISSING)d flag/label changes."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Grouped the local flag changes into %!l(MISSING)d message sets. Expecting %!l(MISSING)d commands."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Ignoring UID %!u(MISSING) outside of range-of-interest %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Ignoring message data."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Limiting server UIDs to %!l(MISSING)d UIDs in range %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Limiting server UIDs to %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Local mailbox is empty. Removed %!l(MISSING)d pending expunge."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Mailbox is empty. DetectChangesToMessages will not do any updates."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking flag changes upload as “has dependencies”."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking mailbox '%!{(MISSING)sensitive,mask.mailbox}s' as needing to run find-missing-messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking mailbox as needing to run upload-messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking no more flag changes pending upload."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking no more messages needing move or copy."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking source messages %!{(MISSING)public}s as deleted."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking step %!s(MISSING) as complete."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Marking task as complete."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Missing: %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No Message UID found."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No change to local HIGHESTMODSEQ."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No flag changes for messages %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No header data in response for '%!{(MISSING)public}s'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No missing message; fetched window upper bound: %!u(MISSING), queriedUIDs: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] No missing message; fetched-window upper bound: nil, queriedUIDs: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Not removing any messages in fetched window %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Number of changes to-be-sent to the persistence: %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Only found %!l(MISSING)d UIDs locally but %!l(MISSING)d on server. Querying server for message batches."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more flag changes to upload. Will mark as needing to re-run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more messages to move/copy. Will mark as needing to re-run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence has more messages to upload. Will mark as needing to re-run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d (min:  %!u(MISSING), max: %!u(MISSING)) messages to download."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d UIDs in range %!{(MISSING)public}s as newest UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned %!l(MISSING)d moves / copies."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned UIDs %!{(MISSING)public}s to download."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned empty list as newest UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Persistence returned no messages to download."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received %!l(MISSING)d UIDs for temporarily growing window-of-interest: %!{(MISSING)public}s (did query %!{(MISSING)public}s)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received 'BAD %!s(MISSING)'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received 'NO %!s(MISSING)'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received body structure for message %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received bytes in range %!s(MISSING) -- some of which have previously been received: %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Received local flag changes for %!l(MISSING)d messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d EXPUNGE messages, still %!l(MISSING)d remaining."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d changes without UID, still %!l(MISSING)d remaining."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d messages in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed %!l(MISSING)d pending expunge, %!l(MISSING)d left."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed UIDs %!{(MISSING)public}s in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed all %!l(MISSING)d EXPUNGE messages."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed all changes without UID."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removed no messages in %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing  %!l(MISSING)d messages in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d deleted messages after uploading flag changes"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d deleted messages with UIDs %!{(MISSING)public}s after uploading flag changes"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping %!l(MISSING)d number of UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing %!l(MISSING)d messages in %!{(MISSING)public}s, keeping UIDs %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing all messages pending upload."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!{(MISSING)public}s in fetched window %!{(MISSING)public}s, keeping %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing unknown messages in range #%!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING) -- but sections for this message have already been added."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING), but we don’t have a body structure for this message."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requested to download %!l(MISSING)d sections for message %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requesting re-run after initial run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requesting re-run."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Requesting sections to download for message %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Search completed for range #%!l(MISSING)d %!{(MISSING)public}s. Got %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Search completed for range #%!l(MISSING)d. Got %!l(MISSING)d UIDs."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Search completed without any UIDs"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Search completed. Found %!l(MISSING)d UIDs locally, %!l(MISSING)d on server in range %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Search returned %!l(MISSING)d UIDs for search #%!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Sent %!l(MISSING)d changes to the persistence."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server completed %!{(MISSING)public}s of messages %!{(MISSING)public}s with destination UIDs %!{(MISSING)public}s and UIDValidity 0x%!x(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server completed %!{(MISSING)public}s of messages %!{(MISSING)public}s without destination UIDs"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server completed move of messages %!{(MISSING)public}s with destination UIDs"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server did not return any data for message %!u(MISSING), part '[%!{(MISSING)public}s]', ranges %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server did not return header data for message %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server failed to %!{(MISSING)public}s messages %!{(MISSING)public}s: %!{(MISSING)public}s %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Server moved messages %!{(MISSING)public}s with destination UIDs %!{(MISSING)public}s and UIDValidity 0x%!x(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Setting mailbox HIGHESTMODSEQ to %!l(MISSING)lu."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Setting window of interest: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Still missing %!l(MISSING)d messages (%!l(MISSING)d completed). Will run again."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Task is completing, but not done."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Total missing message count: %!l(MISSING)d; %!l(MISSING)d done; fetched-window upper bound: %!u(MISSING), queriedUIDs: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Total missing message count: %!l(MISSING)d; %!l(MISSING)d done; fetched-window upper bound: nil, queriedUIDs: %!{(MISSING)public}s"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Trying to add message-to-skip, but mailbox has no UID validity."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING), size %!{(MISSING)iec-bytes}ld"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING), unknown size"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Adding '%!{(MISSING)public}s/%!{(MISSING)public}s' section '[%!{(MISSING)public}s]' (%!{(MISSING)iec-bytes}ld)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Adding multi-part '%!s(MISSING)' section '[%!{(MISSING)public}s]' (approx. %!{(MISSING)iec-bytes}ld)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): All data for section '%!{(MISSING)public}s' has been received."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Forwarding %!l(MISSING)d bytes for section '[%!{(MISSING)public}s]' to the persistence."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received %!l(MISSING)d bytes (offset %!u(MISSING)) for section '%!{(MISSING)public}s'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received %!l(MISSING)d bytes for section '%!{(MISSING)public}s'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received BodySection with NIL data for section '%!{(MISSING)public}s', but we already have all data. Ignoring."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received BodySection with NIL data for section '%!{(MISSING)public}s'. Message may have been deleted."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Received body section data for section '%!{(MISSING)public}s'"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] UID %!u(MISSING): Section '[%!{(MISSING)public}s]' not found in complete body structure."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Unable to append body section data for UID %!u(MISSING). Marking as failed. (%!@(MISSING))"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Unexpectedly received multiple .uploadMessages"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Updating local HIGHESTMODSEQ to %!l(MISSING)lu."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Updating server next UID to %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] Updating sync state next UID to %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] User search did fail."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] User search failed with BAD %!s(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] User search failed with NO %!s(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] [%!{(MISSING)sensitive,mask.mailbox}s] Copying messages %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] [%!{(MISSING)sensitive,mask.mailbox}s] Removing messages %!s(MISSING) in range #%!l(MISSING)d %!s(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [%!{(MISSING)sensitive,mask.mailbox}s] [%!{(MISSING)sensitive,mask.mailbox}s] Updating fetched-window to %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Flag change has no UID and no sequence number."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Flag/label change without UID and without sequence number."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Inserting flag/label change for UID %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Inserting flag/label change without UID. Sequence number %!u(MISSING)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox has pending updates while being deselected."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Mailbox supports CONDSTORE, but flag change has no MODSEQ."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Received expunge %!u(MISSING), but mMessage is already zero."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Received expunge %!u(MISSING). Message count is now %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Received vanished (earlier) for %!l(MISSING)d UID(s)."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Received vanished for %!l(MISSING)d UID(s). Message count is now %!l(MISSING)d."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Updating highest mod-seq to %!l(MISSING)lu"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)sensitive,mask.mailbox}s] Updating message count to %!u(MISSING)"
- "_TtCVV13IMAP2Behavior5State12LocalMailbox6Logger"
- "tag: %!s(MISSING) response: %!h(MISSING)hu"
- "tag: %!s(MISSING), name: %!s(MISSING) %!u(MISSING) %!u(MISSING) %!u(MISSING)"

```
