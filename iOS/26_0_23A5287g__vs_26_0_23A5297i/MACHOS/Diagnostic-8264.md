## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

-921.0.82.0.0
-  __TEXT.__text: 0x3244
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x940
+921.0.98.0.0
+  __TEXT.__text: 0x34f4
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0x980
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__cstring: 0x50b
-  __TEXT.__oslogstring: 0x4ac
+  __TEXT.__cstring: 0x530
+  __TEXT.__oslogstring: 0x504
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x916
+  __TEXT.__objc_methname: 0x94c
   __TEXT.__objc_methtype: 0x131
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x580
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x320
+  __DATA.__objc_selrefs: 0x330
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 160FFC0A-9849-31B6-B37E-A8572DD86602
-  Functions: 47
-  Symbols:   106
-  CStrings:  287
+  UUID: 56759521-526E-3C9E-820D-C12E19E35E3F
+  Functions: 48
+  Symbols:   111
+  CStrings:  296
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_MSUDataAccessor
+ _kCFBooleanTrue
+ _kT200OptionRestoreInternal
+ _kT200TagFWSkipSameVersion
CStrings:
+ "Failed to get prebootPath: %@, error: %@"
+ "InternalBuild"
+ "RestoreSystemPartition"
+ "copyPathForPersonalizedData:error:"
+ "optionsDict failed to allocate"
+ "prebootPath: %@"
+ "sharedDataAccessor"

```
