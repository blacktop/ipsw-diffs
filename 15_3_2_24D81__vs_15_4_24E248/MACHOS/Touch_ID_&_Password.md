## Touch ID & Password

> `/System/Library/ExtensionKit/Extensions/Touch ID & Password.appex/Contents/MacOS/Touch ID & Password`

```diff

-316.0.0.0.0
-  __TEXT.__text: 0x5cd10
-  __TEXT.__auth_stubs: 0x1e00
+317.0.0.0.0
+  __TEXT.__text: 0x5b838
+  __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x994
-  __TEXT.__cstring: 0x812a
+  __TEXT.__objc_methlist: 0xd90
+  __TEXT.__cstring: 0x7f47
   __TEXT.__objc_classname: 0x16e
   __TEXT.__objc_methname: 0x2c31
   __TEXT.__objc_methtype: 0x5cf
-  __TEXT.__const: 0x2d64
+  __TEXT.__const: 0x2d94
   __TEXT.__ustring: 0x6c0
   __TEXT.__gcc_except_tab: 0x134
   __TEXT.__oslogstring: 0x24c
   __TEXT.__constg_swiftt: 0xac0
-  __TEXT.__swift5_typeref: 0x38d3
+  __TEXT.__swift5_typeref: 0x38d7
   __TEXT.__swift5_reflstr: 0x6ef
   __TEXT.__swift5_fieldmd: 0x578
   __TEXT.__swift5_assocty: 0x1e0

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x58
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1440
-  __TEXT.__eh_frame: 0x838
-  __DATA_CONST.__auth_got: 0xf10
+  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__eh_frame: 0x890
+  __DATA_CONST.__auth_got: 0xee8
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__auth_ptr: 0x710
-  __DATA_CONST.__const: 0x2e00
+  __DATA_CONST.__auth_ptr: 0x780
+  __DATA_CONST.__const: 0x2e10
   __DATA_CONST.__cfstring: 0x1a60
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x2078
-  __DATA.__objc_selrefs: 0xc38
+  __DATA.__objc_const: 0x1ca0
+  __DATA.__objc_selrefs: 0xda0
   __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x830
-  __DATA.__data: 0x2338
+  __DATA.__objc_data: 0x4f8
+  __DATA.__data: 0x2340
   __DATA.__bss: 0x1159
   __DATA.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AC2809DD-3FD7-393F-A0BC-8D8477FAD926
-  Functions: 1826
+  UUID: D486749A-6D23-3A72-99DE-76E18ABC1FE0
+  Functions: 2121
   Symbols:   634
-  CStrings:  1775
+  CStrings:  1762
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "AKSGetStashStats"
+ "aks_remote_reset_all_peers"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "Can't construct Array with count < 0"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
