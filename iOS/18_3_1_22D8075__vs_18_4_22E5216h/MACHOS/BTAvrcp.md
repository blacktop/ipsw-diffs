## BTAvrcp

> `/usr/sbin/BTAvrcp`

```diff

-343.1.0.0.0
-  __TEXT.__text: 0xde4c
-  __TEXT.__auth_stubs: 0x810
+344.27.0.0.0
+  __TEXT.__text: 0xde50
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x2560
-  __TEXT.__objc_methlist: 0x1174
+  __TEXT.__objc_methlist: 0x12dc
   __TEXT.__const: 0x50
   __TEXT.__objc_methname: 0x232e
-  __TEXT.__cstring: 0x797
+  __TEXT.__cstring: 0x7c1
   __TEXT.__objc_classname: 0x278
   __TEXT.__objc_methtype: 0x464
   __TEXT.__oslogstring: 0x31c
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x4d8
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0xbe0
+  __TEXT.__unwind_info: 0x4b0
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x1cd8
-  __DATA.__objc_selrefs: 0xaa8
+  __DATA.__objc_const: 0x1a48
+  __DATA.__objc_selrefs: 0xb38
   __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x140
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x40
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 434
-  Symbols:   247
-  CStrings:  712
+  Functions: 433
+  Symbols:   248
+  CStrings:  713
 
Symbols:
+ _DMIsMigrationNeeded
CStrings:
+ "Avoided Watchdog timeout during Migration"

```
