## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

```diff

-195.0.14.0.0
-  __TEXT.__text: 0x1fa8cc
+195.40.5.502.1
+  __TEXT.__text: 0x200728
   __TEXT.__auth_stubs: 0x2d40
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x1db68
-  __TEXT.__cstring: 0x3339
-  __TEXT.__constg_swiftt: 0x4050
-  __TEXT.__swift5_typeref: 0x3264
-  __TEXT.__swift5_reflstr: 0x4b1d
-  __TEXT.__swift5_fieldmd: 0x50a0
+  __TEXT.__const: 0x1dd78
+  __TEXT.__cstring: 0x3399
+  __TEXT.__constg_swiftt: 0x4090
+  __TEXT.__swift5_typeref: 0x328e
+  __TEXT.__swift5_reflstr: 0x4bdd
+  __TEXT.__swift5_fieldmd: 0x5138
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0xac0
-  __TEXT.__swift5_proto: 0xc40
-  __TEXT.__swift5_types: 0x5a8
+  __TEXT.__swift5_proto: 0xc44
+  __TEXT.__swift5_types: 0x5b0
   __TEXT.__swift5_capture: 0x3bc
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x178
-  __TEXT.__oslogstring: 0x3da6
-  __TEXT.__swift_as_entry: 0x498
-  __TEXT.__swift_as_ret: 0x898
-  __TEXT.__unwind_info: 0x7ef0
-  __TEXT.__eh_frame: 0x16fcc
+  __TEXT.__oslogstring: 0x4006
+  __TEXT.__swift_as_entry: 0x49c
+  __TEXT.__swift_as_ret: 0x8ac
+  __TEXT.__unwind_info: 0x7f98
+  __TEXT.__eh_frame: 0x172bc
   __TEXT.__objc_methname: 0x148
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__const: 0xe8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x16a0
-  __AUTH_CONST.__const: 0xad38
+  __AUTH_CONST.__const: 0xae38
   __AUTH_CONST.__objc_const: 0x1130
   __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x4280
-  __DATA.__data: 0x2c88
-  __DATA.__bss: 0x18200
+  __AUTH.__data: 0x4288
+  __DATA.__data: 0x2c98
+  __DATA.__bss: 0x18280
   __DATA.__common: 0x4f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 395F14B5-D827-304D-B26A-BEB9A96CE304
-  Functions: 8728
-  Symbols:   2136
-  CStrings:  663
+  UUID: 805684C0-C972-385A-96F6-F545CD7A30EF
+  Functions: 8767
+  Symbols:   2142
+  CStrings:  675
 
Symbols:
+ ___swift_memcpy355_8
+ ___swift_memcpy42_8
+ _block_copy_helper.163
+ _block_copy_helper.175
+ _block_copy_helper.191
+ _block_copy_helper.200
+ _block_copy_helper.218
+ _block_copy_helper.225
+ _block_copy_helper.238
+ _block_descriptor.165
+ _block_descriptor.177
+ _block_descriptor.193
+ _block_descriptor.202
+ _block_descriptor.220
+ _block_descriptor.227
+ _block_descriptor.240
+ _block_destroy_helper.164
+ _block_destroy_helper.176
+ _block_destroy_helper.192
+ _block_destroy_helper.201
+ _block_destroy_helper.219
+ _block_destroy_helper.226
+ _block_destroy_helper.239
+ _symbolic _____ 8SwiftMLS0B0O18SelfRemoveProposalV
+ _symbolic _____ 8SwiftMLS0B0O19SecretPayloadHeaderV
+ _symbolic _____6sender______4dataACSg9messageIDAE015originalMessageD0_____Sg14generationUsedt 8SwiftMLS0B0O9LeafIndexV 10Foundation4DataV s6UInt32V
+ _symbolic _____m 8SwiftMLS0B0O19SecretPayloadHeaderV
+ _type_layout_string 8SwiftMLS0B0O19SecretPayloadHeaderV
- ___swift_memcpy160_8
- ___swift_memcpy26_8
- ___swift_memcpy354_8
- _block_copy_helper.161
- _block_copy_helper.174
- _block_copy_helper.190
- _block_copy_helper.198
- _block_copy_helper.216
- _block_copy_helper.222
- _block_copy_helper.237
- _block_descriptor.163
- _block_descriptor.176
- _block_descriptor.192
- _block_descriptor.200
- _block_descriptor.218
- _block_descriptor.224
- _block_descriptor.239
- _block_destroy_helper.162
- _block_destroy_helper.175
- _block_destroy_helper.191
- _block_destroy_helper.199
- _block_destroy_helper.217
- _block_destroy_helper.223
- _block_destroy_helper.238
- _symbolic _____6sender______4dataACSg9messageIDAE015originalMessageD0t 8SwiftMLS0B0O9LeafIndexV 10Foundation4DataV
CStrings:
+ "%s: Invalid key generation in secret payload, expected %u, got %u"
+ "%s: advancing to new state"
+ "%s: advancing to new state %s"
+ "%s: did not find current state for epoch %s, likely processing a resync"
+ "%s: found current state for epoch %s"
+ "%s: key generation validated, was %u"
+ "%s: message has wire format %hu and was for %s"
+ "%s: message was client's own commit, hash %s, returning cached state"
+ "%s: message was not client's own commit, hash %s"
+ "%s: processed cached commit, returning"
+ "%s: received application message with generation in the secret payload of %u, but generation used was %s"
+ "%s: validating key generation"
+ "ValidateKeyGeneration"
+ "com.apple.swiftmls MLS 1.0 MLSMessage Reference"
+ "sender data messageID originalMessageID generationUsed "
- "%s: advancing to new state, caused by a re-add"
- "message has wire format %hu and was for %s"
- "sender data messageID originalMessageID "

```
