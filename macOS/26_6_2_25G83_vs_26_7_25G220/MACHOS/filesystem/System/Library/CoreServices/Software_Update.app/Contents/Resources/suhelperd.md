## suhelperd

> `System/Library/CoreServices/Software Update.app/Contents/Resources/suhelperd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2219.160.9.0.0
-  __TEXT.__text: 0xbb30
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x594
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__oslogstring: 0x128e
-  __TEXT.__cstring: 0x12b2
-  __TEXT.__objc_methname: 0x17cc
+2219.160.9.700.2
+  __TEXT.__text: 0xbd94
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x1960
+  __TEXT.__objc_methlist: 0x57c
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__oslogstring: 0x13b4
+  __TEXT.__cstring: 0x12ac
+  __TEXT.__objc_methname: 0x175c
   __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methtype: 0x415
-  __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__auth_got: 0x3c8
+  __TEXT.__objc_methtype: 0x3df
+  __TEXT.__unwind_info: 0x2c8
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x838
-  __DATA_CONST.__cfstring: 0x1160
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__cfstring: 0x1100
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x5f0
-  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_selrefs: 0x6c8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x68
   __DATA.__common: 0x8
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 246
-  Symbols:   204
+  Functions: 247
+  Symbols:   215
   CStrings:  570
 
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
