## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.400.113.0.0
-  __TEXT.__text: 0x5da0d4
+3826.400.121.2.2
+  __TEXT.__text: 0x5dc150
   __TEXT.__auth_stubs: 0x4390
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
   __TEXT.__cstring: 0x8e89
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x42e90
-  __TEXT.__swift5_typeref: 0xe1c3
+  __TEXT.__const: 0x42ec0
+  __TEXT.__swift5_typeref: 0xe1d9
   __TEXT.__swift5_capture: 0x7ecc
-  __TEXT.__constg_swiftt: 0xb8b4
-  __TEXT.__swift5_reflstr: 0xd439
-  __TEXT.__swift5_fieldmd: 0x1203c
-  __TEXT.__swift5_proto: 0x2388
-  __TEXT.__swift5_types: 0x1424
+  __TEXT.__constg_swiftt: 0xb8d0
+  __TEXT.__swift5_reflstr: 0xd459
+  __TEXT.__swift5_fieldmd: 0x12070
+  __TEXT.__swift5_proto: 0x238c
+  __TEXT.__swift5_types: 0x1428
   __TEXT.__swift5_assocty: 0x1620
-  __TEXT.__oslogstring: 0xe8d0
+  __TEXT.__oslogstring: 0xea30
   __TEXT.__swift5_builtin: 0xb04
   __TEXT.__swift5_mpenum: 0x7f0
   __TEXT.__swift5_protos: 0x74

   __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x13020
-  __TEXT.__eh_frame: 0x19398
+  __TEXT.__unwind_info: 0x13070
+  __TEXT.__eh_frame: 0x193a0
   __DATA_CONST.__auth_got: 0x21d8
   __DATA_CONST.__got: 0xb40
   __DATA_CONST.__auth_ptr: 0x3058
-  __DATA_CONST.__const: 0x48558
+  __DATA_CONST.__const: 0x485d8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_const: 0x4c20
   __DATA.__objc_selrefs: 0x798
   __DATA.__objc_data: 0x980
-  __DATA.__data: 0x11de8
-  __DATA.__bss: 0x45bc0
-  __DATA.__common: 0xcf0
+  __DATA.__data: 0x11dd8
+  __DATA.__bss: 0x45c40
+  __DATA.__common: 0xcf8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 29321
+  Functions: 29335
   Symbols:   446
-  CStrings:  2980
+  CStrings:  2984
 
CStrings:
+ "[%.*hhx-%{public}s] Got post-auth capabilities: %{public}s."
+ "[%.*hhx-%{public}s] Got pre-auth capabilities: %{public}s."
+ "[%.*hhx-%{public}s] XOAUTH2 error: status '%{public}s',  schemes '%{public}s',  scope '%{public}s'"
+ "[%.*hhx] Credentials state -> %{public}s"
+ "[%.*hhx] Not resetting backoff timer."
+ "[%.*hhx] [%{sensitive,mask.mailbox}s] Did mark should temporarily grow window of interest. Fetching missing messages, first."
+ "[%.*hhx] [%{sensitive,mask.mailbox}s] Did mark should temporarily grow window of interest. Waiting for FindMissingMessages."
- "[%.*hhx-%{public}s] Got post-auth capabilities: %s."
- "[%.*hhx-%{public}s] Got pre-auth capabilities: %s."
- "[%.*hhx-%{public}s] XOAUTH2 error: status '%{public}s',  schemes '%{public}s',  scope '%{private}s'"

```
