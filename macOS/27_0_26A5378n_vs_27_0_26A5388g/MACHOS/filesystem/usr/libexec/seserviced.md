## seserviced

> `/usr/libexec/seserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-70.35.1.0.0
-  __TEXT.__text: 0xe4ba0
+70.37.0.0.0
+  __TEXT.__text: 0xe51f4
   __TEXT.__auth_stubs: 0x29c0
-  __TEXT.__objc_stubs: 0x3f00
-  __TEXT.__objc_methlist: 0x1d3c
-  __TEXT.__const: 0x9858
-  __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__objc_methname: 0x5811
-  __TEXT.__oslogstring: 0x46e2
-  __TEXT.__cstring: 0x889b
+  __TEXT.__objc_stubs: 0x3f40
+  __TEXT.__objc_methlist: 0x1d4c
+  __TEXT.__const: 0x9868
+  __TEXT.__gcc_except_tab: 0x624
+  __TEXT.__objc_methname: 0x5851
+  __TEXT.__oslogstring: 0x4772
+  __TEXT.__cstring: 0x891b
   __TEXT.__objc_classname: 0x8e8
   __TEXT.__objc_methtype: 0x1fd9
   __TEXT.__constg_swiftt: 0x1948

   __TEXT.__swift_as_ret: 0x1a0
   __TEXT.__swift_as_cont: 0x3a8
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2c00
+  __TEXT.__unwind_info: 0x2c18
   __TEXT.__eh_frame: 0x59d4
-  __DATA_CONST.__const: 0x6cc8
-  __DATA_CONST.__cfstring: 0x29a0
+  __DATA_CONST.__const: 0x6d70
+  __DATA_CONST.__cfstring: 0x2a20
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA_CONST.__auth_got: 0x14f0
   __DATA_CONST.__got: 0x9d8
   __DATA_CONST.__auth_ptr: 0x638
-  __DATA.__objc_const: 0x5660
-  __DATA.__objc_selrefs: 0x1400
+  __DATA.__objc_const: 0x5668
+  __DATA.__objc_selrefs: 0x1410
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0x1ad8
   __DATA.__data: 0x337a

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3459
-  Symbols:   1151
-  CStrings:  2401
+  Functions: 3461
+  Symbols:   1154
+  CStrings:  2411
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "Failed pairing check 1 %d"
+ "Failed to deleteAllApplets"
+ "Pairing not validated %d / %@"
+ "Pairing state (after) %{public}x / %{public}@"
+ "Pairing state (before) %{public}x / %{public}@"
+ "Q28@0:8B16^@20"
+ "Validate pairing re-paired with result %{public}d / %{public}@"
+ "deleteAllApplets:error:"
+ "macOS (27.0) - SecureElementService-70.37"
+ "v20@?0B8@\"NSError\"12"
+ "validatePairing"
+ "validatePairing:callback:"
+ "validatePairing:error:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "Q24@0:8^@16"
- "macOS (27.0) - SecureElementService-70.35.1"
- "validatePairing:"
```
