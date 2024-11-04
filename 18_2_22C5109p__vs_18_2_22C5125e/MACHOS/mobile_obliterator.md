## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-320.60.2.0.0
-  __TEXT.__text: 0x15284
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_stubs: 0x580
+320.60.4.0.0
+  __TEXT.__text: 0x15ad8
+  __TEXT.__auth_stubs: 0x1400
+  __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x8e34
+  __TEXT.__cstring: 0x900a
   __TEXT.__const: 0x688
-  __TEXT.__objc_methname: 0x3ff
+  __TEXT.__objc_methname: 0x478
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0xa08
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_selrefs: 0x198
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x920

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
+  - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   Functions: 222
-  Symbols:   369
-  CStrings:  1100
+  Symbols:   371
+  CStrings:  1112
 
Symbols:
+ _OBJC_CLASS_$_MSUDataAccessor
+ _objc_release_x22
CStrings:
+ "%!@(MISSING) /%!@(MISSING)/"
+ "%!s(MISSING): Cleaning Hardware volume"
+ "%!s(MISSING): Warning: Failed to determine HW volume for MSU DA"
+ "%!s(MISSING): safeObliterate: Cleaning Hardware volume in ephemeral mode"
+ "Failed to parse path '%!@(MISSING)'"
+ "Mismatched rules from MSU DA: new: '%!@(MISSING)' (going to be ignored), current exceptions list for path: '%!@(MISSING)'"
+ "Path not part of HW volume: '%!@(MISSING)'"
+ "Warning: A rule for 'MobileActivation' based on 'copyPersistentDataPaths' already exists: '%!@(MISSING)'"
+ "Warning: A rule for 'dcrt' based on 'copyPersistentDataPaths' already exists: '%!@(MISSING)'"
+ "Warning: A rule for 'sdcrt' based on 'copyPersistentDataPaths' already exists: '%!@(MISSING)'"
+ "Warning: Failed to get default persistent data paths: error %!@(MISSING)"
+ "characterAtIndex:"
+ "copyMountPointForVolumeType:error:"
+ "copyPersistentDataPathsWithError:"
+ "dcrt"
+ "fixup_hardware_volume"
+ "lastOTA"
+ "last_update_result.plist"
+ "pathComponents"
+ "removeExcept /%!@(MISSING)/"
+ "removeExcept /dcrt/ /sdcrt/"
+ "removeExcept /ota_tolerated_failures.plist/"
+ "sdcrt"
+ "sharedDataAccessor"
- "%!s(MISSING): Clearing activation files"
- "%!s(MISSING): Failed to remove 'dcrt' dir"
- "%!s(MISSING): Failed to remove 'mfi' dir"
- "%!s(MISSING): Failed to remove 'su' dir"
- "%!s(MISSING): Successfully removed 'dcrt' dir"
- "%!s(MISSING): Successfully removed 'mfi' dir"
- "%!s(MISSING): Successfully removed 'su' dir"
- "%!s(MISSING): safeObliterate: Clearing activation files"
- "/dcrt"
- "/factory/mfi"
- "/factory/su"
- "clearActivationFiles"

```
