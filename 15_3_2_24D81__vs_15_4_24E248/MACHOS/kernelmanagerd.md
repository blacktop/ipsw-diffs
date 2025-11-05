## kernelmanagerd

> `/usr/libexec/kernelmanagerd`

```diff

-463.40.2.0.0
-  __TEXT.__text: 0x15bbcc
-  __TEXT.__auth_stubs: 0x3260
+463.100.7.0.0
+  __TEXT.__text: 0x158d30
+  __TEXT.__auth_stubs: 0x3240
   __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x5fc
-  __TEXT.__swift5_typeref: 0x44e4
-  __TEXT.__swift5_capture: 0xb8c
-  __TEXT.__const: 0xf8f8
-  __TEXT.__constg_swiftt: 0x6464
-  __TEXT.__swift5_reflstr: 0x2928
-  __TEXT.__swift5_fieldmd: 0x4a98
-  __TEXT.__swift5_types: 0x66c
-  __TEXT.__cstring: 0x17601
+  __TEXT.__objc_methlist: 0x8e8
+  __TEXT.__swift5_typeref: 0x4502
+  __TEXT.__swift5_capture: 0xb7c
+  __TEXT.__const: 0xf9f8
+  __TEXT.__constg_swiftt: 0x64cc
+  __TEXT.__swift5_reflstr: 0x29a8
+  __TEXT.__swift5_fieldmd: 0x4b0c
+  __TEXT.__swift5_types: 0x674
+  __TEXT.__cstring: 0x17641
   __TEXT.__oslogstring: 0xd12
   __TEXT.__swift5_builtin: 0x280
   __TEXT.__swift5_assocty: 0x9c0
   __TEXT.__swift5_protos: 0xd4
-  __TEXT.__swift5_proto: 0xfec
-  __TEXT.__objc_methname: 0x19e7
+  __TEXT.__swift5_proto: 0x1004
+  __TEXT.__objc_methname: 0x19f4
   __TEXT.__swift5_mpenum: 0x64
   __TEXT.__objc_classname: 0x122
   __TEXT.__objc_methtype: 0x665
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x60f8
-  __TEXT.__eh_frame: 0xb6ac
-  __DATA_CONST.__auth_got: 0x1938
-  __DATA_CONST.__got: 0x800
-  __DATA_CONST.__auth_ptr: 0x900
-  __DATA_CONST.__const: 0xcb88
+  __TEXT.__unwind_info: 0x5f80
+  __TEXT.__eh_frame: 0xb174
+  __DATA_CONST.__auth_got: 0x1928
+  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__auth_ptr: 0x970
+  __DATA_CONST.__const: 0xcda8
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4f98
-  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_const: 0x4ad8
+  __DATA.__objc_selrefs: 0x7a0
   __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0xf38
-  __DATA.__data: 0x6c20
-  __DATA.__bss: 0x1c7c8
-  __DATA.__common: 0x700
+  __DATA.__objc_data: 0xed0
+  __DATA.__data: 0x6c18
+  __DATA.__bss: 0x1cab8
+  __DATA.__common: 0x6c8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D78A7B49-4874-3B81-8905-942696B4CE8C
-  Functions: 9372
-  Symbols:   1187
-  CStrings:  2517
+  UUID: 86AB1B41-3729-3CBA-BB5C-35FC0F4B0EA5
+  Functions: 9449
+  Symbols:   1185
+  CStrings:  2516
 
Symbols:
+ _$s10Foundation3URLV13DirectoryHintO13inferFromPathyA2EmFWC
+ _$s10Foundation3URLV13DirectoryHintOMa
+ _$s10Foundation3URLV14absoluteStringSSvg
+ _$s10Foundation3URLV8filePath13directoryHint10relativeToACSS_AC09DirectoryF0OACSgtcfC
+ _$s10Foundation4DataV15_RepresentationOys5UInt8VSicig
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss6ResultOMn
- _memcmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/KernelManagement_executables/core/Errors.swift"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/KernelManagement_executables/kernelmanagerd/KernelManagerDaemon.swift"
+ "Added codeless kext (force loaded) to the kernel load request: %{public}s"
+ "Bundle or the bundle id is nil: %{public}"
+ "CodelessSearchPaths"
+ "Failed to force load codeless kexts: %{public}s"
+ "ForceLoadCodelessIdentifiers"
+ "Found codeless bundles matching the ids listed in codeless exceptions: %{public}s"
+ "Found multiple codeless kexts with the same identifiers, will use the known one: \n\tknown path: %{public}s \n\tduplicated path: %{public}s"
+ "KernelManagement_executables-463.100.7"
+ "No codeless bundle needs to be force loaded."
+ "Skip the codeless kext that is not in the force load list: %{public}s"
+ "Successfully inserted extension: %{public}s"
+ "The codeless exceptions configuration is not provided, skip codeless forceloading"
+ "Unable to insert extension: %{public}s"
+ "Validating extension at %{private}s"
+ "codelessForceLoadLists"
+ "initWithURL:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/KernelManagement_executables/core/Errors.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/KernelManagement_executables/kernelmanagerd/KernelManagerDaemon.swift"
- "Insufficient space allocated to copy string contents"
- "KernelManagement_executables-463.40.2"
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
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "Validating extension at %{public}s"
- "invalid Collection: less than 'count' elements in collection"

```
