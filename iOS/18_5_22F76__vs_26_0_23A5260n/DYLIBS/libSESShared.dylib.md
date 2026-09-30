## libSESShared.dylib

> `/usr/lib/libSESShared.dylib`

```diff

-55.4.0.0.0
-  __TEXT.__text: 0xdb24
+60.26.1.0.0
+  __TEXT.__text: 0xdfd8
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x898
-  __TEXT.__const: 0xa60
-  __TEXT.__cstring: 0xc3a
+  __TEXT.__objc_methlist: 0x900
+  __TEXT.__const: 0xa68
+  __TEXT.__cstring: 0xd0a
   __TEXT.__oslogstring: 0x721
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__unwind_info: 0x3c8
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x148a
-  __TEXT.__objc_methtype: 0x4cb
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x2e0
+  __TEXT.__objc_methname: 0x151a
+  __TEXT.__objc_methtype: 0x4ea
+  __TEXT.__objc_stubs: 0x1080
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x708
+  __DATA_CONST.__objc_selrefs: 0x728
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0xed8
+  __AUTH_CONST.__cfstring: 0x1380
+  __AUTH_CONST.__objc_const: 0xf38
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_ivar: 0xa4
   __DATA.__data: 0x8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E35BE55-38AD-3E57-8D61-B8B3034EEDBE
-  Functions: 273
-  Symbols:   1027
-  CStrings:  750
+  UUID: 8CB9865A-EAB4-3EAA-964A-759A10B77AEB
+  Functions: 285
+  Symbols:   1057
+  CStrings:  773
 
Symbols:
+ +[CALogger bucketRawTrackingRequestDuration:]
+ +[SESTapToRadar requestTapToRadarKML:client:]
+ -[NSSet(Functional) allSatisfy:]
+ -[NSSet(Functional) contains:]
+ -[NSSet(Functional) filter:]
+ -[NSSet(Functional) filterMap:]
+ -[NSSet(Functional) find:]
+ -[NSSet(Functional) ses_map:]
+ -[SESTapToRadar _requestTapToRadarSync:component:client:fullArchive:]
+ GCC_except_table9
+ _DERParseInteger64Signed
+ _DERParseIntegerSigned
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_SESTapToRadar._component
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_Functional
+ __OBJC_$_CATEGORY_NSSet_$_Functional
+ ___26+[SESBootUUID getInstance]_block_invoke.cold.1
+ ___45+[SESTapToRadar requestTapToRadarKML:client:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___getSBUserNotificationDismissOnLockSymbolLoc_block_invoke.cold.1
+ _abort_with_reason
+ _objc_msgSend$_requestTapToRadarSync:component:client:fullArchive:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$dataWithHexString:
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- -[SESTapToRadar _requestTapToRadarSync:client:fullArchive:]
- GCC_except_table7
- _OUTLINED_FUNCTION_3
- _abort_report_np
- _objc_msgSend$_requestTapToRadarSync:client:fullArchive:
- _objc_msgSend$uppercaseString
CStrings:
+ "991522"
+ "ALL"
+ "BuildNonOSPPreShareTlv"
+ "Failed to get kern.bootsessionuuid"
+ "I24@0:8d16"
+ "KML"
+ "NSString *getSBUserNotificationDismissOnLock(void)"
+ "SESTapToRadar.m"
+ "SecureElementService KML TTR - %@"
+ "Serious Bug"
+ "T@\"NSData\",R,N,V_readerIdentifier"
+ "_component"
+ "_requestTapToRadarSync:component:client:fullArchive:"
+ "bucketRawTrackingRequestDuration:"
+ "contains:"
+ "currentHandler"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "requestTapToRadarKML:client:"
+ "v44@0:8@16@24@32B40"
+ "void *SpringBoardServicesLibrary(void)"
- "KeyRoleOnUpgrade"
- "T@\"NSString\",R,N,V_readerIdentifier"
- "_requestTapToRadarSync:client:fullArchive:"
- "uppercaseString"

```
