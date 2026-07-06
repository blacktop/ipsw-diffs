## AppleCameraISPExclaveKitServices

> `/System/Library/PrivateFrameworks/AppleCameraISPExclaveKitServices.framework/AppleCameraISPExclaveKitServices`

```diff

-  __TEXT.__text: 0x2fd40
-  __TEXT.__const: 0x2fa
-  __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__oslogstring: 0x42ae
-  __TEXT.__cstring: 0x8566
+  __TEXT.__text: 0x30b60
+  __TEXT.__const: 0x2ea
+  __TEXT.__gcc_except_tab: 0x8c8
+  __TEXT.__oslogstring: 0x431e
+  __TEXT.__cstring: 0x8876
   __TEXT.__swift5_typeref: 0x2e
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__unwind_info: 0x9a8
   __TEXT.__eh_frame: 0x70
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
-  __DATA_CONST.__const: 0x10b8
+  __DATA_CONST.__const: 0x1128
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8

   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH.__data: 0x98
   __DATA.__data: 0x1185d0
   __DATA.__common: 0x98

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1158
-  Symbols:   2637
-  CStrings:  831
+  Functions: 1174
+  Symbols:   2681
+  CStrings:  844
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ __Z35ispExclaveKitCommandChSetGmcResultsP20sExclaveKitIspCmdHdr
+ __Z44ispExclaveKitCommandChFidSessionConfigUpdateP20sExclaveKitIspCmdHdr
+ ____Z35ispExclaveKitCommandChSetGmcResultsP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z44ispExclaveKitCommandChFidSessionConfigUpdateP20sExclaveKitIspCmdHdr_block_invoke
+ _applecamera_attentionawarenessmodule_ekattentionawareness_setgmcresults
+ _applecamera_attentionawarenessmodule_ekattentionawareness_setgmcresults__result_get_success
+ _applecamera_fidflowmodule_ekfidflow_channelfidsessionconfigupdate
+ _tb_message_raw_decode_f64
+ _tb_message_raw_encode_f64
CStrings:
+ "%s:%d - Attention: p %f r %f yaw %f ori %u dist %f w %f h %f x %f y %f\n\n"
+ "%s:%d - [IR-EK] setGmcResults\n"
+ "%s:%d - [IR-EK] setGmcResults Finished\n"
+ "%s:%d - set GMC results\n"
+ "ISP_EXCLAVEKIT_CMD_CH_FID_SESSION_CONFIG_UPDATE"
+ "ISP_EXCLAVEKIT_CMD_CH_SET_GMC_RESULTS"
+ "TB_FATAL: invalid result returned from channelFidSessionConfigUpdate"
+ "TB_FATAL: invalid result returned from channelFidSessionConfigUpdate (%s:%d)\n"
+ "TB_FATAL: invalid result returned from setGmcResults"
+ "TB_FATAL: invalid result returned from setGmcResults (%s:%d)\n"
+ "ispExclaveKitCommandChFidSessionConfigUpdate"
+ "ispExclaveKitCommandChSetGmcResults"
+ "v24@?0{applecamera_fidflowmodule_ekfidflow_channelfidsessionconfigupdate__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q})}8"
+ "v280@?0{applecamera_fidflowmodule_ekfidflow_channelrunfidflow__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_fidflowmodule_fidresult_s={applecamera_fidflowmodule_frameinfo_s=Q{applecamera_fidflowmodule_fidframetype_s=Q}II{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}}{applecamera_fidflowmodule_fidstate_s=BI}{applecamera_fidflowmodule_fidattentioninfo_s={applecamera_fidflowmodule_facerectf_s=ffff}{applecamera_fidflowmodule_headpose_s=fffIf}BB}})}8"
+ "v48@?0{applecamera_attentionawarenessmodule_ekattentionawareness_setgmcresults__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_attentionawarenessmodule_eksetgmcresultsoutput_s=dddB})}8"
- "%s:%d - Attention: p %f r %f yaw %f ori %u w %f h %f x %f y %f\n\n"
- "v280@?0{applecamera_fidflowmodule_ekfidflow_channelrunfidflow__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_fidflowmodule_fidresult_s={applecamera_fidflowmodule_frameinfo_s=Q{applecamera_fidflowmodule_fidframetype_s=Q}II{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}{applecamera_fidflowmodule_bufferdescriptor_s=QQQ{applecamera_fidflowmodule_bufferformatdescriptor_s=IIII{applecamera_fidflowmodule_elementformat_s=Q}{applecamera_fidflowmodule_channellayout_s=Q}I}}}{applecamera_fidflowmodule_fidstate_s=BI}{applecamera_fidflowmodule_fidattentioninfo_s={applecamera_fidflowmodule_facerectf_s=ffff}{applecamera_fidflowmodule_headpose_s=fffI}BB}})}8"

```
