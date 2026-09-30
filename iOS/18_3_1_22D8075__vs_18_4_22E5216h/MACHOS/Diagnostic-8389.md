## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x1f3ec
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x140
+820.100.56.0.0
+  __TEXT.__text: 0x1ddcc
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x4fc
   __TEXT.__cstring: 0x14dd
-  __TEXT.__const: 0x2fa8
+  __TEXT.__const: 0x3428
   __TEXT.__constg_swiftt: 0xd88
   __TEXT.__swift5_typeref: 0xb93
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_proto: 0x340
   __TEXT.__swift5_types: 0xfc
   __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0xcb7
-  __TEXT.__objc_methtype: 0x67d
+  __TEXT.__objc_methname: 0xccc
+  __TEXT.__objc_methtype: 0x68c
   __TEXT.__swift5_fieldmd: 0xb88
   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xa50
-  __TEXT.__eh_frame: 0x7f8
-  __DATA_CONST.__auth_got: 0x668
+  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__eh_frame: 0x858
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x2128
+  __DATA_CONST.__const: 0x2120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA.__objc_const: 0x1090
-  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_const: 0xa08
+  __DATA.__objc_selrefs: 0x410
   __DATA.__objc_data: 0x728
   __DATA.__data: 0x11d0
   __DATA.__bss: 0x6780

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 943
-  Symbols:   144
+  Functions: 845
+  Symbols:   150
   CStrings:  365
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataSingleCase
- _swift_initStructMetadata
CStrings:
+ "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:"
+ "v84@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@\"NSArray\"68@?<v@?@\"NSString\"@\"NSError\">76"
+ "v84@0:8@16i24@28@36@44@52@60@68@?76"
- "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:"
- "v76@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@?<v@?@\"NSString\"@\"NSError\">68"
- "v76@0:8@16i24@28@36@44@52@60@?68"

```
