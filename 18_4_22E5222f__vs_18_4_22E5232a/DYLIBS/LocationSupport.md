## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`

```diff

-2960.0.55.2.0
-  __TEXT.__text: 0x22d78
-  __TEXT.__auth_stubs: 0xe80
+2960.0.58.0.0
+  __TEXT.__text: 0x24544
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_methlist: 0x1764
-  __TEXT.__const: 0x265
-  __TEXT.__cstring: 0x1936
+  __TEXT.__const: 0x285
+  __TEXT.__cstring: 0x1b25
   __TEXT.__gcc_except_tab: 0x1660
-  __TEXT.__oslogstring: 0x5b35
-  __TEXT.__unwind_info: 0xc18
+  __TEXT.__oslogstring: 0x60e2
+  __TEXT.__unwind_info: 0xc30
   __TEXT.__objc_classname: 0x412
-  __TEXT.__objc_methname: 0x284d
+  __TEXT.__objc_methname: 0x2950
   __TEXT.__objc_methtype: 0x858
-  __TEXT.__objc_stubs: 0x2380
-  __DATA_CONST.__got: 0x298
+  __TEXT.__objc_stubs: 0x24c0
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x570
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xcb0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x930
-  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__const: 0x950
+  __AUTH_CONST.__cfstring: 0x580
   __AUTH_CONST.__objc_const: 0x2b10
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x8
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x2004
   __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x500
-  __DATA.__bss: 0x28
+  __DATA.__data: 0x510
+  __DATA.__bss: 0x30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_ivar: 0x34
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 720
-  Symbols:   464
-  CStrings:  1166
+  Functions: 729
+  Symbols:   484
+  CStrings:  1210
 
Symbols:
+ _CLLogEncryptData
+ _CLLogEncryptDataSize
+ _CLLogEncryptionClearObsoleteKeys
+ _CLLogEncryptionInit
+ _CLLogEncryptionSetDisabled
+ _NSFileProtectionKey
+ _NSFileProtectionNone
+ __tlv_bootstrap
+ _arc4random_uniform
+ _bzero
+ _ccaes_ecb_encrypt_mode
+ _ccecb_block_size
+ _ccecb_one_shot_explicit
+ _localtime
+ _localtime_r
+ _memcpy
+ _mktime
+ _sched_yield
+ _snprintf
+ _time
CStrings:
+ "#LogEncryption Can't determine the year day from the directory name: %{public}@"
+ "#LogEncryption Can't determine the year from the directory name: %{public}@"
+ "#LogEncryption Can't list contents of %@: %@"
+ "#LogEncryption Can't open keyStorePath %@: %@"
+ "#LogEncryption Can't read the key data at path '%@': %@"
+ "#LogEncryption Can't remove obsolete or unrecognized key file: %{public}@ (%{public}@)"
+ "#LogEncryption Found a valid key in %@"
+ "#LogEncryption Key directory '%@' is empty"
+ "#LogEncryption New log encryption key created: %@"
+ "#LogEncryption Not initialized."
+ "#LogEncryption Oversized data"
+ "#LogEncryption mktime() returned error for %{public}@"
+ "/%04d_%03d"
+ "/%@"
+ "/%s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Logging/CLLoggingImpl.mm"
+ "000"
+ "CLLogEncryptData"
+ "CLLogEncryptionBlockSize > 0"
+ "CLLogEncryptionInit() must be called only once"
+ "CLLogEncryptionInit_block_invoke"
+ "CLLogKeyStorePath == nullptr && __c11_atomic_compare_exchange_strong(&CLLogAtomicKeyUpdateInProgress, &expected, true, 5, 5) && __c11_atomic_load(&CLLogAtomicKeyExpirationTime, 5) == 0"
+ "Encryption error"
+ "Internal"
+ "caseInsensitiveCompare:"
+ "createFileAtPath:contents:attributes:"
+ "dataWithContentsOfFile:options:error:"
+ "done == true"
+ "fileExistsAtPath:"
+ "isEqualToString:"
+ "lastObject"
+ "logkey_%04d_%03d_%02d"
+ "numBlocksUsed < availableSize / CLLogEncryptionBlockSize"
+ "removeItemAtPath:error:"
+ "sortedArrayUsingSelector:"
+ "stringByAppendingFormat:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "toggleKeyIndex"
+ "toggleKeyIndex must always be called by a single thread."
+ "{\"msg%{public}.0s\":\"#LogEncryption Not initialized.\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#LogEncryption Oversized data\", \"encryptionSize\":%{public}lu, \"availableSize\":%{public}lu, \"blockSize\":%{public}lu, \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"CLLogEncryptionInit() must be called only once\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"toggleKeyIndex must always be called by a single thread.\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"

```
