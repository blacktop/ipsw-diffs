## InternationalTextSearch

> `/System/Library/PrivateFrameworks/InternationalTextSearch.framework/Versions/A/InternationalTextSearch`

```diff

-1022.0.0.0.0
-  __TEXT.__text: 0x1b0c
+1024.500.21.0.0
+  __TEXT.__text: 0x1adc
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x2eb
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x73
   __TEXT.__objc_stubs: 0xa0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D5AB03B8-B0A3-3BB8-806E-0374C1132245
-  Functions: 52
-  Symbols:   157
+  UUID: EC853736-ABED-3574-81F2-C492026308D2
+  Functions: 54
+  Symbols:   160
   CStrings:  42
 
Symbols:
+ ITSGetCollationContextForDatabaseConnectionHandle.cold.1
+ ITSSetCollationContextForDatabaseConnectionHandle.cold.1
+ ITSTokenListCreate.cold.1
Functions:
~ _ITSCreateCollatorWithPreferredLocale : 344 -> 300
~ _ITSCreateSortKey : 456 -> 464
~ _ITSGetCollationContextForDatabaseConnectionHandle : 132 -> 116
~ _ITSSetCollationContextForDatabaseConnectionHandle : 156 -> 140
~ _ITSTokenListCreate : 156 -> 140
~ _ITSTokenListGetCount : 32 -> 28
+ ITSGetCollationContextForDatabaseConnectionHandle.cold.1
+ ITSTokenListCreate.cold.1

```
