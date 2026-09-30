## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-465.0.0.0.0
-  __TEXT.__text: 0x3ff68
+467.0.0.0.0
+  __TEXT.__text: 0x3fdc8
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x357c
+  __TEXT.__objc_methlist: 0x3614
   __TEXT.__const: 0x382
-  __TEXT.__cstring: 0x5872
+  __TEXT.__cstring: 0x58f2
   __TEXT.__ustring: 0x12c0
-  __TEXT.__gcc_except_tab: 0xbd8
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xdd8
+  __TEXT.__unwind_info: 0xdc0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x515
-  __TEXT.__objc_methname: 0x8236
-  __TEXT.__objc_methtype: 0x113e
-  __TEXT.__objc_stubs: 0x7a20
+  __TEXT.__objc_methname: 0x846b
+  __TEXT.__objc_methtype: 0x1141
+  __TEXT.__objc_stubs: 0x7b20
   __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2348
+  __DATA_CONST.__objc_selrefs: 0x23a8
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x3ba0
   __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x114c0
-  __AUTH_CONST.__objc_const: 0x4668
+  __AUTH_CONST.__const: 0x608
+  __AUTH_CONST.__cfstring: 0x11520
+  __AUTH_CONST.__objc_const: 0x46b0
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x318

   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0xd18
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x28c
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0x2f0
+  __DATA.__objc_ivar: 0x290
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0x300
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 6E35C122-343C-38EE-9FCD-58C9C1584170
-  Functions: 1262
-  Symbols:   4514
-  CStrings:  5260
+  UUID: 8B60BE9F-EC4E-3AB2-8002-53A178CA8AB5
+  Functions: 1268
+  Symbols:   4535
+  CStrings:  5282
 
Symbols:
+ +[TypistKeyboardData getConnectionTimeoutInSec]
+ +[TypistKeyboardData getForceLegacyImplementation]
+ +[TypistKeyboardData getTargetApplicationBundleID]
+ +[TypistKeyboardData setConnectionTimeoutInSec:]
+ +[TypistKeyboardData setForceLegacyImplementation:]
+ +[TypistKeyboardData setTargetApplicationBundleID:]
+ +[TypistKeyboardDataInputUIClient _attemptRemoteKeyboardConnection:targetApplication:]
+ +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:targetApplication:]
+ +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:targetApplication:].cold.1
+ -[TypistKeyboard getTargetApplicationBundleIdentifier]
+ -[TypistKeyboard setTargetApplicationBundleIdentifier:]
+ -[TypistKeyboardDataInputUIClient .cxx_destruct]
+ -[TypistKeyboardDataInputUIClient setTargetApplication:]
+ -[TypistKeyboardDataInputUIClient targetApplication]
+ GCC_except_table84
+ _OBJC_IVAR_$_TypistKeyboardDataInputUIClient._targetApplication
+ __OBJC_$_INSTANCE_METHODS_TypistKeyboardDataInputUIClient
+ __OBJC_$_INSTANCE_VARIABLES_TypistKeyboardDataInputUIClient
+ ___block_literal_global.453
+ __forceLegacyImplementation
+ __globalConnectionTimeoutInSec
+ __globalTargetApplication
+ _objc_msgSend$_attemptRemoteKeyboardConnection:targetApplication:
+ _objc_msgSend$connectToRemoteKeyboard:targetApplication:
+ _objc_msgSend$getConnectionTimeoutInSec
+ _objc_msgSend$getTargetApplicationBundleID
+ _objc_msgSend$getTargetApplicationBundleIdentifier
+ _objc_msgSend$setForceLegacyImplementation:
+ _objc_msgSend$setTargetApplicationBundleID:
+ _objc_msgSend$setTargetApplicationBundleIdentifier:
- +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:]
- +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:].cold.1
- GCC_except_table3
- GCC_except_table38
- GCC_except_table87
- ___38-[TypistKeyboard generateSwipeStream:]_block_invoke
- ___38-[TypistKeyboard generateSwipeStream:]_block_invoke.486
- ___44+[TypistKeyboardEmoji resetSelectedCategory]_block_invoke
- ___55-[TypistKeyboard _getScaleInFrame:isPencil:dimensions:]_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_96_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
- ___block_literal_global.454
CStrings:
+ "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@"
+ "B32@0:8d16@24"
+ "No target application bundle id is provided for IP keyboard."
+ "Setting keyboard %@ of target application: %@"
+ "T@\"NSString\",C,N,GgetTargetApplicationBundleIdentifier,SsetTargetApplicationBundleIdentifier:"
+ "T@\"NSString\",C,N,V_targetApplication"
+ "[%@] cannot be removed, because it's the only keyboard enabled. Aborting..."
+ "_attemptRemoteKeyboardConnection:targetApplication:"
+ "_targetApplication"
+ "connectToRemoteKeyboard:targetApplication:"
+ "forceInProcessDataClient"
+ "getConnectionTimeoutInSec"
+ "getForceLegacyImplementation"
+ "getTargetApplicationBundleID"
+ "getTargetApplicationBundleIdentifier"
+ "setConnectionTimeoutInSec:"
+ "setForceLegacyImplementation:"
+ "setTargetApplication:"
+ "setTargetApplicationBundleID:"
+ "setTargetApplicationBundleIdentifier:"
+ "targetApplication"
+ "targetApplicationBundleIdentifier"
- "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@"
- "B24@0:8d16"
- "[%@] cannot be removed, becuase it's the only keyboard enabled. Aborting..."
- "ko_KR@sw=Korean;hw=Automatic"

```
