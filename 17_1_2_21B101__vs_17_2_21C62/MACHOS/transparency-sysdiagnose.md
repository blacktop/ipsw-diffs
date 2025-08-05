## transparency-sysdiagnose

> `/usr/libexec/transparency-sysdiagnose`

```diff

-948.0.0.0.1
-  __TEXT.__text: 0xc58
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x420
+1033.62.3.0.0
+  __TEXT.__text: 0x1208
+  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__objc_stubs: 0x560
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x19b
-  __TEXT.__objc_methname: 0x265
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x2a0
+  __TEXT.__cstring: 0x206
+  __TEXT.__oslogstring: 0x69
+  __TEXT.__objc_methname: 0x302
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x108
-  __DATA.__objc_classrefs: 0x58
+  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0634105-B0C0-3849-A6A8-ACD373BE233A
-  Functions: 8
-  Symbols:   62
-  CStrings:  83
+  UUID: 22A628A6-F683-3A08-92F2-797D6BCA62D6
+  Functions: 12
+  Symbols:   67
+  CStrings:  110
 
Symbols:
+ _OBJC_CLASS_$_KTIDStaticKeyStore
+ _OBJC_CLASS_$_TransparencyAnalytics
+ __NSConcreteGlobalBlock
+ ___kCFBooleanTrue
+ __os_log_impl
+ _dispatch_once
+ _objc_release_x1
+ _objc_retain_x28
+ _os_log_create
+ _os_log_type_enabled
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "KTIDStaticKeyStore findByIdentifier: %@: %@"
+ "KTIDStaticKeyStore listKTID: %@"
+ "com.apple.Transparency"
+ "contactExternalURI"
+ "contactIdentifier"
+ "count"
+ "default"
+ "failed"
+ "findByIdentifier:error:"
+ "hasInternalDiagnostics"
+ "listKTID:"
+ "mappings"
+ "not KTIDStaticKeyStore store"
+ "numberWithBool:"
+ "publicAccountIdentity"
+ "static_key_peers"
+ "valid"

```
