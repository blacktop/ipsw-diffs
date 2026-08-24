## suhelperd

> `/System/Library/CoreServices/Software Update.app/Contents/Resources/suhelperd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2412.0.5.0.0
-  __TEXT.__text: 0xb53c
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x58c
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x11ba
-  __TEXT.__oslogstring: 0x12b7
-  __TEXT.__objc_methname: 0x17db
+2412.1.1.0.0
+  __TEXT.__text: 0xb754
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x1960
+  __TEXT.__objc_methlist: 0x574
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__cstring: 0x11b4
+  __TEXT.__oslogstring: 0x13dd
+  __TEXT.__objc_methname: 0x176b
   __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methtype: 0x413
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__const: 0x858
-  __DATA_CONST.__cfstring: 0x1020
+  __TEXT.__objc_methtype: 0x3dd
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__cfstring: 0xfc0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x230
   __DATA.__objc_const: 0x5f0
-  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_selrefs: 0x6c8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x68
   __DATA.__common: 0x8
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 243
-  Symbols:   202
+  Functions: 244
+  Symbols:   213
   CStrings:  557
 
Symbols:
+ _PKSIPFullyProtected
+ _PKSIPOpenPathSafely
+ __os_assert_log
+ __os_crash
+ _csr_check
+ _fchmod
+ _fchown
+ _fcopyfile
+ _objc_terminate
+ _openat
+ _unlinkat
CStrings:
+ "%s: copying %@ to %@"
+ "%s: failed to copy source %@ to dest %@: %s (%d)"
+ "%s: failed to create destination %@: %s (%d)"
+ "%s: failed to remove existing destination %@: %s (%d)"
+ "%s: failed to safely open destination dir %@: %s (%d)"
+ "%s: failed to safely open source %@: %s (%d)"
+ "%s: failed to set attributes of destination %@: %s (%d)"
+ "%s: source %@ is not a regular file."
+ "%s: source %@ is protected, refusing."
+ "-[SUHelper(PrivateHelperMethods) _securelyCopyFileAndSetPermissionsFrom:to:inForeground:]"
+ "-[SUHelper(PrivateHelperMethods) _securelyCopyFileAndSetPermissionsFrom:to:inForeground:]_block_invoke"
+ "B48@0:8@\"NSString\"16@\"NSString\"24B32^i36B44"
+ "B48@0:8@16@24B32^i36B44"
+ "URLByDeletingLastPathComponent"
+ "_securelyCopyFileAndSetPermissionsFrom:to:inForeground:"
+ "registerProductFile:forProductKey:firmware:trustLevel:inForeground:"
+ "removeItemAtURL:error:"
- "%s: Failed to copy item to dest path: %@"
- "%s: Failed to remove existing destination"
- "%s: Invalid File Type"
- "-[SUHelper(PrivateHelperMethods) _securelyMoveFileAndSetPermissionsFrom:to:keepOriginal:inForeground:]_block_invoke"
- "@\"NSString\"52@0:8@\"NSString\"16@\"NSString\"24B32^i36B44B48"
- "@52@0:8@16@24B32^i36B44B48"
- "B36@0:8@16B24^@28"
- "B40@0:8@16@24B32B36"
- "Directory %s does not exist."
- "SUDirectoryErrorDomain"
- "Unable to create directory %s."
- "_doesDirectoryExistInThisPath:create:error:"
- "_securelyMoveFileAndSetPermissionsFrom:to:keepOriginal:"
- "_securelyMoveFileAndSetPermissionsFrom:to:keepOriginal:inForeground:"
- "copyItemAtPath:toPath:error:"
- "mainBundle"
- "registerProductFile:forProductKey:firmware:trustLevel:keepOriginal:inForeground:"
```
