## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.0.15.0.0
-  __TEXT.__text: 0xfd3c
+548.0.17.0.0
+  __TEXT.__text: 0xfe00
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x2480
   __TEXT.__objc_methlist: 0xef0
   __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x2416
-  __TEXT.__cstring: 0x81b
+  __TEXT.__oslogstring: 0x243a
+  __TEXT.__cstring: 0x830
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__objc_methname: 0x31cc
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xe81
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__unwind_info: 0x340
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x638
-  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 48AD3F38-BA31-30DE-A2FE-94FDD9D578CA
+  UUID: C731D823-A8DD-3211-BFA7-1919FA1EDFEB
   Functions: 311
   Symbols:   2349
-  CStrings:  932
+  CStrings:  935
 
Symbols:
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.84
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.84.cold.1
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.80
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.80.cold.1
Functions:
~ -[TVRDClientProcessConnection updateDeviceIdentifier:to:] : 140 -> 268
~ -[TVRDServer device:disconnectedForReason:error:] : 800 -> 868
CStrings:
+ "%@ - identifiers: %@"
+ "Updating identifier from: %@ to: %@"

```
