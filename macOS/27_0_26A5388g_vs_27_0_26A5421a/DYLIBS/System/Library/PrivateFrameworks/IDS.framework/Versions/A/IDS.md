## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS`

```diff

-2000.100.2.1.1
-  __TEXT.__text: 0x1c5984
+2003.100.1.0.0
+  __TEXT.__text: 0x1c5b60
   __TEXT.__objc_methlist: 0xdbcc
   __TEXT.__const: 0x5fd8
-  __TEXT.__oslogstring: 0x1b504
+  __TEXT.__oslogstring: 0x1b584
   __TEXT.__cstring: 0x10b06
-  __TEXT.__gcc_except_tab: 0x3dcc
+  __TEXT.__gcc_except_tab: 0x3e04
   __TEXT.__ustring: 0xac
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__swift5_typeref: 0x1c5c

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ce0
+  __DATA_CONST.__objc_selrefs: 0x6ce8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__got: 0x1ab0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 9480
   Symbols:   1785
-  CStrings:  3807
+  CStrings:  3808
 
Functions:
~ sub_196fb3c60 -> sub_19675dc60 : 1856 -> 1892
~ sub_196fb4c54 -> sub_19675ec78 : 1388 -> 1432
~ sub_196fb6974 -> sub_1967609c4 : 1564 -> 1592
~ sub_196fb7af0 -> sub_196761b5c : 920 -> 964
~ sub_196fb7f0c -> sub_196761fa4 : 908 -> 940
~ sub_1970aa508 -> sub_1968545c0 : 2316 -> 2608
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
