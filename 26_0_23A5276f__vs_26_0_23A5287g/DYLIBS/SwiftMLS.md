## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

```diff

-195.0.8.0.0
-  __TEXT.__text: 0x1ef49c
+195.0.11.0.0
+  __TEXT.__text: 0x1f3244
   __TEXT.__auth_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x1d968
+  __TEXT.__const: 0x1d988
   __TEXT.__cstring: 0x31e9
-  __TEXT.__constg_swiftt: 0x3fc8
+  __TEXT.__constg_swiftt: 0x3ff0
   __TEXT.__swift5_typeref: 0x3224
-  __TEXT.__swift5_reflstr: 0x4a7d
-  __TEXT.__swift5_fieldmd: 0x5008
+  __TEXT.__swift5_reflstr: 0x4aad
+  __TEXT.__swift5_fieldmd: 0x502c
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0xac0
   __TEXT.__swift5_proto: 0xc20

   __TEXT.__swift5_capture: 0x3ac
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x178
-  __TEXT.__oslogstring: 0x36b6
-  __TEXT.__swift_as_entry: 0x480
-  __TEXT.__swift_as_ret: 0x844
-  __TEXT.__unwind_info: 0x7cd0
-  __TEXT.__eh_frame: 0x166a4
+  __TEXT.__oslogstring: 0x3786
+  __TEXT.__swift_as_entry: 0x488
+  __TEXT.__swift_as_ret: 0x860
+  __TEXT.__unwind_info: 0x7d68
+  __TEXT.__eh_frame: 0x169fc
   __TEXT.__objc_methname: 0x11e
   __DATA_CONST.__got: 0x908
   __DATA_CONST.__const: 0xe8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __AUTH_CONST.__auth_got: 0x1680
-  __AUTH_CONST.__const: 0x9cd0
+  __AUTH_CONST.__const: 0x9cd8
   __AUTH_CONST.__objc_const: 0x1130
   __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x4220
+  __AUTH.__data: 0x4258
   __DATA.__data: 0x2c38
   __DATA.__bss: 0x17e00
   __DATA.__common: 0x4f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BE0CC9C3-08FE-37E2-9911-1709EE691F94
-  Functions: 8590
-  Symbols:   2122
-  CStrings:  621
+  UUID: D2516FAC-46E4-3DEF-9741-EEF9D9E3FCF6
+  Functions: 8623
+  Symbols:   2124
+  CStrings:  625
 
Symbols:
+ ___swift_memcpy50_8
+ _block_copy_helper.152
+ _block_copy_helper.161
+ _block_copy_helper.169
+ _block_copy_helper.201
+ _block_copy_helper.207
+ _block_copy_helper.222
+ _block_copy_helper.226
+ _block_descriptor.154
+ _block_descriptor.163
+ _block_descriptor.171
+ _block_descriptor.203
+ _block_descriptor.209
+ _block_descriptor.224
+ _block_descriptor.228
+ _block_destroy_helper.153
+ _block_destroy_helper.162
+ _block_destroy_helper.170
+ _block_destroy_helper.202
+ _block_destroy_helper.208
+ _block_destroy_helper.223
+ _block_destroy_helper.227
- _block_copy_helper.149
- _block_copy_helper.157
- _block_copy_helper.166
- _block_copy_helper.195
- _block_copy_helper.204
- _block_copy_helper.213
- _block_copy_helper.220
- _block_descriptor.151
- _block_descriptor.159
- _block_descriptor.168
- _block_descriptor.197
- _block_descriptor.206
- _block_descriptor.215
- _block_descriptor.222
- _block_destroy_helper.150
- _block_destroy_helper.158
- _block_destroy_helper.167
- _block_destroy_helper.196
- _block_destroy_helper.205
- _block_destroy_helper.214
- _block_destroy_helper.221
CStrings:
+ "%s: Committer was self, but cachedStateAndCommitMetadata was already nil"
+ "%s: Deleting client"
+ "%s: Deleting group %s"
+ "%s: Deleting overall client state"
+ "%s: New group contains members that were not in the existing state"
+ "%s: advanced to new state"
+ "%s: advancing to new state, caused by a re-add"
+ "%s: parsed group info: %s, group ID: %s"
+ "%s: parsed key package: %s"
+ "After receiving a Welcome for an existing group, did not find existing group state for %s"
+ "Not configured to use eras, so skipping all processWelcomeForExistingGroup logic"
- "%s: deleting client"
- "Not configured to use eras, so skipping era advancement check"
- "Received Welcome for new era %u that contains members that were not in the previous era %u"
- "Received Welcome for new era %u that is not greater than the current era %u"
- "While checking for era advancement, did not find an existing group for %s"
- "parsed group info: %s"
- "parsed key package: %s"

```
