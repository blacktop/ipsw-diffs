## login

> `/System/Library/PrivateFrameworks/login.framework/Versions/A/login`

```diff

-  __TEXT.__text: 0x17b1c
-  __TEXT.__objc_methlist: 0x124c
+  __TEXT.__text: 0x17f88
+  __TEXT.__objc_methlist: 0x12bc
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xd48
-  __TEXT.__cstring: 0x3aa4
+  __TEXT.__gcc_except_tab: 0xd64
+  __TEXT.__cstring: 0x3aea
   __TEXT.__dlopen_cstrs: 0xf5
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x340
-  __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb08
-  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xb18
+  __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0x8c8
-  __AUTH_CONST.__cfstring: 0x2700
-  __AUTH_CONST.__objc_const: 0x4508
+  __AUTH_CONST.__cfstring: 0x2740
+  __AUTH_CONST.__objc_const: 0x4648
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x550
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__data: 0x5b0
   __DATA.__bss: 0x128
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 565
-  Symbols:   1622
-  CStrings:  823
+  Functions: 572
+  Symbols:   1651
+  CStrings:  827
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[NSXPCConnection(LFEntitlement) lf_boolValueForEntitlementValue:]
+ -[LFSessionAgentListener .cxx_destruct]
+ -[LFSessionAgentListener privilegedInterface]
+ -[LFSessionAgentListener setPrivilegedInterface:]
+ -[LFSessionOwnerListenerDelegate listener:shouldAcceptNewConnection:]
+ -[NSXPCConnection(LFEntitlement) lf_connectionHasEntitlement:]
+ OBJC_IVAR_$_LFSessionAgentListener._privilegedInterface
+ _OBJC_CLASS_$_LFSessionOwnerListenerDelegate
+ _OBJC_METACLASS_$_LFSessionOwnerListenerDelegate
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_CATEGORY_NSXPCConnection_$_LFEntitlement
+ __OBJC_$_INSTANCE_METHODS_LFSessionOwnerListenerDelegate
+ __OBJC_$_INSTANCE_VARIABLES_LFSessionAgentListener
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LFSessionAgentListenerPublicInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LFSessionAgentListenerPublicInterface
+ __OBJC_$_PROTOCOL_REFS_LFSessionAgentListenerPublicInterface
+ __OBJC_CLASS_RO_$_LFSessionOwnerListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LFSessionAgentListenerPublicInterface
+ __OBJC_METACLASS_RO_$_LFSessionOwnerListenerDelegate
+ __OBJC_PROTOCOL_$_LFSessionAgentListenerPublicInterface
+ __OBJC_PROTOCOL_REFERENCE_$_LFSessionAgentListenerPublicInterface
+ ___69-[LFSessionOwnerListenerDelegate listener:shouldAcceptNewConnection:]_block_invoke
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32w40w
+ _objc_msgSend$lf_boolValueForEntitlementValue:
+ _objc_msgSend$lf_connectionHasEntitlement:
- ___block_descriptor_48_e8_32s40w_e5_v8?0l
- ___copy_helper_block_e8_32s40w
- ___destroy_helper_block_e8_32s40w
CStrings:
+ "com.apple.private.sessionagent.spi"
+ "com.apple.private.sessionowner.spi"

```
