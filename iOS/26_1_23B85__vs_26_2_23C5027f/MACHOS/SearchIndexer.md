## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3864.200.81.2.5
-  __TEXT.__text: 0x4a228c
+3864.300.11.2.1
+  __TEXT.__text: 0x4a3eac
   __TEXT.__auth_stubs: 0x4260
   __TEXT.__objc_methlist: 0x3a4
-  __TEXT.__cstring: 0x8b36
+  __TEXT.__cstring: 0x8b86
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__const: 0x5eb9c
-  __TEXT.__swift5_typeref: 0xbf26
-  __TEXT.__swift5_capture: 0x4100
-  __TEXT.__constg_swiftt: 0xb5e0
-  __TEXT.__swift5_reflstr: 0xd758
-  __TEXT.__swift5_fieldmd: 0x1220c
-  __TEXT.__swift5_proto: 0x23ec
+  __TEXT.__const: 0x5ebfc
+  __TEXT.__swift5_typeref: 0xbf16
+  __TEXT.__swift5_capture: 0x41f8
+  __TEXT.__constg_swiftt: 0xb5f8
+  __TEXT.__swift5_reflstr: 0xd7a8
+  __TEXT.__swift5_fieldmd: 0x12248
+  __TEXT.__swift5_proto: 0x23f0
   __TEXT.__swift5_types: 0x13fc
   __TEXT.__swift5_builtin: 0xa28
-  __TEXT.__swift5_mpenum: 0x778
+  __TEXT.__swift5_mpenum: 0x788
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__oslogstring: 0xf710
+  __TEXT.__oslogstring: 0xf810
   __TEXT.__swift5_assocty: 0x16a8
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x17e4
   __TEXT.__objc_methtype: 0x44d
-  __TEXT.__unwind_info: 0xd4d8
-  __TEXT.__eh_frame: 0x13074
+  __TEXT.__unwind_info: 0xd4e8
+  __TEXT.__eh_frame: 0x1304c
   __DATA_CONST.__auth_got: 0x2138
-  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__got: 0xc10
   __DATA_CONST.__auth_ptr: 0x2858
-  __DATA_CONST.__const: 0x3c558
+  __DATA_CONST.__const: 0x3c7b0
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x3bf8
+  __DATA.__objc_const: 0x3c38
   __DATA.__objc_selrefs: 0x8a0
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0x11090
-  __DATA.__common: 0xc49
-  __DATA.__bss: 0x46a60
+  __DATA.__data: 0x110b0
+  __DATA.__common: 0xc59
+  __DATA.__bss: 0x46ae0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D7BED1C-3117-309B-891A-0C14C4991281
-  Functions: 19656
+  UUID: 3D70EB53-1580-3E72-BE09-40B017DCB134
+  Functions: 19688
   Symbols:   446
-  CStrings:  2991
+  CStrings:  2997
 
CStrings:
+ "Current ID {%ld} equal or higher than new {%ld}: Ignoring request to start indexing. Requesting deferral."
+ "No messages to redonate, skipping redonation sync"
+ "Starting new download for %s with sync #%u for %ld account(s): %{public}s"
+ "[%llu] {%ld} Download & index wasn't able to connect to some accounts."
+ "backfillPurpose"
+ "lastIndexID"
+ "mailbox == %@ && (indexGeneration != %@ || indexGeneration == NULL)"
+ "mailbox == %@ && needToRedonate == true"
- "Starting new download with sync #%u for %ld account(s): %{public}s"
- "mailbox == %@ && (indexGeneration != %@ || indexGeneration == NULL || needToRedonate == true)"

```
