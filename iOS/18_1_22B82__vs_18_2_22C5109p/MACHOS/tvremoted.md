## tvremoted

> `/usr/libexec/tvremoted`

```diff

-443.10.21.0.0
-  __TEXT.__text: 0xe7a4
+496.20.14.0.0
+  __TEXT.__text: 0xea70
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x22a0
-  __TEXT.__objc_methlist: 0x96c
+  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0x988
   __TEXT.__const: 0xca
-  __TEXT.__oslogstring: 0x1ec0
+  __TEXT.__oslogstring: 0x1ef7
   __TEXT.__cstring: 0x822
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x2ec7
+  __TEXT.__objc_methname: 0x2f6f
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xdc1
-  __TEXT.__unwind_info: 0x310
+  __TEXT.__unwind_info: 0x318
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x6a0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x16f8
-  __DATA.__objc_selrefs: 0xb28
+  __DATA.__objc_const: 0x1738
+  __DATA.__objc_selrefs: 0xb38
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 281
-  Symbols:   2202
-  CStrings:  840
+  Functions: 284
+  Symbols:   2218
+  CStrings:  844
 
Symbols:
+ -[TVRDClientProcessConnection addItemForDeviceWithIdentifier:mediaIdentifier:completion:]
+ -[TVRDServer clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:]
+ GCC_except_table73
+ GCC_except_table85
+ _TVRCAirplayIDKey
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.77
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.77.cold.1
+ ___89-[TVRDServer clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:]_block_invoke
+ _objc_msgSend$addItemWithMediaIdentifier:completion:
+ _objc_msgSend$clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:
- GCC_except_table71
- GCC_except_table83
- _TVRCMediaRemoteIDKey
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.75
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.75.cold.1
- _objc_msgSend$_impl
CStrings:
+ "Adding %!@(MISSING) to UpNext %!{(MISSING)public}@"
+ "Deallocating TVRDServer"
+ "addItemForDeviceWithIdentifier:mediaIdentifier:completion:"
+ "addItemWithMediaIdentifier:completion:"
+ "clientConnection:addItemForDeviceWithIdentifier:mediaIdentifier:completion:"
- "_impl"

```
