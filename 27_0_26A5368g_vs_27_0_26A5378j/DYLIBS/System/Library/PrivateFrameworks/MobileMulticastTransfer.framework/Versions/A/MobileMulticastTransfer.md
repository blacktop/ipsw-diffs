## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/Versions/A/MobileMulticastTransfer`

```diff

-  __TEXT.__text: 0x3a9f8
-  __TEXT.__objc_methlist: 0x1868
+  __TEXT.__text: 0x3aa90
+  __TEXT.__objc_methlist: 0x1860
   __TEXT.__const: 0x4940
-  __TEXT.__cstring: 0x1093
-  __TEXT.__oslogstring: 0x5107
+  __TEXT.__cstring: 0x10b7
+  __TEXT.__oslogstring: 0x510f
   __TEXT.__gcc_except_tab: 0x6d8
-  __TEXT.__unwind_info: 0xeb8
+  __TEXT.__unwind_info: 0xeb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf88
+  __DATA_CONST.__objc_selrefs: 0xf90
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__got: 0x258
   __AUTH_CONST.__const: 0x3a80
   __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x5038
+  __AUTH_CONST.__objc_const: 0x5018
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x570
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x2c0
+  __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x28
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1629
-  Symbols:   3690
+  Functions: 1631
+  Symbols:   3692
   CStrings:  661
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[MIBUNWServerController _fetchOneBatchOfPacketsWithDelay:]
+ _OBJC_CLASS_$_CUOPACK
+ __45-[MIBUNANSubscriber sendData:withCompletion:]_block_invoke
+ ___59-[MIBUNWServerController _fetchOneBatchOfPacketsWithDelay:]_block_invoke
+ ___59-[MIBUNWServerController _fetchOneBatchOfPacketsWithDelay:]_block_invoke_2
+ _objc_msgSend$_fetchOneBatchOfPacketsWithDelay:
+ _objc_msgSend$decodeData:flags:error:
+ _objc_msgSend$encodeObject:flags:error:
- -[MIBUNWClientController stopMulticast]
- -[MIBUNWServerController _fetchOneBatchOfPacketsFromProvider]
- OBJC_IVAR_$_MIBUNWClientController._multicastSocketSem
- __39-[MIBUNWClientController stopMulticast]_block_invoke
- __39-[MIBUNWClientController stopMulticast]_block_invoke_2
- ___39-[MIBUNWClientController stopMulticast]_block_invoke
- ___39-[MIBUNWClientController stopMulticast]_block_invoke_2
- ___61-[MIBUNWServerController _fetchOneBatchOfPacketsFromProvider]_block_invoke
- ___61-[MIBUNWServerController _fetchOneBatchOfPacketsFromProvider]_block_invoke_2
- _objc_msgSend$_fetchOneBatchOfPacketsFromProvider
- _objc_msgSend$stopMulticast
CStrings:
+ "%{public}@: Ignoring packet reception completion (state=%lu)"
+ "%{public}@: Invalid size of NAN multicast session data: %ld"
+ "%{public}@: failed to encode payload via OPACK: %{public}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fYeGzF/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
+ "Failed to decode multicast data via NSKeyedUnarchiver: %{public}@"
+ "Failed to decode multicast data via OPACK: %{public}@"
+ "Invalid size of NAN multicast session data: %ld"
+ "NAN publisher received multicast data which decodes to: %{public}@"
+ "Reached EOF of packet provider!"
- "%{public}@: Ignoring extra packet reception completion"
- "%{public}@: Multicast semaphore signaled, stopMulticast complete"
- "%{public}@: Signaling multicast socket semaphore"
- "%{public}@: Waiting on multicast semaphore..."
- "%{public}@: stopMulticast called, waiting for multicast to stop..."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.No5F2G/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
- "EOF Reached"
- "NAN publisher received multicast data blob which decodes to: %@"
- "Reached EOF of packet provider! We are done!"

```
