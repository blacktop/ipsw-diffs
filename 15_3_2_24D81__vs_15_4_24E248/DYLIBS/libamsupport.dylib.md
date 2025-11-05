## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-387.0.7.0.0
-  __TEXT.__text: 0x13030
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x188
-  __TEXT.__const: 0x6560
-  __TEXT.__cstring: 0x2d8f
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x4c8
+407.100.7.0.0
+  __TEXT.__text: 0x126c4
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x6588
+  __TEXT.__cstring: 0x2a13
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__unwind_info: 0x500
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0xa7d
   __TEXT.__objc_methtype: 0x4c0
   __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x428
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x408
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x290
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH_CONST.__const: 0x5e8
+  __DATA_CONST.__objc_selrefs: 0x360
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__const: 0x5c8
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__objc_const: 0x588
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x8
   __DATA.__objc_classrefs: 0x80
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /usr/lib/libReverseProxyDevice.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E644B88-575F-37B9-91D6-43F2793B7D52
-  Functions: 402
-  Symbols:   1093
-  CStrings:  767
+  UUID: 3BFD7DD9-1B96-3B89-A5BE-7A1DF2A0C0AA
+  Functions: 497
+  Symbols:   1188
+  CStrings:  736
 
Symbols:
+ AMSupportBase64Decode.cold.1
+ AMSupportBase64Decode.cold.2
+ AMSupportBase64Encode.cold.1
+ AMSupportBase64Encode.cold.2
+ AMSupportCommonCopyHexStringFromData.cold.1
+ AMSupportCommonCopyHexStringFromData.cold.2
+ AMSupportCommonCopyHexStringFromData.cold.3
+ AMSupportCommonCopyHexStringFromData.cold.4
+ AMSupportCommonCopyHexStringFromData.cold.5
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.1
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.2
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.3
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.4
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.5
+ AMSupportCopyBytesFromAsciiEncodedHex.cold.6
+ AMSupportCopyHexStringFromData.cold.1
+ AMSupportCopyHexStringFromData.cold.2
+ AMSupportCopyHexStringFromData.cold.3
+ AMSupportCopyHexStringFromData.cold.4
+ AMSupportCopyHexStringFromData.cold.5
+ AMSupportCopyHexStringFromData.cold.6
+ AMSupportCopyHexStringFromUInt32.cold.1
+ AMSupportCopyHexStringFromUInt32.cold.2
+ AMSupportCopyHexStringFromUInt64.cold.1
+ AMSupportCopyHexStringFromUInt64.cold.2
+ AMSupportCreateCStringFromCFString.cold.1
+ AMSupportCreateCStringFromCFString.cold.2
+ AMSupportCreateCStringFromCFString.cold.3
+ AMSupportCreateCStringFromCFString.cold.4
+ AMSupportCreateCStringFromCFString.cold.5
+ AMSupportCreateRandomNumber.cold.1
+ AMSupportCreateSetFromCFIndexArray.cold.1
+ AMSupportGetValueForKeyPathInDict.cold.1
+ AMSupportGetValueForKeyPathInDict.cold.2
+ AMSupportGetValueForKeyPathInDict.cold.3
+ AMSupportGetValueForKeyPathInDict.cold.4
+ AMSupportHttpCopyProxySettings.cold.1
+ AMSupportHttpCopyProxySettings.cold.2
+ AMSupportHttpMessageSendSyncWithOptions.cold.1
+ AMSupportHttpMessageSendSyncWithOptions.cold.2
+ AMSupportHttpURLSessionSendSync.cold.1
+ AMSupportHttpURLSessionSendSync.cold.2
+ AMSupportHttpURLSessionSendSync.cold.3
+ AMSupportHttpUriEscapeString.cold.1
+ AMSupportHttpUriEscapeString.cold.2
+ AMSupportHttpUriEscapeString.cold.3
+ AMSupportHttpUriUnescapeString.cold.1
+ AMSupportHttpUriUnescapeString.cold.2
+ AMSupportHttpUriUnescapeString.cold.3
+ AMSupportRsaCreateDataFromPem.cold.1
+ AMSupportRsaCreateDataFromPem.cold.2
+ AMSupportRsaCreateDataFromPem.cold.3
+ AMSupportRsaCreateDataFromPem.cold.4
+ AMSupportRsaCreateDataFromPem.cold.5
+ AMSupportRsaCreatePemFromData.cold.1
+ AMSupportRsaCreatePemFromData.cold.10
+ AMSupportRsaCreatePemFromData.cold.11
+ AMSupportRsaCreatePemFromData.cold.12
+ AMSupportRsaCreatePemFromData.cold.13
+ AMSupportRsaCreatePemFromData.cold.2
+ AMSupportRsaCreatePemFromData.cold.3
+ AMSupportRsaCreatePemFromData.cold.4
+ AMSupportRsaCreatePemFromData.cold.5
+ AMSupportRsaCreatePemFromData.cold.6
+ AMSupportRsaCreatePemFromData.cold.7
+ AMSupportRsaCreatePemFromData.cold.8
+ AMSupportRsaCreatePemFromData.cold.9
+ AMSupportX509ChainEvaluateTrust.cold.1
+ AMSupportX509ChainEvaluateTrust.cold.2
+ AMSupportX509ChainEvaluateTrust.cold.3
+ _AMSupportCreateDataFromMappedFileURL
+ _AMSupportCreatePropertyListFromFileURL
+ _AMSupportPlatformCreateDataFromMappedFileURL
+ _AMSupportPlatformOpenFileStreamWithUTF8Path
+ _CFAllocatorAllocate
+ _CFAllocatorCreate
+ _MappedFileDeallocate.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _RPCopyProxyDictionaryWithOptions
+ _RPRegisterForAvailability
+ _RPRegistrationInvalidate
+ _RPRegistrationResume
+ _SecCertificateCopyAMSupportCert.cold.1
+ _SecCertificateCopyAMSupportCert.cold.2
+ _SecCertificateCopyAMSupportCert.cold.3
+ _SecCertificateCopyAMSupportCert.cold.4
+ _SecPKCS12Import
+ __AMSupportCreateDataFromFileURLInternal
+ __AMSupportPlatformWriteDataToFileURLInternal
+ __AMSupportX509DecodeRsaVerifySignatureDataWithOid
+ __Img4DecodePayloadPropertyExistsWithValue
+ __MappedFileDeallocate
+ __os_assumes_log
+ _fcntl
+ _fileno
+ _fwrite
+ _kImg4TagStr_aop2
+ _kSecImportExportPassphrase
+ _kSecImportItemIdentity
+ _rsa_oid
- AMSupportHttpCopyProxySettings.dl_RPCopyProxyDictionaryWithOptions
- AMSupportHttpCopyProxySettings.dl_RPRegisterForAvailability
- AMSupportHttpCopyProxySettings.dl_RPRegistrationInvalidate
- AMSupportHttpCopyProxySettings.dl_RPRegistrationResume
- AMSupportHttpCopyProxySettings.onceToken
- AMSupportPlatformMapFileIntoMemory.cold.1
- AMSupportPlatformMapFileIntoMemory.cold.2
- AMSupportPlatformMapFileIntoMemory.cold.3
- _AMSupportPlatformCreateBufferFromNativeFilePath
- _AMSupportPlatformCreateBufferFromUTF8FilePath
- _AMSupportPlatformMapFileIntoMemory
- _AMSupportPlatformUnmapMemory
- _AMSupportPlatformWriteBufferToNativeFilePath
- _AMSupportPlatformWriteBufferToUTF8FilePath
- _Img4DecodePayloadProperty
- __NSConcreteGlobalBlock
- ___AMSupportHttpCopyProxySettings_block_invoke_2
- ___block_literal_global
- __block_descriptor_tmp.55
- _close
- _dispatch_once
- _dlclose
- _dlerror
- _dlhandle_SecPKCS12Import
- _dlhandle_kSecImportExportPassphrase
- _dlhandle_kSecImportItemIdentity
- _dlopen
- _dlsym
- _libSecurity
- _open
- _read
- _strncmp
- _write
CStrings:
+ "AMSupportCreatePropertyListFromFileURL"
+ "AMSupportHttpCopyProxySettings_block_invoke"
+ "_AMSupportCreateDataFromFileURLInternal"
+ "wb"
- ".."
- "/usr/lib/libReverseProxyDevice.dylib"
- "AMSupportCreateArrayFromFileURL"
- "AMSupportCreateDataFromFileURL"
- "AMSupportCreateDictionaryFromFileURL"
- "AMSupportHttpCopyProxySettings_block_invoke_2"
- "AMSupportPlatformCreateBufferFromNativeFilePath"
- "AMSupportPlatformMapFileIntoMemory"
- "AMSupportPlatformUnmapMemory"
- "AMSupportPlatformWriteBufferToNativeFilePath"
- "RPCopyProxyDictionaryWithOptions"
- "RPRegisterForAvailability"
- "RPRegistrationInvalidate"
- "RPRegistrationResume"
- "SecPKCS12Import"
- "Security Framework does not have expected symbols, aborting. %s"
- "Security framework (10.6?) unsupported in libamsupport."
- "Security.framework/Versions/Current/Security"
- "failed to load %s: %s\n"
- "failed to map file into memory: %s"
- "failed to open file for reading: %s"
- "failed to open file for writing: %s"
- "failed to stat file: %s"
- "fileURL != NULL"
- "fstat failed: %s"
- "kSecImportExportPassphrase"
- "kSecImportItemIdentity"
- "libAMSupportLoadLibrary"
- "malloc(%d) failed: %s"
- "munmap() returned error: %s"
- "open failed: %s"
- "outLength != NULL"
- "outMapping != NULL"
- "path: %s"
- "read failed: %s"

```
