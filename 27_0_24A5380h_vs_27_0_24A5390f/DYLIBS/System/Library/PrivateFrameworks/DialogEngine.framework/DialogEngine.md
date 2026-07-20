## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`

```diff

-3600.23.4.0.0
+3600.23.6.0.0
   __TEXT.__text: 0x46036c
   __TEXT.__init_offsets: 0x28
   __TEXT.__objc_methlist: 0x3394

   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xf40
-  __AUTH.__objc_data: 0x1900
+  __AUTH.__objc_data: 0x18b0
   __AUTH.__data: 0x940
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x3b8
-  __DATA.__data: 0x52c
+  __DATA.__data: 0x4ec
   __DATA.__common: 0x1399
-  __DATA.__bss: 0x2de8
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x1800
+  __DATA.__bss: 0x2d98
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x1840
   __DATA_DIRTY.__common: 0x29b8
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
Functions:
~ __ZN4siri12dialogengine18GetFallbackLocalesERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 3936 -> 3940
~ __ZN6google8protobuf2io18StringOutputStreamD0Ev : 28 -> 24
CStrings:
+ "3600.23.6"
+ "CAT Request (Dialog Engine 3600.23.6)"
- "3600.23.4"
- "CAT Request (Dialog Engine 3600.23.4)"
```
