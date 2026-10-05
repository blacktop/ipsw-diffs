## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

```diff

-341.40.8.0.0
-  __TEXT.__text: 0x4b4b8
+341.40.12.0.0
+  __TEXT.__text: 0x4c17c
   __TEXT.__objc_methlist: 0x2434
-  __TEXT.__const: 0x14a4
+  __TEXT.__const: 0x14b4
   __TEXT.__gcc_except_tab: 0x78c
   __TEXT.__cstring: 0x4447
-  __TEXT.__oslogstring: 0xebc
+  __TEXT.__oslogstring: 0x100c
   __TEXT.__swift5_typeref: 0x2b0
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x3f0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 2221
   Symbols:   3377
-  CStrings:  608
+  CStrings:  613
 
CStrings:
+ "Invalid AES-GCM nonce length %ld, expected 12 to 16 octets"
+ "Invalid AES-GCM tag length %ld, RFC 5084 requires 12 to 16 octets"
+ "Invalid data - AES-GCM algorithm identifier carries no parameters"
+ "Invalid data - aes-ICVlen is negative or too large"
+ "aes-ICVlen %ld does not match mac length %ld"
```
