## AFKUser

> `/System/Library/PrivateFrameworks/AFKUser.framework/Versions/A/AFKUser`

```diff

-743.0.5.0.1
-  __TEXT.__text: 0x6ec4
+743.40.4.0.0
+  __TEXT.__text: 0x718c
   __TEXT.__objc_methlist: 0x3f0
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x92c
-  __TEXT.__oslogstring: 0x8cc
-  __TEXT.__cstring: 0x25d
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__gcc_except_tab: 0x910
+  __TEXT.__oslogstring: 0x998
+  __TEXT.__cstring: 0x27c
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x268
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x88
-  __AUTH_CONST.__const: 0x200
+  __DATA_CONST.__got: 0x98
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x790
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__objc_ivar: 0x7c
-  __DATA.__data: 0x10
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__data: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 176
-  Symbols:   402
-  CStrings:  86
+  Symbols:   399
+  CStrings:  89
 
Symbols:
+ AFKUserRegistryFromSerializedServices
+ _AFKUserRegistryFromSerializedServices
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ ___block_descriptor_40_e8_32s_e46_v32?0"AFKEndpointInterface"8"NSString"1624l
+ ___copy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$setEventHandler:
- _CFRelease
- _IOCFUnserializeWithSize
- ___33-[AFKUserSystemService registry:]_block_invoke_2
- ___33-[AFKUserSystemService registry:]_block_invoke_3
- ___block_descriptor_48_e8_32r40r_e15_v32?08Q16^B24l
- ___block_descriptor_48_e8_32s40r_e15_v32?08Q16^B24l
- ___block_descriptor_48_e8_32s40s_e15_v32?08Q16^B24l
- ___copy_helper_block_e8_32r40r
- ___destroy_helper_block_e8_32r40r
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$setObject:atIndexedSubscript:
CStrings:
+ "0x%llx: IOCFUnserializeBinary failed"
+ "0x%llx: Timeout waiting for endpoint cancellation"
+ "0x%llx: registry capture held no AFKRootService"
+ "0x%llx: registry service children is a %{public}@, expected an array"
+ "0x%llx: registry service unserialized as %{public}@, expected a dictionary"
+ "v32@?0@\"AFKEndpointInterface\"8@\"NSString\"16@24"
- "0x%llx: IOCFUnserializeBinary failed:%@"
- "0x%llx: IOCFUnserializeWithSize:%@"
- "v32@?0@8Q16^B24"
```
