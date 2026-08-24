## ViewBridge

> `/System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge`

```diff

-861.0.0.0.0
-  __TEXT.__text: 0xbb0b8
+864.0.0.0.0
+  __TEXT.__text: 0xbb1f4
   __TEXT.__objc_methlist: 0x7b1c
   __TEXT.__const: 0x1c8
-  __TEXT.__gcc_except_tab: 0x5f7c
-  __TEXT.__cstring: 0x23e2d
-  __TEXT.__oslogstring: 0xde7d
-  __TEXT.__unwind_info: 0x3b18
+  __TEXT.__gcc_except_tab: 0x5f30
+  __TEXT.__cstring: 0x23d82
+  __TEXT.__oslogstring: 0xe015
+  __TEXT.__unwind_info: 0x3b30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48f0
+  __DATA_CONST.__objc_selrefs: 0x48f8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x730
   __AUTH_CONST.__const: 0x3918
-  __AUTH_CONST.__cfstring: 0x10220
+  __AUTH_CONST.__cfstring: 0x101c0
   __AUTH_CONST.__objc_const: 0xb020
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5106
-  Symbols:   8402
+  Functions: 5105
+  Symbols:   8405
   CStrings:  4729
 
Symbols:
+ -[NSRemoteViewControllerAuxiliary invokeCachedConnectionHandlerForController:withError:]
+ GCC_except_table127
+ GCC_except_table130
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FenceGroupMemberProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FenceGroupMemberProtocol
+ __OBJC_LABEL_PROTOCOL_$_FenceGroupMemberProtocol
+ __OBJC_PROTOCOL_$_FenceGroupMemberProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_FenceGroupMemberProtocol
+ _objc_msgSend$viewIfLoaded
+ _vbuSafelyConcretizedColorWithAppearance
- GCC_except_table111
- _OUTLINED_FUNCTION_58
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FenceGroupMember
- __OBJC_$_PROTOCOL_METHOD_TYPES_FenceGroupMember
- __OBJC_LABEL_PROTOCOL_$_FenceGroupMember
- __OBJC_PROTOCOL_$_FenceGroupMember
- __OBJC_PROTOCOL_REFERENCE_$_FenceGroupMember
CStrings:
+ "%@ removed containing %@ KVO observers %@ and %@"
+ "-[NSRemoteViewControllerAuxiliary invokeCachedConnectionHandlerForController:withError:]"
+ "WARNING: %@ unable to create parent token for %@ (element temporarily unsafe to vend?)"
+ "WARNING: %@ unable to create remote accessibility token for %@ (element temporarily unsafe to vend?)"
+ "WARNING: %@ unable to create token for %@ (element temporarily unsafe to vend?)"
+ "WARNING: %@ unable to obtain remote token for %@ (element temporarily unsafe to vend?); proceeding without a host accessibility parent token"
+ "_connectionHandler"
+ "vbuSafelyConcretizedColorWithAppearance"
- "%@ removed containing %@ observers %@, %@, and %@"
- "%@ unable to create parent token for %@"
- "%@ unable to create remote accessibility token for %@"
- "%@ unable to create token for %@"
- "%@ unable to obtain remote token for %@"
- "-[NSRemoteView _accessibilityParentToken:]"
- "-[NSRendezvousPopoverController popoverAccessibilityParent]"
- "-[NSRendezvousWindowController tokenForElement:]"
```
