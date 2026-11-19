## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/Versions/A/MessageSecurity`

```diff

-341.0.17.0.0
-  __TEXT.__text: 0x4f5f4
+341.40.12.0.0
+  __TEXT.__text: 0x50404
   __TEXT.__objc_methlist: 0x2434
-  __TEXT.__const: 0x1494
+  __TEXT.__const: 0x14a4
   __TEXT.__gcc_except_tab: 0x780
   __TEXT.__cstring: 0x4457
-  __TEXT.__oslogstring: 0xebc
+  __TEXT.__oslogstring: 0x100c
   __TEXT.__swift5_typeref: 0x2b0
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x3f0

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x120
   __DATA.__objc_ivar: 0x234
-  __DATA.__data: 0x1228
+  __DATA.__data: 0xfb8
   __DATA.__bss: 0x8e0
   __DATA.__common: 0x2711
-  __DATA_DIRTY.__objc_data: 0xb88
-  __DATA_DIRTY.__data: 0xa8
+  __DATA_DIRTY.__objc_data: 0xca8
+  __DATA_DIRTY.__data: 0x320
   __DATA_DIRTY.__bss: 0x30
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   Functions: 2249
   Symbols:   3836
-  CStrings:  608
+  CStrings:  613
 
CStrings:
+ "Invalid AES-GCM nonce length %ld, expected 12 to 16 octets"
+ "Invalid AES-GCM tag length %ld, RFC 5084 requires 12 to 16 octets"
+ "Invalid data - AES-GCM algorithm identifier carries no parameters"
+ "Invalid data - aes-ICVlen is negative or too large"
+ "aes-ICVlen %ld does not match mac length %ld"
```
