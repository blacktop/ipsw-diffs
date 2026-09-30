## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-6087.1.2.1.0
-  __TEXT.__text: 0x4d580
-  __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0x337c
+6093.0.0.0.0
+  __TEXT.__text: 0x4d8c0
+  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__objc_methlist: 0x339c
   __TEXT.__const: 0xf02
-  __TEXT.__cstring: 0x43c7
-  __TEXT.__oslogstring: 0x25c9
+  __TEXT.__cstring: 0x4407
+  __TEXT.__oslogstring: 0x2709
   __TEXT.__gcc_except_tab: 0x2cec
   __TEXT.__swift5_typeref: 0x352
   __TEXT.__swift5_capture: 0x2c8

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1cf8
+  __TEXT.__unwind_info: 0x1d40
   __TEXT.__eh_frame: 0x450
-  __TEXT.__objc_classname: 0x740
-  __TEXT.__objc_methname: 0x7a3a
-  __TEXT.__objc_methtype: 0x1273
-  __TEXT.__objc_stubs: 0x4560
+  __TEXT.__objc_classname: 0x74b
+  __TEXT.__objc_methname: 0x7a93
+  __TEXT.__objc_methtype: 0x1287
+  __TEXT.__objc_stubs: 0x4580
   __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0xe78
-  __DATA_CONST.__objc_classlist: 0x250
+  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c80
+  __DATA_CONST.__objc_selrefs: 0x1c90
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1c8
-  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__auth_got: 0xbc8
   __AUTH_CONST.__const: 0x1860
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x6ed8
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x6f68
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x818
+  __AUTH.__objc_data: 0x868
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x4f8
   __DATA.__data: 0x530

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A3BE3466-B557-37E0-A63B-5CE29FF4456E
-  Functions: 2082
-  Symbols:   5807
-  CStrings:  2912
+  UUID: 599B379D-650F-3CF3-B4E9-299F67BFDB6C
+  Functions: 2085
+  Symbols:   5825
+  CStrings:  2926
 
Symbols:
+ +[HDTailSpin _isImprovedHealthAndActivityEnabled]
+ +[HDTailSpin generateTailSpinForTeam:category:description:logger:]
+ _DRTailspinRequest
+ _HDTailSpinCategorySlowWorkoutEnd
+ _HDTailSpinCategorySlowWorkoutStart
+ _HDTailSpinTeamIdentifierHealthKit
+ _HKImproveHealthAndActivityAnalyticsAllowed
+ _OBJC_CLASS_$_HDTailSpin
+ _OBJC_METACLASS_$_HDTailSpin
+ __OBJC_$_CLASS_METHODS_HDTailSpin
+ __OBJC_CLASS_RO_$_HDTailSpin
+ __OBJC_METACLASS_RO_$_HDTailSpin
+ _objc_msgSend$_isImprovedHealthAndActivityEnabled
+ _sysctl
CStrings:
+ "HDTailSpin"
+ "SlowWorkoutEnd"
+ "SlowWorkoutStart"
+ "[tailspin] Debugger Attached - Skipping tailspin for  %{public}@-%{public}@: %{public}@"
+ "[tailspin] Failed to generate tailspin for %{public}@-%{public}@: %{public}@"
+ "[tailspin] IH&A is not enabled. Not triggering tailspin for %{public}@-%{public}@: %{public}@"
+ "[tailspin] Saving tailspin for  %{public}@-%{public}@: %{public}@"
+ "_isImprovedHealthAndActivityEnabled"
+ "com.apple.HealthKit"
+ "generateTailSpinForTeam:category:description:logger:"
+ "v48@0:8@16@24@32@40"

```
