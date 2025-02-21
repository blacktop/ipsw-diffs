## com.apple.datamigrator

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator`

```diff

-2817.0.0.0.0
-  __TEXT.__text: 0x11340
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_stubs: 0x2da0
-  __TEXT.__objc_methlist: 0x1114
-  __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x3d3b
-  __TEXT.__cstring: 0x38fa
-  __TEXT.__objc_classname: 0x2fa
-  __TEXT.__objc_methtype: 0x7e7
-  __TEXT.__gcc_except_tab: 0x858
+2830.0.0.0.0
+  __TEXT.__text: 0x114b0
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_methlist: 0x12b4
+  __TEXT.__const: 0x80
+  __TEXT.__objc_methname: 0x3d5e
+  __TEXT.__cstring: 0x3875
+  __TEXT.__objc_classname: 0x311
+  __TEXT.__objc_methtype: 0x7ea
+  __TEXT.__gcc_except_tab: 0x878
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x4e8
-  __DATA_CONST.__auth_got: 0x4f8
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__oslogstring: 0xd6
+  __TEXT.__unwind_info: 0x4f0
+  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x28c0
+  __DATA_CONST.__cfstring: 0x2880
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_dictobj: 0x938
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3310
-  __DATA.__objc_selrefs: 0xd70
+  __DATA.__objc_const: 0x3030
+  __DATA.__objc_selrefs: 0xdf8
   __DATA.__objc_ivar: 0x1a4
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x190

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 427
-  Symbols:   303
-  CStrings:  1168
+  Functions: 440
+  Symbols:   306
+  CStrings:  1172
 
Symbols:
+ _OBJC_CLASS_$_MDMConfiguration
+ __DMCoreLog
+ __os_log_impl
+ _os_log_type_enabled
- _objc_retain_x27
CStrings:
+ "... completed migration for %{public}@ (%g s) with success %d%@"
+ "... completed task '%{public}@' (%g s)"
+ "@48@0:8@16@24@32@40"
+ "Beginning migration for %{public}@; estimate is %g seconds"
+ "Beginning task '%{public}@'; estimate is %g seconds"
+ "DMRapidReturnToService"
+ "DidRestoreFromBackup"
+ "EraseIsRapidReturnToService"
+ "_dispositionDictFromContext:buildVersion:lastBuildVersion:environment:"
+ "isRapidReturnToService"
- "... completed migration for %@ (%g s) with success %d%@"
- "... completed task '%@' (%@ s)"
- "@40@0:8@16@24@32"
- "Beginning migration for %@; estimate is %g seconds"
- "Beginning task '%@'; estimate is %@ seconds"
- "_dispositionDictFromContext:buildVersion:lastBuildVersion:"

```
