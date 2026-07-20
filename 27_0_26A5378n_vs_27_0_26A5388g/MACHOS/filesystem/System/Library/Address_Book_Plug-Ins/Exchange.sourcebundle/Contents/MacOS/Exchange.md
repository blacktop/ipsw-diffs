## Exchange

> `/System/Library/Address Book Plug-Ins/Exchange.sourcebundle/Contents/MacOS/Exchange`

### Sections with Same Size but Changed Content

- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`

```diff

-2759.100.1.0.0
-  __TEXT.__text: 0x5eab4
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_stubs: 0x6a60
-  __TEXT.__objc_methlist: 0x1a44
-  __TEXT.__cstring: 0x1c45
+2761.100.1.0.0
+  __TEXT.__text: 0x6f61c
+  __TEXT.__auth_stubs: 0x18a0
+  __TEXT.__objc_stubs: 0x6b20
+  __TEXT.__objc_methlist: 0x1a6c
+  __TEXT.__cstring: 0x1c85
   __TEXT.__objc_classname: 0x5a7
-  __TEXT.__const: 0xb50
-  __TEXT.__oslogstring: 0x423e
-  __TEXT.__objc_methtype: 0x7ac
-  __TEXT.__gcc_except_tab: 0xb7c
-  __TEXT.__objc_methname: 0x5e71
-  __TEXT.__constg_swiftt: 0x708
-  __TEXT.__swift5_typeref: 0x6b4
-  __TEXT.__swift5_reflstr: 0x384
-  __TEXT.__swift5_fieldmd: 0x558
-  __TEXT.__swift5_capture: 0x158
-  __TEXT.__swift5_types: 0x60
+  __TEXT.__const: 0xcf8
+  __TEXT.__oslogstring: 0x497e
+  __TEXT.__objc_methtype: 0x79c
+  __TEXT.__gcc_except_tab: 0xb6c
+  __TEXT.__objc_methname: 0x5ef1
+  __TEXT.__constg_swiftt: 0x760
+  __TEXT.__swift5_typeref: 0x826
+  __TEXT.__swift5_reflstr: 0x3f4
+  __TEXT.__swift5_fieldmd: 0x5dc
+  __TEXT.__swift5_capture: 0x1b4
+  __TEXT.__swift5_types: 0x68
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xb58
-  __TEXT.__eh_frame: 0x330
-  __DATA_CONST.__const: 0x1610
+  __TEXT.__unwind_info: 0xc68
+  __TEXT.__eh_frame: 0x430
+  __DATA_CONST.__const: 0x17f8
   __DATA_CONST.__cfstring: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0xf98
-  __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA.__objc_const: 0x2450
-  __DATA.__objc_selrefs: 0x1eb8
+  __DATA_CONST.__auth_got: 0xc60
+  __DATA_CONST.__got: 0xff0
+  __DATA_CONST.__auth_ptr: 0x238
+  __DATA.__objc_const: 0x2490
+  __DATA.__objc_selrefs: 0x1ee8
   __DATA.__objc_ivar: 0xf8
-  __DATA.__objc_data: 0xd90
-  __DATA.__data: 0xba0
+  __DATA.__objc_data: 0xd98
+  __DATA.__data: 0xd10
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x300
-  __DATA.__common: 0x70
+  __DATA.__bss: 0x400
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1037
-  Symbols:   706
-  CStrings:  1769
+  Functions: 1127
+  Symbols:   708
+  CStrings:  1800
 
Symbols:
+ _OBJC_CLASS_$_CNCDPersistentStoreCoordinator
+ _OBJC_CLASS_$_NSDateFormatter
CStrings:
+ "410 recovery: failed to persist cleared syncFolderItemsSyncState for %{public}s: %{public}s"
+ "410 — folder %{public}s token cleared; next cycle re-syncs it"
+ "Address book save failed: %{public}@ — not advancing tokens; next cycle re-pulls"
+ "Deleted %{public}ld contact(s) removed on the server"
+ "Did sync folder contents (Graph) (%{public}fs)"
+ "Error saving Exchange DB: %{public}@ — rolling back; tokens not advanced, next cycle re-pulls"
+ "Failed to parse birthday string: %{private}s"
+ "Failed to persist advanced delta tokens after AB save: %{public}@ — next cycle re-pulls (idempotent)"
+ "Fetching ContactFolder rows failed: %{public}s"
+ "Folder %{public}s: delete-mapping fetch failed — halting before advancing token"
+ "Folder %{public}s: existing-mapping fetch failed — halting before applying this page"
+ "Folder %{public}s: response has neither a skip token nor a delta token — server bug; state unchanged"
+ "Folder %{public}s: skip token did not advance — halting to avoid an infinite pagination loop"
+ "Folder contents pull: %{public}ld folder(s)"
+ "No ACAccount for Graph folder contents pull — bailing this sync cycle"
+ "Skipping contact resource with nil/empty id"
+ "Sweep: %{public}ld unconfirmed contact create(s) not echoed by server — cleaning up"
+ "Unable to fetch or create an ABPerson for itemId=%{public}s"
+ "Vacuum: failed to enumerate contacts of folder: %{public}s — will retry next cycle"
+ "Vacuum: failed to remove ABPerson for contact itemId=%{public}s — folder stays flagged; will retry next cycle"
+ "Vacuum: removed %{public}ld contact(s) in a deleted folder"
+ "Will sync folder contents (Graph)"
+ "dateFromString:"
+ "fetchContactMappings(byItemIds:) failed: %{public}s"
+ "folder contents fetch failed: %{public}s underlying=%{public}s"
+ "graph-sync-folder-contents"
+ "initWithUnsignedInteger:"
+ "setDateFormat:"
+ "setLocale:"
+ "unsignedIntegerValue"
+ "withCoordinator:performBlockAndWait:"
```
