## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

```diff

-14.100.5.0.0
-  __TEXT.__text: 0x1b74c
-  __TEXT.__auth_stubs: 0xe50
+14.120.2.0.0
+  __TEXT.__text: 0x220e0
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_methlist: 0x1d4
-  __TEXT.__const: 0x1816
-  __TEXT.__cstring: 0x61a
-  __TEXT.__swift5_typeref: 0x7b8
-  __TEXT.__swift5_capture: 0x1cc
-  __TEXT.__oslogstring: 0x519
-  __TEXT.__constg_swiftt: 0x6f8
-  __TEXT.__swift5_reflstr: 0x31a
-  __TEXT.__swift5_fieldmd: 0x60c
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0xd0
-  __TEXT.__swift5_proto: 0x16c
-  __TEXT.__swift5_types: 0x8c
+  __TEXT.__const: 0x21f6
+  __TEXT.__cstring: 0x7aa
+  __TEXT.__swift5_typeref: 0x996
+  __TEXT.__swift5_capture: 0x288
+  __TEXT.__oslogstring: 0x5b9
+  __TEXT.__constg_swiftt: 0x95c
+  __TEXT.__swift5_reflstr: 0x35a
+  __TEXT.__swift5_fieldmd: 0x754
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_assocty: 0xe8
+  __TEXT.__swift5_proto: 0x210
+  __TEXT.__swift5_types: 0xb4
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x720
-  __TEXT.__eh_frame: 0x908
+  __TEXT.__unwind_info: 0x878
+  __TEXT.__eh_frame: 0xb38
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methname: 0x2cc
   __TEXT.__objc_methtype: 0xa1
   __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x730
-  __AUTH_CONST.__auth_ptr: 0x2d8
-  __AUTH_CONST.__const: 0x1348
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_ptr: 0x2f0
+  __AUTH_CONST.__const: 0x1a88
   __AUTH_CONST.__objc_const: 0x560
   __AUTH.__objc_data: 0x368
   __AUTH.__data: 0xe0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x518
-  __DATA.__bss: 0x2780
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x3c00
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1f8
-  __DATA_DIRTY.__data: 0x3f0
+  __DATA_DIRTY.__data: 0x3e0
   __DATA_DIRTY.__bss: 0x500
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 656
-  Symbols:   205
-  CStrings:  130
+  Functions: 823
+  Symbols:   223
+  CStrings:  144
 
Symbols:
+ _dispatch_semaphore_create
+ _objc_release_x25
+ _objc_retain_x26
+ _swift_cvw_enumFn_getEnumTag
+ _swift_getEnumCaseMultiPayload
+ _swift_getErrorValue
+ _swift_projectBox
+ _swift_storeEnumTagMultiPayload
CStrings:
+ "Done with pattern check"
+ "Error in pattern matching: ("
+ "Failed to connect to listener, error: "
+ "Failed to connect to listener, error: %@"
+ "Failed to send message or decode reply: "
+ "Failed to send message or decode reply: %@"
+ "Failed to send message or get reply: "
+ "Failed to send message: %@"
+ "Invalid number of keys found, expected one."
+ "Received response: %s"
+ "Unexpected error"
+ "XPC request timed out"
+ "com.apple.corediagnostics.patternMatchingQueue"
+ "com.apple.diagnosticservicesd"

```
