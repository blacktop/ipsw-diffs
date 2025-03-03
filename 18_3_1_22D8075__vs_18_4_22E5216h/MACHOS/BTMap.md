## BTMap

> `/usr/sbin/BTMap`

```diff

-343.1.0.0.0
-  __TEXT.__text: 0x3a4c
-  __TEXT.__auth_stubs: 0x5d0
+344.27.0.0.0
+  __TEXT.__text: 0x3b68
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x348
+  __TEXT.__objc_methlist: 0x494
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x3b0
+  __TEXT.__cstring: 0x3da
   __TEXT.__objc_methname: 0xbf6
   __TEXT.__oslogstring: 0x34d
   __TEXT.__objc_classname: 0x70
   __TEXT.__objc_methtype: 0x270
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__auth_got: 0x2f8
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x280
-  __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xa00
-  __DATA.__objc_selrefs: 0x3c8
+  __DATA.__objc_const: 0x790
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x190
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x40
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 94
-  Symbols:   140
-  CStrings:  300
+  Functions: 103
+  Symbols:   141
+  CStrings:  301
 
Symbols:
+ _DMIsMigrationNeeded
CStrings:
+ "Avoided Watchdog timeout during Migration"

```
