## clocksyncd

> `/usr/libexec/clocksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1501.7.0.0.0
-  __TEXT.__text: 0x3d3dc
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_stubs: 0x5a40
+1510.7.0.0.0
+  __TEXT.__text: 0x3dd30
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_stubs: 0x5a80
   __TEXT.__objc_methlist: 0x36b4
   __TEXT.__const: 0x139
-  __TEXT.__cstring: 0x2a97
-  __TEXT.__oslogstring: 0x5ad5
+  __TEXT.__cstring: 0x2c6e
+  __TEXT.__oslogstring: 0x5c92
   __TEXT.__gcc_except_tab: 0x1ac4
-  __TEXT.__objc_methname: 0x91d0
+  __TEXT.__objc_methname: 0x91f3
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
-  __TEXT.__unwind_info: 0x1660
+  __TEXT.__unwind_info: 0x1688
   __DATA_CONST.__const: 0xaa0
-  __DATA_CONST.__cfstring: 0x1f60
+  __DATA_CONST.__cfstring: 0x1f80
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x608
+  __DATA_CONST.__auth_got: 0x610
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1db0
+  __DATA.__objc_selrefs: 0x1dc0
   __DATA.__objc_ivar: 0x514
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1569
-  Symbols:   262
-  CStrings:  2477
+  Functions: 1579
+  Symbols:   263
+  CStrings:  2495
 
Symbols:
+ _strcmp
CStrings:
+ "%@: %s: Refusing a nil UUID\n"
+ "%@: %s: Refusing preferred UUID %@, already registered to %@\n"
+ "%@: Refusing to serialize a malformed trigger timing\n"
+ "%s: Caller pid %d lacks %s, denying mock sync entity request\n"
+ "%s: Failed to deinitialize default MSG device handle. Error: 0x%x\n"
+ "%s: No active XPC connection, denying mock sync entity request\n"
+ "%s: Refusing %lu trigger timings, limit is %lu\n"
+ "%s: Refusing trigger timing encoded as '%s', require '%s'\n"
+ "-[TSDMSGService init]"
+ "-[TSDSyncEntityManager createMockSSAMEntityWithTriggerTiming:machTime:persist:preferredUUID:reply:]"
+ "-[TSDSyncEntityManager createMockSSAMEntityWithTriggerTiming:machTime:persist:preferredUUID:reply:]_block_invoke"
+ "-[TSDSyncEntityManager getSyncEntityForUUID:withReply:]"
+ "-[TSDSyncEntityManager removeAllMockSSAMEntriesWithReply:]"
+ "-[TSDSyncEntityManager removeMockSSAMEntityWithUUID:reply:]"
+ "1510.7"
+ "TSFixed64_64FromValue"
+ "com.apple.private.timesync.mock-entity"
+ "getValue:size:"
+ "objCType"
+ "valueForEntitlement:"
- "1501.7"
- "getValue:"
```
