## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1656.120.5.0.0
-  __TEXT.__text: 0x36728
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x37e8
+1656.120.6.0.0
+  __TEXT.__text: 0x36430
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x37b8
   __TEXT.__const: 0x2d4
   __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0x19e6
+  __TEXT.__cstring: 0x19a0
   __TEXT.__dlopen_cstrs: 0x1cd
   __TEXT.__oslogstring: 0x2748
   __TEXT.__swift5_typeref: 0x6e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12e0
+  __TEXT.__unwind_info: 0x12d8
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa42
-  __TEXT.__objc_methname: 0x6f26
-  __TEXT.__objc_methtype: 0x1d73
-  __TEXT.__objc_stubs: 0x49e0
-  __DATA_CONST.__got: 0x500
+  __TEXT.__objc_classname: 0xa2f
+  __TEXT.__objc_methname: 0x6f47
+  __TEXT.__objc_methtype: 0x1d33
+  __TEXT.__objc_stubs: 0x49c0
+  __DATA_CONST.__got: 0x508
   __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd0
+  __DATA_CONST.__objc_selrefs: 0x1bd8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x19c0
-  __AUTH_CONST.__objc_const: 0x8988
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x88f8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0xbe8
   __DATA.__bss: 0x420
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1471
-  Symbols:   5283
-  CStrings:  2077
+  Functions: 1468
+  Symbols:   5270
+  CStrings:  2073
 
Symbols:
+ -[LAContext optionPushButtonUseMaxPreArmAge]
+ -[LAContext setOptionPushButtonUseMaxPreArmAge:]
+ _OBJC_CLASS_$_LACAccessControl
- +[LASecAccessControl allowAllACL]
- +[LASecAccessControl constraintsFromACL:]
- +[LASecAccessControl denyAllACL]
- +[LASecAccessControl deserializeACL:]
- +[LASecAccessControl serializeACL:]
- _CFDictionaryCreateCopy
- _OBJC_CLASS_$_LASecAccessControl
- _OBJC_METACLASS_$_LASecAccessControl
- __OBJC_$_CLASS_METHODS_LASecAccessControl
- __OBJC_CLASS_RO_$_LASecAccessControl
- __OBJC_METACLASS_RO_$_LASecAccessControl
- _objc_exception_throw
- _objc_msgSend$exceptionWithName:reason:userInfo:
CStrings:
+ "optionPushButtonUseMaxPreArmAge"
+ "setOptionPushButtonUseMaxPreArmAge:"
- "@24@0:8^{__SecAccessControl=}16"
- "Could not initialize trivial ACL (%@)"
- "Could note deserialize ACL (%@)"
- "LASecAccessControl"
- "^{__SecAccessControl=}24@0:8@16"
- "exceptionWithName:reason:userInfo:"

```
