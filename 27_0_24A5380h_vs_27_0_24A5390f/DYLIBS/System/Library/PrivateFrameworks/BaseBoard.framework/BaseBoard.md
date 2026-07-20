## BaseBoard

> `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-825.0.0.0.0
-  __TEXT.__text: 0xa1788
-  __TEXT.__objc_methlist: 0x70b4
+827.0.0.0.0
+  __TEXT.__text: 0xa1be8
+  __TEXT.__objc_methlist: 0x713c
   __TEXT.__const: 0x308
   __TEXT.__dlopen_cstrs: 0xe8
-  __TEXT.__gcc_except_tab: 0x10f88
-  __TEXT.__cstring: 0x8f53
+  __TEXT.__gcc_except_tab: 0x1105c
+  __TEXT.__cstring: 0x8f0e
   __TEXT.__oslogstring: 0x3053
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x52b0
+  __TEXT.__unwind_info: 0x52e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1cb0
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3200
+  __DATA_CONST.__objc_selrefs: 0x3240
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__got: 0x868
   __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x8cc0
-  __AUTH_CONST.__objc_const: 0xd530
+  __AUTH_CONST.__cfstring: 0x8d20
+  __AUTH_CONST.__objc_const: 0xd6c8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x10a8
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x864
+  __AUTH.__objc_data: 0x1360
+  __DATA.__objc_ivar: 0x86c
   __DATA.__data: 0x1168
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x40
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x4b8
+  __DATA_DIRTY.__bss: 0x4c0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3030
-  Symbols:   6867
-  CStrings:  1591
+  Functions: 3039
+  Symbols:   6898
+  CStrings:  1594
 
Symbols:
+ +[BSActionInactivation createWithCallStack:reason:]
+ +[BSActionUsageViolation createWithMessage:priorInactivation:]
+ -[BSAction abortForUsageViolation:]
+ -[BSActionInactivation .cxx_destruct]
+ -[BSActionInactivation callStack]
+ -[BSActionInactivation reason]
+ -[BSActionUsageViolation .cxx_destruct]
+ -[BSActionUsageViolation abort]
+ -[_BSActionResponder _handleUsageViolation:priorInactivation:action:]
+ _OBJC_CLASS_$_BSActionInactivation
+ _OBJC_CLASS_$_BSActionUsageViolation
+ _OBJC_IVAR_$_BSActionInactivation._callStack
+ _OBJC_IVAR_$_BSActionInactivation._reason
+ _OBJC_IVAR_$_BSActionUsageViolation._message
+ _OBJC_IVAR_$_BSActionUsageViolation._priorInactivation
+ _OBJC_IVAR_$__BSActionResponder._lock_inactivation
+ _OBJC_METACLASS_$_BSActionInactivation
+ _OBJC_METACLASS_$_BSActionUsageViolation
+ __OBJC_$_CLASS_METHODS_BSActionInactivation
+ __OBJC_$_CLASS_METHODS_BSActionUsageViolation
+ __OBJC_$_INSTANCE_METHODS_BSActionInactivation
+ __OBJC_$_INSTANCE_METHODS_BSActionUsageViolation
+ __OBJC_$_INSTANCE_VARIABLES_BSActionInactivation
+ __OBJC_$_INSTANCE_VARIABLES_BSActionUsageViolation
+ __OBJC_$_PROP_LIST_BSActionInactivation
+ __OBJC_CLASS_RO_$_BSActionInactivation
+ __OBJC_CLASS_RO_$_BSActionUsageViolation
+ __OBJC_METACLASS_RO_$_BSActionInactivation
+ __OBJC_METACLASS_RO_$_BSActionUsageViolation
+ _objc_msgSend$abort
+ _objc_msgSend$abortForUsageViolation:
+ _objc_msgSend$callStack
+ _objc_msgSend$createWithCallStack:reason:
+ _objc_msgSend$createWithMessage:priorInactivation:
- _OBJC_IVAR_$__BSActionResponder._lock_action_encoded
- _OBJC_IVAR_$__BSActionResponder._lock_action_sent
- _OBJC_IVAR_$__BSActionResponder._lock_inactivationCallStack
CStrings:
+ "%@\nprevious inactivation was at %@"
+ "%@ : action=%@"
+ "BSActionUsageViolation.m"
+ "cannot -encode from an inactive instance"
+ "cannot -sendResponse: from an inactive instance"
+ "cannot -sendResponse: if no response was expected"
+ "cannot -setNullificationHandler: on an inactive instance"
- "cannot -encode from an inactive instance : action=%@\nprevious inactivation was at %@"
- "cannot -sendResponse: from an inactive instance : action=%@\nprevious inactivation was at %@"
- "cannot -sendResponse: if no response was expected : action=%@"
- "cannot -setNullificationHandler: on an inactive instance : action=%@\nprevious inactivation was at %@"
```
