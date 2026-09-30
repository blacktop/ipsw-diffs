## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x4da0
+1656.100.222.0.0
+  __TEXT.__text: 0x5018
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x51c
-  __TEXT.__const: 0xc0
+  __TEXT.__objc_methlist: 0x6fc
+  __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x6e9
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__oslogstring: 0x405
-  __TEXT.__unwind_info: 0x1a0
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x1780
-  __TEXT.__objc_methtype: 0x7be
-  __TEXT.__objc_stubs: 0xfc0
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__objc_classname: 0xcd
+  __TEXT.__objc_methname: 0x1855
+  __TEXT.__objc_methtype: 0x7d5
+  __TEXT.__objc_stubs: 0x10a0
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0xfb0
+  __AUTH_CONST.__objc_const: 0xc28
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x180
-  __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x10
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 122
-  Symbols:   241
-  CStrings:  482
+  Functions: 127
+  Symbols:   252
+  CStrings:  490
 
Symbols:
+ _LACErrorCancelledByHigherPriorityAuthenticationKey
+ _LACErrorCodeSystemCancel
+ _LACErrorSubcodeInterruptedByAnotherEvaluation
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_LACCachedExternalizedContext
+ _OBJC_CLASS_$_LACPolicyUtilities
+ _OBJC_CLASS_$_NSDictionary
+ _objc_retain_x25
- _OBJC_CLASS_$_LACachedExternalizedContext
- _objc_release_x2
CStrings:
+ "@\"<LACRemoteContextOwnership>\""
+ "@\"LACCachedExternalizedContext\""
+ "@28@0:8@16B24"
+ "LACContextExternalizing"
+ "LACRemoteContextOwnership"
+ "T@\"<LACRemoteContextOwnership>\",R,N,V_ownership"
+ "T@\"LACCachedExternalizedContext\",R,N,V_cachedExternalizedContext"
+ "_cancelationErrorWithDescription:cancelledByHigherPriority:"
+ "analyticsData"
+ "biomeDialogEvent"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithCode:subcode:debugDescription:"
+ "errorWithCode:subcode:userInfo:"
+ "numberWithBool:"
+ "setBundleID:"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?B@\"NSError\">32"
+ "v44@0:8B16q20@\"<LACOriginatorProt>\"28@?<v@?B@\"NSError\">36"
+ "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LACOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@16q24@\"<LACOriginatorProt>\"32@?<v@?B@\"NSError\">40"
+ "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LACOriginatorProt>\"40@?<v@?B@\"NSError\">48"
- "@\"<LARemoteContextOwnership>\""
- "@\"LACachedExternalizedContext\""
- "LAContextExternalizationProt"
- "LARemoteContextOwnership"
- "T@\"<LARemoteContextOwnership>\",R,N,V_ownership"
- "T@\"LACachedExternalizedContext\",R,N,V_cachedExternalizedContext"
- "_cancelationError"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?B@\"NSError\">32"
- "v44@0:8B16q20@\"<LAOriginatorProt>\"28@?<v@?B@\"NSError\">36"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LAOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16q24@\"<LAOriginatorProt>\"32@?<v@?B@\"NSError\">40"
- "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LAOriginatorProt>\"40@?<v@?B@\"NSError\">48"

```
