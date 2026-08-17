## login

> `/System/Library/PrivateFrameworks/login.framework/Versions/A/login`

```diff

-264.4.2.0.0
-  __TEXT.__text: 0x16c18
+264.4.2.100.0
+  __TEXT.__text: 0x16d98
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x121c
+  __TEXT.__objc_methlist: 0x127c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0xc64
-  __TEXT.__cstring: 0x3760
+  __TEXT.__cstring: 0x3783
   __TEXT.__dlopen_cstrs: 0xf5
-  __TEXT.__unwind_info: 0x970
-  __TEXT.__objc_classname: 0x339
-  __TEXT.__objc_methname: 0x273d
+  __TEXT.__unwind_info: 0x980
+  __TEXT.__objc_classname: 0x36d
+  __TEXT.__objc_methname: 0x277b
   __TEXT.__objc_methtype: 0x921
-  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_stubs: 0x2000
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac8
-  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x878
-  __AUTH_CONST.__cfstring: 0x25c0
-  __AUTH_CONST.__objc_const: 0x44e8
+  __AUTH_CONST.__cfstring: 0x25e0
+  __AUTH_CONST.__objc_const: 0x4598
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0xa8
-  __DATA.__data: 0x550
+  __DATA.__objc_ivar: 0xac
+  __DATA.__data: 0x5b0
   __DATA.__bss: 0x100
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 544
-  Symbols:   1438
-  CStrings:  1072
+  Functions: 549
+  Symbols:   1456
+  CStrings:  1077
 
Symbols:
+ +[NSXPCConnection(LFEntitlement) lf_boolValueForEntitlementValue:]
+ -[LFSessionAgentListener .cxx_destruct]
+ -[LFSessionAgentListener privilegedInterface]
+ -[LFSessionAgentListener setPrivilegedInterface:]
+ -[NSXPCConnection(LFEntitlement) lf_connectionHasEntitlement:]
+ OBJC_IVAR_$_LFSessionAgentListener._privilegedInterface
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_CATEGORY_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_INSTANCE_VARIABLES_LFSessionAgentListener
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LFSessionAgentListenerPublicInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LFSessionAgentListenerPublicInterface
+ __OBJC_$_PROTOCOL_REFS_LFSessionAgentListenerPublicInterface
+ __OBJC_LABEL_PROTOCOL_$_LFSessionAgentListenerPublicInterface
+ __OBJC_PROTOCOL_$_LFSessionAgentListenerPublicInterface
+ __OBJC_PROTOCOL_REFERENCE_$_LFSessionAgentListenerPublicInterface
+ _objc_msgSend$lf_boolValueForEntitlementValue:
+ _objc_msgSend$lf_connectionHasEntitlement:
CStrings:
+ "LFEntitlement"
+ "LFSessionAgentListenerPublicInterface"
+ "com.apple.private.sessionagent.spi"
+ "lf_boolValueForEntitlementValue:"
+ "lf_connectionHasEntitlement:"
```
