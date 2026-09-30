## Exchange

> `/System/Library/Address Book Plug-Ins/Exchange.sourcebundle/Contents/MacOS/Exchange`

```diff

-  __TEXT.__text: 0x596a0
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_stubs: 0x6a00
-  __TEXT.__objc_methlist: 0x1a14
-  __TEXT.__cstring: 0x1b85
+  __TEXT.__text: 0x5eab4
+  __TEXT.__auth_stubs: 0x1430
+  __TEXT.__objc_stubs: 0x6a60
+  __TEXT.__objc_methlist: 0x1a44
+  __TEXT.__cstring: 0x1c45
   __TEXT.__objc_classname: 0x5a7
-  __TEXT.__const: 0xab0
-  __TEXT.__oslogstring: 0x37ce
+  __TEXT.__const: 0xb50
+  __TEXT.__oslogstring: 0x423e
   __TEXT.__objc_methtype: 0x7ac
   __TEXT.__gcc_except_tab: 0xb7c
-  __TEXT.__objc_methname: 0x5de1
-  __TEXT.__constg_swiftt: 0x6b0
-  __TEXT.__swift5_typeref: 0x62a
-  __TEXT.__swift5_reflstr: 0x324
-  __TEXT.__swift5_fieldmd: 0x4c8
-  __TEXT.__swift5_capture: 0x1e4
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_protos: 0x10
+  __TEXT.__objc_methname: 0x5e71
+  __TEXT.__constg_swiftt: 0x708
+  __TEXT.__swift5_typeref: 0x6b4
+  __TEXT.__swift5_reflstr: 0x384
+  __TEXT.__swift5_fieldmd: 0x558
+  __TEXT.__swift5_capture: 0x158
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x20
-  __TEXT.__swift_as_cont: 0x54
-  __TEXT.__unwind_info: 0xb38
-  __TEXT.__eh_frame: 0x600
-  __DATA_CONST.__const: 0x15b8
+  __TEXT.__unwind_info: 0xb58
+  __TEXT.__eh_frame: 0x330
+  __DATA_CONST.__const: 0x1610
   __DATA_CONST.__cfstring: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__auth_got: 0x958
-  __DATA_CONST.__got: 0xf28
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA.__objc_const: 0x23f0
-  __DATA.__objc_selrefs: 0x1e90
+  __DATA_CONST.__auth_got: 0xa28
+  __DATA_CONST.__got: 0xf98
+  __DATA_CONST.__auth_ptr: 0x1e0
+  __DATA.__objc_const: 0x2450
+  __DATA.__objc_selrefs: 0x1eb8
   __DATA.__objc_ivar: 0xf8
-  __DATA.__objc_data: 0xd88
-  __DATA.__data: 0xad0
+  __DATA.__objc_data: 0xd90
+  __DATA.__data: 0xba0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x200
-  __DATA.__common: 0x40
+  __DATA.__bss: 0x300
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1002
-  Symbols:   704
-  CStrings:  1970
+  Functions: 1037
+  Symbols:   706
+  CStrings:  2015
 
Sections:
~ __TEXT.__objc_classname : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
Symbols:
+ _OBJC_CLASS_$_CNUnfairLock
+ _OBJC_CLASS_$_NSManagedObjectID
CStrings:
+ "410 recovery: failed to persist cleared syncFolderHierarchyState: %{public}s"
+ "410 — syncFolderHierarchyState cleared; next cycle will do full initial sync"
+ "ABGraphRequestRunner.run called from main thread — risk of deadlock"
+ "Applied %{public}ld folder resource(s)"
+ "Confirmed locally-created folder: itemId=%{public}s"
+ "Created ContactFolder mapping for itemId=%{public}s"
+ "Default name for a contact folder that has no display name"
+ "Delete: no mapping for itemId=%{public}s — already gone"
+ "Did finalize (Graph) (%{public}fs)"
+ "Did sync folder hierarchy (Graph) (%{public}fs)"
+ "Error saving Exchange DB: %{public}@ — rolling back; delta token not advanced, next cycle re-fetches"
+ "Error saving address book after Exchange: %{public}@ — token already committed; affected groups will re-heal on the next delta touch"
+ "Finalize: Exchange DB save failed after address book save: %{public}@ — mappings stay flagged; next cycle reconciles"
+ "Finalize: address book save failed: %{public}@ — keeping Exchange mappings; will retry next cycle"
+ "Folder hierarchy pull: %{public}s sync"
+ "Folder marked for deletion: itemId=%{public}s"
+ "GRAPH_UNTITLED_FOLDER_NAME"
+ "Intermediate save before unconfirmed-create sweep failed: %{public}s — skipping sweep this cycle"
+ "Lazy-created stub parent ContactFolder for parentId=%{public}s"
+ "No ACAccount for Graph folder hierarchy pull — bailing this sync cycle"
+ "Page complete — nextLink persisted; ABSS will continue next cycle"
+ "Response has neither nextLink nor deltaLink — server bug; state unchanged"
+ "Round complete — deltaLink persisted"
+ "Skipping folder resource with nil/empty id"
+ "Sweep: %{public}ld unconfirmed folder create(s) not echoed by server — cleaning up"
+ "T@,N,&,VfetcherOverride"
+ "Vacuum: %{public}ld folder(s) marked for deletion"
+ "Vacuum: cyclic parentFolder reference at itemId=%{public}s — stopping recursion"
+ "Vacuum: failed to enumerate subfolders of itemId=%{public}s: %{public}s — skipping this subtree, will retry next cycle"
+ "Vacuum: failed to remove ABGroup for itemId=%{public}s — leaving mapping so the stores stay consistent; will retry next cycle"
+ "Vacuum: removed folder mapping + group for itemId=%{public}s"
+ "Will finalize (Graph)"
+ "Will sync folder hierarchy (Graph)"
+ "_TtC8ExchangeP33_592349839099A5424888F8488AEAAE1010_ResultBox"
+ "fetchContactFolder(byItemId:) failed for %{public}s: %{public}s"
+ "fetcherOverride"
+ "folder hierarchy fetch failed: %{public}s underlying=%{public}s"
+ "graph-finalize-vacuum"
+ "graph-request-runner"
+ "graph-sync-folder-hierarchy"
+ "hasQueuedUpdateOperation fetch failed: %{public}s — assuming an update is queued"
+ "initWithUnsignedShort:"
+ "parentFolder == %@"
+ "rollback"
+ "saveAndReturnError:"
+ "setFetcherOverride:"
+ "sweepUnconfirmedCreates CreateOperation fetch failed: %{public}s"
+ "sweepUnconfirmedCreates fetch failed: %{public}s"
+ "targetMapping == %@"
+ "vacuum fetch failed: %{public}s"
- "GraphSyncContactFolderResource"
- "GraphSyncContactResource"
- "GraphSyncEmptyResponseResource"
- "_TtC8ExchangeP33_97857DDDA606E6C58AB95302710E11A010_ResultBox"
- "runSynchronously called from main thread — risk of deadlock"

```
