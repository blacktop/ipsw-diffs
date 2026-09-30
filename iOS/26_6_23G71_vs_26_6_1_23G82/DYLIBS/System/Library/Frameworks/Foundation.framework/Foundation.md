## Foundation

> `/System/Library/Frameworks/Foundation.framework/Foundation`

```diff

 5026.6.7.0.0
-  __TEXT.__text: 0xac9d9c
+  __TEXT.__text: 0xac9ddc
   __TEXT.__auth_stubs: 0x9f10
   __TEXT.__delay_stubs: 0x800
   __TEXT.__delay_helper: 0x184
   __TEXT.__objc_methlist: 0x23e4c
   __TEXT.__const: 0x267213
-  __TEXT.__cstring: 0x320c0
+  __TEXT.__cstring: 0x3210f
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__swift5_typeref: 0xcab6
   __TEXT.__swift5_capture: 0x29c8

   __TEXT.__gcc_except_tab: 0x6044
   __TEXT.__ustring: 0x53a
   __TEXT.__dof_NSProcess: 0x34f
-  __TEXT.__dof_NSXPCProx: 0x7a2
+  __TEXT.__dof_NSXPCProx: 0x7a3
   __TEXT.__dof_NSXPCList: 0x2e9
   __TEXT.__dof_NSXPCConn: 0x26cc
   __TEXT.__dof_NSXPCLis0: 0x865

   __TEXT.__unwind_info: 0x1c278
   __TEXT.__eh_frame: 0x1fe0c
   __TEXT.__objc_classname: 0x624d
-  __TEXT.__objc_methname: 0x329b0
-  __TEXT.__objc_methtype: 0x95d4
+  __TEXT.__objc_methname: 0x329c0
+  __TEXT.__objc_methtype: 0x95d7
   __TEXT.__objc_stubs: 0x22160
   __DATA_CONST.__got: 0x28e0
   __DATA_CONST.__const: 0x9ec0

   __DATA_CONST.__objc_arraydata: 0xe098
   __AUTH_CONST.__auth_got: 0x5098
   __AUTH_CONST.__const: 0x31a18
-  __AUTH_CONST.__cfstring: 0x25da0
+  __AUTH_CONST.__cfstring: 0x25dc0
   __AUTH_CONST.__objc_const: 0x33238
   __AUTH_CONST.__objc_intobj: 0x1278
   __AUTH_CONST.__objc_arrayobj: 0x2250

   - /usr/lib/swift/libswiftos.dylib
   Functions: 40756
   Symbols:   91168
-  CStrings:  17544
+  CStrings:  17545
 
Symbols:
+ +[_NSPredicateOperatorUtilities copyRegexFindSafePattern:toBuffer:capacity:]
+ _objc_msgSend$copyRegexFindSafePattern:toBuffer:capacity:
- +[_NSPredicateOperatorUtilities copyRegexFindSafePattern:toBuffer:]
- _objc_msgSend$copyRegexFindSafePattern:toBuffer:
Functions:
~ -[NSDictionary(NSDictionary) initWithCoder:] : 1612 -> 1628
~ +[_NSPredicateOperatorUtilities doRegexForString:pattern:likeProtect:flags:context:] : 1696 -> 1692
~ __doPatternNormalization : 1128 -> 1132
~ -[_NSKeyedCoderOldStyleArray fillObjCType:count:at:] : 300 -> 284
~ +[_NSPredicateOperatorUtilities newStringFrom:usingUnicodeTransforms:] : 656 -> 652
~ +[_NSPredicateOperatorUtilities copyRegexFindSafePattern:toBuffer:] -> +[_NSPredicateOperatorUtilities copyRegexFindSafePattern:toBuffer:capacity:] : 1040 -> 1104
~ -[NSURLComponents setPercentEncodedQueryItems:] : 84 -> 88
CStrings:
+ "Failed to provide an adequately sized buffer for escaping regex pattern string"
+ "copyRegexFindSafePattern:toBuffer:capacity:"
+ "q40@0:8@16^S24Q32"
- "copyRegexFindSafePattern:toBuffer:"
- "q32@0:8@16^S24"
```
