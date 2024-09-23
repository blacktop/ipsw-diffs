## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.200.67.0.0
-  __TEXT.__text: 0x5628e0
+3826.200.84.0.0
+  __TEXT.__text: 0x5654cc
   __TEXT.__auth_stubs: 0x43c0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
-  __TEXT.__cstring: 0x8dd9
+  __TEXT.__cstring: 0x8de9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x429d0
-  __TEXT.__swift5_typeref: 0xd58f
-  __TEXT.__swift5_capture: 0x80a8
-  __TEXT.__constg_swiftt: 0xb4ac
-  __TEXT.__swift5_reflstr: 0xd0f9
-  __TEXT.__swift5_fieldmd: 0x11bd8
-  __TEXT.__swift5_proto: 0x236c
-  __TEXT.__swift5_types: 0x13f8
+  __TEXT.__const: 0x42a90
+  __TEXT.__swift5_typeref: 0xd573
+  __TEXT.__swift5_capture: 0x8258
+  __TEXT.__constg_swiftt: 0xb47c
+  __TEXT.__swift5_reflstr: 0xd149
+  __TEXT.__swift5_fieldmd: 0x11be8
+  __TEXT.__swift5_proto: 0x2368
+  __TEXT.__swift5_types: 0x13f0
   __TEXT.__swift5_assocty: 0x18e8
-  __TEXT.__oslogstring: 0xe160
+  __TEXT.__oslogstring: 0xe2a0
   __TEXT.__swift5_builtin: 0xd20
-  __TEXT.__swift5_mpenum: 0xcac
+  __TEXT.__swift5_mpenum: 0xcc0
   __TEXT.__swift5_protos: 0x74
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x12bf8
-  __TEXT.__eh_frame: 0x19410
+  __TEXT.__unwind_info: 0x12c40
+  __TEXT.__eh_frame: 0x19470
   __DATA_CONST.__auth_got: 0x21f0
   __DATA_CONST.__got: 0xb08
   __DATA_CONST.__auth_ptr: 0x2de8
-  __DATA_CONST.__const: 0x4b390
+  __DATA_CONST.__const: 0x4b370
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_const: 0x4bc8
   __DATA.__objc_selrefs: 0x798
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0xe750
-  __DATA.__bss: 0x45830
-  __DATA.__common: 0xc98
+  __DATA.__data: 0xe800
+  __DATA.__bss: 0x457b0
+  __DATA.__common: 0xcb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 29220
+  Functions: 29221
   Symbols:   444
-  CStrings:  2953
+  CStrings:  2956
 
CStrings:
+ "[%!(BADPREC)%!h(MISSING)hx] [1st connection] Running sync requests %!l(MISSING)d: {%!{(MISSING)public}s}, kinds: %!{(MISSING)public}s; App state: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx] Cancelling idle connection %!{(MISSING)public}s."
+ "APPENDLIMIT"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!{(MISSING)public}s IDLE is %!f(MISSING) seconds old (< %!f(MISSING)). Not refreshing."
+ "[%!(BADPREC)%!h(MISSING)hx] {%!l(MISSING)d} [1st connection] Mailbox: {%!(BADPREC)%!h(MISSING)x} '%!{(MISSING)sensitive,mask.mailbox}s' %!{(MISSING)public}s, %!{(MISSING)public}s, {%!{(MISSING)public}s} last sync:  {local: %!{(MISSING)public}s, remote: %!{(MISSING)public}s}"
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Local UID validity: 0x%!x(MISSING), reason: %!{(MISSING)public}s"
+ "[%!(BADPREC)%!h(MISSING)hx] [Background] Skipping mailbox {%!(BADPREC)%!h(MISSING)x} '%!{(MISSING)sensitive,mask.mailbox}s' until next sync."
+ "[%!(BADPREC)%!h(MISSING)hx] Tearing down."
+ "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Completed command for boundary IDs, but didn’t get any result from the server."
+ "[%!(BADPREC)%!h(MISSING)hx] Timer fired: checking for idle connections to cancel."
+ "[%!(BADPREC)%!h(MISSING)hx] Deinit."
- "[[%!(BADPREC)%!h(MISSING)hx]] Deinit."
- "[%!(BADPREC)%!h(MISSING)hx] [1st connection] Running sync requests %!l(MISSING)d: {%!{(MISSING)public}s}, kinds: %!s(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] %!{(MISSING)public}s IDLE is %!l(MISSING)d seconds old (< %!l(MISSING)d). Not refreshing."
- "[%!(BADPREC)%!h(MISSING)hx-%!{(MISSING)public}s] [{%!(BADPREC)%!h(MISSING)x}-%!{(MISSING)sensitive,mask.mailbox}s] Created task. Local UID validity: 0x%!x(MISSING)"
- "[%!(BADPREC)%!h(MISSING)hx] {%!l(MISSING)d} [1st connection] Mailbox: '%!{(MISSING)sensitive,mask.mailbox}s' %!{(MISSING)public}s {%!{(MISSING)public}s} last sync:  {local: %!{(MISSING)public}s, remote: %!{(MISSING)public}s}"
- "[[%!(BADPREC)%!h(MISSING)hx]] Tearing down."
- "[%!(BADPREC)%!h(MISSING)hx] Cancelling connection %!{(MISSING)public}s."
- "[%!(BADPREC)%!h(MISSING)hx] Timer fired: checking for cancelled connections."

```
