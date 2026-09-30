## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.500.181.2.2
-  __TEXT.__text: 0xd9334
+3864.600.1.2.3
+  __TEXT.__text: 0xd947c
   __TEXT.__auth_stubs: 0x14d0
   __TEXT.__objc_methlist: 0xcda4
-  __TEXT.__gcc_except_tab: 0x1b7bc
+  __TEXT.__gcc_except_tab: 0x1b7f8
   __TEXT.__const: 0x1240
-  __TEXT.__cstring: 0xb76c
+  __TEXT.__cstring: 0xb7bc
   __TEXT.__oslogstring: 0x6313
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154

   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xa78
   __AUTH_CONST.__const: 0x18c8
-  __AUTH_CONST.__cfstring: 0x9fa0
+  __AUTH_CONST.__cfstring: 0x9fe0
   __AUTH_CONST.__objc_const: 0x16bb0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F86F075B-336B-36D2-9362-3E32D5CCBAF7
+  UUID: 86E0BE13-5CE1-34DB-8645-3667E824C020
   Functions: 4861
   Symbols:   18110
-  CStrings:  8600
+  CStrings:  8604
 
Symbols:
+ ___26-[EMThread displayMessage]_block_invoke.203
- ___26-[EMThread displayMessage]_block_invoke.196
Functions:
~ -[EMThread initWithObjectID:originatingQuery:builder:] : 288 -> 372
~ -[EMThread _commonInitWithOriginatingQuery:builder:] : 184 -> 428
CStrings:
+ "EMThread must be created with an EMThreadObjectID, not %@"

```
