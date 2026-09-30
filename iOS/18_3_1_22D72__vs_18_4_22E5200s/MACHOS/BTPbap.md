## BTPbap

> `/usr/sbin/BTPbap`

```diff

-343.1.0.0.0
-  __TEXT.__text: 0x23b0
-  __TEXT.__auth_stubs: 0x4c0
+344.25.0.0.0
+  __TEXT.__text: 0x241c
+  __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_stubs: 0x980
   __TEXT.__objc_methlist: 0x280
-  __TEXT.__cstring: 0x245
+  __TEXT.__cstring: 0x26f
   __TEXT.__const: 0x28
   __TEXT.__objc_methname: 0x8a5
   __TEXT.__oslogstring: 0x145
   __TEXT.__objc_classname: 0x36
   __TEXT.__objc_methtype: 0x15d
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18

   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x140
   __DATA.__common: 0x8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 76
-  Symbols:   119
-  CStrings:  191
+  Functions: 82
+  Symbols:   121
+  CStrings:  192
 
Symbols:
+ _DMIsMigrationNeeded
+ _objc_retainAutoreleaseReturnValue
CStrings:
+ "Avoided Watchdog timeout during Migration"

```
