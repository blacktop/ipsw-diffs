## libBasebandCommandDriversARI.dylib

> `/usr/lib/libBasebandCommandDriversARI.dylib`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0xa26c0
-  __TEXT.__auth_stubs: 0x2df0
+1211.0.0.0.0
+  __TEXT.__text: 0xa2f44
+  __TEXT.__auth_stubs: 0x2e50
   __TEXT.__init_offsets: 0x10
-  __TEXT.__cstring: 0x2d89
-  __TEXT.__gcc_except_tab: 0xdda4
-  __TEXT.__const: 0x8090
-  __TEXT.__oslogstring: 0x1db3
-  __TEXT.__unwind_info: 0x39c0
+  __TEXT.__cstring: 0x2da5
+  __TEXT.__gcc_except_tab: 0xde4c
+  __TEXT.__const: 0x80f8
+  __TEXT.__oslogstring: 0x1ea4
+  __TEXT.__unwind_info: 0x39d8
   __DATA_CONST.__got: 0x678
   __DATA_CONST.__const: 0x1088
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1700
-  __AUTH_CONST.__const: 0x6b40
+  __AUTH_CONST.__auth_got: 0x1730
+  __AUTH_CONST.__const: 0x6bd8
   __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x1f0
-  __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0x108
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2119
-  Symbols:   3418
-  CStrings:  702
+  Functions: 2126
+  Symbols:   3431
+  CStrings:  708
 
Symbols:
+ __ZN5trace19ARICommandDriverINT16sendFlushRequestEv
+ __ZN6AriSdk21ARI_TraceFlushReq_SDKC1Ev
+ __ZN6AriSdk21ARI_TraceFlushReq_SDKD1Ev
+ __ZN6AriSdk23ARI_TraceFlushRspCb_SDK6unpackEv
+ __ZN6AriSdk23ARI_TraceFlushRspCb_SDKC1EPKhj
+ __ZN6AriSdk23ARI_TraceFlushRspCb_SDKD1Ev
+ _usleep
CStrings:
+ "#I Sending flush request"
+ "#I [rsp] Successfully sent trace flush request"
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1211"
+ "Failed to send trace flush request (response error)"
+ "Sending trace flush request"
+ "[rsp] Failed to send trace flush request (result error: %!d(MISSING) )"
+ "[rsp] Failed to send trace flush request (unpack error)"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "AppleBasebandManager-AppleBasebandServices_Manager-1209"

```
