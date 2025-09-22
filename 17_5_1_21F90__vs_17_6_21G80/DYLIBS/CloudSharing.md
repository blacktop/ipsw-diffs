## CloudSharing

> `/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing`

```diff

-177.0.0.0.0
-  __TEXT.__text: 0x15074
+177.6.2.0.0
+  __TEXT.__text: 0x16608
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x29a
-  __TEXT.__cstring: 0x1417
+  __TEXT.__cstring: 0x14c7
   __TEXT.__swift5_typeref: 0x319
-  __TEXT.__swift5_capture: 0x2f8
-  __TEXT.__constg_swiftt: 0x150
+  __TEXT.__swift5_capture: 0x328
+  __TEXT.__constg_swiftt: 0x158
   __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x23
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x264
+  __TEXT.__unwind_info: 0x274
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1c
-  __TEXT.__objc_methname: 0xfb9
+  __TEXT.__objc_methname: 0x1123
   __TEXT.__objc_methtype: 0xf6
-  __TEXT.__objc_stubs: 0x240
+  __TEXT.__objc_stubs: 0x260
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1f8
-  __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__objc_const: 0x200
+  __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x28
-  __AUTH_CONST.__const: 0xdf8
+  __AUTH_CONST.__const: 0xec0
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_data: 0x170
+  __DATA.__objc_data: 0x188
   __DATA.__data: 0xa0
   __DATA.__bss: 0x310
-  __DATA_DIRTY.__objc_data: 0x180
+  __DATA_DIRTY.__objc_data: 0x188
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2BEE509D-6ECE-38CC-8197-FF8343CC9C64
-  Functions: 328
-  Symbols:   422
-  CStrings:  171
+  UUID: 939E0ABE-64CA-3D40-92BC-A8F5AB4FCACC
+  Functions: 344
+  Symbols:   437
+  CStrings:  176
 
Symbols:
+ +[CSCloudSharing addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:completionHandler:]
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFileProvider_$_CloudSharing
+ _block_copy_helper.103
+ _block_copy_helper.113
+ _block_copy_helper.124
+ _block_copy_helper.135
+ _block_copy_helper.146
+ _block_copy_helper.157
+ _block_copy_helper.167
+ _block_copy_helper.178
+ _block_copy_helper.188
+ _block_copy_helper.198
+ _block_copy_helper.208
+ _block_copy_helper.219
+ _block_copy_helper.229
+ _block_copy_helper.240
+ _block_copy_helper.251
+ _block_copy_helper.261
+ _block_copy_helper.264
+ _block_copy_helper.88
+ _block_descriptor.105
+ _block_descriptor.115
+ _block_descriptor.126
+ _block_descriptor.137
+ _block_descriptor.148
+ _block_descriptor.159
+ _block_descriptor.169
+ _block_descriptor.180
+ _block_descriptor.190
+ _block_descriptor.200
+ _block_descriptor.210
+ _block_descriptor.221
+ _block_descriptor.231
+ _block_descriptor.242
+ _block_descriptor.253
+ _block_descriptor.263
+ _block_descriptor.266
+ _block_descriptor.90
+ _block_destroy_helper.104
+ _block_destroy_helper.114
+ _block_destroy_helper.125
+ _block_destroy_helper.136
+ _block_destroy_helper.147
+ _block_destroy_helper.158
+ _block_destroy_helper.168
+ _block_destroy_helper.179
+ _block_destroy_helper.189
+ _block_destroy_helper.199
+ _block_destroy_helper.209
+ _block_destroy_helper.220
+ _block_destroy_helper.230
+ _block_destroy_helper.241
+ _block_destroy_helper.252
+ _block_destroy_helper.262
+ _block_destroy_helper.265
+ _block_destroy_helper.89
+ _objc_msgSend$callForAddParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:reply:
- _block_copy_helper.107
- _block_copy_helper.118
- _block_copy_helper.129
- _block_copy_helper.140
- _block_copy_helper.150
- _block_copy_helper.161
- _block_copy_helper.171
- _block_copy_helper.181
- _block_copy_helper.191
- _block_copy_helper.202
- _block_copy_helper.212
- _block_copy_helper.223
- _block_copy_helper.234
- _block_copy_helper.244
- _block_copy_helper.247
- _block_copy_helper.97
- _block_descriptor.109
- _block_descriptor.120
- _block_descriptor.131
- _block_descriptor.142
- _block_descriptor.152
- _block_descriptor.163
- _block_descriptor.173
- _block_descriptor.183
- _block_descriptor.193
- _block_descriptor.204
- _block_descriptor.214
- _block_descriptor.225
- _block_descriptor.236
- _block_descriptor.246
- _block_descriptor.249
- _block_descriptor.99
- _block_destroy_helper.108
- _block_destroy_helper.119
- _block_destroy_helper.130
- _block_destroy_helper.141
- _block_destroy_helper.151
- _block_destroy_helper.162
- _block_destroy_helper.172
- _block_destroy_helper.182
- _block_destroy_helper.192
- _block_destroy_helper.203
- _block_destroy_helper.213
- _block_destroy_helper.224
- _block_destroy_helper.235
- _block_destroy_helper.245
- _block_destroy_helper.248
- _block_destroy_helper.98
CStrings:
+ "addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:completionHandler:"
+ "addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:withReply:"
+ "callForAddParticipantsToShare urlWrapper: %@"
+ "callForAddParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:permissionType:allowOthersToInvite:reply:"
+ "v68@0:8@\"FPSandboxingURLWrapper\"16@\"CKShare\"24@\"NSArray\"32@\"NSArray\"40q48B56@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">60"

```
