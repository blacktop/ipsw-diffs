## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3853.100.6.2.6
-  __TEXT.__text: 0x4be354
+3856.100.4.0.0
+  __TEXT.__text: 0x4d3174
   __TEXT.__auth_stubs: 0x4580
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__cstring: 0x9019
+  __TEXT.__cstring: 0x9089
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5b7a0
-  __TEXT.__swift5_typeref: 0xe5ad
-  __TEXT.__swift5_capture: 0x4824
-  __TEXT.__constg_swiftt: 0xbac8
-  __TEXT.__swift5_reflstr: 0xd8b9
-  __TEXT.__swift5_fieldmd: 0x124a4
-  __TEXT.__swift5_proto: 0x23f0
-  __TEXT.__swift5_types: 0x1460
-  __TEXT.__swift5_assocty: 0x1638
-  __TEXT.__oslogstring: 0xf7e0
-  __TEXT.__swift5_builtin: 0xadc
-  __TEXT.__swift5_mpenum: 0x7f0
+  __TEXT.__const: 0x5c860
+  __TEXT.__swift5_typeref: 0xe7d1
+  __TEXT.__swift5_capture: 0x49b4
+  __TEXT.__constg_swiftt: 0xbc94
+  __TEXT.__swift5_reflstr: 0xdbd9
+  __TEXT.__swift5_fieldmd: 0x127ec
+  __TEXT.__swift5_proto: 0x2488
+  __TEXT.__swift5_types: 0x149c
+  __TEXT.__swift5_assocty: 0x1710
+  __TEXT.__oslogstring: 0xfc40
+  __TEXT.__swift5_builtin: 0xaf0
+  __TEXT.__swift5_mpenum: 0x7f4
   __TEXT.__swift5_protos: 0x74
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methname: 0x17c9
   __TEXT.__objc_methtype: 0x420
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0xfe10
-  __TEXT.__eh_frame: 0x198c0
+  __TEXT.__unwind_info: 0x10040
+  __TEXT.__eh_frame: 0x19c00
   __DATA_CONST.__auth_got: 0x22d0
   __DATA_CONST.__got: 0xc30
-  __DATA_CONST.__auth_ptr: 0x3160
-  __DATA_CONST.__const: 0x3fb70
+  __DATA_CONST.__auth_ptr: 0x31a0
+  __DATA_CONST.__const: 0x406c8
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
-  __DATA.__data: 0x125e8
-  __DATA.__bss: 0x468e0
-  __DATA.__common: 0xc90
+  __DATA.__data: 0x126e8
+  __DATA.__bss: 0x47bf0
+  __DATA.__common: 0xcd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF0CA162-A0C8-3B89-AA57-1BFBBB02183E
-  Functions: 24457
-  Symbols:   465
-  CStrings:  3055
+  UUID: 46CFC542-86D8-3CF0-9EFD-91AF055CED17
+  Functions: 24682
+  Symbols:   461
+  CStrings:  3069
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "Index request. Expects reply: %{BOOL}d"
+ "Invalid object ID."
+ "Invalid response for start index request."
+ "MAILBOXID"
+ "Received response for start index request."
+ "Sending index task reply."
+ "Start index request failed: %@"
+ "Unexpected error %@ while sending a start index request."
+ "Unexpected error %@ while sending a stop index request."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Batch #%ld got response %{public}s and %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Batch #%ld got response %{public}s and %{public}s: Should overlap, but they do not."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Batch #%ld got response NIL and %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Batch #%ld is %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Batch #%ld is empty"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed SEARCH for boundary IDs, but didn’t get any result from the server."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed UIDBATCHES. %ld message batch(es): %{public}s"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed UIDBATCHES. %ld message batch(es): %{public}s (window of interest: %{public}s)"
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed UIDBATCHES. No message batches."
+ "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Duplicate response for batch #%ld is identical."
+ "[%.*hhx] Task %{public}s has been running for %ld s. Still running %ld: %{public}s"
+ "batchSize batchRange "
+ "com.apple.email.SearchIndexer.Indexer."
+ "lastLogAllConnectionStates"
- "Download request. Expects reply: %{BOOL}d"
- "Invalid response for start download request."
- "Received response for start download request."
- "Sending download task reply."
- "Start download request failed: %@"
- "Unexpected error %@ while sending a start download request."
- "Unexpected error %@ while sending a stop download request."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Completed command for boundary IDs, but didn’t get any result from the server."
- "com.apple.email.Downloader."

```
