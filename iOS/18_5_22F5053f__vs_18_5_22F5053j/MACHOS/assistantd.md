## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3405.27.1.1.1
-  __TEXT.__text: 0x36d964
+3405.29.4.0.0
+  __TEXT.__text: 0x36dd54
   __TEXT.__auth_stubs: 0x34c0
-  __TEXT.__objc_stubs: 0x455a0
-  __TEXT.__objc_methlist: 0x22560
+  __TEXT.__objc_stubs: 0x455e0
+  __TEXT.__objc_methlist: 0x22578
   __TEXT.__const: 0x10990
   __TEXT.__dlopen_cstrs: 0xafa
   __TEXT.__gcc_except_tab: 0x4888
-  __TEXT.__cstring: 0x519be
-  __TEXT.__oslogstring: 0x3f9ab
+  __TEXT.__cstring: 0x51a9c
+  __TEXT.__oslogstring: 0x3fab0
   __TEXT.__objc_classname: 0x51a6
-  __TEXT.__objc_methname: 0x5d38c
-  __TEXT.__objc_methtype: 0xf1e2
+  __TEXT.__objc_methname: 0x5d3cd
+  __TEXT.__objc_methtype: 0xf1fd
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa390
+  __TEXT.__unwind_info: 0xa3a0
   __TEXT.__eh_frame: 0xe58
   __DATA_CONST.__auth_got: 0x1a70
-  __DATA_CONST.__got: 0x3b20
+  __DATA_CONST.__got: 0x3b28
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x14c88
-  __DATA_CONST.__cfstring: 0x12b40
+  __DATA_CONST.__cfstring: 0x12b80
   __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6e8

   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33770
-  __DATA.__objc_selrefs: 0x148b8
+  __DATA.__objc_const: 0x33778
+  __DATA.__objc_selrefs: 0x148c8
   __DATA.__objc_ivar: 0x2594
   __DATA.__objc_data: 0x82f0
   __DATA.__data: 0x60f8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14330
-  Symbols:   2890
-  CStrings:  27189
+  Functions: 14333
+  Symbols:   2891
+  CStrings:  27201
 
Symbols:
+ _AFSiriLogContextMyriad
CStrings:
+ "%s %p Failure sending endWaitingForEmergency to client %{public}@"
+ "%s Ending waiting for emergency after receiing Domain Signal ACE command with domain %@"
+ "%s Ending waiting for emergency after receiing SiriKit Plugin Signal ACE command with bundle identifier %@"
+ "-[ADClientConnection didReceiveDomainSignal:]"
+ "-[ADClientConnection didReceiveSiriKitPluginSignal:]"
+ "-[ADClientConnection endWaitingForEmergency]_block_invoke"
+ "20"
+ "ADClientConnection.m"
+ "MobileAssistantDaemons-3405.29.4"
+ "com.apple.siri.audio.AudioFlowDelegatePlugin"
+ "endWaitingForEmergency"
+ "endWaitingForEmergencyIfNeededForCommand:"
+ "v24@0:8@\"<SAAceCommand>\"16"
- "MobileAssistantDaemons-3405.27.1.1.1"

```
