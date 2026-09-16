## com.apple.PrintKit.PrinterTool

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-327.0.0.0.0
-  __TEXT.__text: 0x5a850
+327.1.0.0.0
+  __TEXT.__text: 0x5a918
   __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_stubs: 0x6800
-  __TEXT.__objc_methlist: 0x2e48
+  __TEXT.__objc_stubs: 0x6840
+  __TEXT.__objc_methlist: 0x2e78
   __TEXT.__const: 0xa30
-  __TEXT.__gcc_except_tab: 0xaa10
+  __TEXT.__gcc_except_tab: 0xaa34
   __TEXT.__oslogstring: 0x4322
-  __TEXT.__cstring: 0x94be
-  __TEXT.__objc_methname: 0x6a4a
+  __TEXT.__cstring: 0x94ec
+  __TEXT.__objc_methname: 0x6ae1
   __TEXT.__objc_classname: 0x4c6
   __TEXT.__objc_methtype: 0x2043
   __TEXT.__ustring: 0x66
   __TEXT.__unwind_info: 0x2fb0
-  __DATA_CONST.__const: 0xed60
-  __DATA_CONST.__cfstring: 0xeca0
+  __DATA_CONST.__const: 0xed68
+  __DATA_CONST.__cfstring: 0xece0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__auth_got: 0xc58
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x57f8
-  __DATA.__objc_selrefs: 0x1e08
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_const: 0x5858
+  __DATA.__objc_selrefs: 0x1e28
+  __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x3180
   __DATA.__common: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1629
+  Functions: 1634
   Symbols:   941
-  CStrings:  4131
+  CStrings:  4141
 
Symbols:
+ __Z16PKPromptAuthInfoP8NSStringS0_bb
+ __Z16PKPromptAuthInfoP8NSStringS0_bbU13block_pointerFvP15NSURLCredentialE
- __Z16PKPromptAuthInfoP8NSStringS0_b
- __Z16PKPromptAuthInfoP8NSStringS0_bU13block_pointerFvP15NSURLCredentialE
CStrings:
+ "PK_LEVEL_AUTHENTICATION_CHECKACCESS"
+ "Password"
+ "T@\"NSString\",&,V_msgWhence"
+ "T@?,C,V_credentialCallback"
+ "User Name"
+ "User name placeholder text"
+ "_credentialCallback"
+ "_msgWhence"
+ "credentialCallback"
+ "msgWhence"
+ "setCredentialCallback:"
+ "setMsgWhence:"
- "Username placeholder text"
- "user name"
```
