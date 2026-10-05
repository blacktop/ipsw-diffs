## biomesyncd

> `/usr/libexec/biomesyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-256.0.1.0.0
-  __TEXT.__text: 0x4b260
+258.0.0.0.0
+  __TEXT.__text: 0x4b218
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_stubs: 0x8bc0
-  __TEXT.__objc_methlist: 0x3d04
+  __TEXT.__objc_methlist: 0x3cf4
   __TEXT.__const: 0x1352
   __TEXT.__gcc_except_tab: 0x900
-  __TEXT.__objc_methname: 0xa7b1
-  __TEXT.__cstring: 0x5aa2
+  __TEXT.__objc_methname: 0xa7b2
+  __TEXT.__cstring: 0x5a7b
   __TEXT.__objc_classname: 0x7f2
-  __TEXT.__objc_methtype: 0x1760
-  __TEXT.__oslogstring: 0x6b00
-  __TEXT.__unwind_info: 0x1710
+  __TEXT.__objc_methtype: 0x1759
+  __TEXT.__oslogstring: 0x6ad4
+  __TEXT.__unwind_info: 0x1708
   __DATA_CONST.__const: 0x1148
-  __DATA_CONST.__cfstring: 0x47a0
+  __DATA_CONST.__cfstring: 0x4760
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__got: 0x450
   __DATA.__objc_const: 0x7708
   __DATA.__objc_selrefs: 0x2990
   __DATA.__objc_ivar: 0x3ec

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1656
-  Symbols:   357
-  CStrings:  3122
+  Functions: 1653
+  Symbols:   358
+  CStrings:  3120
 
Symbols:
+ _OBJC_CLASS_$_BMComputeSourceChangeReporter
CStrings:
+ "@\"<BMViewEventReporter>\""
+ "BMXPCSyncChangeReporter: stream %@ remote %@: failed to notify of changes: %@"
+ "BMXPCSyncChangeReporter: stream %@ remote %@: failed to notify of user deletions: %@"
+ "_eventReporter"
+ "streamDeletionWithStreamIdentifier:remoteName:error:"
+ "streamUpdatedWithStreamIdentifier:remoteName:error:"
- "%@:remotes:%@"
- "@\"<BMGDXPCCoordinationService>\""
- "BMCoordinationXPCSyncEventReporter: stream %@: failed to notify coordination service of changes: %@"
- "BMCoordinationXPCSyncEventReporter: stream %@: failed to notify coordination service of user deletions: %@"
- "GDXPCCoordinationService"
- "_coordinationService"
- "streamRemoteIdentifierForStreamName:deviceIdentifier:"
- "streamUpdatedWithStreamName:isDelete:error:"
```
