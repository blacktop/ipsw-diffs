## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-904.40.2.0.0
-  __TEXT.__text: 0x5ae5c
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x6940
+904.60.1.0.1
+  __TEXT.__text: 0x5b114
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_stubs: 0x69e0
   __TEXT.__objc_methlist: 0x2ffc
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x2934
-  __TEXT.__cstring: 0x4977
-  __TEXT.__objc_methname: 0x7e26
-  __TEXT.__oslogstring: 0xae60
+  __TEXT.__cstring: 0x4992
+  __TEXT.__objc_methname: 0x7e6c
+  __TEXT.__oslogstring: 0xaea6
   __TEXT.__objc_classname: 0x407
   __TEXT.__objc_methtype: 0xe8c
   __TEXT.__unwind_info: 0xfd0

   __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x320
-  __DATA_CONST.__auth_got: 0x7a0
-  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__got: 0x270
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4a68
-  __DATA.__objc_selrefs: 0x1f10
+  __DATA.__objc_selrefs: 0x1f38
   __DATA.__objc_ivar: 0x39c
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1241
-  Symbols:   2988
-  CStrings:  3172
+  Functions: 1242
+  Symbols:   2997
+  CStrings:  3180
 
Symbols:
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table247
+ _SANDBOX_CHECK_NO_REPORT
+ _connectionIsPublic
+ _objc_msgSend$auditToken
+ _objc_msgSend$coarsenDiskSpace
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$protocol
+ _objc_msgSend$reduceToTotals
+ _protocol_isEqual
+ _sandbox_check_by_audit_token
- GCC_except_table145
- GCC_except_table148
- GCC_except_table159
- GCC_except_table246
Functions:
~ -[CacheDelete clientUnifiedPurgeableSpace:queryType:replyBlock:] : 1468 -> 2040
+ _connectionIsPublic
CStrings:
+ "Unknown query type! cannot determine the required entitlement"
+ "[%@] clientUnifiedPurgeableSpace queryType: %d, public: %d, info: %@"
+ "auditToken"
+ "coarsenDiskSpace"
+ "exportedInterface"
+ "protocol"
+ "reduceToTotals"
+ "sandbox_check_by_audit_token(%s) failed for %@: %{public}s"
+ "system-info"
+ "vfs.disk-space"
- "Unknown query type! can not determine the required entitelment"
- "[%@] clientUnifiedPurgeableSpace queryType: %d, info: %@"
```
