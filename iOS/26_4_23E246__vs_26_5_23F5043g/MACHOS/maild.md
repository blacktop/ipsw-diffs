## maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

-3864.500.181.2.2
-  __TEXT.__text: 0xdc2ac
+3864.600.1.2.3
+  __TEXT.__text: 0xdc3c0
   __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_stubs: 0x16440
   __TEXT.__objc_methlist: 0xb44c
-  __TEXT.__gcc_except_tab: 0x1b130
+  __TEXT.__gcc_except_tab: 0x1b160
   __TEXT.__objc_methname: 0x1ce37
   __TEXT.__cstring: 0x8cad
   __TEXT.__objc_classname: 0x1ba7
   __TEXT.__objc_methtype: 0x4007
   __TEXT.__const: 0x8da
-  __TEXT.__oslogstring: 0x958e
+  __TEXT.__oslogstring: 0x968e
   __TEXT.__dlopen_cstrs: 0x288
   __TEXT.__ustring: 0x72
   __TEXT.__swift5_typeref: 0x335

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E172FD0E-A91B-31AB-A247-1DD8C70BA531
+  UUID: 5E4DDA82-A664-3E74-A05E-68A349C85763
   Functions: 4432
   Symbols:   1169
-  CStrings:  8399
+  CStrings:  8402
 
Functions:
~ sub_10005f294 : 3568 -> 3844
CStrings:
+ "Delivery returned Retry but retryCount exhausted, treating as transient error"
+ "Delivery returned Retry with %lu bytes sent, deleting outbox copy for re-queue"
+ "Delivery returned Retry with 0 bytes sent, treating as transient error to preserve outbox copy"

```
