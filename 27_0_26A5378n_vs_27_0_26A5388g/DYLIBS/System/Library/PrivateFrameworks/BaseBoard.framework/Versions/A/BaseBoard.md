## BaseBoard

> `/System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard`

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
-  __TEXT.__text: 0xa9d4c
-  __TEXT.__objc_methlist: 0x70a4
+827.0.0.0.0
+  __TEXT.__text: 0xaa1f8
+  __TEXT.__objc_methlist: 0x712c
   __TEXT.__const: 0x310
   __TEXT.__dlopen_cstrs: 0x9f
-  __TEXT.__gcc_except_tab: 0x10fd4
-  __TEXT.__cstring: 0x8f12
+  __TEXT.__gcc_except_tab: 0x110ac
+  __TEXT.__cstring: 0x8ecd
   __TEXT.__oslogstring: 0x2f22
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x5160
+  __TEXT.__unwind_info: 0x5198
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x668
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31f8
+  __DATA_CONST.__objc_selrefs: 0x3238
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__got: 0x868
   __AUTH_CONST.__const: 0x25c0
-  __AUTH_CONST.__cfstring: 0x8ca0
-  __AUTH_CONST.__objc_const: 0xd530
+  __AUTH_CONST.__cfstring: 0x8d00
+  __AUTH_CONST.__objc_const: 0xd6c8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xfa0
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
-  __DATA_DIRTY.__bss: 0x4a8
+  __DATA_DIRTY.__bss: 0x4b0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3076
-  Symbols:   6882
-  CStrings:  1583
+  Functions: 3085
+  Symbols:   6913
+  CStrings:  1586
 
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
+ OBJC_IVAR_$_BSActionInactivation._callStack
+ OBJC_IVAR_$_BSActionInactivation._reason
+ OBJC_IVAR_$_BSActionUsageViolation._message
+ OBJC_IVAR_$_BSActionUsageViolation._priorInactivation
+ OBJC_IVAR_$__BSActionResponder._lock_inactivation
+ _OBJC_CLASS_$_BSActionInactivation
+ _OBJC_CLASS_$_BSActionUsageViolation
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
- OBJC_IVAR_$__BSActionResponder._lock_action_encoded
- OBJC_IVAR_$__BSActionResponder._lock_action_sent
- OBJC_IVAR_$__BSActionResponder._lock_inactivationCallStack
CStrings:
+ "%@\nprevious inactivation was at %@"
+ "%@ : action=%@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NOMWGB/Sources/BaseBoard/BaseBoard/BSCompoundAssertion.m"
+ "BSActionUsageViolation.m"
+ "cannot -encode from an inactive instance"
+ "cannot -sendResponse: from an inactive instance"
+ "cannot -sendResponse: if no response was expected"
+ "cannot -setNullificationHandler: on an inactive instance"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.i6Eqrf/Sources/BaseBoard/BaseBoard/BSCompoundAssertion.m"
- "cannot -encode from an inactive instance : action=%@\nprevious inactivation was at %@"
- "cannot -sendResponse: from an inactive instance : action=%@\nprevious inactivation was at %@"
- "cannot -sendResponse: if no response was expected : action=%@"
- "cannot -setNullificationHandler: on an inactive instance : action=%@\nprevious inactivation was at %@"
```
