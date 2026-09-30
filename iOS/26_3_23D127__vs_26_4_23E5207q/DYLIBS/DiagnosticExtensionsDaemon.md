## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-205.6.0.0.0
-  __TEXT.__text: 0x758fc
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x6c3c
+211.1.0.0.0
+  __TEXT.__text: 0x792c0
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_methlist: 0x6c2c
   __TEXT.__const: 0x31a
-  __TEXT.__cstring: 0x54e2
-  __TEXT.__gcc_except_tab: 0x1f7c
-  __TEXT.__oslogstring: 0x8ce9
+  __TEXT.__cstring: 0x5492
+  __TEXT.__gcc_except_tab: 0x1eb0
+  __TEXT.__oslogstring: 0x8cb9
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x42

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1c18
+  __TEXT.__unwind_info: 0x1cf0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x895
-  __TEXT.__objc_methname: 0xf471
+  __TEXT.__objc_classname: 0x8cd
+  __TEXT.__objc_methname: 0xf442
   __TEXT.__objc_methtype: 0x24b3
-  __TEXT.__objc_stubs: 0xc1a0
-  __DATA_CONST.__got: 0x6e8
+  __TEXT.__objc_stubs: 0xc160
+  __DATA_CONST.__got: 0x6d8
   __DATA_CONST.__const: 0x2100
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a40
+  __DATA_CONST.__objc_selrefs: 0x3a28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x648
   __AUTH_CONST.__const: 0xc40
   __AUTH_CONST.__cfstring: 0x4e00
   __AUTH_CONST.__objc_const: 0x12f68

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6A9DA8D4-FF6E-3F80-BBBE-ED8C13C39681
-  Functions: 2817
-  Symbols:   9783
-  CStrings:  5221
+  UUID: A1A41DAE-CE8A-3B78-A539-A43AAA75F19D
+  Functions: 2825
+  Symbols:   9926
+  CStrings:  5214
 
Symbols:
+ +[NSDate(Serialization) dedDateWithString:]
+ -[NSDate(Serialization) dedSerialize]
+ -[NSURLSessionConfiguration(DEDDataUsage) dedSetUpDataUsageWithConfiguration:]
+ -[NSURLSessionConfiguration(DEDDataUsage) dedSetUpDataUsageWithConfiguration:].cold.1
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _objc_msgSend$dedDateWithString:
+ _objc_msgSend$dedSerialize
+ _objc_msgSend$dedSetUpDataUsageWithConfiguration:
- +[DEDCloudKitExtensionsUtil updateELSSnapshotStatus:]
- +[NSDate(Serialization) _dateWithString:]
- -[NSDate(Serialization) serialize]
- -[NSURLSessionConfiguration(DEDDataUsage) setUpDataUsageWithConfiguration:]
- -[NSURLSessionConfiguration(DEDDataUsage) setUpDataUsageWithConfiguration:].cold.1
- _ELSDefaultStatus
- _OBJC_CLASS_$_ELSManager
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_dateWithString:
- _objc_msgSend$refreshKeyPaths:
- _objc_msgSend$setUpDataUsageWithConfiguration:
- _objc_msgSend$sharedManager
- _objc_msgSend$snapshot
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "dedDateWithString:"
+ "dedSerialize"
+ "dedSetUpDataUsageWithConfiguration:"
- "Setting uploadDelegate: [%{public}@] session [%{public}@]"
- "_dateWithString:"
- "refreshKeyPaths:"
- "setUpDataUsageWithConfiguration:"
- "sharedManager"
- "snapshot"
- "updateELSSnapshotStatus:"

```
