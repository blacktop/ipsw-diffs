## remotectl

> `/usr/libexec/remotectl`

```diff

-172.100.5.0.0
-  __TEXT.__text: 0x19de0
-  __TEXT.__auth_stubs: 0x1a30
+172.100.9.0.0
+  __TEXT.__text: 0x1a214
+  __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x7be

   __TEXT.__objc_methtype: 0xad
   __TEXT.__unwind_info: 0x518
   __TEXT.__eh_frame: 0x73c
-  __DATA_CONST.__auth_got: 0xd28
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x218
   __DATA_CONST.__const: 0x6e0

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 366
-  Symbols:   570
+  Symbols:   571
   CStrings:  441
 
Symbols:
+ _objc_retain_x23
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer

```
