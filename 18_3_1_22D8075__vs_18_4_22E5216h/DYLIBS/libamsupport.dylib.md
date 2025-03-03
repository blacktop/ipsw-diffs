## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-387.0.7.0.0
-  __TEXT.__text: 0x13000
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x188
-  __TEXT.__const: 0x6560
-  __TEXT.__cstring: 0x2d8f
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x4b0
+407.100.6.0.0
+  __TEXT.__text: 0x126b0
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x6588
+  __TEXT.__cstring: 0x2a13
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0xa7d
   __TEXT.__objc_methtype: 0x4c0
   __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x4c8
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x280
+  __DATA_CONST.__objc_selrefs: 0x360
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x528
+  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__auth_ptr: 0x50
+  __AUTH_CONST.__const: 0x508
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__objc_const: 0x588
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libReverseProxyDevice.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 394
-  Symbols:   861
-  CStrings:  646
+  Functions: 490
+  Symbols:   967
+  CStrings:  615
 
Symbols:
+ _AMSupportCreateDataFromMappedFileURL
+ _AMSupportPlatformCreateDataFromMappedFileURL
+ _AMSupportPlatformOpenFileStreamWithUTF8Path
+ _CFAllocatorAllocate
+ _CFAllocatorCreate
+ _RPCopyProxyDictionaryWithOptions
+ _RPRegisterForAvailability
+ _RPRegistrationInvalidate
+ _RPRegistrationResume
+ _SecPKCS12Import
+ __os_assumes_log
+ _fcntl
+ _fileno
+ _fwrite
+ _kImg4TagStr_aop2
+ _kSecImportExportPassphrase
+ _kSecImportItemIdentity
- _AMSupportPlatformCreateBufferFromNativeFilePath
- _AMSupportPlatformCreateBufferFromUTF8FilePath
- _AMSupportPlatformMapFileIntoMemory
- _AMSupportPlatformUnmapMemory
- _AMSupportPlatformWriteBufferToNativeFilePath
- _AMSupportPlatformWriteBufferToUTF8FilePath
- __NSConcreteGlobalBlock
- _close
- _dispatch_once
- _dlclose
- _dlerror
- _dlopen
- _dlsym
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
