## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-934.120.4.0.0
-  __TEXT.__text: 0x2a9e4
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x300c
-  __TEXT.__const: 0xfa
-  __TEXT.__oslogstring: 0x13d5
-  __TEXT.__cstring: 0x2edc
-  __TEXT.__gcc_except_tab: 0x1358
+1000.0.0.0.0
+  __TEXT.__text: 0x2bf28
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x344c
+  __TEXT.__const: 0x10a
+  __TEXT.__oslogstring: 0x13f1
+  __TEXT.__cstring: 0x30cc
+  __TEXT.__gcc_except_tab: 0x1398
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xba8
-  __TEXT.__objc_classname: 0x4f7
-  __TEXT.__objc_methname: 0x6503
-  __TEXT.__objc_methtype: 0xea6
-  __TEXT.__objc_stubs: 0x5d00
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0x1b0
-  __DATA_CONST.__objc_protolist: 0x90
+  __TEXT.__unwind_info: 0xc28
+  __TEXT.__objc_classname: 0x67c
+  __TEXT.__objc_methname: 0x6b1a
+  __TEXT.__objc_methtype: 0xf6c
+  __TEXT.__objc_stubs: 0x6160
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1be0
+  __DATA_CONST.__objc_selrefs: 0x1d40
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x3280
-  __AUTH_CONST.__objc_const: 0x66a8
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__const: 0x5c8
+  __AUTH_CONST.__cfstring: 0x3580
+  __AUTH_CONST.__objc_const: 0x7978
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0xd60
-  __DATA.__objc_ivar: 0x32c
-  __DATA.__data: 0x9c8
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x448
+  __AUTH.__objc_data: 0x10d0
+  __DATA.__objc_ivar: 0x34c
+  __DATA.__data: 0xa98
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0x498
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FC81160F-AAB5-3CF7-971C-3A98382B8F1D
-  Functions: 1104
-  Symbols:   4209
-  CStrings:  2575
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: B5FC6AF4-1BA7-3D1C-B7DC-C17D095E2B2C
+  Functions: 1181
+  Symbols:   4513
+  CStrings:  2710
 
Symbols:
+ +[SKDiskImageCreateParams getDescriptorWithEncryption:]
+ +[SKDiskImageCreateParams getDescriptorWithFormat:]
+ +[SKDiskImageCreateParams getDiskImageEncryptionDescriptors]
+ +[SKDiskImageCreateParams getDiskImageFormatDescriptors]
+ +[SKDiskImageCreateParams supportsSecureCoding]
+ -[SKDIEncryptionDescriptorAES128 encryption]
+ -[SKDIEncryptionDescriptorAES128 name]
+ -[SKDIEncryptionDescriptorAES256 encryption]
+ -[SKDIEncryptionDescriptorAES256 name]
+ -[SKDIEncryptionDescriptorNONE encryption]
+ -[SKDIEncryptionDescriptorNONE name]
+ -[SKDIFormatDescriptorASIF defaultExtension]
+ -[SKDIFormatDescriptorASIF format]
+ -[SKDIFormatDescriptorASIF isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorASIF name]
+ -[SKDIFormatDescriptorRAW defaultExtension]
+ -[SKDIFormatDescriptorRAW format]
+ -[SKDIFormatDescriptorRAW isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorRAW name]
+ -[SKDIFormatDescriptorUDRO defaultExtension]
+ -[SKDIFormatDescriptorUDRO format]
+ -[SKDIFormatDescriptorUDRO isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorUDRO name]
+ -[SKDIFormatDescriptorUDSB defaultExtension]
+ -[SKDIFormatDescriptorUDSB format]
+ -[SKDIFormatDescriptorUDSB isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorUDSB name]
+ -[SKDIFormatDescriptorUDZO defaultExtension]
+ -[SKDIFormatDescriptorUDZO format]
+ -[SKDIFormatDescriptorUDZO isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorUDZO name]
+ -[SKDIFormatDescriptorULFO defaultExtension]
+ -[SKDIFormatDescriptorULFO format]
+ -[SKDIFormatDescriptorULFO isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorULFO name]
+ -[SKDIFormatDescriptorULMO defaultExtension]
+ -[SKDIFormatDescriptorULMO format]
+ -[SKDIFormatDescriptorULMO isSupportedForBlankInitialization]
+ -[SKDIFormatDescriptorULMO name]
+ -[SKDisk diskAndDescendants]
+ -[SKDiskImage chpassWithParams:error:]
+ -[SKDiskImage createBlankWithParams:progress:error:]
+ -[SKDiskImage createFromDiskWithParams:progress:completionBlock:]
+ -[SKDiskImage createFromFolderWithParams:progress:completionBlock:]
+ -[SKDiskImage createWithParams:completionBlock:]
+ -[SKDiskImage createWithParams:progressReadyHandler:completionBlock:]
+ -[SKDiskImage initWithURL:diParams:shadowURLs:error:]
+ -[SKDiskImage initWithURL:shadowURLs:error:]
+ -[SKDiskImage shadowURLs]
+ -[SKDiskImageAttachParams diAttachParamsWithURL:shadowURLs:error:]
+ -[SKDiskImageChpassParams diChpassParamsWithURL:error:]
+ -[SKDiskImageChpassParams init]
+ -[SKDiskImageChpassParams setStdinPassPhrase:]
+ -[SKDiskImageChpassParams setupDIChpassParams:]
+ -[SKDiskImageChpassParams stdinPassPhrase]
+ -[SKDiskImageCreateParams diCreatorFromFolderWithURL:error:]
+ -[SKDiskImageCreateParams diReadPassphraseExtraFlags]
+ -[SKDiskImageCreateParams encodeWithCoder:]
+ -[SKDiskImageCreateParams fsFormat]
+ -[SKDiskImageCreateParams initWithCoder:]
+ -[SKDiskImageCreateParams initWithDiskImage:format:shadowURLs:]
+ -[SKDiskImageCreateParams initWithFolder:]
+ -[SKDiskImageCreateParams initWithFolder:volumeName:format:]
+ -[SKDiskImageCreateParams initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:]
+ -[SKDiskImageCreateParams initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:fsFormat:shadowURLs:]
+ -[SKDiskImageCreateParams initWithNumBlocks:volumeName:format:fsFormat:]
+ -[SKDiskImageCreateParams setFsFormat:]
+ -[SKDiskImageCreateParams setPassphrase:encryptionMethod:]
+ -[SKDiskImageCreateParams setShadowURLs:]
+ -[SKDiskImageCreateParams setSourceFolder:]
+ -[SKDiskImageCreateParams setSourceImage:]
+ -[SKDiskImageCreateParams setTemporaryPassphrase:]
+ -[SKDiskImageCreateParams shadowURLs]
+ -[SKDiskImageCreateParams sourceFolder]
+ -[SKDiskImageCreateParams sourceImage]
+ -[SKDiskImageCreateParams temporaryPassphrase]
+ -[SKDiskImageInfoParams encryptionInfoOnly]
+ -[SKDiskImageInfoParams setEncryptionInfoOnly:]
+ -[SKTemporaryPassphrase buf]
+ -[SKTemporaryPassphrase dealloc]
+ -[SKTemporaryPassphrase initWithPassphrase:]
+ -[SKTemporaryPassphrase setBuf:]
+ GCC_except_table7
+ _OBJC_CLASS_$_DIChpassParams
+ _OBJC_CLASS_$_DICreateASIFParams
+ _OBJC_CLASS_$_DiskImageCreatorFromFolder
+ _OBJC_CLASS_$_SKDIEncryptionDescriptorAES128
+ _OBJC_CLASS_$_SKDIEncryptionDescriptorAES256
+ _OBJC_CLASS_$_SKDIEncryptionDescriptorNONE
+ _OBJC_CLASS_$_SKDIFormatDescriptorASIF
+ _OBJC_CLASS_$_SKDIFormatDescriptorRAW
+ _OBJC_CLASS_$_SKDIFormatDescriptorUDRO
+ _OBJC_CLASS_$_SKDIFormatDescriptorUDSB
+ _OBJC_CLASS_$_SKDIFormatDescriptorUDZO
+ _OBJC_CLASS_$_SKDIFormatDescriptorULFO
+ _OBJC_CLASS_$_SKDIFormatDescriptorULMO
+ _OBJC_CLASS_$_SKDiskImageChpassParams
+ _OBJC_CLASS_$_SKTemporaryPassphrase
+ _OBJC_IVAR_$_SKDiskImage._shadowURLs
+ _OBJC_IVAR_$_SKDiskImageChpassParams._stdinPassPhrase
+ _OBJC_IVAR_$_SKDiskImageCreateParams._fsFormat
+ _OBJC_IVAR_$_SKDiskImageCreateParams._shadowURLs
+ _OBJC_IVAR_$_SKDiskImageCreateParams._sourceFolder
+ _OBJC_IVAR_$_SKDiskImageCreateParams._sourceImage
+ _OBJC_IVAR_$_SKDiskImageCreateParams._temporaryPassphrase
+ _OBJC_IVAR_$_SKDiskImageInfoParams._encryptionInfoOnly
+ _OBJC_IVAR_$_SKTemporaryPassphrase._buf
+ _OBJC_METACLASS_$_SKDIEncryptionDescriptorAES128
+ _OBJC_METACLASS_$_SKDIEncryptionDescriptorAES256
+ _OBJC_METACLASS_$_SKDIEncryptionDescriptorNONE
+ _OBJC_METACLASS_$_SKDIFormatDescriptorASIF
+ _OBJC_METACLASS_$_SKDIFormatDescriptorRAW
+ _OBJC_METACLASS_$_SKDIFormatDescriptorUDRO
+ _OBJC_METACLASS_$_SKDIFormatDescriptorUDSB
+ _OBJC_METACLASS_$_SKDIFormatDescriptorUDZO
+ _OBJC_METACLASS_$_SKDIFormatDescriptorULFO
+ _OBJC_METACLASS_$_SKDIFormatDescriptorULMO
+ _OBJC_METACLASS_$_SKDiskImageChpassParams
+ _OBJC_METACLASS_$_SKTemporaryPassphrase
+ _SKAPFSVolumeRoleEnterprise
+ _SKFormatToDIFormat
+ __OBJC_$_CLASS_METHODS_SKDiskImageCreateParams
+ __OBJC_$_CLASS_PROP_LIST_SKDiskImageCreateParams
+ __OBJC_$_INSTANCE_METHODS_SKDIEncryptionDescriptorAES128
+ __OBJC_$_INSTANCE_METHODS_SKDIEncryptionDescriptorAES256
+ __OBJC_$_INSTANCE_METHODS_SKDIEncryptionDescriptorNONE
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorASIF
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorRAW
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorUDRO
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorUDSB
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorUDZO
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorULFO
+ __OBJC_$_INSTANCE_METHODS_SKDIFormatDescriptorULMO
+ __OBJC_$_INSTANCE_METHODS_SKDiskImageChpassParams
+ __OBJC_$_INSTANCE_METHODS_SKTemporaryPassphrase
+ __OBJC_$_INSTANCE_VARIABLES_SKDiskImageChpassParams
+ __OBJC_$_INSTANCE_VARIABLES_SKTemporaryPassphrase
+ __OBJC_$_PROP_LIST_SKDIEncryptionDescriptorAES128
+ __OBJC_$_PROP_LIST_SKDIEncryptionDescriptorAES256
+ __OBJC_$_PROP_LIST_SKDIEncryptionDescriptorNONE
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorASIF
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorRAW
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorUDRO
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorUDSB
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorUDZO
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorULFO
+ __OBJC_$_PROP_LIST_SKDIFormatDescriptorULMO
+ __OBJC_$_PROP_LIST_SKDiskImageChpassParams
+ __OBJC_$_PROP_LIST_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_$_PROP_LIST_SKDiskImageFormatDescriptorProtocol
+ __OBJC_$_PROP_LIST_SKTemporaryPassphrase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKDiskImageFormatDescriptorProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKDiskImageFormatDescriptorProtocol
+ __OBJC_$_PROTOCOL_REFS_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_$_PROTOCOL_REFS_SKDiskImageFormatDescriptorProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SKDIEncryptionDescriptorAES128
+ __OBJC_CLASS_PROTOCOLS_$_SKDIEncryptionDescriptorAES256
+ __OBJC_CLASS_PROTOCOLS_$_SKDIEncryptionDescriptorNONE
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorASIF
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorRAW
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorUDRO
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorUDSB
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorUDZO
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorULFO
+ __OBJC_CLASS_PROTOCOLS_$_SKDIFormatDescriptorULMO
+ __OBJC_CLASS_PROTOCOLS_$_SKDiskImageCreateParams
+ __OBJC_CLASS_RO_$_SKDIEncryptionDescriptorAES128
+ __OBJC_CLASS_RO_$_SKDIEncryptionDescriptorAES256
+ __OBJC_CLASS_RO_$_SKDIEncryptionDescriptorNONE
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorASIF
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorRAW
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorUDRO
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorUDSB
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorUDZO
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorULFO
+ __OBJC_CLASS_RO_$_SKDIFormatDescriptorULMO
+ __OBJC_CLASS_RO_$_SKDiskImageChpassParams
+ __OBJC_CLASS_RO_$_SKTemporaryPassphrase
+ __OBJC_LABEL_PROTOCOL_$_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_LABEL_PROTOCOL_$_SKDiskImageFormatDescriptorProtocol
+ __OBJC_METACLASS_RO_$_SKDIEncryptionDescriptorAES128
+ __OBJC_METACLASS_RO_$_SKDIEncryptionDescriptorAES256
+ __OBJC_METACLASS_RO_$_SKDIEncryptionDescriptorNONE
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorASIF
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorRAW
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorUDRO
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorUDSB
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorUDZO
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorULFO
+ __OBJC_METACLASS_RO_$_SKDIFormatDescriptorULMO
+ __OBJC_METACLASS_RO_$_SKDiskImageChpassParams
+ __OBJC_METACLASS_RO_$_SKTemporaryPassphrase
+ __OBJC_PROTOCOL_$_SKDiskImageEncryptionDescriptorProtocol
+ __OBJC_PROTOCOL_$_SKDiskImageFormatDescriptorProtocol
+ ___48-[SKDiskImage createWithParams:completionBlock:]_block_invoke
+ ___65-[SKDiskImage createFromDiskWithParams:progress:completionBlock:]_block_invoke
+ ___67-[SKDiskImage createFromFolderWithParams:progress:completionBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_literal_global.121
+ ___eraseDisk_block_invoke.125
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_StorageKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_StorageKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_StorageKit
+ _bzero
+ _kSKDiskRoleEnterprise
+ _malloc_type_malloc
+ _objc_msgSend$blockSize
+ _objc_msgSend$buf
+ _objc_msgSend$changePasswordWithParams:error:
+ _objc_msgSend$convertWithParams:completionBlock:
+ _objc_msgSend$createBlankWithParams:progress:error:
+ _objc_msgSend$createFromDiskWithParams:progress:completionBlock:
+ _objc_msgSend$createFromFolderWithParams:progress:completionBlock:
+ _objc_msgSend$createImageWithSrcFolder:completionBlock:
+ _objc_msgSend$createWithParams:completionBlock:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$diAttachParamsWithURL:shadowURLs:error:
+ _objc_msgSend$diChpassParamsWithURL:error:
+ _objc_msgSend$diCreatorFromFolderWithURL:error:
+ _objc_msgSend$diReadPassphraseExtraFlags
+ _objc_msgSend$diskAndDescendants
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encryptionInfoOnly
+ _objc_msgSend$encryptionMethod
+ _objc_msgSend$filesystemFor:
+ _objc_msgSend$fsFormat
+ _objc_msgSend$getDescriptorWithEncryption:
+ _objc_msgSend$getDescriptorWithFormat:
+ _objc_msgSend$initWithDiskImage:format:shadowURLs:
+ _objc_msgSend$initWithFolder:volumeName:format:
+ _objc_msgSend$initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:
+ _objc_msgSend$initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:fsFormat:shadowURLs:
+ _objc_msgSend$initWithInputURL:outputURL:shadowURLs:error:
+ _objc_msgSend$initWithNumBlocks:volumeName:format:fsFormat:
+ _objc_msgSend$initWithPassphrase:
+ _objc_msgSend$initWithURL:diParams:shadowURLs:error:
+ _objc_msgSend$initWithURL:shadowURLs:error:
+ _objc_msgSend$setBlockSize:
+ _objc_msgSend$setEncryption:
+ _objc_msgSend$setEncryptionInfoOnly:
+ _objc_msgSend$setImageFormat:
+ _objc_msgSend$setPassphrase:encryptionMethod:
+ _objc_msgSend$setPassphrase:encryptionMethod:error:
+ _objc_msgSend$setTemporaryPassphrase:
+ _objc_msgSend$setupDIChpassParams:
+ _objc_msgSend$shadowURLs
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sourceFolder
+ _objc_msgSend$sourceImage
+ _objc_msgSend$temporaryPassphrase
+ _objc_retain_x28
+ _strlcpy
+ _strnlen
+ _swift_bridgeObjectRetain
- +[SKDiskImage createBlankAt:params:error:]
- +[SKDiskImage diskImageConvertFromParamsAt:params:error:]
- +[SKDiskImage diskImageUnsafeWithURL:params:error:]
- -[SKDisk canBeErasedToRole:]
- -[SKDiskImageAttachParams diAttachParamsWithURL:error:]
- -[SKDiskImageCreateParams initWithFormat:sourceURL:]
- -[SKDiskImageCreateParams setSource:]
- -[SKDiskImageCreateParams source]
- GCC_except_table6
- _OBJC_IVAR_$_SKDiskImageCreateParams._source
- ___block_literal_global.21
- ___block_literal_global.43
- ___block_literal_global.60
- ___eraseDisk_block_invoke.31
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_StorageKit
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_StorageKit
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_StorageKit
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_StorageKit
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_StorageKit
- __swift_FORCE_LOAD_$_swiftos
- __swift_FORCE_LOAD_$_swiftos_$_StorageKit
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_StorageKit
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_StorageKit
- _eraseDisk
- _objc_msgSend$convertWithParams:error:
- _objc_msgSend$createBlankAt:params:error:
- _objc_msgSend$diAttachParamsWithURL:error:
- _objc_msgSend$diskImageConvertFromParamsAt:params:error:
- _objc_msgSend$diskImageUnsafeWithURL:params:error:
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$initWithFormat:sourceURL:
- _objc_msgSend$initWithInputURL:outputURL:error:
- _objc_msgSend$initWithURL:diParams:error:
- _objc_msgSend$isFileURL
- _objc_msgSend$setRawBlockSize:
- _objc_msgSend$source
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "%s: Could not create 'convert params': %@"
+ "%s: DiskImageCreatorFromFolder initialization failed: %@"
+ "%s: Failed to initialize SKDiskImage"
+ "*"
+ "*16@0:8"
+ "+[SKDiskImage diskImageWithURL:params:error:]"
+ "-[SKDiskImage createBlankWithParams:progress:error:]"
+ "-[SKDiskImage createFromDiskWithParams:progress:completionBlock:]"
+ "-[SKDiskImage createFromFolderWithParams:progress:completionBlock:]"
+ "<folder>"
+ "@\"SKTemporaryPassphrase\""
+ "@24@0:8r*16"
+ "@40@0:8@16@24q32"
+ "@40@0:8@16q24@32"
+ "@48@0:8Q16@24q32@40"
+ "@56@0:8q16@24@32@40Q48"
+ "@72@0:8q16@24@32@40Q48@56@64"
+ "AES 128-Bit"
+ "AES 256-Bit"
+ "ASIF (Apple Sparse Image Format)"
+ "Create from device failed: %@"
+ "Creation from folder failed: %@"
+ "F"
+ "Failed to change passphrase for image"
+ "LZFSE Compressed (Read-Only)"
+ "LZMA Compressed (Read-Only)"
+ "Raw"
+ "SKAPFSVolumeRoleEnterprise"
+ "SKDIEncryptionDescriptorAES128"
+ "SKDIEncryptionDescriptorAES256"
+ "SKDIEncryptionDescriptorNONE"
+ "SKDIFormatDescriptorASIF"
+ "SKDIFormatDescriptorRAW"
+ "SKDIFormatDescriptorUDRO"
+ "SKDIFormatDescriptorUDSB"
+ "SKDIFormatDescriptorUDZO"
+ "SKDIFormatDescriptorULFO"
+ "SKDIFormatDescriptorULMO"
+ "SKDiskImageChpassParams"
+ "SKDiskImageEncryptionDescriptorProtocol"
+ "SKDiskImageFormatDescriptorProtocol"
+ "SKTemporaryPassphrase"
+ "Sparse Bundle"
+ "T*,N,V_buf"
+ "T@\"NSArray\",&,N,V_shadowURLs"
+ "T@\"NSArray\",R,N,V_shadowURLs"
+ "T@\"NSURL\",&,N,V_sourceFolder"
+ "T@\"NSURL\",&,N,V_sourceImage"
+ "T@\"SKFilesystem\",&,N,V_fsFormat"
+ "T@\"SKTemporaryPassphrase\",&,N,V_temporaryPassphrase"
+ "TB,N,V_encryptionInfoOnly"
+ "Tq,R,N"
+ "Uncompressed (Read-Only)"
+ "Unencrypted"
+ "ZLIB Compressed (Read-Only)"
+ "_buf"
+ "_encryptionInfoOnly"
+ "_fsFormat"
+ "_shadowURLs"
+ "_sourceFolder"
+ "_sourceImage"
+ "_temporaryPassphrase"
+ "asif"
+ "blockSize"
+ "buf"
+ "changePasswordWithParams:error:"
+ "chpassWithParams:error:"
+ "convertWithParams:completionBlock:"
+ "createBlankWithParams:progress:error:"
+ "createFromDiskWithParams:progress:completionBlock:"
+ "createFromFolderWithParams:progress:completionBlock:"
+ "createImageWithSrcFolder:completionBlock:"
+ "createWithParams:completionBlock:"
+ "createWithParams:progressReadyHandler:completionBlock:"
+ "decodeBoolForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectForKey:"
+ "defaultExtension"
+ "diAttachParamsWithURL:shadowURLs:error:"
+ "diChpassParamsWithURL:error:"
+ "diCreatorFromFolderWithURL:error:"
+ "diReadPassphraseExtraFlags"
+ "diskAndDescendants"
+ "dmg"
+ "encodeBool:forKey:"
+ "encodeInt64:forKey:"
+ "encryptionInfoOnly"
+ "encryptionMethod"
+ "fsFormat"
+ "getDescriptorWithEncryption:"
+ "getDescriptorWithFormat:"
+ "getDiskImageEncryptionDescriptors"
+ "getDiskImageFormatDescriptors"
+ "initWithDiskImage:format:shadowURLs:"
+ "initWithFolder:"
+ "initWithFolder:volumeName:format:"
+ "initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:"
+ "initWithFormat:sourceImage:sourceFolder:volumeName:numBlocks:fsFormat:shadowURLs:"
+ "initWithInputURL:outputURL:shadowURLs:error:"
+ "initWithNumBlocks:volumeName:format:fsFormat:"
+ "initWithPassphrase:"
+ "initWithURL:diParams:shadowURLs:error:"
+ "initWithURL:shadowURLs:error:"
+ "isSupportedForBlankInitialization"
+ "kSKDiskRoleEnterprise"
+ "kSKDiskRoleInstaller"
+ "setBlockSize:"
+ "setBuf:"
+ "setEncryptionInfoOnly:"
+ "setFsFormat:"
+ "setImageFormat:"
+ "setPassphrase:encryptionMethod:"
+ "setPassphrase:encryptionMethod:error:"
+ "setShadowURLs:"
+ "setSourceFolder:"
+ "setSourceImage:"
+ "setTemporaryPassphrase:"
+ "setupDIChpassParams:"
+ "shadowURLs"
+ "sharedInstance"
+ "sourceFolder"
+ "sourceImage"
+ "sparsebundle"
+ "temporaryPassphrase"
+ "v24@0:8*16"
+ "v32@0:8r*16q24"
+ "v40@0:8@16@?24@?32"
- "%s: Could not create 'convert params' %@"
- "%s: Couldn't mount disk %@"
- "%s: Failed to create blank disk image %@"
- "%s: Failed to create disk image %@"
- "+[SKDiskImage createBlankAt:params:error:]"
- "+[SKDiskImage diskImageUnsafeWithURL:params:error:]"
- "Could not convert with %@"
- "T@\"NSURL\",&,N,V_source"
- "Unhandled exception during create: %@"
- "_source"
- "canBeErasedToRole:"
- "convertWithParams:error:"
- "createBlankAt:params:error:"
- "diAttachParamsWithURL:error:"
- "diskImageConvertFromParamsAt:params:error:"
- "diskImageUnsafeWithURL:params:error:"
- "fileExistsAtPath:"
- "initWithFormat:sourceURL:"
- "initWithInputURL:outputURL:error:"
- "isFileURL"
- "kSKDIskRoleInstaller"
- "setRawBlockSize:"
- "setSource:"
- "source"

```
