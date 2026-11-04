## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-1084.40.7.0.0
-  __TEXT.__text: 0x3ff34
-  __TEXT.__objc_methlist: 0x5bd8
+1084.60.3.0.0
+  __TEXT.__text: 0x40fa8
+  __TEXT.__objc_methlist: 0x5be0
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x492e
+  __TEXT.__cstring: 0x4964
   __TEXT.__oslogstring: 0x27cb
   __TEXT.__gcc_except_tab: 0x868
   __TEXT.__unwind_info: 0x1e78

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcc0
+  __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d98
+  __DATA_CONST.__objc_selrefs: 0x1dd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__got: 0x500
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6040
+  __AUTH_CONST.__cfstring: 0x6100
   __AUTH_CONST.__objc_const: 0xb018
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x708

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2334
-  Symbols:   4007
-  CStrings:  1067
+  Functions: 2335
+  Symbols:   4010
+  CStrings:  1073
 
Symbols:
+ -[NSError(RBSErrors) rbs_errorRedactedForUntrustedClient]
+ _OBJC_CLASS_$_NSCharacterSet
+ _RBSErrorRedactForUntrustedClientKey
Functions:
~ -[RBSEmbeddedAppProcessIdentity _initEmbeddedApp:personaString:] : 308 -> 988
~ -[RBSExtensionProcessIdentity _initWithExtensionIdentity:hostIdentity:hostIdentifier:auid:] : 544 -> 1872
~ -[RBSXPCServiceProcessIdentity _initWithXPCServiceID:pid:auid:] : 804 -> 1464
~ -[RBSXPCServiceDefinition description] : 128 -> 492
~ -[RBSDextProcessIdentity _initDextWithServerName:label:containingAppBundleID:] : 348 -> 692
+ -[NSError(RBSErrors) rbs_errorRedactedForUntrustedClient]
~ -[RBSEmbeddedAppProcessIdentity debugDescription] : 284 -> 888
CStrings:
+ "%C"
+ "RBSErrorRedactForUntrustedClient"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u{%04x}"
```
