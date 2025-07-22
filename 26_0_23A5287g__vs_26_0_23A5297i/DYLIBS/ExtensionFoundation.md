## ExtensionFoundation

> `/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation`

```diff

-254.0.0.0.0
-  __TEXT.__text: 0xdd368
+257.0.0.0.0
+  __TEXT.__text: 0xdd39c
   __TEXT.__auth_stubs: 0x2810
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x4c1c
   __TEXT.__const: 0x3b60
   __TEXT.__cstring: 0x8a41
-  __TEXT.__gcc_except_tab: 0x7e4
-  __TEXT.__oslogstring: 0x649f
+  __TEXT.__gcc_except_tab: 0x7bc
+  __TEXT.__oslogstring: 0x648f
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__constg_swiftt: 0x2750
   __TEXT.__swift5_typeref: 0x202e

   __TEXT.__swift_as_ret: 0x80
   __TEXT.__unwind_info: 0x3500
   __TEXT.__eh_frame: 0x3300
-  __TEXT.__objc_classname: 0x889
-  __TEXT.__objc_methname: 0x9d72
+  __TEXT.__objc_classname: 0x88d
+  __TEXT.__objc_methname: 0x9d5c
   __TEXT.__objc_methtype: 0x1379
-  __TEXT.__objc_stubs: 0x52e0
+  __TEXT.__objc_stubs: 0x52c0
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0xf98
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25f8
+  __DATA_CONST.__objc_selrefs: 0x25f0
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x1d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BB7C8169-36D1-38D0-8BA4-67A3FFE30924
+  UUID: D87EAE91-EA3C-3AFB-9EA1-F0F2DD05D667
   Functions: 5046
-  Symbols:   16315
+  Symbols:   16314
   CStrings:  3668
 
Symbols:
- _objc_msgSend$remoteObjectInterface
Functions:
~ -[EXExtensionContextImplementation .cxx_destruct] : 172 -> 168
~ -[EXExtensionContextImplementation _principalObject] : 12 -> 44
~ -[EXExtensionContextImplementation _willPerformHostCallback:] : 448 -> 368
~ -[EXExtensionContextImplementation _setPrincipalObject:] : 8 -> 12
~ _$s19ExtensionFoundation23LocalLSDatabaseObserverC6canAdd21extensionPointRecords4hostSbSaySo011LSExtensionI6RecordCG_AA10AuditTokenVtFZ8evaluateL_6recordSbAH_tF : 3380 -> 3468
~ -[EXExtensionContextImplementation _willPerformHostCallback:].cold.1 : 104 -> 116
CStrings:
+ "!1"
+ "Error calling `___nsx_pingHost` on `%lX`"
+ "T@,W,S_setPrincipalObject:,V__principalObject"
- "Error calling `___nsx_pingHost` on `%@` interface `%@`"
- "T@,&,S_setPrincipalObject:,V__principalObject"
- "remoteObjectInterface"

```
