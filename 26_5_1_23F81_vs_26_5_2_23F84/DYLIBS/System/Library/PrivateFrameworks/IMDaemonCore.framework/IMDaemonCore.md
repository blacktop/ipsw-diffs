## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-  __TEXT.__text: 0x36c3a0
+  __TEXT.__text: 0x36cbdc
   __TEXT.__auth_stubs: 0x55a0
-  __TEXT.__objc_methlist: 0x19c7c
+  __TEXT.__objc_methlist: 0x19cdc
   __TEXT.__const: 0x6e98
   __TEXT.__cstring: 0x12dcc
-  __TEXT.__gcc_except_tab: 0x22298
-  __TEXT.__oslogstring: 0x4f447
+  __TEXT.__gcc_except_tab: 0x22324
+  __TEXT.__oslogstring: 0x4f687
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
   __TEXT.__swift5_typeref: 0x3090

   __TEXT.__swift_as_ret: 0x40c
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd8c8
+  __TEXT.__unwind_info: 0xd8d0
   __TEXT.__eh_frame: 0x781c
   __TEXT.__objc_classname: 0x44f1
-  __TEXT.__objc_methname: 0x51657
+  __TEXT.__objc_methname: 0x516a7
   __TEXT.__objc_methtype: 0xb33f
   __TEXT.__objc_stubs: 0x32b80
   __DATA_CONST.__got: 0x3340
-  __DATA_CONST.__const: 0x6680
+  __DATA_CONST.__const: 0x66d0
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x778

   __AUTH_CONST.__auth_got: 0x2ae0
   __AUTH_CONST.__const: 0x8430
   __AUTH_CONST.__cfstring: 0xe7e0
-  __AUTH_CONST.__objc_const: 0x21208
+  __AUTH_CONST.__objc_const: 0x212c8
   __AUTH_CONST.__objc_intobj: 0xac8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3428
   __AUTH.__data: 0x5e0
-  __DATA.__objc_ivar: 0x123c
+  __DATA.__objc_ivar: 0x124c
   __DATA.__data: 0x5860
   __DATA.__bss: 0x5200
   __DATA.__common: 0x178

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13155
+  Functions: 13163
   Symbols:   3028
-  CStrings:  21679
+  CStrings:  21684
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
CStrings:
+ "Adding message GUID to readReceiptsForMissingMessage cache: %@ sender: %@ (size: %lu)"
+ "Dropping cached read receipt for missing message %@: receipt not from me for a message not from me"
+ "Dropping cached read receipt for missing message %@: receipt sender %@ is not the recipient %@"
+ "Refusing to release pending replicated message %@ because the releasing message's sender does not match the cached message's sender (cached set: %{BOOL}d, releasing set: %{BOOL}d)"
+ "Rejecting c=112 (delivered-quietly) for GUID=%@ (msg.isFromMe=%{BOOL}d, sender=%{private}@, handle=%{private}@)"
+ "Rejecting c=113 (notify-recipient) for GUID=%@ (sender=%{private}@, handle=%{private}@)"
+ "addMissingMessageReadReceipt:sender:"
+ "addPendingMessageWithGUID:replicatedFallbackGUIDs:fromIdentifier:isFromMe:releaseBlock:"
+ "initWithServiceName:fallbackGUIDs:encrypted:fromIdentifier:"
+ "popReadReceiptForMissingGUID:messageIsFromMe:account:recipient:"
- "Adding message GUID to readReceiptsForMissingMessage cache: %@ (size: %lu)"
- "addMissingMessageReadReceipt:"
- "addPendingMessageWithGUID:replicatedFallbackGUIDs:releaseBlock:"
- "initWithServiceName:fallbackGUIDs:encrypted:"
- "popReadReceiptForMissingGUID:"

```
