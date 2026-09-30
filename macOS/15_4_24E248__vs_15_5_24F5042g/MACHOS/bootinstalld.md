## bootinstalld

> `/usr/libexec/bootinstalld`

```diff

-657.0.0.0.0
-  __TEXT.__text: 0x4a08
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_stubs: 0xe80
+658.0.0.0.0
+  __TEXT.__text: 0x4f2c
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x33c
-  __TEXT.__cstring: 0x956
-  __TEXT.__objc_methname: 0xe20
+  __TEXT.__cstring: 0x9fa
+  __TEXT.__objc_methname: 0xeea
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methtype: 0x310
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__gcc_except_tab: 0x260
   __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x538
-  __DATA.__objc_selrefs: 0x4b8
+  __DATA.__objc_selrefs: 0x500
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities
+  - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
   - /System/Library/PrivateFrameworks/Install.framework/Frameworks/DistributionKit.framework/Versions/A/DistributionKit
   - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /usr/lib/libIASAuthReboot.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 67
-  Symbols:   92
-  CStrings:  276
+  Symbols:   94
+  CStrings:  288
 
Symbols:
+ _OBJC_CLASS_$_NSMapTable
+ _removefile
CStrings:
+ "Failed to recursively cleanup jump-start path (%s) after install. %s"
+ "Unable to cleanup package after install (%s): %s"
+ "Unable to cleanup package on dequeue (%s): %s"
+ "_installItemsToRequestsForItems:onVolume:removing:error:"
+ "cleanupPackageOnDequeue"
+ "isJumpStartItem"
+ "keyEnumerator"
+ "objectEnumerator"
+ "objectForKey:"
+ "pathWithComponents:"
+ "setCleanupPackageOnDequeue:"
+ "setJumpStartItem:"
+ "setObject:forKey:"
+ "stringByDeletingPathExtension"
+ "strongToStrongObjectsMapTable"
- "_installRequestsForItems:onVolume:removing:error:"
- "arrayWithCapacity:"
- "objectAtIndex:"

```
