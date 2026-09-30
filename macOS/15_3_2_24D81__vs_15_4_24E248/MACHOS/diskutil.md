## diskutil

> `/usr/sbin/diskutil`

```diff

-934.81.1.0.0
-  __TEXT.__text: 0xe9004
-  __TEXT.__auth_stubs: 0x2530
-  __TEXT.__objc_stubs: 0x5020
-  __TEXT.__objc_methlist: 0x1030
-  __TEXT.__const: 0x5970
-  __TEXT.__objc_methname: 0x4fcd
-  __TEXT.__cstring: 0x1ffc6
+934.100.30.0.0
+  __TEXT.__text: 0xdfc68
+  __TEXT.__auth_stubs: 0x24d0
+  __TEXT.__objc_stubs: 0x5000
+  __TEXT.__objc_methlist: 0x106c
+  __TEXT.__const: 0x5570
+  __TEXT.__objc_methname: 0x4fa7
+  __TEXT.__cstring: 0x1fc36
   __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methtype: 0x5e6
   __TEXT.__ustring: 0x16
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__constg_swiftt: 0x1510
-  __TEXT.__swift5_typeref: 0x1829
-  __TEXT.__swift5_reflstr: 0x10ca
-  __TEXT.__swift5_fieldmd: 0x1958
-  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__constg_swiftt: 0x14e8
+  __TEXT.__swift5_typeref: 0x17b3
+  __TEXT.__swift5_reflstr: 0x10ba
+  __TEXT.__swift5_fieldmd: 0x1924
+  __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x398
   __TEXT.__swift5_proto: 0x5a4
-  __TEXT.__swift5_types: 0x20c
+  __TEXT.__swift5_types: 0x208
   __TEXT.__oslogstring: 0x18a
   __TEXT.__swift5_capture: 0x8a4
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__unwind_info: 0x2de8
-  __TEXT.__eh_frame: 0x38f0
-  __DATA_CONST.__auth_got: 0x12a8
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__auth_ptr: 0xf70
-  __DATA_CONST.__const: 0x6360
-  __DATA_CONST.__cfstring: 0x88c0
+  __TEXT.__swift5_mpenum: 0x70
+  __TEXT.__unwind_info: 0x2a50
+  __TEXT.__eh_frame: 0x369c
+  __DATA_CONST.__auth_got: 0x1278
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__auth_ptr: 0xfa0
+  __DATA_CONST.__const: 0x6380
+  __DATA_CONST.__cfstring: 0x88e0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1e90
-  __DATA.__objc_selrefs: 0x16d8
+  __DATA.__objc_const: 0x1e08
+  __DATA.__objc_selrefs: 0x16d0
   __DATA.__objc_ivar: 0x154
   __DATA.__objc_data: 0x6d0
-  __DATA.__data: 0x1c92
-  __DATA.__common: 0x810
+  __DATA.__data: 0x1c32
+  __DATA.__common: 0x808
   __DATA.__bss: 0xa224
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 53C2EC89-1102-3421-868E-2AF8FA152F11
-  Functions: 4044
-  Symbols:   1136
-  CStrings:  4471
+  UUID: 211132A1-B44E-3CDB-A12C-CAB4834571CD
+  Functions: 3956
+  Symbols:   1131
+  CStrings:  4452
 
Symbols:
+ _kSKDiskUnmountOptionRecursive
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _swift_unknownObjectRelease_n
CStrings:
+ " should be a path or a file URL"
+ "--force"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "Failed to find parent disk\n"
+ "Usage:  diskutil eject [force] MountPoint|DiskIdentifier|DeviceNode\n"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "Can't construct Array with count < 0"
- "GrowToEnd"
- "Insufficient space allocated to copy string contents"
- "Mount point cannot be empty"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Range.swift"
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
- "Usage:  diskutil eject MountPoint|DiskIdentifier|DeviceNode\n"
- "invalid Collection: less than 'count' elements in collection"
- "printDissenterParentWithDissenterPID:"

```
