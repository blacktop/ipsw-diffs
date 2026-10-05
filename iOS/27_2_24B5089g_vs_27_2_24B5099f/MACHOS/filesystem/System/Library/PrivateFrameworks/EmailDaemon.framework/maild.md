## maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3901.200.41.0.0
-  __TEXT.__text: 0x14ceb4
+3901.200.66.2.1
+  __TEXT.__text: 0x14d568
   __TEXT.__auth_stubs: 0x2820
-  __TEXT.__objc_stubs: 0x164e0
-  __TEXT.__objc_methlist: 0xae24
+  __TEXT.__objc_stubs: 0x165a0
+  __TEXT.__objc_methlist: 0xae54
   __TEXT.__const: 0x15ec
-  __TEXT.__gcc_except_tab: 0x1962c
-  __TEXT.__cstring: 0x8df8
-  __TEXT.__objc_methname: 0x1cef5
-  __TEXT.__oslogstring: 0xaffe
+  __TEXT.__gcc_except_tab: 0x19718
+  __TEXT.__cstring: 0x8e08
+  __TEXT.__objc_methname: 0x1cfd5
+  __TEXT.__oslogstring: 0xb0ce
   __TEXT.__objc_classname: 0x1acf
   __TEXT.__objc_methtype: 0x4119
   __TEXT.__ustring: 0x72

   __TEXT.__swift_as_ret: 0x94
   __TEXT.__swift_as_cont: 0x118
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x89f0
+  __TEXT.__unwind_info: 0x8a30
   __TEXT.__eh_frame: 0xfd8
-  __DATA_CONST.__const: 0xe5f8
+  __DATA_CONST.__const: 0xe620
   __DATA_CONST.__cfstring: 0x65a0
   __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x70

   __DATA_CONST.__got: 0x1848
   __DATA_CONST.__auth_ptr: 0x410
   __DATA.__objc_const: 0x12e18
-  __DATA.__objc_selrefs: 0x7008
+  __DATA.__objc_selrefs: 0x7038
   __DATA.__objc_ivar: 0xb94
   __DATA.__objc_data: 0x36c8
   __DATA.__data: 0x2d40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5874
+  Functions: 5880
   Symbols:   1549
-  CStrings:  7516
+  CStrings:  7526
 
CStrings:
+ "Delivery did not commit (status %ld), keeping source draft"
+ "Message %@ permanently failed delivery, but no Drafts mailbox is available to move it to"
+ "Message %@ permanently failed delivery, moving to Drafts"
+ "_moveToDraftsAfterPermanentlyFailedDelivery:inOutbox:forAccount:"
+ "_removeSourceDraftForOutgoingMessage:"
+ "_removeSourceDraftForOutgoingMessage:deliveryStatus:"
+ "deleteDraftsInMailboxID:documentID:previousDraftObjectID:"
+ "sourceAutosaveID"
+ "sourceDraftObjectID"
+ "v16@?0@\"EMMessage\"8"
```
