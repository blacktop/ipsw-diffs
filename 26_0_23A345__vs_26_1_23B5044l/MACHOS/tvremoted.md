## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.0.17.0.0
-  __TEXT.__text: 0xfe00
+548.10.16.0.0
+  __TEXT.__text: 0x10184
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0xef0
+  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0xf00
   __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x243a
-  __TEXT.__cstring: 0x830
+  __TEXT.__oslogstring: 0x24a1
+  __TEXT.__cstring: 0x83e
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x31cc
+  __TEXT.__objc_methname: 0x31f1
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xe81
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x638
-  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0xc60
+  __DATA.__objc_selrefs: 0xc70
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 77F4190D-8D04-3169-A564-6B3B294E18A2
-  Functions: 311
-  Symbols:   2349
-  CStrings:  935
+  UUID: 7CFE1D1D-ABD0-3AF4-84DC-14F6EDAEA29C
+  Functions: 313
+  Symbols:   2360
+  CStrings:  943
 
Symbols:
+ -[TVRDServer _interestedClientProcessConnectionsForDevice:].cold.1
+ -[TVRDServer countedSetDescriptionFor:]
+ GCC_except_table93
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.90
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.90.cold.1
+ _objc_msgSend$allObjects
+ _objc_msgSend$countedSetDescriptionFor:
- GCC_except_table92
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.84
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.84.cold.1
CStrings:
+ "%p"
+ "'%@' = %ld"
+ "Before updating identifiers: %{public}@"
+ "Updated Identifiers: %{public}@"
+ "Updating device's name from: %{public}@ to: %{public}@"
+ "allObjects"
+ "countedSetDescriptionFor:"
- "Clearing cached devices"

```
