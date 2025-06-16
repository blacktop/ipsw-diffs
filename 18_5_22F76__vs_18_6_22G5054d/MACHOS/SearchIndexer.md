## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x4ec0d0
+3826.700.51.0.0
+  __TEXT.__text: 0x4fd970
   __TEXT.__auth_stubs: 0x44c0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__cstring: 0x9049
+  __TEXT.__cstring: 0x9069
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5a1b0
-  __TEXT.__swift5_typeref: 0xe1ff
-  __TEXT.__swift5_capture: 0x8100
-  __TEXT.__constg_swiftt: 0xb8ec
-  __TEXT.__swift5_reflstr: 0xd5c9
-  __TEXT.__swift5_fieldmd: 0x120a0
-  __TEXT.__swift5_proto: 0x23c0
-  __TEXT.__swift5_types: 0x1410
+  __TEXT.__const: 0x5a750
+  __TEXT.__swift5_typeref: 0xe321
+  __TEXT.__swift5_capture: 0x9830
+  __TEXT.__constg_swiftt: 0xb980
+  __TEXT.__swift5_reflstr: 0xd689
+  __TEXT.__swift5_fieldmd: 0x121a4
+  __TEXT.__swift5_proto: 0x23e4
+  __TEXT.__swift5_types: 0x1424
   __TEXT.__swift5_assocty: 0x1638
-  __TEXT.__oslogstring: 0xf250
+  __TEXT.__oslogstring: 0xf830
   __TEXT.__swift5_builtin: 0xaa0
-  __TEXT.__swift5_mpenum: 0x7a0
+  __TEXT.__swift5_mpenum: 0x7a8
   __TEXT.__swift5_protos: 0x74
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0x17c9
   __TEXT.__objc_methtype: 0x420
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x101c0
-  __TEXT.__eh_frame: 0x196c8
+  __TEXT.__unwind_info: 0x10300
+  __TEXT.__eh_frame: 0x19810
   __DATA_CONST.__auth_got: 0x2270
   __DATA_CONST.__got: 0xc38
-  __DATA_CONST.__auth_ptr: 0x3048
-  __DATA_CONST.__const: 0x48820
+  __DATA_CONST.__auth_ptr: 0x3058
+  __DATA_CONST.__const: 0x4c458
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4320
+  __DATA.__objc_const: 0x4340
   __DATA.__objc_selrefs: 0x898
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0x12290
-  __DATA.__bss: 0x462b0
+  __DATA.__data: 0x12310
+  __DATA.__bss: 0x46730
   __DATA.__common: 0xc88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 84DD17F6-1F40-3007-AC0F-80634F364C95
-  Functions: 26212
+  UUID: 60B2BCAA-E310-398D-837B-F98EB58A0718
+  Functions: 26688
   Symbols:   460
-  CStrings:  3044
+  CStrings:  3059
 
CStrings:
+ "[%.*hhx-%{public}s] Connection appears to have been stuck for %.*f s. Running commands: %{public}s."
+ "[%.*hhx-%{public}s] Connection appears to have been stuck for %.*f s. Running commands: %{public}s. Cancelling."
+ "[%.*hhx-%{public}s] Connection has %ld IDLE running."
+ "[%.*hhx-%{public}s] Connection has IDLE that has been running for %f s."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did complete fetching body structure for messages %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did complete fetching message size for messages %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did expunge deleted messages."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark source messages %{public}s as deleted."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did receive body structure for message %u."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did receive message size for message %u."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did receive message size for message %u. Missing body structure."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did receive message size for message %u. Using cached body structure."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did successfully upload %ld message(s)."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Received %ld message(s)."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Requesting sections to download for message %u (with body structure)."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Skipping %ld message(s)."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Using cached body structure for message(s) %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] [%{sensitive,mask.mailbox}s] Did copy messages %{public}s."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] [%{sensitive,mask.mailbox}s] Did move messages %{public}s."
+ "[%.*hhx] Resetting mailboxes-need-to-be-updated."
+ "[%.*hhx] Skipping update of mailbox list for sync."
+ "[%.*hhx] Task %{public}s has been running for %ld s. Still running %ld: %{public}s"
+ "lastLogAllConnectionStates"
- "[%.*hhx-%{public}s] Connection appears to have been stuck for %.*f s"
- "[%.*hhx-%{public}s] Connection appears to have been stuck for %.*f s. Cancelling."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed fetching Body Structure for messages %{public}s"
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Expunging deleted messages."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Marking source messages %{public}s as deleted."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Received body structure for message %u."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] [%{sensitive,mask.mailbox}s] Copying messages %{public}s."
- "[%.*hhx] Skipping update of mailbox list for sync ."

```
