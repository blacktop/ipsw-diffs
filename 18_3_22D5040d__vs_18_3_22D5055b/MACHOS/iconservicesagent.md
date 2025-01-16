## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

-644.10.0.0.0
-  __TEXT.__text: 0x31c4
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x48
-  __TEXT.__oslogstring: 0x50f
-  __TEXT.__cstring: 0x1a4
+644.11.0.0.0
+  __TEXT.__text: 0x36e0
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x1b8
+  __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0x635
+  __TEXT.__cstring: 0x1f1
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__objc_methname: 0xc47
+  __TEXT.__objc_methname: 0xceb
   __TEXT.__objc_classname: 0x8a
-  __TEXT.__objc_methtype: 0x334
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_methtype: 0x34c
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x8d0
-  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_selrefs: 0x3c8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 64
-  Symbols:   116
-  CStrings:  270
+  Functions: 66
+  Symbols:   125
+  CStrings:  285
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_LSBundleRecord
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_retain_x4
CStrings:
+ "B60@0:8{?=[8I]}16i48@52"
+ "Client %d requesting it's own icon. Allowing"
+ "Client is disallowed from making such an icon request"
+ "Client is not properly entitled or asking for an non-allowable icon"
+ "Failed to get record from token for client %d. Error: %@"
+ "ISBundleIdentifierIcon"
+ "Rejecting cache configuration request from %d. Disallowed!"
+ "Rejecting generation request from %d for %@ with %@. Disallowed!"
+ "_isRequestValidForToken:clientPID:icon:"
+ "auditToken"
+ "bundleIdentifier"
+ "bundleRecordForAuditToken:error:"
+ "compare:"
+ "defaultWorkspace"
+ "mayProcessWithAuditTokenMapDatabase:"

```
