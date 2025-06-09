## CloudSharing

> `/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing`

```diff

-188.5.1.0.0
-  __TEXT.__text: 0x18e60
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x2bc
-  __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x867
-  __TEXT.__swift5_typeref: 0x321
-  __TEXT.__swift5_capture: 0x358
-  __TEXT.__oslogstring: 0xa2f
-  __TEXT.__constg_swiftt: 0x160
-  __TEXT.__swift5_fieldmd: 0x3c
+209.0.0.0.0
+  __TEXT.__text: 0x1bc84
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x348
+  __TEXT.__const: 0x2f8
+  __TEXT.__cstring: 0xa27
+  __TEXT.__constg_swiftt: 0x188
+  __TEXT.__swift5_typeref: 0x343
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x23
+  __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__swift5_capture: 0x448
+  __TEXT.__oslogstring: 0xb4c
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x1c
-  __TEXT.__objc_methname: 0x11c1
-  __TEXT.__objc_methtype: 0xf6
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x110
+  __TEXT.__objc_methname: 0x1532
+  __TEXT.__objc_methtype: 0xb1
+  __TEXT.__objc_stubs: 0x2c0
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x208
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0xe90
-  __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__const: 0x12a0
+  __AUTH_CONST.__objc_const: 0x278
   __AUTH.__objc_data: 0x48
-  __DATA.__data: 0xa0
+  __DATA.__data: 0x110
   __DATA.__bss: 0x310
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
+  - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A1E3EADD-E854-3F6C-94E2-B226BD87D1F1
-  Functions: 330
-  Symbols:   465
-  CStrings:  168
+  UUID: 6A4426C9-B74C-341E-BBD3-FE13DF9D8225
+  Functions: 406
+  Symbols:   518
+  CStrings:  189
 
Symbols:
+ +[CSCloudSharing addParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:completionHandler:]
+ +[CSCloudSharing addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:optionsGroups:completionHandler:]
+ +[CSCloudSharing completeShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:completionHandler:]
+ +[CSCloudSharing shareFileOrFolderURL:emailAddresses:phoneNumbers:optionsGroups:completionHandler:]
+ +[CSCloudSharing shareFolderRemovingSubshares:emailAddresses:phoneNumbers:optionsGroups:completionHandler:]
+ _NSURLLocalizedNameKey
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$__SWCollaborationOptionsGroup
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CloudSharing
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CloudSharing
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CloudSharing
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CloudSharing
+ _block_copy_helper.100
+ _block_copy_helper.106
+ _block_copy_helper.112
+ _block_copy_helper.118
+ _block_copy_helper.124
+ _block_copy_helper.136
+ _block_copy_helper.147
+ _block_copy_helper.157
+ _block_copy_helper.168
+ _block_copy_helper.179
+ _block_copy_helper.190
+ _block_copy_helper.201
+ _block_copy_helper.212
+ _block_copy_helper.223
+ _block_copy_helper.233
+ _block_copy_helper.244
+ _block_copy_helper.254
+ _block_copy_helper.264
+ _block_copy_helper.274
+ _block_copy_helper.285
+ _block_copy_helper.296
+ _block_copy_helper.306
+ _block_copy_helper.317
+ _block_copy_helper.328
+ _block_copy_helper.339
+ _block_copy_helper.350
+ _block_copy_helper.360
+ _block_copy_helper.363
+ _block_descriptor.102
+ _block_descriptor.108
+ _block_descriptor.114
+ _block_descriptor.120
+ _block_descriptor.126
+ _block_descriptor.138
+ _block_descriptor.149
+ _block_descriptor.159
+ _block_descriptor.170
+ _block_descriptor.181
+ _block_descriptor.192
+ _block_descriptor.203
+ _block_descriptor.214
+ _block_descriptor.225
+ _block_descriptor.235
+ _block_descriptor.246
+ _block_descriptor.256
+ _block_descriptor.266
+ _block_descriptor.276
+ _block_descriptor.287
+ _block_descriptor.298
+ _block_descriptor.308
+ _block_descriptor.319
+ _block_descriptor.330
+ _block_descriptor.341
+ _block_descriptor.352
+ _block_descriptor.362
+ _block_descriptor.365
+ _block_destroy_helper.101
+ _block_destroy_helper.107
+ _block_destroy_helper.113
+ _block_destroy_helper.119
+ _block_destroy_helper.125
+ _block_destroy_helper.137
+ _block_destroy_helper.148
+ _block_destroy_helper.158
+ _block_destroy_helper.169
+ _block_destroy_helper.180
+ _block_destroy_helper.191
+ _block_destroy_helper.202
+ _block_destroy_helper.213
+ _block_destroy_helper.224
+ _block_destroy_helper.234
+ _block_destroy_helper.245
+ _block_destroy_helper.255
+ _block_destroy_helper.265
+ _block_destroy_helper.275
+ _block_destroy_helper.286
+ _block_destroy_helper.297
+ _block_destroy_helper.307
+ _block_destroy_helper.318
+ _block_destroy_helper.329
+ _block_destroy_helper.340
+ _block_destroy_helper.351
+ _block_destroy_helper.361
+ _block_destroy_helper.364
+ _objc_msgSend$callForAddParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:reply:
+ _objc_msgSend$callForAddParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:optionsGroups:reply:
+ _objc_msgSend$callForCloudKitAddToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:reply:
+ _objc_msgSend$callForFileSharing:emailAddresses:phoneNumbers:optionsGroups:reply:
+ _objc_msgSend$callForForciblyShareFolder:emailAddresses:phoneNumbers:optionsGroups:reply:
+ _objc_retain_x27
+ _protocol_copyMethodDescriptionList
+ _swift_initStackObject
+ _swift_setDeallocating
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
+ _symbolic yXlXp
- +[CSCloudSharing completeShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:]
- +[CSCloudSharing shareFileOrFolderShareURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:]
- +[CSCloudSharing shareFileOrFolderURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:]
- _BRCloudDocsErrorDomain
- ___156+[CSCloudSharing shareFileOrFolderURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:]_block_invoke
- ___168+[CSCloudSharing completeShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e39_v32?0"NSURL"8"CKShare"16"NSError"24ls32l8
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CloudSharing
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CloudSharing
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CloudSharing
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CloudSharing
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CloudSharing
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CloudSharing
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CloudSharing
- _block_copy_helper.109
- _block_copy_helper.119
- _block_copy_helper.130
- _block_copy_helper.141
- _block_copy_helper.152
- _block_copy_helper.163
- _block_copy_helper.173
- _block_copy_helper.184
- _block_copy_helper.194
- _block_copy_helper.204
- _block_copy_helper.214
- _block_copy_helper.225
- _block_copy_helper.236
- _block_copy_helper.246
- _block_copy_helper.257
- _block_copy_helper.268
- _block_copy_helper.278
- _block_copy_helper.281
- _block_descriptor.111
- _block_descriptor.121
- _block_descriptor.132
- _block_descriptor.143
- _block_descriptor.154
- _block_descriptor.165
- _block_descriptor.175
- _block_descriptor.186
- _block_descriptor.196
- _block_descriptor.206
- _block_descriptor.216
- _block_descriptor.227
- _block_descriptor.238
- _block_descriptor.248
- _block_descriptor.259
- _block_descriptor.270
- _block_descriptor.280
- _block_descriptor.283
- _block_destroy_helper.110
- _block_destroy_helper.120
- _block_destroy_helper.131
- _block_destroy_helper.142
- _block_destroy_helper.153
- _block_destroy_helper.164
- _block_destroy_helper.174
- _block_destroy_helper.185
- _block_destroy_helper.195
- _block_destroy_helper.205
- _block_destroy_helper.215
- _block_destroy_helper.226
- _block_destroy_helper.237
- _block_destroy_helper.247
- _block_destroy_helper.258
- _block_destroy_helper.269
- _block_destroy_helper.279
- _block_destroy_helper.282
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$completeShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:completionHandler:
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$shareFileOrFolderURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:completionHandler:
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "CloudSharing/InitiateSharing.swift"
+ "Fatal error"
+ "SPIHelper function count for allowed classes (%ld) doesn't match the number of functions in the protocol: %ld"
+ "Unable to convert workSet to Set<AnyHashable>"
+ "addObject:"
+ "addParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:completionHandler:"
+ "addParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:optionsGroups:completionHandler:"
+ "addParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "addToCloudKitSharing:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "callForAddParticipantsToShare optionsGroups: %s"
+ "callForAddParticipantsToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:reply:"
+ "callForAddParticipantsToShareWithURLWrapper:share:emailAddresses:phoneNumbers:optionsGroups:reply:"
+ "callForCloudKitAddToShare optionsGroups: %s"
+ "callForCloudKitAddToShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:reply:"
+ "callForFileSharing optionsGroups: %s"
+ "callForFileSharing:emailAddresses:phoneNumbers:optionsGroups:reply:"
+ "callForForciblyShareFolder:emailAddresses:phoneNumbers:optionsGroups:reply:"
+ "completeShare:containerSetupInfo:emailAddresses:phoneNumbers:optionsGroups:completionHandler:"
+ "extensionlessName error: %s"
+ "forciblyShareFolder:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "shareFileOrFolderURL:emailAddresses:phoneNumbers:optionsGroups:completionHandler:"
+ "shareFolderRemovingSubshares:emailAddresses:phoneNumbers:optionsGroups:completionHandler:"
+ "startFileSharing:emailAddresses:phoneNumbers:optionsGroups:withReply:"
+ "v56@0:8@\"NSURL\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">48"
+ "v64@0:8@\"CKShare\"16@\"CKContainerSetupInfo\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">56"
+ "v64@0:8@\"FPSandboxingURLWrapper\"16@\"CKShare\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48@?<v@?@\"NSURL\"@\"CKShare\"@\"NSError\">56"
- "completeShare:containerSetupInfo:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "errorWithDomain:code:userInfo:"
- "shareFileOrFolderShareURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "shareFileOrFolderURL:emailAddresses:phoneNumbers:accessType:permissionType:allowOthersToInvite:keepExistingParticipants:completionHandler:"
- "v72@0:8@16@24@32q40q48B56B60@?64"
- "v80@0:8@16@24@32@40q48q56B64B68@?72"

```
