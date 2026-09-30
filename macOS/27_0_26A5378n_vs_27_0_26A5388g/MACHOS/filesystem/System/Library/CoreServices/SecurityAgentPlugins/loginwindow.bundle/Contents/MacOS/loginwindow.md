## loginwindow

> `/System/Library/CoreServices/SecurityAgentPlugins/loginwindow.bundle/Contents/MacOS/loginwindow`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-395.0.0.0.0
-  __TEXT.__text: 0x26d90
+396.0.0.0.0
+  __TEXT.__text: 0x272ac
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x6180
-  __TEXT.__objc_methlist: 0x216c
+  __TEXT.__objc_stubs: 0x6200
+  __TEXT.__objc_methlist: 0x218c
   __TEXT.__const: 0x6c
   __TEXT.__gcc_except_tab: 0x4ac
-  __TEXT.__cstring: 0x5bb0
+  __TEXT.__cstring: 0x5c6e
   __TEXT.__oslogstring: 0x119
-  __TEXT.__objc_methname: 0x5ef7
+  __TEXT.__objc_methname: 0x5fa5
   __TEXT.__objc_classname: 0x294
   __TEXT.__objc_methtype: 0x1224
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8f0
-  __DATA_CONST.__const: 0xa88
-  __DATA_CONST.__cfstring: 0x5000
+  __TEXT.__unwind_info: 0x8f8
+  __DATA_CONST.__const: 0xa98
+  __DATA_CONST.__cfstring: 0x50a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x650
   __DATA_CONST.__got: 0x3c8
-  __DATA.__objc_const: 0x1fa0
-  __DATA.__objc_selrefs: 0x1f50
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_const: 0x1fc0
+  __DATA.__objc_selrefs: 0x1f70
+  __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x4e8
   __DATA.__crash_info: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 764
+  Functions: 769
   Symbols:   466
-  CStrings:  2029
+  CStrings:  2040
 
CStrings:
+ "PSSO re-present after failure for user %@: %@"
+ "PSSO re-present check: isShowingCustomUI=%d pssoUser=%@(psso=%d)"
+ "Reporting auth error to PSSO custom UI: %@"
+ "_activatePSSOForUser:withErrorMessage:"
+ "_pssoSubmittedUserName"
+ "a"
+ "activation failed"
+ "authErrorOccurred:params:"
+ "reportAuthError:toProvider:"
+ "representPlatformSSOForUser:afterFailureWithErrorMessage:"
+ "showing custom UI"
```
