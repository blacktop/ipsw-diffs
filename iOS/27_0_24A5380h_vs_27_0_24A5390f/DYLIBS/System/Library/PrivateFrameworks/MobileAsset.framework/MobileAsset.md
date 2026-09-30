## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2215.0.13.0.0
-  __TEXT.__text: 0x8c4f8
+2215.0.16.0.0
+  __TEXT.__text: 0x8c500
   __TEXT.__objc_methlist: 0x6d74
   __TEXT.__const: 0x2c4
   __TEXT.__cstring: 0x13ae2
-  __TEXT.__oslogstring: 0xb965
+  __TEXT.__oslogstring: 0xb975
   __TEXT.__gcc_except_tab: 0x1338
   __TEXT.__unwind_info: 0x1f20
   __TEXT.__objc_stubs: 0x0

   __DATA.__objc_ivar: 0x90c
   __DATA.__data: 0x358
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
Symbols:
+ -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:]
+ ___78-[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:]_block_invoke
+ __readLockedSetStatusFromSharedLockFile:fileDescriptor:error:.readSetStatusSetupDispatchOnce
+ __readLockedSetStatusFromSharedLockFile:fileDescriptor:error:.recordArray
+ _fcntl
+ _objc_msgSend$_readLockedSetStatusFromSharedLockFile:fileDescriptor:error:
- -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:]
- ___63-[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:]_block_invoke
- __readLockedSetStatusFromSharedLockFile:error:.readSetStatusSetupDispatchOnce
- __readLockedSetStatusFromSharedLockFile:error:.recordArray
- _objc_msgSend$_readLockedSetStatusFromSharedLockFile:error:
- _realpath$DARWIN_EXTSN
CStrings:
+ "[ERROR] %{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
+ "[ERROR] %{public}s: Unable to extract plist object for key %{public}@ from dict"
- "%{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
- "%{public}s: Unable to extract plist object for key %{public}@ from dict"
```
