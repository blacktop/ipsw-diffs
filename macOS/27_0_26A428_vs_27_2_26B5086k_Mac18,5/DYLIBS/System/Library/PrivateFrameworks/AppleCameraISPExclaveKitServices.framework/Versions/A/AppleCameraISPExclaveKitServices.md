## AppleCameraISPExclaveKitServices

> `/System/Library/PrivateFrameworks/AppleCameraISPExclaveKitServices.framework/Versions/A/AppleCameraISPExclaveKitServices`

```diff

-20.70.0.0.0
-  __TEXT.__text: 0x2f980
+20.104.2.0.0
+  __TEXT.__text: 0x315bc
   __TEXT.__const: 0x2f2
-  __TEXT.__gcc_except_tab: 0x8c8
-  __TEXT.__oslogstring: 0x421d
-  __TEXT.__cstring: 0x87fc
+  __TEXT.__gcc_except_tab: 0x928
+  __TEXT.__oslogstring: 0x42f2
+  __TEXT.__cstring: 0x8c80
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1230
+  __TEXT.__unwind_info: 0x1298
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
-  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__const: 0xe30
   __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x438
   __AUTH.__data: 0x98
-  __DATA.__data: 0x118bb2
+  __DATA.__data: 0x118bb4
   __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1162
-  Symbols:   947
-  CStrings:  799
+  Functions: 1183
+  Symbols:   964
+  CStrings:  815
 
Symbols:
+ _OUTLINED_FUNCTION_26
+ _Z34ispExclaveKitCommandChInitScanModeP20sExclaveKitIspCmdHdr
+ _Z37ispExclaveKitCommandChGetGmcAnalyticsP20sExclaveKitIspCmdHdr
+ __Z34ispExclaveKitCommandChInitScanModeP20sExclaveKitIspCmdHdr
+ __Z37ispExclaveKitCommandChGetGmcAnalyticsP20sExclaveKitIspCmdHdr
+ ___ZL16decodeAnstResultI26sExclaveKitIspCmdChRunAnstEbP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sPT__block_invoke
+ ___ZL16decodeAnstResultI38sExclaveKitIspCmdChRunAnst__DeprecatedEbP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sPT__block_invoke
+ ___ZL30_ispExclaveKitCommandChRunAnstI26sExclaveKitIspCmdChRunAnstE27eIspExclaveKitCmdHandlerErrPT__block_invoke
+ ___ZL30_ispExclaveKitCommandChRunAnstI38sExclaveKitIspCmdChRunAnst__DeprecatedE27eIspExclaveKitCmdHandlerErrPT__block_invoke
+ ____Z34ispExclaveKitCommandChInitScanModeP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z37ispExclaveKitCommandChGetGmcAnalyticsP20sExclaveKitIspCmdHdr_block_invoke
+ ____ZL16decodeAnstResultI26sExclaveKitIspCmdChRunAnstEbP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sPT__block_invoke
+ ____ZL16decodeAnstResultI38sExclaveKitIspCmdChRunAnst__DeprecatedEbP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sPT__block_invoke
+ ____ZL30_ispExclaveKitCommandChRunAnstI26sExclaveKitIspCmdChRunAnstE27eIspExclaveKitCmdHandlerErrPT__block_invoke
+ ____ZL30_ispExclaveKitCommandChRunAnstI38sExclaveKitIspCmdChRunAnst__DeprecatedE27eIspExclaveKitCmdHandlerErrPT__block_invoke
+ _applecamera_attentionawarenessmodule_ekattentionawareness_getgmcanalytics
+ _applecamera_attentionawarenessmodule_ekattentionawareness_getgmcanalytics__result_get_success
+ _applecamera_attentionawarenessmodule_ekattentionawareness_initscanmode
+ _applecamera_attentionawarenessmodule_ekattentionawareness_initscanmode__result_get_success
+ _applecamera_attentionawarenessmodule_ekgmcanalyticsoutput__decode
+ applecamera_attentionawarenessmodule_ekattentionawareness_getgmcanalytics
+ applecamera_attentionawarenessmodule_ekattentionawareness_initscanmode
- _OUTLINED_FUNCTION_25
- ___Z29ispExclaveKitCommandChRunAnstP20sExclaveKitIspCmdHdr_block_invoke
- ___ZL16decodeAnstResultP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sP26sExclaveKitIspCmdChRunAnst_block_invoke
- ____Z29ispExclaveKitCommandChRunAnstP20sExclaveKitIspCmdHdr_block_invoke
- ____ZL16decodeAnstResultP61applecamera_anstmodule_ispexclavecorechrunkitanstresultv150_sP26sExclaveKitIspCmdChRunAnst_block_invoke
CStrings:
+ "%s:%d - [IR-EK] PCEMgr Finished (gmcRunResult=%u)\n"
+ "%s:%d - [IR-EK] getGmcAnalytics\n"
+ "%s:%d - [IR-EK] getGmcAnalytics Finished\n"
+ "%s:%d - [IR-EK] initScanMode\n"
+ "%s:%d - [IR-EK] initScanMode Finished\n"
+ "%s:%d - get GMC analytics\n"
+ "%s:%d - init scan mode\n"
+ "ISP_EXCLAVEKIT_CMD_CH_GET_GMC_ANALYTICS"
+ "ISP_EXCLAVEKIT_CMD_CH_INIT_SCAN_MODE"
+ "TB_FATAL: invalid result returned from getGmcAnalytics"
+ "TB_FATAL: invalid result returned from getGmcAnalytics (%s:%d)\n"
+ "TB_FATAL: invalid result returned from initScanMode"
+ "TB_FATAL: invalid result returned from initScanMode (%s:%d)\n"
+ "_ispExclaveKitCommandChRunAnst"
+ "ispExclaveKitCommandChGetGmcAnalytics"
+ "ispExclaveKitCommandChInitScanMode"
+ "v248@?0{applecamera_attentionawarenessmodule_ekattentionawareness_getgmcanalytics__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_attentionawarenessmodule_ekgmcanalyticsoutput_s=BQ{applecamera_attentionawarenessmodule_gmccontrollerstatus_s=Q}QdQdddddBddddQBddddBdddddd})}8"
+ "v24@?0Q8r^{applecamera_anstmodule_anstfacev1502_s=II{applecamera_anstmodule_anstcategory2_s=Q}{applecamera_anstmodule_anstrect2_s=ffff}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}BfB{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}{applecamera_anstmodule_anstconfidence_s=Q}}16"
+ "v24@?0{applecamera_attentionawarenessmodule_ekattentionawareness_channelrunpce__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}I)}8"
+ "v24@?0{applecamera_attentionawarenessmodule_ekattentionawareness_initscanmode__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_attentionawarenessmodule_ekinitscanmodeoutput_s=B})}8"
- "%s:%d - [IR-EK] PCEMgr Finished\n"
- "ispExclaveKitCommandChRunAnst"
- "v24@?0Q8r^{applecamera_anstmodule_anstfacev1502_s=II{applecamera_anstmodule_anstcategory2_s=Q}{applecamera_anstmodule_anstrect2_s=ffff}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}{applecamera_anstmodule_anstfaceposedegree_s=Q(?={?=I})}BfB{applecamera_anstmodule_anstconfidence_s=Q}}16"
- "v24@?0{applecamera_attentionawarenessmodule_ekattentionawareness_channelrunpce__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}B)}8"
```
