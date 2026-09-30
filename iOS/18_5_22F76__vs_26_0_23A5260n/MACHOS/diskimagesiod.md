## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-385.120.4.0.0
-  __TEXT.__text: 0x1522e4
-  __TEXT.__auth_stubs: 0x2010
-  __TEXT.__objc_stubs: 0x5680
-  __TEXT.__objc_methlist: 0x30bc
-  __TEXT.__gcc_except_tab: 0x126f0
-  __TEXT.__const: 0xc67c
-  __TEXT.__cstring: 0xe047
-  __TEXT.__oslogstring: 0x1f4b
-  __TEXT.__objc_methname: 0x6561
-  __TEXT.__objc_classname: 0x5b1
-  __TEXT.__objc_methtype: 0x1f25
+485.0.0.0.0
+  __TEXT.__text: 0x192554
+  __TEXT.__auth_stubs: 0x2160
+  __TEXT.__objc_stubs: 0x5b80
+  __TEXT.__objc_methlist: 0x340c
+  __TEXT.__gcc_except_tab: 0x164ec
+  __TEXT.__const: 0x10e24
+  __TEXT.__cstring: 0xfcaf
+  __TEXT.__oslogstring: 0x2001
+  __TEXT.__objc_methname: 0x691e
+  __TEXT.__objc_classname: 0x604
+  __TEXT.__objc_methtype: 0x2151
   __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_typeref: 0x4f
+  __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0x9970
-  __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x1020
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x28ec8
-  __DATA_CONST.__cfstring: 0x3c00
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__unwind_info: 0xb5a0
+  __TEXT.__eh_frame: 0x150
+  __DATA_CONST.__auth_got: 0x10c8
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x304e0
+  __DATA_CONST.__cfstring: 0x3e00
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x4e00
-  __DATA.__objc_selrefs: 0x1a20
-  __DATA.__objc_ivar: 0x2a8
-  __DATA.__objc_data: 0x1520
-  __DATA.__data: 0xc00
-  __DATA.__bss: 0x130
-  __DATA.__common: 0x9
+  __DATA.__objc_const: 0x5220
+  __DATA.__objc_selrefs: 0x1b68
+  __DATA.__objc_ivar: 0x2bc
+  __DATA.__objc_data: 0x1660
+  __DATA.__data: 0xc28
+  __DATA.__bss: 0x160
+  __DATA.__common: 0x19
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /usr/lib/libAppleArchive.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
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
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: A754A1E6-3988-3558-A5B2-2B8170DFF147
-  Functions: 7916
-  Symbols:   709
-  CStrings:  3830
+  UUID: F260880C-88C5-3A5E-8328-ECC3755B9010
+  Functions: 9383
+  Symbols:   731
+  CStrings:  4030
 
Symbols:
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSProgress
+ __ZNSt3__119__shared_mutex_baseC1Ev
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _analytics_send_event_lazy
+ _cc_clear
+ _ccaes_cbc_decrypt_mode
+ _ccaes_cbc_encrypt_mode
+ _ccaes_xts_decrypt_mode
+ _ccaes_xts_encrypt_mode
+ _cccbc_init
+ _cccbc_set_iv
+ _cccbc_update
+ _cccmac_final_generate
+ _cccmac_init
+ _cccmac_update
+ _cchmac_final
+ _cchmac_init
+ _cchmac_update
+ _ccsha1_di
+ _ccxts_init
+ _ccxts_set_tweak
+ _ccxts_update
+ _ffsctl
+ _kSecUseDataProtectionKeychain
+ _objc_exception_rethrow
+ _objc_retainBlock
+ _objc_retain_x9
+ _statfs
+ _swift_arrayDestroy
+ _swift_setDeallocating
+ _vm_page_size
+ _xpc_dictionary_create
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
- _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
- _CCCryptorCreate
- _CCCryptorRelease
- _CCCryptorReset
- _CCCryptorUpdate
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x24
- _objc_retain_x4
- _sched_yield
CStrings:
+ " auth entries"
+ " crypto = "
+ " elements returned "
+ " marked as purgeable"
+ " with "
+ "%"
+ "%.*s: Image file %{private}@ stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)"
+ "%.*s: Unlocked using public key"
+ "%.*s: Unlocked using symmetric key"
+ "%.*s: User data embedding passed"
+ "%.*s: User data retrieving passed, %d value(s) found"
+ "%.*s: Using %{private}@ as read-only"
+ "-[DIChpassParams prepareImageWithXpcHandler:fileMode:encChpass:error:]"
+ "-[DIConvertParams onConvertCompletionWithInError:outError:]"
+ "-[DIConvertParams prepareConvertWithError:]"
+ "-[DICreateParams resizeWithDiskImage:numberOfBlocks:error:]"
+ "-[DIEncryptionChpass consoleAskForPassphraseWithUseStdin:usage:error:]"
+ "-[DIEncryptionChpass unlockWithPassphrase:error:]"
+ "-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:usage:error:]"
+ "-[DIEncryptionFrontend keychainUnlockWithIsSystemKeychain:error:]"
+ "-[DIEncryptionFrontend unlockUsingPublicKeyWithError:]"
+ "-[DIEncryptionFrontend unlockUsingSymmetricKeyWithError:]"
+ "-[DIEncryptionFrontend unlockWithPassphrase:error:]"
+ "-[DIShadowChain addShadowNodes:wrapReadOnly:error:]"
+ "-[DiskImageGraph initWithBaseImageURL:tag:error:]"
+ "-[DiskImageGraph initWithPluginName:pluginParams:tag:error:]"
+ "-[NativeDiskImageGraphNode deleteImage]"
+ "-[SparseBundleBackendXPC getCryptoHeaderBackend]"
+ "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/System/Library/libtest_plugin_shared_object.dylib"
+ "/dev/tty"
+ "@\"DICreateParams\""
+ "@\"DITemporaryPassphrase\""
+ "@\"NSMutableData\""
+ "@\"NSProgress\"32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24"
+ "@24@0:8@?16"
+ "@24@0:8r*16"
+ "@32@0:8@16@?24"
+ "@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=^{header}}24"
+ "@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>=^{header}}24"
+ "@32@0:8^v16r^v24"
+ "@32@0:8r^v16^@24"
+ "@40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32"
+ "@48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40"
+ "AES-CBC"
+ "AES-XTS"
+ "ASIF meta header is unaligned"
+ "ASIF: failed to update parent UUID"
+ "Asif header size unaligned"
+ "Asif header too large"
+ "B32@0:8q16^@24"
+ "B36@0:8B16q20^@28"
+ "B40@0:8Q16^v24^@32"
+ "B40@0:8^B16^B24^@32"
+ "B40@0:8^v16Q24^@32"
+ "B40@0:8r*16Q24^@32"
+ "B40@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16^@32"
+ "B48@0:8@16@24@32^@40"
+ "B48@0:8@16Q24q32^@40"
+ "B48@0:8@16q24@32^@40"
+ "B48@0:8{unexpected<std::error_code>={error_code=i^{error_category}}}16@32^@40"
+ "Backend is not mounted on APFS"
+ "BackendZero"
+ "Block device block size is larger than image block size"
+ "BufferedWriteBackend doesn't support per io crypto"
+ "CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextMetadata &)"
+ "CLIPassphrasePromptCreate"
+ "CLIPassphrasePromptUnlock"
+ "CLIVerifyPassphrasePromptCreate"
+ "Can't parse encryption entry: "
+ "Can't read custom encryption entry header, error "
+ "Can't read encryption entry header, error "
+ "Can't read encryption table, error "
+ "Cannot change passphrase of unencrypted image"
+ "Cannot create target image format with the block size of the source image"
+ "Cannot edit crypto header that has more than "
+ "Cannot find rawTestPluginCreate in libtest_plugin_shared_object.dylib "
+ "Cannot increase size of a block device"
+ "Cannot load libTestPlugin"
+ "Cannot save DiskImageGraph without specifying pstack URL"
+ "Cannot stack images with different block sizes"
+ "Corrupted encryption table, invalid offset/length in entry's descriptor"
+ "Couldn't read asif's full header"
+ "Crypto: Unsupported encryption parameters"
+ "DIChpassParams"
+ "DIEncryptionChpass"
+ "DIImageHandle"
+ "DITemporaryPassphrase"
+ "DiskImageConvert"
+ "Encryption Method"
+ "Error creating AEA backend"
+ "Error creating crypto format"
+ "Error decrypting data using public key, error code "
+ "Failed to add passphrase entry to auth table"
+ "Failed to add public key entry to auth table"
+ "Failed to add symmetric key entry to auth table"
+ "Failed to allocate raw blob data"
+ "Failed to create chiper data for public key auth"
+ "Failed to create crypto serializer"
+ "Failed to create passphrase auth entry"
+ "Failed to create public key auth entry"
+ "Failed to encrypt data using public key from certificate"
+ "Failed to open backend of crypto header"
+ "Failed to open crypto header"
+ "Failed to read auth table"
+ "Failed to replace passphrase entry in auth table"
+ "Failed to serialize passphrase to crypto header"
+ "Failed to serialize public key entry to crypto header"
+ "Failed to serialize symmetric key to crypto header"
+ "Failed to set up image for resize after creation"
+ "Failed to update crypto header"
+ "Failed to use the passphrase that was given"
+ "File system block_size is "
+ "File: Couldn't fetch status, error: "
+ "GUIAskForPassphraseWithEncryptionFrontend:usage:error:"
+ "GUIAskForPassphraseWithEncryptionFrontend:usage:reply:"
+ "GUIAskForPassphraseWithPassphraseUsage:error:"
+ "GUIPassphraseLabelCreate"
+ "GUIPassphraseLabelUnlock"
+ "GUIPassphrasePromptCreate"
+ "GUIPassphrasePromptUnlock"
+ "GUIVerifyPassphraseLabelCreate"
+ "GraphNodeWithDictionary:workDir:error:"
+ "I32@0:8@16^@24"
+ "Ignoring truncate on block device"
+ "Invalid block size for image"
+ "Invalid encryption method"
+ "Invalid field found in shadow file header: "
+ "Invalid format for shadow file"
+ "Invalid value for UDIF header field: %s"
+ "Invalid value for argument 'block-size'"
+ "Invalid value for asif header field: %s"
+ "Key from the certificate is not exportable"
+ "Key size isn't a multiple of 8"
+ "Metadata contains unsupported field "
+ "Metadata corrupted "
+ "NativeDiskImageGraphNode"
+ "No room to add new auth entry"
+ "None"
+ "Overflow detected"
+ "Plugin's async ring cancelled, ret code "
+ "Plugin's ring resumed, ret code "
+ "Plugin's ring suspended, ret code "
+ "Q28@0:8@16I24"
+ "ReadOnlyBackend"
+ "SerializedDiskImageGraph"
+ "T*,N,V_buf"
+ "T@\"DICreateParams\",&,N,V_createParams"
+ "T@\"DITemporaryPassphrase\",R,N,V_temporaryPassphrase"
+ "T@\"DiskImageGraphNode\",R,N"
+ "T@\"FileLocalXPC\",&,N,V_fileBackend"
+ "T@\"NSData\",C,N"
+ "T@\"NSMutableArray\",&,N,V_mutableChildren"
+ "T@\"NSMutableData\",R,N,V_mutableSymmetricKey"
+ "T@\"NSMutableDictionary\",&,N,V_graphDB"
+ "T@\"NSString\",R,N,V_pluginName"
+ "T@\"NSURL\",R,N,V_filePath"
+ "T@\"NSURL\",R,N,V_pstackURL"
+ "TB"
+ "TB,N,V_singleInstanceDaemon"
+ "TB,V_encryptionInfoOnly"
+ "TI,D,N"
+ "TI,N,V_blockSize"
+ "T^v,N,V_passEntryToChange"
+ "The image is encrypted but has no passphrase auth entry"
+ "The image was unlocked before setting userData"
+ "The symmteric key is wrong"
+ "T{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v^v},R,N"
+ "URLRelativeToPstackParentWithURL:"
+ "Unaligned metadata entry size"
+ "Unexpected error creating AEA backend"
+ "Unexpected passphrase header length ("
+ "Unsupported block size for image format"
+ "Zero padding cannot be disabled from this process (res="
+ "Zero padding disabled successfully on fd "
+ "[0x%08x] %{public}s"
+ "[0x%08x](warning) %{public}s"
+ "^v24@0:8^@16"
+ "^v8@?0"
+ "_createParams"
+ "_diskImage"
+ "_encryptionInfoOnly"
+ "_graphDB"
+ "_lockableResources"
+ "_mutableChildren"
+ "_mutableSymmetricKey"
+ "_passEntryToChange"
+ "_singleInstanceDaemon"
+ "_temporaryPassphrase"
+ "addChild:withPendingUnitCount:"
+ "addPassphraseEntryWithXpcHandler:flags:usage:error:"
+ "addPublicKeyEntryWithXpcHandler:error:"
+ "addShadowNodes:wrapReadOnly:error:"
+ "addSymmetricKeyEntryWithError:"
+ "auth_table"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:186:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:190:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8)> &]"
+ "bla"
+ "changePassWithXpcHandler:error:"
+ "checkAuthEntriesWithHasPassphraseEntry:hasPublicKeyEntry:error:"
+ "chpassWithError:"
+ "com.apple.DiskImages2.ASIF.sparsity"
+ "com.apple.diskimage-test-plugin.julio"
+ "com.apple.diskimage-test-plugin.raw"
+ "com.apple.diskimages_cache_update"
+ "consoleAskForPassphraseWithUseStdin:usage:error:"
+ "convertWithCompletionBlock:"
+ "createGraphDictWithNode:"
+ "createInternalWithError:"
+ "createParams"
+ "crypt_consecutive_vector: check errors_in read futures "
+ "crypt_consecutive_vector: write check errors "
+ "crypto_format: Can't decrypt wrapped key "
+ "crypto_format: Can't derive key "
+ "crypto_format: blob length differs"
+ "crypto_format: cookie differs"
+ "crypto_op: can't initializae aes_cbc context"
+ "crypto_op: can't initializae aes_xts context"
+ "di_plugin_t *JulioTestPluginCreate(uint64_t)_block_invoke"
+ "diskimagesuio: future read invalid in read"
+ "diskimageuio: pre-write final error "
+ "diskimageuio: pre-write first error "
+ "diskimageuio: report err "
+ "encryption: header size mismatch"
+ "encryptionInfoOnly"
+ "errorWithUnexpected:verboseInfo:error:"
+ "failWithInError:outError:"
+ "failWithUnexpected:error:"
+ "failWithUnexpected:verboseInfo:error:"
+ "fileExistsAtPath:"
+ "fullDataBytes"
+ "fullDataEntry"
+ "generateAuthTableWithError:"
+ "getBlockSizeFromStr:error:"
+ "getImageUUIDWithURL:allowMissingUUID:error:"
+ "getPublicKeyWithCertificate:error:"
+ "getSerializerWithAuthTable:"
+ "graphDB"
+ "hasBitmapDataEntry"
+ "header read-only flags"
+ "hybrid_queue"
+ "i32@0:8^v16Q24"
+ "initWithBaseImageURL:newPstackURL:tag:error:"
+ "initWithBaseImageURL:pstackURL:tag:error:"
+ "initWithBaseImageURL:tag:error:"
+ "initWithData:"
+ "initWithDictionary:workDir:error:"
+ "initWithDiskImage:lockableResources:"
+ "initWithGraphDB:error:"
+ "initWithGraphDB:pstackURL:error:"
+ "initWithGraphDB:workDir:error:"
+ "initWithPassphrase:"
+ "initWithPluginName:pluginParams:pstackURL:tag:error:"
+ "initWithPluginName:pluginParams:tag:error:"
+ "int BufferedWriteBackend::reset_last_offset(const sg_entry &)"
+ "int crypto::crypt_op::crypt_consecutive_vector::operator()()"
+ "int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)"
+ "int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t, const std::optional<sg_per_io_crypto> &)"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1912:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1948:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:352:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:432:45)]"
+ "isDiskImageWithURL:"
+ "isSparseBundleWithURL:"
+ "iv_tweak_size_t"
+ "lockableResources"
+ "managed future err "
+ "mark purgeable failed on "
+ "metadata_flags_t"
+ "metadata_read_only_flags"
+ "moveDiskImage"
+ "mutableBytes"
+ "mutableChildren"
+ "mutableSymmetricKey"
+ "newAEABackendThrowsWithBackendXPC:error:"
+ "newWithCryptoFormat:error:"
+ "newWithUnlockedBackendXPC:blockSize:error:"
+ "nilWithUnexpected:error:"
+ "nilWithUnexpected:verboseInfo:error:"
+ "numChuncksDefraged"
+ "numChunksInAllocator"
+ "numChunksOfBitmap"
+ "numChunksOfData"
+ "numOfTables"
+ "onConvertCompletionWithInError:outError:"
+ "openExistingImageWithError:"
+ "passEntryToChange"
+ "passphrase_header"
+ "populateNodesDictsWithArray:workDir:nodesDict:error:"
+ "prepareConvertWithError:"
+ "prepareImageWithXpcHandler:fileMode:encChpass:error:"
+ "progressWithTotalUnitCount:"
+ "ramTestPluginCreate"
+ "replacePassWithXpcHandler:params:error:"
+ "replacePassphrase:error:"
+ "resizeWithDiskImage:numberOfBlocks:error:"
+ "rootNode"
+ "savePstackWithURL:error:"
+ "secondaryKey"
+ "sendEvent of type "
+ "setBlockSize:error:"
+ "setCompletedUnitCount:"
+ "setCreateParams:"
+ "setEncryptionInfoOnly:"
+ "setFileBackend:"
+ "setGraphDB:"
+ "setHeader:"
+ "setMutableChildren:"
+ "setPassEntryToChange:"
+ "setPassphrase:encryptionMethod:error:"
+ "setSingleInstanceDaemon:"
+ "setSymmetricKey:"
+ "singleInstanceDaemon"
+ "size_t di_asif::Metadata::read_num_blocks(di_asif::details::ContextMetadata &)"
+ "statfs failed"
+ "static int crypto::crypt_op::crypt_chunk(crypto::context::aes &, char *, size_t, uint64_t, size_t, char *)"
+ "static ssize_t crypto::crypt_op::backend_futures_prepare_and_run(const fixed_size_vector_t<sg_entry> &, Backend &, Backend::future_t (Backend::*)(const sg_entry &), fixed_size_vector_t<Backend::future_t> &)"
+ "static std::expected<passphrase, diskimage_err> crypto::auth_entry_ns::passphrase::create(const auth_table &, const char *, diskimage_uio::option_set<locked_entity> &&, serializer_t &)"
+ "static std::expected<public_key, diskimage_err> crypto::auth_entry_ns::public_key::create(const auth_table &, SecKeyRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)"
+ "static std::expected<symmetric_key, diskimage_err> crypto::auth_entry_ns::symmetric_key::create(const auth_table &, CFDataRef, diskimage_uio::option_set<locked_entity> &&, serializer_t &)"
+ "static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string_view, data_t> &)"
+ "std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::_read_auth_entry_specialized(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &, size_t, const std::function<auth_table::entry_variant (const char *)>)"
+ "std::expected<auth_table::entry_variant, diskimage_err> crypto::crypto_format_auth_table_reader::read_unknown_entry(const auth_table &, const std::vector<auth_entry_descriptor>::const_iterator &)"
+ "std::expected<descriptor_handle_t, diskimage_err> crypto::crypto_serializer_t::get_handle_for_new_entry(size_t, auth_entry_descriptor::mechanism_t)"
+ "std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_derivation_key(const char *) const"
+ "std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::passphrase::generate_wrapped_key(const char *) const"
+ "std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::public_key::generate_wrapped_key() const"
+ "std::expected<std::vector<std::byte>, diskimage_err> crypto::auth_entry_ns::symmetric_key::generate_wrapped_key(CFDataRef) const"
+ "std::expected<void, diskimage_err> crypto::validate_key_size(ssize_t)"
+ "symmetricKey"
+ "telemetryID"
+ "telemetryIndex"
+ "temporaryPassphrase"
+ "toHeaderEncryptionMode:headerEncMode:error:"
+ "uint32_t FileDescriptor::fetch_fs_block_size() const"
+ "uninitDataBytes"
+ "uninitDataEntry"
+ "unlockUsingPublicKeyWithError:"
+ "unlockUsingSaksWithError:"
+ "unlockUsingSymmetricKeyWithError:"
+ "unlockWithPassphrase:error:"
+ "unmappedDataBytes"
+ "unmappedDataEntry"
+ "user data embedding failed"
+ "user data retrieving failed"
+ "v24@0:8^v16"
+ "v24@0:8{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=^{header}}16"
+ "v40@0:8@\"DIEncryptionFrontend\"16q24@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "validateBlockSizeSupport"
+ "virtual int BufferedWriteBackend::write(const sg_entry &)"
+ "virtual int FileLocal::_read(const sg_entry &)"
+ "virtual int FileLocal::_write(const sg_entry &)"
+ "virtual int FileLocal::disable_file_zero_padding() const"
+ "virtual int Ram::_read(const sg_entry &)"
+ "virtual int Ram::_write(const sg_entry &)"
+ "virtual std::expected<std::span<std::byte>, diskimage_err> crypto::crypto_format_auth_table_reader::verify_decrypted_blob(const std::span<std::byte> &)"
+ "virtual std::expected<std::vector<auth_entry_descriptor>, diskimage_err> crypto::crypto_format_auth_table_reader::read_auth_descriptors()"
+ "virtual void crypto_format_backend::run_futures()"
+ "virtualDiskSize"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/crypto/crypto_format.cpp:712:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/crypto/crypto_format.cpp:712:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:624:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:624:24)>::__iterator<false>]"
+ "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>, std::function<void (uint64_t)>)"
+ "void di_hybrid_subscriber_t::cancel()"
+ "void di_hybrid_subscriber_t::resume()"
+ "void di_hybrid_subscriber_t::suspend()"
+ "void lw_future_managed_setter<int>::put() [T = int, empty_value = 0]"
+ "{expected<crypto::crypto_serializer_t, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<crypto::crypto_serializer_t, std::error_code>::__union_t>=(__union_t={crypto_serializer_t=^^?{interval_set<unsigned long long, std::less, boost::icl::discrete_interval<unsigned long long>, std::allocator>={set<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>={__tree<boost::icl::discrete_interval<unsigned long long>, boost::icl::exclusive_less_than<boost::icl::discrete_interval<unsigned long long>>, std::allocator<boost::icl::discrete_interval<unsigned long long>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}}^{format}{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}}{error_code=i^{error_category}})}B}}}24@0:8^v16"
+ "{expected<std::shared_ptr<Backend>, std::error_code>={__conditional_no_unique_address<true, std::__expected_base<std::shared_ptr<Backend>, std::error_code>::__repr>={__repr={__conditional_no_unique_address<false, std::__expected_base<std::shared_ptr<Backend>, std::error_code>::__union_t>=(__union_t={shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}{error_code=i^{error_category}})}B}}}16@0:8"
+ "{expected<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=(storage<std::unique_ptr<diskimage_uio::diskimage>, std::error_code>=c{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>=^{diskimage}}{error_code=i^{error_category}})B}16@0:8"
+ "{optional<crypto::auth_table>=\"\"(?=\"__null_state_\"c\"__val_\"{auth_table=\"descriptors\"{vector<crypto::auth_entry_descriptor, std::allocator<crypto::auth_entry_descriptor>>=\"__begin_\"^{auth_entry_descriptor}\"__end_\"^{auth_entry_descriptor}\"__cap_\"^{auth_entry_descriptor}}\"reader\"{shared_ptr<crypto::auth_table_reader_t>=\"__ptr_\"^{auth_table_reader_t}\"__cntrl_\"^{__shared_weak_count}}})\"__engaged_\"B}"
+ "{shared_ptr<crypto::header>=\"__ptr_\"^{header}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<crypto::passphrase_header>=\"__ptr_\"^{passphrase_header}\"__cntrl_\"^{__shared_weak_count}}"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}16@0:8"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}24@0:8B16B20"
+ "{unique_ptr<DiskImage, std::default_delete<DiskImage>>=^{DiskImage}}24@0:8^@16"
+ "{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>=^{DiskImageInfo}}28@0:8B16^@20"
+ "{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"__ptr_\"^{header}}"
+ "{unique_ptr<diskimage_uio::diskimage, std::default_delete<diskimage_uio::diskimage>>=\"__ptr_\"^{diskimage}}"
+ "{unique_ptr<udif::header, std::default_delete<udif::header>>=\"__ptr_\"^{header}}"
+ "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::shared_ptr<LockableResource>, std::allocator<std::shared_ptr<LockableResource>>>=^v^v^v}16@0:8"
- " returned "
- "#"
- "$"
- "%.*s: Found certificate in keychain"
- "%.*s: Image file stat: dev(0x%x), inode(%lld), mode(%o), uid(%d), gid(%d), size(%lld), blocks(%lld)"
- "-[DIBaseParams setPassphrase:error:]"
- "-[DIConvertParams convertWithError:]"
- "-[DICreateParams resizeWithNumBlocks:error:]"
- "-[DIEncryptionFrontend consoleAskForPassphraseWithUseStdin:error:]"
- "-[DIEncryptionUnlocker keychainUnlockWithIsSystemKeychain:error:]"
- "-[DiskImageGraph initWithPluginName:pluginParams:newPstackURL:tag:error:]"
- "-[DiskImageGraphNodeNative deleteImage]"
- "-[DiskImageParamsLocked_XPC newWithPassphrase:error:]"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "@32@0:8@16{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>={__compressed_pair<di_asif::header *, std::default_delete<di_asif::header>>=^{header}}}24"
- "@32@0:8@16{unique_ptr<udif::header, std::default_delete<udif::header>>={__compressed_pair<udif::header *, std::default_delete<udif::header>>=^{header}}}24"
- "@32@0:8r*16^@24"
- "@44@0:8@16@24B32^@36"
- "@44@0:8@16B24@28^@36"
- "@44@0:8r*16@24B32^@36"
- "@48@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16i32i36^@40"
- "A %@ cannot be specified for RAM disks"
- "A %@ was specified, but the image file doesn't seem to be encrypted"
- "ASIF header calculation overflow"
- "An error occurred while unlocking the encrypted image"
- "B24@0:8^v16"
- "B24@0:8q16"
- "B40@0:8@16^^{__SecKey}24^@32"
- "B40@0:8@16^v24^@32"
- "B40@0:8^v16^^{__SecKey}24^@32"
- "B40@0:8r*16@24^@32"
- "B44@0:8r*16@24B32^@36"
- "B52@0:8@16@24@32B40^@44"
- "CFAutoRelease<CFDictionaryRef> di_asif::Metadata::read(di_asif::details::ContextASIF &)"
- "CLIPassphrasePrompt"
- "CLIVerifyPassphrasePrompt"
- "Can't read UDIF crypto header"
- "Cannot clone a pstack with an import."
- "Cannot initialize public key header"
- "Certificate cannot be empty"
- "CommonCryptoReset @ "
- "CommonCryptoUpdate @ "
- "Couldn't find item in keychain"
- "Crypto: Can't read encryption table"
- "Currently, cache can only be added directly above plugin"
- "DICryptoHelper"
- "DiskImageGraphNodeNative"
- "Error checking for AEA file"
- "Error encrypting new image"
- "Error while creating AEA backend"
- "Error while creating public key header"
- "Error while decrypting data using keychain"
- "Failed opening "
- "Failed opening the crypto header backend"
- "Failed to encrypt data using public key from certificate."
- "Failed truncating crypto header"
- "Failed writing crypto header"
- "GUIAskForPassphraseWithEncryptionFrontend:error:"
- "GUIAskForPassphraseWithEncryptionFrontend:reply:"
- "GUIAskForPassphraseWithError:"
- "GUIPassphraseLabel"
- "GUIPassphrasePrompt"
- "GUIVerifyPassphraseLabel"
- "GraphNodeWithDictionary:updateChangesToDict:workDir:error:"
- "ImportPstack"
- "Invalid certificate out argument"
- "Invalid passphrase or key"
- "Invalid size requested for the new image"
- "Key from the certificate is not exportable."
- "Multiple imports are not allowed."
- "No passphrase or certificate was supplied."
- "Passphrase"
- "Public key"
- "Q32@0:8@16Q24"
- "Shadow file cannot be used with a "
- "Shadow/cache file mismatches the cache file attribute"
- "T@\"FileLocalXPC\",R,N,V_fileBackend"
- "T@\"NSDictionary\",&,N,V_pluginParams"
- "T@\"NSMutableArray\",&,N,V_children"
- "T@\"NSMutableDictionary\",&,N,V_pstackDB"
- "T@\"NSString\",&,N,V_pluginName"
- "T@\"NSString\",R,C,N,V_CLIPassphrasePrompt"
- "T@\"NSString\",R,C,N,V_CLIVerifyPassphrasePrompt"
- "T@\"NSString\",R,C,N,V_GUIPassphraseLabel"
- "T@\"NSString\",R,C,N,V_GUIPassphrasePrompt"
- "T@\"NSString\",R,C,N,V_GUIVerifyPassphraseLabel"
- "T@\"NSURL\",&,N,V_filePath"
- "T@\"NSURL\",C,N,V_pstackURL"
- "TB,N,V_imported"
- "TB,V_openEncryption"
- "TQ,D,N"
- "TQ,N"
- "The image has a 4KB block size, shadow and cache files are not supported"
- "Too many calls to set, the image is already unlocked"
- "UDIF encryption: password header size mismatch"
- "[0x%08x] %s"
- "[0x%08x](warning) %s"
- "_CLIPassphrasePrompt"
- "_CLIVerifyPassphrasePrompt"
- "_GUIPassphraseLabel"
- "_GUIPassphrasePrompt"
- "_GUIVerifyPassphraseLabel"
- "_blob"
- "_blob_encryption_iv"
- "_checksum"
- "_children"
- "_encryptedBlob"
- "_imported"
- "_openEncryption"
- "_pstackDB"
- "_publicKeyHash"
- "_salt"
- "addEntriesFromDictionary:"
- "auth_table_entry_mechanism"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:170:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:174:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:178:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8)> &]"
- "can't read crypto header"
- "checkBeforeSetWithIsPassphrase:error:"
- "com.apple.raw"
- "consoleAskForPassphraseWithUseStdin:error:"
- "convertWithError:"
- "createAEABackendWithBackendXPC:error:"
- "createPstackDictWithNode:"
- "createPublicKeyHeaderWithBackendXPC:publicKeyHeader:error:"
- "crypto_format: Can't decrypt wrapped key"
- "crypto_format: Can't derive key"
- "crypto_format: Can't initialize aes cryptor"
- "crypto_format: Cookie differs"
- "crypto_format: key size isn't a multiple of 8"
- "embedUserDataWithParams:reply:"
- "generateNewImageKeysWithPassphrase:privateKey:pubKeyHeader:header_backend:"
- "getAuthEntryWithBackend:authTableNumEntries:mechanism:error:"
- "getAuthValueWithBackend:authTableNumEntries:mechanism:error:"
- "getCertificateWithEncryptionCreator:outCertificate:error:"
- "getPassphraseUsingSaksWithBackendXPC:passPhrase:error:"
- "getPrivateKeyWithHeader:privateKey:error:"
- "getPublicKeyWithCertificate:key:error:"
- "i32@0:8r^v16Q24"
- "imported"
- "initWithData:pstackURL:imported:error:"
- "initWithDictionary:updateChangesToDict:workDir:error:"
- "initWithPluginName:pluginParams:newPstackURL:tag:error:"
- "initWithPstackURL:imported:error:"
- "int crypto::format::aes_context::crypt(uint32_t, const void *, void *, size_t)"
- "int crypto_format_backend::crypt_chunk(crypto::format::aes_context &, char *, size_t, uint64_t)"
- "int crypto_format_backend::read_aligned(char *, ssize_t, uint64_t)"
- "int crypto_format_backend::write_aligned(char *, ssize_t, uint64_t)"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1284:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1472:30)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1757:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1793:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:306:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:386:45)]"
- "isUDIFWithFormat:"
- "iv_size_t"
- "loadImportedNodesWithError:"
- "makeCryptoFormatWithIsNewImage:pass:certificate:error:"
- "makeNewImageEncryptedWithCertificate:error:"
- "makeNewImageEncryptedWithPassphrase:certificate:error:"
- "nested imports are not allowed."
- "newUnlockBackendXPCValidateArgsWithPassphrase:certificate:isNewImage:error:"
- "newUnlockedBackendXPCWithPassphrase:certificate:isNewImage:error:"
- "newWithCryptoFormat:"
- "newWithPassphrase:error:"
- "populateNodesDictsWithArray:pstackURL:nodesDict:isTopLevelPstack:error:"
- "prngKeys"
- "pstackDB"
- "rawBlockSize"
- "retrieveUserDataWithParams:reply:"
- "setChildren:"
- "setImported:"
- "setPluginName:"
- "setPluginParams:"
- "setPstackDB:"
- "setPstackURL:"
- "setRawBlockSize:"
- "tryCreateAEABackendWithBackendXPC:error:"
- "tryCreateUsingKeychainCertificateWithError:"
- "tryUnlockUsingKeychainCertificateWithError:"
- "tryUnlockUsingSaksWithHasSaksKey:error:"
- "v24@?0@\"DIEncryptionUnlocker\"8@\"NSError\"16"
- "v24@?0@\"DIUserDataParams\"8@\"NSError\"16"
- "v32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"DIEncryptionUnlocker\"16@?<v@?@\"DIEncryptionUnlocker\"@\"NSError\">24"
- "v32@0:8@\"DIUserDataParams\"16@?<v@?@\"DIUserDataParams\"@\"NSError\">24"
- "v32@0:8@\"DIUserDataParams\"16@?<v@?@\"NSError\">24"
- "validateWithPubKeyHeader:"
- "virtual int FileLocal::read(const sg_entry &)"
- "virtual int FileLocal::write(const sg_entry &)"
- "virtual int Ram::read(const sg_entry &)"
- "virtual int Ram::write(const sg_entry &)"
- "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)"
- "{keys={vector<std::byte, std::allocator<std::byte>>=^C^C{__compressed_pair<std::byte *, std::allocator<std::byte>>=^C}}{vector<std::byte, std::allocator<std::byte>>=^C^C{__compressed_pair<std::byte *, std::allocator<std::byte>>=^C}}{unique_ptr<crypto::header, std::default_delete<crypto::header>>={__compressed_pair<crypto::header *, std::default_delete<crypto::header>>=^{header}}}{vector<crypto::password_header, std::allocator<crypto::password_header>>=^{password_header}^{password_header}{__compressed_pair<crypto::password_header *, std::allocator<crypto::password_header>>=^{password_header}}}}612@0:8r*16^{__SecKey=}24{public_key_header={_publicKeyHash={Wrapper<unsigned int, std::integral_constant<bool, true>, be_type>=I}{Wrapper<unsigned char[32], std::integral_constant<bool, true>, print_as_buffer<unsigned char[32]>>=[32C]}}{Wrapper<crypto::public_key_header::public_key_crypto_algo, std::integral_constant<bool, false>, be_type>=I}{Wrapper<crypto::public_key_header::public_key_padding_algo, std::integral_constant<bool, false>, be_type>=I}{Wrapper<crypto::public_key_header::public_key_crypto_algo_mode, std::integral_constant<bool, false>, be_type>=I}{_encryptedBlob={Wrapper<unsigned int, std::integral_constant<bool, true>, be_type>=I}{Wrapper<unsigned char[512], std::integral_constant<bool, true>, print_as_buffer<unsigned char[512]>>=[512C]}}}32{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}596"
- "{shared_ptr<crypto::format>=^{format}^{__shared_weak_count}}44@0:8B16r*20@28^@36"
- "{unique_ptr<DiskImage, std::default_delete<DiskImage>>={__compressed_pair<DiskImage *, std::default_delete<DiskImage>>=^{DiskImage}}}16@0:8"
- "{unique_ptr<DiskImage, std::default_delete<DiskImage>>={__compressed_pair<DiskImage *, std::default_delete<DiskImage>>=^{DiskImage}}}24@0:8B16B20"
- "{unique_ptr<const info::DiskImageInfo, std::default_delete<const info::DiskImageInfo>>={__compressed_pair<const info::DiskImageInfo *, std::default_delete<const info::DiskImageInfo>>=^{DiskImageInfo}}}28@0:8B16^@20"
- "{unique_ptr<crypto::auth_table_entry, std::default_delete<crypto::auth_table_entry>>={__compressed_pair<crypto::auth_table_entry *, std::default_delete<crypto::auth_table_entry>>=^{auth_table_entry}}}48@0:8{shared_ptr<Backend>=^{Backend}^{__shared_weak_count}}16i32i36^@40"
- "{unique_ptr<crypto::header, std::default_delete<crypto::header>>=\"__ptr_\"{__compressed_pair<crypto::header *, std::default_delete<crypto::header>>=\"__value_\"^{header}}}"
- "{unique_ptr<di_asif::header, std::default_delete<di_asif::header>>=\"__ptr_\"{__compressed_pair<di_asif::header *, std::default_delete<di_asif::header>>=\"__value_\"^{header}}}"
- "{unique_ptr<udif::header, std::default_delete<udif::header>>=\"__ptr_\"{__compressed_pair<udif::header *, std::default_delete<udif::header>>=\"__value_\"^{header}}}"

```
