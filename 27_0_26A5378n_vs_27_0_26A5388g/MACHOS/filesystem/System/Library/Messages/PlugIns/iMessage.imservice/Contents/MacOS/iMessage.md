## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1485.100.12.1.1
-  __TEXT.__text: 0x118220
+1487.100.6.1.2
+  __TEXT.__text: 0x119208
   __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0xe720
-  __TEXT.__objc_methlist: 0x303c
+  __TEXT.__objc_stubs: 0xe760
+  __TEXT.__objc_methlist: 0x304c
   __TEXT.__const: 0x1588
-  __TEXT.__gcc_except_tab: 0x9894
-  __TEXT.__cstring: 0x3d7d
-  __TEXT.__oslogstring: 0x1bc5b
+  __TEXT.__gcc_except_tab: 0x98d8
+  __TEXT.__cstring: 0x3d9d
+  __TEXT.__oslogstring: 0x1bd5b
   __TEXT.__objc_classname: 0x72f
-  __TEXT.__objc_methname: 0x14a6e
+  __TEXT.__objc_methname: 0x14b0a
   __TEXT.__objc_methtype: 0x32a9
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xe26

   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift_as_cont: 0x13c
-  __TEXT.__swift5_capture: 0x9b8
+  __TEXT.__swift5_capture: 0x9bc
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2c80
+  __TEXT.__unwind_info: 0x2ca8
   __TEXT.__eh_frame: 0x1a80
-  __DATA_CONST.__const: 0x5860
+  __DATA_CONST.__const: 0x5950
   __DATA_CONST.__cfstring: 0x3d00
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__auth_got: 0x10c8
-  __DATA_CONST.__got: 0x12f0
+  __DATA_CONST.__got: 0x12f8
   __DATA_CONST.__auth_ptr: 0x330
   __DATA.__objc_const: 0x3878
-  __DATA.__objc_selrefs: 0x40a8
+  __DATA.__objc_selrefs: 0x40b8
   __DATA.__objc_ivar: 0x248
   __DATA.__objc_data: 0xc88
   __DATA.__data: 0xdd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2588
+  Functions: 2607
   Symbols:   920
-  CStrings:  5223
+  CStrings:  5228
 
CStrings:
+ "Comm-safety analysis returned no result for transfer %@, proceeding with send. error: %@. %@"
+ "Not sending gradient for message %@, comm-safety blocked the send. %@"
+ "Send failure for collaboration message guid %@ to %@ after already completing the send (reason: %u)."
+ "_analyzeAcquiredAttachmentsForSensitiveContentForMessage:chatIdentifier:completion:"
+ "analyzeContent:ofType:isFromMe:completionHandler:"
+ "analyzeContent:withIdentifier:chatID:isFromMe:completionHandler:"
+ "checkExistingAttachmentSensitivityIfNeededFor:attachmentURL:isFromMe:completion:"
+ "decisioningMetadata"
+ "updateSpamModelMetadataWith:wasJunk:isJunk:"
- "analyzeContent:ofType:completionHandler:"
- "analyzeContent:withIdentifier:chatID:completionHandler:"
- "checkExistingAttachmentSensitivityIfNeededFor:attachmentURL:isFromMe:"
- "setSpamModelMetadata:"
```
