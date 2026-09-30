## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset`

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
-  __TEXT.__text: 0x95c78
+2215.0.16.0.0
+  __TEXT.__text: 0x95c7c
   __TEXT.__objc_methlist: 0x6d74
   __TEXT.__const: 0x2b4
   __TEXT.__cstring: 0x13a45
-  __TEXT.__oslogstring: 0xb883
+  __TEXT.__oslogstring: 0xb893
   __TEXT.__gcc_except_tab: 0x1310
   __TEXT.__unwind_info: 0x1ea8
   __TEXT.__objc_stubs: 0x0

   __DATA.__objc_ivar: 0x90c
   __DATA.__data: 0x358
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x190
+  __DATA.__bss: 0x198
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x210
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
Symbols:
+ -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:]
+ ___78-[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:]_block_invoke
+ _fcntl
+ _objc_msgSend$_readLockedSetStatusFromSharedLockFile:fileDescriptor:error:
+ _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:.readSetStatusSetupDispatchOnce
+ _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:.recordArray
- -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:]
- ___63-[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:]_block_invoke
- _objc_msgSend$_readLockedSetStatusFromSharedLockFile:error:
- _readLockedSetStatusFromSharedLockFile:error:.readSetStatusSetupDispatchOnce
- _readLockedSetStatusFromSharedLockFile:error:.recordArray
- _realpath$DARWIN_EXTSN
Functions:
~ _getPlistDictionary : 540 -> 528
~ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke : 852 -> 856
~ -[MAAutoAssetSet _shortTermOpenSharedLockFile:lockingAtomicInstance:forLockReason:verifyingLocalContentURLs:openingFilename:providingLockedSetStatus:sharedLockError:] : 2900 -> 2904
~ -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:] -> -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:fileDescriptor:error:] : 1272 -> 1280
CStrings:
+ "[ERROR] %{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
+ "[ERROR] %{public}s: Unable to extract plist object for key %{public}@ from dict"
- "%{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
- "%{public}s: Unable to extract plist object for key %{public}@ from dict"
```
