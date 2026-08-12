## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-2000.100.2.2.1
-  __TEXT.__text: 0x1b56ac
+2003.100.1.0.0
+  __TEXT.__text: 0x1b586c
   __TEXT.__objc_methlist: 0xdc3c
   __TEXT.__const: 0x5fe8
-  __TEXT.__oslogstring: 0x1b6f4
+  __TEXT.__oslogstring: 0x1b774
   __TEXT.__cstring: 0x11b36
-  __TEXT.__gcc_except_tab: 0x3da4
+  __TEXT.__gcc_except_tab: 0x3de0
   __TEXT.__ustring: 0xac
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__swift5_typeref: 0x1c5c

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d40
+  __DATA_CONST.__objc_selrefs: 0x6d48
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__got: 0x1ac8

   - /usr/lib/swift/libswiftos.dylib
   Functions: 9466
   Symbols:   1874
-  CStrings:  3878
+  CStrings:  3879
 
Functions:
~ sub_198a3d194 -> sub_197cb9194 : 1260 -> 1296
~ sub_198a65cd8 -> sub_197ce1cfc : 1704 -> 1736
~ sub_198a67f34 -> sub_197ce3f78 : 1476 -> 1512
~ sub_198a68f70 -> sub_197ce4fd8 : 836 -> 876
~ sub_198a69330 -> sub_197ce53c0 : 812 -> 840
~ sub_198b2dc50 -> sub_197da9cfc : 2220 -> 2496
CStrings:
+ "INCOMING-CLIENT_DATA:%@ SERVICE:%@ TRACE_ID:%@"
+ "INCOMING-CLIENT_MESSAGE:%@ SERVICE:%@ TRACE_ID:%@"
+ "INCOMING-CLIENT_PENDING:%@ SERVICE:%@ TRACE_ID:%@"
+ "INCOMING-CLIENT_PROTOBUF:%@ SERVICE:%@ TRACE_ID:%@"
+ "INCOMING-CLIENT_RESOURCE_PENDING:%@ SERVICE:%@ TRACE_ID:%@"
+ "[sm:%@] Completed {errorCode: %ld, account: %@}"
+ "[sm:%@] Registered but missing our aliases %@ - adding and re-registering"
- "INCOMING-CLIENT_DATA:%@ SERVICE:%@"
- "INCOMING-CLIENT_MESSAGE:%@ SERVICE:%@"
- "INCOMING-CLIENT_PENDING:%@ SERVICE:%@"
- "INCOMING-CLIENT_PROTOBUF:%@ SERVICE:%@"
- "INCOMING-CLIENT_RESOURCE_PENDING:%@ SERVICE:%@"
- "[sm:%@] Completed {errorCode: %llu, account: %@}"
```
