## EmbeddedDataReset

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset`

```diff

-49.3.1.0.0
-  __TEXT.__text: 0x2250
+54.0.0.0.0
+  __TEXT.__text: 0x2378
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x42c
+  __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x24b
+  __TEXT.__cstring: 0x26f
   __TEXT.__gcc_except_tab: 0x16c
   __TEXT.__oslogstring: 0x48c
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0xa02
-  __TEXT.__objc_methtype: 0x27c
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_methname: 0xadc
+  __TEXT.__objc_methtype: 0x286
+  __TEXT.__objc_stubs: 0x720
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f0
+  __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0x7d0
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__objc_const: 0x830
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A5A3A4D-23F5-323C-9AAA-DD8108F3BC7A
-  Functions: 63
-  Symbols:   352
-  CStrings:  236
+  UUID: A6DA6E33-2427-3793-9BDA-55929FC1C07C
+  Functions: 67
+  Symbols:   366
+  CStrings:  250
 
Symbols:
+ -[DDRResetOptions bootstrapToken]
+ -[DDRResetOptions revertToSnapshotName]
+ -[DDRResetOptions setBootstrapToken:]
+ -[DDRResetOptions setRevertToSnapshotName:]
+ _OBJC_CLASS_$_NSData
+ _OBJC_IVAR_$_DDRResetOptions._bootstrapToken
+ _OBJC_IVAR_$_DDRResetOptions._revertToSnapshotName
+ _objc_msgSend$bootstrapToken
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$revertToSnapshotName
CStrings:
+ "@\"NSData\""
+ "T@\"NSData\",&,N,V_bootstrapToken"
+ "T@\"NSString\",&,N,V_revertToSnapshotName"
+ "_bootstrapToken"
+ "_revertToSnapshotName"
+ "bootstrapToken"
+ "decodeObjectOfClass:forKey:"
+ "revertToSnapshotName"
+ "setBootstrapToken:"
+ "setRevertToSnapshotName:"

```
