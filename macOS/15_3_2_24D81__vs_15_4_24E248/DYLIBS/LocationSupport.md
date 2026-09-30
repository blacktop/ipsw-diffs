## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/Versions/A/LocationSupport`

```diff

-2956.0.6.0.0
-  __TEXT.__text: 0x24a40
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x1468
-  __TEXT.__const: 0x26d
-  __TEXT.__cstring: 0x1c18
-  __TEXT.__gcc_except_tab: 0x1678
-  __TEXT.__oslogstring: 0x5d8d
-  __TEXT.__unwind_info: 0xc38
+2960.0.57.0.0
+  __TEXT.__text: 0x26364
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x1764
+  __TEXT.__const: 0x28d
+  __TEXT.__cstring: 0x1e47
+  __TEXT.__gcc_except_tab: 0x167c
+  __TEXT.__oslogstring: 0x633a
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_classname: 0x412
-  __TEXT.__objc_methname: 0x291e
+  __TEXT.__objc_methname: 0x2a21
   __TEXT.__objc_methtype: 0x858
-  __TEXT.__objc_stubs: 0x2420
-  __DATA_CONST.__got: 0x2c8
+  __TEXT.__objc_stubs: 0x2560
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc00
+  __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0xde8
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x3060
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0xe08
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x2b10
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x8
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x2004
   __DATA.__objc_ivar: 0x150
-  __DATA.__data: 0x528
-  __DATA.__bss: 0x1e0
+  __DATA.__data: 0x538
+  __DATA.__bss: 0x228
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA37A98C-F5B0-322A-AF86-F612E6637D05
-  Functions: 753
-  Symbols:   446
-  CStrings:  1204
+  UUID: 9E2A3BCD-6FE5-364A-A32C-7E686FC8441C
+  Functions: 763
+  Symbols:   465
+  CStrings:  1250
 
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
- _strcmp
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
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Logging/CLLoggingImpl.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"
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
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnection.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionClient.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/IPC/CLConnectionServer.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLDispatchSilo.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloInterface.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloProxy.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLIntersiloService.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLRunLoopSilo.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLServiceVendor.mm"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLSilo.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLTimer.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Utilities/CLAutoCohortUtilities.mm"
- "R@"

```
