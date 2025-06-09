## SiriPowerInstrumentation

> `/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation`

```diff

-3300.3.1.0.0
-  __TEXT.__text: 0x3f2c
+3500.3.1.0.0
+  __TEXT.__text: 0x420c
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0xf44
+  __TEXT.__objc_methlist: 0xf64
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x908
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x300
   __TEXT.__objc_classname: 0x866
-  __TEXT.__objc_methname: 0xb94
+  __TEXT.__objc_methname: 0xc27
   __TEXT.__objc_methtype: 0x2bb
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x398
+  __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x120

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E820E127-7681-3BEE-9F6F-3B7D02A248B8
-  Functions: 220
-  Symbols:   971
-  CStrings:  423
+  UUID: 4FD93C65-20F2-3AD8-83EA-7B99298DEBE4
+  Functions: 222
+  Symbols:   980
+  CStrings:  432
 
Symbols:
+ +[SPIPowerLogger _staticWrappedInitWithCurrentProcess]
+ +[SPIPowerLogger _staticWrappedInitWithProcessIdentifier:]
+ __OBJC_$_CLASS_METHODS_SPIPowerLogger
+ _objc_msgSend$_setError
+ _objc_msgSend$data
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithCurrentProcess
+ _objc_msgSend$length
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
Functions:
~ _POWSchemaProvisionalPOWClientEventReadFrom : 552 -> 596
~ _POWSchemaProvisionalPOWUsageReadFrom : 768 -> 980
~ _POWSchemaProvisionalPOWProcessUsageReadFrom : 968 -> 1328
+ +[SPIPowerLogger _staticWrappedInitWithProcessIdentifier:]
+ +[SPIPowerLogger _staticWrappedInitWithCurrentProcess]
CStrings:
+ "_setError"
+ "_staticWrappedInitWithCurrentProcess"
+ "_staticWrappedInitWithProcessIdentifier:"
+ "data"
+ "getBytes:range:"
+ "hasError"
+ "length"
+ "position"
+ "setPosition:"

```
