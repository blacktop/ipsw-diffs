## AdPlatforms

> `/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms`

```diff

-637.1.6.0.0
-  __TEXT.__text: 0x200c
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x1dc
+637.1.7.0.0
+  __TEXT.__text: 0x2134
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__cstring: 0x43c
   __TEXT.__oslogstring: 0x3
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0x524
+  __TEXT.__objc_methname: 0x540
   __TEXT.__objc_methtype: 0x141
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x180
+  __TEXT.__objc_stubs: 0x660
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x198
+  __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x398
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6ED09E6C-E8C1-3AAB-A47F-3B91FC9BAA18
-  Functions: 49
-  Symbols:   269
-  CStrings:  144
+  UUID: 1BC2BC0E-0DF2-39C4-8231-7AB75214FE69
+  Functions: 51
+  Symbols:   287
+  CStrings:  147
 
Symbols:
+ +[ADStatusConditionsImpl sharedRingBufferLock]
+ +[ADStatusConditionsImpl sharedRingBufferLock].cold.1
+ -[ADStatusConditionsImpl resetRateLimitingBuffer]
+ GCC_except_table16
+ GCC_except_table22
+ _OBJC_CLASS_$_NSLock
+ __OBJC_$_CLASS_METHODS_ADStatusConditionsImpl
+ ___46+[ADStatusConditionsImpl sharedRingBufferLock]_block_invoke
+ ___block_literal_global.89
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$lock
+ _objc_msgSend$resetRateLimitingBuffer
+ _objc_msgSend$sharedRingBufferLock
+ _objc_msgSend$unlock
+ _objc_opt_class
+ _objc_release_x9
+ _objc_terminate
+ _sharedRingBufferLock._sharedLock
+ _sharedRingBufferLock.onceToken
- -[ADStatusConditionsImpl initializeRateLimitingBuffer]
- ___61-[ADStatusConditionsImpl isConditionRateLimited:onOperation:]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- _isConditionRateLimited:onOperation:.onceToken
- _objc_msgSend$initializeRateLimitingBuffer
CStrings:
+ "lock"
+ "resetRateLimitingBuffer"
+ "sharedRingBufferLock"
+ "unlock"
- "initializeRateLimitingBuffer"

```
