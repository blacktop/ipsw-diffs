## PackageKit

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit`

```diff

-1470.81.1.0.0
-  __TEXT.__text: 0x85cc0
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_methlist: 0x725c
-  __TEXT.__cstring: 0x1149d
-  __TEXT.__const: 0x328
+1474.100.4.0.0
+  __TEXT.__text: 0x85f68
+  __TEXT.__auth_stubs: 0x2000
+  __TEXT.__objc_methlist: 0x77dc
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x115ec
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_typeref: 0x7c
   __TEXT.__swift5_reflstr: 0x21
   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x1320
+  __TEXT.__gcc_except_tab: 0x1364
   __TEXT.__oslogstring: 0x19
   __TEXT.__dof_PackageKi: 0x1ba4
-  __TEXT.__unwind_info: 0x2078
+  __TEXT.__unwind_info: 0x2050
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x1091
   __TEXT.__objc_methname: 0x11c0a
   __TEXT.__objc_methtype: 0x2538
   __TEXT.__objc_stubs: 0xdea0
-  __DATA_CONST.__got: 0x9a0
-  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0xc68
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4428
+  __DATA_CONST.__objc_selrefs: 0x4520
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x1008
+  __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__const: 0x17a0
-  __AUTH_CONST.__cfstring: 0xb680
-  __AUTH_CONST.__objc_const: 0xc4f0
-  __AUTH_CONST.__objc_intobj: 0x408
+  __AUTH_CONST.__cfstring: 0xb720
+  __AUTH_CONST.__objc_const: 0xbb48
+  __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x2af0
   __AUTH.__data: 0x28

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 53003609-1F13-379E-BCCB-7CDD2EA59A64
-  Functions: 2801
-  Symbols:   7489
-  CStrings:  6952
+  UUID: 2A782D77-918D-3597-B1D5-510AE8E51C32
+  Functions: 2796
+  Symbols:   7492
+  CStrings:  6960
 
Symbols:
+ _PKCoreShoveErrorDestinationNotAccessible
+ _PKCoreShoveErrorDestinationParentNotAccessible
+ _pthread_fchdir_np
CStrings:
+ "Error relinking file (copy item): %@ to %@, errno = %d\nsrcPath = %@\ndstParentPath = %@"
+ "Error relinking file (remove dst item): %@ to %@, errno = %d\ndstPath = %@"
+ "Error relinking file (remove dst link): %@ to %@, errno = %d\ndstPath = %@"
+ "Error relinking file (unable to set per-thread cwd to parent dir): %@ to %@, errno = %d\nsrcPath = %@\ndstParentPath = %@"
+ "PKCoreShoveErrorDestinationNotAccessible"
+ "PKCoreShoveErrorDestinationParentNotAccessible"
+ "Unable to restore overriden per-thread working directory. %s"
+ "Warning relinking item (remove item): %@ , NSError = \"%@\""
- "Error relinking file (copy item): %@ to %@, NSError = \"%@\"\nsrcPath = %@\ndstParentPath = %@"
- "Error relinking file (remove item): %@ to %@, NSError = \"%@\"\ndstPath = %@"
- "Warning relinking file (remove item): %@ , NSError = \"%@\""
- "f"

```
