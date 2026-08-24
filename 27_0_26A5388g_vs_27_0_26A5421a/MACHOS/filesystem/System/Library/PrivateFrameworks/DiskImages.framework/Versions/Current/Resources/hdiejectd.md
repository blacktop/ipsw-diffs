## hdiejectd

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/Current/Resources/hdiejectd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__data`

```diff

-701.0.0.0.0
-  __TEXT.__text: 0x3f08
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__cstring: 0x95c
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__objc_methname: 0x9eb
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methtype: 0x384
-  __TEXT.__unwind_info: 0x1a0
+704.0.0.0.0
+  __TEXT.__text: 0x41ec
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x3d4
+  __TEXT.__cstring: 0x99f
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__objc_methname: 0xa58
+  __TEXT.__objc_classname: 0x7a
+  __TEXT.__objc_methtype: 0x3c0
+  __TEXT.__oslogstring: 0xaf
+  __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x6e0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0xe8
-  __DATA.__objc_const: 0x568
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_ivar: 0x50
-  __DATA.__objc_data: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0xf8
+  __DATA.__objc_const: 0x640
+  __DATA.__objc_selrefs: 0x3b8
+  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
-  __DATA.__common: 0x20
+  __DATA.__common: 0x28
   __DATA.__bss: 0x19
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 93
-  Symbols:   141
-  CStrings:  278
+  Functions: 97
+  Symbols:   148
+  CStrings:  294
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSXPCConnection
+ __os_log_error_impl
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _os_log_create
+ _os_log_type_enabled
CStrings:
+ "@\"NSXPCListenerEndpoint\""
+ "@56@0:8@16{?=[8I]}24"
+ "DIBrokeredEndpoint"
+ "auditToken"
+ "boolValue"
+ "com.apple.diskimages"
+ "com.apple.private.diskimages.helper"
+ "currentConnection"
+ "endpoint"
+ "hdiejectd"
+ "initWithEndpoint:ownerToken:"
+ "ownerToken"
+ "refusing endpoint overwrite for uuid %{public}@ from a different process than the one that registered it"
+ "refusing sendEndpointForUUID for uuid %{public}@, missing entitlement"
+ "valueForEntitlement:"
+ "{?=\"val\"[8I]}"
```
