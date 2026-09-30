## Network

> `/System/Library/Frameworks/Network.framework/Network`

```diff

-4277.102.4.0.0
-  __TEXT.__text: 0xcbfd34
+4277.120.35.0.0
+  __TEXT.__text: 0xcc73b8
   __TEXT.__auth_stubs: 0x65b0
   __TEXT.__delay_stubs: 0x3c8
   __TEXT.__delay_helper: 0xc58
   __TEXT.__init_offsets: 0x5c0
   __TEXT.__objc_methlist: 0x82ac
   __TEXT.__const: 0xd3288
-  __TEXT.__cstring: 0x5f71e
+  __TEXT.__cstring: 0x5f8d7
   __TEXT.__swift5_typeref: 0x44ae
-  __TEXT.__swift5_capture: 0x1ec0
+  __TEXT.__swift5_capture: 0x1ee0
   __TEXT.__swift5_reflstr: 0x2818
   __TEXT.__swift5_assocty: 0xa00
   __TEXT.__constg_swiftt: 0x48a4

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift_as_entry: 0x124
   __TEXT.__swift_as_ret: 0xe8
-  __TEXT.__oslogstring: 0x123621
-  __TEXT.__gcc_except_tab: 0x8e664
-  __TEXT.__unwind_info: 0x18220
+  __TEXT.__oslogstring: 0x1232a0
+  __TEXT.__gcc_except_tab: 0x8e6f8
+  __TEXT.__unwind_info: 0x18488
   __TEXT.__eh_frame: 0x66dc
   __TEXT.__objc_classname: 0x225d
-  __TEXT.__objc_methname: 0x14766
+  __TEXT.__objc_methname: 0x14774
   __TEXT.__objc_methtype: 0x8fd9
   __TEXT.__objc_stubs: 0xa020
   __DATA_CONST.__got: 0xf48
-  __DATA_CONST.__const: 0x13040
+  __DATA_CONST.__const: 0x13090
   __DATA_CONST.__objc_classlist: 0x9a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x4d8

   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x6f0
   __AUTH_CONST.__auth_got: 0x33a0
-  __AUTH_CONST.__auth_ptr: 0x1348
-  __AUTH_CONST.__const: 0xda78
+  __AUTH_CONST.__auth_ptr: 0x1298
+  __AUTH_CONST.__const: 0xdb10
   __AUTH_CONST.__cfstring: 0x8340
-  __AUTH_CONST.__objc_const: 0x26a48
+  __AUTH_CONST.__objc_const: 0x26aa8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x38e0
   __AUTH.__data: 0x5158
-  __DATA.__objc_ivar: 0x26a8
+  __DATA.__objc_ivar: 0x26b4
   __DATA.__data: 0x6fd8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x14099

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21256
-  Symbols:   15725
-  CStrings:  33344
+  Functions: 21283
+  Symbols:   15745
+  CStrings:  33346
 
Symbols:
+ _nw_http2_get_send_truncated_data_frames
+ _nw_http2_set_send_truncated_data_frames
+ _nw_oblivious_http_metadata_set_receive_aead_key_and_nonce
+ _nw_protocol_metadata_is_oblivious_http
CStrings:
+ "%{public}s %{public}s%s<i%u:s%d> truncated data frame length: %u"
+ "%{public}s %{public}s%s<i%u> Already have metadata metadata for datagram capsule type %llu"
+ "%{public}s %{public}s%sReceive AEAD nonce and key are not ready yet for context %llu, cannot decrypt chunk of length %llu"
+ "%{public}s %{public}s%sReceived updated keys for receive-only context"
+ "%{public}s called with null nw_protocol_metadata_is_oblivious_http(metadata)"
+ "%{public}s called with null nw_protocol_metadata_is_oblivious_http(metadata), backtrace limit exceeded"
+ "%{public}s called with null nw_protocol_metadata_is_oblivious_http(metadata), dumping backtrace:%{public}s"
+ "%{public}s called with null nw_protocol_metadata_is_oblivious_http(metadata), no backtrace"
+ "%{public}s called with null ohttp_context_handle"
+ "%{public}s called with null ohttp_context_handle, backtrace limit exceeded"
+ "%{public}s called with null ohttp_context_handle, dumping backtrace:%{public}s"
+ "%{public}s called with null ohttp_context_handle, no backtrace"
+ "%{public}s created end frame %p with parent %p"
+ "%{public}s releasing frame %p parent frame %p"
+ "%{public}s split frame (%u bytes) into start child %p (%u bytes) and end child %p (%u bytes)"
+ "4277.120.35"
+ "_hasCompleted"
+ "ios_s"
+ "metadata->ref_count"
+ "nw_http2_get_send_truncated_data_frames"
+ "nw_http2_set_send_truncated_data_frames"
+ "nw_oblivious_http_access_context_handle"
+ "nw_oblivious_http_clear_context_handle"
+ "nw_oblivious_http_create_metadata_for_context"
+ "nw_oblivious_http_metadata_set_receive_aead_key_and_nonce"
+ "nw_oblivious_http_metadata_set_receive_aead_key_and_nonce_block_invoke"
+ "nw_protocol_metadata_is_oblivious_http"
+ "parent_metadata->ref_count"
+ "v24@?0^v8^v16"
- "%{public}s called with null parent_frame"
- "%{public}s called with null parent_frame, backtrace limit exceeded"
- "%{public}s called with null parent_frame, dumping backtrace:%{public}s"
- "%{public}s called with null parent_frame, no backtrace"
- "%{public}s continuing to parent frame %p because both children have been finalized"
- "%{public}s finalizing top of tree frame %p, finalizing parent immediately (%p)"
- "%{public}s frame %p processed in loop, stopping"
- "%{public}s inserted top of tree split frame %p with parent %p"
- "%{public}s parent frame is not waiting for our end child finalizer"
- "%{public}s parent frame is not waiting for our end child finalizer, backtrace limit exceeded"
- "%{public}s parent frame is not waiting for our end child finalizer, dumping backtrace:%{public}s"
- "%{public}s parent frame is not waiting for our end child finalizer, no backtrace"
- "%{public}s parent frame is not waiting for our start child finalizer"
- "%{public}s parent frame is not waiting for our start child finalizer, backtrace limit exceeded"
- "%{public}s parent frame is not waiting for our start child finalizer, dumping backtrace:%{public}s"
- "%{public}s parent frame is not waiting for our start child finalizer, no backtrace"
- "%{public}s processing finalize for frame %p with parent_frame %p"
- "%{public}s processing finalize for split frame that has parent missing sentinel"
- "%{public}s processing finalize for split frame that has parent missing sentinel, backtrace limit exceeded"
- "%{public}s processing finalize for split frame that has parent missing sentinel, dumping backtrace:%{public}s"
- "%{public}s processing finalize for split frame that has parent missing sentinel, no backtrace"
- "%{public}s processing finalize for split frame that isn't a child"
- "%{public}s processing finalize for split frame that isn't a child, backtrace limit exceeded"
- "%{public}s processing finalize for split frame that isn't a child, dumping backtrace:%{public}s"
- "%{public}s processing finalize for split frame that isn't a child, no backtrace"
- "%{public}s split frame %p (%u bytes) into start child %p (%u bytes) and end child %p (%u bytes)"
- "4277.102.4"

```
