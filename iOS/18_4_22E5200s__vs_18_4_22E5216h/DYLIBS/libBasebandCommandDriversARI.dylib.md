## libBasebandCommandDriversARI.dylib

> `/usr/lib/libBasebandCommandDriversARI.dylib`

```diff

-1245.0.0.0.0
-  __TEXT.__text: 0x9dad8
-  __TEXT.__auth_stubs: 0x2eb0
+1248.0.0.0.0
+  __TEXT.__text: 0xa0fe0
+  __TEXT.__auth_stubs: 0x2fd0
   __TEXT.__init_offsets: 0x10
-  __TEXT.__const: 0x8198
-  __TEXT.__cstring: 0x2df0
-  __TEXT.__gcc_except_tab: 0xddac
-  __TEXT.__oslogstring: 0x1ef8
-  __TEXT.__unwind_info: 0x3c30
-  __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x10a0
+  __TEXT.__const: 0x83b8
+  __TEXT.__cstring: 0x2e84
+  __TEXT.__gcc_except_tab: 0xe490
+  __TEXT.__oslogstring: 0x1f85
+  __TEXT.__unwind_info: 0x3d50
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x10d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1760
-  __AUTH_CONST.__const: 0x6c88
+  __AUTH_CONST.__auth_got: 0x17f0
+  __AUTH_CONST.__const: 0x6ea0
   __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x1f0
   __DATA.__bss: 0x20

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2169
-  Symbols:   3540
-  CStrings:  715
+  Functions: 2205
+  Symbols:   3602
+  CStrings:  724
 
Symbols:
+ __ZN12capabilities5radio7initiumEv
+ __ZN3abm18kBasebandVendorIntE
+ __ZN3abm23kBasebandWakeSubTypeACPE
+ __ZN4util8to_lowerERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN5radio13CommandDriver19kKeyBasebandBoardIdE
+ __ZN5radio13CommandDriver19kKeyBasebandUidModeE
+ __ZN5radio13CommandDriver24kKeyBasebandSecurityModeE
+ __ZN5radio13CommandDriver26kKeyBasebandProductionModeE
+ __ZN5radio13CommandDriver26kKeyBasebandSecurityDomainE
+ __ZN6AriSdk29ARI_IBIGetRFFEScanDataReq_SDKC1Ev
+ __ZN6AriSdk29ARI_IBIGetRFFEScanDataReq_SDKD1Ev
+ __ZN6AriSdk31ARI_IBIGetRFFEScanDataRspCb_SDK6unpackEv
+ __ZN6AriSdk31ARI_IBIGetRFFEScanDataRspCb_SDKC1EPKhj
+ __ZN6AriSdk31ARI_IBIGetRFFEScanDataRspCb_SDKD1Ev
+ __ZN6AriSdk39ARI_GetPersonalizationParametersReq_SDKC1Ev
+ __ZN6AriSdk39ARI_GetPersonalizationParametersReq_SDKD1Ev
+ __ZN6AriSdk41ARI_GetPersonalizationParametersRspCb_SDK6unpackEv
+ __ZN6AriSdk41ARI_GetPersonalizationParametersRspCb_SDKC1EPKhj
+ __ZN6AriSdk41ARI_GetPersonalizationParametersRspCb_SDKD1Ev
+ __ZN6AriSdk42ARI_CsiIceSecSendRFSelfTestTicketV2Req_SDKC1Ev
+ __ZN6AriSdk42ARI_CsiIceSecSendRFSelfTestTicketV2Req_SDKD1Ev
+ __ZN6AriSdk44ARI_CsiIceSecSendRFSelfTestTicketV2RspCb_SDK6unpackEv
+ __ZN6AriSdk44ARI_CsiIceSecSendRFSelfTestTicketV2RspCb_SDKC1EPKhj
+ __ZN6AriSdk44ARI_CsiIceSecSendRFSelfTestTicketV2RspCb_SDKD1Ev
+ __ZNK3xpc6object9to_stringEv
+ ___tolower
CStrings:
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "ACP"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1248"
+ "Failed on getting RFFE Scan Data: could not unpack"
+ "Failed on getting RFFE Scan Data: wrong data size"
+ "Failed to get Pers Params (%s) but proceeding to get SCRT Pub Key anyway"
+ "Failed to get RFFE Scan Data"
+ "Failed to get pers params"
+ "Int"
+ "No callback for getting RFFE scan data"
+ "get RFFE Scan Data"
+ "send Getting Pers Params"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "AppleBasebandManager-AppleBasebandServices_Manager-1245"
- "Unsupported cmd: getPersParams"

```
