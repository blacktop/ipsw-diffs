## deferred_install

> `/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/deferred_install`

```diff

-1470.81.1.0.0
-  __TEXT.__text: 0x61dc
-  __TEXT.__auth_stubs: 0x5a0
+1474.100.4.0.0
+  __TEXT.__text: 0x6500
+  __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x154
+  __TEXT.__objc_methlist: 0x190
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x81d
+  __TEXT.__objc_methname: 0x812
   __TEXT.__objc_classname: 0x4b
   __TEXT.__objc_methtype: 0xe7
-  __TEXT.__cstring: 0x189d
-  __TEXT.__gcc_except_tab: 0x320
+  __TEXT.__cstring: 0x19f0
+  __TEXT.__gcc_except_tab: 0x36c
   __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x1000
+  __DATA_CONST.__cfstring: 0x10a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x228
+  __DATA_CONST.__objc_intobj: 0x270
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x448
+  __DATA.__objc_const: 0x3f0
   __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 932916C2-5CFB-3E66-BDBA-9722B8B9AF03
+  UUID: 3D862512-8A06-321F-81CA-A2E04EE273A1
   Functions: 52
-  Symbols:   122
-  CStrings:  403
+  Symbols:   125
+  CStrings:  413
 
Symbols:
+ _copyfile
+ _pthread_fchdir_np
+ _removefileat
Functions:
~ sub_1000033b8 -> sub_100001ae4 : 1236 -> 1240
~ sub_10000388c -> sub_100001fbc : 6808 -> 7004
~ sub_10000577c -> sub_100003f70 : 1272 -> 1268
~ sub_100005c74 -> sub_100004464 : 3000 -> 3684
~ sub_10000682c -> sub_1000052c8 : 884 -> 868
~ sub_100006e38 -> sub_1000058c4 : 1928 -> 1924
~ sub_1000075c0 -> sub_100006048 : 908 -> 904
~ sub_100007d48 -> sub_1000067cc : 692 -> 648
~ sub_100008074 -> sub_100006acc : 304 -> 296
CStrings:
+ "Error relinking file (copy item): %@ to %@, errno = %d\nsrcPath = %@\ndstParentPath = %@"
+ "Error relinking file (remove dst item): %@ to %@, errno = %d\ndstPath = %@"
+ "Error relinking file (remove dst link): %@ to %@, errno = %d\ndstPath = %@"
+ "Error relinking file (unable to set per-thread cwd to parent dir): %@ to %@, errno = %d\nsrcPath = %@\ndstParentPath = %@"
+ "PKCoreShoveErrorDestinationNotAccessible"
+ "PKCoreShoveErrorDestinationParentNotAccessible"
+ "Unable to restore overriden per-thread working directory. %s"
+ "Warning relinking item (remove item): %@ , NSError = \"%@\""
+ "lastPathComponent"
- "Error relinking file (copy item): %@ to %@, NSError = \"%@\"\nsrcPath = %@\ndstParentPath = %@"
- "Error relinking file (remove item): %@ to %@, NSError = \"%@\"\ndstPath = %@"
- "Warning relinking file (remove item): %@ , NSError = \"%@\""
- "copyItemAtPath:toPath:error:"

```
