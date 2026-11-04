## libKTLDynamic.dylib

> `/usr/lib/libKTLDynamic.dylib`

```diff

-1594.0.0.0.0
-  __TEXT.__text: 0x2620c
+1596.0.0.0.0
+  __TEXT.__text: 0x262e4
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x1a18
-  __TEXT.__cstring: 0x37b0
+  __TEXT.__cstring: 0x380e
   __TEXT.__oslogstring: 0x41
   __TEXT.__unwind_info: 0xcd8
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 440
   Symbols:   944
-  CStrings:  437
+  CStrings:  439
 
Functions:
~ __ZN3ktl16KTLReceivePacket24fetchARIMsgFromTransportEP10KTLOptions : 1228 -> 1272
~ __ZL22sFetchMessageRemainderP10KTLOptionsPN3ktl16KTLReceivePacketEj : 464 -> 552
~ __ZN3ktl16KTLReceivePacket6appendEjPh : 76 -> 160
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "Cannot append bytes. offset (%ld) + bufSize (%u) + appendSize (%u) > storageSize (%u)\n"
+ "append"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
```
