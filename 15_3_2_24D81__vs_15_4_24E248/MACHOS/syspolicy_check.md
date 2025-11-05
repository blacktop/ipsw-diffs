## syspolicy_check

> `/usr/bin/syspolicy_check`

```diff

-620.81.1.0.0
-  __TEXT.__text: 0x15a3c
+620.100.82.0.0
+  __TEXT.__text: 0x15d1c
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x63c
+  __TEXT.__objc_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0xa14
-  __TEXT.__cstring: 0x3a26
-  __TEXT.__oslogstring: 0xa6e
-  __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__objc_methname: 0x15ee
-  __TEXT.__objc_classname: 0x9b
+  __TEXT.__cstring: 0x3a56
+  __TEXT.__oslogstring: 0xabe
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__objc_methname: 0x169a
+  __TEXT.__objc_classname: 0x9c
   __TEXT.__objc_methtype: 0x232
   __TEXT.__swift5_typeref: 0x20a
   __TEXT.__swift5_reflstr: 0x54

   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__unwind_info: 0x500
   __TEXT.__eh_frame: 0x258
   __DATA_CONST.__auth_got: 0x658
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__auth_ptr: 0x180
-  __DATA_CONST.__const: 0x700
-  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x3b0
-  __DATA_CONST.__objc_arrayobj: 0x120
+  __DATA_CONST.__objc_arraydata: 0x3c8
+  __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dupclass: 0x40
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x11e0
-  __DATA.__objc_selrefs: 0x618
-  __DATA.__objc_ivar: 0x108
+  __DATA.__objc_const: 0x1260
+  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x430
-  __DATA.__data: 0x318
+  __DATA.__data: 0x320
   __DATA.__common: 0x60
   __DATA.__bss: 0xfd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 49593817-EDF4-3E50-9006-0A032856B49A
-  Functions: 465
-  Symbols:   382
-  CStrings:  953
+  UUID: 1E8FBA6A-C19D-31DE-BFC1-D1E6CD9F588F
+  Functions: 493
+  Symbols:   385
+  CStrings:  969
 
Symbols:
+ _NSURLCreationDateKey
+ __kCFURLDiskImageBackingURLKey
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _os_variant_allows_internal_security_policies
- _csr_check
CStrings:
+ "Alacritty.app"
+ "Process path doesn't match Wrappedbundle symlink: %@, %@"
+ "SystemPolicy"
+ "T@\"NSDate\",R,N,V_createdTime"
+ "TB,N,V_isBadAppWrapper"
+ "TB,R,N,V_isBackingDMGNotarized"
+ "Terminal.app"
+ "WrappedBundle symlink points outside of the bundle: %@, %@"
+ "_createdTime"
+ "_isBackingDMGNotarizationChecked"
+ "_isBackingDMGNotarized"
+ "_isBadAppWrapper"
+ "checkAppWrapperWithURL:withProcessURL:"
+ "createdTime"
+ "iTerm2.app"
+ "isBackingDMGNotarized"
+ "isBadAppWrapper"
+ "setIsBadAppWrapper:"
- "App wrapper has bad symlink: %@, %@"
- "TB,R,N,V_hasBadAppWrapperSymlink"
- "_hasBadAppWrapperSymlink"
- "checkAppWrapperSymlink:"
- "hasBadAppWrapperSymlink"

```
