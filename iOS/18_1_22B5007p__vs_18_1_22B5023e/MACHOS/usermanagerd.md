## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-414.0.0.0.0
-  __TEXT.__text: 0xace44
-  __TEXT.__auth_stubs: 0x1850
+415.0.0.0.0
+  __TEXT.__text: 0xaccec
+  __TEXT.__auth_stubs: 0x1820
   __TEXT.__objc_stubs: 0x2220
   __TEXT.__objc_methlist: 0x1064
   __TEXT.__const: 0x10e4
-  __TEXT.__gcc_except_tab: 0xe40
+  __TEXT.__gcc_except_tab: 0xe08
   __TEXT.__cstring: 0x66fe
   __TEXT.__objc_classname: 0x39a
   __TEXT.__objc_methname: 0x346d
   __TEXT.__objc_methtype: 0x12c2
-  __TEXT.__oslogstring: 0x10770
-  __TEXT.__unwind_info: 0x12c0
-  __DATA_CONST.__auth_got: 0xc38
+  __TEXT.__oslogstring: 0x107da
+  __TEXT.__unwind_info: 0x12b8
+  __DATA_CONST.__auth_got: 0xc20
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x2660

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1530
-  Symbols:   458
+  Functions: 1528
+  Symbols:   455
   CStrings:  3182
 
Symbols:
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ "Calling _SecKeychainDeleteMultiUser, not waiting for completion.."
+ "_SecKeychainDeleteMultiUser Completed: Failed to delete persona keychain items: %!{(MISSING)public}@"
+ "_SecKeychainDeleteMultiUser Completion: Deleted keychain items for persona %!{(MISSING)public}@"
- "Calling _SecKeychainDeleteMultiUser..."
- "Deleted keychain items for persona %!{(MISSING)public}@"
- "Failed to delete persona keychain items: %!{(MISSING)public}@"

```
