## PassKitEngagementExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitEngagementExtension.appex/PassKitEngagementExtension`

```diff

-1591.6.7.0.0
-  __TEXT.__text: 0x1d6c
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__objc_methlist: 0x20c
+1619.6.3.0.0
+  __TEXT.__text: 0x1934
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x520
+  __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0xf6
-  __TEXT.__oslogstring: 0xa2
+  __TEXT.__cstring: 0xea
+  __TEXT.__oslogstring: 0xe9
   __TEXT.__objc_classname: 0x5b
-  __TEXT.__objc_methname: 0x4a0
+  __TEXT.__objc_methname: 0x4eb
   __TEXT.__objc_methtype: 0x133
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x220
-  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x128
   __DATA.__bss: 0x18

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78197A5A-919A-3C95-B5FA-1866F36D9C63
-  Functions: 28
+  UUID: D7716942-2082-351E-B527-248A67F9E57E
+  Functions: 21
   Symbols:   77
-  CStrings:  115
+  CStrings:  122
 
Symbols:
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_PKEngagementBatchRequest
+ _OBJC_CLASS_$_PKEngagementRequest
+ _objc_alloc
- _OBJC_CLASS_$_NSMutableArray
- _PKEqualObjects
- _objc_retain_x26
- _objc_retain_x28
- _objc_retain_x3
CStrings:
+ "Unable to parse engagement request due to error %{public}@:\n%{public}@"
+ "Unknown error"
+ "Unrecognized property"
+ "code"
+ "domain"
+ "handleBatchPayload:completion:"
+ "initWithDictionary:error:"
+ "initWithDictionary:errorsByRequestID:error:"
+ "initWithObjectsAndKeys:"
+ "message"
+ "numberWithInteger:"
+ "objectForKey:"
+ "parameters"
+ "parametersByPropertyName"
+ "performRequest:completion:"
+ "propertiesForSource:"
+ "propertySource"
+ "requests"
+ "safelySetObject:forKey:"
+ "userInfo"
- "PKStringForKey:"
- "addObject:"
- "allKeys"
- "command"
- "commandFromRequest:"
- "fetchFinHealthProperty"
- "fetchProperty"
- "isEqualToString:"
- "noCommandError"
- "noPropertyError"
- "parameter"
- "performBatchRequest:completion:"
- "performFetchFinHealthPropertyRequest:completion:"
- "performFetchPropertyRequest:completion:"
- "unrecognizedCommandError"

```
