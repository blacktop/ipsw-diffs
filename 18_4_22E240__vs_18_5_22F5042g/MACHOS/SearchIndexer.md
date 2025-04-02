## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.500.181.2.5
-  __TEXT.__text: 0x4dfe5c
-  __TEXT.__auth_stubs: 0x4430
+3826.600.15.2.1
+  __TEXT.__text: 0x4e147c
+  __TEXT.__auth_stubs: 0x4440
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__cstring: 0x8d39
+  __TEXT.__cstring: 0x8d99
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x59d98
-  __TEXT.__swift5_typeref: 0xe031
+  __TEXT.__const: 0x59e10
+  __TEXT.__swift5_typeref: 0xe055
   __TEXT.__swift5_capture: 0x8164
-  __TEXT.__constg_swiftt: 0xb7b8
-  __TEXT.__swift5_reflstr: 0xd479
-  __TEXT.__swift5_fieldmd: 0x11f1c
-  __TEXT.__swift5_proto: 0x2384
-  __TEXT.__swift5_types: 0x13f8
+  __TEXT.__constg_swiftt: 0xb7e0
+  __TEXT.__swift5_reflstr: 0xd4b9
+  __TEXT.__swift5_fieldmd: 0x11f50
+  __TEXT.__swift5_proto: 0x2388
+  __TEXT.__swift5_types: 0x13fc
   __TEXT.__swift5_assocty: 0x1620
   __TEXT.__oslogstring: 0xef00
   __TEXT.__swift5_builtin: 0xaa0
   __TEXT.__swift5_mpenum: 0x7a0
   __TEXT.__swift5_protos: 0x74
   __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0x179f
+  __TEXT.__objc_methname: 0x17c9
   __TEXT.__objc_methtype: 0x420
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x10078
-  __TEXT.__eh_frame: 0x195b0
-  __DATA_CONST.__auth_got: 0x2228
+  __TEXT.__unwind_info: 0x100b0
+  __TEXT.__eh_frame: 0x195b8
+  __DATA_CONST.__auth_got: 0x2230
   __DATA_CONST.__got: 0xc40
   __DATA_CONST.__auth_ptr: 0x2ff8
-  __DATA_CONST.__const: 0x48678
+  __DATA_CONST.__const: 0x486a0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x42b0
-  __DATA.__objc_selrefs: 0x888
+  __DATA.__objc_const: 0x42c0
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0x12150
-  __DATA.__bss: 0x45b30
+  __DATA.__data: 0x12158
+  __DATA.__bss: 0x45bb0
   __DATA.__common: 0xc70
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 26097
+  Functions: 26118
   Symbols:   457
-  CStrings:  3003
+  CStrings:  3007
 
CStrings:
+ "%s: received %{iec-bytes}ld, sent %{iec-bytes}ld, messages indexed %ld, updated flags %ld, deleted messages %ld, complete re-index %ld, message re-donate requests %ld, over quota count %ld, was unavailable: %{BOOL}d"
+ "Done marking items for re-donation."
+ "Spotlight is requesting a re-donation of %ld items, but only %ld identifiers were valid."
+ "Spotlight is requesting a re-donation of %ld items."
+ "Spotlight is requesting a re-donation of %{public}s"
+ "mailbox == %@ && (indexGeneration != %@ || indexGeneration == NULL || needToRedonate == true)"
+ "messagesToRedonate"
+ "primitiveNeedToRedonate"
+ "setAscending:"
+ "setPrimitiveNeedToRedonate:"
- "%s: received %{iec-bytes}ld, sent %{iec-bytes}ld, messages indexed %ld, updated flags %ld, deleted messages %ld, complete re-index %ld, message re-index requests %ld, over quota count %ld, was unavailable: %{BOOL}d"
- "Done marking items for re-indexing."
- "Spotlight is requesting a re-index of %ld items, but only %ld identifiers were valid."
- "Spotlight is requesting a re-index of %ld items."
- "Spotlight is requesting a re-index of %{public}s"
- "mailbox == %@ && (indexGeneration != %@ || indexGeneration == NULL)"

```
