## libBasebandCommandDriversARI.dylib

> `/usr/lib/libBasebandCommandDriversARI.dylib`

```diff

-1218.0.0.0.0
-  __TEXT.__text: 0xa2f44
-  __TEXT.__auth_stubs: 0x2e50
-  __TEXT.__init_offsets: 0x10
-  __TEXT.__cstring: 0x2ddf
-  __TEXT.__gcc_except_tab: 0xde4c
-  __TEXT.__const: 0x80f8
-  __TEXT.__oslogstring: 0x1ea4
-  __TEXT.__unwind_info: 0x39d8
+1219.0.0.0.0
+  __TEXT.__text: 0xa395c
+  __TEXT.__auth_stubs: 0x2e90
+  __TEXT.__init_offsets: 0xc
+  __TEXT.__cstring: 0x2ddd
+  __TEXT.__gcc_except_tab: 0xde98
+  __TEXT.__const: 0x8198
+  __TEXT.__oslogstring: 0x1ef8
+  __TEXT.__unwind_info: 0x3a38
   __DATA_CONST.__got: 0x678
   __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1730
-  __AUTH_CONST.__const: 0x6bd8
+  __AUTH_CONST.__auth_got: 0x1750
+  __AUTH_CONST.__const: 0x6cc8
   __AUTH_CONST.__cfstring: 0xa0
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x1a0
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2126
-  Symbols:   3434
-  CStrings:  711
+  Functions: 2140
+  Symbols:   3449
+  CStrings:  714
 
Symbols:
+ __ZN6AriSdk35ARI_FactoryGetNvItemsSettingReq_SDKC1Ev
+ __ZN6AriSdk35ARI_FactoryGetNvItemsSettingReq_SDKD1Ev
+ __ZN6AriSdk37ARI_FactoryGetNvItemsSettingRspCb_SDK6unpackEv
+ __ZN6AriSdk37ARI_FactoryGetNvItemsSettingRspCb_SDKC1EPKhj
+ __ZN6AriSdk37ARI_FactoryGetNvItemsSettingRspCb_SDKD1Ev
+ __ZN7antenna13CommandDriver8toStringENS_7NVItemsE
+ __ZN7antenna16ARICommandDriver10getNVItemsEN8dispatch8callbackIU13block_pointerFvbNS_7NVItemsEEEE
+ __ZN7antenna16ARICommandDriver14convertNVItemsE15FACTORY_NV_ITEM
- _CFBooleanGetTypeID
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyBasebandWatchdogStop
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
- __ZN3ctu2cf6assignERbPK11__CFBoolean
CStrings:
+ "#I Getting NV Items: %s"
+ "/AppleInternal/Library/BuildRoots/7d2a62ca-bb83-11ef-9317-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1219"
+ "Failed to get NV items"
+ "Failed to unpack result for NV items"
+ "Getting NV items"
- "/AppleInternal/Library/BuildRoots/602d817d-b298-11ef-8387-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "AppleBasebandManager-AppleBasebandServices_Manager-1218"
- "Watchdog timed out"

```
