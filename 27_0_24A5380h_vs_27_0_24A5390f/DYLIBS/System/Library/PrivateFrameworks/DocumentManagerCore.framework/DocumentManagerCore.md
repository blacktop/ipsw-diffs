## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-394.0.0.0.0
-  __TEXT.__text: 0x6f144
-  __TEXT.__objc_methlist: 0x4428
-  __TEXT.__const: 0x17a0
+396.0.0.0.0
+  __TEXT.__text: 0x7153c
+  __TEXT.__objc_methlist: 0x4478
+  __TEXT.__const: 0x17f0
   __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__cstring: 0x4f7a
-  __TEXT.__oslogstring: 0x47e2
+  __TEXT.__cstring: 0x4fda
+  __TEXT.__oslogstring: 0x4872
   __TEXT.__ustring: 0x98
-  __TEXT.__swift5_typeref: 0xbc2
+  __TEXT.__swift5_typeref: 0xbd6
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x264

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0xc8
   __TEXT.__swift5_capture: 0x2c4
-  __TEXT.__unwind_info: 0x1df0
-  __TEXT.__eh_frame: 0xf68
+  __TEXT.__unwind_info: 0x1e38
+  __TEXT.__eh_frame: 0xf40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2968
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x740
-  __AUTH_CONST.__const: 0x1778
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0x6db0
+  __AUTH_CONST.__const: 0x1798
+  __AUTH_CONST.__cfstring: 0x30a0
+  __AUTH_CONST.__objc_const: 0x6dc8
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__auth_got: 0xde8
   __AUTH.__objc_data: 0x438
   __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0x10f0
-  __DATA.__bss: 0x17e0
+  __DATA.__data: 0x1118
+  __DATA.__bss: 0x17f0
   __DATA_DIRTY.__objc_data: 0x1130
-  __DATA_DIRTY.__data: 0x718
+  __DATA_DIRTY.__data: 0x728
   __DATA_DIRTY.__bss: 0xa20
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2904
-  Symbols:   4000
-  CStrings:  891
+  Functions: 2926
+  Symbols:   4018
+  CStrings:  897
 
Symbols:
+ -[FINode(DOCNode) actionsForPermissions:]
+ -[FINode(DOCNode) doc_eligibleActionsFor:]
+ -[FINode(DOCNode) permissionsForActions:]
+ -[FPItem(DOCNode) doc_eligibleActionsFor:]
+ -[FPItem(DOCNode) shouldUseDSEnumeration]
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table78
+ _FPActionPin
+ ___41-[FPItem(DOCNode) shouldUseDSEnumeration]_block_invoke
+ ___42-[FINode(DOCNode) doc_eligibleActionsFor:]_block_invoke
+ _getuid
+ _objc_msgSend$actionsForPermissions:
+ _objc_msgSend$doc_eligibleActionsFor:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$permissionsForActions:
+ _objc_msgSend$shouldUseDSEnumeration
+ _objc_msgSend$stringValue
+ _objc_msgSend$unionSet:
+ _objc_msgSend$unsignedIntValue
+ _shouldUseDSEnumeration.onceToken
+ _shouldUseDSEnumeration.sProviderIDToDSEnumerationState
+ _swift_dynamicCastObjCClassUnconditional
+ _symbolic _____ySiG s16PartialRangeFromV
+ _symbolic _____ySiG s16PartialRangeUpToV
- GCC_except_table193
- GCC_except_table198
- GCC_except_table77
- _FPActionDownloadNoContextMenu
- _FPActionDownloadRecursivelyNoContextMenu
- _FPActionFetchPublishingURL
- _FPActionIgnore
- _FPActionUnignore
- _FPActionUnpin
CStrings:
+ "%{public}s: failed to get FINode for item: %{public}@\n\t error: %{public}@"
+ "%{public}s: failed to get cached domain from item: %{public}@\n\t error: %{public}@"
+ "-[FPItem(DOCNode) doc_eligibleActionsFor:]"
+ "-[FPItem(DOCNode) shouldUseDSEnumeration]"
+ ".Trash"
+ ".Trashes"
+ "I"
+ "Received Permissions bits that were not requested.\n\t node: %{public}@\n\t Requested: %u\n\t Received: %u\n\t Not Requested: %u"
- "Unknown/Unexpected action: %{public}@. Falling back to FPItem: %{public}@"
- "Unsupported action: %{public}@. Falling back to FPItem: %{public}@"
```
